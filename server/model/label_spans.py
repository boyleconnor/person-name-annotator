from typing import Tuple, List
from model.load_data import AnnotationSet


PERSON_TYPES = {'PATIENT', 'DOCTOR'}


Tokens = List[str]
Label = int
Labels = List[int]
Span = Tuple[int, int]
Spans = List[Span]


def label_span(span: Span, annotation_set: AnnotationSet) -> Label:
    """Return majority annotation type for a given span
    """
    start, end = span

    # Count annotated characters
    overlap = 0
    for annotation in annotation_set:
        if annotation['TYPE'] in PERSON_TYPES:
            overlap += max(
                min(end, annotation['end']) - max(start, annotation['start']),
                0
            )

    # Return 1 if most of the characters in the range are in a person
    # annotation, else 0.
    span_length = end - start
    return 0 if (span_length / 2) > overlap else 1


def label_spans(spans: Spans, annotation_set: AnnotationSet) -> Labels:
    """Take list of spans and iterable of annotations; use those annotations to
    make list of labels parallel to list of spans
    """
    return [label_span(span, annotation_set) for span in spans]
