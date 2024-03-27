product = {'pencil':{'price': 50,'color':'red'},
          'rubber':{'price': 3,'color':'green'},
           'color pencil':{'price':100,'color':'orange'}}

while True:
    print('--------please fill information-------')
    p  = input('product name : ')
    q  = int(input('quantity : '))
    print('-----')
    if p in product:
        print(f'product name: {p} \nprice: {product[p]['price']} Bath \ncolor: {product[p]['color']}')
        print(f'quantity: {q}  pcs \ntotal price :{product[p]['price'] * q} Bath')
    else:
        print("don't have a product")
    #out of loop by ctrl+c
        