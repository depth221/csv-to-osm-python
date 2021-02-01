import csv
import sys
import re

csv_file_path = sys.argv[1]

if not len(sys.argv) in [3, 4]: # if without a path of csv file to read
    print("Usage: python convertaddress.py <csv_file> (<incoding_of_csv_file>)\n")
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

fr_csv[0].append('addr:district')
fr_csv[0].append('addr:street')
fr_csv[0].append('addr:housenumber')
fr_csv[0].append('addr:subdistrict')
fr_csv[0].append('level')

for j in range(2, len(keys_to_add)):
    if keys_to_add[j] in ['address', 'addr:full']:
        # if addresses exist
        print("Info: Found the tag '" + keys_to_add[j] + "'")
        
        for i in range(1, len(fr_csv)):
            province = ""
            is_exception = False # cannot be automatically converted
            
            if fr_csv[i][j]: # if the address exists
                address_splitted = fr_csv[i][j].replace("(", " (").split()
                fr_csv[i].extend([None, None, None, None, None])
                for factor in address_splitted:
                    
                    if factor[-1] == "도": # addr:province
                        province = "do"
                    
                    elif len(factor) >= 3 and factor[-3:] in ["특별시", "광역시", "자치시"]: # addr:province
                        if factor[-3:] == "특별시":
                            province = "teuk"
                        elif factor[-3:] == "광역시":
                            province = "gwang"
                        elif factor[-3:] == "자치시":
                            province = "jachi"

                    elif factor[-1] in ["시", "군", "구"]:
                        if province in ["teuk", "gwang", "jachi"]:
                           fr_csv[i][-5] == factor # addr:district
                        # else:
                            # addr:city
                    
                    elif factor[-1] in ["읍", "면", "동", "가"]:
                        fr_csv[i][-2] = factor # addr:subdistrict
                    elif len(factor) >= 4 and\
                             len(re.findall("\d", factor)) <= 1 and\
                             factor[0] == "(" and factor[-1] == ")" and\
                             factor[-2] in ["동", "가"]: 
                        # 1. avoid out of range error
                        # 2. only has one digit
                        fr_csv[i][-2] = factor[1:-1] # (OOn-dong)

                    elif factor[-1] in ["로", "길"]: # addr:street
                        fr_csv[i][-4] = factor
                        
                    elif factor.replace('-', '').replace(',', '').isdecimal(): # addr:housenumber
                        if factor[-1] == ",":
                            fr_csv[i][-3] = factor[:-1]
                        else:
                            fr_csv[i][-3] = factor

                    elif factor[-1] == "층": # level
                        if factor[0:2] == "지하":
                            fr_csv[i][-1] = "-" + factor[2:-1] # basement
                        elif factor[:-1].isdecimal():
                            fr_csv[i][-1] = factor[:-1]
                        else:
                            is_exception = True

                    else:
                        is_exception = True

                if not is_exception:
                    fr_csv[i][j] = ""

print("Info: Done converting")
fr.close()
try:
    fw = open(csv_file_path[:-4] + "_address.csv", 'w', encoding=csv_incoding, newline='') # write
except:
    print("Error: Please delete '" + csv_file_path[:-4] + "_address.csv'")
    sys.exit()

writer = csv.writer(fw)
for i in fr_csv:
    writer.writerow(i)

print("Info: Writed to '" + csv_file_path[:-4] + "_address.csv'")
fw.close()
