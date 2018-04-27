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
        result['token'] = token.decode('UTF-8')
        #result ('diccionario : ', result)
        return result

    def validatePatient(self, form):
        print ('Patient login')
        username = form['username']
        pssword = form['pssword']
        dao = LoginDAO()
        row = dao.validatePatient(username, pssword)
        if not row:
            return False
        else:
            result = self.build_PLogin_dict(row)
            return result

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
                rle = 1
                result = self.build_ALogin_dict(assistant[0], rle)
                return result
        else:
            rle = 2
            result = self.build_ALogin_dict(doctor[0], rle)
            return result

    def build_dict(self, username, token):
        print ('username : ', username)
        print ('token : ', token)
        result = self.build_FEinfo_dict(username, token)
        return jsonify(user = result)
