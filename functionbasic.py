
def land(width,long,price =999888):
    """ที่ดินสาธร"""
    cal =  width * long
    cal_wa = cal / 4 
    print('ที่ดินผืนนี้กว้าง : {} เมตร  ยาว: {}'.format(width,long))
    print('ที่ดินพื้นนี้ีพื้นที่ : {} ตารางเมตร'.format(cal))
    print('ที่ดินพื้นนี้ีพื้นที่ : {} ตารางวา '.format(cal_wa))
    calprice = cal_wa * price
    return (f'ที่ดินผืนนี้ราคา : {calprice:,.2f} บาท')
res=land(20,80)

print(res)


