import sys
import json


f1=open('output.txt')


print f1

#decoded_json=json.load(f1).strip()

#print decoded_json

"""
json_content = []
json_dict = {}
for line in f1:
   json_dict = json.loads(line)
   json_content.append(json_dict)
"""
for lines in f1:
	s = json.loads(lines)
	print s

f1.close()

