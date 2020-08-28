import game
import random #載入產生隨機數套件

bg = game.create_sprite('bg_0.jpg', 'bg_1.jpg') #背景圖
ceiling = game.create_sprite('w.png') #天花板的針刺
left_wall = game.create_sprite('wall.png') #左邊牆壁
right_wall = game.create_sprite('wall.png') #右邊牆壁
player = game.create_sprite('p1.png', 'p2.png', 'p3.png', 'p4.png', 'p5.png') #玩家

# 初始化角色位置&圖層
player.y = 100
left_wall.x -= 450
right_wall.x += 450
ceiling.moveTo(600, 18)
ceiling.layer = 1

life = 10 #玩家血量
floor = 0 #階梯數
stairs = [] #存放階梯角色
vy = 0 #玩家墜落的速度
touchOn = None #當前踩著的階梯 id
clock = 0 #計時器
flash = False

# game.create_sound('bgm.mp3', True)

#初始化階梯
for i in range(6):
    s = game.create_sprite("s1.png","s2.png","s3.png","s4.png","s5.png","s6.png")
    s.costume_id = random.randint(0,5)
    s.x = random.randrange(350,850)
    s.y = i * 150 + 550
    s.id = i
    stairs.append(s)
print(len(stairs))
# 遊戲主迴圈
def loop ():
    update_stairs()
    update_player()
    update_info()
    update_background()
    gameover_check()
    update_costume()
    pass
# 偵測玩家操控並更新角色位置
def update_player ():
    global vy
    if key.left and not player.touched(left_wall):
        player.x -= 12
    if key.right and not player.touched(right_wall):
        player.x += 12
    vy += 0.6
    player.y += vy
    pass
    

# # 讓所有階梯向上捲動
def update_stairs ():
    global floor
    for s in stairs:
        s.y -= 3
        if s.y < -30:
            s.y += 1350
            s.costume_id = random.randint(0,5)
            s.hidden = False
            floor += 1
# # 玩家踩到階梯時執行階梯對應的功能
def on_touch_stair (s):
    global touchOn, life, vy,flash
    vy = 0
    player.y = s.y - 50
    
    if s.costume_id == 0:
        player.x-= 6
    elif s.costume_id == 1:
        player.x += 6
    elif s.costume_id == 2:
        vy = -16
    elif s.costume_id == 3 and s.id != touchOn:
        life += 1
    elif s.costume_id == 4 and s.id != touchOn:
        life -= 3
        flash = True
    elif s.costume_id == 5:
        s.hidden = True
    touchOn = s.id
# # 更新遊戲分數
def update_info ():
    # global floor,life
    drawText('分數：' + str(floor), 10, 10, 'white', 30)
    drawText('生命：' + str(life), 10, 40, 'white', 30)
# # 判斷遊戲是否結束
def gameover_check ():
    if life <= 0 or player.touched(ceiling) or player.y >= 900:
        bg.costume_id = 1
        stop()
# # 捲動更新背景圖
def update_background ():
    global flash
    
    bg.y -= 1
    if bg.y < 400:
        bg.y += 100
    
    bg.costume_id = 0
    if flash:
        bg.costume_id = 1
        flash = False
# # 玩家走路動畫
def update_costume ():
    global clock
    
    clock+= 1
    if clock % 4 == 0:
        if key.right:
            if player.costume_id == 1:
                player.costume_id = 2
            else:
                player.costume_id = 1
        elif key.left:
            if player.costume_id == 3:
                player.costume_id = 4
            else:
                player.costume_id = 3
        else:
            player.costume_id = 0

player.on('touch', stairs, on_touch_stair)
game.forever(loop) #重複不斷執行遊戲迴圈


