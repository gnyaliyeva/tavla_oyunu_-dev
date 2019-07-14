checkers = dict()
starGates = [5, 6, 7, 8, 17, 18, 19, 20] # define special gates

# getting checkers and dice from user
for i in range(0, 5):
    data = input("Enter the key and value separated by ':' => ")
    data = data.split(':')
    checkers[int(data[0])] = int(data[1])

dice1 = int(input("Enter first dice => "))
dice2 = int(input("Enter second dice => "))
