from flask import jsonify, request
from dao.Login import LoginDAO

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

    def build_FEinfo_dict(self, username, token):
        result = {}
        #print ('estoy en el diccionario')
        result['username'] = username
        result['token'] = token
        #result ('diccionario : ', result)
        return result

    def validatePatient(self, form):
        print ('Patient login')
        username = form['username']
        pssword = form['pssword']
        dao = LoginDAO()
        row = dao.validatePatient(username, pssword)
        if not row:
            return None
        else:
            result = self.build_PLogin_dict(row)
            return 0

    def validateAdmin(self, form):
        print ('Admin login')
        username = form['username']
        pssword = form['pssword']
        dao = LoginDAO()
        doctor = dao.validateDoctor(username, pssword)
        assistant = dao.validateAssistant(username, pssword)
        if not doctor:
            if not assistant:
                return None
            else:
                rle = '1'
                result = self.build_ALogin_dict(assistant[0], rle)
                return int(1)
        else:
            #print('estoy en el role de doctor')
            rle = '2'
            result = self.build_ALogin_dict(doctor[0], rle)
            return 2

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
                result = self.build_FEinfo_dict(username, token)
                return jsonify(Patient=result), 200
            if role == 1:
                dao.updateloggedAssistant(username, token, logged)
                result = self.build_FEinfo_dict(username, token)
                return jsonify(Patient=result), 200
            if role == 2:
                dao.updateloggedDoctor(username, token, logged)
                result = self.build_FEinfo_dict(username, token)
                return jsonify(Patient=result), 200
            else:
                return jsonify(Error="Invalid user"), 400