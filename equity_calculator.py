import itertools
from random import randint


deck = [ 'Ah', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh' ,'Qh', 'Kh',
                'Ac', '2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc' ,'Qc', 'Kc',
                'As', '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js' ,'Qs', 'Ks',
                'Ad', '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd' ,'Qd', 'Kd']


choose_hand_a = input("Choose hand A or press rn for random: ")
choose_hand_b = input("Choose hand B or press rn for random: ")

if choose_hand_a == 'rn':
        hand_a = []
        for i in range(1,3):
            d = 52 - i
            a = randint(0,d)
            card = deck.pop(a)
            hand_a.append(card)
else:
        hand_a = []
        a = choose_hand_a[:2]
        b = choose_hand_a[2:]
        hand_a.append(a)
        hand_a.append(b)
        try:
            deck.remove(a)
            deck.remove(b)
        except ValueError:
            print("This card is already chosen. Try again")

if choose_hand_b == 'rn':
         hand_b = []
         for i in range(1,3):
            d = 50 - i
            a = randint(0,d)
            card = deck.pop(a)
            hand_b.append(card)
else:
        hand_b = []
        c = choose_hand_b[:2]
        d = choose_hand_b[2:]
        hand_b.append(c)
        hand_b.append(d)
        try:
            deck.remove(c)
            deck.remove(d)
        except ValueError:
            print("This card is already chosen. Try again")
            

def check_for_straight_flush(hand_strength):
        if 'Td'  in hand_strength and 'Jd'in hand_strength and 'Qd' in hand_strength and 'Kd' in hand_strength and 'Ad' in hand_strength:
                     points = 10010
                     return points
        elif '9d'  in hand_strength and 'Td'  in hand_strength and 'Jd' in hand_strength and 'Qd' in hand_strength and 'Kd' in hand_strength:
                     points = 10009
                     return points
        elif '8d' in hand_strength and '9d'in hand_strength  and 'Td' in hand_strength and 'Jd' in hand_strength and 'Qd' in hand_strength:
                     points = 10008
                     return points
        elif  '7d' in hand_strength and '8d' in hand_strength and '9d'  in hand_strength and 'Td'  in hand_strength and 'Jd' in hand_strength:
                     points = 10007
                     return points
        elif '6d' in hand_strength and '7d' in hand_strength and '8d' in hand_strength and '9d' in hand_strength and 'Td' in hand_strength:
                     points = 10006
                     return points
        elif '5d' in hand_strength and '6d' in hand_strength and '7d' in hand_strength and '8d' in hand_strength and '9d' in hand_strength:
                     points = 10005
                     return points
        elif  '4d' in hand_strength and  '5d' in hand_strength and '6d' in hand_strength and '7d' in hand_strength and '8d' in hand_strength:
                     points = 10004
                     return points
        elif  '3d' in hand_strength and '4d' in hand_strength and '5d' in hand_strength and '6d' in hand_strength and '7d' in hand_strength:
                     points = 10003
                     return points
        elif  '2d' in hand_strength and '3d' in hand_strength and '4d' in hand_strength and '5d' in hand_strength and '6d' in hand_strength:
                     points = 10002
                     return points
        elif  'Ad' in hand_strength and '2d' in hand_strength and '3d' in hand_strength and '4d' in hand_strength and '5d' in hand_strength:
                     points = 10001
                     return points

        elif 'Tc'  in hand_strength and 'Jc'in hand_strength and 'Qc' in hand_strength and 'Kc' in hand_strength and 'Ac' in hand_strength:
                     points = 10010
                     return points
        elif '9c'  in hand_strength and 'Tc'  in hand_strength and 'Jc' in hand_strength and 'Qc' in hand_strength and 'Kc' in hand_strength:
                     points = 10009
                     return points
        elif '8c' in hand_strength and '9c'in hand_strength  and 'Tc' in hand_strength and 'Jc' in hand_strength and 'Qc' in hand_strength:
                     points = 10008
                     return points
        elif  '7c' in hand_strength and '8c' in hand_strength and '9c'  in hand_strength and 'Tc'  in hand_strength and 'Jc' in hand_strength:
                     points = 10007
                     return points
        elif '6c' in hand_strength and '7c' in hand_strength and '8c' in hand_strength and '9c' in hand_strength and 'Tc' in hand_strength:
                     points = 10006
                     return points
        elif '5c' in hand_strength and '6c' in hand_strength and '7c' in hand_strength and '8c' in hand_strength and '9c' in hand_strength:
                     points = 10005
                     return points
        elif  '4c' in hand_strength and  '5c' in hand_strength and '6c' in hand_strength and '7c' in hand_strength and '8c' in hand_strength:
                     points = 10004
                     return points
        elif  '3c' in hand_strength and '4c' in hand_strength and '5c' in hand_strength and '6c' in hand_strength and '7c' in hand_strength:
                     points = 10003
                     return points
        elif  '2c' in hand_strength and '3c' in hand_strength and '4c' in hand_strength and '5c' in hand_strength and '6c' in hand_strength:
                     points = 10002
                     return points
        elif  'Ac' in hand_strength and '2c' in hand_strength and '3c' in hand_strength and '4c' in hand_strength and '5c' in hand_strength:
                     points = 10001
                     return points

        elif 'Ts'  in hand_strength and 'Js'in hand_strength and 'Qs' in hand_strength and 'Ks' in hand_strength and 'As' in hand_strength:
                     points = 10010
                     return points
        elif '9s'  in hand_strength and 'Ts'  in hand_strength and 'Js' in hand_strength and 'Qs' in hand_strength and 'Ks' in hand_strength:
                     points = 10009
                     return points
        elif '8s' in hand_strength and '9s'in hand_strength  and 'Ts' in hand_strength and 'Js' in hand_strength and 'Qs' in hand_strength:
                     points = 10008
                     return points
        elif  '7s' in hand_strength and '8s' in hand_strength and '9s'  in hand_strength and 'Ts'  in hand_strength and 'Js' in hand_strength:
                     points = 10007
                     return points
        elif '6s' in hand_strength and '7s' in hand_strength and '8s' in hand_strength and '9s' in hand_strength and 'Ts' in hand_strength:
                     points = 10006
                     return points
        elif '5s' in hand_strength and '6s' in hand_strength and '7s' in hand_strength and '8s' in hand_strength and '9s' in hand_strength:
                     points = 10005
                     return points
        elif  '4s' in hand_strength and  '5s' in hand_strength and '6s' in hand_strength and '7s' in hand_strength and '8s' in hand_strength:
                     points = 10004
                     return points
        elif  '3s' in hand_strength and '4s' in hand_strength and '5s' in hand_strength and '6s' in hand_strength and '7s' in hand_strength:
                     points = 10003
                     return points
        elif  '2s' in hand_strength and '3s' in hand_strength and '4s' in hand_strength and '5s' in hand_strength and '6s' in hand_strength:
                     points = 10002
                     return points
        elif  'As' in hand_strength and '2s' in hand_strength and '3s' in hand_strength and '4s' in hand_strength and '5s' in hand_strength:
                     points = 10001
                     return points

        elif 'Th'  in hand_strength and 'Jh'in hand_strength and 'Qh' in hand_strength and 'Kh' in hand_strength and 'Ah' in hand_strength:
                     points = 10010
                     return points
        elif '9h'  in hand_strength and 'Th'  in hand_strength and 'Jh' in hand_strength and 'Qh' in hand_strength and 'Kh' in hand_strength:
                     points = 10009
                     return points
        elif '8h' in hand_strength and '9h'in hand_strength  and 'Th' in hand_strength and 'Jh' in hand_strength and 'Qh' in hand_strength:
                     points = 10008
                     return points
        elif  '7h' in hand_strength and '8h' in hand_strength and '9h'  in hand_strength and 'Th'  in hand_strength and 'Jh' in hand_strength:
                     points = 10007
                     return points
        elif '6h' in hand_strength and '7h' in hand_strength and '8h' in hand_strength and '9h' in hand_strength and 'Th' in hand_strength:
                     points = 10006
                     return points
        elif '5h' in hand_strength and '6h' in hand_strength and '7h' in hand_strength and '8h' in hand_strength and '9h' in hand_strength:
                     points = 10005
                     return points
        elif  '4h' in hand_strength and  '5h' in hand_strength and '6h' in hand_strength and '7h' in hand_strength and '8h' in hand_strength:
                     points = 10004
                     return points
        elif  '3h' in hand_strength and '4h' in hand_strength and '5h' in hand_strength and '6h' in hand_strength and '7h' in hand_strength:
                     points = 10003
                     return points
        elif  '2h' in hand_strength and '3h' in hand_strength and '4h' in hand_strength and '5h' in hand_strength and '6h' in hand_strength:
                     points = 10002
                     return points
        elif  'Ah' in hand_strength and '2h' in hand_strength and '3h' in hand_strength and '4h' in hand_strength and '5h' in hand_strength:
                     points = 10001
                     return points

        else:
                     points = None
                     return points

pat = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2' ]                   

karep = { 'A' : 9950, 'K': 9900,  'Q': 9850, 'J': 9800, 'T': 9750, '9': 9700, '8': 9650,
               '7': 9600, '6':  9550, '5': 9500, '4': 9450,  '3': 9400,  '2': 9350}

highp = { 'A' : 13, 'K': 12,  'Q': 11, 'J': 10, 'T': 9, '9': 8, '8': 7,
               '7': 6, '6':  5, '5': 4, '4': 3,  '3': 2,  '2': 1 }

fhp = {'AK': 9000, 'AQ': 8995, 'AJ': 8990, 'AT': 8985, 'A9': 8980, 'A8': 8975, 'A7': 8970, 'A6': 8965,
       'A5': 8960, 'A4': 8955, 'A3': 8950, 'A2': 8945, 'KA': 8940, 'KQ': 8935, 'KJ': 8930, 'KT': 8925,
       'K9': 8920, 'K8': 8915, 'K7': 8910, 'K6': 8905, 'K5': 8900, 'K4': 8895, 'K3': 8890, 'K2': 8885,
       'QA': 8880, 'QK': 8875, 'QJ': 8870, 'QT': 8865, 'Q9': 8860, 'Q8': 8855, 'Q7': 8850, 'Q6': 8845,
       'Q5': 8840, 'Q4': 8835, 'Q3': 8830, 'Q2': 8825, 'JA': 8820, 'JK': 8815, 'JQ': 8810, 'JT': 8805,
       'J9': 8800, 'J8': 8795, 'J7': 8790, 'J6': 8785, 'J5': 8780, 'J4': 8775, 'J3': 8770, 'J2': 8765,
       'TA': 8760, 'TK': 8755, 'TQ': 8750, 'TJ': 8745, 'T9': 8740, 'T8': 8735, 'T7': 8730, 'T6': 8725,
       'T5': 8720, 'T4': 8715, 'T3': 8710, 'T2': 8705, '9A': 8700, '9K': 8695, '9Q': 8690, '9J': 8685,
       '9T': 8680, '98': 8675, '97': 8670, '96': 8665, '95': 8660, '94': 8655, '93': 8650, '92': 8645,
       '8A': 8640, '8K': 8635, '8Q': 8630, '8J': 8625, '8T': 8620, '89': 8615, '87': 8610, '86': 8605,
       '85': 8600, '84': 8595, '83': 8590, '82': 8585, '7A': 8580, '7K': 8575, '7Q': 8570, '7J': 8565,
       '7T': 8560, '79': 8555, '78': 8550, '76': 8545, '75': 8540, '74': 8535, '73': 8530, '72': 8525,
       '6A': 8520, '6K': 8515, '6Q': 8510, '6J': 8505, '6T': 8500, '69': 8495, '68': 8490, '67': 8485,
       '65': 8480, '64': 8475, '63': 8470, '62': 8465, '5A': 8460, '5K': 8455, '5Q': 8450, '5J': 8445,
       '5T': 8440, '59': 8435, '58': 8430, '57': 8425, '56': 8420, '54': 8415, '53': 8410, '52': 8405,
       '4A': 8400, '4K': 8395, '4Q': 8390, '4J': 8385, '4T': 8380, '49': 8375, '48': 8370, '47': 8365,
       '46': 8360, '45': 8355, '43': 8350, '42': 8345, '3A': 8340, '3K': 8335, '3Q': 8330, '3J': 8325,
       '3T': 8320, '39': 8315, '38': 8310, '37': 8305, '36': 8300, '35': 8295, '34': 8290, '32': 8285,
       '2A': 8280, '2K': 8275, '2Q': 8270, '2J': 8265, '2T': 8260, '29': 8255, '28': 8250, '27': 8245,
       '26': 8240, '25': 8235, '24': 8230, '23': 8225}

tps = {'A': 6000, 'K': 5950, 'Q': 5900, 'J': 5850, 'T': 5800, '9': 5750, '8': 5700, '7': 5650,
            '6': 5600, '5': 5550, '4': 5500, '3': 5450, '2': 5400}

tpps = {'AK': 5000,'AQ': 4950, 'AJ': 4900, 'AT': 4850, 'A9': 4800, 'A8': 4750, 'A7': 4700, 'A6': 4650,'A5': 4600, 'A4': 4550, 'A3': 4500, 'A2': 4450,
           'KQ': 4400, 'KJ': 4350, 'KT': 4300, 'K9': 4250, 'K8': 4200, 'K7': 4150, 'K6': 4100, 'K5': 4050, 'K4': 4000, 'K3': 3950, 'K2': 3900,
            'QJ': 3850, 'QT': 3800, 'Q9': 3750, 'Q8': 3700, 'Q7': 3650, 'Q6': 3600,'Q5': 3550, 'Q4': 3500, 'Q3': 3450, 'Q2': 3400,
             'JT': 3350, 'J9': 3300, 'J8': 3250, 'J7': 3200, 'J6': 3150, 'J5': 3100, 'J4': 3050, 'J3': 3000, 'J2': 2950,
            'T9': 2900, 'T8': 2850, 'T7': 2800, 'T6': 2750,'T5': 2700, 'T4': 2650, 'T3': 2600, 'T2': 2550,
            '98': 2500, '97': 2450, '96': 2400, '95': 2350,'94': 2300, '93': 2250, '92': 2200,
            '87': 2150, '86': 2100, '85': 2050, '84': 2000, '83': 1950, '82': 1900,
            '76': 1850, '75': 1800, '74': 1750, '73': 1700, '72': 1650,
            '65': 1600, '64': 1550, '63': 1500, '62': 1450,
            '54': 1400, '53': 1350, '52': 1300,
            '43': 1250, '42': 1200,
            '32': 1150 }

opps = {'A': 1000, 'K': 935, 'Q': 870, 'J': 805, 'T': 740, '9': 675, '8': 610, '7': 545,
            '6': 480, '5': 415, '4': 350, '3': 285, '2': 220}

def check_for_4kind(hand_strength):
    pairs = []
    kare = []
    for i in hand_strength:
       pairs.append (i[0])
    pairs.sort(key=lambda x: pat.index(x[0]))
    for i in pairs:
       if pairs.count(i) == 4:
           kare.append(i)
           pairs = list(filter(lambda a: a != i, pairs))
           kare.append(pairs[0])
           points =  karep.get(kare[0]) + highp.get(kare[1])
           return points
    else:
        points = None
        return None


def check_for_fullhouse(hand_strength):
    fh = []
    pairs = []
    for i in hand_strength:
       pairs.append (i[0])
    pairs.sort(key=lambda x: pat.index(x[0]))
    for i in pairs:
       if pairs.count(i) == 3:
           fh.append(i)
           pairs = list(filter(lambda a: a != i, pairs))
           for i in pairs:
               if pairs.count(i) == 2 or pairs.count(i) == 3:
                   fh.append(i)
                   fhs = fh[0] + fh[1]
                   points = fhp.get(fhs)
                   return points
 

def check_for_flush(hand_strength):
    h=[]
    c=[]
    s=[]
    d=[]
    hh= []
    cc = []
    ss =[]
    dd = []

    for i in hand_strength:
        if i[1] ==  'h':
            h.append(i[1])
            hh.append(i[0])
        elif i[1] == 'c':
            c.append(i[1])
            cc.append(i[0])
        elif i[1] == 's':
            s.append(i[1])
            ss.append(i[0])
        else:
            d.append(i[1])
            dd.append(i[0])

    pat = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2' ]
    hh.sort(key=lambda x: pat.index(x[0]))
    cc.sort(key=lambda x: pat.index(x[0]))
    ss.sort(key=lambda x: pat.index(x[0]))
    dd.sort(key=lambda x: pat.index(x[0]))

    fps = []

    if len(h) >= 5:
        for i in range(5):
            fps.append(highp.get(hh[i]))
            points = 7000 + sum(fps)
        return points
    elif len(c) >= 5:
         for i in range(5):
            fps.append(highp.get(cc[i]))
            points = 7000 + sum(fps)
         return points
    elif len(s) >= 5:
        for i in range(5):
            fps.append(highp.get(ss[i]))
            points = 7000 + sum(fps)
        return points
    elif len(d) >= 5:
        for i in range(5):
            fps.append(highp.get(dd[i]))
            points = 7000 + sum(fps)
        return points
    else:
        points = None
        return points

def check_for_straight(hand_strength):
    straight = []
    for i in hand_strength:
           straight.append(i[0])
    if 'T'  in straight and 'J'in straight and 'Q' in straight and 'K' in straight and 'A' in straight:
                     points = 7000
                     return points
    elif '9'  in straight and 'T'  in straight and 'J' in straight and 'Q' in straight and 'K' in straight:
                     points = 6900
                     return points
    elif '8' in straight and '9'in straight  and 'T' in straight and 'J' in straight and 'Q' in straight:
                     points = 6800
                     return points
    elif  '7' in straight and '8' in straight and '9'  in straight and 'T'  in straight and 'J' in straight:
                     points = 6700
                     return points
    elif '6' in straight  and '7' in straight and '8' in straight and '9' in straight and 'T' in straight:
                     points = 6600
                     return points
    elif '5' in straight and '6' in straight and '7' in straight and '8' in straight and '9' in straight:
                     points = 6500
                     return points
    elif  '4' in straight and  '5' in straight and '6' in straight and '7' in straight and '8' in straight:
                     points = 6400
                     return points
    elif  '3' in straight and '4' in straight and '5' in straight and '6' in straight and '7' in straight:
                     points = 6300
                     return points
    elif  '2' in straight and '3' in straight and '4' in straight and '5' in straight and '6' in straight:
                     points = 6200
                     return points
    elif  'A' in straight and '2' in straight and '3' in straight and '4' in straight and '5' in straight:
                    points = 6100
                    return points
    else:
                    points = None
                    return points


def check_for_trips(hand_strength):
    pairs = []
    for i in hand_strength:
       pairs.append (i[0])
    pairs.sort(key=lambda x: pat.index(x[0]))
    for i in pairs:

       if pairs.count(i) == 3:
           tripoints = tps.get(i)
           pairs = list(filter(lambda a: a != i, pairs))
           points = tripoints + highp.get(pairs[0]) + highp.get(pairs[1])
           return points


def check_for_two_pairs(hand_strength):
    pairs = []
    tp = []
    for i in hand_strength:
       pairs.append (i[0])
    pairs.sort(key=lambda x: pat.index(x[0]))
    for i in pairs:
       if  pairs.count(i) == 2:
            tp.append(i)
            pairs = list(filter(lambda a: a != i, pairs))
            for i in pairs:
                if pairs.count(i)==2:
                    tp.append(i)
                    pairs = list(filter(lambda a: a != i, pairs))
                    highpoints = highp.get(pairs[0])
                    tps = tp[0] + tp[1]
                    points =  tpps.get(tps) + highpoints
                    return points


def check_for_one_pair(hand_strength):
    pairs = []
    for i in hand_strength:
       pairs.append (i[0])
    pairs.sort(key=lambda x: pat.index(x[0]))
    for i in pairs:
        if  pairs.count(i) == 2:
            onepairpoints = opps.get(i)
            pairs = list(filter(lambda a: a != i, pairs))
            points = onepairpoints + highp.get(pairs[0]) + highp.get(pairs[1]) + highp.get(pairs[2])
            return points
        
def check_for_high(hand_strength):
    pairs = []
    pat = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2' ]

    for i in hand_strength:
       pairs.append (i[0])
    pairs.sort(key=lambda x: pat.index(x[0]))

    points = highp.get(pairs[0]) + highp.get(pairs[1]) +highp.get(pairs[2]) + highp.get(pairs[3]) +highp.get(pairs[4])
    return points

def find_best_hand(test):
        points_list = []
        points_list.append(check_for_straight_flush(test))
        points_list.append(check_for_4kind(test))
        points_list.append(check_for_fullhouse(test))
        points_list.append(check_for_flush(test))
        points_list.append(check_for_straight(test))
        points_list.append(check_for_trips(test))
        points_list.append(check_for_two_pairs(test))
        points_list.append(check_for_one_pair(test))
        points_list.append(check_for_high(test))
        for i in points_list:
                if i == None:
                        continue
                else:
                        return i

def who_wins(hand_a, hand_b):

    win_a =  0
    win_b = 0
    tie = 0
    boards = list(itertools.combinations(deck, 5))

    for i in boards:
            hand_strength_a = hand_a + list(i)
            hand_strength_b = hand_b + list(i)
            points_a = find_best_hand(hand_strength_a)
            points_b = find_best_hand(hand_strength_b)

            if  points_a > points_b:
                win_a += 1
            if  points_a < points_b:
                win_b += 1
            if  points_a == points_b:
                tie +=  1

    win_a_percent = (win_a / 1712304) * 100
    win_b_percent = (win_b / 1712304) * 100
    tie_percent = (tie / 1712304) * 100

    print(f" {hand_a}: {round(win_a_percent, 2)}% \n {hand_b}: {round(win_b_percent,2)}% \n Tie: {round(tie_percent,2)}%")

who_wins(hand_a, hand_b)
