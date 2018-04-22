from flask import jsonify, request
from dao.InitialForm import InitialFormDAO

class InitialFormHandler:

    def mapToDict(self,row):
        result = {}
        result['RecordNumber'] = row[0]
        result['InitialFormID'] = row[1]
        result['InitialFormName'] = row[2]
        result['AssistantID'] = row[2]
        result['DoctorID'] = row[4]
        result['Date'] = row[5]
        result['Time'] = row[6]
        return result

    def getAllInitialForm(self, rn):
        dao = InitialFormDAO()
        result = dao.getAllInitialForm(rn)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Users=mapped_result)

    def getInitialFormByID(self, rn, ifid):
        dao = InitialFormDAO()
        result = dao.getInitialFormByID(rn, ifid)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
            return jsonify(Users=mapped_result)