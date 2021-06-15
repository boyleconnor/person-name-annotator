import os
from model.load_data import load_file, load_files

# Use dummy data in GitHub CI environment
if os.getenv('CI'):
    TEST_DIRECTORY = 'model/dummy-data'
    FILE_INDICES = (0, 1)
else:
    TEST_DIRECTORY = \
        'model/i2b2-data/2014_training-PHI-Gold-Set1/training-PHI-Gold-Set1'
    FILE_INDICES = (8, 2, 5, 24)
TEST_FILEPATH = os.path.join(TEST_DIRECTORY, '220-01.xml')


def test_load_file():
    raise Exception(os.environ)
    with open(TEST_FILEPATH) as test_file:
        text, annotation_set = load_file(test_file)

    for annotation in annotation_set:
        annotated_text = text[annotation['start']: annotation['end']]
        assert annotated_text == annotation['text']


def test_load_files():
    paths = [os.path.join(TEST_DIRECTORY, filename) for filename in
             os.listdir(TEST_DIRECTORY)]
    files = [open(path) for path in paths]
    texts, annotations_sets = load_files(files)

    for i in FILE_INDICES:
        sample_text = texts[i]
        sample_annotation_set = annotations_sets[i]

        for annotation in sample_annotation_set:
            annotated_text = sample_text[annotation['start']: annotation['end']]
            assert annotated_text == annotation['text']
