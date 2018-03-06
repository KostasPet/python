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
    return ResultList

results = ResultsToArray()

def MoneyMovement ():
    Array = ResultsToArray()
    money = 36
    mainBet = 1
    bet = mainBet
    profit  = []
    count = 0
    cunt = []
    bets  = 0
    minus = 0
    lost = 0
    
    
    for i in Array:
        if i[0] == 1.66 or i[0] == 2.21:
            bets += 1
            if i[1] == 0:
                lost += bet
                minus+=1
                if i[0] == 1.66:
                    money = money - bet
                    bet*=2.5
                if i[0] == 2.21:
                    money = money - bet
                    bet*=1.5
                if minus > 2:
                    print bet+lost
                    print minus
            if i[1] == 1:
                lost = 0
                minus = 0
                money = money + (i[0]*bet - bet)
                bet = mainBet

        cunt.append(count)
        count += 1
        profit.append(money)
    print bets
    plt.plot(cunt, profit)
    plt.ylabel('Euros')
    plt.xlabel('Bets')
    plt.show()

def check(kof):
    global results
    money = 50
    main = 1
    bet = main
    for i in results :
        if str(round(i[0],2)) == str(kof):
            if i[1] == 0:
                money = money - bet;
                if money < 0:
                    return (0,0)
                bet*=2
            if i[1] == 1:
                money = money + (i[0]*bet - bet)
                bet = main
    if money > 100 or kof == 1.51:
        print kof
        print money
        print " "
    return (money,kof)

def BestProfit ():
    profit = -100
    minkof = 0
    allinfo = []
    allprofits = []
    allkofs = []
    kof = 1.00
    
    while kof < 100.00 :
        
        info = check(kof)
        
        if profit < info[0]:
            profit = info[0]
            minkof = info[1]
        allinfo.append(info)
        kof+= 0.01

    for i in allinfo :
        allprofits.append(allinfo[0])
        allkofs.append(allinfo[1])
    
    plt.plot(allkofs, allprofits)
    plt.ylabel('some numbers')
    plt.show()
    print profit
    print minkof
selection()
