from flask import jsonify, request
from dao.Doctor import DoctorDAO

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


    def build_doctor_dict(self,row):
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

    def getAllDoctor(self):
        dao = DoctorDAO()
        result = dao.getAllDoctor()
        result_list = []
        for r in result:
            result = self.build_doctorlist_dict(r)
            result.append(result)
        return jsonify(Doctor=result_list)

    def getDoctorByID(self, args):
        dao = DoctorDAO()
        did = int(args.get("doctorid"))
        row = dao.getAssistantByID(did)
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            doctor = self.build_doctor_dict(row)
            return jsonify(Doctor = doctor)

    def updateDoctorInformation(self, args, form):
        dao = DoctorDAO()
        did = args.get("doctorid")
        if not dao.getDoctorByID(did):
            return jsonify(Error="Part not found."), 404
        else:
            if len(args) != 18:
                return jsonify(Error="Malformed update request"), 400
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
                addressid = form['addressid']
                street = form['street']
                aptno = form['aptno']
                city = form['city']
                st = form['st']
                country = form['country']
                zipcode = form['zipcode']
                if licenseno and firstname and middlename and lastname and officename and\
                        phone and status and email and username and pssword and addressid and\
                        street and aptno and city and st and country and zipcode:
                    dao.updateDoctorInformationByID(doctorid, licenseno, firstname, middlename, lastname,
                                                officename, phone, status, email, username,
                                                pssword)
                    dao.UpdatePatientAddress(addressid, doctorid, street, aptno, city, st,
                                             country, zipcode)
                    result = self.build_doctor_dict(doctorid, licenseno, firstname, middlename,
                                                    lastname, officename, phone, status, email,
                                                    username, pssword, addressid, street, aptno,
                                                    city, st, country, zipcode)
                    return jsonify(Doctor = result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

########## Doctor History #############
#Para hacerle insert al history del Doctor

    def insertDoctorHistory(self, form):
        dao = DoctorDAO()
        if len(form) != 18:
            return jsonify(Error="Malformed update request"), 400
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
            addressid = form['addressid']
            street = form['street']
            aptno = form['aptno']
            city = form['city']
            st = form['st']
            country = form['country']
            zipcode = form['zipcode']
            if doctorid and licenseno and firstname and middlename and lastname and \
                    officename and phone and status and email and username and pssword \
                    and addressid and street and aptno and city and st and country and zipcode:
                dao.insertDoctorHistory(doctorid, licenseno, firstname, middlename, lastname,
                                        officename, phone, status, email, username, pssword,
                                        addressid, street, aptno, city, st, country, zipcode)
                result = self.build_doctor_dict(doctorid, licenseno, firstname, middlename,
                                                    lastname, officename, phone, status, email,
                                                    username, pssword, addressid, street, aptno,
                                                    city, st, country, zipcode)
                return jsonify(Doctor = result), 201 #Verificar porque 201
            else:
                return jsonify(Error="Unexpected attributes in update request"), 400