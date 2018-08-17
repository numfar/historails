import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'historailsdb.sqlite'),
    )

    app.config['UPLOAD_FOLDER'] = '/data/trainy/uploads'
    app.config['ACCESS_TOKEN'] = 'pk.eyJ1IjoibnVtZmFyIiwiYSI6ImNqN2F2NXdhcjBlcGMzMnN0a2wxaDd3YnoifQ.HZKACURfmAwSBLKkGVOprA'
    app.config['ALLOWED_EXTENSIONS'] = set(['csv','txt'])
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.update(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from mctrainface import db
    db.init_app(app)

    from mctrainface import auth, historails
    app.register_blueprint(auth.bp, url_prefix='/')
    app.register_blueprint(historails.bp)
    app.add_url_rule('/', endpoint='index')


    return app

