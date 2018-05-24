import re
import sys
import itertools
import NLPlib
from random import randint


def feat1(text):
	"""
	Takes in a sentence and returns the number of pronouns in first person.
	"""
	count1 = len(re.findall(r'(\b(I|i|me|Me|my|My|mine|Mine|we|We)\b)', text))
	count2 = len(re.findall(r'(\b(ours|Ours|our|Our|us|Us)\b)', text))
	#count = len(re.findall(r'(\b(I|i|(M|m)e)|(m|M)y|(m|M)ine|(w|W)e|(u|U)s|(o|O)ur|(o|O)urs\b)', text))
	return count1 +count2
	
def feat2(text):
	"""
	Takes in a sentence and returns the number of pronouns in second person.
	"""
	count1 = len(re.findall(r'(\b(you|You|your|Your|yours|Yours)\b)', text))
	count2 = len(re.findall(r'(\b(u|U|ur|Ur|urs|Urs)\b)', text))
	#count = len(re.findall(r'(\b(y|Y)ou|(y|Y)our|(y|Y)ours|(u|U)|(u|U)r|(u|U)rs\b)', text))
	return count1 + count2

	
def feat3(text):
	"""
	Takes in a sentence and returns the number of pronouns in third person.
	"""
	#count = len(re.findall(r'(\b()\b)', text))
	count1 = len(re.findall(r'(\b(Their|theirs|Theirs|her|Her|hers)\b)', text))
	count2 = len(re.findall(r'(\b(he|He|him|Him|His|his|she|She)\b)', text))
	count3 = len(re.findall(r'(\b(Hers|it|It|its|Its|they|They|them)\b)', text))
	count4 = len(re.findall(r'(\b(Them|their)\b)', text))
	return count1 + count2 +count3+count4

def feat4(text):
	"""
	Takes in a sentence and returns the number of conjunctions.
	"""
	count1 = len(re.findall(r'(\b(alternatively|Alternatively)\b)', text))
	count2 = len(re.findall(r'(\b(altogether|Altogether|conversely)\b)', text))
	count3 = len(re.findall(r'(\b(Conversely|e.g.|E.g.|else|Else)\b)', text))
	count4 = len(re.findall(r'(\b(furthermore|Furthermore|hence|Hence)\b)', text))
	count5 = len(re.findall(r'(\b(however|However|i.e.|I.e.|instead)\b)', text))
	count6 = len(re.findall(r'(\b(Instead|likewise|Likewise)\b)', text))
	count7 = len(re.findall(r'(\b(moreover|Moreover|namely|Namely)\b)', text))
	count8 = len(re.findall(r'(\b(nevertheless|Nevertheless)\b)', text))
	count9 = len(re.findall(r'(\b(nonetheless|Nonetheless)\b)', text))
	count10 = len(re.findall(r'(\b(notwithstanding|Notwithstanding)\b)', text))
	count11 = len(re.findall(r'(\b(otherwise|Otherwise|rather)\b)', text))
	count12 = len(re.findall(r'(\b(Rather|similarly|Similarly)\b)', text))
	count13 = len(re.findall(r'(\b(therefore|Therefore|thus|Thus)\b)', text))
	count14 = len(re.findall(r'(\b(viz.|Viz.)\b)', text))

	return count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8 + count9 + count10 + count11 + count12 + count13 + count14

	
def feat5(text):
	"""
	Takes in a sentence and counts the number of past tense verbs.
	"""
	count = len(re.findall(r'(\b(VBD)\b)', text))
	return count

def feat6(text):
	"""
	Takes a sentence and returns the number of future tense verbs.
	"""
	count1 = len(re.findall(r'(\b(gonna|will|\'ll)\b)', text))
	count2 = len(re.findall(r'(\b(going/VBG to\/TO\s\w+\/VB)\b)', text))
	return count1 + count2

def feat7(text):
	"""
	Takes a sentence and returns the number of commas.
	"""
	count = len(re.findall(r',\/,', text))
	return count

def feat8(text):
	"""
	Takes a sentence and returns the number of colons.
	"""
	count = len(re.findall(r':\/:', text))
	return count

def feat9(text):
	"""
	Takes a sentence and returns the number of dashes
	"""
	count = len(re.findall(r'-', text))
	return count

def feat10(text):
	"""
	Takes a sentence and returns the number of parentheses.
	"""
	count = len(re.findall(r'\(.*\)', text))
	return count

def feat11(text):
	"""
	Takes a sentence and counts the number of elipsis.
	"""
	count = len(re.findall(r'...\/:', text))
	return count

def feat12(text):
	"""
	Takes a sentence and counts the number of common nouns by its tag.(NN,NNS)
	"""
	count = len(re.findall(r'(\b(NN|NNS)\b)', text))
	return count

def feat13(text):
	"""
	Takes a sentence and counts the number of propoer nouns by its tag.(NNP,NNPS)
	"""
	count = len(re.findall(r'(\b(NNP|NNPS)\b)', text))
	return count

def feat14(text):
	"""
	Takes a sentence and counts the number of adverbs by its tag.(RB,RBR,RBS)
	"""
	count = len(re.findall(r'(\b(RB|RBR|RBS)\b)', text))
	return count

def feat15(text):
	"""
	Takes a sentence and returns the number of wh-words.
	"""
	count = len(re.findall(r'(\b(WDT|WP|WP$|WRB)\b)', text))
	return count

def feat16(text):
	"""
	Takes a sentence and returns the number of slang words.
	"""
	count1 = len(re.findall(r'(\b(smh|fwb|lmfao|lmao|lms|tbh|rofl)\b)', text))
	count2 = len(re.findall(r'(\b(wtf|bff|wyd|lylc|brb|atm|imao)\b)', text))
	count3 = len(re.findall(r'(\b(sml|btw|bw|imho|fyi|ppl|sob|ttyl)\b)', text))
	count4 = len(re.findall(r'(\b(imo|ltr|thx|kk|omg|ttys|afn|bbs)\b)', text))
	count5 = len(re.findall(r'(\b(cya|ez|f2f|gtr|ic|jk|k|ly|ya)\b)', text))
	count6 = len(re.findall(r'(\b(nm|np|plz|ru|so|tc|tmi|ym|ur|u)\b)', text))
	count7 = len(re.findall(r'(\b(sol|lol)\b)', text))
	return count1 + count2 +count3 +count4+count5+count6+count7



def feat17(text):
	"""
	Takes a sentence and returns the number of words all in Uppercase.
	"""
	#2 or more caps letts letters form a uppercase word.
	count = len(re.findall(r'[A-A]{2,}\/\w+',text))
	return count

def feat18(num_token_sent,num_sents):
	"""
	Given the total number of tokens and the number of sentences, returns
	the average sentence length.
	"""
	avg_sent_length = num_token_sent / num_sents
	return avg_sent_length

def feat19(token_length,num_tokens):
	"""
	Given the length of tokens and the total number of them, returns the 
	average token length (in characters.)
	"""
	avg_token_length = token_length/num_tokens
	return avg_token_length
def feat20(num_sents):
	"""
	Given the total number of tweets reutrn the amount.
	"""
	return num_sents

def arff_features():
	arff_file.write('@relation twit_classification\n\n')
	arff_file.write('@attribute "feat1" numeric\n')
	arff_file.write('@attribute "feat2" numeric\n')
	arff_file.write('@attribute "feat3" numeric\n')
	arff_file.write('@attribute "feat4" numeric\n')
	arff_file.write('@attribute "feat5" numeric\n')
	arff_file.write('@attribute "feat6" numeric\n')
	arff_file.write('@attribute "feat7" numeric\n')
	arff_file.write('@attribute "feat8" numeric\n')
	arff_file.write('@attribute "feat9" numeric\n')
	arff_file.write('@attribute "feat10" numeric\n')
	arff_file.write('@attribute "feat11" numeric\n')
	arff_file.write('@attribute "feat12" numeric\n')
	arff_file.write('@attribute "feat13" numeric\n')
	arff_file.write('@attribute "feat14" numeric\n')
	arff_file.write('@attribute "feat15" numeric\n')
	arff_file.write('@attribute "feat16" numeric\n')
	arff_file.write('@attribute "feat17" numeric\n')
	arff_file.write('@attribute "feat18" numeric\n')
	arff_file.write('@attribute "feat19" numeric\n')
	arff_file.write('@attribute "feat20" numeric\n')
	arff_file.write('@attribute "class" {0, 4}\n')

	arff_file.write('\n@data\n')
	

def buildarff(twt_file, arff_file, tweetlimit):
	
	#Print the relation name, attributes.
	arff_features()
	data_list=[]
	tweet_list = []
	
	for line in twt_file:
		tweet_list.append(line)

	#initialize data array
	f1count=0
	f2count=0
	f3count=0
	f4count=0
	f5count=0
	f6count=0
	f7count=0
	f8count=0
	f9count=0
	f10count=0
	f11count=0
	f12count=0
	f13count=0
	f14count=0
	f15count=0
	f16count=0
	f17count=0
	f18count=0
	f19count=0
	f20count=0
	class_num= 0
	
	
	line_features = [f1count,f2count,f3count,f4count,f5count,f6count,f7count,f8count,f9count,f10count,f11count,f12count,f13count,f14count,f15count,f16count,f17count,f18count,f19count,f20count,class_num]
	
	#Global counters for calculation features 18,19,20.
	num_sents = 0
	num_token_sent = 0

	num_tokens = 0
	token_length = 0

	for i in range(0,len(tweet_list)):
		#it is a sentence
		if not re.match(r'<A=\d>',tweet_list[i]):
			f1count += feat1(tweet_list[i])
			f2count += feat2(tweet_list[i])
			f3count += feat3(tweet_list[i])
			f4count += feat4(tweet_list[i])
			f5count += feat5(tweet_list[i])
			f6count += feat6(tweet_list[i])
			f7count += feat7(tweet_list[i])
			f8count += feat8(tweet_list[i])
			f9count += feat9(tweet_list[i])
			f10count += feat10(tweet_list[i])
			f11count += feat11(tweet_list[i])
			f12count += feat12(tweet_list[i])
			f13count += feat13(tweet_list[i])
			f14count += feat14(tweet_list[i])
			f15count += feat15(tweet_list[i])
			f16count += feat16(tweet_list[i])
			f17count += feat17(tweet_list[i])
			
			num_token_sent += len(tweet_list[i].split(" "))
			
			num_sents += 1
			#the punctuation mark itself followed by the appropiate tag assigned to it
			#followed by a space and any other non-space character.
			
			no_punc_tokens = re.findall(r'\S+\/[^$#,\.:]\S+',tweet_list[i])
			for token in no_punc_tokens:
				num_tokens+=1
				token = re.sub(r'(.+)\/(.+)',r'\1',token)
				token_length += len(token)

			#assign counts to the appropiate element in the array
			line_features[0] = f1count
			line_features[1] = f2count
			line_features[2] = f3count
			line_features[3] = f4count
			line_features[4] = f5count
			line_features[5] = f6count
			line_features[6] = f7count
			line_features[7] = f8count
			line_features[8] = f9count
			line_features[9] = f10count
			line_features[10] = f11count
			line_features[11] = f12count
			line_features[12] = f13count
			line_features[13] = f14count
			line_features[14] = f15count
			line_features[15] = f16count
			line_features[16] = f17count


		else:
			#For the first tweet, we know the demarcation since its the first 
			#line
			if i == 0:
				f1count=0
				f2count=0
				f3count=0
				f4count=0
				f5count=0
				f6count=0
				f7count=0
				f8count=0
				f9count=0
				f10count=0
				f11count=0
				f12count=0
				f13count=0
				f14count=0
				f15count=0
				f16count=0
				f17count=0
				f18count=0
				f19count=0
				f20count=0
				
				class_num=0
			#print line_features
			#print "tag at", i
				line_features = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
				line_features[20] = int(re.match(r'<A=(\d)>',tweet_list[0]).groups()[0])
			else:
				data_list.append(line_features)
				f1count=0
				f2count=0
				f3count=0
				f4count=0
				f5count=0
				f6count=0
				f7count=0
				f8count=0
				f9count=0
				f10count=0
				f11count=0
				f12count=0
				f13count=0
				f14count=0
				f15count=0
				f16count=0
				f17count=0
				f18count=0
				f19count=0
				f20count=0
				
				class_num=0
			#print line_features
			#print "tag at", i
				line_features = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
				line_features[20] = int(re.match(r'<A=(\d)>',tweet_list[i]).groups()[0])
	#For the last tweet
	data_list.append(line_features)
	#avg_sent_length = num_token_sent / num_sents
	avg_sent_length = feat18(num_token_sent,num_sents)
	#avg_token_length = token_length/num_tokens
	avg_token_length = feat19(token_length,num_tokens)
	
	#print(num_token_sent)
	#print(num_sents)
	#print(avg_sent_length)
	#print(token_length)
	#print(num_tokens)
	#print(avg_token_length)
	#print(avg_sent_length)
	#print(num_token_sent)
	#print(num_sents)
	num_sents = feat20(num_sents)

	#append global data to each tweet
	for l in data_list:
		l[17] = avg_sent_length
		l[18] = avg_token_length
		l[19] = num_sents
		#print l
	
	#print(data_list)
	
	#Combines each count in tweet as an entire string seperated by spaces.
	data_list = [' '.join(str(token) for token in tweet)for tweet in data_list]
	#print (data_list[0:5])
	#print(data_list)

	
	#check third argument for specified format
	if tweetlimit == -1:
		print "tweetlimit is -1"
		for count in data_list:
			count = count + '\n'
			arff_file.write(count)
		
	else:
		
		#Collect n tweets for each class specified by the thrid system argument.
		print "tweetlimit NOT -1"
		#print tweetlimit
		c4count = 0
		c0count = 0
		class_tweet_list = []
		for tweet in data_list:
			#print tweet 
			split_tweet = tweet.split(" ")
			#print split_tweet[20]
			if split_tweet[20] == '4' and c4count < float(tweetlimit):
				class_tweet_list.append(tweet)
				c4count += 1
			elif split_tweet[20] == '0' and c0count < float(tweetlimit):
				class_tweet_list.append(tweet)
				c0count += 1
		#print class_tweet_list
		for tweet in class_tweet_list:
			tweet = tweet + '\n'
			arff_file.write(tweet)
		
		
		

if __name__ == '__main__':
	#print len(sys.argv)
	if len(sys.argv) == 3:
		print "USING TWO ARGUMENTS"
		#output of twtt.py
		#input_file = "test.twt"
		input_file = sys.argv[1]
		#arff file
		#output_file = "test.arff" 
		output_file = sys.argv[2] 
		tweetlimit = -1
		tagger = NLPlib.NLPlib()

		with open(input_file, 'r') as twt_file, open(output_file, 'w') as arff_file:
			buildarff(twt_file, arff_file, tweetlimit)
	elif len(sys.argv) == 4:
		print "USING THREE ARGUMENTS"
		print sys.argv
		#output of twtt.py
		#input_file = "train.twt"
		input_file = sys.argv[1]
		#arff file
		#output_file = "train.arff"
		output_file = sys.argv[2] 
		tweetlimit = sys.argv[3]
		print tweetlimit
		if int(sys.argv[3]) >= 20000:
			print "True"
			tweetlimit = -1
		else:
			tweetlimit = sys.argv[3]
		print tweetlimit
		
		tagger = NLPlib.NLPlib()

		with open(input_file, 'r') as twt_file, open(output_file, 'w') as arff_file:
			buildarff(twt_file, arff_file, tweetlimit)
	else:
		print "ERROR"

