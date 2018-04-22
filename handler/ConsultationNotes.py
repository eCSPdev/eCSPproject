from flask import jsonify, request
from dao.ConsultationNotes import ConsultationNotesDAO

class ConsultationNotesHandler:

    def build_consultationnoteslist_dict(self,row):
        result = {}
        result['consultationnoteid'] = row[0]
        result['consultationnote'] = row[1]
        result['assistantid'] = row[2]
        result['doctorid'] = row[2]
        result['dateofupload'] = row[4]
        result['patientid'] = row[5]
        return result

    def build_cninsert_dict(self,row):
        result = {}
        result['consultationnote'] = row[0]
        result['assistantid'] = row[1]
        result['doctorid'] = row[2]
        result['dateofupload'] = row[3]
        result['patientid'] = row[4]
        return result

    def getPatientConsultationNotes(self, args):
        pid = args.get("patientid")
        dao = ConsultationNotesDAO()
        consultationnotes_list = dao.getPatientConsultationNotes(pid)
        result_list = []
        for row in consultationnotes_list:
            result = self.build_consultationnoteslist_dict(row)
            result_list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(ConsultationNotes=result_list)

    def getConsultationNotesByID(self, args):
        pid = args.get("patientid")
        nid = args.get("consultationnoteid")
        dao = ConsultationNotesDAO()
        row = dao.getConsultationNotesByID(int(pid), int(nid))
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            result = self.build_consultationnoteslist_dict(row)
            return jsonify(ConsultatioNote=result)

    def insertConsultationNotes(self, form):
        dao = ConsultationNotesDAO()
        if len(form) != 5:
            return jsonify(Error="Malformed insert request"), 400
        else:
            consultationnote = form['consultationnote']
            assistantid = form['assistantid']
            doctorid = form['doctorid']
            dateofupload = form['dateofupload']
            patientid = form['patientid']
            if consultationnote and assistantid and doctorid and dateofupload and patientid:
                dao.insertConsultationNotes(consultationnote, assistantid, doctorid, dateofupload, patientid)
                result = self.build_cninsert_dict(consultationnote, assistantid, doctorid, dateofupload, patientid)
                return jsonify(ConsultatioNote = result), 201 #Verificar porque 201
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400