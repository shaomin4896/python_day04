import random
import time

# 建立字母串列
char_arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# 紀錄遊戲開始時間
count = 0
time_start = time.time()
# 隨機挑選字母
index = random.randint(0,25)
def main():
    # global
    global char_arr,index,count
    # 顯示
    percent = count / 200 * 100
    t = time.time() - time_start
    drawText(char_arr[index],300,300,"black",80)
    drawText("經過時間："+str(t),300,450,"black",80)
    drawText("完成：" + str(percent) + "%",300,600,"black",80)
    # 按鍵按下
    for i in char_arr:
        if getattr(key,i) and char_arr[index] == i:
            count += 1
            index = random.randint(0,25)
    
    # 土法煉鋼寫法
    # if key.a and char_arr[index] == 'a':
    #     index = random.randint(0,25)
    # if key.b and char_arr[index] == 'b':
    #     index = random.randint(0,25)
    # if key.c and char_arr[index] == 'c':
    #     index = random.randint(0,25)
    # if key.d and char_arr[index] == 'd':
    #     index = random.randint(0,25)
    # if key.e and char_arr[index] == 'e':
    #     index = random.randint(0,25)
    # if key.f and char_arr[index] == 'f':
    #     index = random.randint(0,25)
    # if key.g and char_arr[index] == 'g':
    #     index = random.randint(0,25)
    # if key.h and char_arr[index] == 'h':
    #     index = random.randint(0,25)
    # if key.i and char_arr[index] == 'i':
    #     index = random.randint(0,25)
    # if key.j and char_arr[index] == 'j':
    #     index = random.randint(0,25)
    # if key.k and char_arr[index] == 'k':
    #     index = random.randint(0,25)
    # if key.l and char_arr[index] == 'l':
    #     index = random.randint(0,25)
    # if key.m and char_arr[index] == 'm':
    #     index = random.randint(0,25)
    # if key.n and char_arr[index] == 'n':
    #     index = random.randint(0,25)
    # if key.o and char_arr[index] == 'o':
    #     index = random.randint(0,25)
    # if key.p and char_arr[index] == 'p':
    #     index = random.randint(0,25)
    # if key.q and char_arr[index] == 'q':
    #     index = random.randint(0,25)
    # if key.r and char_arr[index] == 'r':
    #     index = random.randint(0,25)
    # if key.s and char_arr[index] == 's':
    #     index = random.randint(0,25)
    # if key.t and char_arr[index] == 't':
    #     index = random.randint(0,25)
    # if key.u and char_arr[index] == 'u':
    #     index = random.randint(0,25)
    # if key.v and char_arr[index] == 'v':
    #     index = random.randint(0,25)
    # if key.w and char_arr[index] == 'w':
    #     index = random.randint(0,25)
    # if key.x and char_arr[index] == 'x':
    #     index = random.randint(0,25)
    # if key.y and char_arr[index] == 'y':
    #     index = random.randint(0,25)
    # if key.z and char_arr[index] == 'z':
    #     index = random.randint(0,25)
    # 遊戲終止
    if count == 200:
        stop()
    pass
forever(main)