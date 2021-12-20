import csv
import sys
import time

start = time.time()

csv_file_path = "한전KDN_광주시 버스 정류장 정보_20200410.csv"


csv_incoding = "utf-8" # set the incoding of csv file to read
if len(sys.argv) == 4:
    csv_incoding = sys.argv[3]
print("Info: Incoding of the csv file is " + csv_incoding)

country_code = "82" # set the country code

fr = open(csv_file_path, 'r', encoding=csv_incoding)

fr_csv_r = csv.reader(fr);
fr_csv = []
for line in fr_csv_r: # convert the csv object to a list
    fr_csv.append(line)

keys_to_add = fr_csv[0]

for j in range(2, len(keys_to_add)):
    if keys_to_add[j] in ['phone', 'fax', 'contact:phone', 'contact:mobile', 'contact:fax', 'contact:tty']:
        # if phone numbers exist
        print("Info: Found the tag '" + keys_to_add[j] + "'")
        
        for i in range(1, len(fr_csv)):
            if fr_csv[i][j] in ["-"]:
                fr_csv[i][j] = None
                continue
            
            if fr_csv[i][j]: # if the phone number exists
                phone = "+" + country_code
                phone_splitted = fr_csv[i][j].strip().split('-')
    
                if phone_splitted[0][0] == "0": # delete the first '0'
                    phone_splitted[0] = phone_splitted[0][1:]
                
                for phone_factor in phone_splitted: # delete '-' and insert a space
                    phone += " " + phone_factor
                    
                fr_csv[i][j] = phone

print("Info: Done converting")
fr.close()
try:
    fw = open(csv_file_path[:-4] + "_phone.csv", 'w', encoding=csv_incoding, newline='') # write
except:
    print("Error: Please delete '" + csv_file_path[:-4] + "_phone.csv' (%.3fs)" %(time.time() - start))
    sys.exit()

writer = csv.writer(fw)
for i in fr_csv:
    writer.writerow(i)

print("Info: Writed to '" + csv_file_path[:-4] + "_phone.csv' (%.3fs)" %(time.time() - start))
fw.close()
