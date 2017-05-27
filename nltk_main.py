
from nltk.corpus import stopwords, wordnet
from nltk import FreqDist,sent_tokenize, word_tokenize

import json
from speech_part import return_speech_part_information
from tokenize_training import training

class Text_Statistics:

    def lexical_diversity(text):
        return len(text)/ len(set(text))

    def join_from_list_to_text(text):
        return ' '.join(text)

    def split_text_to_list(text):
        return text.split()

    def txt_to_list(text):
        l = []
        for line in text:
            for word in line.split():
                l.append(word.lower())
        return l

    def word_length_searching(text,method_number, letter_number):
        #wyszukuje slowa o danej dlugosci
        if method_number == 1:
            l = [ w for w in text if len(w)>= letter_number ]
            return l
        elif method_number == 2:
            l = [w for w in text if len(w) == letter_number]
            return l
        elif method_number == 3:
            l = [w for w in text if len(w) <= letter_number]
            return l
        else:
            return ("nieznana metoda!!!")
    #funkcja zwraczjaca najpopularniejsze slowa i ich licznosc
    def word_frequency_list(text, number):
        #wyswietla f najpopularniejszych slow w tekscie
        print(text)
        res = []
        stop_words = set(stopwords.words("english"))
        for w in text:
            if w not in stop_words:
                res.append(w)

        f =  FreqDist(res)
        return f.most_common(number)

    def word_frequency_list_without_stopwords(text, number):
        #wyswietla f najpopularniejszych slow w tekscie
        print(text)
        res = []

        for w in text:

            res.append(w)

        f =  FreqDist(res)
        return f.most_common(number)

    def search_words_with_characters(text, characters):
        #wyswietla wyrazy z ciagiem znakow podanym w characters
        return [w for w in set(text) if characters in w]

    def sent_tokenize(text):
        return sent_tokenize(text)




class Model:
    def __init__(self):

        self.syn_list = []

    def Add_Synonyms(self, word):
        """funkcja przyjmuje slowo i zwraca jego  synonimy"""

        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                self.syn_list.append(l.name())

        self.syn_list =  list(set(self.syn_list))

        return self.syn_list





#funkcja odpowiadajaca za znalezienie kliknietego slowa i zdania
def click_event_processing2(id, text):
    id = int(id)

    text = str(text)
    l = text.split()
    if id >= len(text):
        return['','']

    elif len(text)==0:
        return['empty','empty']

    else:
        word_counter = 0
        i = 0
        while i<= id:
            i += len(l[word_counter])+1
            word_counter += 1

        s = sent_tokenize(text)

        list = []
        for word in s:
            li = word.split()
            list.append(li)
        print(list)
        counter = 0
        j = 0
        while counter <= word_counter-1:
            counter+= len(list[j])
            j+=1

        return [l[word_counter-1],s[j-1]]



def return_speech_part_dict(sent):

    dict_list = []
    c = training(sent)
    for i in range(len(c)):
        dict2 = {}
        a1 = str(c[i][0])
        a2 = str(c[i][1])
        a3 = return_speech_part_information(a2)
        dict2['word'] = a1
        dict2['speech_part'] = a3[0]
        dict_list.append(dict2)
    return(dict_list)





def return_speech_parts_and_count(state):
    c = json.loads(state)
    content = []
    text = ''
    for i in range(len(c['blocks'])):
        content.append([c['blocks'][i]['text']])
        text += ' ' + c['blocks'][i]['text']
    speech_parts = return_speech_part_dict(text)
    tab2 = []
    for i in range(len(speech_parts)):

        s = ''
        s += str(speech_parts[i]['word'])
        s += ':   '
        s += str(speech_parts[i]['speech_part'])
        tab2.append(s)

    text = word_tokenize(text)
    word_count = Text_Statistics.word_frequency_list_without_stopwords(text,4)
    print (word_count)
    tab = []
    for i in range(len(word_count)):
        w = ''
        w += word_count[i][0]
        w+= ': '
        w += str(word_count[i][1])
        tab.append(w)

    res = []
    res.append(tab)
    res.append(tab2)
    return res



def return_speech_parts(text):

    speech_parts = return_speech_part_dict(text)
    tab2 = []
    for i in range(len(speech_parts)):

        s = ''
        s += str(speech_parts[i]['word'])
        s += ':   '
        s += str(speech_parts[i]['speech_part'])
        tab2.append(s)
    return tab2







