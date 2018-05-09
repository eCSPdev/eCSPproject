from flask import jsonify, request
from dao.Login import LoginDAO
import datetime, time

class LoginHandler:

    def build_PLogin_dict(self, row):
        result = {}
        result['username'] = row[0]
        result['rle'] = 0
        return result

    def build_ALogin_dict(self, row, rle):
        result = {}
        result['username'] = row[0]
        result['rle'] = rle
        return result

    def build_FEinfo_dict(self, username, token, role):
        result = {}
        #print ('estoy en el diccionario')
        result['username'] = username
        result['token'] = token
        result['role'] = role
        #result ('diccionario : ', result)
        return result

    def validatePatient(self, form):
        print ('Patient login')
        username = form['username']
        pssword = form['pssword']
        dao = LoginDAO()
        row = dao.validatePatient(username, pssword)
        print('row : ', row)
        status = row[0][1]
        print('status : ', status)
        deactivationdate = row[0][2].strftime('%Y-%m-%d %H:%M:%S')
        now_time = time.time()
        today = datetime.datetime.fromtimestamp(now_time).strftime('%Y-%m-%d %H:%M:%S')
        print ('deactivationdate : ', deactivationdate)
        print('dateofchanges : ', today)
        if not row:
            return None
        elif status == True or today <= deactivationdate :
            print ('estoy validando')
            result = self.build_PLogin_dict(row)
            return 0
        else:
            return None

    def validateAdmin(self, form):
        print ('Admin login')
        username = form['username']
        print(form['username'])
        pssword = form['pssword']
        print(form['pssword'])
        dao = LoginDAO()
        doctor = dao.validateDoctor(username, pssword)
        assistant = dao.validateAssistant(username, pssword)
        print('AFTER LoginDAO')
        if not doctor:
            if not assistant:
                return None
            else:
                print ('Assistant')
                rle = '1'
                print('row : ', assistant)
                status = assistant[0][1]
                print('status : ', status)
                if status == True :
                    result = self.build_ALogin_dict(assistant[0], rle)
                    return int(1)
                else:
                    deactivationdate = assistant[0][2].strftime('%Y-%m-%d %H:%M:%S')
                    now_time = time.time()
                    today = datetime.datetime.fromtimestamp(now_time).strftime('%Y-%m-%d %H:%M:%S')
                    print('deactivationdate : ', deactivationdate)
                    print('dateofchanges : ', today)
                    if today <= deactivationdate:
                        return int(1)
                    else:
                        return None
        else:
            print ('Doctor')
            print('row : ', doctor)
            status = doctor[0][1]
            print('status : ', status)
            if status == True:
                rle = '2'
                result = self.build_ALogin_dict(doctor[0], rle)
                return int(2)
            else:
                deactivationdate = assistant[0][2].strftime('%Y-%m-%d %H:%M:%S')
                now_time = time.time()
                today = datetime.datetime.fromtimestamp(now_time).strftime('%Y-%m-%d %H:%M:%S')
                print('deactivationdate : ', deactivationdate)
                print('dateofchanges : ', today)
                if today <= deactivationdate:
                    return int(2)
                else:
                    return None

    def build_dict(self, username, token):
        #print ('username : ', username)
        #print ('token : ', token)
        result = self.build_FEinfo_dict(username, token)
        return jsonify(user = result)

    def updateLogInformation(self, username, t, role):
        print ('updating ...')
        dao = LoginDAO()
        logged = True
        token = t.decode('UTF-8')
        if username :
            print("CALLING DAO HERE")
            if role == 0:
                dao.updateloggedPatient(username, token, logged)
                result = self.build_FEinfo_dict(username, token, 'Patient')
                return jsonify(Patient=result), 200
            if role == 1:
                dao.updateloggedAssistant(username, token, logged)
                result = self.build_FEinfo_dict(username, token, 'Assistant')
                return jsonify(Patient=result), 200
            if role == 2:
                dao.updateloggedDoctor(username, token, logged)
                result = self.build_FEinfo_dict(username, token, 'Doctor')
                return jsonify(Patient=result), 200
            else:
                return jsonify(Error="Invalid user"), 400