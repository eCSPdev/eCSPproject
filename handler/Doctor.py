from flask import jsonify, request
from dao.Doctor import DoctorDAO

## Coralis Camacho##
class DoctorHandler:

    def build_doctor_dict(self,row):
        result = {}
        result['doctorid'] = row[0]
        result['licenseno'] = row[1]
        result['firstname'] = row[2]
        result['middlename'] = row[3]
        result['lastname'] = row[4]
        result['officename'] = row[5]
        result['phone'] = row[6]
        result['status'] = row[7]
        result['email'] = row[8]
        result['username'] = row[9]
        result['pssword'] = row[10]
        return result

    def getAllDoctor(self):
        dao = DoctorDAO()
        result = dao.getAllDoctor()
        result_list = []
        for r in result:
            result = self.build_doctor_dict()
            result.append(result)
        return jsonify(Doctor=result_list)

    def getDoctorByID(self, args):
        dao = DoctorDAO()
        doctorid = int(args.get("doctorid"))
        row = dao.getAssistantByID(doctorid)
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            doctor = self.build_doctor_dict(row)
            return jsonify(Doctor = doctor)

    def updateDoctor(self, args):
        dao = DoctorDAO()
        doctorid = int(args.get("doctorid"))
        if not dao.getDoctorByID(doctorid):
            return jsonify(Error="Part not found."), 404
        else:
            if len(args) != 10:
                return jsonify(Error="Malformed update request"), 400
            else:
                licenseno = args.get("liceseno")
                firstname = args.get("firstname")
                middlename = args.get("middlename")
                lastname = args.get("lastname")
                officename = args.get("officename")
                phone = args.get("phone")
                status = bool(args.get("status"))
                email = args.get("email")
                username = args.get("username")
                pssword = args.get("pssword")
                if doctorid and licenseno and firstname and middlename and lastname and officename and phone and status and email and username and pssword:
                    dao.update(doctorid, licenseno, firstname, middlename, lastname, officename, phone, status, email, username, pssword)
                    result = self.build_doctor_dict(doctorid, licenseno, firstname, middlename, lastname, officename, phone, status, email, username, pssword)
                    return jsonify(Doctor = result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
