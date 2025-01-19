n = input()

while n != "0":

    donations = [int(x) for x in input().split()]
    donationFrequency = {x: 0 for x in donations}

    for x in donations:
        donationFrequency[x] += 1

    maxValue = 0
    maxItem = 0

    for key, value in donationFrequency.items():
        if value > maxValue:
            maxValue = value
            maxItem = key
        elif value == maxValue:
            if key < maxItem:
                maxItem = key

    """
    We should try to learn how to write the following code:
    
    maxItem = min(donationFrequency.keys(), key=lambda k: (-donationFrequency[k], k))
    """

    print(maxItem)
    n = input()
