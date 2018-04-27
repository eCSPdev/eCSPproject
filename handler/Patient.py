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
        result['insurancecompanyname'] = row[12]
        result['recordno'] = row[13]
        result['consultationnoteid'] = row[14]
        result['prescriptionid'] = row[15]
        result['referralid'] = row[16]
        result['resultid'] = row[17]
        result['initialformid'] = row[18]
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
        result['insurancecompanyname'] = row[12]
        result['addressid'] = row[13]
        result['street'] = row[14]
        result['aptno'] = row[15]
        result['city'] = row[16]
        result['st'] = row[17]
        result['country'] = row[18]
        result['zipcode'] = row[19]
        result['recordno'] = row[20]
        result['consultationnoteid'] = row[21]
        result['prescriptionid'] = row[22]
        result['referralid'] = row[23]
        result['resultid'] = row[24]
        result['initialformid'] = row[25]
        return result

    def update_patient_Dict(self, patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, status,
                            email, username, insurancecompanyname, street, aptno, city, st, country, zipcode):
        result = {}
        result['patientid'] = patientid
        result['firstname'] = firstname
        result['middlename'] = middlename
        result['lastname'] = lastname
        result['ssn'] = ssn
        result['birthdate'] = birthdate
        result['gender'] = gender
        result['phone'] = phone
        result['status'] = status
        result['email'] = email
        result['username'] = username
        result['insurancecompanyname'] = insurancecompanyname
        result['street'] = street
        result['aptno'] = aptno
        result['city'] = city
        result['st'] = st
        result['country'] = country
        result['zipcode'] = zipcode
        return result

    def new_patient_Dict(self, patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone,
                         email, username, pssword, addressid, street, aptno, city, st, country,zipcode,
                         insurancecompanyname, recordno):
        result = {}
        result['patientid'] = patientid
        result['firstname'] = firstname
        result['middlename'] = middlename
        result['lastname'] = lastname
        result['ssn'] = ssn
        result['birthdate'] = birthdate
        result['gender'] = gender
        result['phone'] = phone
        result['email'] = email
        result['username'] = username
        result['Password'] = pssword
        result['addressid'] = addressid
        result['street'] = street
        result['aptno'] = aptno
        result['city'] = city
        result['st'] = st
        result['country'] = country
        result['zipcode'] = zipcode
        result['insurancecompanyname'] = insurancecompanyname
        result['recordno'] = recordno
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

    def updatePatientInformation(self, form):
        try:
            dao = PatientsDAO()
            patientid = form['patientid']
            row = dao.getPatientByID(patientid)
            if row == None :
                return jsonify(Error="Patient not found."), 404
            else:
                if len(form) != 18:
                    return jsonify(Error="Malformed update request"), 400
                else:
                    print('length of form : ', len(form))
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
                    insurancecompanyname = form['insurancecompanyname']
                    street = form['street']
                    aptno = form['aptno']
                    city = form['city']
                    st = form['st']
                    country = form['country']
                    zipcode = form['zipcode']

                    #PROBAR SOLO LOS QUE NO PUEDEN SER NULOS
                    if patientid and firstname and lastname and ssn and birthdate and phone and status \
                            and username and street and aptno and city and country and zipcode:
                        print("CALLING DAO HERE")
                        dao.updatePatientInfoByID(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, status, email,
                                   username, insurancecompanyname)
                        dao.updatePatientAddress(patientid, street, aptno, city, st, country, zipcode)

                        result = self.update_patient_Dict(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, status,
                                    email, username, insurancecompanyname, street, aptno, city, st, country, zipcode)
                        return jsonify(Patient=result), 200
                    else:
                        return jsonify(Error="Unexpected attributes in update request"), 400
        except Exception as ex:
            print('{}'.format(ex))

    def updatePatientPassword(self):
        return 'IN PROCESS YET'

    def insertPatient(self, form):
        if len(form) != 19:
            return jsonify(Error="Malformed post request"), 400
        else:
            print('length of form : ', len(form))
            print('form : ', form)
            firstname = form['firstname']
            middlename = form['middlename']
            lastname = form['lastname']
            ssn = form['ssn']
            birthdate = form['birthdate']
            gender = form['gender']
            phone = form['phone']
            email = form['email']
            username = form['username']
            pssword = form['pssword']
            insurancecompanyname = form['insurancecompanyname']
            street = form['street']
            aptno = form['aptno']
            city = form['city']
            st = form['st']
            country = form['country']
            zipcode = form['zipcode']
            type = form['type']
            recordno = form['recordno']
            if firstname and lastname and ssn and birthdate and phone and username and pssword\
                    and pssword and street and aptno and city and country and zipcode \
                    and insurancecompanyname and type and recordno:
                dao = PatientsDAO()
                patientid = dao.insertPatientInfo(firstname, middlename, lastname, ssn, birthdate, gender, phone,
                                       email, username, pssword, insurancecompanyname)
                print('zipcode : ', zipcode)
                addressid = dao.insertPatientAddress(patientid, street, aptno, city, st, country, zipcode)
                dao.insertMedicalRecord(recordno, patientid)
                visit_time = time.time()
                visitdate = datetime.datetime.fromtimestamp(visit_time).strftime('%Y-%m-%d %H:%M:%S')
                dao.insertVisit(recordno, patientid, visitdate, type)
                result = self.new_patient_Dict(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone,
                                       email, username, pssword, addressid, street, aptno, city, st, country,
                                       zipcode, insurancecompanyname, recordno)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    #PENDING
    def verifyPatient(self, firstname, lastname, ssn, birthdate, gender, status):
        dao = PatientsDAO()
        result = dao.VerifyPatient(firstname, lastname, ssn, birthdate, gender, status)