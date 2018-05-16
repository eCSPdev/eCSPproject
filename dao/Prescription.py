from config.dbconfig import pg_config
import psycopg2

class PrescriptionDAO:
    # def __init__(self):
    #     connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
    #         pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getPatientPrescription(self, pid):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select * " \
                        "from prescriptions " \
                        "where patientid = %s ; "
                cursor.execute(query, (pid, ))
                result = []
                for row in cursor:
                    result.append(row)
                print('result : ', result)
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

    def getPrescriptionByID(self, pid, nid):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select * " \
                        "from prescriptions " \
                        "where patientid = %s and prescriptionid = %s ; "
                cursor.execute(query, (pid, nid, ))
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

    def insertPrescription(self, filename, assistantusername, doctorusername, dateofupload, patientid, recordno):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "insert into prescriptions (filename, assistantusername, doctorusername, dateofupload, " \
                        "patientid, recordno) " \
                        "values (%s,%s,%s,%s,%s,%s) " \
                        "returning prescriptionid;"
                cursor.execute(query, (filename, assistantusername, doctorusername, dateofupload, patientid, recordno,))
                prescriptionid = cursor.fetchone()[0]
                self.conn.commit()

                return prescriptionid
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")

    def verifyRecordno(self, recordno):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select patientid " \
                        "from medicalrecord " \
                        "where recordno = %s;"
                cursor.execute(query, (recordno,))
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

    def getPrescriptionDates(self, pid):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select EXTRACT(YEAR FROM dateofupload) AS year, EXTRACT(MONTH FROM dateofupload) AS month " \
                        "from prescriptions " \
                        "where patientid = %s ; "
                cursor.execute(query, (pid, ))
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

    def getPrescriptionNameById(self, pid, prescriptionid):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select filename " \
                        "from prescriptions " \
                        "where patientid = %s and prescriptionid = %s ; "
                cursor.execute(query, (pid, prescriptionid, ))
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