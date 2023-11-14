from flask import Flask,request,jsonify

app = Flask(__name__)
#get request
@app.route("/get-user/<user_id>")
def  get_user(user_id):
    user_data = {
        "user_id":user_id,
        "name":"john doe",
        "email":"john.doe@example.com"
    }

    #query perameter - extra value included after the main path
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

#post request
@app.route("/create-user", methods= ["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data),201
"""
HTTP methods
GET: Retrieve a resource
POST: Create a new resource / Upload data to the server
PUT: Update an existing resource
DELETE: Delete a resource

"""

if __name__ == "__main__":
    app.run(debug=True)