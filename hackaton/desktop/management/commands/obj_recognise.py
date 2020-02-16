from google.cloud import vision
from django.core.management import BaseCommand


def get_most_similar(url_or_path: str):
    client = vision.ImageAnnotatorClient()
    image = vision.types.Image()

    image.source.image_uri = url_or_path
    request = {
       'image': {
            'source': {'image_uri': url_or_path},
        },
    }

    response = client.annotate_image(request)

    return [entity.description for entity in response.web_detection.web_entities if entity.score > 0.5 and entity.description]


class Command(BaseCommand):

    def handle(self, *args, **options):
        print(get_most_similar("https://sun9-5.userapi.com/c857232/v857232182/e26bf/VRB-DMI0lGU.jpg"))
