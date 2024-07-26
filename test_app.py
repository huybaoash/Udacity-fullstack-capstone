import json
import unittest
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        self.dummy_scene1 = {
            'title': 'Dummy Title 1',
            'duration': 123
        }
        self.dummy_scene2 = {
            'title': 'Dummy Title 2',
            'duration': 231
        }
        self.dummy_character = {
            'name': 'Dummy Name',
            'role': 'antagonist',
            'scene_id': 2
        }
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.drop_all()
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_scenes(self):
        response = self.client().get('/scenes')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Get scenes successfully')
        self.assertTrue(data['scenes'])

    def test_add_scene(self):
        response = self.client().post('/scenes/add', json=self.dummy_scene1)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Add scene successfully')
        self.assertTrue(data['scene'])

    def test_add_scene_fail(self):
        response = self.client().post('/scenes/add', json={
            'title': 'Dummy'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['status'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_update_scene(self):
        response = self.client().patch('/scenes/1/update', json={
            'title': 'Test update name'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Update scene successfully')
        self.assertTrue(data['scene'])

    def test_update_scene_fail(self):
        response = self.client().patch('/scenes/1000/update', json={
            'title': 'Test update name'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Not found')

    def test_delete_scene(self):
        response = self.client().delete('/scenes/1/delete')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Delete scene successfully')
        self.assertTrue(data['scene_id'])

    def test_delete_scene_fail(self):
        response = self.client().delete('/scenes/1000/delete')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Not found')

    def test_get_character(self):
        response = self.client().get('/characters')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Get characters successfully')
        self.assertTrue(data['characters'])

    def test_add_character(self):
        response = self.client().post('/scenes/add', json=self.dummy_character)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Add character successfully')
        self.assertTrue(data['character'])

    def test_add_character_fail(self):
        response = self.client().post('/characters/add', json={
            'name': 'Dummy'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['status'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_update_character(self):
        response = self.client().patch('/characters/1/update', json={
            'name': 'Test update name character'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Update character successfully')
        self.assertTrue(data['character'])

    def test_update_character_fail(self):
        response = self.client().patch('/characters/1000/update', json={
            'title': 'Test update name character'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Not found')

    def test_delete_character(self):
        response = self.client().delete('/scenes/1/delete')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Delete character successfully')
        self.assertTrue(data['character_id'])

    def test_delete_character_fail(self):
        response = self.client().delete('/characters/1000/delete')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Not found')


if __name__ == '__main__':
    unittest.main()
