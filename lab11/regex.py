import re

counter = 0
file_name = "server.log.2018-04-12"
file = open(file_name, "r")
pattern = ' Caused by: '
for line in file.readlines():
    if re.findall(pattern, line):
        counter += 1
        print(line)

print("Number of matches:", counter)

