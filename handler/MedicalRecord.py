from flask import jsonify, request
from dao.MedicalRecord import MedicalRecordDAO

class MedicalRecordHandler:

    def mapToDict(self,row):
        result = {}
        result['RecordNo'] = row[0]
        return result

    def getAllMedicalRecord(self):
        dao = MedicalRecordDAO()
        result = dao.getAllMedicalRecord()
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Messages=mapped_result)

    def getMedicalRecordByID(self, mr):
        dao = MedicalRecordDAO()
        result = dao.getPatientByID(mr)
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToDict(r))
            return jsonify(Messages=mapped_result)