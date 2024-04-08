from src.database.database import connect
import bcrypt

def client_login(username, password):
    client, collection = connect("client")
    user = collection.find_one({"username": username})
    response = {
        "message": "Failed login",
        "status": False
    }

    if user:
        stored_password = user.get("password", b"")
        if bcrypt.checkpw(password.encode("utf-8"), stored_password):
            response = {
                "message": "Success login",
                "status": True
            }
    else:
        response = client_signup(username, password)
    client.close()
    return response
    
def client_signup (usr, password):
    usr = usr.strip().lower()
    client, collection = connect("client")
    response = {
        "message": "Failed client sign up",
        "status": False
    } 
        
    existing_user = collection.find_one({"username": usr})
    if existing_user is None:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        collection.insert_one({"username": usr, "password": hashed })
        response = {
            "message": "Sign up success",
            "status": True
        }
    client.close()
    return response