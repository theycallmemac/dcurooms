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
To check the current availabilty of labs in the DCU School of Computing run ```dcurooms -nc``` or ```dcurooms --now --computing```.

To show the rooms which are currently free in the Henry Grattan building run ```dcurooms -fnc``` or ```dcurooms --free --now --computing```.


For help run ```dcurooms -h``` and for the current version run ```dcurooms --version```.
