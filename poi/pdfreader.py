import tabula

tables = tabula.read_pdf("JEE-2019-Report.pdf", pages="40-55")

outfile = open("centres.txt", "w")
for table in tables:
	outfile.write(table.to_string())
	outfile.write("\n")
	print("Printed table")
