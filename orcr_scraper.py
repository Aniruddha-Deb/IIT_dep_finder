from bs4 import BeautifulSoup
import csv
import sqlite3
from os import path
import conf

def html_to_csv():
	if path.exists(path.join(conf.csv_loc, conf.record_name + ".txt")):
		print("File already exists. This may be the data file, so not reprocessing")
		print("Please type any key to continue or Ctrl-C to stop execution")
	else:
		outfile = open(path.join(conf.csv_loc, conf.record_name + ".txt"), "w");
		infile = open(path.join(conf.html_loc, conf.record_name + ".html"), "r");
		soup = BeautifulSoup(infile, "lxml");
		
		main_table = soup.find("table", {"class":"border_table_at"})
		table_rows = main_table.find_all("tr")
		
		for row in table_rows:
			cells = row.find_all("td")
			for cell in cells:
				field = cell.text.strip()
				if field == "Female-only (including Supernumerary)":
					field = field.replace(" (including Supernumerary)", "")
				outfile.write(field.replace(",", "").replace("  ", " ") + ",")
			outfile.write("\n")
		
		outfile.close()
		infile.close()
		print("HTML converted to CSV")
		print("Please check for errors and type any key to continue")
	input()

def csv_to_sqlite():
	reader = csv.reader(open(path.join(conf.csv_loc, conf.record_name + ".txt"), "r"))
	conn = sqlite3.connect(conf.db_loc)

	c = conn.cursor()
	query = conf.queries["create_table_query"]

	# Create table
	c.execute(query)
	conn.commit()
	query = conf.queries["insert_record_query"]

	for row in reader:
		if row[5].endswith("P"):
			row[5] = row[5].replace("P","")
			row.insert(6,"1")
			print("OPR preparatory for " + str(row))
		else:
			row.insert(6,"0")

		if row[7].endswith("P"):
			row[7] = row[7].replace("P","")
			row.insert(8,"1")
			print("CPR preparatory for " + str(row))
		else:
			row.insert(8,"0")
		c.execute(query, row)

	conn.commit()
	conn.close()
	print("Successfully inserted all rows into db")

def main():
	html_to_csv()
	csv_to_sqlite()

if __name__ == "__main__":
	main()
