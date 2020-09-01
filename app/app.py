import os

import connexion
import connexion.resolver

DEBUG = os.environ.get('DEBUG', '') != ''

app = connexion.FlaskApp(
    __name__, specification_dir='../', debug=DEBUG,
    options={
        'swagger_ui': DEBUG,
    }
)

app.add_api(
    'bitsbox/swagger.yaml',
    resolver=connexion.resolver.RestyResolver('bitsbox'),
    validate_responses=DEBUG,
)

application = app.app
application.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
