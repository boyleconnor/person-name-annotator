from typing import List
from scipy.sparse import hstack
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from openapi_server.annotator.label_spans import Tokens


DEFAULT_N_RANGE = (1, 3)


def extract_features_from_sequence(sequence: Tokens) -> List[dict]:
    """Given a sequence of tokens, return a sequence (of the same length) of
    feature dictionaries, one representing each token.
    """
    feature_dicts = []
    for i in range(len(sequence)):
        token = sequence[i]
        feature_dict = {
            'token_lower': token.lower(),
            'capitalized': len(token) and token[0].isupper(),
            'all_caps': token.isupper(),
            'contains_whitespace': any(char.isspace() for char in token),
            'next': '' if i+1 >= len(sequence) else sequence[i+1],
            'next_next': '' if i+2 >= len(sequence) else sequence[i+2],
            'prev': '' if i-1 < 0 else sequence[i-1],
            'prev_prev': '' if i-2 < 0 else sequence[i-2]
        }
        feature_dicts.append(feature_dict)
    return feature_dicts


def flatten(token_sequences: List[Tokens]):
    return [token for sequence in token_sequences for token in sequence]


def extract_features_from_sequences(
        sequences: List[Tokens]) -> List[dict]:
    """Given list of token sequences, turn tokens into feature dicts,
    flatten list.
    """
    feature_dict_sequences = [extract_features_from_sequence(sequence)
                              for sequence in sequences]
    return [feature_dict for sequence in feature_dict_sequences for
            feature_dict in sequence]


class Vectorizer:
    def __init__(self):
        self.feature_vectorizer = DictVectorizer()
        self.ngram_vectorizer = CountVectorizer(analyzer='char',
                                                ngram_range=DEFAULT_N_RANGE)

    def transform(self, sequences: List[Tokens]):
        feature_dicts = extract_features_from_sequences(sequences)
        feature_vectors = self.feature_vectorizer.transform(feature_dicts)
        ngram_vectors = self.ngram_vectorizer.transform(flatten(sequences))
        return hstack([feature_vectors, ngram_vectors])

    def fit_transform(self, sequences: List[Tokens]):
        feature_dicts = extract_features_from_sequences(sequences)
        feature_vectors = self.feature_vectorizer.fit_transform(feature_dicts)
        ngram_vectors = self.ngram_vectorizer.fit_transform(flatten(sequences))
        return hstack([feature_vectors, ngram_vectors])
