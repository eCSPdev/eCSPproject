from flask import jsonify, request
from dao.Assistant import AssistantDAO

class AssistantHandler:

    def mapToDict(self,row):
        result = {}
        result['AssistantID'] = row[0]
        result['Firstname'] = row[1]
        result['LastName'] = row[2]
        result['Phone'] = row[3]
        result['Status'] = row[4]
        result['Email'] = row[5]
        result['Password'] = row[6]
        return result

    def getAllAssistant(self):
        dao = AssistantDAO()
        result = dao.getAllAssistant()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Users=mapped_result)

    def getAssistantByID(self, aid):
        dao = AssistantDAO()
        result = dao.getAssistantByID(aid)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
            return jsonify(Users=mapped_result)