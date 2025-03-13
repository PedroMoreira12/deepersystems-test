from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb://localhost:27017/")
db = client["myDatabase"]
users_collection = db["users"]

@app.route("/users", methods=["GET"])
def get_users():
    users = list(users_collection.find())
    for user in users:
        user["_id"] = str(user["_id"])
    return jsonify(users)

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    result = users_collection.insert_one(data)
    data["_id"] = str(result.inserted_id)
    return jsonify(data), 201

@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    result = users_collection.update_one({"_id": ObjectId(user_id)}, {"$set": data})
    if result.matched_count:
        return jsonify({"message": "User updated"})
    return jsonify({"error": "User not found"}), 404

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count:
        return jsonify({"message": "User deleted"})
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
