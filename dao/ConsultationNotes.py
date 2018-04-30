from config.dbconfig import pg_config
import psycopg2

class ConsultationNotesDAO:
    def __init__(self):
        connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
            pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getPatientConsultationNotes(self, pid):
        cursor = self.conn.cursor()
        query = "select * " \
                "from consultationnotes " \
                "where patientid = %s ; "
        result = []
        for row in cursor:
            result.append(row)
        print('result : ', result)
        return result

    def getConsultationNotesByID(self, pid, nid):
        cursor = self.conn.cursor()
        query = "select * " \
                "from consultationnotes " \
                "where patientid = %s and consultationnoteid = %s ; "
        cursor.execute(query, (pid, nid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insertConsultationNote(self, consultationnote, assistantid, doctorid, dateofupload, patientid, recordno):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "insert into consultationnotes (consultationnote, assistantid, doctorid, dateofupload, " \
                        "patientid, recordno) " \
                        "values (%s,%s,%s,%s,%s,%s) " \
                        "returning consultationnoteid;"
                cursor.execute(query, (consultationnote, assistantid, doctorid, dateofupload, patientid, recordno,))
                consultationnoteid = cursor.fetchone()[0]
                self.conn.commit()

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
                query = "select * " \
                        "from recordno;"
                cursor.execute(query, (recordno,))
                consultationnoteid = cursor.fetchone()[0]
                self.conn.commit()

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