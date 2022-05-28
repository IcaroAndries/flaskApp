from encodings import utf_8
from flask_restful import Resource
from control.apiResources.basicSources import ai_quotes

class pesquisa(Resource):
    def get(self, id):
        try:
            id = int(id)
            response = ai_quotes[id]
        except (KeyError, IndexError):
            response = {
                "error" : True,
                "msg" : "Nao existe registro nesse id"
            }
        except ValueError:
            response = {
                "error" : True,
                "msg" : "Favor inserir um valor inteiro para o Id"
            }
        else:
            response = ai_quotes[id]
        
        return response