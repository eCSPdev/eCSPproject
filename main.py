from flask import Flask, jsonify, request, Blueprint, render_template
from functools import wraps
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

import jwt
import datetime

application = app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisthesecretkey' #hay que cambiarlo


"""def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        print ('estoy verificando el token')
        #print('token', token)
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify(Error="Invalid Token"), 403
        return f(*args, **kwargs)
    return decorated
"""

# @app.before_request
# def before_execute():
#     print ('BEFORE_EXECUTE')
#     #print ('path', request.path)
#     validate = RoleBase().validate(request.path, request.args)
#     #print ('user', validate)
#     if validate != True:
#         return validate
#     #print (request.args.get('username'))

# attempt at loading index.html

#Load and render 'index.html'

@app.route('/')
def index():
    return render_template('index.html')
#

@app.route('/Patient/eCSP/Login', methods = ['GET'])
def plogin():
    if request.method == 'GET':
        print('PLOGIN')
        username = request.args.get('username')
        role = LoginHandler().validatePatient(request.args)
        if not role == 0:
            return jsonify(Error="Invalid Username or password"), 401
        else:
            token = jwt.encode({'user' : username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours=8)}, app.config['SECRET_KEY'])
            #print('token : ', token)
            return LoginHandler().updateLogInformation(username, token, role)
    else:
        return jsonify(Error="Method not allowed."), 405

#Logout
@app.route('/Patient/eCSP/Logout', )
@app.route('/Assistant/eCSP/Logout')
@app.route('/Doctor/eCSP/Logout')
def Logout():
    print ('LOGOUT')
    return jsonify(Status="Success")

#Login
@app.route('/Doctor/eCSP/Login', methods = ['GET'])
@app.route('/Assistant/eCSP/Login', methods = ['GET'])
def DAlogin():
    if request.method == 'GET':
        print('Doctor & Assistant Login')
        username = request.args.get('username')
        #print('username : ', username)
        role = LoginHandler().validateAdmin(request.args)
        #print ('role : ', role)
        if role != 1 and role != 2:
            #print ('estoy dentro del if')
            return jsonify(Error="Invalid Username or password"), 401
        else:
            #print('estoy dentro del if')
            token = jwt.encode({'user' : username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return LoginHandler().updateLogInformation(username, token, role)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get a Doctor List
@app.route('/Doctor/eCSP/DoctorList', methods=['GET', 'POST'])
#@token_required
def getAllDoctor():
    if request.method == 'GET':
        print('GET - GETDOCTORLIST')
        return DoctorHandler().getAllDoctor()
    elif request.method == 'POST':
        return DoctorHandler().insertDoctor(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get the Doctor Personal Information by Doctor ID
@app.route('/Doctor/eCSP/PersonalInformation', methods=['GET', 'PUT'])
def getDoctorByID():
    if request.method == 'GET':
        print('GET - GETDOCTORBYID')
        if not request.args:
            return jsonify(Error="No Doctor ID Included."), 405
        else:
            return DoctorHandler().getDoctorByID(request.args)
    if request.method == 'PUT':
        return DoctorHandler().updateDoctorInformation(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Deactivate Assistant Status
@app.route('/Doctor/eCSP/Assistant/Deactivate', methods = ['PUT'])
def deactivateAssistantStatus():
    if request.method == 'PUT':
        status = False
        print('estoy en el deactivate assistant')
        return AssistantHandler().manageAssistantStatus(request.args, status)
    else:
        return jsonify(Error="Method not allowed."), 405

#Activate Assistant Status
@app.route('/Doctor/eCSP/Assistant/Activate', methods = ['PUT'])
def activateAssistantStatus():
    if request.method == 'PUT':
        status = True
        return AssistantHandler().manageAssistantStatus(request.args, status)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get an Assistant List
@app.route('/Doctor/eCSP/AssistantList', methods=['GET', 'POST'])
def getAllAssistant():
    if request.method == 'GET':
        print('GET - GETASSISTANTLIST')
        return AssistantHandler().getAllAssistant()
    elif request.method == 'POST':
        return AssistantHandler().insertAssistant(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405


#Get an Assistant Personal Information by Assistant ID
@app.route('/Doctor/eCSP/Assistant/PersonalInformation', methods=['GET', 'PUT'])
@app.route('/Assistant/eCSP/PersonalInformation', methods=['GET', 'PUT'])
def getAssistantByID():
    if request.method == 'GET':
        print('GET - GETASSISTANTBYID')
        if not request.args:
            return jsonify(Error="No Assistant ID Included."), 405
        else:
            return AssistantHandler().getAssistantByID(request.args)
    if request.method == 'PUT':
        path = request.path
        return AssistantHandler().updateAssistantInformation(request.args, path)
    else:
        return jsonify(Error="Method not allowed."), 405

#Deactivate Patient Status
@app.route('/Doctor/eCSP/Patient/Deactivate', methods = ['PUT'])
@app.route('/Assistant/eCSP/Patient/Deactivate', methods = ['PUT'])
def deactivatePatientStatus():
    if request.method == 'PUT':
        path = request.path
        status = False
        return PatientHandler().managePatientStatus(request.args, path, status)
    else:
        return jsonify(Error="Method not allowed."), 405

#Activate Patient Status
@app.route('/Doctor/eCSP/Patient/Activate', methods = ['PUT'])
@app.route('/Assistant/eCSP/Patient/Activate', methods = ['PUT'])
def activatePatientStatus():
    if request.method == 'PUT':
        path = request.path
        status = True
        return PatientHandler().managePatientStatus(request.args, path, status)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient List
@app.route('/Doctor/eCSP/PatientList', methods=['GET', 'POST'])
@app.route('/Assistant/eCSP/PatientList', methods=['GET', 'POST'])
def getAllPatients():
    if request.method == 'GET':
        print('GET - GETPATIENTLIST')
        return PatientHandler().getAllPatients()
    elif request.method == 'POST':
        return PatientHandler().insertPatient(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get a Patient Personal Information by PatientID
@app.route('/Doctor/eCSP/Patient/PersonalInformation', methods=['GET', 'PUT'])
@app.route('/Assistant/eCSP/Patient/PersonalInformation', methods=['GET', 'PUT'])
@app.route('/Patient/eCSP/PersonalInformation', methods=['GET', 'PUT'])
def getPatientByID():
    if request.method == 'GET':
        print('GET - GETPATIENTBYID')
        if not request.args:
            return jsonify(Error="No Patient ID Included."), 405
        else:
            return PatientHandler().getPatientByID(request.args)
    if request.method == 'PUT':
        print ('PUT - Patient Personal Information')
        path = request.path
        return PatientHandler().updatePatientInformation(request.args, path)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Consultation Note List
@app.route('/Doctor/eCSP/Patient/ConsultationNotesList', methods=['GET'])
@app.route('/Assistant/eCSP/Patient/ConsultationNotesList', methods=['GET'])
@app.route('/Patient/eCSP/ConsultationNotesList', methods=['GET'])
def getAllConsultationNotes():
    if request.method == 'GET':
        print('GET - GETALLCONSULTATIONNOTES')
        if not request.args:
            return jsonify(Error="ID Included."), 405
        else:
            return ConsultationNotesHandler().getPatientConsultationNotes(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Consultation Note Information
@app.route('/Doctor/eCSP/Patient/ConsultationNotes', methods=['GET','POST'])
@app.route('/Assistant/eCSP/Patient/ConsultationNotes', methods=['GET','POST'])
@app.route('/Patient/eCSP/ConsultationNotes', methods=['GET','POST'])
def getConsultationNotesByID():
    if request.method == 'GET':
        print('GET - GETCONSULTATIONNOTEBYID')
        if not request.args:
            return jsonify(Error="No Consultation Note ID Included."), 405
        else:
            return ConsultationNotesHandler().getConsultationNotesByID(request.args)
    if request.method == 'POST':
        return ConsultationNotesHandler().insertConsultationNotes(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Initial Form List
@app.route('/Doctor/eCSP/Patient/InitialFormList', methods=['GET'])
@app.route('/Assistant/eCSP/Patient/InitialFormList', methods=['GET'])
@app.route('/Patient/eCSP/InitialFormList', methods=['GET'])
def getAllInitialForm():
    if request.method == 'GET':
        print('GET - GETALLINITIALFORM')
        if not request.args:
            return jsonify(Error="No Doctor ID Included."), 405
        else:
            return InitialFormHandler().getPatientInitialForm(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Initial Form Information
@app.route('/Doctor/eCSP/Patient/InitialForm', methods=['GET','POST'])
@app.route('/Assistant/eCSP/Patient/InitialForm', methods=['GET','POST'])
@app.route('/Patient/eCSP/InitialForm', methods=['GET','POST'])
def getInitialFormByID():
    if request.method == 'GET':
        print('GET - GETINITIALFORMBYID')
        if not request.args:
            return jsonify(Error="No Initial Form ID Included."), 405
        else:
            return InitialFormHandler().getInitialFormByID(request.args)
    if request.method == 'POST':
        return InitialFormHandler().insertInitialForm(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Prescription List
@app.route('/Doctor/eCSP/Patient/PrescriptionList', methods=['GET'])
@app.route('/Assistant/eCSP/Patient/PrescriptionList', methods=['GET'])
@app.route('/Patient/eCSP/PrescriptionList', methods=['GET'])
def getAllPrescription():
    if request.method == 'GET':
        print('GET - GETALLPRESCRIPTIONS')
        return PrescriptionHandler().getPatientPrescription(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Prescription Information
@app.route('/Doctor/eCSP/Patient/Prescription', methods=['GET','POST'])
@app.route('/Assistant/eCSP/Patient/Prescription', methods=['GET','POST'])
@app.route('/Patient/eCSP/Prescription', methods=['GET','POST'])
def getPrescriptionByID():
    if request.method == 'GET':
        print('GET - GETPRESCRIPTIONBYID')
        if not request.args:
            return jsonify(Error="No Prescription ID Included."), 405
        else:
            return PrescriptionHandler().getPrescriptionByID(request.args)
    if request.method == 'POST':
        return PrescriptionHandler().insertPrescription(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Referral List
@app.route('/Doctor/eCSP/Patient/ReferralList', methods=['GET'])
@app.route('/Assistant/eCSP/Patient/ReferralList', methods=['GET'])
@app.route('/Patient/eCSP/ReferralList', methods=['GET'])
def getAllReferral():
    if request.method == 'GET':
        print('GET - GETALLREFERRAL')
        return ReferralHandler().getPatientReferral(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Referral Information
@app.route('/Doctor/eCSP/Patient/Referral', methods=['GET','POST'])
@app.route('/Assistant/eCSP/Patient/Referral', methods=['GET','POST'])
@app.route('/Patient/eCSP/Referral', methods=['GET','POST'])
def getReferralByID():
    if request.method == 'GET':
        print('GET - GETREFERRALBYID')
        if not request.args:
            return jsonify(Error="No Referral ID Included."), 405
        else:
            return ReferralHandler().getReferralByID(request.args)
    if request.method == 'POST':
        return ReferralHandler().insertReferral(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Result List
@app.route('/Doctor/eCSP/Patient/ResultList', methods=['GET'])
@app.route('/Assistant/eCSP/Patient/ResultList', methods=['GET'])
@app.route('/Patient/eCSP/ResultList', methods=['GET'])
def getAllResult():
    if request.method == 'GET':
        print('GET - GETALLRESULTS')
        return ResultHandler().getPatientResult(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Result Information
@app.route('/Patient/eCSP/Doctor/Result', methods=['GET','POST'])
@app.route('/Assistant/eCSP/Patient/Result', methods=['GET','POST'])
@app.route('/Patient/eCSP/Result', methods=['GET','POST'])
def getResultByID():
    if request.method == 'GET':
        print('GET - GETRESULTBYID')
        if not request.args:
            return jsonify(Error="No Result ID Included."), 405
        else:
            return ResultHandler().getResultByID(request.args)
    if request.method == 'POST':
        return ResultHandler().insertResult(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405


if __name__== '__main__':
    application.run(debug=True)