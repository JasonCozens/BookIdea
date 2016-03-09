""" Time Tracker is a study in TDD in python.

Create a time tracker that has two inputs start and stop.
When start is pressed the time of this is recorded.
When stop is pressed the time of this is recorded.
There is a query that lists the duration.

How should a class be laid out?

    Properties - This tells the user about the state.

    Queries - This tells more about the state.

    Commands - These change the state.

Step 2.

    What can be tested?

    start() will have no observable effect, unless we include open tasks in
    the list.

    start()
    history -> "(t,)"

Step 3.

    Introduce simple Mock for time.

Step 4.

    Need to think about data structure.
    At the moment the index is being used to determine whether a history
    is at a start of stop time. It is better to used the length of the
    history to determine if we are at a start time or a stop time.

    len(H) % 2 == 1 ---> Start
    len(H) % 2 == 0 ---> Stop
"""
