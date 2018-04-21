from config.dbconfig import pg_config
import psycopg2

class PatientsDAO:
    def __init__(self):
        connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
            pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPatients(self):
        cursor = self.conn.cursor()
        query = "select * from patients;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPatientByID(self,pid):
        cursor = self.conn.cursor()
        query = "select * from patients where patientid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result