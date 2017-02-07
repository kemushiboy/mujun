#coding:utf-8
import wn
import sys

def abstract_word(lemma):
    result = []
    for word in wn.getWords(lemma):
        for sense in wn.getSenses(word):
            #if sense.src != 'hand': continue
            for synlink in wn.getSynLinks(sense, 'hype'):
                abst_sense = wn.getSense(synlink.synset2)
                if abst_sense and word.wordid != abst_sense.wordid:
                    for abst_synlink in wn.getSynLinks(abst_sense, 'hypo'):
                        abst_sense2 = wn.getSense(abst_synlink.synset2)
                        if abst_sense2 and word.wordid != abst_sense2.wordid:
                            result.append(wn.getWord(abst_sense2.wordid).lemma)
    if len(result) == 0:
        print "len(result) = 0"
    return result

def print_abst_word(word):
    for abst_word in abstract_word(lemma=word):
        print '-', abst_word

if __name__ == "__main__":
    lemma = unicode(sys.argv[1],'utf-8')
    print lemma
    print_abst_word(lemma)
