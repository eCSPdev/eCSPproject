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
        cursor.execute(query, pid, )
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

    def insertConsultationNote(self):
        return "In process"