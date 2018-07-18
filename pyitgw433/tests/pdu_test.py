from pyitgw433 import Pdu

pdus = [
# 0: Livinroom West 0% - 50% - 100% - off - on
[ 0,0,6,0,256,75,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,39,0 ],
# 1
[ 0,0,6,0,256,75,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,39,0 ],
# 2
[ 0,0,6,0,256,75,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,39,0 ],
# 3
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,39,0 ],
# 4
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,39,0 ],
# 5: Bedroom on
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,39,0 ],
# 6: Bedroom
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,39,0 ],
# 7: Corrior south on
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,39,0 ],
# 8: Corrior south off
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,39,0 ],
# 9: Corridor north on 
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,39,0 ],
# 10: Corridor north off
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,39,0 ],
# 11
[ 0,0,6,0,256,75,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,39,0 ],
# 12
[ 0,0,6,0,256,75,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,39,0 ],
# 13
[ 0,0,6,0,256,75,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,39,0 ],
# 14
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,39,0 ],
# 15
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,39,0 ],
# 16
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,39,0 ],
# 17
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,39,0 ],
# 18
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,39,0 ],
# 19
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,39,0 ],
# 20
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,39,0 ],
# 21
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,39,0 ],
# 22
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,39,0 ],
# 23
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,39,0 ],
# 24
[ 0,0,6,0,256,67,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,39,0 ],
# 25
[ 0,0,6,0,256,75,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,39,0 ],
# 26
[ 0,0,6,0,256,75,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,39,0 ],
# 27
[ 0,0,6,0,256,75,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,39,0 ],
# 28
[ 0,0,6,0,256,75,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,39,0 ],
# 29
[ 0,0,6,0,256,75,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,39,0 ],
# 30
[ 0,0,6,0,256,75,0,1,10,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,1,1,1,1,5,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,5,1,1,1,39,0 ]
]

outputs = [
    "H75____|__|_|_|____|__|__|||||o_|__||||E",
    "H75____|__|_|_|____|__|__|||||o_|___|||E",
    "H75____|__|_|_|____|__|__|||||o_|______E",
    "H67____|__|_|_|____|__|__||||||_|__E",
    "H67____|__|_|_|____|__|__|||||__|__E",
    "H67____|__|_|_|____|__|__|||||_____E",
    "H67____|__|_|_|____|__|__||||||____E",
    "H67____|__|_|_|____|__|__|||||_||__E",
    "H67____|__|_|_|____|__|__||||||||__E",
    "H67____|__|_|_|____|__|__|||||___|_E",
    "H67____|__|_|_|____|__|__||||||__|_E",
    "H75____|__|_|_|____|__|__|||||o_|__||__E",
    "H75____|__|_|_|____|__|__|||||o_|__||||E",
    "H75____|__|_|_|____|__|__|||||o_|__||||E",
    "H67____|__|_|_|____|__|__||||||____E",
    "H67____|__|_|_|____|__|__|||||_____E",
    "H67____|__|_|_|____|__|__||||||_|__E",
    "H67____|__|_|_|____|__|__|||||_||__E",
    "H67____|__|_|_|____|__|__|||||___|_E",
    "H67____|__|_|_|____|__|__||||||__|_E",
    "H67____|__|_|_|____|__|__||||||||__E",
    "H67____|__|_|_|____|__|__||||||_|__E",
    "H67____|__|_|_|____|__|__|||||||___E",
    "H67____|__|_|_|____|__|__|||||_|___E",
    "H67____|__|_|_|____|__|__||||||____E",
    "H75____|__|_|_|____|__|__|||||o_|__||||E",
    "H75____|__|_|_|____|__|__|||||o_|___|||E",
    "H75____|__|_|_|____|__|__|||||o_|______E",
    "H75____|__|_|_|____|__|__|||||o|___||||E",
    "H75____|__|_|_|____|__|__|||||o|___|___E",
    "H75____|__|_|_|____|__|__|||||o|_______E"
]

def test_pdu_analysis():
    for i in range(0, len(pdus)):
        assert str(Pdu(pdus[i])) == outputs[i]