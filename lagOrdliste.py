ordliste = open("NSF-ordlisten.txt")
output = open("ordliste.txt", "a")

for line in ordliste:
	output.write(line.split()[0].lower() + "\n")

ordliste.close()
output.close()
