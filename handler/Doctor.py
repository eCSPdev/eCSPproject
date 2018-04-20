from flask import jsonify, request
from dao.Doctor import DoctorDAO

## Coralis Camacho##
class DoctorHandler:

    def mapToDict(self,row):
        result = {}
        result['DoctorID'] = row[0]
        result['LicNo'] = row[1]
        result['Firstname'] = row[2]
        result['LastName'] = row[3]
        result['OfficeName'] = row[4]
        result['Phone'] = row[5]
        result['Status'] = row[6]
        result['Email'] = row[7]
        result['Password'] = row[8]
        return result

    def getAllDoctor(self):
        dao = DoctorDAO()
        result = dao.getAllDoctor()
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Messages=mapped_result)

    def getDoctorByID(self, did):
        dao = DoctorDAO()
        result = dao.getAssistantByID(did)
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Messages=mapped_result)