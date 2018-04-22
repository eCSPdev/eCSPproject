from flask import jsonify, request
from dao.Referral import ReferralDAO

class ReferralHandler:

    def build_referrallist_dict(self,row):
        result = {}
        result['referralid'] = row[0]
        result['referral'] = row[1]
        result['assistantid'] = row[2]
        result['doctorid'] = row[2]
        result['dateofupload'] = row[4]
        result['patientid'] = row[5]
        return result

    def build_refinsert_dict(self,row):
        result = {}
        result['referral'] = row[0]
        result['assistantid'] = row[1]
        result['doctorid'] = row[2]
        result['dateofupload'] = row[3]
        result['patientid'] = row[4]
        return result

    def getPatientReferral(self, args):
        pid = args.get("patientid")
        dao = ReferralDAO()
        referral_list = dao.getPatientReferral(int(pid))
        result_list = []
        for row in referral_list:
            result = self.build_referrallist_dict(row)
            result_list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Referral=result_list)

    def getReferralByID(self, args):
        pid = args.get("patientid")
        refid = args.get("referralid")
        dao = ReferralDAO()
        row = dao.getReferralByID(int(pid), int(refid))
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            result = self.build_referrallist_dict(row)
            return jsonify(Referral=result)

    def insertReferral(self, form):
        dao = ReferralDAO()
        if len(form) != 5:
            return jsonify(Error="Malformed insert request"), 400
        else:
            referral = form['referral']
            assistantid = form['assistantid']
            doctorid = form['doctorid']
            dateofupload = form['dateofupload']
            patientid = form['patientid']
            if referral and assistantid and doctorid and dateofupload and patientid:
                dao.insertReferral(referral, assistantid, doctorid, dateofupload, patientid)
                result = self.build_refinsert_dict(referral, assistantid, doctorid, dateofupload, patientid)
                return jsonify(Referral = result), 201 #Verificar porque 201
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400