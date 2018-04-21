from flask import jsonify, request
from dao.Patient import PatientsDAO

## Luis Santiago ##
class PatientHandler:

    def build_patientinfo_Dict(self,row):
        result = {}
        result['patientid'] = row[0]
        result['firstname'] = row[1]
        result['middlename'] = row[2]
        result['lastname'] = row[3]
        result['ssn'] = row[4]
        result['birthdate'] = row[5]
        result['gender'] = row[6]
        result['phone'] = row[7]
        result['status'] = row[8]
        result['email'] = row[9]
        result['username'] = row[10]
        result['Password'] = row[11]
        return result

    def getAllPatients(self):
        dao = PatientsDAO()
        patient_list = dao.getAllPatients()
        result_list = []
        for row in patient_list:
            result_list.append(self.build_patientinfo_Dict(row)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Users=result_list)

    def getPatientByID(self, args):
        pid = args.get("patientid")
        dao = PatientsDAO()
        print ('este es el pid: ' + pid)
        row = dao.getPatientByID(int(pid))
        if row == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            patient = self.build_patientinfo_Dict(row) #mapToDict() turns returned array of arrays to an array of maps
            return jsonify(Users=patient)