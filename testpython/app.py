from flask import Flask , request , render_template , jsonify , redirect
from flask_cors import CORS, cross_origin
from bson.objectid import ObjectId

from flask_pymongo import PyMongo 
from bson import json_util
import json

app = Flask("myapp") 
app.config["MONGO_URI"] = "mongodb://localhost:27017/mydb"
mongo = PyMongo(app)


@app.route('/chart')
@cross_origin(origin="*")


def members():
  return {"members": ["Member1", "Member2", "Member3"]}

@app.route('/chartin/<idt>', methods=['GET'])
@cross_origin(origin="*")

def index(idt):
  print(idt)
  #cursr= list(mongo.db.weather.find({"timestamp": "1654701067021"}))

  #details = mongo.db.weather.find({"_id": ObjectId("62a09c00c44a36b5d64df463")})
  details = mongo.db.charts.find({"identifier.ident": idt})

  details_dicts = [doc for doc in details]
  details_json_string = json.dumps(details_dicts,default=json_util.default)
  
  return details_json_string





  #return json.dumps(cursr, default=cursr.default)
  #return json.dumps(cursr)
  #print(cursr)

  #for rkt in cursr:
    #print(rkt)


  
  #return "gghsd"

if __name__ == "__main__":
    app.run(debug=True)