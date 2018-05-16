from flask import jsonify, request
from dao.Referral import ReferralDAO
from dao.s3connection import s3Connection
import datetime, time

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

    def build_refinsert_dict(self,referralid, referrallink, assistantusername, doctorusername, dateofupload, patientid, recordno):
        result = {}
        result['referralid'] = referralid
        result['referral'] = referrallink
        result['assistantusername'] = assistantusername
        result['doctorusername'] = doctorusername
        result['dateofupload'] = dateofupload
        result['patientid'] = patientid
        result['recordno'] = recordno
        return result

    def build_rdates_dict(self, row):
        result = {}
        result['year'] = row[0]
        result['month'] = row[1]
        return result

    def getPatientReferral(self, args):
        pid = args.get("patientid")
        dao = ReferralDAO()
        referral_list = dao.getPatientReferral(int(pid))
        result_list = []
        if not referral_list:
            return jsonify(Error="NOT FOUND"),404
        for row in referral_list:
            result = self.build_referrallist_dict(row)
            result_list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Referral=result_list)

    def getReferralByID(self, args):
        pid = args.get("patientid")
        refid = args.get("referralid")
        dao = ReferralDAO()
        row = dao.getReferralByID(pid, refid)
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            result = self.build_referrallist_dict(row[0])
            return jsonify(Referral=result)

    def insertReferral(self, form):
        dao = ReferralDAO()
        if len(form) != 5:
            return jsonify(Error="Malformed insert request"), 400
        else:
            referral = form['referral']
            # assistantid = form['assistantid']
            # doctorid = form['doctorid']
            assistantusername = form['assistantusername']
            doctorusername = form['doctorusername']
            patientid = form['patientid']
            recordno = form['recordno']

            upload_time = time.time()
            dateofupload = datetime.datetime.fromtimestamp(upload_time).strftime('%Y-%m-%d %H:%M:%S')

            if referral and dateofupload and recordno:
                if str(dao.verifyRecordno(recordno)) == str(patientid):

                    # insert the file in s3
                    s3 = s3Connection()
                    targetlocation = 'referrals/' + dateofupload + '.pdf'
                    referrallink = s3.uploadfile(referral,targetlocation)  # returns the url after storing it
                    print ("referral link : ", referrallink)
                    referralid = dao.insertReferral(referrallink, assistantusername, doctorusername, dateofupload, patientid, recordno)
                    result = self.build_refinsert_dict(referralid, referrallink, assistantusername, doctorusername, dateofupload, patientid, recordno)
                    return jsonify(Referral = result), 201
                else:
                    return jsonify(Error="Record Number does not exist.", RecordNo=recordno), 400
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400

    def getReferralDates(self, args):
        print('estoy en el Referral Dates')
        pid = args.get("patientid")
        dao = ReferralDAO()
        referral_list = dao.getReferralDates(pid)
        result_list = []
        if not referral_list:
            return jsonify(Error="NOT FOUND"),404
        for row in referral_list:
            result = self.build_rdates_dict(row)
            result_list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(ReferralDates=result_list)