import tornado.web
import logging
import sqlite3
import json

class WebRequestHandler(tornado.web.RequestHandler):

    def initialize(self, conn):
        self.conn = conn

    def get(self):
        self.write("Web server is alive")

    def post(self):
        data = self.get_argument('name')

        result = self.get_cocktail_data(data)
        
        json_data = {
            'id': result[0],
            'name': result[1],
            'description': result[2],
            'garnish': result[3],
            'instructions': result[4],
            'url': result[5]
        }


        self.write(json.dumps(json_data))

    def get_cocktail_data(self, cocktail_name):
        cur = self.conn.cursor()
        cur.execute('SELECT * FROM COCKTAILS WHERE NAME = ?', (cocktail_name, ))
        results = cur.fetchall()
        for row in results:
            print(row)
            return row