from flask import jsonify, request
from dao.Login import LoginDAO

class LoginHandler:

    def build_login_dict(self, row):
        result = {}
        result['username'] = row[0]
        result['rle'] = row[1]
        return result

    def validatePatient(self, args):
        username = args.get("username")
        pssword = args.get("pssword")
        dao = LoginDAO()
        row = dao.validatePatient(username, pssword)
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            result = self.build_login_dict(row)
            return jsonify(user=result)

    def validateAdmin(self, args):
        username = args.get("username")
        pssword = args.get("pssword")
        dao = LoginDAO()
        row = dao.validateAdmin(username, pssword)
        if not row:
            return jsonify(Error="NOT FOUND"), 404
        else:
            result = self.build_login_dict(row)
            return jsonify(User=result)