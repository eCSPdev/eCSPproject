from flask import Flask, jsonify, request
from handler.Assistant import AssistantHandler
from handler.Doctor import DoctorHandler
from handler.Patient import PatientHandler
from handler.MedicalRecord import MedicalRecordHandler
from handler.ConsultationNotes import ConsultationNotesHandler

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

if __name__=='__main__':
    app.run()