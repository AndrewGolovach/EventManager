from event_manager.action_decorator import action_handler
from event_manager.occurrence_generators import specific_events


@action_handler(specific_events(10))
def print_10nd_event(event):
    print "Concrete: This is 10 event!"


@action_handler(specific_events(3, 7))
def print_3rd_and_7nd_event(event):
    print "Concrete: This is 3 or 7 event!"
