import re


pattern = r"eggs"

if re.match(pattern,"BACONeggseggseggsBACON"):
    print('match found')
else:
     print('no match found')
# -----------------------------------------------------------
if re.search(pattern, "BACONeggseggseggsBACON"):
    print('match found')
else:
    print('no mTCH found')
# ------------------------------------------------------------
if re.findall(pattern, "BACONeggseggseggsBACON"):
    print('match found')
else:
    print('no mTCH found')
# -------------------------------------------------------------
print(re.findall(pattern, "BACONeggseggseggsBACON"))
# ---------------------------------------------------------------
# find & replace
string = "my name is minal"
pattern = r"minal"
newstring = re.sub(pattern, "meenal", string)
print(newstring)