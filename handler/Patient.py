from flask import jsonify, request
from dao.Patient import PatientsDAO
from dao.Doctor import DoctorDAO
from dao.Assistant import AssistantDAO
from handler.RoleBase import RoleBase
import datetime, time

## Luis Santiago ##
class PatientHandler:

    def build_patientlist_dict(self, row):
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
        # result['consultationnoteid'] = row[14]
        # result['prescriptionid'] = row[15]
        # result['referralid'] = row[16]
        # result['resultid'] = row[17]
        # result['initialformid'] = row[18]
        return result

    def build_patientinfo_dict(self, row):
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
        # result['consultationnoteid'] = row[21]
        # result['prescriptionid'] = row[22]
        # result['referralid'] = row[23]
        # result['resultid'] = row[24]
        # result['initialformid'] = row[25]
        return result

    def update_patient_dict(self, patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, status,
                            email, insurancecompanyname, street, aptno, city, st, country, zipcode):
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
        result['insurancecompanyname'] = insurancecompanyname
        result['street'] = street
        result['aptno'] = aptno
        result['city'] = city
        result['st'] = st
        result['country'] = country
        result['zipcode'] = zipcode
        return result

    def new_patient_dict(self, patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone,
                         email, username, pssword, addressid, street, aptno, city, st, country, zipcode,
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

    def verify_existantpatient_dict(self, row):
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
        return result

    def patient_byrecordno_dict(self, row):
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
        # result['consultationnoteid'] = row[21]
        # result['prescriptionid'] = row[22]
        # result['referralid'] = row[23]
        # result['resultid'] = row[24]
        # result['initialformid'] = row[25]
        return result

    def update_patient_pssword_dict(self, row):
        result = {}
        result['patientid'] = row[0]
        return result

    def getAllPatients(self):
        dao = PatientsDAO()
        patient_list = dao.getAllPatients()
        print('patient_list : ',patient_list)
        result_list = []
        for row in patient_list:
            result_list.append(self.build_patientlist_dict(row)) #mapToDict() turns returned array of arrays to an array of maps
        return jsonify(Patient=result_list)

    def getPatientByID(self, args):
        pid = args.get("patientid")
        dao = PatientsDAO()
        row = dao.getPatientByID(int(pid))
        if row == None:
            return jsonify(Error="Patient NOT FOUND"),404
        else:
            patient = self.build_patientinfo_dict(row) #mapToDict() turns returned array of arrays to an array of maps
            return jsonify(Patient=patient)

    def getPatientToken(self, patientid):

        dao = PatientsDAO()
        token = dao.getPatientToken(int(patientid))
        if token == None:
            return jsonify(Error="Token NOT FOUND for that Patient ID")
        else:
            return jsonify(Token=token)

    def updatePatientInformation(self, form, path):
        # A-adido
        pathlist = RoleBase().splitall(path)
        role = pathlist[1]
        DoctorSign = None
        AssistantSign = None
        if role == 'Doctor':
            DoctorSign = form['username']
        elif role == 'Assistant':
            AssistantSign = form['username']
        #
        print ('Estoy en el update')
        dao = PatientsDAO()
        #print ('antes del DAO')
        print('form : ', form)
        patientid = form['patientid']
        print ('patientid : ', patientid)
        row = dao.getPatientByID(patientid)
        print ('estoy antes del primer if')
        if row == None :
            return jsonify(Error="Patient not found."), 404
        else:
            if len(form) != 19:
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
                insurancecompanyname = form['insurancecompanyname']
                print (insurancecompanyname)
                username = ['username']
                pssword = ['pssword']
                street = form['street']
                print (street)
                aptno = form['aptno']
                print(aptno)
                city = form['city']
                print (city)
                st = form['st']
                print (st)
                country = form['country']
                print (country)
                zipcode = form['zipcode']
                print (zipcode)
                print ('antes del segundo if')

                if pssword == None:
                    pssword = dao.getPsswordByID(patientid)

                #PROBAR SOLO LOS QUE NO PUEDEN SER NULOS
                if patientid and firstname and lastname and ssn and birthdate and phone and status \
                        and street and aptno and city and country and zipcode:
                    print("CALLING DAO HERE")
                    dao.updatePatientInfoByID(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, status, email,
                               insurancecompanyname)
                    dao.updatePatientAddress(patientid, street, aptno, city, st, country, zipcode)

            # History
                    changes_time = time.time()
                    changesdate = datetime.datetime.fromtimestamp(changes_time).strftime('%Y-%m-%d %H:%M:%S')
                    # Modificado (... , AssistantSign, DoctorSign)
                    dao.insertPatientHistory(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone,
                                            status, email, username, pssword, insurancecompanyname, street, aptno, city,
                                            st, country, zipcode, changesdate, AssistantSign, DoctorSign)

                    result = self.update_patient_dict(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, status,
                                email, insurancecompanyname, street, aptno, city, st, country, zipcode)
                    return jsonify(Patient=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def updatePatientPssword(self, form):
        dao = PatientsDAO()
        patientid = form["patientid"]
        if not dao.getPatientByID(patientid):
            return jsonify(Error="Patient not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                pssword = form['pssword']
                if pssword:
                    dao.updatePatientPssword(patientid, pssword)
                    result = self.update_patient_pssword_dict(patientid)
                    return jsonify(Patient=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400


    def insertPatient(self, form):
        if len(form) != 20:
            return jsonify(Error="Malformed post request"), 400
        else:
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
            insurancecompanyname = form['insurancecompanyname']
            street = form['street']
            aptno = form['aptno']
            city = form['city']
            st = form['st']
            country = form['country']
            zipcode = form['zipcode']
            type = form['type']
            recordno = form['recordno']

            #Verify if cirtical(not null) info is complete
            if firstname and lastname and ssn and birthdate and phone and username and pssword\
                    and street and aptno and city and country and zipcode and insurancecompanyname \
                    and type and recordno:

                dao = PatientsDAO()
                doctordao = DoctorDAO()
                assistantdao = AssistantDAO()

                #verify if a patient exist with this information
                existantpatient_list = dao.verifyPatient(firstname, middlename, lastname, ssn, birthdate)
                #no patient exist with this information
                if not existantpatient_list:

                    #verify if the record number is already taken
                    if dao.getMedicalRecordByRecordno(recordno) == None:

                        #verify if username already exist
                        if dao.verifyUsername(username) == None \
                                and doctordao.verifyUsername(username) == None \
                                and assistantdao.verifyUsername(username) == None:

                            #record number and username is not taken yet, Patient can be inserted
                            patientid = dao.insertPatientInfo(firstname, middlename, lastname, ssn, birthdate, gender, phone,
                                                   email, username, pssword, insurancecompanyname)
                            addressid = dao.insertPatientAddress(patientid, street, aptno, city, st, country, zipcode)
                            dao.insertMedicalRecord(recordno, patientid)
                            visit_time = time.time()
                            visitdate = datetime.datetime.fromtimestamp(visit_time).strftime('%Y-%m-%d %H:%M:%S')
                            dao.insertVisit(recordno, patientid, visitdate, type)

                #History
                            dao.insertPatientHistory(patientid, firstname, middlename, lastname, ssn, birthdate, gender,
                                                     phone, status, email, username, pssword, insurancecompanyname, street,
                                                     aptno, city, st, country, zipcode, visitdate)

                            result = self.new_patient_dict(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone,
                                                   email, username, pssword, addressid, street, aptno, city, st, country,
                                                   zipcode, insurancecompanyname, recordno)
                            return jsonify(Success="Patient added correctly", New_Patient=result), 201

                            # return jsonify(Success="Patient added correctly")

                        #username already exist
                        else:
                            return jsonify(Error="Username is already taken.")

                    #record number already taken
                    else:

                        #get patient info with this record number
                        patient = dao.getPatientByRecordno(recordno)
                        result = self.patient_byrecordno_dict(patient)
                        return jsonify(Error="Record Number is already taken.", Patient=result)

                #a patient with this info already exists
                else:

                    #return patient or patients with this critical information
                    result_list = []
                    for row in existantpatient_list:
                        result_list.append(self.verify_existantpatient_dict(row))
                    return jsonify(Error="A Patient with this information already exist.", Patients=result_list)

            #some critical information missing
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400