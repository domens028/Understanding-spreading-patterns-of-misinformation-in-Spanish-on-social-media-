#!/bin/bash
cd /Users/domingomenendezrua/Desktop/TFG/backup;
pip3 install requests
python3 dataCollection.py 
export DATE="$( date +%d-%b )"
mkdir $DATE
mv *.json $DATE
cd $DATE

