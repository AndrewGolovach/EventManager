class Action(object):

    def __init__(self, action, is_critical, priority, occurrence_counter):
        self.action = action
        self.is_critical = is_critical
        self.priority = priority
        self.occurrence_counter = occurrence_counter

