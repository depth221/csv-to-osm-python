import csv
import sys

csv_file_path = sys.argv[1]

if not len(sys.argv) in [3, 4]: # if without a path of csv file to read
    print("Usage: python convertphonenumber.py <csv_file> <country_code> (<incoding_of_csv_file>)\n")
    sys.exit()

csv_incoding = "utf-8" # set the incoding of csv file to read
if len(sys.argv) == 4:
    csv_incoding = sys.argv[3]
print("Info: Incoding of the csv file is " + csv_incoding)

country_code = sys.argv[2] # set the country code

fr = open(csv_file_path, 'r', encoding=csv_incoding)

fr_csv_r = csv.reader(fr);
fr_csv = []
for line in fr_csv_r: # convert the csv object to a list
    fr_csv.append(line)

keys_to_add = fr_csv[0]

for j in range(2, len(keys_to_add)):
    if keys_to_add[j] in ['phone', 'contact:phone', 'contact:mobile', 'contact:fax', 'contact:tty']:
        # if phone numbers exist
        print("Info: Found the tag '" + keys_to_add[j] + "'")
        
        for i in range(1, len(fr_csv)):
            if fr_csv[i][j]: # if the phone number exists
                phone = "+" + country_code
                phone_splitted = fr_csv[i][j].split('-')
    
                if phone_splitted[0][0] == "0": # delete the first '0'
                    phone_splitted[0] = phone_splitted[0][1:]
                
                for phone_factor in phone_splitted: # delete '-' and insert a space
                    phone += " " + phone_factor
                    
                
            fr_csv[i][j] = phone

print("Info: Done converting")
fr.close()
fw = open(csv_file_path[:-4] + "_phone.csv", 'w', encoding=csv_incoding, newline='') # write

writer = csv.writer(fw)
for i in fr_csv:
    writer.writerow(i)

print("Info: Writed to " + csv_file_path[:-4] + "_phone.csv")
fw.close()
