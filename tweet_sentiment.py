import sys
import json
import re

"""
def hw():
	print 'Hello, world!'

def lines(fp):
	print str(len(fp.readlines()))
"""
def json_parse_text():
	tweet_encoded=open(sys.argv[2])
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
	afinnfile = open(sys.argv[1])
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	#print scores.items() # Print every (term, score) pair in the dictionary
	return scores

def score_report(score,tweet):
	tweet_score=[0]*len(tweet)
	for line in tweet:
		for key in score.keys():		
			i=tweet.index(line)
			#print i
			occur=len(re.findall('\\b'+key+'\\b',line,flags=re.IGNORECASE))
			if occur!=0:
				tweet_score[i]=tweet_score[i]+score[key]*occur
	for x in tweet_score:
		print x
	#print tweet_score
	return tweet_score
		
	
	
def main():
	
	afinn=afinn_parse()
	tweet=json_parse_text()
	score_report(afinn,tweet)
"""
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	hw()
	lines(sent_file)
	lines(tweet_file)
	sent_file.close()
	tweet_file.close()
"""
	
if __name__ == '__main__':
	main()
