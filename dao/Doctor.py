from config.dbconfig import pg_config
import psycopg2

class DoctorDAO:
    def __init__(self):
        connection_url = "host=%s, port=%s, dbname=%s user=%s password=%s" % (
            pg_config['host'], pg_config['port'], pg_config['dbname'], pg_config['user'], pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllDoctor(self):
        cursor = self.conn.cursor()
        query = "select doctorid, licenseno, firstname, middlename, lastname, officename, phone, " \
                        "status, email, username, pssword "\
                "from doctor;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getDoctorByID(self,did):
        cursor = self.conn.cursor()
        query = "select doctor.doctorid, licenseno, firstname, middlename, lastname, officename, phone, " \
                "status, email, username, pssword, addressid, street, aptno, city, st, country, zipcode " \
                "from doctor " \
                "inner join doctoraddress on doctor.doctorid = doctoraddress.doctorid " \
                "where doctor.doctorid = %s;"
        cursor.execute(query, (did,))
        result = cursor.fetchone()
        return result

    def updateDoctorInfoByID(self, doctorid, licenseno, firstname, middlename, lastname, officename, phone, status,
                             email, username):
        cursor = self.conn.cursor()
        query = "update doctor " \
                "set licenseno=%s, firstname=%s, middlename=%s, lastname=%s, officename=%s, phone=%s, status=%s, " \
                    "email=%s, username=%s " \
                "where doctorid=%s;"
        cursor.execute(query, ( licenseno, firstname, middlename, lastname, officename, phone, status,
                                email, username, doctorid, ))
        self.conn.commit()
        return doctorid

    def updateDoctorAddress(self, doctorid, street, aptno, city, st, country, zipcode):
        cursor = self.conn.cursor()
        query = "update doctoraddress " \
                "set street=%s, aptno=%s, city=%s, st=%s, country=%s, zipcode=%s " \
                "where doctorid=%s" \
                "returning addressid;"
        cursor.execute(query, (street, aptno, city, st, country, zipcode, doctorid,))
        addressid = cursor.fetchone()[0]
        self.conn.commit()
        return addressid

    def insertDoctorInfo(self, licenseno, firstname, middlename, lastname, officename, phone, email, username, pssword):
        status = True
        cursor = self.conn.cursor()
        query = "insert into doctor (licenseno, firstname, middlename, lastname, officename, phone, status, email, username, pssword) " \
                "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " \
                "returning doctorid;"
        cursor.execute(query, (licenseno, firstname, middlename, lastname, officename, phone, status, email, username, pssword,))
        doctorid = cursor.fetchone()[0]
        self.conn.commit()
        print('new doctor id : ', doctorid)
        return doctorid
        # print('Insertando un nuevo asistente')

    def insertDoctorAddress(self, doctorid, street, aptno, city, st, country, zipcode):
        cursor = self.conn.cursor()
        query = "insert into doctoraddress (doctorid, street, aptno, city, st, country, zipcode) " \
                "values (%s,%s,%s,%s,%s,%s,%s) " \
                "returning addressid;"
        cursor.execute(query, (doctorid, street, aptno, city, st, country, zipcode,))
        addressid = cursor.fetchone()[0]
        self.conn.commit()
        print('new address id : ', addressid)
        return addressid
        # print('Insertando un nuevo address')

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

