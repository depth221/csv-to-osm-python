import csv
import sys
import re
import time

start = time.time()

csv_file_path = sys.argv[1]

if not len(sys.argv) in [2, 3]: # if without a path of csv file to read
    print("Usage: python addnameen.py <csv_file> (<incoding_of_csv_file>)\n")
    sys.exit()

csv_incoding = "utf-8" # set the incoding of csv file to read
if len(sys.argv) == 3:
    csv_incoding = sys.argv[2]
print("Info: Incoding of the csv file is " + csv_incoding)

fr = open(csv_file_path, 'r', encoding=csv_incoding)

fr_csv_r = csv.reader(fr);
fr_csv = []
for line in fr_csv_r: # convert the csv object to a list
    fr_csv.append(line)

keys_to_add = fr_csv[0]

fr_csv[0].append('name:en')
fr_csv[0].append('name:ko')

for j in range(2, len(keys_to_add)):
    if keys_to_add[j] in ['name']:
        # if names exist
        print("Info: Found the tag '" + keys_to_add[j] + "'")
        
        for i in range(1, len(fr_csv)):
            if fr_csv[i][j]: # if the name exists
                fr_csv[i].extend([None] * 2)

                if (fr_csv[i][j])[-1] == ")":
                    pos_of_left = [a.start() for a in re.finditer('\(', fr_csv[i][j])][-1]
                    fr_csv[i][-2] = (fr_csv[i][j])[pos_of_left + 1:-1] # name:en
                    fr_csv[i][-1] = (fr_csv[i][j])[:pos_of_left] # name:ko

print("Info: Done converting")
fr.close()
try:
    fw = open(csv_file_path[:-4] + "_nameen.csv", 'w', encoding=csv_incoding, newline='') # write
except:
    print("Error: Please delete '" + csv_file_path[:-4] + "_nameen.csv' (%.3fs)" %(time.time() - start))
    sys.exit()

writer = csv.writer(fw)
for i in fr_csv:
    writer.writerow(i)

print("Info: Writed to '" + csv_file_path[:-4] + "_nameen.csv' (%.3fs)" %(time.time() - start))
fw.close()
