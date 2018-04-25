from config.dbconfig import pg_config
import psycopg2

class PatientsDAO:
    def __init__(self):
        connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
            pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPatients(self):
        cursor = self.conn.cursor()
        query = "select patients.patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone," \
                        "status, email, username, pssword, insurancecompanyname, recordno, consultationnoteid, " \
                        "prescriptionid, referralid, resultid, initialformid " \
                "from patients " \
                "inner join patientaddress on patients.patientid = patientaddress.patientid " \
                "inner join medicalrecord on patients.patientid = medicalrecord.patientid;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        print(result)
        return result

    def getPatientByID(self,pid):
        cursor = self.conn.cursor()
        query = "select patients.patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, " \
                "status, email, username, pssword, insurancecompanyname, addressid, street, aptno, city, st, " \
                "country, zipcode, recordno, consultationnoteid, prescriptionid, referralid, resultid, initialformid " \
                "from patients " \
                "inner join patientaddress on patients.patientid = patientaddress.patientid " \
                "inner join medicalrecord on patients.patientid = medicalrecord.patientid " \
                "where patients.patientid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        print('patient FOUND id : ', result[0])
        return result

    def updatePatientInfoByID(self, patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, status, email,
                               username, insurancecompanyname):
        cursor = self.conn.cursor()
        query = "update patients set firstname=%s, middlename=%s, lastname=%s, ssn=%s, birthdate=%s, gender=%s, phone=%s, " \
                "status=%s, email=%s, username=%s, insurancecompanyname=%s where patientid=%s;"
        cursor.execute(query, ( firstname, middlename, lastname, ssn, birthdate, gender, phone, status, email,
                               username, insurancecompanyname, patientid, ))
        self.conn.commit()
        print('estoy dentro del update patient info')
        return patientid

    def updatePatientAddress(self, patientid, street, aptno, city, st, country, zipcode):
        cursor = self.conn.cursor()
        query = "update patientaddress set street=%s, aptno=%s, city=%s, st=%s, country=%s, zipcode=%s " \
                "where patientid=%s returning addressid;"
        cursor.execute(query, (street, aptno, city, st, country, zipcode, patientid,))
        addressid = cursor.fetchone()[0]
        self.conn.commit()
        print('estoy dentro del update patient address')
        return addressid
        # return patientid

    def getInsuranceCompanyID(self, companyname):
        cursor = self.conn.cursor()
        query = "select companyid " \
                "from insurancecompany " \
                "where companyname=%s;"
        cursor.execute(query, (companyname,))
        result = cursor.fetchone()
        return result

    def updatePatientInsuranceCompany(self, insurancecompanyid, patientid):
        cursor = self.conn.cursor()
        query = "update patients set companyid=%s " \
                "where patientid=%s" \
                "returning insurancecompanyid;"
        cursor.execute(query, (insurancecompanyid, patientid,))
        insurancecompanyid = cursor.fetchone()[0]
        self.conn.commit()
        return insurancecompanyid

    def insertInsuranceCompany(self, companyname):
        cursor = self.conn.cursor()
        query = "insert into insurancecompany (companyname) values (%s) returning companyid;"
        cursor.execute(query, (companyname,))
        insurancecompanyid = cursor.fetchone()[0]
        self.conn.commit()
        return insurancecompanyid

    def insertPatientInfo(self, firstname, middlename, lastname, ssn, birthdate, gender, phone,
                        email, username, pssword, insurancecompanyname):
        status = True
        cursor = self.conn.cursor()
        query = "insert into patients (firstname, middlename, lastname, ssn, birthdate, gender, phone, " \
                "status, email, username, pssword, insurancecompanyname) " \
                "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " \
                "returning patientid;"
        cursor.execute(query, (firstname, middlename, lastname, ssn, birthdate, gender, phone, status,
                        email, username, pssword , insurancecompanyname,))
        patientid = cursor.fetchone()[0]
        self.conn.commit()
        print('new patient id : ', patientid)
        return patientid
        # print('Insertando un nuevo paciente')

    def insertPatientAddress(self, patientid, street, aptno, city, st, country, zipcode):
        cursor = self.conn.cursor()
        query = "insert into patientaddress (patientid, street, aptno, city, st, country, zipcode) " \
                "values (%s,%s,%s,%s,%s,%s,%s) " \
                "returning addressid;"
        cursor.execute(query, (patientid, street, aptno, city, st, country, zipcode,))
        addressid = cursor.fetchone()[0]
        self.conn.commit()
        print('new address id : ', addressid)
        return addressid
        # print('Insertando un nuevo address')

    def insertVisit(self, recordno, patientid, visitdate, type):
        cursor = self.conn.cursor()
        query = "insert into visit (recordno, patientid, visitdate, type) " \
                "values (%s,%s,%s,%s) " \
                "returning visitdate;"
        cursor.execute(query, (recordno, patientid, visitdate, type,))
        visitdate = cursor.fetchone()[0]
        self.conn.commit()
        print('new visit date : ', visitdate)
        return visitdate
        # print('Insertando una nueva visita')

    def getAllPatientVisits(self, patientid):
        cursor = self.conn.cursor()
        query = "select visitdate " \
                "from visit " \
                "where patientid=%s;"
        cursor.execute(query, (patientid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertMedicalRecord(self, recordno, patientid):
        cursor = self.conn.cursor()
        query = "insert into medicalrecord (recordno, patientid) " \
                "values (%s,%s) " \
                "returning recordno;"
        cursor.execute(query, (recordno, patientid,))
        recordno = cursor.fetchone()[0]
        self.conn.commit()
        print('new visit date : ', recordno)
        return recordno
        # print('Insertando un nuevo record')

    def getAllMedicalRecords(self):
        cursor = self.conn.cursor()
        query = "select recordno " \
                "from medicalrecord;"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #PENDING
    def verifyPatient(self, firstname, lastname, ssn, birthdate, gender, status):
        cursor = self.conn.cursor()
        query = "select patients.patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, " \
                "status, email, username, pssword, insurancecompanyname, addressid, street, aptno, city, st, " \
                "country, zipcode, recordno, consultationnoteid, prescriptionid, referralid, resultid, initialformid " \
                "from patients " \
                "inner join patientaddress on patients.patientid = patientaddress.patientid " \
                "inner join medicalrecord on patients.patientid = medicalrecord.patientid " \
                "where (firstname=%s and lastname=%s and birthdate) or ssn=%s;"
        cursor.execute(query, (firstname, lastname, birthdate, ssn, status,))
        result = []
        for row in cursor:
            result.append(row)
        return result