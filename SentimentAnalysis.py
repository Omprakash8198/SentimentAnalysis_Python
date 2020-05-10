
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(word):
    for char in punctuation_chars:
        word=word.replace(char,"")
        
    return word

def get_pos(sentences):
    sent_lst=sentences.split()
    pos_count=0
    for wrd in sent_lst:
        wrd=wrd.lower()
        #print(wrd)
        wrd=strip_punctuation(wrd)
        #print(wrd)
        if wrd in positive_words:
            pos_count+=1
            
    return pos_count
                    
def get_neg(sentences):
    sent_lst=sentences.split()
    neg_count=0
    for wrd in sent_lst:
        wrd=wrd.lower()
        #print(wrd)
        wrd=strip_punctuation(wrd)
        #print(wrd)
        if wrd in negative_words:
            neg_count+=1
            
    return neg_count            
            
ptd_filename=open("project_twitter_data.csv","r")

with open('resulting_data.csv',"w") as rdc_file:
    rdc_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    rdc_file.write('\n')
    
    lines=ptd_filename.readlines()
    for line in lines[1:]:
        cont_lst=line.strip().split(',')
        rdc_file.write('{}, {}, {}, {}, {}'.format(cont_lst[1],cont_lst[2],get_pos(cont_lst[0]), get_neg(cont_lst[0]), (get_pos(cont_lst[0])-get_neg(cont_lst[0]))))
        rdc_file.write('\n')

        
ptd_filename.close()

