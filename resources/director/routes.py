from flask import request
from flask.views import MethodView
from uuid import uuid4
from flask_smorest import abort

from schemas import DirectorSchema
from . import bp

# from db import director
from models.director_model import DirectorModel

from app import db

@bp.route('/director')
class UserList(MethodView):
    
    @bp.response(200, DirectorSchema(many=True))
    def get(self):
        return DirectorModel.query.all() #.all should return all items
        
    @bp.arguments(DirectorSchema)
    @bp.response(201, DirectorSchema)
    def post(self, data):
    
        try:
            director = DirectorModel()
            director.from_dict(data)
            director.save_director()
            return {'success': f'{data["username"]} added'}, 201
        except:
            return {'error': 'username or email already taken; try again'}, 400

@bp.route('/director/<int:id>')
class User(MethodView):
    
    @bp.response(200, DirectorSchema)
    def get(self, id):
        director = DirectorModel.query.get(id)
        if director:
            return director
        else:
            abort(400, msg='not a valid entry')


    @bp.arguments(DirectorSchema)
    def put(self, data, id):
        director = DirectorModel.query.get(id)
        if director:
            director.from_dict(data)
            director.save_director()
            return {'message': 'director updated'}, 200
        else:
            abort(400, message='not a valid entry')
     

    def delete(self, id):
        director = DirectorModel.query.get(id)
        if director:
            director.del_director()
            return {'message': 'director deleted'}, 200
        abort(400, message='not a valid entry')
        

