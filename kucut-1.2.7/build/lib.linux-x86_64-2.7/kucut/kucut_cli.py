#! /usr/bin/python
#-*- coding:utf-8 -*-

from wordcut import *
import os.path

def cutfile():
    usage = 'usage: %prog [options] inputfile'
    opt_parser = optparse.OptionParser(usage)
    opt_parser.add_option('-d','', dest='database_file',default='',
                          help = 'manually define database for training (default is corpus.db)',
                          metavar='FILE')
    opt_parser.add_option('','--no_heuristic',action='store_true',dest='NO_HEURISTIC',
                          default=False,
                          help='do not use heuristic method (Maximum Matching) for pruning invalid patterns (only available with --no_stat option)')
    opt_parser.add_option('','--skip',action = 'store_true', dest='SKIP',
                          default = False,help='skip ambiguity results (only available with --no_stat option)')
    opt_parser.add_option('','--all',action = 'store_true', dest='GET_ALL',
                          default = False,help='take all ambiguity results (only available with --no_stat option)') 
    opt_parser.add_option('','--input',dest='input_dir',default='',metavar='DIR',
                          help = 'define directory of input files')
    opt_parser.add_option('','--output',dest='output_dir',default='',metavar='DIR',
                          help = 'define directory of output files')
    opt_parser.add_option('-c','',action = 'store_true', dest= 'DO_STDOUT',
                          default = False, help = 'force output to std_out (not avalible in list mode)')
    opt_parser.add_option('-q','--quiet',action = 'store_true', dest= 'DO_QUIET', 
                          default = True, help = 'quiet mode')
    opt_parser.add_option('-v','--verbose',action = 'store_false', dest= 'DO_QUIET', 
                          default = True, help = 'verbose mode')
    opt_parser.add_option('-l','--list',action = 'store_true', dest='DO_LIST',
                              default = False, help = 'read input from list filename')
    opt_parser.add_option('--local_bias',help='[0.0 - 1.0] (for advance user)',metavar='FLOAT',
                              dest='L_BIAS', default = 0.5)
    opt_parser.add_option('--global_bias',help='[0.0 - 1.0] (for advance user)',metavar='FLOAT',
                              dest='G_BIAS', default = 0.5)
    opt_parser.add_option('--no_stat',action = 'store_true', dest='NO_STAT',
                          default = False, help='do not use any statistic from corpus (-d option '
                          'will be ignored) and it will reduce processing time.')
    opt_parser.add_option('--no_local',action = 'store_true', dest='NO_LOCAL',
                              default=False,help='do not use local statistic from input document (for reducing memory usage)')
    opt_parser.add_option('','--line',dest='blank',metavar='"STRING"',
                          help = 'let result of cutting remain original space and substitute the space with "STRING"')
    opt_parser.add_option('','--mode',dest='cutmode',default='word',metavar='MODE',
                          help = 'select segmenation mode [word, morpheme, syllable] (default is word)')
    opt_parser.add_option('--timer',action = 'store_true', dest='DO_TIMER',
                              default=False,help='show starting timer and ending time')
    opt_parser.add_option('','--debug',action = 'store_true', dest= 'DO_DEBUG', 
                          default = False, help = 'generate debug file (inputfile.debug and inputfile.mi)')     
    opt_parser.add_option('','--extend',dest='extend',metavar='"FILES"', default = None,
                          help = 'append extended and user-defined dictionary;'
                          ' The kucut provides two extended dictionary; there are person name and country name'
                          ' that represented by PERSON and COUNTRY respectively. For user-defined,'
                          ' the format is one word per line'
                          ' and if you have more than one file then you must seperate it by colon.'
                          ' For example, "PERSON:COUNTRY:/some/where/dict.txt"'
                          )
    opt_parser.add_option('','--xml',dest='xml',metavar='TAG[,TAG,...]', default = None,
                            help = 'To use XML file as input, the tag backeting the text that want to be segmented must' 
                            'be given')
    
    (options,args) = opt_parser.parse_args()

    
    if options.DO_TIMER:
        print 'start:', time.ctime()

    if len(args) != 1:
        opt_parser.error('no input file')

    #HOME = ''
    #if 'WORDCUT_HOME' not in os.environ:
    #   print 'Warning: you do not define WORDCUT_HOME, Current directory will be used instead.'
    #else:
    #   HOME = os.environ['WORDCUT_HOME']



    lexicon_file = os.path.join(os.path.dirname(__file__), os.path.join("dict", "lexicon.txt"))
    syllable_file = os.path.join(os.path.dirname(__file__), os.path.join("dict", "syllable.txt"))
    prohibit_file = os.path.join(os.path.dirname(__file__), os.path.join("dict", "prohibit.txt"))
    
    #lexicon_file = os.path.join(HOME,'dict/lexicon.txt')
    #syllable_file = os.path.join(HOME,'dict/syllable.txt')
    #prohibit_file = os.path.join(HOME,'dict/prohibit.txt')

    if options.database_file == '':
        database_file = os.path.join(os.path.dirname(__file__),
                                     "train.skip.cut.db")
    else:
        database_file = options.database_file
    
    inputfile = args[0]
    
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
        
    #hidden_file = os.path.join(HOME,'dict/hidden.txt')
    hidden_file = os.path.join(os.path.dirname(__file__), os.path.join("dict", "hidden.txt"))

    
    if not os.path.exists(hidden_file):
        print 'The file "%s" does not exist' % (hidden_file)
        sys.exit(1)

    #totalDict_file = os.path.join(HOME,'dict/totalDict.txt')
    totalDict_file = os.path.join(os.path.dirname(__file__), os.path.join("dict", "totalDict.txt"))
    if not os.path.exists(totalDict_file):
        print 'The file "%s" does not exist' % (totalDict_file)
        sys.exit(1)
        
        
    input_dir = options.input_dir
    output_dir = options.output_dir
    
    _dospace = 0
    if options.blank != None:
        _dospace = 1
    
    seg = Segmentation(inputfile, 
                       syllable = syllableDict, 
                       lexicon = lexiconDict, 
                       debug = options.DO_DEBUG,
                       quiet = options.DO_QUIET, 
                       database = database_file,
                       gw = options.G_BIAS, 
                       lw = options.L_BIAS, 
                       output_dir = output_dir, 
                       no_local = options.NO_LOCAL,
                       mode = options.cutmode,
                       blank = options.blank,
                       home = os.path.dirname(__file__), #FIXME
                       extend = options.extend)
        
    seg.loadProhibitPattern(prohibit_file)

    if options.DO_LIST:
        files = open(inputfile).readlines()
        for file in files:
            seg.input_file = file.strip()
            output = open(os.path.join(output_dir,seg.input_file)+'.cut','w')
                
            if options.DO_DEBUG:
                output3 = open(os.path.join(output_dir,seg.input_file+'.mi'),'w')
            results,ambiguous_list = seg.tokenize(open(os.path.join(input_dir,seg.input_file),'r').readlines(),
                                                  style='Normal',
                                                  space=_dospace,
                                                  no_stat=options.NO_STAT,
                                                  skip=options.SKIP,
                                                  no_heuristic=options.NO_HEURISTIC,
                                                  get_all=options.GET_ALL,
                                                  output_stream=output)
                
            
            if not options.NO_STAT:
                for result in results:
                    for t in result[1]:
                        for r in t[0]:
                            output.write(r+' ')
                        output.write('\n')
                            
                if options.DO_TIMER:
                    print 'end:', time.ctime()
                    
            output.close()
            if options.DO_DEBUG:
                output3.close()
    else:
        seg.input_file = inputfile
        output = None
        if not options.DO_STDOUT:
            output = open(os.path.join(output_dir,seg.input_file+'.cut'),'w')
        if options.DO_DEBUG:
            output3 = open(os.path.join(output_dir,seg.input_file+'.mi'),'w')
        results,ambiguous_list = seg.tokenize(open(os.path.join(input_dir,seg.input_file),'r').readlines(),
                                              style='Normal',
                                              space=_dospace,
                                              no_stat=options.NO_STAT,
                                              skip=options.SKIP,
                                              no_heuristic=options.NO_HEURISTIC,
                                              get_all=options.GET_ALL,
                                              output_stream=output)
        
        
        
        if not options.NO_STAT:     
            if not options.DO_STDOUT:
                for result in results:
                    for t in result[1]:
                        for r in t[0]:
                            output.write(r+' ')
                        output.write('\n')
            else:
                for result in results:
                    for t in result[1]:
                        for r in t[0]:
                            sys.__stdout__.write(r+' ')
                        sys.__stdout__.write('\n')
    
        if options.DO_TIMER:
            print 'end:', time.ctime()
        if not options.DO_STDOUT:
            output.close()
        if options.DO_DEBUG:
            output3.close()
        
if __name__ == '__main__':
    cutfile()

