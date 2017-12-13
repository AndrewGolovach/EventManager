def once():
    yield 0


def every_event():
    event_number = 0
    while True:
        yield event_number
        event_number += 1


def specific_events(*event_numbers):
    for ind in sorted(event_numbers):
        yield ind


def regularly(start_event_number, period, number_of_repeats = None):
    event_number = start_event_number
    if number_of_repeats is None:
        while True:
            yield event_number
            event_number += period
    else:
        last_event_number = start_event_number + period * (number_of_repeats - 1)
        for ind in xrange(start_event_number, last_event_number, period):
            yield ind
