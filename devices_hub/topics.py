from devices_hub.mqtt.topics import Topic
from devices_hub.subscribers import SonoffControlSubscriber

topics = [
    Topic('sonoff/switch', SonoffControlSubscriber.as_subscriber()),
]