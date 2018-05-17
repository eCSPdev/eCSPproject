from config.dbconfig import pg_config
import psycopg2

class LoginDAO:
    """def __init__(self):
        connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
            pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)
    """

    def validatePatient(self, username, pssword):
        print('')
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select username, status, deactivationdate, firstname, middlename, lastname, patients.patientid, recordno " \
                        "from patients " \
                        "inner join medicalrecord on patients.patientid = medicalrecord.patientid " \
                        "where (username = %s and pssword = %s) " \
                        "or (email = %s and pssword = %s);"
                cursor.execute(query, (username, pssword, username, pssword, ))
                result = cursor.fetchone()
                print(result)
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


    def validateDoctor(self, username, pssword):
        try:
            print('validateDoctor')
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select username, status, deactivationdate, firstname, middlename, lastname, doctorid " \
                        "from doctor " \
                        "where (username = %s and pssword = %s) " \
                        "or (email = %s and pssword = %s); "
                cursor.execute(query, (username, pssword, username, pssword))
                result = cursor.fetchone()
                #print(result)
                return result
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            #self.conn.close()
            print("Connection closed.")

    def validateAssistant(self, username, pssword):
        try:
            print('validateAssistant')
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select username, status, deactivationdate, firstname, middlename, lastname,assistantid " \
                        "from assistants " \
                        "where (username = %s and pssword = %s) " \
                        "or (email = %s and pssword = %s); "
                cursor.execute(query, (username, pssword, username, pssword))
                result = cursor.fetchone()
                print(result)
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


    def updateloggedPatient(self, username, token, logged):
        print ('token : ', token)
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "update patients " \
                        "set token=%s, logged=%s " \
                        "where username=%s; "
                cursor.execute(query, (token, logged, username,))
                self.conn.commit()
                print ('token : ', token)
                return token
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")

    def updateloggedAssistant(self, username, token, logged):
        print ('token : ', token)
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "update assistants " \
                        "set token=%s, logged=%s " \
                        "where username=%s; "
                cursor.execute(query, (token, logged, username,))
                self.conn.commit()
                print ('token : ', token )
                return token
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")

    def updateloggedDoctor(self, username, token, logged):
        print ('token : ', token)
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "update doctor " \
                        "set token=%s, logged=%s " \
                        "where username=%s; "
                cursor.execute(query, (token, logged, username,))
                self.conn.commit()
                print ('token : ', token)
                return token
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")