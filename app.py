from flask import Flask, render_template, make_response , jsonify, request, url_for, json
from nltk_main import Model, Text_Statistics,click_event_processing2
from json_tests import return_speech_part_dict
from speech_part import return_speech_part_information
import json
from nltk import word_tokenize
import ast
app = Flask(__name__)



@app.route('/background_process')
def background_process():

    word = request.args.get('proglang', 0, type=str)


    syno_sets = Model().Add_Synonyms(word)
    return jsonify(result=syno_sets)

@app.route('/speech_parts')
def speech_parts():
    sent = request.args.get('proglang', 1, type=str)
    res = return_speech_part_dict(sent)
    tab = []
    for i in len(range(res)):
        s = ''
        s+= res[i]['speech_part']
        s+= res[i]['word']
        tab.append(s)




    print(sent)
    print(res)
    return jsonify(result=tab)


@app.route('/words_counting')
def word_counting():
    sent = request.args.get('proglang', 0, type=str)

    sent = Text_Statistics.split_text_to_list(sent)

    res = Text_Statistics.word_frequency_list_without_stopwords(sent,3)
    tab = []
    for i in range(len(res)):
        w = ''
        w += res[i][0]
        w += res[i][1]
        tab.append(w)




    return jsonify(result=tab)


@app.route('/send_editor_state')
def editor_state_handling():
    state = request.args.get('editor_state', 0)
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



    return jsonify(word_count = tab, speech_parts = tab2)



@app.route("/")
def index():
    return render_template('index.html')


@app.route('/click_event=')
def click_event():
    kursor_id = request.args.get('ID', 1, type=str)
    text = request.args.get('content', 1, type=str)
    res =  click_event_processing2(kursor_id, text)
    #res2 = click_sentence(kursor_id, text)
    print (text)
    print(text)
    print(kursor_id)
    return jsonify(word = res[0], sentence = res[1])



if __name__ == "__main__":
    app.run()