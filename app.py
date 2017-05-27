from flask import Flask, render_template, make_response , jsonify, request, url_for, json
from nltk_main import Model, Text_Statistics,click_event_processing2, return_speech_parts_and_count,return_speech_part_dict, return_speech_parts
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
    res =  return_speech_parts_and_count(state)



    return jsonify(word_count = res[0], speech_parts = res[1])



@app.route("/")
def index():
    return render_template('index.html')


@app.route('/click_event=')
def click_event():
    kursor_id = request.args.get('ID', 1, type=str)
    text = request.args.get('content', 1, type=str)
    res =  click_event_processing2(kursor_id, text)
    word = Model().Add_Synonyms(res[0])
    speech_part = return_speech_parts(res[1])
    return jsonify(synonims = word, speech_parts = speech_part)



if __name__ == "__main__":
    app.run()