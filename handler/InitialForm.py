from flask import jsonify, request
from dao.InitialForm import InitialFormDAO
from dao.s3connection import s3Connection
# import datetime, time
from datetime import datetime, timezone
class InitialFormHandler:

    #### List of Initial Form Diccionary ####
    def build_initialformlist_dict(self,row):
        result = {}
        result['initialformid'] = row[0]
        result['initialform'] = row[1]
        result['assistantid'] = row[2]
        result['doctorid'] = row[2]
        result['dateofupload'] = row[4]
        result['patientid'] = row[5]
        return result

    #### Insert Initial Form Diccionary ####
    def build_ifinsert_dict(self, initialformid, filename, assistantusername, doctorusername, dateofupload, patientid, recordno):
        result = {}
        result['initialformid'] = initialformid
        result['filename'] = filename
        result['assistantusername'] = assistantusername
        result['doctorusername'] = doctorusername
        result['dateofupload'] = dateofupload
        result['patientid'] = patientid
        result['recordno'] = recordno
        return result

    #### List of Initial Form Dates Diccionary ####
    def build_ifdates_dict(self, row):
        result = {}
        result['year'] = row[0]
        result['month'] = row[1]
        return result

    ### Get Patient Initial Form By Patient ID
    # Parameters:   args - requested parameters
    # Return:   Json or Error
    def getPatientInitialForm(self, args):
        pid = args.get("patientid")
        dao = InitialFormDAO()
        initialform_list = dao.getPatientInitialForm(pid)
        result_list = []
        if not initialform_list:
            return jsonify(Error="NOT FOUND"),404
        for row in initialform_list:
            result = self.build_initialformlist_dict(row)
            result_list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(InitialForm=result_list)

    ### Get Patient Initial Form By Patient ID and Initial Form ID
    # Parameters:   args - requested parameters
    # Return:   Json or Error
    def getInitialFormByID(self, args):
        pid = args.get("patientid")
        nid = args.get("initialformid")
        dao = InitialFormDAO()
        row = dao.getInitialFormByID(pid, nid)
        if not row:
            return jsonify(Error="NOT FOUND"),404
        else:
            result = self.build_initialformlist_dict(row[0])
            return jsonify(ConsultatioNote=result)

    ### Insert Initial form
    # Parameters:   args - requested parameters
    # Return:  Json or Error
    def insertInitialForm(self, args, file):
        dao = InitialFormDAO()
        # filepath = file  # this is the file to insert
        filename = args.get("filename")  # form['filename']
        assistantusername = args.get("assistantusername")  # form['assistantusername']
        doctorusername = args.get("doctorusername")  # form['doctorusername']
        patientid = args.get("patientid")  # form['patientid']
        recordno = args.get("recordno")  # form['recordno']

        # print("args : ", args)
        print("filename : ", filename)
        print("assistantusername : ", assistantusername)
        print("doctorusername : ", doctorusername)
        print("patientid : ", patientid)
        print("recordno : ", recordno)
        print("file : ", file)

        # return jsonify(Success="Consultation Node inserted."), 201

        # upload_time = time.time()
        dateofupload = datetime.now(timezone.utc).astimezone().strftime('%Y-%m-%d %H:%M:%S')#datetime.datetime.fromtimestamp(upload_time).strftime('%Y-%m-%d %H:%M:%S')

        if file and dateofupload and recordno:
            if str(dao.verifyRecordno(recordno)) == str(patientid):

                initialformid = dao.insertInitialForm(filename, assistantusername, doctorusername, dateofupload, patientid, recordno)

                s3 = s3Connection()
                targetlocation = 'initialforms/' + str(initialformid) + filename
                print("target location : ", targetlocation)
                #ELIMINAR EL LINK
                link = s3.uploadfile(file, targetlocation)  # returns the url after storing it
                print("link : ", link)

                result = self.build_ifinsert_dict(initialformid, filename, assistantusername, doctorusername, dateofupload, patientid, recordno)
                return jsonify(Success="Initial Form inserted.", InitialForm = result), 201 #Verificar porque 201
            else:
                return jsonify(Error="Record Number does not exist.", RecordNo=recordno), 400
        else:
            return jsonify(Error="Unexpected attributes in insert request"), 400
    ### Get Initial Form Dates
    # Parameters:   args - requested parameters
    # Return:  Json or Error
    def getInitialFormDates(self, args):
        print('estoy en el IF Dates')
        pid = args.get("patientid")
        dao = InitialFormDAO()
        initialform_list = dao.getInitialFormDates(pid)
        result_list = []
        if not initialform_list:
            return jsonify(Error="NOT FOUND"),404
        for row in initialform_list:
            result = self.build_ifdates_dict(row)
            result_list.append(result)  # mapToDict() turns returned array of arrays to an array of maps
        return jsonify(InitialFormDates=result_list)