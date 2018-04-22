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

    def build_presinsert_dict(self,row):
        result = {}
        result['prescription'] = row[0]
        result['assistantid'] = row[1]
        result['doctorid'] = row[2]
        result['dateofupload'] = row[3]
        result['patientid'] = row[4]
        return result

    def getPatientPrescription(self, args):
        pid = args.get("patientid")
        dao = PrescriptionDAO()
        prescription_list = dao.getAllPrescription(pid)
        result_list = []
        for row in prescription_list:
            result = self.build_prescriptionlist_dict(row)
            result_list.append(result) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Prescription=result_list)

    def getPrescriptionByID(self, args):
        pid = args.get("patientid")
        preid = args.get("prescriptionid")
        dao = PrescriptionDAO()
        row = dao.getPrescriptionByID(int(pid), int(preid))
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            result = self.build_prescriptionlist_dict(row)
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
            if prescription and assistantid and doctorid and dateofupload and patientid:
                dao.insertPrescription(prescription, assistantid, doctorid, dateofupload, patientid)
                result = self.build_presinsert_dict(prescription, assistantid, doctorid, dateofupload, patientid)
                return jsonify(Prescription = result), 201 #Verificar porque 201
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400