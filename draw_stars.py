
def drawstars(arr):
    for x in arr:
        print "*" * x
nums = [4,8,3,1,9,4,2]
drawstars(nums)

#next function
def drawstars2(arr):
    for x in arr:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print letter * length
x = [2, 10, 1, "Grok", "$@*#", 10, "Longer String"]
drawstars2(x)