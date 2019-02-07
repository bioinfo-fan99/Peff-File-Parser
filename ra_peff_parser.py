import re
with open('File_Path\sample.peff') as f:
    lines = f.readlines()

#rint(lines[13])
#print(lines[15])
#print(lines[17])
#print(lines[19])
count=13
pattern = ["PE=1","PE=2","PE=3","PE=4","PE=5"]
sequence1 = "PE=1"
start = []
end = []
if (start == "MK" and end == "SV"):
        print ("TRUE")
else:
    print("try again")