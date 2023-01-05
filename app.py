from flask import Flask,Response, json
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from src.ScraperFunction import joblist
import pandas as pd

app = Flask(__name__)
api = Api(app)
'''
engine = create_engine('sqlite:///joblist.db', echo = True)
sqlite_connection = engine.connect()
sqlite_table = 'JobsTable'
df = pd.DataFrame(joblist)
df.to_sql(sqlite_table, sqlite_connection, if_exists='fail')
sqlite_connection.close()'''



class index(Resource):
    def get(self):
        return json.dumps(joblist)
        
    
api.add_resource(index, '/api')



if __name__ == '__main__':
    app.run()