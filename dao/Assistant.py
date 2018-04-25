from config.dbconfig import pg_config
import psycopg2

class AssistantDAO:

    def __init__(self):
        connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
            pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAssistants(self):
        cursor = self.conn.cursor()
        query = "select assistantid, firstname, middlename, lastname, phone, status, email, username, pssword " \
                "from assistants;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)

        print(result)
        return result

    def getDoctorByID(self,did):
        cursor = self.conn.cursor()
        query = "select assistants.assistantid, firstname, middlename, lastname, phone, " \
                "status, email, username, pssword, addressid, street, aptno, city, st, country, zipcode " \
                "from assistants " \
                "inner join assistantaddress on assistants.assistantid = assistantaddress.assistantid " \
                "where assistants.assistantid = %s;"
        cursor.execute(query, (did,))
        result = cursor.fetchone()
        return result