from flask import jsonify, request
from dao.Doctor import DoctorDAO
from dao.Patient import PatientsDAO
from dao.Assistant import AssistantDAO
from handler.RoleBase import RoleBase
import datetime, time
import uuid

class AssistantHandler:

    def build_assistantlist_dict(self,row):
        result = {}
        result['assistantid'] = row[0]
        result['firstname'] = row[1]
        result['middlename'] = row[2]
        result['lastname'] = row[3]
        #result['phone'] = row[4]
        result['status'] = row[5]
        #result['email'] = row[6]
        result['username'] = row[7]
        #result['pssword'] = row[8]
        return result

    def build_assistantinfo_dict(self,row):
        print(row)
        result = {}
        result['assistantid'] = row[0]
        result['firstname'] = row[1]
        result['middlename'] = row[2]
        result['lastname'] = row[3]
        result['phone'] = row[4]
        result['status'] = row[5]
        result['email'] = row[6]
        result['username'] = row[7]
        result['Password'] = row[8]
        result['addresid'] = row[9]
        result['street'] = row[10]
        result['aptno'] = row[11]
        result['city'] = row[12]
        result['st'] = row[13]
        result['country'] = row[14]
        result['zipcode'] = row[15]
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

    def update_assistant_pssword_dict(self, row):
        result = {}
        result['assistantid'] = row[0]
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
        DoctorSign = form['username']
        if len(form) != 16: # 15 del asistente + el username y token del doctor activo
            return jsonify(Error="Malformed post request"), 400
        else:
            firstname = form['firstname']
            middlename = form['middlename']
            lastname = form['lastname']
            phone = form['phone']
            status = form['status']
            email = form['email']
            username = form['assistantusername']
            pssword = form['pssword']
            street = form['street']
            aptno = form['aptno']
            city = form['city']
            st = form['st']
            country = form['country']
            zipcode = form['zipcode']
            deactivationdate = None
            daysofgrace = None

            if firstname and lastname and phone and status and username and pssword and street and city \
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

                        # assistantid = uuid.uuid4()
                        # license number and username is not taken yet, Doctor can be inserted
                        assistantid = dao.insertAssistantInfo(firstname, middlename, lastname, phone, email, username, pssword)
                        addressid = dao.insertAssistantAddress(assistantid, street, aptno, city, st, country, zipcode)

                        changes_time = time.time()
                        changesdate = datetime.datetime.fromtimestamp(changes_time).strftime('%Y-%m-%d %H:%M:%S')
                        dao.insertAssistantHistory(assistantid, firstname, middlename, lastname, phone, status,
                                                   email, username, pssword, street, aptno, city, st, country, zipcode,
                                                   changesdate, DoctorSign, deactivationdate, daysofgrace)

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

    def updateAssistantInformation(self, form, path):
        # A-adido
        pathlist = RoleBase().splitall(path)
        role = pathlist[1]
        DoctorSign = None
        if role == 'Doctor':
            DoctorSign = form['username']
        #
        dao = AssistantDAO()
        assistantid = form['assistantid']
        row = dao.getAssistantByID(assistantid)
        if row == None:
            return jsonify(Error="Assistant not found."), 404
        else:
            # if len(form) != 16:
            #     print('Entre al jsonify')
            #     print(len(form))
            #     return jsonify(Error="Malformed update request"), 400
            # else:
                print(form)
                assistantid = form['assistantid']
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
                deactivationdate = None
                daysofgrace = None

                if pssword == None:
                    pssword = dao.getPsswordByID(assistantid)

                if assistantid and firstname and lastname and phone and status and street \
                        and city and country and zipcode:
                    print('En el IF')
                    dao.updateAssistantInfoByID(assistantid, firstname, middlename, lastname, phone, status,
                                                email, username, pssword)
                    dao.updateAssistantAddress(assistantid, street, aptno, city, st, country, zipcode)

            #History
                    changes_time = time.time()

                    dateofchanges = datetime.datetime.fromtimestamp(changes_time).strftime('%Y-%m-%d %H:%M:%S')
                    ## Modificado (... , DoctorSign)
                    dao.insertAssistantHistory(assistantid, firstname, middlename, lastname, phone, status,
                                             email, username, pssword, street, aptno, city, st, country, zipcode,
                                               dateofchanges, DoctorSign, deactivationdate, daysofgrace)

                    result = self.update_assistant_dict(assistantid, firstname, middlename, lastname, phone, status,
                                                        email, street, aptno, city, st, country, zipcode)
                    return jsonify(Assistant = result), 200
                else:
                    print('Entre al else')
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def updateAssistantPssword(self, form):
        dao = AssistantDAO()
        assistantid = form["assistantid"]
        if not dao.getAssistantByID(assistantid):
            return jsonify(Error="Assistant not found."), 404
        else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                pssword = form['pssword']
                if pssword:
                    dao.updateAssistantPssword(assistantid, pssword)
                    result = self.update_assistant_pssword_dict(assistantid)
                    return jsonify(Assistant=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

    def manageAssistantStatus(self, form, status):
        print('estoy en el manageAssistantStatus')
        DoctorSign = form['username']
        dao = AssistantDAO()
        assistantid = form["assistantid"]
        assistant = dao.getAssistantByID(assistantid)
        print ('Assistant : ', assistant)
        if not assistant:
            return jsonify(Error="Assistant not found."), 404
        else:
            if len(form) != 4: #username, token, assistantid, deactivationdays
                return jsonify(Error="Malformed update request"), 400
            else:
                firstname = assistant[1]
                middlename = assistant[2]
                lastname = assistant[3]
                phone = assistant[4]
                email = assistant[6]
                username = assistant[7]
                pssword = assistant[8]
                street = assistant[10]
                aptno = assistant[11]
                city = assistant[12]
                st = assistant[13]
                country = assistant[14]
                zipcode = assistant[15]
                changes_time = time.time()
                print('status', status)
                if status == True:
                    daysofgrace = None
                    deactivationdate = None
                else:
                    daysofgrace = form['daysofgrace']
                    print ('days fo grace : ', daysofgrace)
                    date = datetime.datetime.fromtimestamp(changes_time)
                    print('date', date)
                    deactivationdate = (date + datetime.timedelta(days=int(daysofgrace))).strftime('%Y-%m-%d %H:%M:%S')
                    print('deactivationdate : ', deactivationdate)
                dao.updateAssistantStatus(assistantid, status, deactivationdate, daysofgrace)
                # History
                changesdate = datetime.datetime.fromtimestamp(changes_time).strftime('%Y-%m-%d %H:%M:%S')
                ## Modificado (... , DoctorSign)
                dao.insertAssistantHistory(assistantid, firstname, middlename, lastname, phone, status,
                                           email, username, pssword, street, aptno, city, st, country, zipcode,
                                           changesdate, DoctorSign, deactivationdate, daysofgrace) #hay que a-adir al history el campo de deactivationdays
                result = self.update_assistant_dict(assistantid, firstname, middlename, lastname, phone, status,
                                                    email, street, aptno, city, st, country, zipcode)
                return jsonify(Assistant=result), 200


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
                    and street and city and st and country and zipcode:
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