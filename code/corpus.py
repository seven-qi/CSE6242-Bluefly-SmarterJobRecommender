import logging
from gensim import corpora, models, similarities
import sys

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
stoplist = set('for a of the and to in'.split())
inFilename = sys.argv[1]
class MyCorpus(object):
    def __iter__(self):
        for line in open(inFilename):
            # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.lower().split())



dictionary = corpora.Dictionary(line.lower().split() for line in open(inFilename))
# remove stop words and words that appear only once
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
            if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
dictionary.compactify() # remove gaps in id sequence after words that were removed
dictionary.save('/Users/sevensevens/CSE6242_Proj/data/'+inFilename.split('/')[-1]+'.dict')

corpus_mem_frd = MyCorpus()
corpus = []
for vec in corpus_mem_frd:
	corpus.append(vec)
corpora.MmCorpus.serialize('/Users/sevensevens/CSE6242_Proj/data/'+inFilename.split('/')[-1]+'_corpus.mm', corpus)


