from flask import jsonify, request
from dao.Patient import PatientsDAO
from dao.Doctor import DoctorDAO
from dao.Assistant import AssistantDAO
from handler.RoleBase import RoleBase
# import datetime, time
from datetime import datetime, timezone, timedelta
import uuid

## Luis Santiago ##
class PatientHandler:

    def build_patientlist_dict(self, row):
        result = {}
        result['patientid'] = row[0]
        result['firstname'] = row[1]
        result['middlename'] = row[2]
        result['lastname'] = row[3]
        #result['ssn'] = row[4]
        #result['birthdate'] = row[5]
        #result['gender'] = row[6]
        #result['phone'] = row[7]
        result['status'] = row[8]
        #result['email'] = row[9]
        result['username'] = row[10]
        #result['Password'] = row[11]
        #result['insurancecompanyname'] = row[12]
        result['recordno'] = row[13]
        # result['consultationnoteid'] = row[14]
        # result['prescriptionid'] = row[15]
        # result['referralid'] = row[16]
        # result['resultid'] = row[17]
        # result['initialformid'] = row[18]
        return result

    def build_patientinfo_dict(self, row):
        print('row')
        print(row)
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
        result['pssword'] = row[11]
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
        result['pssword'] = pssword
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
        result['pssword'] = row[11]
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
        result['pssword'] = row[11]
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
        print ('Estoy en el update patient info')
        print('estoy en este path : ', path)
        print('Este es el form que me enviaron: ', form)
        pathlist = RoleBase().splitall(path)
        role = pathlist[1]
        DoctorSign = None
        AssistantSign = None
        if role == 'Doctor':
            DoctorSign = form['username']
        elif role == 'Assistant':
            AssistantSign = form['username']
        dao = PatientsDAO()
        patientid = form['patientid']
        row = dao.getPatientByID(patientid)
        if row == None :
            return jsonify(Error="Patient not found."), 404
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
            username = form['username']
            print('voy a tratar de acceder el pssword, si no esta exploto')
            pssword = form['pssword']
            street = form['street']
            aptno = form['aptno']
            city = form['city']
            st = form['st']
            country = form['country']
            zipcode = form['zipcode']
            deactivationdate = None
            daysofgrace = None

            if not pssword:
                pssword = dao.getPsswordByID(patientid)

            #PROBAR SOLO LOS QUE NO PUEDEN SER NULOS
            if patientid and firstname and lastname and ssn and birthdate and phone and status \
                    and street and city and country and zipcode:
                print("CALLING DAO HERE")
                dao.updatePatientInfoByID(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, status, email,
                           insurancecompanyname, username, pssword)
                dao.updatePatientAddress(patientid, street, aptno, city, st, country, zipcode)

                # History
                # changes_time = time.time()
                dateofchanges = datetime.now(timezone.utc).astimezone().strftime('%Y-%m-%d %H:%M:%S')#datetime.datetime.fromtimestamp(changes_time).strftime('%Y-%m-%d %H:%M:%S')
                # Modificado (... , AssistantSign, DoctorSign)
                dao.insertPatientHistory(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone,
                                        status, email, username, pssword, insurancecompanyname, street, aptno, city,
                                        st, country, zipcode, dateofchanges, AssistantSign, DoctorSign, deactivationdate, daysofgrace)

                result = self.update_patient_dict(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, status,
                            email, insurancecompanyname, street, aptno, city, st, country, zipcode)
                return jsonify(Patient=result), 200
            else:
                print("Unexpected attributes in update request")
                return jsonify(Error="Unexpected attributes in update request"), 400

    def updatePatientPssword(self, form):
        dao = PatientsDAO()
        patientid = form["patientid"]
        if not dao.getPatientByID(patientid):
            return jsonify(Error="Patient not found."), 404
        else:
            pssword = form['pssword']
            if pssword:
                dao.updatePatientPssword(patientid, pssword)
                result = self.update_patient_pssword_dict(patientid)
                return jsonify(Patient=result), 200
            else:
                return jsonify(Error="Unexpected attributes in update request"), 400

    def managePatientStatus(self, form, path, status):
        print ('iniciando manage patient status')
        # A-adido
        pathlist = RoleBase().splitall(path)
        role = pathlist[1]
        print ('role : ', role)
        DoctorSign = None
        AssistantSign = None
        if role == 'Doctor':
            DoctorSign = form['username']
        elif role == 'Assistant':
            AssistantSign = form['username']
            print ('assistant sign : ', AssistantSign)
        print('luego de las firmas')
        dao = PatientsDAO()
        patientid = form["patientid"]
        patient = dao.getPatientByID(patientid)
        print ('patient : ', patient)
        if not patient:
            return jsonify(Error="Patient not found."), 404
        else:
            firstname = patient[1]
            middlename = patient[2]
            lastname = patient[3]
            ssn = patient[4]
            birthdate = patient[5]
            gender = patient[6]
            phone = patient[7]
            email = patient[9]
            username = patient[10]
            pssword = patient[11]
            insurancecompanyname = patient[12]
            street = patient[14]
            aptno = patient[15]
            city = patient[16]
            st = patient[17]
            country = patient[18]
            zipcode = patient[19]
            # changes_time = time.time()

            if status == True:
                daysofgrace = None
                deactivationdate = None
            else:
                daysofgrace = form['daysofgrace']
                print ('days fo grace : ', daysofgrace)
                date = datetime.now(timezone.utc).astimezone()#datetime.datetime.fromtimestamp(changes_time)
                print('date', date)
                #deactivationdate = (date + datetime.timedelta(days=int(daysofgrace))).strftime('%Y-%m-%d %H:%M:%S')
                deactivationdate = (date + timedelta(days=int(daysofgrace))).strftime('%Y-%m-%d %H:%M:%S')
                print('deactivationdate : ', deactivationdate)

            dao.updatePatientStatus(patientid, status, deactivationdate, daysofgrace)
            # History
            changesdate = datetime.now(timezone.utc).astimezone().strftime('%Y-%m-%d %H:%M:%S')#datetime.datetime.fromtimestamp(changes_time).strftime('%Y-%m-%d %H:%M:%S')
            ## Modificado (... , DoctorSign)
            dao.insertPatientHistory(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone,
                                     status, email, username, pssword, insurancecompanyname, street, aptno, city,
                                     st, country, zipcode, changesdate, AssistantSign, DoctorSign, deactivationdate,
                                     daysofgrace)

            #hay que a-adir al history el campo de deactivationdays y creo que hay que a-adirlo al diccionario

            result = self.update_patient_dict(patientid, firstname, middlename, lastname, ssn, birthdate, gender,
                                              phone, status, email, insurancecompanyname, street, aptno, city, st,
                                              country,zipcode)
            return jsonify(Assistant=result), 200



    def insertPatient(self, form):

            print("estoy añadiendo un paciente : ", form)
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
            rle = form['role']
            recordno = form['recordno']

            #Verify if cirtical(not null) info is complete
            if firstname and lastname and ssn and birthdate and phone and username and pssword\
                    and street and city and country and zipcode \
                    and rle and recordno:
                print("Tengo toda la info requerida asi que pase el primer if")
                dao = PatientsDAO()
                doctordao = DoctorDAO()
                assistantdao = AssistantDAO()

                print("Voy a verificar el nombre completo, ssn y fecha de nacimiento a ver si no existe este paciente")
                #verify if a patient exist with this information
                existantpatient_list = dao.verifyPatient(firstname, middlename, lastname, ssn, birthdate)
                #no patient exist with this information
                if not existantpatient_list:
                    print("paciente no existe, puedo añadirlo")
                    #verify if the record number is already taken
                    if dao.getMedicalRecordByRecordno(recordno) == None:
                        print("Recordno es valido y unico")
                        #verify if username already exist
                        if dao.verifyUsername(username) == None \
                                and doctordao.verifyUsername(username) == None \
                                and assistantdao.verifyUsername(username) == None:
                            print("Username es valido y unico")
                            # patientid = uuid.uuid4()
                            #record number and username is not taken yet, Patient can be inserted
                            patientid = dao.insertPatientInfo(firstname, middlename, lastname, ssn, birthdate, gender, phone,
                                                   email, username, pssword, insurancecompanyname)
                            print("Añadi el patient info")
                            addressid = dao.insertPatientAddress(patientid, street, aptno, city, st, country, zipcode)
                            print("Añadi el patient address")
                            dao.insertMedicalRecord(recordno, patientid)
                            print("Añadi el medical record")
                            # visit_time = time.time()
                            visitdate = datetime.now(timezone.utc).astimezone().strftime('%Y-%m-%d %H:%M:%S')#datetime.datetime.fromtimestamp(visit_time).strftime('%Y-%m-%d %H:%M:%S')
                            dao.insertVisit(recordno, patientid, visitdate, type)
                            print("Añadi la visita")

                #History
                            dao.insertPatientHistory(patientid, firstname, middlename, lastname, ssn, birthdate, gender,
                                                     phone, status, email, username, pssword, insurancecompanyname, street,
                                                     aptno, city, st, country, zipcode, visitdate, None, None, None, None)
                            print("Añadi el patient history")
                            result = self.new_patient_dict(patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone,
                                                   email, username, pssword, addressid, street, aptno, city, st, country,
                                                   zipcode, insurancecompanyname, recordno)
                            print("Patient added correctly")
                            return jsonify(Success="Patient added correctly", New_Patient=result), 201

                            # return jsonify(Success="Patient added correctly")

                        #username already exist
                        else:
                            print("Username is already taken.")
                            return jsonify(Error="Username is already taken.")

                    #record number already taken
                    else:

                        #get patient info with this record number
                        patient = dao.getPatientByRecordno(recordno)
                        result = self.patient_byrecordno_dict(patient)
                        print("Record Number is already taken.")
                        return jsonify(Error="Record Number is already taken.", Patient=result)

                #a patient with this info already exists
                else:
                    print("A Patient with this information already exist.")
                    #return patient or patients with this critical information
                    result_list = []
                    for row in existantpatient_list:
                        result_list.append(self.verify_existantpatient_dict(row))
                    return jsonify(Error="A Patient with this information already exist.", Patients=result_list)

            #some critical information missing
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400