import matplotlib.pyplot as plt

def selection():
    print "******"
    print "1 MoneyMovement"
    print "2 Best Profit"
    app = input("Enter function number : ")
    if app == 1:
        MoneyMovement()
    if app == 2:
        BestProfit()
    if app == 3:
        return 0
    selection()
    

def ResultsToArray():
    file = open('results.txt', 'r') 
    content = file.read()
    file.close()
    ResultList = []
    elements = content.split('||')
    count = 0
    for i in elements :
        count += 1
        element = i.split('|')
        if element[0] != '':
            if element[1] == 'lost':
                element[1] = 0
            if element[1] == 'won':
                element[1] = 1
            element[0] = float(element[0])
            ResultList.append(element)
    print count
    return ResultList

def MoneyMovement ():
    Array = ResultsToArray()
    money = 10
    bet = 1
    profit  = []
    count = 0
    cunt = []
    bets  = 0
    
    for i in Array:
        #if i[0] >= minBet and i[0] <= maxBet:
        if i[0] == 1.44 or i[0] == 1.51 or i[0] == 1.66:
            bets += 1
            if i[1] == 0:
                money = money - bet;
            if i[1] == 1:
                money = money + (i[0]*bet - bet)
        cunt.append(count)
        count += 1
        profit.append(money)
    print bets
    print money
    plt.plot(cunt, profit)
    plt.ylabel('Euros')
    plt.xlabel('Bets')
    plt.show()
    MoneyMovement()
    
        

def generateKof():
    array = []
    x = 0.1
    while x < 2 :
        a = 1.0
        b = a + x
        while b <= 3 :
            array.append([a,b])
            a +=0.01
            b +=0.01
        x += 0.01
    return array

def check(minBet, maxBet,Array):
    minBet = round(minBet,2)
    maxBet = round(maxBet,2)
    money = 10
    bet = 1
    for i in Array :
        if money < 0 :
                return (0,0,0)
        if i[0] > minBet and i[0] < maxBet:
            if i[1] == 0:
                money = money - bet;
            if i[1] == 1:
                money = money + (i[0]*bet - bet)
                
    return (money,minBet,maxBet)

def BestProfit ():
    kof = generateKof()
    results = ResultsToArray()
    profit = -100
    minkof = 0
    maxkof = 0
    allinfo = []
    allprofits = []
    allkofs = []
    for i in kof :
        info = check(i[0], i[1],results)
        if profit < info[0]:
            profit = info[0]
            minkof = info[1]
            maxkof = info[2]
        allinfo.append(info)
    count = []
    cunt = 0
    for i in allinfo :
        count.append(cunt)
        cunt+=1
        allprofits.append(i[0])
        allkofs.append(str(i[1])+"-"+str(i[2]))
    
    plt.plot(count, allprofits)
    plt.ylabel('some numbers')
    plt.show()
    print profit
    print minkof
    print maxkof
selection()
