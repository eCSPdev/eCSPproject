from flask import jsonify, request
from dao.Prescription import PrescriptionDAO
from dao.s3connection import s3Connection
# import datetime, time
from datetime import datetime, timezone
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

    def build_presinsert_dict(self, prescriptionid, filename, assistantusername, doctorusername, dateofupload, patientid, recordno):
        result = {}
        result['prescriptionid'] = prescriptionid
        result['filename'] = filename
        result['assistantusername'] = assistantusername
        result['doctorusername'] = doctorusername
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

    def insertPrescription(self, args, file):
        dao = PrescriptionDAO()
        # filepath = file  # this is the file to insert
        filename = args.get("filename")  # form['filename']
        assistantusername = args.get("assistantusername")  # form['assistantusername']
        doctorusername = args.get("doctorusername")  # form['doctorusername']
        patientid = args.get("patientid")  # form['patientid']
        recordno = args.get("recordno")  # form['recordno']

        # print("args : ", args)
        print("filename : ", filename)
        print("assistantusername : ", assistantusername)
        print("doctorusername : ", doctorusername)
        print("patientid : ", patientid)
        print("recordno : ", recordno)
        print("file : ", file)

        # return jsonify(Success="Consultation Node inserted."), 201

        upload_time = datetime.now(timezone.utc).astimezone()#time.time()
        dateofupload = datetime.datetime.fromtimestamp(upload_time).strftime('%Y-%m-%d %H:%M:%S')

        if file and dateofupload and recordno:

            if str(dao.verifyRecordno(recordno)) == str(patientid):

                prescriptionid = dao.insertPrescription(filename, assistantusername, doctorusername, dateofupload, patientid, recordno)

                s3 = s3Connection()
                targetlocation = 'prescriptions/' + str(prescriptionid) + filename
                print("target location : ", targetlocation)
                #ELIMINAR EL LINK
                link = s3.uploadfile(file, targetlocation)  # returns the url after storing it
                print("link : ", link)

                result = self.build_presinsert_dict(prescriptionid, filename, assistantusername, doctorusername, dateofupload, patientid, recordno)
                return jsonify(Success="Prescription inserted.", Prescription = result), 201 #Verificar porque 201
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