from flask import jsonify, request
from dao.RoleBase import RoleBaseDAO

import os, sys
import jwt

class RoleBase:

    ### Method to split the path ###
    # Parameters : path - requested path
    # Return : Splitted path in one Array
    def splitall(self, path):
        allparts = []
        while 1:
            parts = os.path.split(path)
            if parts[0] == path:  # sentinel for absolute paths
                allparts.insert(0, parts[0])
                break
            elif parts[1] == path:  # sentinel for relative paths
                allparts.insert(0, parts[1])
                break
            else:
                path = parts[0]
                allparts.insert(0, parts[1])
        return allparts

    ### Method to validate the path and credencials ###
    # Parameters : path - requested path
    # Return :  True if the request pass the validation
    #           False of Error if the request don't pass the validation
    def validate(self, path, form):
        try:
            # Home Page - Don't access the sytem #
            if path == '/':
                return True

            #### Validating Path #### - no es necesario, con el try & catch es suficiente
            #vpath = self.validateroute(path)
            #f vpath != True:
            #    return jsonify(Error="Invalid Route"), 400 #Bad Request

            p = self.splitall(path)
            validate = False

            #### Check if Form contain the username ####
            try:
                username = form['username']
            except Exception as e:
                print("Any username : ", e)
                return e

            ### Exception - Login Routes ###
            if p[3] == 'Login':
                validate = True

            ### Exception - Logout Routes ###
            elif p[3] == 'Logout' :
                try:
                    token = form['token']
                except Exception as e:
                    print("Any token : ", e)
                    return e
                ### Validating User ###
                vUser = self.validateUser(p[1], username, token, form)
                if vUser != True:
                    return vUser
                Logout = self.Logout(p[1], username)
                if Logout != True:
                    return Logout
                else:
                    validate = True

            ### Other Routes ###
            else:
                vRequest = True
                # To check that an assistant can't access other assistant information
                if p[1] == 'assistant':
                    vRequest = self.validateRequest(path, username, form)
                if vRequest == False:
                    return jsonify(Error="Invalid Request"), 400 #Bad Request
                try:
                    token = form['token']
                except Exception as e:
                    print("Any token : ", e)
                    return e
                vUser = self.validateUser(p[1], username, token, form)
                if vUser != True :
                    return vUser
            return validate
        except:
            return jsonify(Error = "Error Validating User"), 400 #Bad Request

    ### Method to logout a user from the system ###
    # Parameters:   role - user role (patient, assistant, doctor)
    #               username - requested username
    # Return :  True if the logout execute correctly
    #           Error if the role or username are not valid
    def Logout(self, role, username):
        dao = RoleBaseDAO()
        if role == 'Patient':
            logged = False
            dao.updateloggedPatient(username, logged)
            return True
        elif role == 'Assistant':
            logged = False
            dao.updateloggedAssistant(username, logged)
            return True
        elif role == 'Doctor':
            logged = False
            dao.updateloggedDoctor(username, logged)
            return True
        else:
            return jsonify(Error="Invalid Role or Not currently Logged in"), 401 #Unauthorized

    ### Validate the role, username, token and id (if it is required)
    # Parameters:   role - user role in the system
    #               username - user username
    #               token - user token
    #               form - requested parameters
    # Return:   Error if one of the condition don't pass
    def validateUser(self, role, username, token, form):
        dao = RoleBaseDAO()
        ### Patient Role ###
        if role == 'Patient':
            patient = dao.validatePatient(username)
            # Check the role in the path
            if not patient:
                return jsonify(Error="Invalid Username"), 401 #Unauthorized
            pusername = patient[0][0]
            ptoken = patient[0][1]
            plogged = patient[0][2]
            pid = patient [0][3]
            patientid = form['patientid']
            # Check if the patient id in the DB
            if str(pid) != str(patientid):
                return jsonify(Error="Unauthorized patient ID"), 401 #Unauthorized
            # Check if the username in the DB
            if pusername != username:
                return jsonify(Error="Invalid Username"), 400 #Bad Request
            # Validating the token
            if ptoken != token or self.validateToken(ptoken) != True :
                return jsonify(Error="Invalid Token"), 400 #Bad Request
            # Check if the user is currently logged in
            if plogged != True:
                return jsonify(Error="Not currently Logged in"), 401 #Unauthorized

        ### Assistant Role ###
        elif role == 'Assistant':
            assistant = dao.validateAssistant(username)
            # Check the role in the path
            if not assistant:
                return jsonify(Error="Invalid Username"), 400 #Bad Request
            ausername = assistant[0][0]
            atoken = assistant[0][1]
            alogged = assistant[0][2]
            # Check username in the DB
            if ausername != username:
                return jsonify(Error="Invalid Username"), 400 #Bad Request
            # Validating the token
            if atoken != token or self.validateToken(atoken) != True:
                return jsonify(Error="Invalid Token"), 400 #Bad Request
            # Check if the user is currently logged in
            if alogged != True:
                return jsonify(Error="Not currently Logged in"), 401 #Unauthorized

        ### Doctor Role ###
        elif role == 'Doctor':
            doctor = dao.validateDoctor(username)
            if not doctor:
                return jsonify(Error="Invalid Username"), 400 #Bad Request
            dusername = doctor[0][0]
            dtoken = doctor[0][1]
            dlogged = doctor[0][2]
            # Check username in the DB
            if dusername != username:
                return jsonify(Error="Invalid Username"), 400 #Bad Request
            # Validating the token
            if dtoken != token or self.validateToken(dtoken) != True :
                return jsonify(Error="Invalid Token"), 400 #Bad Request
            # Check if the user is currently logged in
            if dlogged != True:
                return jsonify(Error="Not currently Logged in"), 401 #Unauthorized
        else:
            return jsonify(Error="Invalid Role"), 401 #Unauthorized

    ## Method to validate the token ##
    # Parameters: token - token received by the frontend
    # Return:   True if validate the token correctly
    #           False if the validation of the token fail
    def validateToken(self, token):
        try:
            data = jwt.decode(token, 'thisisthesecretkey') # hay que cambiarlo
            return True
        except:
            return False


    # To be sure that one assistant can't access other assistant information #
    # Parameters:   path - requested path
    #               username - active user username
    #               form - requested parameters
    def validateRequest(self, path, username, form):
        try:
            dao = RoleBaseDAO()
            if path == '/Assistant/eCSP/PersonalInformation':
                assistantid = form['assistantid']
                assistantRequest = dao.validateAID(username, assistantid)
                if not assistantRequest:
                    return False
            return True
        except Exception as e:
            print("Any token : ", e)
            return e


    # Hay que borrarlo # Si corre bien sin ello, lo borramos
    def validateroute(self, path):
        if path == '/' or \
            path == '/Patient/eCSP/Login' or \
            path == '/Doctor/eCSP/Login' or \
            path == '/Assistant/eCSP/Login' or \
            path == '/Patient/eCSP/Logout' or \
            path == '/Assistant/eCSP/Logout' or \
            path == '/Doctor/eCSP/Logout' or \
            path == '/Doctor/eCSP/DoctorList' or \
            path == '/Doctor/eCSP/PersonalInformation' or \
            path == '/Doctor/eCSP/AssistantList' or \
            path == '/Doctor/eCSP/Assistant/Deactivate' or \
            path == '/Doctor/eCSP/Assistant/Activate' or \
            path == '/Doctor/eCSP/Patient/Deactivate' or \
            path == '/Assistant/eCSP/Patient/Deactivate' or \
            path == '/Doctor/eCSP/Patient/Activate' or \
            path == '/Assistant/eCSP/Patient/Activate' or \
            path == '/Doctor/eCSP/Assistant/PersonalInformation' or \
            path == '/Assistant/eCSP/PersonalInformation' or \
            path == '/Doctor/eCSP/PatientList' or \
            path == '/Assistant/eCSP/PatientList' or \
            path == '/Doctor/eCSP/Patient/PersonalInformation' or \
            path == '/Assistant/eCSP/Patient/PersonalInformation' or \
            path == '/Patient/eCSP/PersonalInformation' or \
            path == '/Doctor/eCSP/Patient/ConsultationNotesList' or \
            path == '/Assistant/eCSP/Patient/ConsultationNotesList' or \
            path == '/Patient/eCSP/ConsultationNotesList' or \
            path == '/Doctor/eCSP/Patient/ConsultationNotes' or \
            path == '/Assistant/eCSP/Patient/ConsultationNotes' or \
            path == '/Patient/eCSP/ConsultationNotes' or \
            path == '/Doctor/eCSP/Patient/InitialFormList' or \
            path == '/Assistant/eCSP/Patient/InitialFormList' or \
            path == '/Patient/eCSP/InitialFormList' or \
            path == '/Doctor/eCSP/Patient/InitialForm' or \
            path == '/Assistant/eCSP/Patient/InitialForm' or \
            path == '/Patient/eCSP/InitialForm' or \
            path == '/Doctor/eCSP/Patient/PrescriptionList' or \
            path == '/Assistant/eCSP/Patient/PrescriptionList' or \
            path == '/Patient/eCSP/PrescriptionList' or \
            path == '/Doctor/eCSP/Patient/Prescription' or \
            path == '/Assistant/eCSP/Patient/Prescription' or \
            path == '/Patient/eCSP/Prescription' or \
            path == '/Doctor/eCSP/Patient/ReferralList' or \
            path == '/Assistant/eCSP/Patient/ReferralList' or \
            path == '/Patient/eCSP/ReferralList' or \
            path == '/Doctor/eCSP/Patient/Referral' or \
            path == '/Assistant/eCSP/Patient/Referral' or \
            path == '/Patient/eCSP/Referral' or \
            path == '/Doctor/eCSP/Patient/ResultList' or \
            path == '/Assistant/eCSP/Patient/ResultList' or \
            path == '/Patient/eCSP/ResultList' or \
            path == '/Doctor/eCSP/Patient/Result' or \
            path == '/Assistant/eCSP/Patient/Result' or \
            path == '/Patient/eCSP/Result' or \
            path == '/Doctor/eCSP/Patient/Files' or \
            path == '/Doctor/eCSP/Patient/Files/Dates' :
            return True
        return False