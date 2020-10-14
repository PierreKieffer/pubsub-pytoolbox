from google.cloud import pubsub_v1
from google.oauth2 import service_account

def publish(project_id, topic_id, credentials, payload): 
    """
    Méthode de publication d'un message sur un broker pub/sub
    """

    # Credentials
    credentials = service_account.Credentials.from_service_account_file(credentials)

    # Init publisher
    publisher = pubsub_v1.PublisherClient(credentials=credentials)

    # Renseignement d'un topic sur lequel publier
    topic_path = publisher.topic_path(project_id, topic_id)

    payload = payload.encode("utf-8")
    future = publisher.publish(topic_path, data=payload)

    print("Message published : ", future.result())



