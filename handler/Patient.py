from flask import jsonify, request
from dao.Patient import PatientsDAO
import datetime, time

## Luis Santiago ##
class PatientHandler:

    def build_patientlist_Dict(self,row):
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
        result['recordno'] = row[12]
        result['consultationnoteid'] = row[13]
        result['prescriptionid'] = row[14]
        result['referralid'] = row[15]
        result['resultid'] = row[16]
        result['initialformid'] = row[17]
        result['insurancecompanyid'] = row[18]
        result['companyname'] = row[19]
        return result

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
        result['addressid'] = row[12]
        result['street'] = row[13]
        result['aptno'] = row[14]
        result['city'] = row[15]
        result['st'] = row[16]
        result['country'] = row[17]
        result['zipcode'] = row[18]
        result['recordno'] = row[19]
        result['consultationnoteid'] = row[20]
        result['prescriptionid'] = row[21]
        result['referralid'] = row[22]
        result['resultid'] = row[23]
        result['initialformid'] = row[24]
        result['insurancecompanyid'] = row[25]
        result['companyname'] = row[26]
        return result

    def update_patient_Dict(self,row):
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
        result['addressid'] = row[12]
        result['street'] = row[13]
        result['aptno'] = row[14]
        result['city'] = row[15]
        result['st'] = row[16]
        result['country'] = row[17]
        result['zipcode'] = row[18]
        result['insurancecompanyid'] = row[19]
        result['companyname'] = row[20]
        return result

    def new_patient_Dict(self, row):
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
        result['addressid'] = row[12]
        result['street'] = row[13]
        result['aptno'] = row[14]
        result['city'] = row[15]
        result['st'] = row[16]
        result['country'] = row[17]
        result['zipcode'] = row[18]
        result['insurancecompanyid'] = row[19]
        result['companyname'] = row[20]
        result['recordno'] = row[21]
        return result

    def getAllPatients(self):
        dao = PatientsDAO()
        patient_list = dao.getAllPatients()
        result_list = []
        for row in patient_list:
            result_list.append(self.build_patientlist_Dict(row)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Patient=result_list)

    def getPatientByID(self, args):
        pid = args.get("patientid")
        dao = PatientsDAO()
        row = dao.getPatientByID(int(pid))
        if row == None:
            return jsonify(Error="Patient NOT FOUND"),404
        else:
            patient = self.build_patientinfo_Dict(row) #mapToDict() turns returned array of arrays to an array of maps
            return jsonify(Patient=patient)

    def updatePatientInformation(self, args, form):
        pid = args.get("patientid")
        dao = PatientsDAO()
        if not dao.getPatientByID(pid):
            return jsonify(Error="Patient not found."), 404
        else:
            if len(form) != 21:
                return jsonify(Error="Malformed update request"), 400
            else:
                patientid = form['patientid']
                firstname = form['firstname']
                middlename = form['middlename']
                lastname = form['lastname']
                ssn = form['ssn']
                birthdate = form['birthdate']
                gender = form['gender']
                phone = form['phone']
                status = form['status']
                email = form['email']
                username = form['username']
                pssword = form['pssword']
                addressid = form['addressid']
                street = form['street']
                aptno = form['aptno']
                city = form['city']
                st = form['st']
                country = form['country']
                zipcode = form['zipcode']
                insurancecompanyid = form['insurancecompanyid']
                companyname = form['companyname']

                if patientid and firstname and middlename and lastname and ssn and birthdate and gender and phone and status \
                        and email and username and pssword and addressid and street and aptno and city and st and country \
                        and zipcode and insurancecompanyid and companyname:

                    dao.updatePatientInfoByID(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, status, email,
                               username, pssword)
                    dao.UpdatePatientAddress(addressid, patientid, street, aptno, city, st, country, zipcode)

                    newinsurancecompanyid = dao.getInsuranceCompanyID(companyname)
                    if newinsurancecompanyid == None:
                        return jsonify(Error="INSURANCE COMPANY NOT FOUND"), 404
                    else:
                        result = dao.updatePatientInsuranceCompany(newinsurancecompanyid, patientid)
                        if result == None:
                            return jsonify(Error="UPDATE ERROR"), 404

                    result = self.update_patient_Dict(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, status, email,
                               username, pssword, addressid, street, aptno, city, st, country, zipcode, insurancecompanyid, companyname)
                    return jsonify(Patient=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def insertPatient(self, form):
        if len(form) != 22:
            return jsonify(Error="Malformed post request"), 400
        else:
            recordno = form['recordno']
            firstname = form['firstname']
            middlename = form['middlename']
            lastname = form['lastname']
            ssn = form['ssn']
            birthdate = form['birthdate']
            gender = form['gender']
            phone = form['phone']
            status = form['status']
            email = form['email']
            username = form['username']
            pssword = form['pssword']
            street = form['street']
            aptno = form['aptno']
            city = form['city']
            st = form['st']
            country = form['country']
            zipcode = form['zipcode']
            insurancecompanyid = form['insurancecompanyid']
            companyname = form['companyname']
            type = form['type']
            if recordno and firstname and middlename and lastname and ssn and birthdate and gender and phone and status \
                    and email and username and pssword and street and aptno and city and st and country \
                    and zipcode and insurancecompanyid and companyname and type:
                dao = PatientsDAO()

                patientid = dao.insertPatientInfo(firstname, middlename, lastname, ssn, birthdate, gender, phone, status,
                                       email, username, pssword, insurancecompanyid)
                addressid = dao.insertPatientAddress(street, aptno, city, st, country, zipcode)

                dao.insertMedicalRecord(recordno, patientid)

                visit_time = time.time()
                visitdate = datetime.datetime.fromtimestamp(visit_time).strftime('%Y-%m-%d %H:%M:%S')
                dao.insertVisit(recordno, patientid, visitdate, type)

                result = self.new_patient_Dict(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, status,
                                       email, username, pssword, addressid, street, aptno, city, st, country,
                                       zipcode, insurancecompanyid, companyname, recordno)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400