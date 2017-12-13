class Action(object):

    def __init__(self, action, is_critical, priority, occurrence_counter):
        self.action = action
        self.is_critical = is_critical
        self.priority = priority
        self.occurrence_counter = occurrence_counter
        self.occurrence_index = -1

    def __lt__(self, other):
        return self.priority < other.priority

    def get_occurence_index(self):
        if self.occurrence_index < 0:
            self.occurrence_index = next(self.occurrence_counter)

        return self.occurrence_index

    def get_next_occurrence_index(self):
        try:
            return next(self.occurrence_counter)
        except StopIteration:
            self.occurrence_index = -1
