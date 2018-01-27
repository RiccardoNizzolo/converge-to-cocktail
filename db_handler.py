import sqlite3
import codecs

conn = sqlite3.connect('cocktails.db')

conn.execute('''CREATE TABLE COCKTAILS
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           CHAR(256)    NOT NULL,
         DESCRIPTION    CHAR(256),
         GARNISH    CHAR(256), 
         INSTRUCTIONS   CHAR(256),
         URL    CHAR(256));''')

with codecs.open('cocktails_photos.csv', 'r', encoding='utf-8') as file:
    line = file.readline()
    while line:
        print(line)
        line = line.replace("'", '"')
        words = line.split(';-')
        print(words)
        conn.execute('INSERT INTO COCKTAILS (ID, NAME, DESCRIPTION, GARNISH, INSTRUCTIONS, URL) VALUES (\'{}\', \'{}\', \'{}\', \'{}\', \'{}\', \'{}\');'.format(words[0], words[1], words[2], words[3], words[4], words[5]))
        conn.commit()
        line = file.readline()