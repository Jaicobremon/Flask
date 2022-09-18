from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "contact": "6472721225",
        "Name": "Mom",
        "done": False, 
        "id":1
    },
    {
        "contact": "4168170849",
        "Name": "Dad",
        "done":False,
        "id":2
    },
]

@app.route("/")

def app_initiliazed():
    return "App Initiliazed"

@app.route("/add-data",methods = ["POST"])

def addContact():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please provide data"
        },400)
    
    contact = {
        "id":contacts[-1]["id"]+1,
        "contact":request.json.get("contact",""),
        "Name":request.json["Name"],
        "done": False
    }

    contacts.append(contact)

    return jsonify({
        "status":"Success",
        "Message":"Contact added succsfully"
    })

@app.route("/get-data")

def get_task():
    return jsonify({
        "data":contacts
    })

if (__name__ == "__main__"):
    app.run(debug = True)