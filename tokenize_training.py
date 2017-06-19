import nltk
from nltk.corpus import state_union
from speech_part import return_speech_part_information
from nltk.tokenize import PunktSentenceTokenizer, sent_tokenize

# w tym module znajduja sie funkcja ktore odpowiadaja za przetwarzanie jezyka naturalego (rowniez wersje testowe)


# wykorzystujaca biblioteki nltk funkcja znajdujaca czesci mowy
def training(sample_text):
    try:
        #print(train_text)
        for i in sent_tokenize(sample_text):
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            return tagged

    except Exception as e:
        print(str(e))

# nieuzywana w edytorze funkcja wyszukajaca zwiazki wyrazowe
def chunking(sample_text):
    try:
        #print(train_text)
        for i in sent_tokenize(sample_text):

            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            #<RB adverb (very, silently).any char except new line? (aby bylo RBR RBS)>*
            #(match 0 or more repetitions)<VERBS>*<NNP> -zreczownik osobowy+
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            #chunked.draw()
            print (chunked)

    except Exception as e:
        print(str(e))




def print_speech_table(sample_text):
    tagged = training(sample_text)
    print('|%15s|%15s|%50s|%50s|' % ('word','speech_part','info','info PL'))
    print('-'*80)
    for i in range(len(tagged)):
        print('|%15s|%15s|%50s|%50s|' % (tagged[i][0], tagged[i][1], return_speech_part_information(tagged[i][1])[0],return_speech_part_information(tagged[i][1])[1]))





def example_text():
    l = []
    for line in open("example.txt"):
        for word in line.split():
            l.append(word.lower())
            return l

#print (chunking(example_text()))
