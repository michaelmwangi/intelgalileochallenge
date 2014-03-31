__author__ = 'micheal'
import sqlite3 as db
import consts


class Admin:
    def __init__(self):
        self.conn = db.connect(consts.DBPATH)
        self.cursor = self.conn.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS Admin
         (
          email text,
          password text,
          loggedin text
         )'''
        self.cursor.execute(sql)
        self.conn.commit()

    def fetch_admin(self, email):
        sql = 'SELECT email FROM Admin WHERE email=?'
        self.cursor.execute(sql, (email, ))
        res = self.cursor.fetchone()
        return res

    def create_admin(self, email, password):
        sql = 'INSERT INTO Admin VALUES (?,?,?)'
        res = self.fetch_admin(email)
        if not res:
            self.cursor.execute(sql, (email, password, 'False'))
            self.conn.commit()
            return True
        else:
            return False

    def admin_login(self, email, password):
        sql = 'SELECT * FROM Admin WHERE email=? and password=?'
        res = self.cursor.execute(sql, (email, password)).fetchone()
        if res:
            status = 'True'
            sql = 'UPDATE Admin SET loggedin=? WHERE email=? AND password=?'
            self.cursor.execute(sql, (status, email, password))
            self.conn.commit()
            return True
        else:
            return False

    def admin_logout(self, email, password):
        sql = 'SELECT * FROM Admin WHERE email=? and password=?'
        res = self.cursor.execute(sql(email, password)).fetchone()
        if res:
            status = 'False'
            sql = 'UPDATE Admin SET loggedin=? WHERE email=? AND password=?'
            self.cursor.execute(sql, (status, email, password))
            self.conn.commit()
            return True
        else:
            return False

    def is_admin_logged_in(self, email):
        sql = 'SELECT loggedin FROM Admin WHERE email=?'
        status = self.cursor.execute(sql, (email, )).fetchone()
        if status:
            if status[0] == 'True':
                return True
        return False


class Humans:
    def __init__(self):
        sql = '''CREATE TABLE IF NOT EXISTS Humans
         (
          date text,
          totalhumans integer
         )
         '''
        self.conn = db.connect(consts.DBPATH)
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql)
        self.conn.commit()

    def fetch_humans(self, date):
        sql = 'SELECT totalhumans FROM Humans WHERE date=?'
        res = self.cursor.execute(sql, (date, )).fetchone()
        return res

    def update_humans(self, date, numhumans):
        oldtotal = self.fetch_humans(date)
        if oldtotal:
            newtotal = oldtotal[0] + numhumans
            sql = 'UPDATE Humans SET totalhumans=? WHERE date=?'
            self.cursor.execute(sql, (newtotal, date))
            self.conn.commit()
        else:
            #we have a new date entry
            sql = 'INSERT INTO Humans VALUES(?,?)'
            self.cursor.execute(sql, (date, numhumans))
            self.conn.commit()


class Events:
    def __init__(self):
        sql = '''CREATE TABLE IF NOT EXISTS Events
        (
            date text,
            name text,
            maxhumans integer,
            totalsignups integer
        )
         '''
        self.conn = db.connect(consts.DBPATH)
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql)
        self.conn.commit()

    def create_event(self, date, name, maxsignups):
        sql = 'INSERT INTO Events VALUES(?,?,?,?)'
        initotalsignups = 0
        self.cursor.execute(sql, (date, name, maxsignups, initotalsignups))
        self.conn.commit()

    def fetch_totalsignups(self, date):
        sql = 'SELECT totalsignups FROM Events WHERE date=?'
        res = self.cursor.execute(sql, (date, )).fetchone()
        return res

    def update_totalsignups(self, date, newones):
        res = self.fetch_totalsignups(date)
        if res:
            oldsignups = res[0]
            newsignups = oldsignups + newones
            sql = 'UPDATE Events SET totalsignups=? WHERE date=?'
            self.cursor.execute(sql, (newsignups, date))
            self.conn.commit()
            return True
        return False

    def fetch_events(self, date):
        sql = 'SELECT *FROM Events'
        events = self.cursor.execute(sql).fetchall()
        if events:
            futureevents = list()
            for event in events:
                edate = event[0]
                if date == edate:
                    futureevents.append(event)
                else:
                    #extract month and compare with current month
                    firstpos = edate.find('-')+1
                    lastpos = firstpos+2
                    month = int(edate[firstpos:lastpos])
                    firstpos = date.find('-')+1
                    lastpos = firstpos+2
                    curmonth = int(date[firstpos:lastpos])
                    curday = int(date[-2:])
                    eventday = int(edate[-2:])
                    if month >= curmonth and eventday >= curday:
                        futureevents.append(event)
            return futureevents
        else:
            return None


class EventSignups:
    def __init__(self):
        sql = '''CREATE TABLE IF NOT EXISTS EventSignups
        (
            email text,
            accesstoken text,
            eventname text,
            date text
        )
        '''
        self.conn = db.connect(consts.DBPATH)
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql)
        self.conn.commit()

    def check_double_signups(self, email, date, eventname):
        sql = 'SELECT *FROM EventSignups WHERE email=? AND date=? AND eventname=?'
        res = self.cursor.execute(sql, (email, date, eventname)).fetchone()
        return res

    def create_attendee(self, email, accesstoken, eventname, date):
        res = self.check_double_signups(email, date, eventname)
        if not res:
            sql = 'INSERT INTO EventSignups VALUES (?,?,?,?)'
            self.cursor.execute(sql, (email, accesstoken, eventname, date))
            self.conn.commit()
            return True
        return False


class Status:
    def __init__(self):
        sql = '''CREATE TABLE IF NOT EXISTS Status
        (
            temperature integer,
            light integer
        )
        '''
        self.conn = db.connect(consts.DBPATH)
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql)

    def update_status(self, temperature, light):
        sql = 'UPDATE Status SET temperature=? AND light=?'
        self.cursor.execute(sql, (temperature, light))
        self.conn.execute()

    def fetch_status(self):
        sql = 'SELECT * FROM Status '
        status = self.cursor.execute(sql).fetchone()
        return status

if __name__ == '__main__':
    pass


