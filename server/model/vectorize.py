from typing import List
from sklearn.feature_extraction import DictVectorizer
from model.label_spans import Tokens


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
        self.vectorizer = DictVectorizer(sparse=True)

    def transform(self, sequences: List[Tokens]):
        feature_dicts = extract_features_from_sequences(sequences)
        return self.vectorizer.transform(feature_dicts)

    def fit_transform(self, sequences: List[Tokens]):
        feature_dicts = extract_features_from_sequences(sequences)
        return self.vectorizer.fit_transform(feature_dicts)
