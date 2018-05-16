from flask import jsonify, request
from dao.InitialForm import InitialFormDAO
from dao.s3connection import s3Connection
import datetime, time

class InitialFormHandler:

    def build_initialformlist_dict(self,row):
        result = {}
        result['initialformid'] = row[0]
        result['initialform'] = row[1]
        result['assistantid'] = row[2]
        result['doctorid'] = row[2]
        result['dateofupload'] = row[4]
        result['patientid'] = row[5]
        return result

    def build_ifinsert_dict(self, initialformid, initialformlink, assistantid, doctorid, dateofupload, patientid, recordno):
        result = {}
        result['initialformid'] = initialformid
        result['initialform'] = initialformlink
        result['assistantid'] = assistantid
        result['doctorid'] = doctorid
        result['dateofupload'] = dateofupload
        result['patientid'] = patientid
        result['recordno'] = recordno
        return result

    def build_ifdates_dict(self, row):
        result = {}
        result['year'] = row[0]
        result['month'] = row[1]
        return result

    def getPatientInitialForm(self, args):
        pid = args.get("patientid")
        dao = InitialFormDAO()
        initialform_list = dao.getPatientInitialForm(pid)
        result_list = []
        if not initialform_list:
            return jsonify(Error="NOT FOUND"),404
        for row in initialform_list:
            result = self.build_initialformlist_dict(row)
            result_list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(InitialForm=result_list)

    def getInitialFormByID(self, args):
        pid = args.get("patientid")
        nid = args.get("initialformid")
        dao = InitialFormDAO()
        row = dao.getInitialFormByID(pid, nid)
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            result = self.build_initialformlist_dict(row[0])
            return jsonify(ConsultatioNote=result)

    def insertInitialForm(self, form):
        dao = InitialFormDAO()
        if len(form) != 5:
            return jsonify(Error="Malformed insert request"), 400
        else:
            initialform = form['initialform']
            assistantid = form['assistantid']
            doctorid = form['doctorid']
            patientid = form['patientid']
            recordno = form['recordno']

            upload_time = time.time()
            dateofupload = datetime.datetime.fromtimestamp(upload_time).strftime('%Y-%m-%d %H:%M:%S')

            if initialform and dateofupload and recordno:
                if dao.verifyRecordno(recordno) != None:

                    s3 = s3Connection()
                    targetlocation = 'initialforms/' + dateofupload + '.pdf'
                    initialformlink = s3.uploadfile(initialform,targetlocation)  # returns the url after storing it

                    initialformid = dao.insertInitialForm(initialformlink, assistantid, doctorid, dateofupload, patientid, recordno)
                    result = self.build_ifinsert_dict(initialformid, initialformlink, assistantid, doctorid, dateofupload, patientid, recordno)
                    return jsonify(InitialForm = result), 201 #Verificar porque 201
                else:
                    return jsonify(Error="Record Number does not exist.", RecordNo=recordno), 400
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400

    def getInitialFormDates(self, args):
        print('estoy en el IF Dates')
        pid = args.get("patientid")
        dao = InitialFormDAO()
        initialform_list = dao.getInitialFormDates(pid)
        result_list = []
        if not initialform_list:
            return jsonify(Error="NOT FOUND"),404
        for row in initialform_list:
            result = self.build_ifdates_dict(row)
            result_list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(InitialFormDates=result_list)