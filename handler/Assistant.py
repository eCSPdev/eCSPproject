from flask import jsonify, request
from dao.Doctor import DoctorDAO
from dao.Patient import PatientsDAO
from dao.Assistant import AssistantDAO

class AssistantHandler:

    def build_assistantlist_dict(self,row):
        result = {}
        result['assistantid'] = row[0]
        result['firstname'] = row[1]
        result['middlename'] = row[2]
        result['lastname'] = row[3]
        result['phone'] = row[4]
        result['status'] = row[5]
        result['email'] = row[6]
        result['username'] = row[7]
        result['pssword'] = row[8]
        return result

    def build_assistantinfo_dict(self,row):
        result = {}
        result['assistantid'] = row[0]
        result['firstname'] = row[1]
        result['middlename'] = row[2]
        result['lastname'] = row[3]
        result['phone'] = row[4]
        result['status'] = row[5]
        result['email'] = row[6]
        result['username'] = row[7]
        result['addressid'] = row[8]
        result['street'] = row[9]
        result['aptno'] = row[10]
        result['city'] = row[11]
        result['st'] = row[12]
        result['country'] = row[13]
        result['zipcode'] = row[14]
        return result

    def update_assistant_dict(self, assistantid, firstname, middlename, lastname, phone, status,
                           email, street, aptno, city, st, country, zipcode):
        result = {}
        result['assistantid'] = assistantid
        result['firstname'] = firstname
        result['middlename'] = middlename
        result['lastname'] = lastname
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

    def new_assistant_dict(self, assistantid, firstname, middlename, lastname, phone, status, email, username,
                           pssword, addressid, street, aptno, city, st, country, zipcode):
        result = {}
        result['assistantid'] = assistantid
        result['firstname'] = firstname
        result['middlename'] = middlename
        result['lastname'] = lastname
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


    def build_assistanthistory_dict(self, assistantid, firstname, middlename, lastname, phone, status,
                                 email, username, street, aptno, city, st, country, zipcode):
        result = {}
        result['assistantid'] = assistantid
        result['firstname'] = firstname
        result['middlename'] = middlename
        result['lastname'] = lastname
        result['phone'] = phone
        result['status'] = status
        result['email'] = email
        result['username'] = username
        result['street'] = street
        result['aptno'] = aptno
        result['city'] = city
        result['st'] = st
        result['country'] = country
        result['zipcode'] = zipcode
        return result

    def verify_existantassistant_dict(self, row):
        result = {}
        result['assistantid'] = row[0]
        result['firstname'] = row[1]
        result['middlename'] = row[2]
        result['lastname'] = row[3]
        result['phone'] = row[4]
        result['status'] = row[5]
        result['email'] = row[6]
        result['username'] = row[7]
        result['addressid'] = row[8]
        result['street'] = row[9]
        result['aptno'] = row[10]
        result['city'] = row[11]
        result['st'] = row[12]
        result['country'] = row[13]
        result['zipcode'] = row[14]
        return result


    def getAllAssistant(self):
        dao = AssistantDAO()
        result = dao.getAllAssistants()
        result_list = []
        for row in result:
            result_list.append(self.build_assistantlist_dict(row))
        return jsonify(Assistant=result_list)

    def getAssistantByID(self, args):
        dao = AssistantDAO()
        aid = args.get("assistantid")
        row = dao.getAssistantByID(aid)
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            result = self.build_assistantinfo_dict(row)
            return jsonify(Assistant = result)

    def insertAssistant(self, form):
        if len(form) != 14:
            return jsonify(Error="Malformed post request"), 400
        else:
            firstname = form['firstname']
            middlename = form['middlename']
            lastname = form['lastname']
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

            if firstname and lastname and phone and status and username and pssword and street and aptno and city \
                    and country and zipcode:

                dao = AssistantDAO()
                doctordao = DoctorDAO()
                patientdao = PatientsDAO()

                # verify if a assistant exist with this information
                existantassistant_list = dao.verifyAssistant(firstname, middlename, lastname)

                # no doctor exist with this information
                if not existantassistant_list:
                    # verify if username already exist
                    if dao.verifyUsername(username) == None \
                            and patientdao.verifyUsername(username) == None \
                            and doctordao.verifyUsername(username) == None:
                        # license number and username is not taken yet, Doctor can be inserted
                        assistantid = dao.insertAssistantInfo(firstname, middlename, lastname, phone, email, username, pssword)
                        addressid = dao.insertAssistantAddress(assistantid, street, aptno, city, st, country, zipcode)
                        result = self.new_assistant_dict(assistantid, firstname, middlename, lastname, phone, status,
                                               email, username, pssword, addressid, street, aptno, city, st, country, zipcode)
                        return jsonify(Success="Assistant added correctly", Assistant=result), 201
                        # return jsonify(Success="Assistant added correctly")
                    # username already exist
                    else:
                        return jsonify(Error="Username is already taken.")
                # a patient with this info already exists
                else:
                    # return doctor or doctors with this critical information
                    result_list = []
                    for row in existantassistant_list:
                        result_list.append(self.verify_existantassistant_dict(row))
                    return jsonify(Error="A Assistant with this information already exist.", Assistant=result_list)
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateAssistantInformation(self, form):
        dao = AssistantDAO()
        assistantid = form['assistantid']
        row = dao.getAssistantByID(assistantid)
        if row == None:
            return jsonify(Error="Assistant not found."), 404
        else:
            if len(form) != 13:
                return jsonify(Error="Malformed update request"), 400
            else:
                assistantid = form['assistantid']
                firstname = form['firstname']
                middlename = form['middlename']
                lastname = form['lastname']
                phone = form['phone']
                status = form['status']
                email = form['email']
                street = form['street']
                aptno = form['aptno']
                city = form['city']
                st = form['st']
                country = form['country']
                zipcode = form['zipcode']
                if assistantid and firstname and lastname and phone and status and street and aptno \
                        and city and country and zipcode:
                    dao.updateAssistantInfoByID(assistantid, firstname, middlename, lastname, phone, status,
                                                email)
                    dao.updateAssistantAddress(assistantid, street, aptno, city, st, country, zipcode)
                    result = self.update_assistant_dict(assistantid, firstname, middlename, lastname, phone, status,
                                                        email, street, aptno, city, st, country, zipcode)
                    return jsonify(Assistant = result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

########## Assistant History #############
#Para hacerle insert al history del Asistente

    def insertAssistantHistory(self, form):
        dao = AssistantDAO()
        if len(form) != 14:
            return jsonify(Error="Malformed insert request"), 400
        else:
            assistantid = form['assistantid']
            firstname = form['firstname']
            middlename = form['middlename']
            lastname = form['lastname']
            phone = form['phone']
            status = form['status']
            email = form['email']
            username = form['username']
            street = form['street']
            aptno = form['aptno']
            city = form['city']
            st = form['st']
            country = form['country']
            zipcode = form['zipcode']
            if assistantid and firstname and middlename and lastname and \
                    phone and status and username \
                    and street and aptno and city and st and country and zipcode:
                dao.insertAssistantHistory(assistantid, firstname, middlename, lastname,
                                        phone, status, email, username,
                                        street, aptno, city, st, country, zipcode)
                result = self.build_assistanthistory_dict(assistantid, firstname, middlename,
                                                    lastname, phone, status, email,
                                                    username, street, aptno,
                                                    city, st, country, zipcode)
                return jsonify(Assistant = result), 201 #Verificar porque 201
            else:
                return jsonify(Error="Unexpected attributes in insert request"), 400