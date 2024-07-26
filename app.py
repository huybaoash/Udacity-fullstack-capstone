import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Movie, Actor
from auth import AuthError, requires_auth

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app, resources={r'/api/*': {'origins': '*'}})
    setup_db(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PUT,PATCH,DELETE,OPTIONS')
        return response

    @app.route('/')
    def get_official():
        return "Final Project. One more time..!"

    @app.route('/movies', methods=['GET'])
    @requires_auth('view:movies')
    def get_all_movies(jwt):
        movies = Movie.query.all()
        movies_response = [movie.format() for movie in movies]
        return jsonify({
            'status': True,
            'message': 'Get movies successfully',
            'movies': movies_response
        })

    @app.route('/movies/add', methods=['POST'])
    @requires_auth('add:movies')
    def add_movie(jwt):
        body = request.get_json()
        title = body.get('title')
        duration = body.get('duration')

        if not title or not duration:
            abort(422)
        try:
            movie = Movie(title=title, duration=duration)
            movie.insert()
            return jsonify({
                'status': True,
                'message': 'Add movie successfully',
                'movie': movie.format()
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/movies/<int:movie_id>/update', methods=['PATCH'])
    @requires_auth('update:movies')
    def update_movie(jwt, movie_id):
        movie = Movie.query.get(movie_id)
        if not movie:
            abort(404)

        body = request.get_json()
        title = body.get('title')
        duration = body.get('duration')

        if not title or not duration:
            abort(422)

        try:
            movie.title = title
            movie.duration = duration
            movie.update()
            return jsonify({
                'status': True,
                'message': 'Update movie successfully',
                'movie': movie.format()
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/movies/<int:movie_id>/delete', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):
        movie = Movie.query.get(movie_id)
        if not movie:
            abort(404)
        try:
            movie.delete()
            return jsonify({
                'status': True,
                'message': 'Delete movie successfully',
                'movie_id': movie_id
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/actors', methods=['GET'])
    @requires_auth('view:actors')
    def get_actors(jwt):
        actors = Actor.query.all()
        actors_response = [actor.format() for actor in actors]
        return jsonify({
            'status': True,
            'message': 'Get actors successfully',
            'actors': actors_response
        })

    @app.route('/actors/add', methods=['POST'])
    @requires_auth('add:actors')
    def add_actor(jwt):
        body = request.get_json()
        name = body.get('name')
        role = body.get('role')
        movie_id = body.get('movie_id')

        if not name or not role or not movie_id:
            abort(422)
        try:
            actor = Actor(name=name, role=role, movie_id=movie_id)
            actor.insert()
            return jsonify({
                'status': True,
                'message': 'Add actor successfully',
                'actor': actor.format()
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/actors/<int:actor_id>/update', methods=['PATCH'])
    @requires_auth('update:actors')
    def update_actor(jwt, actor_id):
        actor = Actor.query.get(actor_id)
        if not actor:
            abort(404)

        body = request.get_json()
        name = body.get('name')
        role = body.get('role')
        movie_id = body.get('movie_id')

        if not name or not role or not movie_id:
            abort(422)

        try:
            actor.name = name
            actor.role = role
            actor.movie_id = movie_id
            actor.update()
            return jsonify({
                'status': True,
                'message': 'Update actor successfully',
                'actor': actor.format()
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/actors/<int:actor_id>/delete', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(jwt, actor_id):
        actor = Actor.query.get(actor_id)
        if not actor:
            abort(404)
        try:
            actor.delete()
            return jsonify({
                'status': True,
                'message': 'Delete actor successfully',
                'actor_id': actor_id
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'status': False,
            'error': 422,
            'message': 'Unprocessable'
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'status': False,
            'error': 404,
            'message': 'Not found'
        }), 404

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
            'status': False,
            'error': error.status_code,
            'message': error.error
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run()