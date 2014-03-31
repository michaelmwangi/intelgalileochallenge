from src.controller import *
from beaker.middleware import SessionMiddleware


sessionopts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

app = SessionMiddleware(app(), sessionopts)


@route('/')
@view('adminlogin')
def show_home():
    return {}


@route('/admin')
@view('admin')
def showadminpage():
    cont = Controller()
    res = cont.get_session('user')
    if res:
        if cont.is_adminloggedin(res):
            return {}
    else:
        redirect('/')


@route('/events')
@view('event')
def showeventpage():
    cont = Controller()
    events = cont.fetch_events()
    return {'events': events}


@route('/setdata/<humans>/<temp>/<light>')
def set_data(humans, temp, light):
    #set data from the intel galileo into the database
    cont = Controller()
    cont.update_number_of_humans(int(humans))
    cont.update_status(int(temp), int(light))


@route('/getdata')
def get_data():
    #update site with data from intel galileo
    return '0'

@post('/adminlogin')
def handle_login_attempt():
    cont = Controller()
    email = request.forms.get('email')
    password = request.forms.get('password')
    res = cont.admin_login(email, password)
    print str(res)
    if res:
        cont.create_session('user', email)
        redirect('/admin')
    redirect('/')


@post('/createevent')
def create_event():
    eventname = request.forms.get('eventname')
    eventdate = request.forms.get('eventdate')
    maxhumans = request.forms.get('maxhumans')
    if len(eventname) and len(eventdate) and len(maxhumans):
        #we have all fields filled
        try:
            maxhumans = int(maxhumans)
            cont = Controller()
            cont.create_event(eventname, eventdate, maxhumans)
            redirect('/admin')
        except ValueError:
            redirect('/error/cannot convert string to integer')


@post('/eventsignup')
def event_signup():
    eventname = request.forms.get('eventname')
    email = request.forms.get('email')
    cont = Controller()
    if len(email):
        accesstoken = cont.event_signup(eventname, email)
        mesg = 'Thank you for signing up ,your acces token is ' + accesstoken
        redirect('/info/'+mesg)
    else:
        redirect('/info/Please include your email address for identification')

@route('/info/<msg>')
@view('info')
def show_info(msg):
    return {'info': msg}

@route('/staticfiles/<filepath:path>')
def static_serve(filepath):
    return static_file(filepath, root='staticfiles')

if __name__ == '__main__':
    debug(True)
    run(port='8000', reloader=True, app=app)