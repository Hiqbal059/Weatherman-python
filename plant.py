# pylint: disable=missing-function-docstring
# Finds out the days after that no plant will die.
def poison_plant(array):
    index = []
    temp = []
    count = -1
    while array != temp:
        for i in range(len(array)-1):
            if array[i] < array[i+1]:
                index.append(array[i+1])
        count += 1
        temp = array
        array = [x for x in array if x not in index]
    return count
NUMBER_OF_PLANTS = int(input().strip())
PLANTS_POISON = list(map(int, input().rstrip().split()))
RESULT = poison_plant(PLANTS_POISON)
print("No plant will die after {}".format(RESULT))
