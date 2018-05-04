from config.dbconfig import pg_config
import psycopg2

class AssistantDAO:

    # def __init__(self):
    #     connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
    #         pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllAssistants(self):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select assistantid, firstname, middlename, lastname, phone, status, email, username, pssword " \
                        "from assistants;"
                cursor.execute(query)
                result = []
                for row in cursor:
                    result.append(row)

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

    def getAssistantByID(self,assistantid):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select assistants.assistantid, firstname, middlename, lastname, phone, " \
                        "status, email, username, pssword, addressid, street, aptno, city, st, country, zipcode " \
                        "from assistants " \
                        "inner join assistantaddress on assistants.assistantid = assistantaddress.assistantid " \
                        "where assistants.assistantid = %s;"
                cursor.execute(query, (assistantid,))
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

    def getPsswordByID(self, assistantid):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select pssword " \
                        "from assistants " \
                        "where assistantid = %s;"
                cursor.execute(query, (assistantid,))
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

    def verifyUsername(self, username):

        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)
            try:
                cursor = self.conn.cursor()
                query = "select firstname, lastname, status " \
                        "from assistants " \
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

    def updateAssistantInfoByID(self, assistantid, firstname, middlename, lastname, phone, status,
                             email, pssword):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "update assistants " \
                        "set firstname=%s, middlename=%s, lastname=%s, phone=%s, status=%s, email=%s " \
                        "where assistantid=%s;"
                cursor.execute(query, ( firstname, middlename, lastname, phone, status,
                                        email, assistantid, ))
                self.conn.commit()
                return assistantid
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")

    def updateAssistantAddress(self, assistantid, street, aptno, city, st, country, zipcode):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "update assistantaddress " \
                        "set street=%s, aptno=%s, city=%s, st=%s, country=%s, zipcode=%s " \
                        "where assistantid=%s " \
                        "returning addressid;"
                cursor.execute(query, (street, aptno, city, st, country, zipcode, assistantid,))
                addressid = cursor.fetchone()[0]
                self.conn.commit()
                return addressid
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")

    def updateAssistantPssword(self, assistantid, pssword):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "update assistants " \
                        "set pssword=%s " \
                        "where assistantid=%s " \
                        "returning assistantid; "
                cursor.execute(query, (pssword, assistantid,))
                assistantid = cursor.fetchone()[0]
                self.conn.commit()
                return assistantid
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")


    def insertAssistantInfo(self, firstname, middlename, lastname, phone, email, username, pssword):
        status = True
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "insert into assistants (firstname, middlename, lastname, phone, status, email, username, pssword) " \
                        "values (%s,%s,%s,%s,%s,%s,%s,%s) " \
                        "returning assistantid;"
                cursor.execute(query, (firstname, middlename, lastname, phone, status, email, username, pssword,))
                assistantid = cursor.fetchone()[0]
                self.conn.commit()
                print('new assistant id : ', assistantid)
                return assistantid
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")

    def insertAssistantAddress(self, assistantid, street, aptno, city, st, country, zipcode):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "insert into assistantaddress (assistantid, street, aptno, city, st, country, zipcode) " \
                        "values (%s,%s,%s,%s,%s,%s,%s) " \
                        "returning addressid;"
                cursor.execute(query, (assistantid, street, aptno, city, st, country, zipcode,))
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
            self.conn.close()
            print("Connection closed.")

    def insertAssistantHistory(self, assistantid, firstname, middlename, lastname, phone, status, email, username,
                               pssword, street, aptno, city, st, country, zipcode, changesdate, DoctorSign):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "insert into assistanthistory (assistantid, firstname, middlename, lastname, phone, status, " \
                                                        "email, username, pssword, street, aptno, city, st, country, " \
                                                        "zipcode, changesdate, doctorid) " \
                        "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " \
                        "returning historyid;"
                cursor.execute(query, (assistantid, firstname, middlename, lastname, phone, status, email, username,
                               pssword, street, aptno, city, st, country, zipcode, changesdate, DoctorSign))
                historyid = cursor.fetchone()[0]
                self.conn.commit()

                return historyid
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")

    def verifyAssistant(self, firstname, middlename, lastname):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select assistants.assistantid, firstname, middlename, lastname, phone, " \
                        "status, email, username, addressid, street, aptno, city, st, country, zipcode " \
                        "from assistants " \
                        "inner join assistantaddress on assistants.assistantid = assistantaddress.assistantid " \
                        "where firstname=%s and middlename=%s and lastname=%s;"
                cursor.execute(query, (firstname, middlename, lastname,))
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