from flask import jsonify, request
from dao.Login import LoginDAO
import datetime, time

class LoginHandler:

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
        result['rle'] = 'Patient'
        print (result)
        return result

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
        print (result)
        return result

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
        print (result)
        return result

    def build_FEinfo_dict(self, username, token, role):
        result = {}
        #print ('estoy en el diccionario')
        result['username'] = username
        result['token'] = token
        result['role'] = role
        #result ('diccionario : ', result)
        return result

    def validatePatient(self, form, token):
        print ('Patient login')
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
            now_time = time.time()
            today = datetime.datetime.fromtimestamp(now_time).strftime('%Y-%m-%d %H:%M:%S')
            if today <= deactivationdate:
                result = self.build_PLogin_dict(patient, token)
                self.updateLogInformation(username, token, 'Patient')
                return jsonify(Patient=result)
            else:
                return jsonify(Error="Expited Account"), 400


    def validateAdmin(self, form, token):
        print ('Admin login')
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
                print('status : ', status)
                if status == True :
                    result = self.build_ALogin_dict(assistant, token)
                    self.updateLogInformation(username, token, 'Assistant')
                    return jsonify(Assistant=result)
                else:
                    deactivationdate = assistant[2].strftime('%Y-%m-%d %H:%M:%S')
                    now_time = time.time()
                    today = datetime.datetime.fromtimestamp(now_time).strftime('%Y-%m-%d %H:%M:%S')
                    print('deactivationdate : ', deactivationdate)
                    print('dateofchanges : ', today)
                    if today <= deactivationdate:
                        result = self.build_ALogin_dict(assistant, token)
                        self.updateLogInformation(username, token, 'Assistant')
                        return jsonify(Assistant=result)
                    else:
                        return jsonify(Error="Expired Account"), 400
        else:
            status = doctor[1]
            print('status : ', status)
            if status == True:
                result = self.build_DLogin_dict(doctor, token)
                self.updateLogInformation(username, token, 'Doctor')
                return jsonify(Doctor=result)
            else:
                deactivationdate = doctor[2].strftime('%Y-%m-%d %H:%M:%S')
                now_time = time.time()
                today = datetime.datetime.fromtimestamp(now_time).strftime('%Y-%m-%d %H:%M:%S')
                print('deactivationdate : ', deactivationdate)
                print('dateofchanges : ', today)
                if today <= deactivationdate:
                    result = self.build_DLogin_dict(doctor, token)
                    self.updateLogInformation(username, token, 'Doctor')
                    return jsonify(Doctor=result)
                else:
                    return jsonify(Error="Expired Account"), 400

    def build_dict(self, username, token):
        #print ('username : ', username)
        #print ('token : ', token)
        result = self.build_FEinfo_dict(username, token)
        return jsonify(user = result)

    def updateLogInformation(self, username, token, role):
        print ('updating ...')
        dao = LoginDAO()
        logged = True
        if username :
            print("CALLING DAO HERE")
            if role == 'Patient':
                dao.updateloggedPatient(username, token, logged)
                #result = self.build_FEinfo_dict(username, token, 'Patient',firstname, middlename, lastname)
                return
            if role == 'Assistant':
                dao.updateloggedAssistant(username, token, logged)
                #result = self.build_FEinfo_dict(username, token, 'Assistant',firstname, middlename, lastname)
                return
            if role == 'Doctor':
                dao.updateloggedDoctor(username, token, logged)
                #result = self.build_FEinfo_dict(username, token, 'Doctor',firstname, middlename, lastname)
                return
            else:
                return jsonify(Error="Invalid user"), 400