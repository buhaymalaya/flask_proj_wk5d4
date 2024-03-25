from flask import request, jsonify, json
from flask.views import MethodView
from flask_smorest import abort
from uuid import uuid4

from schemas import MovieSchema
from . import bp

# from db import directors, movies

# from models.movie_model import MovieModel

from app import db 

@bp.route('/movie')
class MovieList(MethodView):
    
    @bp.arguments(MovieSchema)
    def post(self, movie_data):
        if movie_data['director'] not in director:
            return {"message": "director does not exist"}, 400
        movie_id = uuid4().hex
        movie[movie_id] = movie_data

        return {
            'message': "Movie created",
            'movie-id': movie_id
            }, 201

    @bp.response(200, MovieSchema(many=True))
    def get(self):
        return list(movie.values())

@bp.route('/movie/<movie_id>')
class Post(MethodView):

    @bp.response(200, MovieSchema)
    def get(self, movie_id):
        try: 
            return movie[movie_id]
        except KeyError:
            return {'message':"invalid movie"}, 400

    @bp.arguments(MovieSchema)
    def put(self, movie_data, movie_id):
        if movie_id in movie:
            movie[movie_id] = {k:v for k,v in movie_data.items() if k != 'id'} 

            return {'message': f'movie: {movie_id} updated'}, 201
        
        return {'message': "invalid movie"}, 400

    def delete(self, movie_id):

        if movie_id not in movie:
            return { 'message' : "Invalid movie"}, 400
        
        movie.pop(movie_id)
        return {'message': f'Post: {movie_id} deleted'}

