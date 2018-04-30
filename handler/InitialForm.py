from flask import jsonify, request
from dao.InitialForm import InitialFormDAO

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

    def build_ifinsert_dict(self, initialform, assistantid, doctorid, dateofupload, patientid):
        result = {}
        result['initialform'] = initialform
        result['assistantid'] = assistantid
        result['doctorid'] = doctorid
        result['dateofupload'] = dateofupload
        result['patientid'] = patientid
        return result

    def getPatientInitialForm(self, args):
        pid = args.get("patientid")
        dao = InitialFormDAO()
        initialform_list = dao.getPatientInitialForm(pid)
        result_list = []
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
            result = self.build_initialformlist_dict(row)
            return jsonify(ConsultatioNote=result)

    def insertInitialForm(self, form):
        dao = InitialFormDAO()
        if len(form) != 5:
            return jsonify(Error="Malformed insert request"), 400
        else:
            initialform = form['initialform']
            assistantid = form['assistantid']
            doctorid = form['doctorid']
            dateofupload = form['dateofupload']
            patientid = form['patientid']
            recordno = form['recordno']
            if initialform and dateofupload and recordno:
                if dao.verifyRecordno(recordno) != None:
                    dao.insertInitialForm(initialform, assistantid, doctorid, dateofupload, patientid)
                    result = self.build_ifinsert_dict(initialform, assistantid, doctorid, dateofupload, patientid)
                    return jsonify(InitialForm = result), 201 #Verificar porque 201
                else:
                    return jsonify(Error="Record Number does not exist.", RecordNo=recordno), 400
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400