""" 

Usage:

from Asst3 import nyt_big  ## the full NYT corpus for A3
from Asst3 import nyt_mini ## only the first 100K lines from nyt_big, for 
                           ## development 

from Asst3 import DefaultNpChunker ## a simple NP chunker to get things started

"""

# T(he original version of t)his code was written by Ulrich Germann (11/2010)


######################################################################

import nltk
nltk.data.path[0:0] = ['/u/csc485h/include/a3/nltk']

# The following code provides access to the tagged NY Times corpus
# nyt_big is the full corpus
# nyt_mini a small subset for development
from nltk.data         import ZipFilePathPointer
from nltk.corpus       import TaggedCorpusReader

nyt_zipped = ZipFilePathPointer('/u/csc485h/include/a3/nltk/corpora/nyt.zip','nyt/')
nyt_big    = TaggedCorpusReader(nyt_zipped,['2004-tagged.txt'],sep='/', encoding='latin2')
nyt_mini   = TaggedCorpusReader(nyt_zipped,['nytimes-mini.txt'],sep='/', encoding='latin2')

# Finally, let's set up a default pattern for NP chunking
# Setting up the NP chunker itself is left to the main script, to encourage
# trying different variants of the pattern

##  Operator 	Behavior
##  . 	        Wildcard, matches any character
##  ^abc 	Matches some pattern abc at the start of a string
##  abc$ 	Matches some pattern abc at the end of a string
##  [abc] 	Matches one of a set of characters
##  [A-Z0-9] 	Matches one of a range of characters
##  ed|ing|s 	Matches one of the specified strings (disjunction)
##  * 	        Zero or more of previous item, e.g. a*, [a-z]* (also known as Kleene Closure)
##  + 	        One or more of previous item, e.g. a+, [a-z]+
##  ? 	        Zero or one of the previous item (i.e. optional), e.g. a?, [a-z]?
##  {n} 	Exactly n repeats where n is a non-negative integer
##  {n,} 	At least n repeats
##  {,n} 	No more than n repeats
##  {m,n} 	At least m and no more than n repeats
##  a(b|c)+ 	Parentheses that indicate the scope of the operators





NpPattern = ''.join([r'(<DT|AT>?<RB>?)?',
			    r'<JJ.*|CD.*>*',
			    r'(<JJ.*|CD.*><,>)*',
			    r'(<N.*>)+'])



HearstPattern1 = ''.join([r'(<DT|AT>?<RB>?)?',
                          r'<JJ.*|CD.*>*',
                          r'(<JJ.*|CD.*><,>)*',
                          r'(<N.*>)+',
                          r'<,>?',
                          r'(<JJ>)+',
                          r'(<IN>)+',
                          NpPattern,
                          r'(<,>((<DT|AT>?<RB>?)?<JJ.*|CD.*>*(<JJ.*|CD.*><,>)*(<N.*>)+)<,>((<DT|AT>?<RB>?)?<JJ.*|CD.*>*(<JJ.*|CD.*><,>)*(<N.*>)+<,>)*<CC>((<DT|AT>?<RB>?)?<JJ.*|CD.*>*(<JJ.*|CD.*><,>)*(<N.*>)+))*'])

HearstPattern2 = ''.join([r'(<JJ>)',
                          NpPattern,
                          r'(<IN>)',
                          NpPattern,
                          r'(<,>((<DT|AT>?<RB>?)?<JJ.*|CD.*>*(<JJ.*|CD.*><,>)*(<N.*>)+)<,>((<DT|AT>?<RB>?)?<JJ.*|CD.*>*(<JJ.*|CD.*><,>)*(<N.*>)+<,>)*<CC>((<DT|AT>?<RB>?)?<JJ.*|CD.*>*(<JJ.*|CD.*><,>)*(<N.*>)+))*'])

HearstPattern3 = ''.join([NpPattern,
                          r'(<,>((<DT|AT>?<RB>?)?<JJ.*|CD.*>*(<JJ.*|CD.*><,>)*(<N.*>)+<,>)*)*',
                          r'<CC>',
                          r'<JJ>',
                          NpPattern])

HearstPattern4 = ''.join([NpPattern,
                          r'<,>?',
                          r'<VBG>',
                          NpPattern,
                          r'(<,>((<DT|AT>?<RB>?)?<JJ.*|CD.*>*(<JJ.*|CD.*><,>)*(<N.*>)+)<,>((<DT|AT>?<RB>?)?<JJ.*|CD.*>*(<JJ.*|CD.*><,>)*(<N.*>)+<,>)*<CC>((<DT|AT>?<RB>?)?<JJ.*|CD.*>*(<JJ.*|CD.*><,>)*(<N.*>)+))*'])
                          
HearstPattern5 = ''.join([NpPattern,
                          r'<,>?',
                          r'<RB>',
                          NpPattern,
                          r'(<,>((<DT|AT>?<RB>?)?<JJ.*|CD.*>*(<JJ.*|CD.*><,>)*(<N.*>)+)<,>((<DT|AT>?<RB>?)?<JJ.*|CD.*>*(<JJ.*|CD.*><,>)*(<N.*>)+<,>)*<CC>((<DT|AT>?<RB>?)?<JJ.*|CD.*>*(<JJ.*|CD.*><,>)*(<N.*>)+))*'])
                          
                          
                         
#print(HearstPattern1)
