"""
Given an array V of vote decisions, return the winner of the election.
You are guaranteed to have a winner. Also, you can assume the winner have more than
floor(n/2) votes in favor.
"""
def duplicate_zeros(arr):
    """Modifies arr in place duplicating all zeros while maitining the original length."""
    zeroes = 0
    iteration = 0
    size = len(arr) - 1

    while zeroes + iteration < size:
        if arr[iteration] == 0:
            zeroes += 1
        iteration += 1

    while zeroes:
        if arr[size - zeroes] == 0 and zeroes + iteration != size:
            arr[size] = 0
            size -= 1
            zeroes -= 1
        arr[size] = arr[size - zeroes]
        size -= 1

    return arr

if __name__ == "__main__":
    print(duplicate_zeros([1,0,2,3,0,4,5,0]))
