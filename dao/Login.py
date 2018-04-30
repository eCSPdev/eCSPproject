from config.dbconfig import pg_config
import psycopg2

class LoginDAO:
    def __init__(self):
        connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
            pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def validatePatient(self, username, pssword):
        cursor = self.conn.cursor()
        query = "select username " \
                "from patients " \
                "where (username = %s and pssword = %s) " \
                "or (email = %s and pssword = %s);"
        cursor.execute(query, (username, pssword, username, pssword, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def validateDoctor(self, username, pssword):
        cursor = self.conn.cursor()
        query = "select username " \
                "from doctor " \
                "where (username = %s and pssword = %s) " \
                "or (email = %s and pssword = %s); "
        cursor.execute(query, (username, pssword, username, pssword))
        result = []
        for row in cursor:
            result.append(row)
        #print(result)
        return result

    def validateAssistant(self, username, pssword):
        cursor = self.conn.cursor()
        query = "select username " \
                "from assistants " \
                "where (username = %s and pssword = %s) " \
                "or (email = %s and pssword = %s); "
        cursor.execute(query, (username, pssword, username, pssword))
        result = []
        for row in cursor:
            result.append(row)
        #print(result)
        return result