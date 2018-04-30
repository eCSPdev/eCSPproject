from flask import Flask, jsonify, request, Blueprint
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

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisthesecretkey' #hay que cambiarlo



def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        #print('token', token)
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify(Error="Invalid Token"), 403
        return f(*args, **kwargs)
    return decorated

@app.before_request
def before_execute():
    print ('Estoy en el before')
    #print ('path', request.path)
    user = RoleBase().validate(request.path, request.args)
    print ('user', user)
    #print (request.args.get('username'))



@app.route('/eCSP')
@app.route('/eCSP/Home')
def home():
    return 'INDEX'

@app.route('/Patient/eCSP/Login', methods = ['GET'])
def plogin():
    if request.method == 'GET':
        #print('Login')
        username = request.args.get('username')
        validate = LoginHandler().validatePatient(request.args)
        if not validate:
            return jsonify(Error="Invalid Username or password"), 401
        else:
            token = jwt.encode({'user' : username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            #print('token : ', token)
            return LoginHandler().build_dict(username, token)
    else:
        return jsonify(Error="Method not allowed."), 405


#@app.route('/eCSP/Logout')

@app.route('/Doctor/eCSP/Login', methods = ['GET'])
@app.route('/Assistant/eCSP/Login', methods = ['GET'])
def DAlogin():
    if request.method == 'GET':
        #print('Login')
        username = request.args.get('username')
        validate = LoginHandler().validateAdmin(request.args)
        if not validate:
            return jsonify(Error="Invalid Username or password"), 401
        else:
            token = jwt.encode({'user' : username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return LoginHandler().build_dict(username, token)
    else:
        return jsonify(Error="Method not allowed."), 405


#Get a Doctor List
@app.route('/Doctor/eCSP/DoctorList', methods=['GET', 'POST'])
#@token_required
def getAllDoctor():
    print('getalldoctorlist')
    if request.method == 'GET':
        return DoctorHandler().getAllDoctor()
    elif request.method == 'POST':
        return DoctorHandler().insertDoctor(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get the Doctor Personal Information by Doctor ID
@app.route('/Doctor/eCSP/Doctor/PersonalInformation', methods=['GET', 'PUT'])
def getDoctorByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Doctor ID Included."), 405
        else:
            return DoctorHandler().getDoctorByID(request.args)
    if request.method == 'PUT':
        return DoctorHandler().updateDoctorInformation(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get an Assistant List
@app.route('/Doctor/eCSP/Doctor/AssistantList', methods=['GET', 'POST'])
def getAllAssistant():
    if request.method == 'GET':
        return AssistantHandler().getAllAssistant()
    elif request.method == 'POST':
        return AssistantHandler().insertAssistant(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405


#Get an Assistant Personal Information by Assistant ID
@app.route('/eCSP/Doctor/Assistant/PersonalInformation', methods=['GET', 'PUT'])
@app.route('/eCSP/Assistant/PersonalInformation', methods=['GET', 'PUT'])
def getAssistantByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Assistant ID Included."), 405
        else:
            return AssistantHandler().getAssistantByID(request.args)
    if request.method == 'PUT':
        return AssistantHandler().updateAssistantInformation(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient List
@app.route('/eCSP/Doctor/PatientList', methods=['GET', 'POST'])
@app.route('/eCSP/Assistant/PatientList', methods=['GET', 'POST'])
def getAllPatients():
    if request.method == 'GET':
        return PatientHandler().getAllPatients()
    elif request.method == 'POST':
        return PatientHandler().insertPatient(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get a Patient Personal Information by PatientID
@app.route('/eCSP/Doctor/Patient/PersonalInformation', methods=['GET', 'PUT'])
@app.route('/eCSP/Assistant/Patient/PersonalInformation', methods=['GET', 'PUT'])
@app.route('/eCSP/Patient/PersonalInformation', methods=['GET', 'PUT'])
def getPatientByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Patient ID Included."), 405
        else:
            return PatientHandler().getPatientByID(request.args)
    if request.method == 'PUT':
        return PatientHandler().updatePatientInformation(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Consultation Note List
@app.route('/eCSP/Doctor/Patient/ConsultationNotesList', methods=['GET'])
@app.route('/eCSP/Assistant/Patient/ConsultationNotesList', methods=['GET'])
@app.route('/eCSP/Patient/ConsultationNotesList', methods=['GET'])
def getAllConsultationNotes():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Doctor ID Included."), 405
        else:
            return ConsultationNotesHandler().getPatientConsultationNotes(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Consultation Note Information
@app.route('/eCSP/Doctor/Patient/ConsultationNotes', methods=['GET','POST'])
@app.route('/eCSP/Assistant/Patient/ConsultationNotes', methods=['GET','POST'])
@app.route('/eCSP/Patient/ConsultationNotes', methods=['GET','POST'])
def getConsultationNotesByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Consultation Note ID Included."), 405
        else:
            return ConsultationNotesHandler().getConsultationNotesByID(request.args)
    if request.method == 'POST':
        return ConsultationNotesHandler().insertConsultationNotes(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Initial Form List
@app.route('/eCSP/Doctor/Patient/InitialFormList', methods=['GET'])
@app.route('/eCSP/Assistant/Patient/InitialFormList', methods=['GET'])
@app.route('/eCSP/Patient/InitialFormList', methods=['GET'])
def getAllInitialForm():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Doctor ID Included."), 405
        else:
            return InitialFormHandler().getPatientInitialForm(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Initial Form Information
@app.route('/eCSP/Doctor/Patient/InitialForm', methods=['GET','POST'])
@app.route('/eCSP/Assistant/Patient/InitialForm', methods=['GET','POST'])
@app.route('/eCSP/Patient/InitialForm', methods=['GET','POST'])
def getInitialFormByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Initial Form ID Included."), 405
        else:
            return InitialFormHandler().getInitialFormByID(request.args)
    if request.method == 'POST':
        return InitialFormHandler().insertInitialForm(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Prescription List
@app.route('/eCSP/Doctor/Patient/PrescriptionList', methods=['GET'])
@app.route('/eCSP/Assistant/Patient/PrescriptionList', methods=['GET'])
@app.route('/eCSP/Patient/PrescriptionList', methods=['GET'])
def getAllPrescription():
    if request.method == 'GET':
        return PrescriptionHandler().getPatientPrescription(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Prescription Information
@app.route('/eCSP/Doctor/Patient/Prescription', methods=['GET','POST'])
@app.route('/eCSP/Assistant/Patient/Prescription', methods=['GET','POST'])
@app.route('/eCSP/Patient/Prescription', methods=['GET','POST'])
def getPrescriptionByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Prescription ID Included."), 405
        else:
            return PrescriptionHandler().getPrescriptionByID(request.args)
    if request.method == 'POST':
        return PrescriptionHandler().insertPrescription(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Referral List
@app.route('/eCSP/Doctor/Patient/ReferralList', methods=['GET'])
@app.route('/eCSP/Assistant/Patient/ReferralList', methods=['GET'])
@app.route('/eCSP/Patient/ReferralList', methods=['GET'])
def getAllReferral():
    if request.method == 'GET':
        return ReferralHandler().getPatientReferral(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Referral Information
@app.route('/eCSP/Doctor/Patient/Referral', methods=['GET','POST'])
@app.route('/eCSP/Assistant/Patient/Referral', methods=['GET','POST'])
@app.route('/eCSP/Patient/Referral', methods=['GET','POST'])
def getReferralByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Referral ID Included."), 405
        else:
            return ReferralHandler().getReferralByID(request.args)
    if request.method == 'POST':
        return ReferralHandler().insertReferral(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Result List
@app.route('/eCSP/Doctor/Patient/ResultList', methods=['GET'])
@app.route('/eCSP/Assistant/Patient/ResultList', methods=['GET'])
@app.route('/eCSP/Patient/ResultList', methods=['GET'])
def getAllResult():
    if request.method == 'GET':
        return ResultHandler().getPatientResult(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Result Information
@app.route('/eCSP/Doctor/Patient/Result', methods=['GET','POST'])
@app.route('/eCSP/Assistant/Patient/Result', methods=['GET','POST'])
@app.route('/eCSP/Patient/Result', methods=['GET','POST'])
def getResultByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Result ID Included."), 405
        else:
            return ResultHandler().getResultByID(request.args)
    if request.method == 'POST':
        return ResultHandler().insertResult(request.args)
    else:
        return jsonify(Error="Method not allowed."), 405


if __name__== '__main__':
    app.run()