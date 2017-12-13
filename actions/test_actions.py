from eventmanager.action_decorator import action_handler
from eventmanager.occurrence_generators import specific_events


@action_handler(specific_events(10), priority=3)
def print_10th_event(event):
    print "Concrete: This is low priority 10th event!"


@action_handler(specific_events(10), priority=1, is_critical=True)
def print_another_10th_event(event):
    print "Concrete: This is high priority 10th event!"


@action_handler(specific_events(3, 7), priority=2)
def print_3rd_and_7nd_event(event):
    print "Concrete: This is 3 or 7 event!"
