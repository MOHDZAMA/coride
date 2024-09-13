from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB
app.config["MONGO_URI"] = "mongodb://mongodb:27017/user_db"
mongo = PyMongo(app)

# Collection reference
users_collection = mongo.db.users

# format user object
def user_to_dict(user):
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"]
    }


# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = users_collection.find()
    return jsonify([user_to_dict(user) for user in users]), 200


# Get a user by ID
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = users_collection.find_one({"_id": ObjectId(id)})
    if user:
        return jsonify(user_to_dict(user)), 200
    return jsonify({"error": "User not found"}), 404


# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not all(field in data for field in ("name", "email", "password")):
        return jsonify({"error": "Invalid input"}), 400
    new_user = {
        "name": data["name"],
        "email": data["email"],
        "password": data["password"]
    }
    result = users_collection.insert_one(new_user)
    return jsonify({"message": "User created", "id": str(result.inserted_id)}), 201


# Update an existing user
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    update_fields = {key: data[key] for key in data if key in ("name", "email", "password")}
    result = users_collection.update_one({"_id": ObjectId(id)}, {"$set": update_fields})
    if result.matched_count:
        return jsonify({"message": "User updated"}), 200
    return jsonify({"error": "User not found"}), 404


# Delete a user
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    result = users_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
