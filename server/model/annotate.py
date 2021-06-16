from typing import Union, BinaryIO

import joblib
import numpy as np
from sklearn.linear_model import SGDClassifier

from model.label_spans import label_spans
from model.tokenize import Tokenizer
from model.vectorize import Vectorizer


class Annotator:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.model = SGDClassifier()
        self.vectorizer = Vectorizer()

    def train(self, texts, annotation_sets):
        # Turn texts + annotations into (sequences of) tokens + labels
        token_sequences, span_sequences, label_sequences = [], [], []
        for text, annotation_set in zip(texts, annotation_sets):
            tokens, spans = self.tokenizer.get_tokens_and_spans(text)
            token_sequences.append(tokens)
            span_sequences.append(spans)
            label_sequences.append(label_spans(spans, annotation_set))

        # Turn token sequences into flat array of feature vectors
        x = self.vectorizer.fit_transform(token_sequences)

        # Flatten label sequences
        y = np.array(
            [label for sequence in label_sequences for label in sequence]
        )

        # Train model
        self.model.fit(x, y)

    def annotate(self, text: str):
        """Create annotations for a given text
        """
        raise NotImplementedError

    def save(self, file: Union[str, BinaryIO]):
        """Save annotator to file (either path-string or file-object).
        """
        joblib.dump(self, file)

    @staticmethod
    def load(file: Union[str, BinaryIO]):
        """Load annotator from file
        """
        return joblib.load(file)
