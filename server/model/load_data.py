import os
from typing import Any
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

from py._io.capture import TextIO

Annotation = dict[str, Any]
AnnotationSet = list[Annotation]


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


def load_directory(path: str) -> (list[str], list[AnnotationSet]):
    '''Load a directory of I2B2 PHI data (in XML)
    '''
    texts, annotation_sets = [], []
    for filename in os.listdir(path):
        text, annotation_set = load_file(os.path.join(path, filename))
        texts.append(text)
        annotation_sets.append(annotation_set)
    return texts, annotation_sets
