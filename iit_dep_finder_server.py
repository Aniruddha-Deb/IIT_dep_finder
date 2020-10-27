from flask import Flask, request, send_from_directory
import sqlite3
import json

app = Flask(__name__)

DB_LOC = "data/data.db"
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

ADV_QUERY = """
SELECT * FROM orcr_2020_r2 WHERE 
((OPR_prep=:prepRL AND CPR_prep=:prepRL) OR (CPR_prep=:prepRL)) AND 
((OPR<=:advRank AND CPR>=:advRank) OR ((CPR-:advRank)>=0 AND (CPR-:advRank)<300)) AND
institute LIKE "Indian Institute of Technology %" AND 
category=:category AND gender=:gender
ORDER BY CPR ASC
"""

INSTI_INSPECT_QUERY = """
SELECT * FROM orcr_2020_r2 WHERE
((OPR_prep=:prepRL AND CPR_prep=:prepRL) OR (CPR_prep=:prepRL)) AND 
institute=:institute AND CPR>=:advRank AND
category=:category AND gender=:gender
ORDER BY CPR ASC
"""

def exec_select_query(query, data):
	db_conn = sqlite3.connect(DB_LOC)
	db_cursor = db_conn.cursor()

	db_cursor.execute(query, data)
	deps = db_cursor.fetchall()
	db_conn.close()
	return deps;

@app.route("/api/getdeps", methods=["POST"])
def get_deps():
	data = request.get_json()
	return json.dumps(exec_select_query(ADV_QUERY, data))

@app.route("/api/institute", methods=["POST"])
def institute_inspect():
	data = request.get_json()
	return json.dumps(exec_select_query(INSTI_INSPECT_QUERY, data))
