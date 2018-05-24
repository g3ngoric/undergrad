#Richard Ngo
#!/usr/bin/env python
import sys
sys.path.append('/u/csc485h/include/a3') 
from Asst3 import nyt_big, nyt_mini, NpPattern, HearstPattern1, HearstPattern2, HearstPattern3, HearstPattern4, HearstPattern5
from nltk.corpus import wordnet as wn
import nltk

# nyt_big  is the full POS-tagged 2004 NY Times corpus. 
# nyt_mini is the first 100K lines of nyt_big. 
# Use nyt_big for your final submission. You can use nyt_mini
# for testing and debugging your code during code development.
# DefaultNpPattern is a simple baseline pattern for NP chunking

# create a chunk parser with the default pattern for NPs
from nltk.chunk.regexp import *
BaselineNpChunkRule = ChunkRule(NpPattern, 
                                'Default rule for NP chunking')
NpChunker = RegexpChunkParser([BaselineNpChunkRule], 
                              chunk_label='NPCHUNK')


HP1 = ChunkRule(HearstPattern1, 
                                'Hearst Pattern Rule 1')

HP2 = ChunkRule(HearstPattern2, 'Hearst Pattern 2')

HP3 = ChunkRule(HearstPattern3, 'Hearst Pattern 3')

HP4 = ChunkRule(HearstPattern4, 'Hearst Pattern 4')

HP5 = ChunkRule(HearstPattern5, 'Hearst Pattern 5')

NpChunker = RegexpChunkParser([HP1,HP2,HP3,HP4,HP5], 
                              chunk_label='NPCHUNK')

# just for the purpose of illustration, print the output of the 
# NP Chunker for the first 3 sentences of nyt_mini

l = []

#[0:3]
#Debugging purposes
none_sents = [794,1822,1838,7038,15311,17369,17865,18386,18939,20681,20688,20799,51134,
        52554,54662,56504,56507,56509,56512,56519,56540,56541,56542,56543,56544,
        56547,56550,56558,56562,64502,66563,73910,73911,78362,85090,89890]

such_as_exact_sents = [4259, 9682, 10087, 18309, 19082, 19650, 19782, 19796, 19801, 20057,
                 21727,22274, 23005, 25618, 28557, 29619, 30771, 36035, 36192, 43486,
                 44740, 55335, 56087, 58702, 59750, 62515, 62927, 66793, 67229, 67272,
                 67276, 67922, 68894, 71293, 73560, 73724, 81153, 81656, 91367, 93485,
                 95426, 95855, 97839, 98206, 98623, 98864]

such_as_variable_sents = [1757, 3121, 5839, 9322, 9754, 9861, 10836, 12046, 12470,
                    13004, 14871, 15326, 16132, 16361, 16425, 18522, 20248,
                    22323, 23784, 26238, 27855, 27872, 28673, 29092, 29648,
                    30411, 31063, 31204, 31694, 31697, 31800, 32854, 33038,
                    35107, 35126, 35507, 40750, 40897, 41960, 43475, 44331,
                    44346, 46140, 46258, 49618, 50999, 51213, 53567, 53946,
                    54544, 55173, 56493, 56823, 58902, 59369, 60514, 61449,
                    62826, 63480, 63699, 64223, 64727, 65356, 65639, 65703,
                    66834, 67202, 68086, 68224, 69695, 75687, 75733, 75821,
                    75885, 77840, 78552, 80906, 81090, 81914, 85154, 86300,
                    86601, 91628, 92606, 93867, 94410, 95255, 97030, 97074,
                    98198, 99755]

other_sents = [] #ALOT
especially_sents = []
including_sents = []

case1_sents = []
case2_sents = []
case3_sents = []
case4_sents = []

wnl = nltk.WordNetLemmatizer()
sents = nyt_big.tagged_sents()
all_pairs = []


for e in range(0,800000):
    #Check if the sentence is malformed (None POS tag)
    skip = False
    for w in range(len(sents[e])):
        if sents[e][w][1] == None:
            skip = True
    if skip == True:
        pass
    else:
        p = NpChunker.parse(sents[e])
        for subtree in p.subtrees():
            rule = 0
            if subtree.label() == 'NPCHUNK':
                words = []
                st = subtree.leaves()

                #add all words from the chunk
                for l in range(len(st)):
                    words.append(st[l][0])

                #Determine which rule to use
                if 'such' in words and 'as' in words:
                    such_index = words.index('such')
                    as_index = words.index('as')
                    if such_index < as_index and as_index - such_index == 1:
                        rule = 1
                        has_chunk = True
                    elif such_index < as_index and as_index - such_index > 1:
                        rule = 2
                        has_chunk = True

                elif 'especially' in words:
                    rule = 5
                    has_chunk = True
                elif 'including' in words:
                    rule = 4
                    has_chunk = True
                elif 'other' in words:
                    rule = 3
                    has_chunk = True
                
                if rule == 0:
                    pass
                else:
                    noun_list_chunk = []
                    subtree_pairs= []
                    #take noun pairs, compute each case
                    
                    #find all NPs
                    for l in subtree.leaves():
                        if 'N' in l[1][0]:
                            noun_list_chunk.append(l[0])
                    #make the pairs in the right order based on the rule 
                    if rule == 1 or rule == 2 or rule == 4 or rule == 5:
                        for n in noun_list_chunk[1:]:
                            r1_pair = []
                            r1_pair.append(wnl.lemmatize(n))
                            r1_pair.append(wnl.lemmatize(noun_list_chunk[0]))
                            subtree_pairs.append(r1_pair)
                    elif rule == 3:
                        for n in noun_list_chunk[:-1]:
                            r1_pair = []
                            r1_pair.append(wnl.lemmatize(n))
                            r1_pair.append(wnl.lemmatize(noun_list_chunk[-1]))
                            subtree_pairs.append(r1_pair)

                    #Evaluation
                    #compute each case for each pair
                    for pair in subtree_pairs:
                        #First time
                        if all_pairs == []:
                            num_case1 = 0
                            num_case2 = 0
                            p1_sets = []
                            p2_sets = []
                            p3_sets = []
                            p4_sets = []
                            case3 = 0
                            case4_set = []
                            case4_count = 0
                            case1_list = []
                            case2_list = []
                            
                            #Case 1
                            for s in wn.synsets(pair[0]):
                                p1_sets.append(s)

                            
                            for s2 in wn.synsets(pair[1]):
                                for hs in s2.hyponyms():
                                    p2_sets.append(hs)

                            for synset in p2_sets:
                                if synset in p1_sets:
                                    case1_list.append(synset)
                                    num_case1 = num_case1+1
                                    #print(synset)
                        
                            #Case 2
                            for s in wn.synsets(pair[0]):
                                for h in s.hyponyms():
                                    p3_sets.append(h)

                            for s in wn.synsets(pair[1]):
                                p4_sets.append(s)
                            
                            for synset in p3_sets:
                                if synset in p4_sets:
                                    case2_list.append(synset)
                                    num_case2 = num_case2 + 1
                                    #print(synset)
                            #Case 3
                            if num_case1 == 0:
                                case3 = case3 + 1

                            #Case 4
                            if wn.synsets(pair[0]) == []:
                                if case4_set != []:
                                    if pair[0] not in case4_set:
                                        case4_set.append(pair[0])
                                else:
                                    case4_set.append(pair[0])
                                    case4_count =case4_count + 1
                            
                                
                                        
                            if wn.synsets(pair[1]) == []:
                                if case4_set != []:
                                    if pair[1] not in case4_set:
                                        case4_set.append(pair[1])
                                    
                                else:
                                    case4_set.append(pair[1])
                                    case4_count = case4_count + 1          
                                    
                                    
                            
                                

                            
                            final_pair = []
                            final_pair.append("SENTENCE") 
                            final_pair.append(e) 
                            final_pair.append(pair)    
                            final_pair.append('LOW')
                            final_pair.append('CASE 1:')
                            final_pair.append(num_case1)
                            final_pair.append(case1_list)
                            final_pair.append('CASE 2:')
                            final_pair.append(num_case2)
                            final_pair.append(case2_list)
                            final_pair.append('CASE 3:')
                            final_pair.append(case3)
                            final_pair.append('CASE 4:')
                            final_pair.append(case4_count)
                            final_pair.append(case4_set)
                            
                            final_pair.append("RULE:")
                            final_pair.append(rule)
                            
                            all_pairs.append(final_pair)
      
                        else:
                            #check if pair is already there
                            new = True
                            for hpair in range(len(all_pairs)):
                                if all_pairs[hpair][2] == pair:
                                    new = False
                                    curr_level = all_pairs[hpair][3]
                                    if curr_level == 'LOW':
                                        curr_level = 'MEDIUM'
                                        all_pairs[hpair][3] = curr_level
                                    elif curr_level == 'MEDIUM':
                                        curr_level = 'HIGH'
                                        all_pairs[hpair][3] = curr_level
                            if new == False:
                                pass
                            else:
                                #non empty list, but first time seeing this pair
                                num_case1 = 0
                                num_case2 = 0
                                p1_sets = []
                                p2_sets = []
                                p3_sets = []
                                p4_sets = []
                                case3 = 0
                                case4_set = []
                                case4_count = 0
                                case1_list = []
                                case2_list = []
                                
                                #Case 1
                                for s in wn.synsets(pair[0]):
                                    p1_sets.append(s)

                                
                                for s2 in wn.synsets(pair[1]):
                                    for hs in s2.hyponyms():
                                        p2_sets.append(hs)

                                for synset in p2_sets:
                                    if synset in p1_sets:
                                        case1_list.append(synset)
                                        num_case1 = num_case1+1
                            
                                #Case 2
                                for s in wn.synsets(pair[0]):
                                    for h in s.hyponyms():
                                        p3_sets.append(h)

                                for s in wn.synsets(pair[1]):
                                    p4_sets.append(s)
                                
                                for synset in p3_sets:
                                    if synset in p4_sets:
                                        case2_list.append(synset)
                                        num_case2 = num_case2 + 1
                                #Case 3
                                if num_case1 == 0:
                                    case3 = case3 + 1

                                #Case 4
                                if wn.synsets(pair[0]) == []:
                                    if case4_set != []:
                                        if pair[0] not in case4_set:
                                            case4_set.append(pair[0])
                                    else:
                                        case4_set.append(pair[0])
                                        case4_count =case4_count + 1
                                
                                    
                                            
                                if wn.synsets(pair[1]) == []:
                                    if case4_set != []:
                                        if pair[1] not in case4_set:
                                            case4_set.append(pair[1])
                                        
                                    else:
                                        case4_set.append(pair[1])
                                        case4_count = case4_count + 1 

                                
                                final_pair = []
                                final_pair.append("SENTENCE") 
                                final_pair.append(e) 
                                final_pair.append(pair)    
                                final_pair.append('LOW')
                                final_pair.append('CASE 1:')
                                final_pair.append(num_case1)
                                final_pair.append(case1_list)
                                final_pair.append('CASE 2:')
                                final_pair.append(num_case2)
                                final_pair.append(case2_list)
                                final_pair.append('CASE 3:')
                                final_pair.append(case3)
                                final_pair.append('CASE 4:')
                                final_pair.append(case4_count)
                                final_pair.append(case4_set)
                                final_pair.append('RULE:')
                                final_pair.append(rule)
                                all_pairs.append(final_pair)
                                

for allp in all_pairs:
    if allp[5] > 0:
        case1_sents.append(allp)
    elif allp[8] > 0:
        case2_sents.append(allp)
    elif allp[11] > 0 and allp[13] > 0:
        case4_sents.append(allp)
    elif allp[11] > 0:
        case3_sents.append(allp)
    else:
        pass

try: 
    print(" ")
    print("===CASE1 START===")
    print(" ")
    for cp in case1_sents:
        print(cp, end=" ")
        print("\n", end=" ")
    print(" ")
    print("===CASE1 END===")
    print(" ")

    print(" ")
    print("===CASE2 START===")
    print(" ")
    for cp in case2_sents:
        print(cp, end=" ")
        print("\n", end=" ")
    print(" ")
    print("===CASE2 END===")
    print(" ")

    


    print(" ")
    print("===CASE3 START===")
    print(" ")
    for cp in case3_sents:
        print(cp, end=" ")
        print("\n", end=" ")
    print(" ")
    print("===CASE3 END===")
    print(" ")

    print(" ")
    print("===CASE4 START===")
    print(" ")
    for cp in case4_sents:
        print(cp, end=" ")
        print("\n", end=" ")
    print(" ")
    print("===CASE4 END===")
    print(" ")
   
except UnicodeEncodeError:
    pass

print(" ")
print("CASE 1 COUNT", len(case1_sents))
print("CASE 2 COUNT", len(case2_sents))
print("CASE 3 COUNT", len(case3_sents))
print("CASE 4 COUNT", len(case4_sents))



