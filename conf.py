round = "r4"
year = "2020"

db_loc = "data/data.db"
csv_loc = "data/csv"
html_loc = "data/html"
fprefix = "orcr"

record_name = "_".join([fprefix, year, round])

# SQLite does not allow parameterization of table names, hence the hacky 
# workaround in the query strings.
queries = {
	"insert_record_query": "INSERT INTO " + record_name + " VALUES (?,?,?,?,?,?,?,?,?)"
	,
	"create_table_query": """
		CREATE TABLE IF NOT EXISTS """ + record_name + """ (
			institute varchar(256),
			department varchar(256),
			quota varchar(4),
			category varchar(32),
			gender varchar(32),
			OPR integer,
			OPR_prep integer,
			CPR integer,
			CPR_prep integer
		);
	"""
	,
	"rank_query": """
		SELECT * FROM """ + record_name + """ WHERE 
		((OPR_prep=:prepRL AND CPR_prep=:prepRL) OR (CPR_prep=:prepRL)) AND 
		((OPR<=:advRank AND CPR>=:advRank) OR ((CPR-:advRank)>=0 AND (CPR-:advRank)<300)) AND
		institute LIKE "Indian Institute of Technology %" AND 
		category=:category AND gender=:gender
		ORDER BY CPR ASC
	"""
	,
	"institute_query": """
		SELECT * FROM """ + record_name + """ WHERE
		((OPR_prep=:prepRL AND CPR_prep=:prepRL) OR (CPR_prep=:prepRL)) AND 
		institute=:institute AND CPR>=:advRank AND
		category=:category AND gender=:gender
		ORDER BY CPR ASC
	"""
}

keys = {
	"institute": "institute",
	"department": "department",
	"quota": "quota",
	"category": "category",
	"gender": "gender",
	"opening_rank": "OPR",
	"opening_rank_prep": "OPR_prep",
	"closing_rank": "CPR",
	"closing_rank_prep": "CPR_prep"
}

api_paths = {
	"rank_query": "/IIT_dep_finder/api/getdeps",
	"institute_query": "/IIT_dep_finder/api/institute"
}
