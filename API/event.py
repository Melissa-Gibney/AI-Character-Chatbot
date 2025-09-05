subscribers = dict()

def subscribe(eventType: str, fn):
    print(f"Subscribing to {eventType}")
    if not eventType in subscribers:
        subscribers[eventType] = []
    subscribers[eventType].append(fn)

def postEvent(eventType: str, data):
    if not eventType in subscribers:
        return
    for fn in subscribers[eventType]:
        fn(data)