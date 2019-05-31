from models.utils import Embeddings, _Embeddings


class Word2Vec(Embeddings):
    google_news_300 = _Embeddings(name=u'word2vec-google_new-300',
                                  dimensions=300,
                                  corpus_size='100B',
                                  vocabulary_size='3M',
                                  download_path='',
                                  format='.vec',
                                  architecture='skip-gram',
                                  trained_data=[]
                                  )

    _members = (
        google_news_300,
    )