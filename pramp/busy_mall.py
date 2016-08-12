"""
The mall management is trying to figure out what was the busiest moment in the mall in the last year.
You are given data from the door detectors: each data entry includes a timestamp (seconds in Unix Epoch format),
an amount of people and whether they entered or exited.

Example of a data entry:
{ time: 1440084737,  count: 4,  type: "enter" }

Find what was the busiest period in the mall on the last year. Return an array with two Epoch timestamps
representing the beginning and end of that period. You may assume that the data your are given is accurate
and that each second with entries or exits is recorded. Implement the most efficient solution possible and
analyze its time and space complexity.
"""

def find_busy(arr):
    """ find the second where the mall has the most people in it """

    # sort array first by ascending time, and then by type (exit first)
    # sort is O(n log n)
    sorted(arr, key=lambda x: (x[0], -x[2]))

    # initialize maximum and current population variables, and timestamp of max people
    max_pop = 0
    curr_pop = max_pop
    peak_time = None

    # iterate over array, incr curr_pop if entering, decr curr_pop if exiting
    # account for exits first, otherwise net gain of enters alone will spike population
    # iterating over array is O(n)
    for i, timeslot in enumerate(arr):

        if arr[i][2] == "exit":
            curr_pop -= arr[i][1]
        else:
            curr_pop += arr[i][1]

        if curr_pop > max_pop:
            max_pop = curr_pop
            peak_time = arr[i][0]

    return [peak_time, peak_time + 1]

    # Runtime is O(n log n)
    # Space is O(1), no additional space except for 3 variables