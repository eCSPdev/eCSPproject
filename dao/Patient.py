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
                        "status, email, username, pssword, recordno, consultationnoteid, prescriptionid, referralid, " \
                        "resultid, initialformid, insurancecompanyid, insurancecompany.companyname " \
                "from patients, patientaddress, medicalrecord, insurancecompany " \
                "where patients.patientid = medicalrecord.patientid " \
                "and patients.insurancecompanyid = insurancecompany.companyid";
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPatientByID(self,pid):
        cursor = self.conn.cursor()
        query = "select patients.patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, " \
                "status, email, username, pssword, addressid, street, aptno, city, st, country, zipcode, " \
                "recordno, consultationnoteid, prescriptionid, referralid, resultid, initialformid, " \
                "insurancecompanyid, companyname " \
                "from patients " \
                "inner join patientaddress on patients.patientid = patientaddress.patientid " \
                "inner join medicalrecord on patients.patientid = medicalrecord.patientid " \
                "inner join insurancecompany on patients.patientid = insurancecompany.companyid " \
                "where patients.patientid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def updatePatientInfoByID(self, patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, status, email,
                               username, pssword):
        cursor = self.conn.cursor()
        query = "update patients set firstname=%s, middlename=%s, lastname=%s, ssn=%s, birthdate=%s, gender=%s, phone=%s, " \
                "status=%s, email=%s, username=%s, pssword=%s where patientid=%s;"
        cursor.execute(query, ( firstname, middlename, lastname, ssn, birthdate, gender, phone, status, email,
                               username, pssword, patientid, ))
        self.conn.commit()
        return patientid

    def updatePatientAddress(self, addressid, patientid, street, aptno, city, st, country, zipcode):
        cursor = self.conn.cursor()
        query = "update patientaddress set street=%s, aptno=%s, city=%s, st=%s, country=%s, zipcode=%s " \
                "where patientid=%s and addressid=%s;"
        cursor.execute(query, (street, aptno, city, st, country, zipcode, patientid, addressid,))
        self.conn.commit()
        return addressid

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
        cursor.execute(query, (insurancecompanyid, patientid))
        insurancecompanyid = cursor.fetchone()[0]
        self.conn.commit()
        return insurancecompanyid

    def insertPatientInfo(self, firstname, middlename, lastname, ssn, birthdate, gender, phone, status,
                        email, username, pssword , insurancecompanyid):
        cursor = self.conn.cursor()
        query = "insert into patients (firstname, middlename, lastname, ssn, birthdate, gender, phone, " \
                "status, email, username, pssword, insurancecompanyid)" \
                "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " \
                "returning patientid;"
        cursor.execute(query, (firstname, middlename, lastname, ssn, birthdate, gender, phone, status,
                        email, username, pssword , insurancecompanyid,))
        patientid = cursor.fetchone()[0]
        self.conn.commit()

        return patientid