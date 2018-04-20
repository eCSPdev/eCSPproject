from flask import jsonify, request
from dao.Patient import PatientDAO

## Luis Santiago ##
class PatientHandler:

    def mapToDict(self,row):
        result = {}
        result['RecordNo'] = row[0]
        result['SSN'] = row[1]
        result['Firstname'] = row[2]
        result['LastName'] = row[3]
        result['BirthDate'] = row[4]
        result['Gener'] = row[5]
        result['Phone'] = row[6]
        result['Status'] = row[7]
        result['Email'] = row[8]
        result['Password'] = row[9]
        return result

    def getAllPatient(self):
        dao = PatientDAO()
        result = dao.getAllPatient()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Users=mapped_result)

    def getPatientByID(self, pid):
        dao = PatientDAO()
        result = dao.getPatientByID(pid)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
            return jsonify(Users=mapped_result)