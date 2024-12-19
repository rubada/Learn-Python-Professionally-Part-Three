
def subtract(*args):
    # "num" should be equal to the first number in args
    num = args[0]
    # Starting the range with 1 to exclude the first number in args
    for i in range(1, len(args)):
        num = num - args[i]
    return num
