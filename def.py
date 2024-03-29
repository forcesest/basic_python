money = 200
style = 'japanese'

def  checkstyle(style,money):
    stylecheck = ['japanese','thai','chinese']
    if money >= 200 and style in stylecheck:
        print('welcome')
    elif style not in stylecheck and money>= 300:
        print('You must buy our clothes price 100 bath')
    else:
        print("sorry , you can't come in")

checkstyle('france',400)