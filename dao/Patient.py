from config.dbconfig import pg_config
import psycopg2
import threading

class PatientsDAO:
    # def __init__(self):
    #     try:
    #         connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
    #             pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
    #         self.conn = psycopg2._connect(connection_url)
    #     except:
    #         print("Error connecting to database.")

    def getAllPatients(self):

        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select patients.patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone," \
                        "status, email, username, pssword, insurancecompanyname, recordno " \
                        "from patients " \
                        "inner join patientaddress on patients.patientid = patientaddress.patientid " \
                        "inner join medicalrecord on patients.patientid = medicalrecord.patientid;"
                cursor.execute(query)
                result = []
                for row in cursor:
                    result.append(row)
                print ('result : ', result)
                return result
            except Exception as e:
                print("Query failed : ", e)
                return e

        except Exception as e:
            print("Error connecting to database.")
            return e


        finally:
            self.conn.close()
            print("Connection closed.")

    def getPatientByID(self,pid):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select patients.patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, " \
                        "status, email, username, pssword, insurancecompanyname, addressid, street, aptno, city, st, " \
                        "country, zipcode, recordno " \
                        "from patients " \
                        "inner join patientaddress on patients.patientid = patientaddress.patientid " \
                        "inner join medicalrecord on patients.patientid = medicalrecord.patientid " \
                        "where patients.patientid = %s;"
                cursor.execute(query, (pid,))
                result = cursor.fetchone()
                return result
            except Exception as e:
                print("Query failed : ", e)
                return e

        except Exception as e:
            print("Error connecting to database.")
            return e

        finally:
            # self.conn.close()
            print("Connection closed.")

    def getPatientByRecordno(self, recordno):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select patients.patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, " \
                        "status, email, username, pssword, insurancecompanyname, addressid, street, aptno, city, st, " \
                        "country, zipcode, recordno " \
                        "from patients " \
                        "inner join patientaddress on patients.patientid = patientaddress.patientid " \
                        "inner join medicalrecord on patients.patientid = medicalrecord.patientid " \
                        "where recordno = %s;"
                cursor.execute(query, (recordno,))
                result = cursor.fetchone()
                return result
            except Exception as e:
                print("Query failed : ", e)
                return e

        except Exception as e:
            print("Error connecting to database.")
            return e

        finally:
            self.conn.close()
            print("Connection closed.")

    def getPatientByUsername(self, username):

        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select patients.patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, " \
                        "status, email, username, pssword, insurancecompanyname, addressid, street, aptno, city, st, " \
                        "country, zipcode, recordno, " \
                        "from patients " \
                        "inner join patientaddress on patients.patientid = patientaddress.patientid " \
                        "inner join medicalrecord on patients.patientid = medicalrecord.patientid " \
                        "where username = %s;"
                cursor.execute(query, (username,))
                result = cursor.fetchone()
                return result
            except Exception as e:
                print("Query failed : ", e)
                return e

        except Exception as e:
            print("Error connecting to database.")
            return e

        finally:
            self.conn.close()
            print("Connection closed.")

    def getPatientToken(self, patientid):

        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select token " \
                        "from patients " \
                        "where patientid = %s;"
                cursor.execute(query, (patientid,))
                result = cursor.fetchone()[0]
                return result
            except Exception as e:
                print("Query failed : ", e)
                return e

        except Exception as e:
            print("Error connecting to database.")
            return e

        finally:
            self.conn.close()
            print("Connection closed.")


    def verifyUsername(self, username):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select firstname, lastname, status " \
                        "from patients " \
                        "where username = %s;"
                cursor.execute(query, (username,))
                result = cursor.fetchone()
                return result
            except Exception as e:
                print("Query failed : ", e)
                return e

        except Exception as e:
            print("Error connecting to database.")
            return e

        finally:
            self.conn.close()
            print("Connection closed.")

    def updatePatientInfoByID(self, patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, status, email,
                               username, insurancecompanyname):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "update patients set firstname=%s, middlename=%s, lastname=%s, ssn=%s, birthdate=%s, gender=%s, phone=%s, " \
                        "status=%s, email=%s, username=%s, insurancecompanyname=%s where patientid=%s;"
                cursor.execute(query, ( firstname, middlename, lastname, ssn, birthdate, gender, phone, status, email,
                                       username, insurancecompanyname, patientid, ))
                self.conn.commit()
                print('estoy dentro del update patient info')
                return patientid
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e

        finally:
            # self.conn.close()
            print("Connection closed.")

    def updatePatientAddress(self, patientid, street, aptno, city, st, country, zipcode):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "update patientaddress set street=%s, aptno=%s, city=%s, st=%s, country=%s, zipcode=%s " \
                        "where patientid=%s returning addressid;"
                cursor.execute(query, (street, aptno, city, st, country, zipcode, patientid,))
                addressid = cursor.fetchone()[0]
                self.conn.commit()
                print('estoy dentro del update patient address')
                return addressid
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            # self.conn.close()
            print("Connection closed.")

    def getInsuranceCompanyID(self, companyname):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select companyid " \
                        "from insurancecompany " \
                        "where companyname=%s;"
                cursor.execute(query, (companyname,))
                result = cursor.fetchone()
                return result
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            # self.conn.close()
            print("Connection closed.")

    def updatePatientInsuranceCompany(self, insurancecompanyid, patientid):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "update patients set companyid=%s " \
                        "where patientid=%s" \
                        "returning insurancecompanyid;"
                cursor.execute(query, (insurancecompanyid, patientid,))
                insurancecompanyid = cursor.fetchone()[0]
                self.conn.commit()
                return insurancecompanyid
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            # self.conn.close()
            print("Connection closed.")

    def insertInsuranceCompany(self, companyname):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "insert into insurancecompany (companyname) values (%s) returning companyid;"
                cursor.execute(query, (companyname,))
                insurancecompanyid = cursor.fetchone()[0]
                self.conn.commit()
                return insurancecompanyid
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            # self.conn.close()
            print("Connection closed.")

    def insertPatientInfo(self, firstname, middlename, lastname, ssn, birthdate, gender, phone,
                        email, username, pssword, insurancecompanyname):
        status = True
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "insert into patients (firstname, middlename, lastname, ssn, birthdate, gender, phone, " \
                        "status, email, username, pssword, insurancecompanyname) " \
                        "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " \
                        "returning patientid;"
                cursor.execute(query, (firstname, middlename, lastname, ssn, birthdate, gender, phone, status,
                                email, username, pssword , insurancecompanyname,))
                patientid = cursor.fetchone()[0]
                self.conn.commit()
                return patientid
            except Exception as e:
                print("Query failed : ", e)
                return e

        except Exception as e:
            print("Error connecting to database.")
            return e

        finally:
            self.conn.close()
            print("Connection closed.")



    def insertPatientAddress(self, patientid, street, aptno, city, st, country, zipcode):

        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "insert into patientaddress (patientid, street, aptno, city, st, country, zipcode) " \
                        "values (%s,%s,%s,%s,%s,%s,%s) " \
                        "returning addressid;"
                cursor.execute(query, (patientid, street, aptno, city, st, country, zipcode,))
                addressid = cursor.fetchone()[0]
                self.conn.commit()
                print('new address id : ', addressid)
                return addressid
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            # self.conn.close()
            print("Connection closed.")

    def insertVisit(self, recordno, patientid, visitdate, type):

        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "insert into visit (recordno, patientid, visitdate, type) " \
                        "values (%s,%s,%s,%s) " \
                        "returning visitdate;"
                cursor.execute(query, (recordno, patientid, visitdate, type,))
                visitdate = cursor.fetchone()[0]
                self.conn.commit()
                print('new visit date : ', visitdate)
                return visitdate
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            # self.conn.close()
            print("Connection closed.")

    def getAllPatientVisits(self, patientid):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select visitdate " \
                        "from visit " \
                        "where patientid=%s;"
                cursor.execute(query, (patientid,))
                result = []
                for row in cursor:
                    result.append(row)
                return result
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            # self.conn.close()
            print("Connection closed.")

    def insertMedicalRecord(self, recordno, patientid):

        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "insert into medicalrecord (recordno, patientid) " \
                        "values (%s,%s) " \
                        "returning recordno;"
                cursor.execute(query, (recordno, patientid,))
                recordno = cursor.fetchone()[0]
                self.conn.commit()
                print('new visit date : ', recordno)
                return recordno
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            # self.conn.close()
            print("Connection closed.")

    def getAllMedicalRecords(self):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select recordno " \
                        "from medicalrecord;"
                cursor.execute(query,)
                result = []
                for row in cursor:
                    result.append(row)
                return result
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            # self.conn.close()
            print("Connection closed.")

    def getMedicalRecordByRecordno(self, recordno):

        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select recordno " \
                        "from medicalrecord " \
                        "where recordno = %s;"
                cursor.execute(query, (recordno,))
                result = cursor.fetchone()
                return result
            except Exception as e:
                print("Query failed : ", e)
                return e

        except Exception as e:
            print("Error connecting to database.")
            return e

        finally:
            self.conn.close()
            print("Connection closed.")

    def verifyPatient(self, firstname, middlename, lastname, ssn, birthdate):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select patients.patientid, firstname, middlename, lastname, ssn, birthdate, gender, phone, " \
                        "status, email, username, pssword, insurancecompanyname, addressid, street, aptno, city, st, " \
                        "country, zipcode, recordno " \
                        "from patients " \
                        "inner join patientaddress on patients.patientid = patientaddress.patientid " \
                        "inner join medicalrecord on patients.patientid = medicalrecord.patientid " \
                        "where (firstname=%s and middlename=%s, and lastname=%s and birthdate=%s) or ssn=%s;"
                cursor.execute(query, (firstname, middlename, lastname, birthdate, ssn,))
                result = []
                for row in cursor:
                    result.append(row)
                return result

            except Exception as e:
                print("Query failed : ", e)
                return e

        except Exception as e:
            print("Error connecting to database.")
            return e

        finally:
            self.conn.close()
            print("Connection closed.")