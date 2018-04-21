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

    def getDoctorByID(self, did):
        dao = DoctorDAO()
        row = dao.getAssistantByID(did)
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            doctor = self.build_doctor_dict(row)
            return jsonify(Doctor = doctor)