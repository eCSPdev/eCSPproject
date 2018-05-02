from flask import jsonify, request
from dao.Prescription import PrescriptionDAO

class PrescriptionHandler:

    def build_prescriptionlist_dict(self,row):
        result = {}
        result['prescriptionid'] = row[0]
        result['prescription'] = row[1]
        result['assistantid'] = row[2]
        result['doctorid'] = row[2]
        result['dateofupload'] = row[4]
        result['patientid'] = row[5]
        return result

    def build_presinsert_dict(self, prescription, assistantid, doctorid, dateofupload, patientid):
        result = {}
        result['prescription'] = prescription
        result['assistantid'] = assistantid
        result['doctorid'] = doctorid
        result['dateofupload'] = dateofupload
        result['patientid'] = patientid
        return result

    def getPatientPrescription(self, args):
        pid = args.get("patientid")
        dao = PrescriptionDAO()
        prescription_list = dao.getPatientPrescription(pid)
        result_list = []
        if not prescription_list:
            return jsonify(Error="NOT FOUND"),404
        for row in prescription_list:
            result = self.build_prescriptionlist_dict(row)
            result_list.append(result) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Prescription=result_list)

    def getPrescriptionByID(self, args):
        pid = args.get("patientid")
        preid = args.get("prescriptionid")
        dao = PrescriptionDAO()
        row = dao.getPrescriptionByID(pid, preid)
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            result = self.build_prescriptionlist_dict(row[0])
            return jsonify(Prescription=result)

    def insertPrescription(self, form):
        dao = PrescriptionDAO()
        if len(form) != 5:
            return jsonify(Error="Malformed insert request"), 400
        else:
            prescription = form['prescription']
            assistantid = form['assistantid']
            doctorid = form['doctorid']
            dateofupload = form['dateofupload']
            patientid = form['patientid']
            recordno = form['recordno']
            if prescription and dateofupload and recordno:
                if dao.verifyRecordno(recordno) != None:
                    dao.insertPrescription(prescription, assistantid, doctorid, dateofupload, patientid)
                    result = self.build_presinsert_dict(prescription, assistantid, doctorid, dateofupload, patientid)
                    return jsonify(Prescription = result), 201 #Verificar porque 201
                else:
                    return jsonify(Error="Record Number does not exist.", RecordNo=recordno), 400
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400