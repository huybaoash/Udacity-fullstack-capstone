import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Scene, Character
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

    @app.route('/scenes', methods=['GET'])
    @requires_auth('view:scenes')
    def get_all_scenes(jwt):
        scenes = Scene.query.all()
        scenes_response = [scene.format() for scene in scenes]
        return jsonify({
            'status': True,
            'message': 'Get scenes successfully',
            'scenes': scenes_response
        })

    @app.route('/scenes/add', methods=['POST'])
    @requires_auth('add:scenes')
    def add_scene(jwt):
        body = request.get_json()
        title = body.get('title')
        duration = body.get('duration')

        if not title or not duration:
            abort(422)
        try:
            scene = Scene(title=title, duration=duration)
            scene.insert()
            return jsonify({
                'status': True,
                'message': 'Add scene successfully',
                'scene': scene.format()
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/scenes/<int:scene_id>/update', methods=['PATCH'])
    @requires_auth('update:scenes')
    def update_scene(jwt, scene_id):
        scene = Scene.query.get(scene_id)
        if not scene:
            abort(404)

        body = request.get_json()
        title = body.get('title')
        duration = body.get('duration')

        if not title or not duration:
            abort(422)

        try:
            scene.title = title
            scene.duration = duration
            scene.update()
            return jsonify({
                'status': True,
                'message': 'Update scene successfully',
                'scene': scene.format()
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/scenes/<int:scene_id>/delete', methods=['DELETE'])
    @requires_auth('delete:scenes')
    def delete_scene(jwt, scene_id):
        scene = Scene.query.get(scene_id)
        if not scene:
            abort(404)
        try:
            scene.delete()
            return jsonify({
                'status': True,
                'message': 'Delete scene successfully',
                'scene_id': scene_id
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/characters', methods=['GET'])
    @requires_auth('view:characters')
    def get_characters(jwt):
        characters = Character.query.all()
        characters_response = [character.format() for character in characters]
        return jsonify({
            'status': True,
            'message': 'Get characters successfully',
            'characters': characters_response
        })

    @app.route('/characters/add', methods=['POST'])
    @requires_auth('add:characters')
    def add_character(jwt):
        body = request.get_json()
        name = body.get('name')
        role = body.get('role')
        scene_id = body.get('scene_id')

        if not name or not role or not scene_id:
            abort(422)
        try:
            character = Character(name=name, role=role, scene_id=scene_id)
            character.insert()
            return jsonify({
                'status': True,
                'message': 'Add character successfully',
                'character': character.format()
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/characters/<int:character_id>/update', methods=['PATCH'])
    @requires_auth('update:characters')
    def update_character(jwt, character_id):
        character = Character.query.get(character_id)
        if not character:
            abort(404)

        body = request.get_json()
        name = body.get('name')
        role = body.get('role')
        scene_id = body.get('scene_id')

        if not name or not role or not scene_id:
            abort(422)

        try:
            character.name = name
            character.role = role
            character.scene_id = scene_id
            character.update()
            return jsonify({
                'status': True,
                'message': 'Update character successfully',
                'character': character.format()
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/characters/<int:character_id>/delete', methods=['DELETE'])
    @requires_auth('delete:characters')
    def delete_character(jwt, character_id):
        character = Character.query.get(character_id)
        if not character:
            abort(404)
        try:
            character.delete()
            return jsonify({
                'status': True,
                'message': 'Delete character successfully',
                'character_id': character_id
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


APP = create_app()

if __name__ == '__main__':
    APP.run()


