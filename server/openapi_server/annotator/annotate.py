import joblib
import numpy as np
from typing import Union, BinaryIO, List
from sklearn.linear_model import SGDClassifier
from openapi_server.annotator.label_spans import label_tokens
from openapi_server.annotator.load_data import AnnotationSet
from openapi_server.annotator.tokenize import Tokenizer
from openapi_server.annotator.vectorize import Vectorizer


class Annotator:
    def __init__(self):
        self.tokenizer = Tokenizer()
        self.model = SGDClassifier()
        self.vectorizer = Vectorizer()

    def train(self, texts: List[str], annotation_sets: List[AnnotationSet]):
        # Turn texts + annotations into (sequences of) tokens + labels
        token_sequences, span_sequences, label_sequences = [], [], []
        for text, annotation_set in zip(texts, annotation_sets):
            tokens, spans = self.tokenizer.get_tokens_and_spans(text)
            token_sequences.append(tokens)
            span_sequences.append(spans)
            label_sequences.append(label_tokens(tokens, spans, annotation_set))

        # Turn token sequences into flat array of feature vectors
        x = self.vectorizer.fit_transform(token_sequences)

        # Flatten label sequences
        y = np.array(
            [label for sequence in label_sequences for label in sequence]
        )

        # Train annotator
        self.model.fit(x, y)

    def annotate(self, texts: List[str]) -> List[AnnotationSet]:
        """Create annotations for a given text
        """
        token_sequences, span_sequences = [], []
        for text in texts:
            tokens, spans = self.tokenizer.get_tokens_and_spans(text)
            token_sequences.append(tokens)
            span_sequences.append(spans)

        # Get input vectors
        x = self.vectorizer.transform(token_sequences)

        # Get predictions
        y = self.model.predict(x)

        i = 0
        annotation_sets = []
        for tokens, spans in zip(token_sequences, span_sequences):
            annotation_set = []
            for token, span in zip(tokens, spans):
                # If the token has been marked, create an annotation for it
                if y[i] == 1:
                    start, end = span
                    annotation_set.append({
                        'text': token,
                        'start': start,
                        'end': end
                    })
                i += 1
            annotation_sets.append(annotation_set)

        return annotation_sets

    def save(self, file: Union[str, BinaryIO]):
        """Save annotator to file (either path-string or file-object).
        """
        joblib.dump(self, file)

    @staticmethod
    def load(file: Union[str, BinaryIO]):
        """Load annotator from file
        """
        return joblib.load(file)
