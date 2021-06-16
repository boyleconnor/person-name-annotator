from typing import Tuple
from nltk import TreebankWordTokenizer
from model.label_spans import Tokens, Spans


class Tokenizer:
    def __init__(self):
        self.tokenizer = TreebankWordTokenizer()

    def get_tokens_and_spans(self, text: str) -> Tuple[Tokens, Spans]:
        """Get a list of tokens & a list of labels (one for each token)
        """
        tokens = self.tokenizer.tokenize(text)
        spans = self.tokenizer.span_tokenize(text)

        return tokens, spans
