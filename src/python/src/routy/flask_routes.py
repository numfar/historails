import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort
from flask import send_from_directory
from werkzeug.utils import secure_filename

from file_coordinates_extractor import TrainStopp, Route, FileCoordinatesExtractor
from cruddymodule import Crudder

UPLOAD_FOLDER = '/data/trainy/uploads' 
ALLOWED_EXTENSIONS = set(['csv','txt'])
app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'route.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/show')
def show():
    db = get_db()
    cur = db.execute('select route_name from route')
    entries = cur.fetchall()
    html = '<ul>'
    for row in entries:
        html += '<li>' + row[0] + '</li>'
    html += '</ul>'
    return html

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('confirm_route',filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/comfirm-route/<filename>')
def confirm_route(filename):
    conn = sqlite3.connect('routy/route.db')
    db = conn.cursor()
    crudder = Crudder(db)
    extractor = FileCoordinatesExtractor()
    route = extractor.extract_route(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    added_route = crudder.add_route(route)
    conn.commit()
    html = '<h3>Added route: ' + added_route.name + '</h3>'
    html += '<ul>'
    for conn in added_route.connections:
        html += '<li>' + ', '.join([conn.node1.name,str(conn.node1.longitude),str(conn.node1.latitude)]) + ' | ' + ', '.join([conn.node2.name,str(conn.node2.longitude),str(conn.node2.latitude)]) + '</li>'
    html += '</ul>'
    return html

@app.route('/add',methods=['POST'])
def add_single_route():
    extractor = FileCoordinatesExtractor()
    filename = 'NOPE'
    route = extractor.extract_route(filename)

    #db = get_db()
    #
    html = '<h3>Added route: ' + route.name + '</h3>'
    html += '<ul>'
    for stop in route.stops:
        html += '<li>' + ', '.join([stop.name,stop.x,stop.y]) + '</li>'
    html += '</ul>'

    return html

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

if __name__ == '__main__':
    app.run()

