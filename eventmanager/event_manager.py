from heapq import heapify, heappop, heappush

from collections import defaultdict

from eventmanager.collector import Collector
from eventmanager.error_handling import handle_error_context


class EventManager(object):
    def __init__(self, package_name):
        self.event_count = -1
        self.indexed_actions = defaultdict(list)

        actions = self._collect_actions(package_name)
        for action in actions:
            self.register_action(action)

    def notify(self, event):
        self.event_count += 1
        self._handle_event(event)

    def _collect_actions(self, package_name):
        collector = Collector(package_name)
        return collector.collect()

    def _handle_event(self, event):
        actions = self.indexed_actions[self.event_count]
        while len(actions) > 0:
            action = heappop(actions)

            with handle_error_context(re_raise=action.is_critical, log_traceback=True):
                action.action(event)

            next_index = action.occurrence_index = action.get_next_occurrence_index()
            if next_index > 0:
                heappush(self.indexed_actions[next_index], action)

    def register_action(self, action):
        index = action.get_occurence_index()
        if self.event_count > 0:
            action.occurrence_index += self.event_count
        heappush(self.indexed_actions[index], action)

    def remove_action(self, action):
        self.indexed_actions[action.occurrence_index].remove(action)
        heapify(self.indexed_actions)
