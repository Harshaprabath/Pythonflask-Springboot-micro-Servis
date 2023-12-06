from flask_pymongo import PyMongo

def conn(app: object):
  app.config['MONGO_URI'] = "mongodb+srv://cw_user:d8Y5veXHCUFR6O4Y@cw.3zua9iz.mongodb.net/cw_db?retryWrites=true&w=majority"
  mongo = PyMongo(app)
  return mongo     
