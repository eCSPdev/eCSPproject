from flask import jsonify, request
from dao.Prescription import PrescriptionDAO

class PrescriptionHandler:

    def mapToDict(self,row):
        result = {}
        result['RecordNumber'] = row[0]
        result['PrescriptionID'] = row[1]
        result['PrescriptionName'] = row[2]
        result['AssistantID'] = row[2]
        result['DoctorID'] = row[4]
        result['Date'] = row[5]
        result['Time'] = row[6]
        return result

    def getAllPrescription(self, rn):
        dao = PrescriptionDAO()
        result = dao.getAllPrescription(rn)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Users=mapped_result)

    def getPrescriptionByID(self, rn, pid):
        dao = PrescriptionDAO()
        result = dao.getPrescriptionByID(rn, pid)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
            return jsonify(Users=mapped_result)