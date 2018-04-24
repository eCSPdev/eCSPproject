from flask import Flask, jsonify, request, session, render_template
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

app = Flask(__name__)
app.debuger = True

@app.route('/')
@app.route('/eCSP')
@app.route('/eCSP/Home')
def home():
    return 'INDEX'

@app.route('/eCSP/PLogin', methods=['GET', 'POST'])
def Plogin():
    if request.method == 'POST':
        username = request.args.get("username")
       # print ('username : ', username )
        row = LoginHandler().validatePatient(request.args)
        if not row:
            return jsonify(Error="NOT FOUND"), 404
        else:
            session['logged_in'] = True
            session['role'] = 'patient'
            session['username'] = username
            return row
    else:
        return jsonify(Error="Method not allowed."), 405

def patient_is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return jsonify(Error="Unauthorized"), 405
    return wrap

@app.route('/eCSP/Logout')
@patient_is_logged_in
def logout():
    session.clear()
    return True

@app.route('/eCSP/DALogin')
def DAlogin():
    if request.method == 'POST':
        username = request.form['username']
        rle = LoginHandler().validateAdmin(request.form)
        if not rle:
            return jsonify(Error="NOT FOUND"), 404
        else:
            session['logged_in'] = True
            session['role'] = rle.get('rle') #no se si se puede
            session['username'] = username
            return rle
    else:
        return jsonify(Error="Method not allowed."), 405

def doctor_is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            if session.get('role') == 'doctor':
                return f(*args, **kwargs)
        else:
            return jsonify(Error="Unauthorized"), 405
    return wrap

def assistant_is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            if session.get('role') == 'assistant':
                return f(*args, **kwargs)
        else:
            return jsonify(Error="Unauthorized"), 405
    return wrap


#Get the Doctor Personal Information by Doctor ID
@app.route('/eCSP/Doctor/PersonalInformation', methods=['GET', 'PUT'])
def getDoctorByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Doctor ID Included."), 405
        else:
            return DoctorHandler().getDoctorByID(request.args)
    if request.method == 'PUT':
        DoctorHandler().updateDoctorInformation(request.form)
        return DoctorHandler().updateDoctorInformation(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get an Assistant List
@app.route('/eCSP/Doctor/AssistantList', methods=['GET', 'POST'])
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
        return ConsultationNotesHandler().getPatientConsultationNotes(request.form)
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
            return ConsultationNotesHandler().getConsultationNotesByID(request.form)
    if request.method == 'POST':
        return ConsultationNotesHandler().insertConsultationNotes(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Initial Form List
@app.route('/eCSP/Doctor/Patient/InitialFormList', methods=['GET'])
@app.route('/eCSP/Assistant/Patient/InitialFormList', methods=['GET'])
@app.route('/eCSP/Patient/InitialFormList', methods=['GET'])
def getAllInitialForm():
    if request.method == 'GET':
        return InitialFormHandler().getPatientInitialForm(request.form)
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
            return InitialFormHandler().getInitialFormByID(request.form)
    if request.method == 'POST':
        return InitialFormHandler().insertInitialForm(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Prescription List
@app.route('/eCSP/Doctor/Patient/PrescriptionList', methods=['GET'])
@app.route('/eCSP/Assistant/Patient/PrescriptionList', methods=['GET'])
@app.route('/eCSP/Patient/PrescriptionList', methods=['GET'])
def getAllPrescription():
    if request.method == 'GET':
        return PrescriptionHandler().getPatientPrescription(request.form)
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
            return PrescriptionHandler().getPrescriptionByID(request.form)
    if request.method == 'POST':
        return PrescriptionHandler().insertPrescription(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Referral List
@app.route('/eCSP/Doctor/Patient/ReferralList', methods=['GET'])
@app.route('/eCSP/Assistant/Patient/ReferralList', methods=['GET'])
@app.route('/eCSP/Patient/ReferralList', methods=['GET'])
def getAllReferral():
    if request.method == 'GET':
        return ReferralHandler().getPatientReferral(request.form)
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
            return ReferralHandler().getReferralByID(request.form)
    if request.method == 'POST':
        return ReferralHandler().insertReferral(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Result List
@app.route('/eCSP/Doctor/Patient/ResultList', methods=['GET'])
@app.route('/eCSP/Assistant/Patient/ResultList', methods=['GET'])
@app.route('/eCSP/Patient/ResultList', methods=['GET'])
def getAllResult():
    if request.method == 'GET':
        return ResultHandler().getPatientResult(request.form)
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
            return ResultHandler().getResultByID(request.form)
    if request.method == 'POST':
        return ResultHandler().insertResult(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405


if __name__== '__main__':
    app.run()