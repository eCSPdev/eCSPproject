from flask import jsonify, request
from dao.ConsultationNotes import ConsultationNotesDAO

class ConsultationNotesHandler:

    def mapToDict(self,row):
        result = {}
        result['RecordNumber'] = row[0]
        result['NoteID'] = row[1]
        result['NoteName'] = row[2]
        result['AssistantID'] = row[2]
        result['DoctorID'] = row[4]
        result['Date'] = row[5]
        result['Time'] = row[6]
        return result

    def getAllColsultationNotes(self, rn):
        dao = ConsultationNotesDAO()
        result = dao.getAllConsultationNotes(rn)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Users=mapped_result)

    def getConsultationNotesByID(self, rn, nid):
        dao = ConsultationNotesDAO()
        result = dao.getConsultationNotesByID(rn, nid)
        mapped_result = []
        if result == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            for r in result:
                mapped_result.append(self.mapToDict(r)) #mapToDict() turns returned array of arrays to an array of maps
            return jsonify(Users=mapped_result)