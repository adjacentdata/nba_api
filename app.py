from flask import Flask
from dotenv import load_dotenv
import psycopg2
import os 
import queries

load_dotenv()

app = Flask(__name__)

connection_link = psycopg2.connect(os.getenv("DB_LINK"))
cursor = connection_link.cursor()
fetch_one = cursor.fetchone()
fetch_all = cursor.fetchall()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"