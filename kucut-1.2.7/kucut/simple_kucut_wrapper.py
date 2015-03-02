#-*- coding:utf-8 -*-

from wordcut import *
import os.path

class SimpleKucutWrapper:
    def __init__(self):
        lexicon_file = os.path.join(os.path.dirname(__file__), os.path.join("dict", "lexicon.txt"))
        syllable_file = os.path.join(os.path.dirname(__file__), os.path.join("dict", "syllable.txt"))
        prohibit_file = os.path.join(os.path.dirname(__file__), os.path.join("dict", "prohibit.txt"))
        

        database_file = os.path.join(os.path.dirname(__file__),
                                         "train.skip.cut.db")
        
        if not os.path.exists(lexicon_file):
            print 'The file "%s" does not exist' % (lexicon_file)
            sys.exit(1)
        lexiconDict = Dictionary(lexicon_file)

        if not os.path.exists(syllable_file):
            print 'The file "%s" does not exist' % (syllable_file)
            sys.exit(1)
        syllableDict = Dictionary(syllable_file)

        if not os.path.exists(database_file):
            print 'The file "%s" does not exist' % (database_file)
            sys.exit(1)

        if not os.path.exists(prohibit_file):
            print 'The file "%s" does not exist' % (prohibit_file)
            sys.exit(1)
            
        hidden_file = os.path.join(os.path.dirname(__file__), os.path.join("dict", "hidden.txt"))

        
        if not os.path.exists(hidden_file):
            print 'The file "%s" does not exist' % (hidden_file)
            sys.exit(1)

        totalDict_file = os.path.join(os.path.dirname(__file__), os.path.join("dict", "totalDict.txt"))
        if not os.path.exists(totalDict_file):
            print 'The file "%s" does not exist' % (totalDict_file)
            sys.exit(1)
            
            
        
        
        self.seg = Segmentation(syllable = syllableDict, 
                                lexicon = lexiconDict, 
                                debug = False,
                                quiet = True, 
                                database = database_file,
                                gw = 0.5, 
                                lw = 0.5, 
                                #output_dir = output_dir, 
                                no_local = False,
                                mode = 'word',
                                blank = "_",
                                home = os.path.dirname(__file__), #FIXME
                                extend = None)
            
        self.seg.loadProhibitPattern(prohibit_file)

    def tokenize(self, input):
        results, ambiguous_list = \
            self.seg.tokenize(map(treat_line, input),
                              style='Normal',
                              space=1,
                              no_stat=False,
                              skip=False,
                              no_heuristic=False,
                              get_all=False,
                              output_stream=None)
        return map(treat_result, results)
                    

def treat_line(w):
    return w.encode("CP874")

def treat_word(w):
    return unicode(w, "CP874")

def treat_t(t):
    return map(treat_word, t[0])

def treat_result(result):
    return map(treat_t, result[1])
