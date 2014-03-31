import datetime
from src.bottle import *
from database import *
import hashlib
__author__ = 'micheal'


class Controller:
    def __init__(self):
        self.admindb = Admin()
        self.humansdb = Humans()
        self.eventdb = Events()
        self.esignups = EventSignups()
        self.statusdb = Status()

    def create_session(self, key, value):
        session = request.environ.get('beaker.session')
        session[str(key)] = str(value)
        session.save()

    def get_session(self, key):
        session = request.environ.get('beaker.session')
        try:
            session[str(key)]
            return session[str(key)]
        except KeyError:
            return None

    def create_hash(self, data):
        data = hashlib.sha256(data).hexdigest()
        return data

    def admin_login(self, email, password):
        password = self.create_hash(password)
        res = self.admindb.admin_login(email, password)
        if res:
            return True
        return False

    def is_adminloggedin(self, email):
        res = self.admindb.is_admin_logged_in(email)
        return res

    def create_admin(self, email, password):
        password = self.create_hash(password)
        res = self.admindb.create_admin(email, password)
        if res:
            return True
        return False

    def update_number_of_humans(self, numhumans):
        date = datetime.datetime.today().date().isoformat()
        self.humansdb.update_humans(date, numhumans)

    def create_event(self, eventname, eventdate, maxhumans):
        self.eventdb.create_event(eventdate, eventname, maxhumans)

    def fetch_events(self):
        todaydate = datetime.now().date().isoformat()
        print todaydate
        return self.eventdb.fetch_events(todaydate)

    def event_signup(self, eventname, email):
        #use email as access token since its unique
        accesstoken = email
        self.esignups.create_attendee(email, accesstoken, eventname, 'NOT_IMPLEMENTED_YET')
        return accesstoken

    def fetch_humans(self):
        #use current date for demo purposes only
        today_date = datetime.today().date().isoformat()
        tot_humans = self.humansdb.fetch_humans(today_date)
        if tot_humans:
            return tot_humans[0]
        return 0

    def fetch_status(self):
        status = self.statusdb.fetch_status()
        return status

    def update_status(self, temperature, light):
        self.statusdb.update_status(temperature, light)

    def add_command(self, command, value):
        pass

if __name__ == '__main__':
    pass
