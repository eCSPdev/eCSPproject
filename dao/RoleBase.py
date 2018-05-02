from config.dbconfig import pg_config
import psycopg2

class RoleBaseDAO:

    def validatePatient(self, username):
        print ('Patient')
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select username, token, logged " \
                        "from patients " \
                        "where (username = %s and logged = True ) " \
                        "or (email = %s and logged = True );"
                cursor.execute(query, (username, username, ))
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

    def validateAssistant(self, username):
        print('Assistant')
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select username, token, logged " \
                        "from assistants " \
                        "where (username = %s and logged = True ) " \
                        "or (email = %s and logged = True );"
                cursor.execute(query, (username, username, ))
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

    def validateDoctor(self, username):
        print('Doctor')
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select username, token, logged " \
                        "from doctor " \
                        "where (username = %s and logged = True ) " \
                        "or (email = %s and logged = True );"
                cursor.execute(query, (username, username, ))
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

    def updateloggedPatient(self, username, logged):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "update patients " \
                        "set logged=%s " \
                        "where username=%s " \
                        "returning logged; "
                cursor.execute(query, (logged, username,))
                logged = cursor.fetchone()[0]
                self.conn.commit()
                return logged
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")

    def updateloggedAssistant(self, username, logged):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "update assistants " \
                        "set logged=%s " \
                        "where username=%s " \
                        "returning logged; "
                cursor.execute(query, (logged, username,))
                logged = cursor.fetchone()[0]
                self.conn.commit()
                return logged
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")

    def updateloggedDoctor(self, username, logged):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "update doctor " \
                        "set logged=%s " \
                        "where username=%s " \
                        "returning logged; "
                cursor.execute(query, (logged, username,))
                logged = cursor.fetchone()[0]
                self.conn.commit()
                return logged
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")