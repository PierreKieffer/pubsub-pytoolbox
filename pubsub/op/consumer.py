from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
from google.oauth2 import service_account


def callback(message):
    """
    Envoi un accusé reception au broker pub/sub à la reception du message
    """

    print("Received message: {}".format(message))
    message.ack()

def consume(project_id, subscription_id, credentials) : 
    """
    Méthode de subscription en stream sur un broker pub/sub
    """

    # Credentials 
    credentials = service_account.Credentials.from_service_account_file(credentials)

    # Init du client subscriber 
    subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

    # Renseignement d'un abonnement sur lequel écouter
    subscription_path = subscriber.subscription_path(project_id, subscription_id)
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    
    print("Listening for messages on {}..\n".format(subscription_path))

    with subscriber:
        try:
            streaming_pull_future.result()
        except TimeoutError:
            streaming_pull_future.cancel()





