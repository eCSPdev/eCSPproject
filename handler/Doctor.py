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

    def build_doctorhistory_dict(self,row):
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
        result['street'] = row[11]
        result['aptno'] = row[12]
        result['city'] = row[13]
        result['st'] = row[14]
        result['country'] = row[15]
        result['zipcode'] = row[16]
        return result


    def getAllDoctor(self):
        dao = DoctorDAO()
        result = dao.getAllDoctor()
        result_list = []
        for row in result:
            result = self.build_doctorlist_dict(row)
            result.append(result)
        return jsonify(Doctor=result_list)

    def getDoctorByID(self, args):
        did = args.get("doctorid")
        print ('doctor id : ', did )
        dao = DoctorDAO()
        row = dao.getDoctorByID(did)
        if row == None:
            return jsonify(Error="NOT FOUND"),404
        else:
            doctor = self.build_doctorinformation_dict(row)
            return jsonify(Doctor = doctor)

    def updateDoctorInformation(self, args, form):
        dao = DoctorDAO()
        did = args.get("doctorid")
        if not dao.getDoctorByID(did):
            return jsonify(Error="Doctor not found."), 404
        else:
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
                if licenseno and firstname and middlename and lastname and officename and\
                        phone and status and email and username and pssword and addressid and\
                        street and aptno and city and st and country and zipcode:
                    dao.updateDoctorInfoByID(doctorid, licenseno, firstname, middlename, lastname,
                                                officename, phone, status, email, username,
                                                pssword)
                    dao.updateDoctorAddress(addressid, doctorid, street, aptno, city, st,
                                             country, zipcode)
                    result = self.build_doctorinformation_dict(doctorid, licenseno, firstname, middlename,
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
            if doctorid and licenseno and firstname and middlename and lastname and \
                    officename and phone and status and email and username and pssword \
                    and street and aptno and city and st and country and zipcode:
                dao.insertDoctorHistory(doctorid, licenseno, firstname, middlename, lastname,
                                        officename, phone, status, email, username, pssword,
                                        street, aptno, city, st, country, zipcode)
                result = self.build_doctorhistory_dict(doctorid, licenseno, firstname, middlename,
                                                    lastname, officename, phone, status, email,
                                                    username, pssword, street, aptno,
                                                    city, st, country, zipcode)
                return jsonify(History = result), 201 #Verificar porque 201
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400