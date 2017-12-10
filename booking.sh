OPTION=$1
ARG1=$2


DIR=$HOME/Documents/Redbrick/EventScripts/RoomBooking/
cd $DIR

if [ $OPTION == '-h' ] || [ $OPTION == '--help' ];then
echo -e "NAME"
echo -e "    booking - interacts with scripts to automate events officer tasks\n"
echo -e "DESCRIPTION"
echo -e "    -r   To book a room using DCU registry booking forms:- booking -r\n"
echo -e "    -l   To book a lab by emailing the DCU School of Computing secretary:- booking -l LG25\n"
echo -e "    -c    Checks a rooms availability during a given timeslot:- booking -c\n"
echo -e "    -h    Brings up these options:- booking -h\n"
echo -e "AUTHOR"
echo -e "    James McDermott (theycallmemac)\n"
exit 0
fi


if [ $OPTION == '-c' ] || [ $OPTION == '--check' ];then
  python check_availability.py $ARG1
fi


if [ $OPTION == '-l' ] || [ $OPTION == '--lab' ];then
    python book_lab.py $ARG1
fi


if [ $OPTION == '-r' ] || [ $OPTION == '--room' ];then
  python book_room.py $ARG1
fi

