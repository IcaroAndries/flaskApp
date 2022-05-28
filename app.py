from flask import Flask
from flask_restful import Api
from control.interfaces.principal import pesquisa

app = Flask(__name__)
api = Api(app)

api.add_resource(pesquisa, '/pesquisa/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)