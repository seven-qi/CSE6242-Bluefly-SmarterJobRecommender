import logging, gensim
import sys

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

name = sys.argv[1]
id2word = gensim.corpora.Dictionary.load('/Users/sevensevens/CSE6242_Proj/data/' + name + '.dict')
mm = gensim.corpora.MmCorpus('/Users/sevensevens/CSE6242_Proj/data/'+name+'_tfidf_corpus.mm')
# lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=100, update_every=1, chunksize=10000, passes=1)
lda = gensim.models.ldamodel.LdaModel(corpus=mm, id2word=id2word, num_topics=100, update_every=0, passes=20)
lda.print_topics(20)
mm_lda = lda[mm]
count = 0
for doc in mm:
	count +=1
	if count < 10:
		print doc