import unittest
import json
from app import app


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test GET /users
    def test_get_users(self):
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    # Test POST /users
    def test_create_user(self):
        user = {'id': 1, 'username': 'testuser', 'email': 'testuser@example.com'}
        response = self.app.post('/users', data=json.dumps(user), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')
        self.assertIn('testuser', str(response.data))

    # Test GET /users/<id>
    def test_get_user(self):
        user = {'id': 1, 'username': 'testuser', 'email': 'testuser@example.com'}
        self.app.post('/users', data=json.dumps(user), content_type='application/json')
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertIn('testuser', str(response.data))

    # Test PUT /users/<id>
    def test_update_user(self):
        user = {'id': 1, 'username': 'testuser', 'email': 'testuser@example.com'}
        self.app.post('/users', data=json.dumps(user), content_type='application/json')
        updated_user = {'username': 'updateduser', 'email': 'updateduser@example.com'}
        response = self.app.put('/users/1', data=json.dumps(updated_user), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertIn('updateduser', str(response.data))

    # Test DELETE /users/<id>
    def test_delete_user(self):
        user = {'id': 1, 'username': 'testuser', 'email': 'testuser@example.com'}
        self.app.post('/users', data=json.dumps(user), content_type='application/json')
        response = self.app.delete('/users/1')
        self.assertEqual(response.status_code, 204)

    # Test GET /posts
    def test_get_posts(self):
        response = self.app.get('/posts')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    # Test POST /posts
    def test_create_post(self):
        post = {'id': 1, 'title': 'Test Post', 'content': 'This is a test post.'}
        response = self.app.post('/posts', data=json.dumps(post), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')
        self.assertIn('Test Post', str(response.data))

    # Test GET /posts/<id>
    def test_get_post(self):
        post = {'id': 1, 'title': 'Test Post', 'content': 'This is a test post.'}
        self.app.post('/posts', data=json.dumps(post), content_type='application/json')
        response = self.app.get('/posts/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertIn('Test Post', str(response.data))

    # Test PUT /posts/<id>
    def test_update_post(self):
        post = {'id': 1, 'title': 'Test Post', 'content': 'This is a test post.'}
        self.app.post('/posts', data=json.dumps(post), content_type='application/json')
        updated_post = {'title': 'Updated Post', 'content': 'This is an updated post.'}
        response = self.app.put('/posts/1', data=json.dumps(updated_post), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertIn('Updated Post', str(response.data))

    # Test DELETE /posts/<id>
    def test_delete_post(self):
        post = {'id': 1, 'title': 'Test Post', 'content': 'This is a test post.'}
        self.app.post('/posts', data=json.dumps(post), content_type='application/json')
        response = self.app.delete('/posts/1')
        self.assertEqual(response.status_code, 204)


if __name__ == '__main__':
    unittest.main()
