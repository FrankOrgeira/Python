#!/usr/bin/env python3
import re
import sys
import operator
import csv

per_user = {}
error = {}

logfile = sys.argv[1]
with open(logfile) as f:
	for line in f:
		usuario = re.search(r"\((\w.*)\)$", line)
		if usuario[1] not in per_user:
			per_user[usuario[1]] = {"INFO": 0, "ERROR": 0}
		cant_info = per_user[usuario[1]].get("INFO")
		cant_error = per_user[usuario[1]].get("ERROR")
		if "INFO" in line:
			cant_info += 1
		if "ERROR" in line:
			cant_error += 1
			tipo_error = re.search(r"ERROR ([\w ']*)", line)
			if tipo_error[1] not in error:
				error[tipo_error[1]] = 0 
			error[tipo_error[1]] += 1
		per_user.update({usuario[1]: {"INFO": cant_info, "ERROR": cant_error}})
f.close()

error_order = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
user_order = sorted(per_user.items(), key=operator.itemgetter(0))

labels = ["Error","Count"]

try:
	with open("error_message.csv","w") as f:
		writer = csv.DictWriter(f, fieldnames=labels)
		writer.writeheader()
		for elem in enumerate(error_order):
			linea = {"Error": elem[1][0], "Count": error[elem[1][0]]}
			#print(linea)
			writer.writerow(linea)
except IOError:
	print("IO Error")
f.close()

labels = ["Username","INFO","ERROR"]

try:
	with open("user_statistics.csv","w") as f:
		writer = csv.DictWriter(f, fieldnames=labels)
		writer.writeheader()
		for elem in enumerate(user_order):
			linea = {"Username": elem[1][0], "INFO": elem[1][1].get("INFO"), "ERROR": elem[1][1].get("ERROR")} 
			#print(linea)
			writer.writerow(linea)
except IOError:
	print("IO Error")
f.close()
