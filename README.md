# dcurooms


### Description
This is a command line tool I hope to develop overtime. In time it will be able to support the booking of rooms on the DCU Glasnevin Campus. Along with this, it will be able to display room timetables information as well as be able to check the availability of a room in a few different ways.

Currently the dcurooms script can show you which rooms in the Henry Grattan building and the School of Computing are free and booked currently.


### Installation
Clone this repo by running ```git clone https://github.com/theycallmemac/dcurooms.git```.
cd into the clone and run ```python setup.py install``` as root to install.


### Dependencies
 - bs4
 - mechanize
 - requests


### Usage
Buildings are referenced using their assigned building letters. The School of Computing is given the letter "L" and the Henry Grattan is given the letter "C". Don't ask me why it's like that, it's a very odd naming convention.

To book L125 in the School of Computing on the 7/2/2018 from 16:00 to 17:00, run ```dcurooms -b L125 7/2/2018 1600 1700```.

To book CG04 in the Henry Grattan on the 5/2/2018 from 18:00 to 20:00, run ```dcurooms -b CG04 5/2/2018 1800 2000```.

To check the current availabilty of labs in the DCU School of Computing run ```dcurooms -nL``` or ```dcurooms --now --computing```.

To show the rooms which are currently available in the Henry Grattan building run ```dcurooms -anC``` or ```dcurooms --available --now --grattan```.

To display the information of a specific room in the Henry Grattan building at 16:00 on the Monday of the 4th week of the college year run ```dcurooms -l CG05 4 1 1600``` or ```dcurooms --lookup CG05 4 1 1600```.

To look up the info of all rooms in the School of Computing at 13:00 on the Thursday of the 10th week of the college year run ```dcurooms -lL 10 4 1300``` or ```dcurooms --lookup --computing 10 4 1300```

To lookup the info of all free rooms in the Henry Grattan building at 16:00 on the Monday of the 21st week of the college year run ```dcurooms -laC 21 1 1600``` or ```dcurooms --lookup --available --grattan 21 4 1600```.

For help run ```dcurooms -h``` and for the current version run ```dcurooms --version```.
