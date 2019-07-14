checkers = dict()
starGates = [5, 6, 7, 8, 17, 18, 19, 20] # define special gates

# getting checkers and dice from user
for i in range(0, 5):
    data = input("Enter the key and value separated by ':' => ")
    data = data.split(':')
    checkers[int(data[0])] = int(data[1])

dice1 = int(input("Enter first dice => "))
dice2 = int(input("Enter second dice => "))


def find_moves(checkers, dice1, dice2):
    i = 0
    for k1, v1 in checkers.items():  # first loop
        tmp = checkers.copy()  # copying the dict to save original
        move1 = k1 + dice1  # first move amount of key1
        result1 = find_result(tmp, k1, v1, move1)  # set rules and find result point of first key & dice

        j = i + 1  # for second loop
        while j < len(checkers.items()):  # second loop
            k2 = list(checkers)[j] # get second key from checkers
            v2 = checkers.get(k2) # get the value of the second key
            move2 = k2 + dice2 # find move amount of key2
            result2 = find_result(tmp, k2, v2, move2) # set rules and find result point of second key & dice

            result = result1+result2 # calculate result point

            if result > 0:
                print((k1, move1), (k2, move2), result)

            j += 1 # loop till the finished dictionary

        i += 1 # set second loop starter


find_moves(checkers, dice1, dice2)
