from flask import jsonify, request
from dao.ConsultationNotes import ConsultationNotesDAO
from dao.InitialForm import InitialFormDAO
from dao.Prescription import PrescriptionDAO
from dao.Referral import ReferralDAO
from dao.Result import ResultDAO
from dao.s3connection import s3Connection
# import datetime, time
from datetime import datetime, timezone
# import os

class ConsultationNotesHandler:

    def build_consultationnoteslist_dict(self,row):
        result = {}
        print(row)
        result['consultationnoteid'] = row[0]
        result['consultationnote'] = row[1]
        result['assistantid'] = row[2]
        result['doctorid'] = row[2]
        result['dateofupload'] = row[4]
        result['patientid'] = row[5]
        result['recordno'] = row[6]
        return result

    def build_cninsert_dict(self, consultationnoteid, filename, assistantusername, doctorusername,
                                                      dateofupload, patientid, recordno):
        result = {}
        result['consultationnoteid'] = consultationnoteid
        result['filename'] = filename
        result['assistantusername'] = assistantusername
        result['doctorusername'] = doctorusername
        result['dateofupload'] = dateofupload
        result['patientid'] = patientid
        result['recordno'] = recordno
        return result

    def build_cndates_dict(self, row):
        result = {}
        result['year'] = row[0]
        result['month'] = row[1]
        return result

    def build_fileslist_dict(self,row):
        result = {}
        print(row)
        result['patientid'] = row[0]
        result['fileid'] = row[1]
        result['filename'] = row[2]
        result['type'] = row[3]
        result['dateofupload'] = row[4].strftime('%Y-%m-%d %H:%M:%S')
        if row[5] != None:
            result['sign'] = row[5]
        elif row[6] != None:
            result['sign'] = row[6]
        else:
            result['sign'] = None
        result['recordno'] = row[7]
        return result

    def build_link_dict(self, link):
        result = {}
        result['filelink'] = link
        return link

    def getPatientConsultationNotes(self, args):
        print('estoy en el CN List')
        pid = args.get("patientid")
        dao = ConsultationNotesDAO()
        consultationnotes_list = dao.getPatientConsultationNotes(pid)
        result_list = []
        if not consultationnotes_list:
            return jsonify(Error="NOT FOUND"),404
        for row in consultationnotes_list:
            result = self.build_consultationnoteslist_dict(row)
            result_list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(ConsultationNotes=result_list)

    def getConsultationNotesByID(self, args):
        pid = args.get("patientid")
        nid = args.get("consultationnoteid")
        dao = ConsultationNotesDAO()
        row = dao.getConsultationNotesByID(pid, nid)
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            result = self.build_consultationnoteslist_dict(row[0])
            return jsonify(ConsultatioNote=result)

    def insertConsultationNotes(self, args, file):
        dao = ConsultationNotesDAO()

        # filepath = file                                                            #this is the file to insert
        filename = args.get("filename")             #form['filename']
        assistantusername = args.get("assistantusername")    #form['assistantusername']
        doctorusername = args.get("doctorusername")       #form['doctorusername']
        patientid = args.get("patientid")            #form['patientid']
        recordno = args.get("recordno")             #form['recordno']

        # print("args : ", args)
        print("filename : ", filename)
        print("assistantusername : ", assistantusername)
        print("doctorusername : ", doctorusername)
        print("patientid : ", patientid)
        print("recordno : ", recordno)
        print("file : ", file)

        # return jsonify(Success="Consultation Node inserted."), 201

        upload_time = datetime.now(timezone.utc).astimezone()#time.time()
        dateofupload = datetime.datetime.fromtimestamp(upload_time).strftime('%Y-%m-%d %H:%M:%S')

        if (file and dateofupload and recordno):

            if str(dao.verifyRecordno(recordno)) == str(patientid):

                consultationnoteid = dao.insertConsultationNote(filename, assistantusername, doctorusername, dateofupload,
                                                                patientid, recordno)

                #insert the file in s3
                s3 = s3Connection()
                targetlocation = 'consultationnotes/'+str(consultationnoteid)+str(filename) #cambiar por filename
                print("target location : ", targetlocation)
                #ELIMINAR EL LINK
                link = s3.uploadfile(file,targetlocation) #returns the url after storing it
                print("link : ", link)

                result = self.build_cninsert_dict(consultationnoteid, filename, assistantusername, doctorusername,
                                                  dateofupload, patientid, recordno)
                return jsonify(Success="Consultation Node inserted.", ConsultatioNote = result), 201
            else:
                return jsonify(Error="Record Number does not exist.", RecordNo=recordno), 400
        else:
            return jsonify(Error="Unexpected attributes in insert request"), 400

    def getFilesDates(self, args):
        print('estoy en el CN Dates')
        pid = args.get("patientid")
        dao = ConsultationNotesDAO()
        files_list = dao.getConsultationNotesDates(pid)
        result_list = []
        if not files_list:
            return jsonify(Error="NOT FOUND"),404
        for row in files_list:
            result = self.build_cndates_dict(row)
            result_list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(FilesDates=result_list)

    def getPatientFiles(self, args):
        print('estoy en los Files')
        pid = args.get("patientid")
        year = args.get("year")
        month = args.get("month")
        dao = ConsultationNotesDAO()
        files_list = dao.getPatientFiles(pid, year, month)
        result_list = []
        print(files_list)
        if not files_list:
            return jsonify(Error="NOT FOUND"),404
        for row in files_list:
            result = self.build_fileslist_dict(row)
            result_list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(FilesList=result_list)

    def getDownloadFile(self, args):
        print('estoy en el Download File args: ', args)
        pid = args.get("patientid")
        print("pid : ", pid)
        type = args.get("type")
        print("type : ", type)
        fileid = args.get("fileid")
        print("fileid : ", fileid)

        if type == 'consultationnote':
            s3 = s3Connection()
            dao = ConsultationNotesDAO()
            filename = dao.getConsultatioNoteNameById(pid, fileid)[0]
            print("filename : ", filename)
            if filename != "None":
                s3filename = str(fileid) + filename
                target_filename = "consultationnotes/"+ s3filename
                link = s3.getfileurl(target_filename)
                result = self.build_link_dict(link)
                return jsonify(FileLink=result)
            else:
                return jsonify(Error="NOT FOUND"), 404

        elif type == 'initialform':
            s3 = s3Connection()
            dao = InitialFormDAO()
            filename = dao.getInitialFormNameById(pid, fileid)[0]
            print("filename : ", filename)
            if filename != "None":
                s3filename = str(fileid) + filename
                target_filename = "initialforms/" + s3filename
                link = s3.getfileurl(target_filename)
                result = self.build_link_dict(link)
                return jsonify(FileLink=result)
            else:
                return jsonify(Error="NOT FOUND"), 404

        elif type == 'prescription':
            s3 = s3Connection()
            dao = PrescriptionDAO()
            filename = dao.getPrescriptionNameById(pid, fileid)[0]
            print("filename : ", filename)
            if filename != "None":
                s3filename = str(fileid) + filename
                target_filename = "prescriptions/" + s3filename
                link = s3.getfileurl(target_filename)
                result = self.build_link_dict(link)
                return jsonify(FileLink=result)
            else:
                return jsonify(Error="NOT FOUND"), 404

        elif type == 'referral':
            s3 = s3Connection()
            dao = ReferralDAO()
            filename = dao.getReferralNameById(pid, fileid)[0]
            print("filename : ", filename)
            if filename != "None":
                s3filename = str(fileid) + filename
                target_filename = "referrals/" + s3filename
                link = s3.getfileurl(target_filename)
                result = self.build_link_dict(link)
                return jsonify(FileLink=result)
            else:
                return jsonify(Error="NOT FOUND"), 404

        elif type == 'result':
            s3 = s3Connection()
            dao = ResultDAO()
            filename = dao.getResultNameById(pid, fileid)[0]
            print("filename : ", filename)
            if filename != "None":
                s3filename = str(fileid) + filename
                target_filename = "results/" + s3filename
                link = s3.getfileurl(target_filename)
                result = self.build_link_dict(link)
                return jsonify(FileLink=result)
            else:
                return jsonify(Error="NOT FOUND"), 404

        else:
            return jsonify(Error="INVALID FILE TYPE"), 404