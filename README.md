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
If one or more of `phone`, `contact:phone`, `contact:mobile`, `contact:fax`, `contact:tty` exist, this application convert it smartly.
