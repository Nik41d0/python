# 键盘监听,停止条件：ESC 键

from pynput.keyboard import Key,Listener

def on_press(key):
    print("按下 %s" %key)

def on_release(key):
    print("抬起 %s" %key)
    file = open("key.txt","ab")
    file.write(str(key).encode('utf-8'))
    if key == Key.esc:
        return False

if __name__ == '__main__':
    with Listener(
    on_press = on_press,
    on_release = on_release) as listener:
        listener.join()
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 鼠标监听

import pynput.mouse as pm
import threading

def on_click(x, y, button, pressed):
    if pressed:
        print("按下坐标")
        mxy="{},{}".format(x, y)
        print(mxy)
    if not pressed:
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',(x, y)))
 
while(1):
    with pm.Listener(on_click=on_click,on_scroll = on_scroll) as pmlistener:
        pmlistener.join()
