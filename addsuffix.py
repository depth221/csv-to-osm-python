import csv
import sys
import time

start = time.time()

csv_file_path = sys.argv[1]

if not len(sys.argv) in [4, 5]: # if without a path of csv file to read
    print("Usage: python addsuffix.py <csv_file> <column> <suffix> (<incoding_of_csv_file>)\n")
    sys.exit()

csv_incoding = "utf-8" # set the incoding of csv file to read
if len(sys.argv) == 5:
    csv_incoding = sys.argv[4]
print("Info: Incoding of the csv file is " + csv_incoding)

fr = open(csv_file_path, 'r', encoding=csv_incoding)

fr_csv_r = csv.reader(fr);
fr_csv = []
for line in fr_csv_r: # convert the csv object to a list
    fr_csv.append(line)

keys_to_add = fr_csv[0]

for j in range(2, len(keys_to_add)):
    if keys_to_add[j] in [sys.argv[2]]:
        # if the column exists
        print("Info: Found the tag '" + keys_to_add[j] + "'")
        
        for i in range(1, len(fr_csv)):  
            if fr_csv[i][j]: # if the value exists

                fr_csv[i][j] += " " + sys.argv[3]

print("Info: Done converting")
fr.close()
try:
    fw = open(csv_file_path[:-4] + "_add%s.csv" %sys.argv[3], 'w', encoding=csv_incoding, newline='') # write
except:
    print("Error: Please delete '" + csv_file_path[:-4] + "_add%s.csv (%.3fs)" %(sys.argv[3], (time.time() - start)))
    sys.exit()

writer = csv.writer(fw)
for i in fr_csv:
    writer.writerow(i)

print("Info: Writed to '" + csv_file_path[:-4] + "_add%s.csv (%.3fs)" %(sys.argv[3], (time.time() - start)))
fw.close()
