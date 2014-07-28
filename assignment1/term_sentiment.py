import sys
import json
import re
import codecs

"""
def hw():
	print 'Hello, world!'

def lines(fp):
	print str(len(fp.readlines()))
"""

def json_parse_text():
	with open(sys.argv[2]) as tweet_encoded:
		lst=[]
		for l in tweet_encoded:
			json_decoded=json.loads(l)
			s=json_decoded.get("text")
			if s:
				s_encode=s.encode('utf-8',errors='ignore')
				#print s
				lst.append(s_encode)
				#print lst
			#print lst
		return lst	

def afinn_parse():
	with open(sys.argv[1]) as afinnfile:
		scores = {} # initialize an empty dictionary
		for line in afinnfile:
			term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
			scores[term] = int(score)  # Convert the score to an integer.
		#print scores.items() # Print every (term, score) pair in the dictionary
		return scores		
		
def search_non_senti(list,dict):
	non_senti=[]
	for line in list:
		tweet_word=re.findall('\w+',line,flags=re.IGNORECASE)
		for word in tweet_word:
			if not (word in dict.keys()):
				non_senti.append(word)
	non_dup_senti=set(non_senti)
	for word in non_dup_senti.copy():
		for i in word:
			if (ord(i) > 90 and ord(i) < 97) or (ord(i) > 122 or ord(i) < 65):
				non_dup_senti.remove(word)
				break
	return non_dup_senti		#return a set instead of a list	
	
	

def main():
	tweet_list=json_parse_text()
	senti_dict=afinn_parse()
	nonsenti_list=search_non_senti(tweet_list,senti_dict)
	print nonsenti_list
	
"""
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	hw()
	lines(sent_file)
	lines(tweet_file)
"""

if __name__ == '__main__':
	main()
