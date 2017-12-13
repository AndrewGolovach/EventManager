import functools

from event_manager.occurrence_generators import every_event


class ActionDecorator(object):
    action_key = "<action_handler>"

    def __init__(self, occurrence_counter=every_event, is_critical=False, priority=3):
        self.occurrence_counter = occurrence_counter
        self.is_critical = is_critical
        self.priority = priority

    def __call__(self, f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            return f(*args, **kwargs)

        if ActionDecorator.action_key not in wrapped.func_dict:
            wrapped.func_dict[ActionDecorator.action_key] = self

        return wrapped

    def get_decorator_info(self):
        return self.is_critical, self.priority, self.occurrence_counter

action_handler = ActionDecorator
