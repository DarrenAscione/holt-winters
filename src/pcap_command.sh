#!/bin/bash 

echo ">>> Converting PCAP file to TXT >>>"

FILENAME=${1? Error: "no file given"}
DEST=${2? Error: "no dest given"}

tshark -r ../data/PCAP/$FILENAME -Y "ip.src==192.168.1.40 or ip.src==192.168.1.50 && cip" -T fields -e ip.src -e ip.dst -e frame.number -e _ws.col.Info -E header=y > ../data/TIME/40$DEST
#tshark -r ../data/PCAP/$FILENAME -Y "ip.src==192.168.1.50 && cip" -T fields -e ip.src -e ip.dst -e frame.number -e _ws.col.Info -E header=y > ../data/TIME/50$DEST

echo "."
echo "."
echo "."
echo ">>> Conversion Completed!! >>>"
