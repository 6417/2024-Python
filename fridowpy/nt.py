from typing import Any

import ntcore

instance = ntcore.NetworkTableInstance.getDefault()

def publish(topic: str, val: Any) -> None:
    topic = None
    if isinstance(val, int): topic = instance.getIntTopic(topic)
    elif isinstance(val, float): topic = instance.getFloatTopic(topic)
    elif isinstance(val, str): topic = instance.getStringTopic(topic)
    else:
        raise NotImplementedError(f"nt.publish: val of type {type(val)} not implemented")
    topic.publish(val)

def subscribe(topic: str) -> ntcore.GenericSubscriber:
    assert topic in instance.getTopics(), "topic unknown"
    instance.getTopic()

