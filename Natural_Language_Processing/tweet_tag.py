import codecs
import re
import NLPlib
import csv
import sys
from HTMLParser import HTMLParser


def twtt1(text):
    """
    Takes in a tweet and returns it without any html tags and attributes.
    """
    return re.sub(r'<[^>]+>','',text)

def twtt2(text):
    """
    Takes in a tweet and replaces html character codes with their ASCII equivalent.
    """
    htmlparser = HTMLParser()
    #unescape function takes in a html tag and converts it to bytecode
    #encode takes result and turns it into ascii equivalent
    return htmlparser.unescape(text).encode('utf-8','ignore')

def twtt3(text):
    """
    Takes in a tweet and removes all URLs.
    """

    #pattern handles variable amount of links, including different domains.
    #remove www
    no_www = re.sub(r'www[\S]+', '',text)
    #then remove http 
    return re.sub(r'http[\S]+', '',no_www) 

def twtt4(text):
    """
    Takes in a tweet and removes hashtags and the symbol before the username
    """

    #remove hashtag
    no_hashtag = re.sub(r'#([\w]+)', r'\1',text)
    #remove user symbol
    return re.sub(r'@([\w]+)', r'\1', no_hashtag)

def twtt5(text):
    """
    Takes in a tweet and returns the tweet seperated by sentences based on 
    a approximation heuristic
    """

    #find all words with a period
    candidate_end_words = re.findall(r'\s\w+\.+[\s|\n]+\w', text)


    #Mark candidates as valid when they are not an abbreviation or part of an
    #elipsis and the word right after is lower case
    for word in candidate_end_words:
        #strip spaces
        word = word.strip(" ")
        if word.lower() in abv_list or "..." in word.lower() or ".." in word.lower():
            pass
        else:
            text = text.replace(word, word[:-1] + "/SENT" + ".")

    #? and ! denote an end of a sentence.
    definite_end_words = re.findall(r'[\?|!]+[\s|\n]', text)
    for word in definite_end_words:
        text = text.replace(word, word[:-1] + "/SENT")

    #remove the empty string 
    new_text = text.strip('/SENT').split('/SENT')
    
    return new_text


def twtt7(text):
    """
    Takes in a tweet and adds a space for each token including punctuation and 
    clitics.
    """
    #example: dogs'
    plural = re.sub(r'([A-z]+[s|S])(\')',r'\1 \2',text) 
    return re.sub(r'([A-z])(\'[s|S])',r'\1 \2',plural)

def rm_space(text):
    """
    Takes in a tweet and removes double spaces
    """
    return re.sub(r'\s\s+', ' ', text)


def token_punctuation(text):
    """
    Takes in a tweet now sentence(s) and splits punctuation marks with a space.
    """
    return re.sub(r'(\w+)([!;:.,?])',r'\1 \2', text)

def token_contraction(text):
    """
    Takes in a tweet now sentence(s) and splits contractions with a space.
    """
    contraction_list = ["'d", "'ll","'m","'re","'ve"]
    #find all words with a '
    candidate_contractions = re.findall(r'[A-z]+\'[A-z]+', text)
    for candidate in candidate_contractions:
        #e.g. John's, they've
        short_form = re.search(r'\'[A-z]+',candidate).group()
        #e.g don't, won't
        negations = re.search(r'[n|N]\'[t|T]', candidate)
        #Spacing specififed from handout: e.g. don't -> do, n't
        if negations is not None:
            text = text.replace(candidate, candidate[:-3] + " " + negations.group())
        #find the word without the contraction
        elif short_form.lower() in contraction_list:
            text = text.replace(candidate, candidate[:-len(short_form)] + " " + short_form)
    return text


def recombine_tokens(tokens):
    sentence = ""
    for token in tokens:
        sentence = sentence + token + " "
    return sentence[:-1]

def twtt9(tweet):
    """
    Takes in a tweet and returns the class with specified format.
    """ 
    tweet_class = '<A=' + tweet + '>'
    return tweet_class

def twtt8(tokens):
    """
    Takes a list of tokens and tags them.
    """
    tagged_tokens= tagger.tag(tokens)
    return tagged_tokens




def twtt(input_file,output_file,sid):
    tweet_list = []
    for tweet in input_file:
    	tweet_list.append(tweet)
    
    X = (int(sid) % 80)
    if "training" in sys.argv[1]:
        print "USING TRAINING"
        tweet_list_1 = tweet_list[X*10000:(X*10000)+10000]
        tweet_list_2 = tweet_list[X*10000+800000:X*10000+800000+10000]
        tweet_list = tweet_list_1 + tweet_list_2
    elif "test" in sys.argv[1]:
        print "USING TESTING"
        pass
    else:
        print "ERROR"
        pass
    #print len(tweet_list_1)
    #print len(tweet_list_2)
    
    #print len(tweet_list)
    
    #Loop through each row given by the csv file 
    #TESTING
    #for i in range(0,len(tweet_list)):
    for i in range(0,len(tweet_list)):
        tweet_text= tweet_list[i][5].decode('utf-8', 'ignore')
        #run through twtt functions, results is a list of possible sentences
        #within the tweet
        filtered_text = twtt1(tweet_text)
        #print filtered_text
        filtered_text = twtt2(filtered_text)
        #print filtered_text
        filtered_text = twtt3(filtered_text)
        #print filtered_text
        filtered_text = twtt4(filtered_text)
        #print filtered_text
        filtered_text = twtt7(filtered_text)
        #print filtered_text
        filtered_text = rm_space(filtered_text)
        #print filtered_text
        filtered_text = twtt5(filtered_text)
        #print filtered_text
        try:
            #tweet class in first column from the csv file
            
            tweet_class = twtt9(tweet_list[i][0])
            output_file.write(tweet_class + "\n")

            #loop through each sentence(s)
            for j in range(0,len(filtered_text)):
                #output_file.write("SENTENCE:")
                #functions to split for tagging punctuation and contraction properly.
                filtered_text[j] = token_punctuation(filtered_text[j])
                filtered_text[j] = twtt7(filtered_text[j])
                filtered_text[j] = token_contraction(filtered_text[j])
                tokens = filtered_text[j].strip().split(" ")
                #tag tokens and merge and then output to file
                tagged_tokens= twtt8(tokens)
                token_and_tag = []
                for i in range(len(tokens)):
                    token_and_tag.append(tokens[i] + "/" + tagged_tokens[i])
                final_sentence = recombine_tokens(token_and_tag)
                output_file.write(final_sentence + "\n")
        except UnicodeDecodeError:
            pass
        except UnicodeEncodeError:
            pass

if __name__ == "__main__":

    #input file
    #csv_name = "/u/cs401/A1/tweets/training.1600000.processed.noemoticon.csv"
    #csv_name = "/u/cs401/A1/tweets/testdata.manualSUBSET.2009.06.14.csv"
    csv_name = sys.argv[1]
    #output file
    #tweet_name = "test.twt"
    tweet_name = sys.argv[3]
    #student number
    #sid = "998689593"
    sid = sys.argv[2]
    #Abbreviations
    ABV_name = "/u/cs401/Wordlists/abbrev.english"
    abv_file = open(ABV_name)
    abv_list = []
    for line in abv_file.readlines():
        abv_list.append(line.strip('\n'))
    abv_file.close()

    input_file = csv.reader(codecs.open(csv_name, 'r'))
    tagger = NLPlib.NLPlib()
    
    with open(tweet_name, 'w') as output_file:
        twtt(input_file, output_file, sid)

    