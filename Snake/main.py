import sys
import os
import field
import time
from pynput import keyboard

noExit = False

fld = field.cField()
##fld.SetFieldDimension((5*8),(7*2))
snake = field.cSnake()
fld.AddSnake(snake)
##for i in range(2):
##    snake.IncrementBody()

def Exit():
    NoExit = False

def on_press(key):
    try:
##        print('alphanumeric key {0} pressed'.format(key.char))
        if key == keyboard.Key.up:
            fld.snake.SetDirUp()
        if key == keyboard.Key.down:
            fld.snake.SetDirDown()
        if key == keyboard.Key.left:
            fld.snake.SetDirLeft()
        if key == keyboard.Key.right:
            fld.snake.SetDirRight()
        if key.char == 'q':
            fld.snake.head.position.SetPosition(0,0)
    except AttributeError:
##        print('special key {0} pressed'.format(key))
        pass

def on_release(key):
##    Exit()
##    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        Exit()
        print('NoExit =',noExit)
        # Stop listener
        return False

# Collect events until released
##with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
##    listener.join()


def main(argv):
    print('main() - run')

    print('time.sleep(1)')
    time.sleep(0.1)
    os.system('cls')

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(on_press=on_press,on_release=on_release)
    listener.start()

    sleep_time = 0.1#0.05
    noExit = True
    while noExit == True: ## TODO noExit при вызове Exit() почему-то остаётся True
        fld.Show()
        time.sleep(sleep_time)
        
    listener.stop()


if __name__ == '__main__':
    sys.exit(main(sys.argv))
