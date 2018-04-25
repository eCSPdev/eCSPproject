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

    def getAssistantByID(self,assistantid):
        cursor = self.conn.cursor()
        query = "select assistants.assistantid, firstname, middlename, lastname, phone, " \
                "status, email, username, pssword, addressid, street, aptno, city, st, country, zipcode " \
                "from assistants " \
                "inner join assistantaddress on assistants.assistantid = assistantaddress.assistantid " \
                "where assistants.assistantid = %s;"
        cursor.execute(query, (assistantid,))
        result = cursor.fetchone()
        return result

    def updateAssistantInfoByID(self, assistantid, firstname, middlename, lastname, phone, status,
                             email, username):
        cursor = self.conn.cursor()
        query = "update assistants " \
                "set firstname=%s, middlename=%s, lastname=%s, phone=%s, status=%s, email=%s, username=%s " \
                "where assistantid=%s;"
        cursor.execute(query, ( firstname, middlename, lastname, phone, status,
                                email, username, assistantid, ))
        self.conn.commit()
        return assistantid

    def updateAssistantAddress(self, assistantid, street, aptno, city, st, country, zipcode):
        cursor = self.conn.cursor()
        query = "update assistantaddress " \
                "set street=%s, aptno=%s, city=%s, st=%s, country=%s, zipcode=%s " \
                "where assistantid=%s " \
                "returning addressid;"
        cursor.execute(query, (street, aptno, city, st, country, zipcode, assistantid,))
        addressid = cursor.fetchone()[0]
        self.conn.commit()
        return addressid

    def insertAssistantInfo(self, firstname, middlename, lastname, phone, email, username, pssword):
        status = True
        cursor = self.conn.cursor()
        query = "insert into assistants (firstname, middlename, lastname, phone, status, email, username, pssword) " \
                "values (%s,%s,%s,%s,%s,%s,%s,%s) " \
                "returning assistantid;"
        cursor.execute(query, (firstname, middlename, lastname, phone, status, email, username, pssword,))
        assistantid = cursor.fetchone()[0]
        self.conn.commit()
        print('new assistant id : ', assistantid)
        return assistantid
        # print('Insertando un nuevo asistente')

    def insertAssistantAddress(self, assistantid, street, aptno, city, st, country, zipcode):
        cursor = self.conn.cursor()
        query = "insert into assistantaddress (assistantid, street, aptno, city, st, country, zipcode) " \
                "values (%s,%s,%s,%s,%s,%s,%s) " \
                "returning addressid;"
        cursor.execute(query, (assistantid, street, aptno, city, st, country, zipcode,))
        addressid = cursor.fetchone()[0]
        self.conn.commit()
        print('new address id : ', addressid)
        return addressid
        # print('Insertando un nuevo address')

    def insertAssistantHistory(self, assistantid, firstname, middlename, lastname,
                                        phone, status, email, username, pssword,
                                        street, aptno, city, st, country, zipcode):
        cursor = self.conn.cursor()
        query = "insert into assistanthistory (assisantid, firstname, middlename, lastname, phone, status, email, " \
                                                "username, pssword, street, aptno, city, st, country, zipcode) " \
                "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " \
                "returning historyid;"
        cursor.execute(query, (assistantid,firstname, middlename, lastname,
                                        phone, status, email, username, pssword,
                                        street, aptno, city, st, country, zipcode,))
        historyid = cursor.fetchone()[0]
        self.conn.commit()

        return historyid