from typing import Any, Dict, List
from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from typing import TextIO


Annotation = Dict[str, Any]
AnnotationSet = List[Annotation]


def load_annotation(tag: Element) -> Annotation:
    annotation = dict(tag.items())

    # Convert index values to integers
    for key in ('start', 'end'):
        annotation[key] = int(annotation[key])

    return annotation


def load_file(file: TextIO) -> (str, AnnotationSet):
    tree = ElementTree.parse(file)
    text: str = tree.find('TEXT').text
    tags: Element = tree.find('TAGS')

    annotations = []
    for tag in tags:
        annotations.append(load_annotation(tag))

    return text, annotations


def load_files(files: List[TextIO]) -> (List[str], list[AnnotationSet]):
    '''Load several files of I2B2 PHI data (in XML); return two arrays:
    (texts, annotation_sets)
    '''
    texts, annotation_sets = [], []
    for file in files:
        text, annotation_set = load_file(file)
        texts.append(text)
        annotation_sets.append(annotation_set)
    return texts, annotation_sets
