from config.dbconfig import pg_config
import psycopg2

class ConsultationNotesDAO:
    # def __init__(self):
    #     connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
    #         pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getPatientConsultationNotes(self, pid):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select * " \
                        "from consultationnotes " \
                        "where patientid = %s ; "
                cursor.execute(query, (pid,))
                result = []
                #print ('result : ', result)
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

    def getConsultationNotesByID(self, pid, nid):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select * " \
                        "from consultationnotes " \
                        "where patientid = %s and consultationnoteid = %s ; "
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

    def insertConsultationNote(self, filename, assistantusername, doctorusername, dateofupload, patientid, recordno):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "insert into consultationnotes (filename, assistantusername, doctorusername, dateofupload, " \
                        "patientid, recordno) " \
                        "values (%s,%s,%s,%s,%s,%s) " \
                        "returning consultationnoteid;"
                cursor.execute(query, (filename, assistantusername, doctorusername, dateofupload, patientid, recordno,))
                consultationnoteid = cursor.fetchone()[0]
                self.conn.commit()
                print("new consultation note id : ", consultationnoteid)

                return consultationnoteid
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

    def getConsultationNotesDates(self, pid):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                print('entre al query de CN dates')
                cursor = self.conn.cursor()
                query = "(select EXTRACT(YEAR FROM dateofupload) AS year, EXTRACT(MONTH FROM dateofupload) AS month " \
                        "from consultationnotes " \
                        "where patientid = %s ) " \
                        "Union " \
                        "(select EXTRACT(YEAR FROM dateofupload) AS year, EXTRACT(MONTH FROM dateofupload) AS month " \
                        "from initialform " \
                        "where patientid = %s ) " \
                        "Union " \
                        "(select EXTRACT(YEAR FROM dateofupload) AS year, EXTRACT(MONTH FROM dateofupload) AS month " \
                        "from prescriptions " \
                        "where patientid = %s ) " \
                        "Union " \
                        "(select EXTRACT(YEAR FROM dateofupload) AS year, EXTRACT(MONTH FROM dateofupload) AS month " \
                        "from referrals " \
                        "where patientid = %s ) " \
                        "Union " \
                        "(select EXTRACT(YEAR FROM dateofupload) AS year, EXTRACT(MONTH FROM dateofupload) AS month " \
                        "from results " \
                        "where patientid = %s ) "
                cursor.execute(query, (pid, pid, pid, pid, pid, ))
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

    def getPatientFiles(self, pid, year, month):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                print('entre al query de patient files')
                cursor = self.conn.cursor()
                query = "(select patientid, consultationnoteid as fileid, filename, 'consultationnote' as type, dateofupload, doctorusername, assistantusername, recordno " \
                        "from consultationnotes " \
                        "where patientid = %s and EXTRACT(YEAR FROM dateofupload) = %s and EXTRACT(MONTH FROM dateofupload) = %s ) " \
                        "Union " \
                        "(select patientid, initialformid as fileid, filename, 'initialform' as type, dateofupload, doctorusername, assistantusername, recordno " \
                        "from initialform " \
                        "where patientid = %s and EXTRACT(YEAR FROM dateofupload) = %s and EXTRACT(MONTH FROM dateofupload) = %s) " \
                        "Union " \
                        "(select patientid, prescriptionid as fileid, filename, 'prescription' as type, dateofupload, doctorusername, assistantusername, recordno " \
                        "from prescriptions " \
                        "where patientid = %s and EXTRACT(YEAR FROM dateofupload) = %s and EXTRACT(MONTH FROM dateofupload) = %s) " \
                        "Union " \
                        "(select patientid, referralid as fileid, filename, 'referral' as type, dateofupload, doctorusername, assistantusername, recordno " \
                        "from referrals " \
                        "where patientid = %s and EXTRACT(YEAR FROM dateofupload) = %s and EXTRACT(MONTH FROM dateofupload) = %s) " \
                        "Union " \
                        "(select patientid, resultid as fileid, filename, 'result' as type, dateofupload, doctorusername, assistantusername, recordno " \
                        "from results " \
                        "where patientid = %s and EXTRACT(YEAR FROM dateofupload) = %s and EXTRACT(MONTH FROM dateofupload) = %s) "
                cursor.execute(query, (pid, year, month, pid, year, month, pid, year, month, pid, year, month, pid, year, month,))
                result = []
                #print ('result : ', result)
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

    def getConsultatioNoteNameById(self, pid, consultationnoteid):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select filename " \
                        "from consultationnotes " \
                        "where patientid = %s and consultationnoteid = %s ; "
                cursor.execute(query, (pid, consultationnoteid, ))
                result = cursor.fetchone()
                print("result : ",result)
                if result == None:
                    result = ["None"]
                    print("filename result : ", result)
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

