from flask import jsonify, request
from dao.ConsultationNotes import ConsultationNotesDAO

class ConsultationNotesHandler:

    def build_consultationnoteslist_dict(self,row):
        result = {}
        print(row)
        result['consultationnoteid'] = row[0]
        result['consultationnote'] = row[1]
        result['assistantid'] = row[2]
        result['doctorid'] = row[2]
        result['dateofupload'] = row[4]
        result['patientid'] = row[5]
        result['recordno'] = row[6]
        return result

    def build_cninsert_dict(self, consultationnoteid, consultationnote, assistantid, doctorid, dateofupload, patientid, recordno):
        result = {}
        result['consultationnoteid'] = consultationnoteid
        result['consultationnote'] = consultationnote
        result['assistantid'] = assistantid
        result['doctorid'] = doctorid
        result['dateofupload'] = dateofupload
        result['patientid'] = patientid
        result['recordno'] = recordno
        return result

    def getPatientConsultationNotes(self, args):
        print('estoy en el CN List')
        pid = args.get("patientid")
        dao = ConsultationNotesDAO()
        consultationnotes_list = dao.getPatientConsultationNotes(pid)
        result_list = []
        if not consultationnotes_list:
            return jsonify(Error="NOT FOUND"),404
        for row in consultationnotes_list:
            result = self.build_consultationnoteslist_dict(row)
            result_list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(ConsultationNotes=result_list)

    def getConsultationNotesByID(self, args):
        pid = args.get("patientid")
        nid = args.get("consultationnoteid")
        dao = ConsultationNotesDAO()
        row = dao.getConsultationNotesByID(pid, nid)
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            result = self.build_consultationnoteslist_dict(row[0])
            return jsonify(ConsultatioNote=result)

    def insertConsultationNotes(self, form):
        dao = ConsultationNotesDAO()
        if len(form) != 6:
            return jsonify(Error="Malformed insert request"), 400
        else:
            consultationnote = form['consultationnote']
            assistantid = form['assistantid']
            doctorid = form['doctorid']
            dateofupload = form['dateofupload']
            patientid = form['patientid']
            recordno = form['recordno']
            if (consultationnote and dateofupload and recordno):

                if dao.verifyRecordno(recordno) != None:
                    consultationnoteid = dao.insertConsultationNotes(consultationnote, assistantid, doctorid, dateofupload,
                                                                     patientid, recordno)
                    result = self.build_cninsert_dict(consultationnoteid, consultationnote, assistantid, doctorid,
                                                      dateofupload, patientid, recordno)
                    return jsonify(Success="Consultation Node inserted.", ConsultatioNote = result), 201
                else:
                    return jsonify(Error="Record Number does not exist.", RecordNo=recordno), 400
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400