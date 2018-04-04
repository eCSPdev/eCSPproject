from flask import jsonify, request
from dao.Result import ResultDAO

class ResultHandler:

    def mapToDict(self,row):
        result = {}
        result['RecordNumber'] = row[0]
        result['ResultID'] = row[1]
        result['ResultName'] = row[2]
        result['AssistantID'] = row[2]
        result['DoctorID'] = row[4]
        result['Date'] = row[5]
        result['Time'] = row[6]
        return result

    def getAllResult(self, rn):
        dao = ResultDAO()
        result = dao.getAllResult(rn)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Users=mapped_result)

    def getResultByID(self, rn, rid):
        dao = ResultDAO()
        result = dao.getResultByID(rn, rid)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
            return jsonify(Users=mapped_result)