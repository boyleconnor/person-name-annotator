from typing import Tuple
from nltk import TreebankWordTokenizer
from openapi_server.annotator.label_spans import Tokens, Spans


class Tokenizer:
    def __init__(self):
        self.tokenizer = TreebankWordTokenizer()

    def get_tokens_and_spans(self, text: str) -> Tuple[Tokens, Spans]:
        """Get a list of tokens & a list of labels (one for each token)
        """
        # Handle empty or all-whitespace notes
        if text == '' or text.isspace():
            return [''], [(0, 0)]

        # Handle non-empty notes
        tokens = self.tokenizer.tokenize(text)
        spans = self.tokenizer.span_tokenize(text)

        return tokens, spans
