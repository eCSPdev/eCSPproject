from flask import jsonify, request
from dao.Result import ResultDAO

class ResultHandler:

    def build_resultlist_dict(self,row):
        result = {}
        result['resultid'] = row[0]
        result['result'] = row[1]
        result['assistantid'] = row[2]
        result['doctorid'] = row[2]
        result['dateofupload'] = row[4]
        result['patientid'] = row[5]
        return result

    def build_resinsert_dict(self, result, assistantid, doctorid, dateofupload, patientid):
        result = {}
        result['result'] = result
        result['assistantid'] = assistantid
        result['doctorid'] = doctorid
        result['dateofupload'] = dateofupload
        result['patientid'] = patientid
        return result

    def getPatientResult(self, args):
        pid = args.get("patientid")
        dao = ResultDAO()
        result_list = dao.getPatientResult(int(pid))
        list = []
        if not result_list:
            return jsonify(Error="NOT FOUND"),404
        for row in result_list:
            result = self.build_resultlist_dict(row)
            list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Result=list)

    def getResultByID(self, args):
        pid = args.get("patientid")
        resid = args.get("resultid")
        dao = ResultDAO()
        row = dao.getResultByID(pid, resid)
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            result = self.build_resultlist_dict(row[0])
            return jsonify(Result=result)

    def insertResult(self, form):
        dao = ResultDAO()
        if len(form) != 5:
            return jsonify(Error="Malformed insert request"), 400
        else:
            result = form['result']
            assistantid = form['assistantid']
            doctorid = form['doctorid']
            dateofupload = form['dateofupload']
            patientid = form['patientid']
            recordno = form['recordno']
            if result and dateofupload and recordno:
                if dao.verifyRecordno(recordno) != None:
                    dao.insertReferral(result, assistantid, doctorid, dateofupload, patientid)
                    result = self.build_refinsert_dict(result, assistantid, doctorid, dateofupload, patientid)
                    return jsonify(Referral = result), 201
                else:
                    return jsonify(Error="Record Number does not exist.", RecordNo=recordno), 400
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400