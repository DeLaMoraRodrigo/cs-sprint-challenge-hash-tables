#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    # O(len(tickets) + length)
    route = [None] * length

    cache = dict()

    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    dest = cache["NONE"]

    for i in range(length):
        route[i] = dest
        dest = cache[dest]

    return route
