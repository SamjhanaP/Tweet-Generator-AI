# ### Tweets Cleaner STEPS

# 1. @mentions
# 2. url links
# 3. hashtag - remove #only but keep text
# 4. punctuation
# 5. stop words
# 6. Replace abbreviations and some spell correction [Cleaning]
# 7. lowercase


import re, string
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gingerit.gingerit import GingerIt

def removeMention(text):
    return re.sub(r'@[A-Za-z0-9]+','',text)

def removeUrl(text):
    return re.sub('https?://[A-Za-z0-9./]+','',text)

def removeHashtag(text):
    return re.sub(r'#', '', text)

def removePunctuation(text):
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    return regex.sub('', text)

def removeStopWords(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    return " ".join(filtered_sentence)

def fixSlangAndSpelling(text):
    parser = GingerIt()
    return parser.parse(text)['result']

def changeToLower(text):
    return text.lower()

def cleanTweet(tweet, verbose = False):
    if tweet is None:
        return ""
    
    tweet = changeToLower(tweet)
    if verbose: print(f"changeToLower: \n{tweet}\n")
                   
#     tweet = fixSlangAndSpelling(tweet)
#     if verbose: print(f"fixSlangAndSpelling: \n{tweet}\n")

    tweet = removeMention(tweet)
    if verbose: print(f"removeMention: \n{tweet}\n")
    
    tweet = removeUrl(tweet)
    if verbose: print(f"removeUrl: \n{tweet}\n")

    tweet = removeHashtag(tweet)
    if verbose: print(f"removeHashtag: \n{tweet}\n")

    tweet = removePunctuation(tweet)
    if verbose: print(f"removePunctuation: \n{tweet}\n")
        
    tweet = removeStopWords(tweet)
    if verbose: print(f"removeStopWords: \n{tweet}\n")

    return tweet