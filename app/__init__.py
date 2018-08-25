import os

from flask import Flask

def create_app(test_config=None):
    flaskapp = Flask(__name__, instance_relative_config=True)
    flaskapp.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(flaskapp.instance_path, 'historailsdb.sqlite'),
    )

    flaskapp.config['UPLOAD_FOLDER'] = '/data/trainy/uploads'
    flaskapp.config['FROM_YEAR'] = '1855'    
    flaskapp.config['ACCESS_TOKEN'] = 'pk.eyJ1IjoibnVtZmFyIiwiYSI6ImNqN2F2NXdhcjBlcGMzMnN0a2wxaDd3YnoifQ.HZKACURfmAwSBLKkGVOprA'
    flaskapp.config['ALLOWED_EXTENSIONS'] = set(['csv','txt'])
    if test_config is None:
        flaskapp.config.from_pyfile('config.py', silent=True)
    else:
        flaskapp.config.update(test_config)

    try:
        os.makedirs(flaskapp.instance_path)
    except OSError:
        pass

    from app import db
    db.init_app(flaskapp)

    from app import auth, historails
    flaskapp.register_blueprint(auth.bp, url_prefix='/')
    flaskapp.register_blueprint(historails.bp)
    flaskapp.add_url_rule('/', endpoint='index')

    return flaskapp

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)