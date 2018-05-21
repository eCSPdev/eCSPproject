from flask import jsonify, request
from dao.Login import LoginDAO
# import datetime, time
from datetime import datetime, timezone

#### Login Handler Class - Login a user if all credentials are correct ####
class LoginHandler:

    #### Patient Login Diccionary ####
    def build_PLogin_dict(self, row, token):
        result = {}
        result['username'] = row[0]
        result['status'] = row[1]
        result['deactivationdate'] = row[2]
        result['firstname'] = row[3]
        result['middlename'] = row[4]
        result['lastname'] = row[5]
        result['token'] = token
        result['patientid'] = row[6]
        result['recordno'] = row[7]
        result['rle'] = 'Patient'
        return result

    #### Assistant Login Diccionary ####
    def build_ALogin_dict(self, row, token):
        result = {}
        result['username'] = row[0]
        result['status'] = row[1]
        result['deactivationdate'] = row[2]
        result['firstname'] = row[3]
        result['middlename'] = row[4]
        result['lastname'] = row[5]
        result['token'] = token
        result['assistantid'] = row[6]
        result['rle'] = 'Assistant'
        return result

    #### Doctor Login Diccionary ####
    def build_DLogin_dict(self, row, token):
        result = {}
        result['username'] = row[0]
        result['status'] = row[1]
        result['deactivationdate'] = row[2]
        result['firstname'] = row[3]
        result['middlename'] = row[4]
        result['lastname'] = row[5]
        result['token'] = token
        result['doctorid'] = row[6]
        result['rle'] = 'Doctor'
        return result

    ### Validate Patient credentials
    # Parameters:   token - user token
    #               form - requested parameters
    # Return:   Error if one of the condition don't pass
    def validatePatient(self, form, token):
        username = form['username']
        pssword = form['pssword']
        dao = LoginDAO()
        patient = dao.validatePatient(username, pssword)
        status = patient[1]
        if patient == None:
            return jsonify(Error="Invalid Username or Password"), 400
        if status == True:
            result = self.build_PLogin_dict(patient, token)
            self.updateLogInformation(username, token, 'Patient')
            return jsonify(Patient = result)
        else:
            deactivationdate = patient[2].strftime('%Y-%m-%d %H:%M:%S')
            # now_time = time.time()
            today = datetime.now(timezone.utc).astimezone().strftime('%Y-%m-%d %H:%M:%S')#datetime.datetime.fromtimestamp(now_time).strftime('%Y-%m-%d %H:%M:%S')
            if today <= deactivationdate:
                result = self.build_PLogin_dict(patient, token)
                self.updateLogInformation(username, token, 'Patient')
                return jsonify(Patient=result)
            else:
                return jsonify(Error="Expired Account"), 400

    ### Validate Admin (Doctor & Assistant) credentials
    # Parameters:   token - user token
    #               form - requested parameters
    # Return:   Error if one of the condition don't pass
    def validateAdmin(self, form, token):
        username = form['username']
        pssword = form['pssword']
        dao = LoginDAO()
        doctor = dao.validateDoctor(username, pssword)
        assistant = dao.validateAssistant(username, pssword)
        if not doctor:
            if not assistant:
                return jsonify(Error="Invalid Username or Password"), 400
            else:
                status = assistant[1]
                if status == True :
                    result = self.build_ALogin_dict(assistant, token)
                    self.updateLogInformation(username, token, 'Assistant')
                    return jsonify(Assistant=result)
                else:
                    return jsonify(Error="Expired Account"), 400
        else:
            status = doctor[1]
            if status == True:
                result = self.build_DLogin_dict(doctor, token)
                self.updateLogInformation(username, token, 'Doctor')
                return jsonify(Doctor=result)
            else:
                return jsonify(Error="Expired Account"), 400

    ### Update the login information in the database
    # Parameters:   token - user token
    #               form - requested parameters
    #               role - role of the active user
    # Return:   Error if one of the condition don't pass
    def updateLogInformation(self, username, token, role):
        dao = LoginDAO()
        logged = True
        if username :
            if role == 'Patient':
                dao.updateloggedPatient(username, token, logged)
                return
            if role == 'Assistant':
                dao.updateloggedAssistant(username, token, logged)
                return
            if role == 'Doctor':
                dao.updateloggedDoctor(username, token, logged)
                return
            else:
                return jsonify(Error="Invalid user"), 400