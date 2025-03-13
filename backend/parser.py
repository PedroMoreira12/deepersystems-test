import json
from dataclasses import dataclass, asdict
from datetime import datetime
from pymongo import MongoClient

@dataclass
class UserPreferences:
    timezone: str

@dataclass
class User:
    username: str
    password: str
    roles: list
    preferences: UserPreferences
    active: bool
    created_ts: float

def parse_user_data(json_file):
    with open(json_file) as f:
        data = json.load(f)
    
    users = []
    for item in data["users"]:
        username = item["user"]
        password = item["password"]
        roles = []
        if item.get("is_user_admin"):
            roles.append("admin")
        if item.get("is_user_manager"):
            roles.append("manager")
        if item.get("is_user_tester"):
            roles.append("tester")
        
        preferences = UserPreferences(timezone=item["user_timezone"])
        active = item.get("is_user_active", True)
        
        # Convert ISO date to timestamp
        dt = datetime.fromisoformat(item["created_at"].replace("Z", "+00:00"))
        created_ts = dt.timestamp()

        user = User(
            username=username,
            password=password,
            roles=roles,
            preferences=preferences,
            active=active,
            created_ts=created_ts
        )
        users.append(user)
    return users

def import_users_to_mongodb(users, db_name="myDatabase", collection_name="users"):
    client = MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]
    # Clear existing data if needed
    collection.delete_many({})
    for user in users:
        collection.insert_one(asdict(user))
    print("Data imported successfully!")

if __name__ == "__main__":
    users = parse_user_data("udata.json")
    import_users_to_mongodb(users)
