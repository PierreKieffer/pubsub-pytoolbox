# pubsub-pytoolbox
Google Cloud Platform Pub/Sub toolbox 

## Prerequisities 
- GCP project with a Pub/Sub up & running. 
- GCP service account and the credential file `private_key.json` associated.

## Install 
```bash
pip install .
```

## Usage 
### Publisher
```python
import json
from pubsub.op import publisher

data = {"field1" : "value1", "field2" : "value2"}
event = json.dumps(data)

publisher.publish("PROJECT_ID", "TOPIC_ID", "private_key.json", event)
```

### Consumer
Start a background thread to receive messages from Pub/Sub and calls a callback with each message received.

```python
from pubsub.op import consumer

consumer.consume("PROJECT_ID", "SUBSCRIBER_ID", "private_key.json")
```

