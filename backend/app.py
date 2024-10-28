from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage for demonstration purposes
users = []
posts = []


# User Endpoints
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


@app.route('/users', methods=['POST'])
def create_user():
    user = request.get_json()
    users.append(user)
    return jsonify(user), 201


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = next((u for u in users if u['id'] == id), None)
    if user:
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = next((u for u in users if u['id'] == id), None)
    if user:
        data = request.get_json()
        user.update(data)
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404


@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    global users
    users = [u for u in users if u['id'] != id]
    return '', 204


# Post Endpoints
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts), 200


@app.route('/posts', methods=['POST'])
def create_post():
    post = request.get_json()
    posts.append(post)
    return jsonify(post), 201


@app.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = next((p for p in posts if p['id'] == id), None)
    if post:
        return jsonify(post), 200
    return jsonify({'error': 'Post not found'}), 404


@app.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = next((p for p in posts if p['id'] == id), None)
    if post:
        data = request.get_json()
        post.update(data)
        return jsonify(post), 200
    return jsonify({'error': 'Post not found'}), 404


@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    global posts
    posts = [p for p in posts if p['id'] != id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
