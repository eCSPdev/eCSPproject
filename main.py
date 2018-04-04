from flask import Flask, jsonify, request
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

@app.route('/eCSP/Home')
def home():
    return 'Welcome to eCSP Home Page'

@app.route('/eCSP/PLogin')
def Plogin():
    return "Patient Login Not Currently Available"

@app.route('/eCSP/DALogin')
def DAlogin():
    return "Doctor and Assistant Login Not Currently Available"

#Get the Doctor Personal Information by Doctor ID
@app.route('/eCSP/Doctor/PersonalInformation/<string:did>')
def getDoctorByID(did):
    return DoctorHandler().getDoctorByID(did)

#Get an Assistant List
@app.route('/eCSP/Doctor/AssistantList')
def getAllAssistant():
    return AssistantHandler().getAllAssistant()

#Get an Assistant Personal Information by Assistant ID
@app.route('/eCSP/Assistant/PersonalInformation/<string:aid>')
@app.route('/eCSP/Doctor/Assistant/PersonalInformation/<string:aid>')
def getAssistantByID(aid):
    return AssistantHandler().getAssistantByID(aid)

#Get Patient List
@app.route('/eCSP/Doctor/PatientList')
@app.route('/eCSP/Assistant/PatientList')
def getAllMedicalRecord():
    return MedicalRecordHandler().getAllMedicalRecord()

#Get a Patient Personal Information by Record Number
@app.route('/eCSP/Patient/PersonalInformation/<string:pid>')
@app.route('/eCSP/Assistant/Patient/PersonalInformation/<string:pid>')
@app.route('/eCSP/Doctor/Patient/PersonalInformation/<string:pid>')
def getPatientByID(pid):
    return PatientHandler().getPatientByID(pid)

#Get Patient Consultation Note List
@app.route('/eCSP/Doctor/ConsultationNotes/<string:rn>')
@app.route('/eCSP/Assistant/ConsultationNotes/<string:rn>')
@app.route('/eCSP/Patient/ConsultationNotes/<string:rn>')
def getAllConsultationNotes(rn):
    return ConsultationNotesHandler().getAllColsultationNotes(rn)

#Get Patient Consultation Note Information
@app.route('/eCSP/Doctor/ConsultationNotes/<string:rn>/<string:nid>')
@app.route('/eCSP/Assistant/ConsultationNotes/<string:rn>/<string:nid>')
@app.route('/eCSP/Patient/ConsultationNotes/<string:rn>/<string:nid>')
def getConsultationNotesByID(rn, nid):
    return ConsultationNotesHandler().getConsultationNotesByID(rn, nid)

#Get Patient Initial Form List
@app.route('/eCSP/Doctor/ConsultationNotes/<string:rn>')
@app.route('/eCSP/Assistant/ConsultationNotes/<string:rn>')
@app.route('/eCSP/Patient/ConsultationNotes/<string:rn>')
def getAllInitialForm(rn):
    return InitialFormHandler().getAllInitialForm(rn)

#Get Patient Initial Form Information
@app.route('/eCSP/Doctor/InitialForm/<string:rn>/<string:ifid>')
@app.route('/eCSP/Assistant/InitialForm/<string:rn>/<string:ifid>')
@app.route('/eCSP/Patient/InitialForm/<string:rn>/<string:ifid>')
def getInitialFormByID(rn, ifid):
    return InitialFormHandler().getInitialFormByID(rn, ifid)

#Get Patient Prescription List
@app.route('/eCSP/Doctor/Prescription/<string:rn>')
@app.route('/eCSP/Assistant/Prescription/<string:rn>')
@app.route('/eCSP/Patient/Prescription/<string:rn>')
def getAllPrescription(rn):
    return PrescriptionHandler().getAllPrescription(rn)

#Get Patient Prescription Information
@app.route('/eCSP/Doctor/Prescription/<string:rn>/<string:pid>')
@app.route('/eCSP/Assistant/Prescription/<string:rn>/<string:pid>')
@app.route('/eCSP/Patient/Prescription/<string:rn>/<string:pid>')
def getPrescriptionByID(rn, pid):
    return PrescriptionHandler().getPrescriptionByID(rn, pid)

#Get Patient Referral List
@app.route('/eCSP/Doctor/Referral/<string:rn>')
@app.route('/eCSP/Assistant/Referral/<string:rn>')
@app.route('/eCSP/Patient/Referral/<string:rn>')
def getAllReferral(rn):
    return ReferralHandler().getAllReferral(rn)

#Get Patient Referral Information
@app.route('/eCSP/Doctor/Referral/<string:rn>/<string:rid>')
@app.route('/eCSP/Assistant/Referral/<string:rn>/<string:rid>')
@app.route('/eCSP/Patient/Referral/<string:rn>/<string:rid>')
def getReferralByID(rn, rid):
    return ReferralHandler().getReferralByID(rn, rid)

#Get Patient Result List
@app.route('/eCSP/Doctor/Result/<string:rn>')
@app.route('/eCSP/Assistant/Result/<string:rn>')
@app.route('/eCSP/Patient/Result/<string:rn>')
def getAllResult(rn):
    return ResultHandler().getAllResult(rn)

#Get Patient Result Information
@app.route('/eCSP/Doctor/Result/<string:rn>/<string:rid>')
@app.route('/eCSP/Assistant/Result/<string:rn>/<string:rid>')
@app.route('/eCSP/Patient/Result/<string:rn>/<string:rid>')
def getResultByID(rn, rid):
    return ResultHandler().getResultByID(rn, rid)

if __name__=='__main__':
    app.run()