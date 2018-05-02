from flask import jsonify, request
from dao.Doctor import DoctorDAO
from dao.Patient import PatientsDAO
from dao.Assistant import AssistantDAO

## Coralis Camacho##
class DoctorHandler:

    def build_doctorlist_dict(self,row):
        result = {}
        result['doctorid'] = row[0]
        result['licenseno'] = row[1]
        result['firstname'] = row[2]
        result['middlename'] = row[3]
        result['lastname'] = row[4]
        result['officename'] = row[5]
        result['phone'] = row[6]
        result['status'] = row[7]
        result['email'] = row[8]
        result['username'] = row[9]
        result['pssword'] = row[10]
        return result


    def build_doctorinformation_dict(self,row):
        result = {}
        result['doctorid'] = row[0]
        result['licenseno'] = row[1]
        result['firstname'] = row[2]
        result['middlename'] = row[3]
        result['lastname'] = row[4]
        result['officename'] = row[5]
        result['phone'] = row[6]
        result['status'] = row[7]
        result['email'] = row[8]
        result['username'] = row[9]
        result['pssword'] = row[10]
        result['addressid'] = row[11]
        result['street'] = row[12]
        result['aptno'] = row[13]
        result['city'] = row[14]
        result['st'] = row[15]
        result['country'] = row[16]
        result['zipcode'] = row[17]
        return result

    def update_doctor_dict(self,doctorid, licenseno, firstname, middlename, lastname, officename, phone, status,
                                 email, street, aptno, city, st, country, zipcode):
        result = {}
        result['doctorid'] = doctorid
        result['licenseno'] = licenseno
        result['firstname'] = firstname
        result['middlename'] = middlename
        result['lastname'] = lastname
        result['officename'] = officename
        result['phone'] = phone
        result['status'] = status
        result['email'] = email
        result['street'] = street
        result['aptno'] = aptno
        result['city'] = city
        result['st'] = st
        result['country'] = country
        result['zipcode'] = zipcode
        return result

    def build_doctorhistory_dict(self, doctorid, licenseno, firstname, middlename, lastname, officename, phone, status,
                                 email, username, pssword, street, aptno, city, st, country, zipcode):
        result = {}
        result['doctorid'] = doctorid
        result['licenseno'] = licenseno
        result['firstname'] = firstname
        result['middlename'] = middlename
        result['lastname'] = lastname
        result['officename'] = officename
        result['phone'] = phone
        result['status'] = status
        result['email'] = email
        result['username'] = username
        result['pssword'] = pssword
        result['street'] = street
        result['aptno'] = aptno
        result['city'] = city
        result['st'] = st
        result['country'] = country
        result['zipcode'] = zipcode
        return result

    def new_doctor_dict(self, doctorid, firstname, middlename, lastname, officename, phone, status, email,
                           username, pssword, addressid, street, aptno, city, st, country, zipcode):
        result = {}
        result['doctorid'] = doctorid
        result['firstname'] = firstname
        result['middlename'] = middlename
        result['lastname'] = lastname
        result['officename'] = officename
        result['phone'] = phone
        result['status'] = status
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
        return result

    def verify_existantdoctor_dict(self, row):
        result = {}
        result['doctorid'] = row[0]
        result['licenseno'] = row[1]
        result['firstname'] = row[2]
        result['middlename'] = row[3]
        result['lastname'] = row[4]
        result['officename'] = row[5]
        result['phone'] = row[6]
        result['status'] = row[7]
        result['email'] = row[8]
        result['username'] = row[9]
        result['addressid'] = row[10]
        result['street'] = row[11]
        result['aptno'] = row[12]
        result['city'] = row[13]
        result['st'] = row[14]
        result['country'] = row[15]
        result['zipcode'] = row[16]
        return result

    def update_doctor_pssword_dict(self, row):
        result = {}
        result['doctorid'] = row[0]
        return result

    def getAllDoctor(self):
        dao = DoctorDAO()
        result = dao.getAllDoctor()
        result_list = []
        for row in result:
            result_list.append(self.build_doctorlist_dict(row))
        return jsonify(Doctor=result_list)

    def getDoctorByID(self, args):
        doctorid = args.get("doctorid")
        dao = DoctorDAO()
        row = dao.getDoctorByID(doctorid)
        if row == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            doctor = self.build_doctorinformation_dict(row)
            return jsonify(Doctor = doctor)

    def updateDoctorInformation(self,form):
        dao = DoctorDAO()
        doctorid = form["doctorid"]
        if not dao.getDoctorByID(doctorid):
            return jsonify(Error="Doctor not found."), 404
        else:
            if len(form) != 15:
                return jsonify(Error="Malformed update request"), 400
            else:
                doctorid = form['doctorid']
                licenseno = form['licenseno']
                firstname = form['firstname']
                middlename = form['middlename']
                lastname = form['lastname']
                officename = form['officename']
                phone = form['phone']
                status = form['status']
                email = form['email']
                street = form['street']
                aptno = form['aptno']
                city = form['city']
                st = form['st']
                country = form['country']
                zipcode = form['zipcode']
                if doctorid and licenseno and firstname and lastname and officename and phone and status \
                        and street and aptno and city and country and zipcode:
                    dao.updateDoctorInfoByID(doctorid, licenseno, firstname, middlename, lastname, officename, phone,
                                             status, email)
                    dao.updateDoctorAddress(doctorid, street, aptno, city, st, country, zipcode)
                    result = self.update_doctor_dict(doctorid, licenseno, firstname, middlename, lastname, officename,
                                                     phone, status, email, street, aptno,
                                                    city, st, country, zipcode)
                    return jsonify(Doctor = result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400



    def insertDoctor(self, form):
        if len(form) != 16:
            return jsonify(Error="Malformed post request"), 400
        else:
            licenseno = form['licenseno']
            firstname = form['firstname']
            middlename = form['middlename']
            lastname = form['lastname']
            officename = form['officename']
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
            if licenseno and firstname and lastname and officename and phone and status and username and pssword \
                    and street and aptno and city and country and zipcode:
                dao = DoctorDAO()
                patientdao = PatientsDAO()
                assistantdao = AssistantDAO()

                # verify if a doctor exist with this information
                existantdoctor_list = dao.verifyDoctor(firstname, middlename, lastname, licenseno)

                # no doctor exist with this information
                if not existantdoctor_list:
                    # verify if username already exist
                    if dao.verifyUsername(username) == None \
                            and patientdao.verifyUsername(username) == None \
                            and assistantdao.verifyUsername(username) == None:

                        # license number and username is not taken yet, Doctor can be inserted
                        doctorid = dao.insertDoctorInfo(licenseno, firstname, middlename, lastname, officename, phone,
                                                     email, username, pssword)
                        addressid = dao.insertDoctorAddress(doctorid, street, aptno, city, st, country, zipcode)

                        result = self.new_doctor_dict(doctorid, firstname, middlename, lastname, officename, phone, status,
                                                       email, username, pssword, addressid, street, aptno, city, st, country, zipcode)
                        return jsonify(Success="Doctor added correctly", Doctor=result), 201

                        # return jsonify(Success="Doctor added correctly")
                    # username already exist
                    else:
                        return jsonify(Error="Username is already taken.")

                # a patient with this info already exists
                else:
                    # return doctor or doctors with this critical information
                    result_list = []
                    for row in existantdoctor_list:
                        result_list.append(self.verify_existantdoctor_dict(row))
                    return jsonify(Error="A Doctor with this information already exist.", Doctors=result_list)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateDoctorPssword(self, form):
        dao = DoctorDAO()
        doctorid = form["doctorid"]
        if not dao.getDoctorByID(doctorid):
            return jsonify(Error="Doctor not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                pssword = form['pssword']
                if pssword:
                    dao.updateDoctorPssword(doctorid, pssword)
                    result = self.update_doctor_pssword_dict(doctorid)
                    return jsonify(Doctor=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

########## Doctor History #############
#Para hacerle insert al history del Doctor

    def insertDoctorHistory(self, form):
        dao = DoctorDAO()
        if len(form) != 17:
            return jsonify(Error="Malformed insert request"), 400
        else:
            doctorid = form['doctorid']
            licenseno = form['liceseno']
            firstname = form['firstname']
            middlename = form['middlename']
            lastname = form['lastname']
            officename = form['officename']
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
            if doctorid and licenseno and firstname and lastname and officename and phone and status and username and \
                    pssword and street and aptno and city and country and zipcode:
                dao.insertDoctorHistory(doctorid, licenseno, firstname, middlename, lastname, officename, phone, status,
                                        email, username, pssword, street, aptno, city, st, country, zipcode)
                result = self.build_doctorhistory_dict(doctorid, licenseno, firstname, middlename, lastname, officename,
                                                       phone, status, email, username, pssword, street, aptno, city, st,
                                                       country, zipcode)
                return jsonify(History = result), 201 #Verificar porque 201
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400