
from nltk.corpus import stopwords, wordnet
from nltk import FreqDist,sent_tokenize

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
        return['out of range','ount of range']

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














