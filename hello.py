print(" Hello...Python !!!")

num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    print('Number: '+ sval)
    if sval == 'Done':
        break
    try :
        fval = float(sval)
        print(fval)
        num = num + 1
        tot = tot + fval

    except:
        print('Invalid input')

print(tot,  num, tot/num )

print('Total:', tot, ' Count:', num, ' Avg:', tot / num )
