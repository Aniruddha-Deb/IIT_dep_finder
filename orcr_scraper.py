from bs4 import BeautifulSoup
import csv
import sqlite3

KEY_INSTITUTE  = "institute"
KEY_DEPARTMENT = "department"
KEY_QUOTA      = "quota"
KEY_CATEGORY   = "category"
KEY_GENDER     = "gender"
KEY_OPR        = "OPR"
KEY_CPR        = "CPR"

def html_to_csv():
	outfile = open("data/csv/orcr_2020_r3.txt", "w");
	infile = open("data/html/orcr_2020_r3.html", "r");
	soup = BeautifulSoup(infile, "lxml");
	
	main_table = soup.find("table", {"class":"border_table_at"})
	table_rows = main_table.find_all("tr")
	
	for row in table_rows:
		cells = row.find_all("td")
		for cell in cells:
			field = cell.text.strip()
			if field == "Female-only (including Supernumerary)":
				field = field.replace(" (including Supernumerary)", "")
			outfile.write(field.replace(",", "") + ",") 
		outfile.write("\n")
	
	outfile.close()
	infile.close()

def csv_to_sqlite():
	reader = csv.reader(open("data/csv/orcr_2020_r3.txt", "r"))
	conn = sqlite3.connect("data/data.db")

	c = conn.cursor()
	query = "INSERT INTO orcr_2020_r3 VALUES (?,?,?,?,?,?,?,?,?)"

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
	csv_to_sqlite()

if __name__ == "__main__":
	main()
