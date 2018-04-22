from config.dbconfig import pg_config
import psycopg2

class DoctorDAO:
    def __init__(self):
        connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
            pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllDoctor(self):
        cursor = self.conn.cursor()
        query = "select doctorid, licenseno, firstname, middlename, lastname, officename, phone," \
                        "status, email, username, pssword"\
                "from doctor;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDoctorByID(self,did):
        cursor = self.conn.cursor()
        query = "select doctorid, firstname, middlename, lastname, officename,phone, " \
                "status, email, username, pssword, addressid, street, aptno, city, st, country, zipcode " \
                "from doctor " \
                "inner join doctoraddress on doctor.doctorid = doctoraddress.doctorid " \
                "where doctor.doctorid = %s;"
        cursor.execute(query, (did,))
        result = cursor.fetchone()
        return result

    def updateDoctorInfoByID(self, doctorid, licenseno, firstname, middlename, lastname,
                                                officename, phone, status, email, username,
                                                pssword):
        cursor = self.conn.cursor()
        query = "update doctor set firstname=%s, middlename=%s, lastname=%s, officename=%s, phone=%s, " \
                "status=%s, email=%s, username=%s, pssword=%s where doctorid=%s;"
        cursor.execute(query, ( doctorid, licenseno, firstname, middlename, lastname,
                                                officename, phone, status, email, username,
                                                pssword, doctorid, ))
        self.conn.commit()
        return doctorid

    def updateDoctorAddress(self, addressid, doctorid, street, aptno, city, st, country, zipcode):
        cursor = self.conn.cursor()
        query = "update doctoraddress set street=%s, aptno=%s, city=%s, st=%s, country=%s, zipcode=%s " \
                "where doctorid=%s and addressid=%s;"
        cursor.execute(query, (street, aptno, city, st, country, zipcode, doctorid, addressid,))
        self.conn.commit()
        return addressid

    def insertDoctorHistory(self, doctorid, licenseno, firstname, middlename, lastname,
                                        officename, phone, status, email, username, pssword,
                                        street, aptno, city, st, country, zipcode):
        cursor = self.conn.cursor()
        query = "insert into doctorhistory (doctorid, licenseno, firstname, middlename, lastname, "\
                                        "officename, phone, status, email, username, pssword,"\
                                        "street, aptno, city, st, country, zipcode)" \
                "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " \
                "returning historyid;"
        cursor.execute(query, (doctorid, licenseno, firstname, middlename, lastname,
                                        officename, phone, status, email, username, pssword,
                                        street, aptno, city, st, country, zipcode,))
        historyid = cursor.fetchone()[0]
        self.conn.commit()

        return historyid

