from model.load_data import load_directory


TEST_DIRECTORY = \
    'model/i2b2-data/2014_training-PHI-Gold-Set1/training-PHI-Gold-Set1'


def test_load_directory():
    texts, annotations_sets = load_directory(TEST_DIRECTORY)

    for i in (8, 2, 5, 24):
        sample_text = texts[i]
        sample_annotation_set = annotations_sets[i]

        for annotation in sample_annotation_set:
            annotated_text = sample_text[annotation['start']: annotation['end']]
            assert annotated_text == annotation['text']
