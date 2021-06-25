import argparse
from openapi_server.annotator.annotate import Annotator
from openapi_server.annotator.load_data import load_files


parser = argparse.ArgumentParser()
parser.add_argument('model_file', type=argparse.FileType('rb'))
parser.add_argument('test_files', nargs='+', type=argparse.FileType('r'))
args = parser.parse_args()

if __name__ == '__main__':
    print("Loading annotator...")
    annotator = Annotator.load(args.model_file)
    print("Model loaded.")

    print("Loading testing data...")
    texts, annotation_sets = load_files(args.test_files)
    print("Data loaded.")

    print("Annotating text:")
    model_annotation_sets = annotator.annotate(texts)
    for text, model_annotation_set, annotation_set \
            in zip(texts, model_annotation_sets, annotation_sets):
        print(text[:50])
        print(model_annotation_set)
        print(list(filter(
            lambda annot: annot['TYPE'] in {'DOCTOR', 'PATIENT'},
            annotation_set)))
