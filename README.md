# csv-to-osm-python
a python client for converting csv files to osm files

* csvtoosm.py

Usage: `python csvtoosm.py <csv_file> (<incoding_of_csv_file>)`

ex. `python csvtoosm.py test.csv`

`python csvtoosm.py test.csv euc-kr`

default incoding is 'utf-8'. The two columns of the csv file must have coordinates. (lat, lon)

* convertphonenumber.py

Usage: `python convertphonenumber.py <csv_file> <country_code> (<incoding_of_csv_file>)`

ex. `python csvtoosm.py test.csv 82`

`python csvtoosm.py test.csv 82 euc-kr`

default incoding is 'utf-8'. The two columns of the csv file must not have infomation unless coordinates.
If one or more of `phone`, `contact:phone`, `contact:mobile`, `contact:fax`, `contact:tty` exist, this application convert it smartly. (e.g. 02-123-4567 → +82 2 123 4567)

* convertaddress.py

Usage: `python convertaddress.py <csv_file> (<incoding_of_csv_file>)`

default incoding is 'utf-8'. The two columns of the csv file must have coordinates. (lat, lon)
If one or more of `address`, `addr:full` exist, this application convert it smartly. (e.g. 서울특별시 광진구 동일로 114 (화양동) → addr:street = 동일로, addr:housenumber = 114, addr:subdistrict = 화양동) If a entered address is successfully converted, this app removes the full address. If can't, this app leaves the full address.
