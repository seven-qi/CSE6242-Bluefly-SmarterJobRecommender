import logging
from gensim import corpora, models, similarities
import sys

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

name = sys.argv[1]
dictionary = corpora.Dictionary.load('/Users/sevensevens/CSE6242_Proj/data/' + name + '.dict')
corpus = corpora.MmCorpus('/Users/sevensevens/CSE6242_Proj/data/' + name + '_corpus.mm')
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

corpora.MmCorpus.serialize('/Users/sevensevens/CSE6242_Proj/data/'+name+'_tfidf_corpus.mm', corpus_tfidf)


