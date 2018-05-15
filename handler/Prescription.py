from flask import jsonify, request
from dao.Prescription import PrescriptionDAO
from dao.s3connection import s3Connection

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

    def build_presinsert_dict(self, prescriptionid, prescriptionlink, assistantid, doctorid, dateofupload, patientid, recordno):
        result = {}
        result['prescriptionid'] = prescriptionid
        result['prescription'] = prescriptionlink
        result['assistantid'] = assistantid
        result['doctorid'] = doctorid
        result['dateofupload'] = dateofupload
        result['patientid'] = patientid
        result['recordno'] = recordno
        return result

    def build_pdates_dict(self, row):
        result = {}
        result['year'] = row[0]
        result['month'] = row[1]
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
            targetlocation = "prescriptions/"
            if prescription and dateofupload and recordno:
                if dao.verifyRecordno(recordno) != None:

                    s3 = s3Connection()
                    prescriptionlink = s3.uploadfile(prescription, targetlocation)  # returns the url after storing it

                    prescriptionid = dao.insertPrescription(prescriptionlink, assistantid, doctorid, dateofupload, patientid, recordno)
                    result = self.build_presinsert_dict(prescriptionid, prescriptionlink, assistantid, doctorid, dateofupload, patientid, recordno)
                    return jsonify(Prescription = result), 201 #Verificar porque 201
                else:
                    return jsonify(Error="Record Number does not exist.", RecordNo=recordno), 400
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400

    def getPrescriptionDates(self, args):
        print('estoy en el Pres Dates')
        pid = args.get("patientid")
        dao = PrescriptionDAO()
        prescription_list = dao.getPrescriptionDates(pid)
        result_list = []
        if not prescription_list:
            return jsonify(Error="NOT FOUND"),404
        for row in prescription_list:
            result = self.build_pdates_dict(row)
            result_list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(PrescriptionDates=result_list)