from eventmanager.event_manager import EventManager

path = "actions"

manager = EventManager(path)
for i in range(11):
    print i
    manager.notify(object)
