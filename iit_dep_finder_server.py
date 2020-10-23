from flask import Flask, request, send_from_directory
import sqlite3
import json

app = Flask(__name__, static_folder='static')

DB_LOC = "data.db"
KEY_INSTITUTE  = "institute"
KEY_DEPARTMENT = "department"
KEY_QUOTA      = "quota"
KEY_CATEGORY   = "category"
KEY_GENDER     = "gender"
KEY_OPR        = "OPR"
KEY_OPR_PREP   = "OPR_prep"
KEY_CPR        = "CPR"
KEY_CPR_PREP   = "CPR_prep"

PREP_TRUE  = 1
PREP_FALSE = 0

JEEA_RANK_KEY = "advRank"
JEEM_RANK_KEY = "mainRank"
CATEGORY_KEY  = "category"
GENDER_KEY    = "gender"
PREP_KEY      = "prepRL"

ADV_NOP_QUERY = """
SELECT * FROM orcr_2020 WHERE 
((OPR_prep=:prepRL AND CPR_prep=:prepRL) OR (CPR_prep=:prepRL)) AND 
((OPR>=:advRank AND CPR<=:advRank) OR ((CPR-:advRank)>=0 AND (CPR-:advRank)<300)) AND
institute LIKE "Indian Institute of Technology %" AND 
category=:category AND gender=:gender
ORDER BY CPR ASC
"""

@app.route("/")
@app.route("/index")
def root():
	return app.send_static_file("index.html")

@app.route("/<file>")
def serve_static(file):
	return app.send_static_file(file)

@app.route("/api/getdeps", methods=["POST"])
def get_deps():

	db_conn = sqlite3.connect(DB_LOC)
	db_cursor = db_conn.cursor()

	data = request.get_json()
	db_cursor.execute(ADV_NOP_QUERY, data)
	deps = db_cursor.fetchall()

	return json.dumps(deps)

