
def return_speech_part_information(part):
    for i in speech_parts:
        if part == i:
            return speech_parts[i]

speech_parts = {
'CC':	['coordinating conjunction','laczy dwie czesci zdania o tej samej waznosci'],
'CD':	['cardinal digit', 'liczba'],
'DT':	['determiner','znajduje sie przed rzeczownikiem'],
'EX':	['existential there (like: "there is" ... think of it like "there exists")','?'],
'FW':	['foreign word','?'],
'IN':	['preposition/subordinating conjunction','?'],
'JJ':	['adjective	(big)','przymiotnik w stopniu najnizszym'],
'JJR':	['adjective, comparative (bigger)','prymiotnik w stopniu srednim'],
'JJS':	['adjective, superlative (biggest)','przymiotnik w stopniu najwyzszym'],
'LS':	['list marker	1)','znacznik w liscie numerowanej'],
'MD':	['modal	could, will','czasownik modalny'],
'NN':	['noun, singular (desk)','rzecownik LP'],
'NNS':	['noun plural (desks)','rzeczownik LM'],
'NNP':	['proper noun, singular (Harrison)','rzeczownik wlasny LP'],
'NNPS':	['proper noun, plural (Americans)','rzeczownik wlasny LM'],
'PDT':	['predeterminer	(all the kids)','przed rzeczownikiem np half,all'],
'POS':	['possessive ending	parents','?'],
'PRP':	['personal pronoun	I, he, she','ja ona on'],
'PRP$':	['possessive pronoun my, his, hers','moj jej jego'],
'RB':	['adverb	very, silently,','przyslowek'],
'RBR':	['adverb, comparative better','przyslowek stopnia 2'],
'RBS':	['adverb, superlative best','przyslowek stopnia 3'],
'RP':	['particle	give up','funkcjonuje z innymi slowami'],
'TO':	['to go (to) the store.','do'],
'UH':	['interjection	errrrrrrrm', '?'],
'VB':	['verb, base form	take','czasownik'],
'VBD':	['verb, past tense	took','czasownik w czasie przeszlym'],
'VBG':	['verb, gerund/present participle	taking','czasownik w czasie terazniejszym'],
'VBN':	['verb, past participle	taken','czasownik w 3 formie'],
'VBP':	['verb, sing. present, non-3d	take','czasownik bez 3 formy'],
'VBZ':	['verb, 3rd person sing. present takes','czasownik w 3 osobie'],
'WDT':	['wh-determiner	which','?'],
'WP':	['wh-pronoun	who, what','?'],
'WP$':	['possessive wh-pronoun	whose','?'],
'.':	['.','?'],
',':	[',','?'],
'!':	['!','?'],
':':	['!','?'],

'WRB':	['wh-abverb	where, when','?'],


}


#print(return_speech_part_information('WDT'))