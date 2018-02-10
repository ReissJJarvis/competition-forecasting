
def ResultsSort(Input, Ascending):
    # Base case. A list of zero or one elements is sorted, by definition.
    if len(Input) <= 1:
        return Input

    # Recursive case. First, divide the list into equal-sized sublists
    # consisting of the first half and second half of the list.
    # This assumes lists start at index 0.
    Split = round(len(Input)/2)
    Left = Input[:Split]
    Right = Input[Split:]

    # Recursively sort both sublists.
    Left = ResultsSort(Left, Ascending)
    Right = ResultsSort(Right, Ascending)

    # Then merge the now-sorted sublists.
    return Merge(Left, Right, Ascending)

def Merge(Left, Right, Ascending):
    Result = []

    while len(Left) > 0 and len(Right) > 0:
        if Ascending:
            if (Left[0]['rt'] >= Right[0]['rt'] and Right[0]['rt'] != 0) or (Left[0]['rt'] == 0):
                Result.append(Right[0])
                Right.pop(0)
            else:
                Result.append(Left[0])
                Left.pop(0)

        else:
            if Left[0]['rt'] >= Right[0]['rt']: #only looking at the second element of the list
                Result.append(Left[0])
                Left.pop(0)
            else:
                Result.append(Right[0])
                Right.pop(0)

    # Either left or right may have elements left; consume them.
    # (Only one of the following loops will actually be entered.)
    while len(Left) > 0:
        Result.append(Left[0])
        Left.pop(0)
    while len(Right) > 0:
        Result.append(Right[0])
        Right.pop(0)
    return Result
