#!/bin/bash 

echo ">>> Converting PCAP file to TXT >>>"

FILENAME=${1? Error: "no file given"}
DEST=${2? Error: "no dest given"}

tshark -r ../data/PCAP/$FILENAME -T fields -e frame.number -e frame.time_delta -E header=y > ../data/TIME/$DEST
echo "."
echo "."
echo ">>> Conversion Completed!! >>>"
