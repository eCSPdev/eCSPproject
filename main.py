from flask import Flask, render_template, request, jsonify
from handler.Assistant import AssistantHandler
from handler.Doctor import DoctorHandler
from handler.Patient import PatientHandler
from handler.ConsultationNotes import ConsultationNotesHandler
from handler.InitialForm import InitialFormHandler
from handler.Prescription import PrescriptionHandler
from handler.Referral import ReferralHandler
from handler.Result import ResultHandler
from handler.Login import LoginHandler
from handler.RoleBase import RoleBase
import logging
import jwt
import datetime

application = Flask(__name__)

application.config['SECRET_KEY'] = 'thisisthesecretkey' #hay que cambiarlo

#Secret Key para el token
application.config['SECRET_KEY'] = 'thisisthesecretkey' #hay que cambiarlo cuando se entregue

#### Before Execute Routine to validate user ####
@application.before_request
def before_execute():
    if request.path.split('/')[1] == 'Doctor' or request.path.split('/')[1] == 'Assistant' or request.path.split('/')[1] == 'Patient':
        validate = RoleBase().validate(request.path, request.args)
        if validate != True:
            return validate
        print (request.args.get('username'))

#Load and render 'index.html'
@application.route('/')
def index():
    return render_template('index.html')

#### Patient login Routes ####
@application.route('/Patient/eCSP/Login', methods = ['GET'])
def plogin():
    if request.method == 'GET':
        username = request.args.get('username')
        token = (jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=8)},
                            application.config['SECRET_KEY'])).decode('UTF-8')
        result = LoginHandler().validatePatient(request.args, token)
        return result
    else:
        return jsonify(Error="Method not allowed."), 405

#### Users Logout Routes ####
@application.route('/Patient/eCSP/Logout', )
@application.route('/Assistant/eCSP/Logout')
@application.route('/Doctor/eCSP/Logout')
def Logout():
    return jsonify(Status="Success")

#### Admin Login Routes ####
@application.route('/Doctor/eCSP/Login', methods = ['GET'])
@application.route('/Assistant/eCSP/Login', methods = ['GET'])
def DAlogin():
    if request.method == 'GET':
        username = request.args.get('username')
        token = (jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=8)},
                            application.config['SECRET_KEY'])).decode('UTF-8')
        result = LoginHandler().validateAdmin(request.args, token)
        return result
    else:
        return jsonify(Error="Method not allowed."), 405

#### Doctor List GET & POST Routes ###
@application.route('/Doctor/eCSP/DoctorList', methods=['GET', 'POST'])
def getAllDoctor():
    if request.method == 'GET':
        return DoctorHandler().getAllDoctor()
    elif request.method == 'POST':
        return DoctorHandler().insertDoctor(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#### Doctor Personal Information by Doctor ID GET & PUT Route ####
@application.route('/Doctor/eCSP/PersonalInformation', methods=['GET', 'PUT'])
def getDoctorByID():
    if request.method == 'GET':
        if not request.args:
            print('405 here')
            return jsonify(Error="No Doctor ID Included."), 405
        else:
            return DoctorHandler().getDoctorByID(request.args)
    if request.method == 'PUT':
        return DoctorHandler().updateDoctorInformation(request.get_json())
    else:
        return jsonify(Error="Method not allowed."), 405

#### Deactivate Assistant Status PUT Route ####
@application.route('/Doctor/eCSP/Assistant/Deactivate', methods = ['PUT'])
def deactivateAssistantStatus():
    if request.method == 'PUT':
        status = False
        print('estoy en el deactivate assistant')
        return AssistantHandler().manageAssistantStatus(request.args, status)
    else:
        return jsonify(Error="Method not allowed."), 405

#### Activate Assistant Status PUT Route ####
@application.route('/Doctor/eCSP/Assistant/Activate', methods = ['PUT'])
def activateAssistantStatus():
    if request.method == 'PUT':
        status = True
        return AssistantHandler().manageAssistantStatus(request.args, status)
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get All Assistant List GET & POST Route ####
@application.route('/Doctor/eCSP/AssistantList', methods=['GET', 'POST'])
def getAllAssistant():
    if request.method == 'GET':
        return AssistantHandler().getAllAssistant()
    elif request.method == 'POST':
        return AssistantHandler().insertAssistant(request.get_json())
    else:
        return jsonify(Error="Method not allowed."), 405


#### Get Assistant Personal Information by Assistant ID GET & PUT Routes ####
@application.route('/Doctor/eCSP/Assistant/PersonalInformation', methods=['GET', 'PUT'])
@application.route('/Assistant/eCSP/PersonalInformation', methods=['GET', 'PUT'])
def getAssistantByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Assistant ID Included."), 405
        else:
            return AssistantHandler().getAssistantByID(request.args)
    if request.method == 'PUT':
        path = request.path
        return AssistantHandler().updateAssistantInformation(request.get_json(), path)
    else:
        return jsonify(Error="Method not allowed."), 405

#### Deactivate Patient Status PUT Routes ####
@application.route('/Doctor/eCSP/Patient/Deactivate', methods = ['PUT'])
@application.route('/Assistant/eCSP/Patient/Deactivate', methods = ['PUT'])
def deactivatePatientStatus():
    if request.method == 'PUT':
        path = request.path
        status = False
        return PatientHandler().managePatientStatus(request.args, path, status)
    else:
        return jsonify(Error="Method not allowed."), 405

#### Activate Patient Status PUT Route ####
@application.route('/Doctor/eCSP/Patient/Activate', methods = ['PUT'])
@application.route('/Assistant/eCSP/Patient/Activate', methods = ['PUT'])
def activatePatientStatus():
    if request.method == 'PUT':
        path = request.path
        status = True
        return PatientHandler().managePatientStatus(request.args, path, status)
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get Patient List GET & POST Routes ####
@application.route('/Doctor/eCSP/PatientList', methods=['GET', 'POST'])
@application.route('/Assistant/eCSP/PatientList', methods=['GET', 'POST'])
def getAllPatients():
    if request.method == 'GET':
        return PatientHandler().getAllPatients()
    elif request.method == 'POST':
        return PatientHandler().insertPatient(request.get_json())
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get a Patient Personal Information by PatientID GET & PUT Routes ####
@application.route('/Doctor/eCSP/Patient/PersonalInformation', methods=['GET', 'PUT'])
@application.route('/Assistant/eCSP/Patient/PersonalInformation', methods=['GET', 'PUT'])
@application.route('/Patient/eCSP/PersonalInformation', methods=['GET', 'PUT'])
def getPatientByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Patient ID Included."), 405
        else:
            return PatientHandler().getPatientByID(request.args)
    if request.method == 'PUT':
        path = request.path

        return PatientHandler().updatePatientInformation(request.get_json(), path)
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get Patient Consultation Note List GET Routes ####
@application.route('/Doctor/eCSP/Patient/ConsultationNotesList', methods=['GET'])
@application.route('/Assistant/eCSP/Patient/ConsultationNotesList', methods=['GET'])
@application.route('/Patient/eCSP/ConsultationNotesList', methods=['GET'])
def getAllConsultationNotes():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="ID Included."), 405
        else:
            return ConsultationNotesHandler().getPatientConsultationNotes(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get Patient Consultation Note Information by ID GET & POST Routes ####
@application.route('/Doctor/eCSP/Patient/ConsultationNotes', methods=['GET','POST'])
@application.route('/Assistant/eCSP/Patient/ConsultationNotes', methods=['GET','POST'])
@application.route('/Patient/eCSP/ConsultationNotes', methods=['GET','POST'])
def getConsultationNotesByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Consultation Note ID Included."), 405
        else:
            return ConsultationNotesHandler().getConsultationNotesByID(request.args)
    if request.method == 'POST':
        print("Estoy en el POST Consultation Notes")
        return ConsultationNotesHandler().insertConsultationNotes(request.args, request.files['file'])
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get Patient Initial Form List GET Routes ####
@application.route('/Doctor/eCSP/Patient/InitialFormList', methods=['GET'])
@application.route('/Assistant/eCSP/Patient/InitialFormList', methods=['GET'])
@application.route('/Patient/eCSP/InitialFormList', methods=['GET'])
def getAllInitialForm():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Doctor ID Included."), 405
        else:
            return InitialFormHandler().getPatientInitialForm(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get Patient Initial Form Information by ID GET & POST Routes ####
@application.route('/Doctor/eCSP/Patient/InitialForm', methods=['GET','POST'])
@application.route('/Assistant/eCSP/Patient/InitialForm', methods=['GET','POST'])
@application.route('/Patient/eCSP/InitialForm', methods=['GET','POST'])
def getInitialFormByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Initial Form ID Included."), 405
        else:
            return InitialFormHandler().getInitialFormByID(request.args)
    if request.method == 'POST':
        return InitialFormHandler().insertInitialForm(request.args, request.files['file'])
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get Patient Prescription List GET Routes ####
@application.route('/Doctor/eCSP/Patient/PrescriptionList', methods=['GET'])
@application.route('/Assistant/eCSP/Patient/PrescriptionList', methods=['GET'])
@application.route('/Patient/eCSP/PrescriptionList', methods=['GET'])
def getAllPrescription():
    if request.method == 'GET':
        print('GET - GETALLPRESCRIPTIONS')
        return PrescriptionHandler().getPatientPrescription(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get Patient Prescription Information by ID GET & POST ####
@application.route('/Doctor/eCSP/Patient/Prescription', methods=['GET','POST'])
@application.route('/Assistant/eCSP/Patient/Prescription', methods=['GET','POST'])
@application.route('/Patient/eCSP/Prescription', methods=['GET','POST'])
def getPrescriptionByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Prescription ID Included."), 405
        else:
            return PrescriptionHandler().getPrescriptionByID(request.args)
    if request.method == 'POST':
        return PrescriptionHandler().insertPrescription(request.args, request.files['file'])
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get Patient Referral List GET Routes ####
@application.route('/Doctor/eCSP/Patient/ReferralList', methods=['GET'])
@application.route('/Assistant/eCSP/Patient/ReferralList', methods=['GET'])
@application.route('/Patient/eCSP/ReferralList', methods=['GET'])
def getAllReferral():
    if request.method == 'GET':
        return ReferralHandler().getPatientReferral(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get Patient Referral Information by ID GET & POST Routes ####
@application.route('/Doctor/eCSP/Patient/Referral', methods=['GET','POST'])
@application.route('/Assistant/eCSP/Patient/Referral', methods=['GET','POST'])
@application.route('/Patient/eCSP/Referral', methods=['GET','POST'])
def getReferralByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Referral ID Included."), 405
        else:
            return ReferralHandler().getReferralByID(request.args)
    if request.method == 'POST':
        return ReferralHandler().insertReferral(request.args, request.files['file'])
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get Patient Result List GET Routes ####
@application.route('/Doctor/eCSP/Patient/ResultList', methods=['GET'])
@application.route('/Assistant/eCSP/Patient/ResultList', methods=['GET'])
@application.route('/Patient/eCSP/ResultList', methods=['GET'])
def getAllResult():
    if request.method == 'GET':
        print('GET - GETALLRESULTS')
        return ResultHandler().getPatientResult(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get Patient Result Information by ID Routes ####
@application.route('/Doctor/eCSP/Patient/Result', methods=['GET','POST'])
@application.route('/Assistant/eCSP/Patient/Result', methods=['GET','POST'])
@application.route('/Patient/eCSP/Result', methods=['GET','POST'])
def getResultByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Result ID Included."), 405
        else:
            return ResultHandler().getResultByID(request.args)
    if request.method == 'POST':
        return ResultHandler().insertResult(request.args, request.files['file'])
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get all files by Patient ID GET Routes ####
@application.route('/Doctor/eCSP/Patient/Files', methods=['GET'])
@application.route('/Assistant/eCSP/Patient/Files', methods=['GET'])
@application.route('/Patient/eCSP/Files', methods=['GET'])
def getPatientFiles():
    if request.method == 'GET':
        return ConsultationNotesHandler().getPatientFiles(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#### Get files dates by Patient ID GET Routes ####
@application.route('/Doctor/eCSP/Patient/Files/Dates', methods=['GET'])
@application.route('/Assistant/eCSP/Patient/Files/Dates', methods=['GET'])
@application.route('/Patient/eCSP/Files/Dates', methods=['GET'])
def getFilesDates():
    if request.method == 'GET':
        return ConsultationNotesHandler().getFilesDates(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#### Download File by File ID GET Routes ####
@application.route('/Doctor/eCSP/Patient/Files/Download', methods=['GET'])
@application.route('/Assistant/eCSP/Patient/Files/Download', methods=['GET'])
@application.route('/Patient/eCSP/Files/Download', methods=['GET'])
def getDownloadFile():

    # logging.debug('DEBUG : ESTOY EN LA RUTA DE DOWNLOAD FILES')
    print("pase el logger")
    if request.method == 'GET':
        return ConsultationNotesHandler().getDownloadFile(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

if __name__== '__main__':
    application.run(debug=True)
