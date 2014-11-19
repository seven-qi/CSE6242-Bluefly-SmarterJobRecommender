import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


from gensim import corpora, models, similarities

corpus = [[(0, 1.0), (1, 1.0), (2, 1.0)],
          [(2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0), (8, 1.0)],
          [(1, 1.0), (3, 1.0), (4, 1.0), (7, 1.0)],
          [(0, 1.0), (4, 2.0), (7, 1.0)],
          [(3, 1.0), (5, 1.0), (6, 1.0)],
          [(9, 1.0)],
          [(9, 1.0), (10, 1.0)],
          [(9, 1.0), (10, 1.0), (11, 1.0)],
          [(8, 1.0), (10, 1.0), (11, 1.0)]]

documents = ["Human machine interface for lab abc computer applications",
             "A survey of user opinion of computer system response time",
             "The EPS user interface management system",
             "System and human system engineering testing of EPS",
             "Relation of user perceived response time to error measurement",
             "The generation of random binary unordered trees",
             "The intersection graph of paths in trees",
             "Graph minors IV Widths of trees and well quasi ordering",
             "Graph minors A survey"]

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]
# remove words that appear only once
all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once]
         for text in texts]

dictionary = corpora.Dictionary(texts)
dictionary.save('/tmp/deerwester.dict') # store the dictionary, for future reference

print(dictionary.token2id)

new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_vec)  # the word "interaction" does not appear in the dictionary and is ignored

corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus) # store to disk, for later use
print(corpus)

class MyCorpus(object):
    def __iter__(self):
        for line in open('/Users/sevensevens/Google Drive/GT/Academics/Fall2014/CSE 6242/Proj/mycorpus.txt'):
            # assume there's one document per line, tokens separated by whitespace
            yield dictionary.doc2bow(line.lower().split())

corpus_memory_friendly = MyCorpus() # doesn't load the corpus into memory!
print(corpus_memory_friendly)

for vector in corpus_memory_friendly: # load one vector into memory at a time
    print(vector)

# collect statistics about all tokens
dictionary = corpora.Dictionary(line.lower().split() for line in open('/Users/sevensevens/Google Drive/GT/Academics/Fall2014/CSE 6242/Proj/mycorpus.txt'))
# remove stop words and words that appear only once
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
            if stopword in dictionary.token2id]
once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
dictionary.filter_tokens(stop_ids + once_ids) # remove stop words and words that appear only once
dictionary.compactify() # remove gaps in id sequence after words that were removed
print(dictionary)

from gensim import corpora
# create a toy corpus of 2 documents, as a plain Python list
corpus = [[(1, 0.5)], []]  # make one document empty, for the heck of it

corpora.MmCorpus.serialize('/tmp/corpus.mm', corpus)
corpora.SvmLightCorpus.serialize('/tmp/corpus.svmlight', corpus)
corpora.BleiCorpus.serialize('/tmp/corpus.lda-c', corpus)
corpora.LowCorpus.serialize('/tmp/corpus.low', corpus)

corpus = corpora.MmCorpus('/tmp/corpus.mm')
print(list(corpus))
corpora.BleiCorpus.serialize('/tmp/corpus.lda-c', corpus)

from gensim import corpora, models, similarities
dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
corpus = corpora.MmCorpus('/tmp/deerwester.mm')
print(corpus)

from gensim import corpora, models, similarities
dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
corpus = corpora.MmCorpus('/tmp/deerwester.mm')
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]














