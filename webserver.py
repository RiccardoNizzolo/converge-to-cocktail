import tornado.ioloop
from WebRequestHandler import WebRequestHandler
import logging
import sqlite3

try:
    conn = sqlite3.connect('cocktails.db')
    web_application = tornado.web.Application([
        (r"/", WebRequestHandler, dict(conn=conn))
    ])
    web_application.listen(8000)
    tornado.ioloop.IOLoop.current().start()
except:
    logging.exception("Error while handling web requests.")