tile_color = {'red':100,'gold':200,'white':90,'grey': 30}

print('-------price-------')
for c,t in tile_color.items():
    print(f'สี ： {c} ราคา：{t}')
  
print('-----calculate tiles program-----')
try:
    tiles = int(input('requirement tiles : '))
    row = int(input(' 1 row used many tiles: '))
    color = input("what's tiles color [red/gold/white]:")

except :
    print('กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น')
    tiles = int(input('requirement tiles : '))
    row = int(input(' 1 row used many tiles: '))
    color = input("what's tiles color [red/gold/white/grey]:")
print('----------Calculate--------')
total_row = tiles//row
remain_tiles = tiles % row

buy_more = row - remain_tiles
if remain_tiles == 0 :
    buy_more = 0
print(f'total tiles = : {tiles}  pcs')
print(f'1 row used tiles : {row} pcs')
print('====cal====')
print(f'must be used tiles {total_row}  row')
print(f'the remaining tiles have not yet been laid {remain_tiles} pcs')
print(f'must buy additional tiles {buy_more} tiles')
print(f'total purchase more {buy_more*tile_color[color]} bath')

print('-----------end----------')