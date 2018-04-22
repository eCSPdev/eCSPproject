from flask import jsonify, request
from dao.Referral import ReferralDAO

class ReferralHandler:

    def mapToDict(self,row):
        result = {}
        result['RecordNumber'] = row[0]
        result['ReferralID'] = row[1]
        result['ReferralName'] = row[2]
        result['AssistantID'] = row[2]
        result['DoctorID'] = row[4]
        result['Date'] = row[5]
        result['Time'] = row[6]
        return result

    def getAllReferral(self, rn):
        dao = ReferralDAO()
        result = dao.getAllReferral(rn)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Users=mapped_result)

    def getReferralByID(self, rn, rid):
        dao = ReferralDAO()
        result = dao.getReferralByID(rn, rid)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
            return jsonify(Users=mapped_result)