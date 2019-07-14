checkers = dict()

# getting checkers and dice from user
for i in range(0, 5):
    data = input("Enter the key and value separated by ':' => ")
    data = data.split(':')
    checkers[int(data[0])] = int(data[1])
    print(checkers.items())

dice1 = int(input("Enter first dice => "))
dice2 = int(input("Enter second dice => "))

starGates = [5, 6, 7, 8, 17, 18, 19, 20] # define special gates


# for find total point of tuple
# dict_c: tmp checkers, move: key+dice
def find_result(dict_c, key, value, move):
    # total: result point
    total = 0
    if move <= 24:  # moves are not bigger than 24
        if value - 1 == 1:  # detect key state, if the stone is a gate or not
            # when the stone is a gate, than detect is it special gate or not
            if key in starGates:
                total += -2
            else:
                total += -1
        dict_c.update({key: value-1})
        if move in dict_c:  # detect the move existing state
            move_val = dict_c.get(move)  # getting the move's amount
            if move_val == 1:  # detect if the value will be a gate or not
                # when the move will be a gate, than detect is it special gate or not
                if move in starGates:
                    total += 2
                else:
                    total += 1
                total += 1 # saving the stone against rival
            dict_c.update({move: move_val + 1})  # set the first dice move on tmp checkers
        else:
            dict_c.update({move: 1})  # set the first dice move on tmp checkers

        return total


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
