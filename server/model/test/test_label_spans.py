from model.label_spans import label_spans


TEXT = "Hi my name is John Smith"
SPANS = [(0, 2), (3, 5), (6, 10), (11, 13), (14, 18), (19, 24)]
ANNOTATION_SET_ONE = [{'TYPE': 'PATIENT', 'start': 14, 'end': 18},
                      {'TYPE': 'PATIENT', 'start': 19, 'end': 24}]
ANNOTATION_SET_TWO = [{'TYPE': 'PATIENT', 'start': 14, 'end': 24}]
OVERLAPPING_ANNOTATION_SET_ONE = [
    {'TYPE': 'PATIENT', 'start': 14, 'end': 20},
    {'TYPE': 'DOCTOR', 'start': 19, 'end': 24},
]
OVERLAPPING_ANNOTATION_SET_TWO = [
    {'TYPE': 'DOCTOR', 'start': 14, 'end': 20},
    {'TYPE': 'PATIENT', 'start': 19, 'end': 24},
]


def test_label_span_one():
    labels = label_spans(SPANS, ANNOTATION_SET_ONE)
    assert labels == [0, 0, 0, 0, 1, 1]


def test_label_span_two():
    labels = label_spans(SPANS, ANNOTATION_SET_TWO)
    assert labels == [0, 0, 0, 0, 1, 1]


def test_label_span_three():
    labels = label_spans(SPANS, OVERLAPPING_ANNOTATION_SET_ONE)
    assert labels == [0, 0, 0, 0, 1, 1]


def test_label_span_four():
    labels = label_spans(SPANS, OVERLAPPING_ANNOTATION_SET_TWO)
    assert labels == [0, 0, 0, 0, 1, 1]
