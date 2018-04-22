from flask import Flask, jsonify, request, render_template
from handler.Assistant import AssistantHandler
from handler.Doctor import DoctorHandler
from handler.Patient import PatientHandler
from handler.MedicalRecord import MedicalRecordHandler
from handler.ConsultationNotes import ConsultationNotesHandler
from handler.InitialForm import InitialFormHandler
from handler.Prescription import PrescriptionHandler
from handler.Referral import ReferralHandler
from handler.Result import ResultHandler

app = Flask(__name__)
app.debuger = True

@app.route('/')
@app.route('/eCSP')
@app.route('/eCSP/Home')
def home():
    return 'INDEX'

@app.route('/eCSP/PLogin')
def Plogin():
    return 'Patient Login Not Currently Available'

@app.route('/eCSP/DALogin')
def DAlogin():
    return 'Doctor and Assistant Login Not Currently Available'

#######################################
######### Second Draft ################
#######################################

#Get the Doctor Personal Information by Doctor ID
@app.route('/eCSP/Doctor/PersonalInformation', methods=['GET', 'PUT'])
def getDoctorByID():
    if request.method == 'GET':
        if not request.args:
            return jsonify(Error="No Patient ID Included."), 405
        else:
            return DoctorHandler().getDoctorByID(request.form)
    if request.method == 'PUT':
        DoctorHandler().updateDoctorInformation(request.form)
        return DoctorHandler().updateDoctorInformation(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get an Assistant List
@app.route('/eCSP/Doctor/AssistantList', methods=['GET'])
def getAllAssistant():
    if request.method == 'GET':
        return AssistantHandler().getAllAssistant()
    else:
        return jsonify(Error="Method not allowed."), 405

#Get an Assistant Personal Information by Assistant ID
@app.route('/eCSP/Doctor/Assistant/PersonalInformation', methods=['GET', 'PUT', 'POST'])
@app.route('/eCSP/Assistant/PersonalInformation', methods=['GET', 'PUT', 'POST'])
def getAssistantByID():
    if request.method == 'GET':
        return AssistantHandler().getAssistantByID(request.form)
    if request.method == 'PUT':
        return AssistantHandler().updateAssistant(request.form)
    if request.method == 'POST':
        return AssistantHandler().insertAssistant(request.form)
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
        return ConsultationNotesHandler().getAllColsultationNotes(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Consultation Note Information
@app.route('/eCSP/Doctor/Patient/ConsultationNotes', methods=['GET','POST'])
@app.route('/eCSP/Assistant/Patient/ConsultationNotes', methods=['GET','POST'])
@app.route('/eCSP/Patient/ConsultationNotes', methods=['GET','POST'])
def getConsultationNotesByID():
    if request.method == 'GET':
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
        return InitialFormHandler().getAllInitialForm(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Initial Form Information
@app.route('/eCSP/Doctor/Patient/InitialForm', methods=['GET','POST'])
@app.route('/eCSP/Assistant/Patient/InitialForm', methods=['GET','POST'])
@app.route('/eCSP/Patient/InitialForm', methods=['GET','POST'])
def getInitialFormByID():
    if request.method == 'GET':
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
        return PrescriptionHandler().getAllPrescription(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Prescription Information
@app.route('/eCSP/Doctor/Patient/Prescription', methods=['GET','POST'])
@app.route('/eCSP/Assistant/Patient/Prescription', methods=['GET','POST'])
@app.route('/eCSP/Patient/Prescription', methods=['GET','POST'])
def getPrescriptionByID():
    if request.method == 'GET':
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
        return ReferralHandler().getAllReferral(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Referral Information
@app.route('/eCSP/Doctor/Patient/Referral', methods=['GET','POST'])
@app.route('/eCSP/Assistant/Patient/Referral', methods=['GET','POST'])
@app.route('/eCSP/Patient/Referral', methods=['GET','POST'])
def getReferralByID():
    if request.method == 'GET':
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
        return ResultHandler().getAllResult(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#Get Patient Result Information
@app.route('/eCSP/Doctor/Patient/Result', methods=['GET','POST'])
@app.route('/eCSP/Assistant/Patient/Result', methods=['GET','POST'])
@app.route('/eCSP/Patient/Result', methods=['GET','POST'])
def getResultByID():
    if request.method == 'GET':
        return ResultHandler().getResultByID(request.form)
    if request.method == 'POST':
        return ResultHandler().insertResult(request.form)
    else:
        return jsonify(Error="Method not allowed."), 405

#######################################
########## First Draft ################
#######################################


#Get an Assistant Personal Information by Assistant ID
#@app.route('/eCSP/Assistant/PersonalInformation/<string:aid>')
#@app.route('/eCSP/Doctor/Assistant/PersonalInformation/<string:aid>')
#def getAssistantByID(aid):
#    return AssistantHandler().getAssistantByID(aid)

#Get Patient List
#@app.route('/eCSP/Doctor/PatientList')
#@app.route('/eCSP/Assistant/PatientList')
#def getAllMedicalRecord():
#    return MedicalRecordHandler().getAllMedicalRecord()

#Get a Patient Personal Information by Record Number
#@app.route('/eCSP/Patient/PersonalInformation/<string:pid>')
#@app.route('/eCSP/Assistant/Patient/PersonalInformation/<string:pid>')
#@app.route('/eCSP/Doctor/Patient/PersonalInformation/<string:pid>')
#def getPatientByID(pid):
#    return PatientHandler().getPatientByID(pid)

#Get Patient Consultation Note List
#@app.route('/eCSP/Doctor/ConsultationNotes/<string:rn>')
#@app.route('/eCSP/Assistant/ConsultationNotes/<string:rn>')
#@app.route('/eCSP/Patient/ConsultationNotes/<string:rn>')
#def getAllConsultationNotes(rn):
#    return ConsultationNotesHandler().getAllColsultationNotes(rn)

#Get Patient Consultation Note Information
#@app.route('/eCSP/Doctor/ConsultationNotes/<string:rn>/<string:nid>')
#@app.route('/eCSP/Assistant/ConsultationNotes/<string:rn>/<string:nid>')
#@app.route('/eCSP/Patient/ConsultationNotes/<string:rn>/<string:nid>')
#def getConsultationNotesByID(rn, nid):
#    return ConsultationNotesHandler().getConsultationNotesByID(rn, nid)

#Get Patient Initial Form List
#@app.route('/eCSP/Doctor/ConsultationNotes/<string:rn>')
#@app.route('/eCSP/Assistant/ConsultationNotes/<string:rn>')
#@app.route('/eCSP/Patient/ConsultationNotes/<string:rn>')
#def getAllInitialForm(rn):
#    return InitialFormHandler().getAllInitialForm(rn)

#Get Patient Initial Form Information
#@app.route('/eCSP/Doctor/InitialForm/<string:rn>/<string:ifid>')
#@app.route('/eCSP/Assistant/InitialForm/<string:rn>/<string:ifid>')
#@app.route('/eCSP/Patient/InitialForm/<string:rn>/<string:ifid>')
#def getInitialFormByID(rn, ifid):
#   return InitialFormHandler().getInitialFormByID(rn, ifid)

#Get Patient Prescription List
#@app.route('/eCSP/Doctor/Prescription/<string:rn>')
#@app.route('/eCSP/Assistant/Prescription/<string:rn>')
#@app.route('/eCSP/Patient/Prescription/<string:rn>')
#def getAllPrescription(rn):
#    return PrescriptionHandler().getAllPrescription(rn)

#Get Patient Prescription Information
#@app.route('/eCSP/Doctor/Prescription/<string:rn>/<string:pid>')
#@app.route('/eCSP/Assistant/Prescription/<string:rn>/<string:pid>')
#@app.route('/eCSP/Patient/Prescription/<string:rn>/<string:pid>')
#def getPrescriptionByID(rn, pid):
#    return PrescriptionHandler().getPrescriptionByID(rn, pid)

#Get Patient Referral List
#@app.route('/eCSP/Doctor/Referral/<string:rn>')
#@app.route('/eCSP/Assistant/Referral/<string:rn>')
#@app.route('/eCSP/Patient/Referral/<string:rn>')
#def getAllReferral(rn):
#    return ReferralHandler().getAllReferral(rn)

#Get Patient Referral Information
#@app.route('/eCSP/Doctor/Referral/<string:rn>/<string:rid>')
#@app.route('/eCSP/Assistant/Referral/<string:rn>/<string:rid>')
#@app.route('/eCSP/Patient/Referral/<string:rn>/<string:rid>')
#def getReferralByID(rn, rid):
#    return ReferralHandler().getReferralByID(rn, rid)

#Get Patient Result List
#@app.route('/eCSP/Doctor/Result/<string:rn>')
#@app.route('/eCSP/Assistant/Result/<string:rn>')
#@app.route('/eCSP/Patient/Result/<string:rn>')
#def getAllResult(rn):
#    return ResultHandler().getAllResult(rn)

#Get Patient Result Information
#@app.route('/eCSP/Doctor/Result/<string:rn>/<string:rid>')
#app.route('/eCSP/Assistant/Result/<string:rn>/<string:rid>')
#@app.route('/eCSP/Patient/Result/<string:rn>/<string:rid>')
#def getResultByID(rn, rid):
#    return ResultHandler().getResultByID(rn, rid)

if __name__== '__main__':
    app.run()