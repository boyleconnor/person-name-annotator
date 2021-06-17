import connexion
from openapi_server.annotator.annotate import Annotator
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.text_person_name_annotation_request import TextPersonNameAnnotationRequest  # noqa: E501
from openapi_server.models.text_person_name_annotation import TextPersonNameAnnotation  # noqa: E501
from openapi_server.models.text_person_name_annotation_response import TextPersonNameAnnotationResponse  # noqa: E501


annotator: Annotator = Annotator.load(
    'openapi_server/annotator/cached/annotator_model.joblib')


def create_text_person_name_annotations():  # noqa: E501
    """Annotate person names in a clinical note

    Return the person name annotations found in a clinical note # noqa: E501

    :rtype: TextPersonNameAnnotationResponse
    """
    res = None
    status = None
    if connexion.request.is_json:
        try:
            annotation_request = TextPersonNameAnnotationRequest.from_dict(connexion.request.get_json())  # noqa: E501
            note = annotation_request.note  # noqa: E501
            annotation_set, = annotator.annotate([note.text])
            annotations = [TextPersonNameAnnotation(
                start=annotation['start'],
                length=annotation['end'] - annotation['start'],
                text=annotation['text'],
                confidence=95.0
            ) for annotation in annotation_set]

            res = TextPersonNameAnnotationResponse(annotations)
            status = 200
        except Exception as error:
            status = 500
            res = Error("Internal error", status, str(error))
    return res, status
