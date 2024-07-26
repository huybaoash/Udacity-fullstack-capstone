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

        self.dummy_movie1 = {
            'title': 'Dummy Title 1',
            'duration': 123
        }
        self.dummy_movie2 = {
            'title': 'Dummy Title 2',
            'duration': 231
        }
        self.dummy_actor = {
            'name': 'Dummy Name',
            'role': 'antagonist',
            'movie_id': 2
        }
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.drop_all()
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Get movies successfully')
        self.assertTrue(data['movies'])

    def test_add_movie(self):
        response = self.client().post('/movies/add', json=self.dummy_movie1)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Add movie successfully')
        self.assertTrue(data['movie'])

    def test_add_movie_fail(self):
        response = self.client().post('/movies/add', json={
            'title': 'Dummy'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['status'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_update_movie(self):
        response = self.client().patch('/movies/1/update', json={
            'title': 'Test update name'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Update movie successfully')
        self.assertTrue(data['movie'])

    def test_update_movie_fail(self):
        response = self.client().patch('/movies/1000/update', json={
            'title': 'Test update name'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Not found')

    def test_delete_movie(self):
        response = self.client().delete('/movies/1/delete')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Delete movie successfully')
        self.assertTrue(data['movie_id'])

    def test_delete_movie_fail(self):
        response = self.client().delete('/movies/1000/delete')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Not found')

    def test_get_actor(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Get actors successfully')
        self.assertTrue(data['actors'])

    def test_add_actor(self):
        response = self.client().post('/movies/add', json=self.dummy_actor)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Add actor successfully')
        self.assertTrue(data['actor'])

    def test_add_actor_fail(self):
        response = self.client().post('/actors/add', json={
            'name': 'Dummy'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(data['status'], False)
        self.assertEqual(data['error'], 422)
        self.assertEqual(data['message'], 'Unprocessable')

    def test_update_actor(self):
        response = self.client().patch('/actors/1/update', json={
            'name': 'Test update name actor'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Update actor successfully')
        self.assertTrue(data['actor'])

    def test_update_actor_fail(self):
        response = self.client().patch('/actors/1000/update', json={
            'title': 'Test update name actor'
        })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Not found')

    def test_delete_actor(self):
        response = self.client().delete('/movies/1/delete')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], True)
        self.assertEqual(data['message'], 'Delete actor successfully')
        self.assertTrue(data['actor_id'])

    def test_delete_actor_fail(self):
        response = self.client().delete('/actors/1000/delete')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['status'], False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'], 'Not found')


if __name__ == '__main__':
    unittest.main()
