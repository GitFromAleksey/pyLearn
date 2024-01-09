import os
import random as rnd
from enum import Enum
from colorama import init, Fore, Back, Style

##------------------------------------------------------------------------------
class cDimension(object):
    def __init__(self, name):
        self.width = 0
        self.height = 0
        self.name = name ## TODO перенести в cObject

    def SetDimension(self, width, height):
        self.width = width
        self.height = height

    def PrintDimension(self):
        print(self.name + ' dimensions: width:', self.width, '; height:', self.height)

##------------------------------------------------------------------------------
class cPosition():
    def __init__(self):
        self.x = 0
        self.y = 0

    def Up(self):
        self.y -= 1
    def Down(self):
        self.y += 1
    def Left(self):
        self.x -= 1
    def Right(self):
        self.x += 1

    def CheckEqual(self, pos):
        if pos.GetXpos() == self.GetXpos():
            if pos.GetYpos() == self.GetYpos():
                return True
        return False

    def GenerateRandomPosition(self, height, width):
        self.y = int(rnd.random()*height)
        self.x = int(rnd.random()*width)
        pass

    def SetPosition(self,x,y):
        self.x = x
        self.y = y

    def GetXpos(self):
        return self.x
    
    def GetYpos(self):
        return self.y
    
    def PrintPosition(self):
        print('x =', self.x,'y =', self.y)

##------------------------------------------------------------------------------
class cObject(cDimension):
    def __init__(self, name):
        super().__init__(name)
        super().SetDimension(1,1)
        self.position = cPosition()
        self.simbol = Fore.GREEN+'*'+Style.RESET_ALL

    def SetSimbol(self, simb):
        self.simbol = simb

    def PrintName(self):
        print(self.name)

##------------------------------------------------------------------------------
class cDirection(Enum):
    DIR_UP = 1
    DIR_DOWN = 2
    DIR_LEFT = 3
    DIR_RIGHT = 4
    DIR_STOP = 5
##------------------------------------------------------------------------------
##class cSnake(object):
class cSnake():
    max_snake_len = 300
    min_snake_len = 1
    x_start_pos = 0
    y_start_pos = 0
    
    def __init__(self):
        self.body_list = []
        self.head = cObject('Head')
        self.head.position.SetPosition(self.x_start_pos,self.y_start_pos)
        self.head.SetSimbol(Fore.YELLOW+'#'+Style.RESET_ALL)
        self.AddBody(self.head)
        self.direction = cDirection.DIR_RIGHT
        self.x_max_pos = 40-1
        self.y_max_pos = 14-1        

    def TailPositionChange(self):
        for index in range(len(self.body_list)):
            if self.body_list[index] == self.head:
                prev_x = self.body_list[index].position.GetXpos()
                prev_y = self.body_list[index].position.GetYpos()
                continue
            cur_x = self.body_list[index].position.GetXpos()
            cur_y = self.body_list[index].position.GetYpos()
            self.body_list[index].position.SetPosition(prev_x,prev_y)
            prev_x = cur_x
            prev_y = cur_y

    ## проверка попадания координаты в координату змеи
    def CheckSnakeHit(self, pos):
        for item in self.body_list:
            if item.position.CheckEqual(pos):
                return True
        return False
    ## проверка самопересечения
    def CheckSelfCross(self):
        res = False
        for item in self.body_list:
            if item.name == 'Head':
                continue
            if self.head.position.CheckEqual(item.position) == True:
                res = True
        return res
    
    ## проверка касания края поля
    def IsBorderTouch(self,_pos,_dir):
        res = False
        pos = cPosition()
        pos.SetPosition(_pos.GetXpos(),_pos.GetYpos())
##        if _dir == cDirection.DIR_UP:
##            pos.Up()
##        elif _dir == cDirection.DIR_DOWN:
##            pos.Down()
##        elif _dir == cDirection.DIR_LEFT:
##            pos.Left()
##        elif _dir == cDirection.DIR_RIGHT:
##            pos.Right()
## проверка касаний границ поля
        if (_pos.GetXpos() > self.x_max_pos):
            res = True
            _pos.SetPosition(0, _pos.GetYpos())
        if (_pos.GetXpos() < 0):
            res = True
            _pos.SetPosition(self.x_max_pos, _pos.GetYpos())
        if (_pos.GetYpos() > self.y_max_pos):
            res = True
            _pos.SetPosition(_pos.GetXpos(), 0)
        if (_pos.GetYpos() < 0):
            res = True
            _pos.SetPosition(_pos.GetXpos(), self.y_max_pos)
        
        return res

    def Up(self):
        self.direction = cDirection.DIR_UP
        self.TailPositionChange()
        self.head.position.Up()

    def Down(self):
        self.direction = cDirection.DIR_DOWN
        self.TailPositionChange()
        self.head.position.Down()

    def Left(self):
        self.direction = cDirection.DIR_LEFT
        self.TailPositionChange()
        self.head.position.Left()

    def Right(self):
        self.direction = cDirection.DIR_RIGHT
        self.TailPositionChange()
        self.head.position.Right()
        
    def AddBody(self,obj):
        self.body_list.append(obj)

    def GetBody(self):
        return self.body_list

    def GetLen(self):
        return len(self.body_list)

    def SetDirUp(self):
        self.direction = cDirection.DIR_UP

    def SetDirDown(self):
        self.direction = cDirection.DIR_DOWN

    def SetDirLeft(self):
        self.direction = cDirection.DIR_LEFT

    def SetDirRight(self):
        self.direction = cDirection.DIR_RIGHT

    def run(self):
        _dir = self.direction

        if _dir == cDirection.DIR_UP:
            self.Up()
        elif _dir == cDirection.DIR_DOWN:
            self.Down()
        elif _dir == cDirection.DIR_LEFT:
            self.Left()
        elif _dir == cDirection.DIR_RIGHT:
            self.Right()
        elif _dir == cDirection.DIR_STOP:
            pass

        if self.IsBorderTouch(self.head.position,_dir):
            pass

        if self.CheckSelfCross():
            self.direction = cDirection.DIR_STOP

    def IncrementBody(self):
        if len(self.body_list) < self.max_snake_len:
            end_body = self.body_list[len(self.body_list)-1]
            new_body = cObject('Snake Body')
            x = end_body.position.GetXpos()
            y = end_body.position.GetYpos()
            new_body.position.SetPosition(x,y)
            if self.direction == cDirection.DIR_LEFT:
                new_body.position.Right()
            elif self.direction == cDirection.DIR_RIGHT:
                new_body.position.Left()
            elif self.direction == cDirection.DIR_UP:
                new_body.position.Down()
            elif self.direction == cDirection.DIR_DOWN:
                new_body.position.Up()
            self.body_list.append(new_body)

    def GetSnakeLen(self):
        return len(self.body_list)
    
    def DecrementBody(self):
        if len(self.body_list) > self.min_snake_len:
            self.body_list.pop()

##------------------------------------------------------------------------------
class cField(cDimension):
    def __init__(self):
        print('Create cField')
        super().__init__('field')
        init()
        self.default_width = (5*8)
        self.default_height = (7*2)
        super().SetDimension(self.default_width,self.default_height)
        self.apple = cObject('apple')
        self.apple.SetSimbol(Style.BRIGHT+Fore.RED+'Q'+Style.RESET_ALL)

    def GenerateAnApplePosition(self):
        self.apple.position.GenerateRandomPosition(self.default_height, self.default_width)
        while self.snake.CheckSnakeHit(self.apple.position):
            self.apple.position.GenerateRandomPosition(self.default_height, self.default_width)
        
    def Show(self):
        self.snake.run()
        if self.snake.CheckSnakeHit(self.apple.position):
            self.snake.IncrementBody()
            self.GenerateAnApplePosition()
        snake_body = self.snake.GetBody()
        string = str()
        for y in range(self.height):
            body_cnt = 0
            for x in range(self.width):
                if self.apple.position.GetXpos() == x:
                    if self.apple.position.GetYpos() == y:
                        string += self.apple.simbol
                        body_cnt += 1
                for body_item in snake_body:
                    x_pos = body_item.position.GetXpos()
                    y_pos = body_item.position.GetYpos()
                    if (y == y_pos) and (x == x_pos):
                        string += body_item.simbol
                        body_cnt += 1
                if body_cnt == 0:
                    string += '-'
                else:
                    body_cnt -= 1
                    continue
            string += '\n'#print(string)
        os.system('cls')
        print(string)
        print('Snake len:', self.snake.GetSnakeLen())
        print('dir:',self.snake.direction)

    def SetFieldDimension(self, width, height):
        super().SetDimension( width, height)
        self.default_width = width
        self.default_height = height

    def AddSnake(self,snake):
        self.snake = snake

##------------------------------------------------------------------------------


