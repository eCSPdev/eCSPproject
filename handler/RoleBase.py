from flask import jsonify, request
from dao.RoleBase import RoleBaseDAO

import os, sys
import jwt

class RoleBase:

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

    def validate(self, path, form):
        #valida el path
        vpath = self.validateroute(path)
        if vpath != True:
            return jsonify(Error="Invalid Route"), 405
        p = self.splitall(path)
        validate = False
        #verifica si el username esta en el form
        try:
            username = form['username']
        except Exception as e:
            print("Any username : ", e)
            return e
        #print (p[3])
        #Login
        if p[3] == 'Login':
            #print ('User : ', p[1])
            #print ('Action : ', p[3])
            validate = True
        #Logout
        elif p[3] == 'Logout' :
            try:
                token = form['token']
            except Exception as e:
                print("Any token : ", e)
                return e
            #print('token : ', token)
            vUser = self.validateUser(p[1], username, token)
            if vUser != True:
                return vUser
            Logout = self.Logout(p[1], username)
            #print ('result : ', vRoleLog)
            if Logout != True:
                return Logout
            else:
                validate = True
        else:
            print ('Validando ... ')
            try:
                token = form['token']
            except Exception as e:
                print("Any token : ", e)
                return e
            #print('token : ', token)
            vUser = self.validateUser(p[1], username, token)
            if vUser != True:
                return vUser
        return validate

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
            #print ('estoy en el validate del doctor')
            logged = False
            dao.updateloggedDoctor(username, logged)
            return True
        else:
            return jsonify(Error="Invalid Role or Not currently Logged in"), 405

    def validateUser(self, role, username, token):
        dao = RoleBaseDAO()
        if role == 'Patient':
            patient = dao.validatePatient(username)
            if not patient:
                return jsonify(Error="Invalid Username"), 405
            pusername = patient[0][0]
            ptoken = patient[0][1]
            plogged = patient[0][2]

            if pusername != username:
                return jsonify(Error="Invalid Username"), 405
            if ptoken != token or self.validateToken(ptoken) != True :
                #print('token : ', token)
                #print('ptoken : ', ptoken)
                return jsonify(Error="Invalid Token"), 405
            if plogged != True:
                return jsonify(Error="Not currently Logged in"), 405

        elif role == 'Assistant':
            assistant = dao.validateAssistant(username)
            if not assistant:
                return jsonify(Error="Invalid Username"), 405
            ausername = assistant[0][0]
            atoken = assistant[0][1]
            alogged = assistant[0][2]
            if ausername != username:
                return jsonify(Error="Invalid Username"), 405
            if atoken != token or self.validateToken(atoken) != True :
                return jsonify(Error="Invalid Token"), 405
            if alogged != True:
                return jsonify(Error="Not currently Logged in"), 405

        elif role == 'Doctor':
            #print('estoy en el validate del doctor')
            doctor = dao.validateDoctor(username)
            if not doctor:
                return jsonify(Error="Invalid Username"), 405
            dusername = doctor[0][0]
            dtoken = doctor[0][1]
            dlogged = doctor[0][2]
            if dusername != username:
                return jsonify(Error="Invalid Username"), 405
            if dtoken != token or self.validateToken(dtoken) != True :
                return jsonify(Error="Invalid Token"), 403
            if dlogged != True:
                return jsonify(Error="Not currently Logged in"), 405
        else:
            return jsonify(Error="Invalid Role"), 405

    def validateToken(self, token):
        #print('estoy verificando el token')
        # print('token', token)
        try:
            #print('validate token : ')
            data = jwt.decode(token, 'thisisthesecretkey')
            #print ('validate token : True')
            return True
        except:
            #print('validate token : False')
            return False

    def validateroute(self, path):
        if path == '/Patient/eCSP/Login' or \
            path == '/Doctor/eCSP/Login' or \
            path == '/Assistant/eCSP/Login' or \
            path == '/Patient/eCSP/Logout' or \
            path == '/Assistant/eCSP/Logout' or \
            path == '/Doctor/eCSP/Logout' or \
            path == '/Doctor/eCSP/DoctorList' or \
            path == '/Doctor/eCSP/PersonalInformation' or \
            path == '/Doctor/eCSP/AssistantList' or \
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
            path == '/Patient/eCSP/Result':
            return True
        return False
