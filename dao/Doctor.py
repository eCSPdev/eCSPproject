from config.dbconfig import pg_config
import psycopg2

class DoctorDAO:
    # def __init__(self):
    #     connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
    #         pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
    #     self.conn = psycopg2._connect(connection_url)

    def getAllDoctor(self):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select doctorid, licenseno, firstname, middlename, lastname, officename, phone, " \
                                "status, email, username, pssword "\
                        "from doctor;"
                cursor.execute(query)
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

    def getDoctorByID(self,did):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select doctor.doctorid, licenseno, firstname, middlename, lastname, officename, phone, " \
                        "status, email, username, pssword, addressid, street, aptno, city, st, country, zipcode " \
                        "from doctor " \
                        "inner join doctoraddress on doctor.doctorid = doctoraddress.doctorid " \
                        "where doctor.doctorid = %s;"
                cursor.execute(query, (did,))
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

    def getPsswordByID(self, doctorid):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select pssword " \
                        "from doctor " \
                        "where doctorid = %s;"
                cursor.execute(query, (doctorid,))
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
                        "from doctor " \
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

    def updateDoctorInfoByID(self, doctorid, licenseno, firstname, middlename, lastname, officename, phone, status,
                             email):
        try:

            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:

                cursor = self.conn.cursor()
                query = "update doctor " \
                        "set licenseno=%s, firstname=%s, middlename=%s, lastname=%s, officename=%s, phone=%s, status=%s, " \
                            "email=%s " \
                        "where doctorid=%s;"
                cursor.execute(query, ( licenseno, firstname, middlename, lastname, officename, phone, status,
                                        email,  doctorid, ))
                self.conn.commit()
                return doctorid
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")

    def updateDoctorAddress(self, doctorid, street, aptno, city, st, country, zipcode):
        try:

            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:

                cursor = self.conn.cursor()
                query = "update doctoraddress " \
                        "set street=%s, aptno=%s, city=%s, st=%s, country=%s, zipcode=%s " \
                        "where doctorid=%s " \
                        "returning addressid;"
                cursor.execute(query, (street, aptno, city, st, country, zipcode, doctorid,))
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

    def updateDoctorPssword(self, doctorid, pssword):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "update doctor " \
                        "set pssword=%s " \
                        "where doctorid=%s " \
                        "returning doctorid; "
                cursor.execute(query, (pssword, doctorid,))
                doctorid = cursor.fetchone()[0]
                self.conn.commit()
                return doctorid
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")


    def insertDoctorInfo(self, licenseno, firstname, middlename, lastname, officename, phone, email, username, pssword):
        status = True
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "insert into doctor (licenseno, firstname, middlename, lastname, officename, phone, status, email, username, pssword) " \
                        "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " \
                        "returning doctorid;"
                cursor.execute(query, (licenseno, firstname, middlename, lastname, officename, phone, status, email, username, pssword,))
                doctorid = cursor.fetchone()[0]
                self.conn.commit()
                print('new doctor id : ', doctorid)
                return doctorid
            except Exception as e:
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")

    def insertDoctorAddress(self, doctorid, street, aptno, city, st, country, zipcode):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "insert into doctoraddress (doctorid, street, aptno, city, st, country, zipcode) " \
                        "values (%s,%s,%s,%s,%s,%s,%s) " \
                        "returning addressid;"
                cursor.execute(query, (doctorid, street, aptno, city, st, country, zipcode,))
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

    def insertDoctorHistory(self, doctorid, licenseno, firstname, middlename, lastname,
                                        officename, phone, status, email, username, pssword,
                                        street, aptno, city, st, country, zipcode, changesdate):
        try:
            print("estoy en el try")
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                print("estoy en el otro try")
                cursor = self.conn.cursor()
                query = "insert into doctorhistory (doctorid, licenseno, firstname, middlename, lastname, "\
                                                "phone, status, email, username, pssword,"\
                                                "street, aptno, city, st, country, zipcode, changesdate)" \
                        "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " \
                        "returning historyid;"
                cursor.execute(query, (doctorid, licenseno, firstname, middlename, lastname,
                                                phone, status, email, username, pssword,
                                                street, aptno, city, st, country, zipcode, changesdate,))
                historyid = cursor.fetchone()[0]
                print(historyid)
                self.conn.commit()

                print(historyid)
                return historyid
            except Exception as e:
                print("estoy en el error der diablo")
                print("Query failed : ", e)
                return e
        except Exception as e:
            print("Error connecting to database.")
            return e
        finally:
            self.conn.close()
            print("Connection closed.")

    def verifyDoctor(self, firstname, middlename, lastname, licenseno):
        try:
            connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
                pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
            self.conn = psycopg2._connect(connection_url)

            try:
                cursor = self.conn.cursor()
                query = "select doctor.doctorid, licenseno, firstname, middlename, lastname, officename, phone, " \
                        "status, email, username, addressid, street, aptno, city, st, country, zipcode " \
                        "from doctor " \
                        "inner join doctoraddress on doctor.doctorid = doctoraddress.doctorid " \
                        "where (firstname=%s and middlename=%s and lastname=%s) or licenseno=%s;"
                cursor.execute(query, (firstname, middlename, lastname, licenseno,))
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