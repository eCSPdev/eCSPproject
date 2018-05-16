from flask import jsonify, request
from dao.Result import ResultDAO
from dao.s3connection import s3Connection
import datetime, time

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

    def build_resinsert_dict(self, resultid, resultlink, assistantusername, doctorusername, dateofupload, patientid, recordno):
        result = {}
        result['resultid'] = resultid
        result['resultlink'] = resultlink
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
            # assistantid = form['assistantid']
            # doctorid = form['doctorid']
            assistantusername = form['assistantusername']
            doctorusername = form['doctorusername']
            patientid = form['patientid']
            recordno = form['recordno']

            upload_time = time.time()
            dateofupload = datetime.datetime.fromtimestamp(upload_time).strftime('%Y-%m-%d %H:%M:%S')

            if result and dateofupload and recordno:
                if str(dao.verifyRecordno(recordno)) == str(patientid):

                    # insert the file in s3
                    s3 = s3Connection()
                    targetlocation = 'results/' + dateofupload + '.pdf'
                    resultlink = s3.uploadfile(result,targetlocation)  # returns the url after storing it
                    print ("result link : ", resultlink)
                    resultid = dao.insertResult(resultlink, assistantusername, doctorusername, dateofupload, patientid, recordno)
                    result = self.build_resinsert_dict(resultid, resultlink, assistantusername, doctorusername, dateofupload, patientid, recordno)
                    return jsonify(Results = result), 201
                else:
                    return jsonify(Error="Record Number does not exist.", RecordNo=recordno), 400
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400

    def getResultDates(self, args):
        print('estoy en el Result Dates')
        pid = args.get("patientid")
        dao = ResultDAO()
        results_list = dao.getResultDates(pid)
        result_list = []
        if not results_list:
            return jsonify(Error="NOT FOUND"),404
        for row in results_list:
            result = self.build_rdates_dict(row)
            result_list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(ResultDates=result_list)