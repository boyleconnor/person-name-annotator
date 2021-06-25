import argparse
from openapi_server.annotator.annotate import Annotator
from openapi_server.annotator.load_data import load_files


parser = argparse.ArgumentParser()
parser.add_argument('model_file', type=argparse.FileType('wb'))
parser.add_argument('data_files', nargs='+', type=argparse.FileType('r'))
args = parser.parse_args()


if __name__ == '__main__':
    print("Loading training data...")
    texts, annotation_sets = load_files(args.data_files)
    print("Data loaded.")
    annotator = Annotator()
    print("Training annotator...")
    annotator.train(texts, annotation_sets)
    print("Model trained.")
    print("Saving annotator...")
    annotator.save(args.model_file)
    print("Model saved. Exiting.")
