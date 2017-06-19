
from nltk.corpus import stopwords, wordnet
from nltk import FreqDist,sent_tokenize, word_tokenize
import json
from speech_part import return_speech_part_information
from tokenize_training import training

class Text_Statistics:
    # metoda przyjmujaca tekst i liczbe slow do wyswietlenia i
    #  zwracajaca najpopularniejsze slowa i ich licznosc
    def word_frequency_list(text, number):
        # wyswietla f najpopularniejszych slow w tekscie
        res = []
        # zbior angielskich stopwords - slow ktore nie maja znaczenia przy analizie jeszyka
        stop_words = set(stopwords.words("english"))
        for w in text:
            if w not in stop_words:
                res.append(w)

        f =  FreqDist(res)
        return f.most_common(number)

    # metoda zwracajaca najpopularniejsze slowa z wylaczeniem tych z listy stopwords#
    def word_frequency_list_without_stopwords(text, number):
        #wyswietla f najpopularniejszych slow w tekscie

        res = []

        for w in text:

            res.append(w)

        f =  FreqDist(res)
        return f.most_common(number)

    # wyswietla wyrazy z ciagiem znakow podanym w characters
    def search_words_with_characters(text, characters):
        return [w for w in set(text) if characters in w]

    def sent_tokenize(text):
        return sent_tokenize(text)

class Model:
    def __init__(self):

        self.syn_list = []

    # metoda przyjmuje slowo i zwraca jego  synonimy
    def Add_Synonyms(self, word):


        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                self.syn_list.append(l.name())

        self.syn_list =  list(set(self.syn_list))

        return self.syn_list





# funkcja odpowiadajaca za znalezienie kliknietego slowa i zdania w akapicie
# przyjmujaca jako cursor_position pozycje kursora w edytorze oraz tekst (akapit)
#i zwracajaca klikniete slowo i klikniete zdanie
def click_event_processing2(cursor_position, text):
    cursor_position = int(cursor_position)
    text = str(text)
    l = text.split()
    if cursor_position >= len(text):
        return['','']
    #jesli akapit jest pusty zwraca klikniete slowo i zdanie jako empty
    elif len(text)==0:
        return['empty','empty']
    else:
        word_counter = 0
        # length_of_line_to_clicked_word to zmienna zwiekszana do czasu
        # az nie bedzie rowna lub wieksza od id
        length_of_line_to_clicked_word = 0
        while length_of_line_to_clicked_word <= cursor_position:
            length_of_line_to_clicked_word += len(l[word_counter])+1
            word_counter += 1
        # uzycie wbudowanej w nltk funkcji dzielenia lancucha znakow na zdania
        sentences = sent_tokenize(text)
        list_of_words_in_sentences = []
        for word in sentences:
            li = word.split()
            list_of_words_in_sentences.append(li)
        counter = 0
        j = 0
        #petla dodajaca kolejne wyrazy do dopoki
        # counter nie bedzie rownal sie  kliknietemu slowu
        while counter <= word_counter-1:
            counter += len(list_of_words_in_sentences[j])
            j+=1
        # zwrocenie kliknietego slowa i zdania
        return [l[word_counter-1], sentences[j-1]]


# funkcja zwracajaca czesci mowy danego zdania
# przyjmujaca jako argument zdanie i zwracajaca liste slownikow  {slowo: czesc mowy}
def return_speech_part_dict(sent):
    dict_list = []
    c = training(sent)
    if c is not None:
        for i in range(len(c)):
            dict2 = {}
            a1 = str(c[i][0])
            a2 = str(c[i][1])
            a3 = return_speech_part_information(a2)
            dict2['word'] = a1
            dict2['speech_part'] = a3[0]
            dict_list.append(dict2)
        return(dict_list)
    else:
        return(' ')





# funkcja zwracajaca czesci mowy
def return_speech_parts_and_count(state):
    c = json.loads(state)
    list_of_lines = []
    text = ''
    # petla przetwarzajaca wyslany stan edytora
    # na liste akapitow
    for line in range(len(c['blocks'])):
        list_of_lines.append([c['blocks'][line]['text']])
        text += ' ' + c['blocks'][line]['text']
    speech_parts = return_speech_part_dict(text)

    tab2 = []
    # instrukcja warunkowa pozwalajaca uniknac bledu, gdy w edytorze jest
    # wpisany tylko jeden znak
    if len(speech_parts) == 1 and speech_parts[0] == ' ':
        return[' ',' ']
    else:

        for i in range(len(speech_parts)):
            # tworzenie string wyswietlanego w edytorze
            # jako slowo : czesc mowy
            s = ''
            s += str(speech_parts[i]['word'])
            s += ':   '
            s += str(speech_parts[i]['speech_part'])
            tab2.append(s)

        # czesc odopwiadajaca za czesci zdania w danym akapicie
        text = word_tokenize(text)
        word_count = Text_Statistics.word_frequency_list_without_stopwords(text,10)
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


# funkcja przyjmujaca lancuch znakow i zwracajaca czesci mowy
def return_speech_parts(text):
    if len(text)!= 0:
        speech_parts = return_speech_part_dict(text)
        tab2 = []
        for i in range(len(speech_parts)):
            s = ''
            s += str(speech_parts[i]['word'])
            s += ':   '
            s += str(speech_parts[i]['speech_part'])
            tab2.append(s)
        return tab2
    else:
        return ' '










