import turtle

# สร้างเต่าและกำหนดรูปร่างเป็นรูปเต่า
tao = turtle.Pen()
tao.shape('turtle')

# สร้างพจน์ tao1 เพื่อใช้เก็บสีและระยะทางที่จะวาด
tao1 = {'color': 'green', 'dis': 100}

# กำหนดสีให้กับเต่า
tao.color(tao1['color'])

def rect(tao_object,tdict):
    for i in range(4):
        tao_object.forward(tdict['dis'])
        tao_object.left(90)
rect(tao,tao1)
tao2 = turtle.Pen()
tao2.shape('turtle')
tao2dict = {'color': 'red', 'dis': 50}

tao.color(tao1['color'])

rect(tao2,tao2dict)
turtle.mainloop()



