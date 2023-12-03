import enum #import Enum
from typing import List

@enum.unique
class Color(enum.Enum):
    NONE   = 'NONE',
    WHITE  = 'WHITE',
    YELLO  = 'YELLO',
    GREEN  = 'GREEN',
    BLUE   = 'BLUE',
    RED    = 'RED',
    ORANGE = 'ORANGE'

@enum.unique
class Direction(enum.Enum):
    NONE  = 'none',
    FRONT = 'front',
    REAR  = 'rear',
    LEFT  = 'left',
    RIGHT = 'right',
    UP    = 'up',
    DOWN  = 'down'

class Coordinates:
    def __init__(self, x:int=-1, y:int=-1, z:int=-1) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f'Coordinates: x={self.x}, y={self.y}, z={self.z}.'

class BlockSide:
    def __init__(self) -> None:
        self.color = Color.NONE
        self.dir   = Direction.NONE        
    
    def SetColor(self, color:Color) -> None:
        self.color = color

    def GetColor(self) -> Color:
        return self.color

    def SetDirection(self, dir:Direction) -> None:
        self.dir = dir
        print(f'BlockSide: color={self.GetColor()}, Dir={self.GetDirection()}')

    def GetDirection(self) -> Direction:
        return self.dir

class Block:
    def __init__(self, name:str, sides_count: int) -> None:
        self.name = name
        self.coordinates = Coordinates()
        self.sides = []
        for i in range(sides_count):
            self.sides.append(BlockSide())
        print(f'Create {self.name}. Sides={sides_count}')
    
    def GetSidesCount(self) -> int:
        return len(self.sides)
    
    def GetSideColor(self, side_num:int) -> Color:
        if side_num >= self.GetSidesCount():
            return None
        return self.sides[side_num].GetColor()

    def SetSideColor(self, side_num:int, color: Color) -> bool:
        if side_num >= self.GetSidesCount():
            print(f'{self.name}. SetSideColor {color} Fault.')
            return False
        self.sides[side_num].SetColor(color)
        print(f'{self.name}. SetSideColor {color} Success.')
        return True

    def SetCoordinates(self, coordinates:Coordinates) -> None:
        self.coordinates = coordinates
        print(self.coordinates)
    
    def SetSideDirection(self, side_num:int, dir:Direction) -> None:
        if side_num >= self.GetSidesCount():
            return
        return self.sides[side_num].SetDirection(dir)

    def GetSideDirection(self, side_num:int) -> Direction:
        if side_num >= self.GetSidesCount():
            return
        return self.sides[side_num].GetDirection()

    def GetCoordinates(self) -> Coordinates:
        return self.coordinates

    def GetSideNumAndColorAndDir(self):
        result = []
        for side in self.sides:
            side_index = self.sides.index(side)
            side_dir = self.GetSideDirection(side_index)
            side_color = self.GetSideColor(side_index)
            result.append((side_index, side_dir, side_color))
        return result

class ConerBlock(Block):
    def __init__(self) -> None:
        super().__init__('ConerBlock', 3)

    def SetSideColor(self, side_num: int, color: Color) -> bool:
        return super().SetSideColor(side_num, color)

class EdgeBlock(Block):
    def __init__(self) -> None:
        super().__init__('EdgeBlock', 2)

class CentralBlock(Block):
    def __init__(self, color: Color) -> None:
        super().__init__('CentralBlock', 1)
        self.SetSideColor(0, color)

    def SetSideDirection(self, dir: Direction) -> None:
        return super().SetSideDirection(0, dir)

class Rubik:
    def __init__(self) -> None:
        self.white_dir = Direction.UP
        self.yellow_dir = Direction.DOWN
        self.green_dir = Direction.LEFT
        self.blue_dir = Direction.RIGHT
        self.red_dir = Direction.FRONT
        self.orange_dir = Direction.REAR

        self.bloks_list = []
        bloks = self.bloks_list

        self.CreateCentrals(bloks)
        self.CreateCorners(bloks)
        self.CreateEdges(bloks)

        print(f'Bloks count: {len(bloks)}')

        self.CheckNoneDirNoneColor(bloks)
        self.CheckCororsAndDirs(bloks)

        self.PrintRubik()

    def PrintRubik(self):
        bloks = self.bloks_list
        white_list = []
        for blok in bloks:
            ress = blok.GetSideNumAndColorAndDir()
            for side_index, side_dir, side_color in ress:
                if side_color == Color.WHITE:
                    white_list.append(blok)
                    print(f'{blok.name},{side_color},{side_dir}')

    def CheckNoneDirNoneColor(self, bloks):
        for blok in bloks:
            ress = blok.GetSideNumAndColorAndDir()
            for side_index, side_dir, side_color in ress:
                if (side_dir == Direction.NONE) or (side_color == Color.NONE):
                    print(f'Bloknum({bloks.index(blok)}):Side={side_index}, {side_dir}, {side_color}')

    def CheckCororsAndDirs(self, bloks):
        white_dir = self.white_dir
        yellow_dir = self.yellow_dir
        green_dir = self.green_dir
        blue_dir = self.blue_dir
        red_dir = self.red_dir
        orange_dir = self.orange_dir

        for blok in bloks:
            ress = blok.GetSideNumAndColorAndDir()
            for side_index, side_dir, side_color in ress:
                if side_color == Color.WHITE:
                    if side_dir != white_dir:
                        print(f'Bloknum({bloks.index(blok)}):Side={side_index}, {side_dir}, {side_color}')
                        break
                if side_color == Color.YELLO:
                    if side_dir != yellow_dir:
                        print(f'Bloknum({bloks.index(blok)}):Side={side_index}, {side_dir}, {side_color}')
                        break
                if side_color == Color.GREEN:
                    if side_dir != green_dir:
                        print(f'Bloknum({bloks.index(blok)}):Side={side_index}, {side_dir}, {side_color}')
                        break
                if side_color == Color.BLUE:
                    if side_dir != blue_dir:
                        print(f'Bloknum({bloks.index(blok)}):Side={side_index}, {side_dir}, {side_color}')
                        break
                if side_color == Color.RED:
                    if side_dir != red_dir:
                        print(f'Bloknum({bloks.index(blok)}):Side={side_index}, {side_dir}, {side_color}')
                        break
                if side_color == Color.ORANGE:
                    if side_dir != orange_dir:
                        print(f'Bloknum({bloks.index(blok)}):Side={side_index}, {side_dir}, {side_color}')
                        break

    def CreateCentrals(self, bloks):
        self.center_wite   = CentralBlock(Color.WHITE) # 1
        self.center_wite.SetSideDirection(self.white_dir)
        bloks.append(self.center_wite)
        self.center_yello  = CentralBlock(Color.YELLO) # 2
        self.center_yello.SetSideDirection(self.yellow_dir)
        bloks.append(self.center_yello)
        self.center_green  = CentralBlock(Color.GREEN) # 3
        self.center_green.SetSideDirection(self.green_dir)
        bloks.append(self.center_green)
        self.center_blue   = CentralBlock(Color.BLUE)  # 4
        self.center_blue.SetSideDirection(self.blue_dir)
        bloks.append(self.center_blue)
        self.center_red    = CentralBlock(Color.RED)   # 5
        self.center_red.SetSideDirection(self.red_dir)
        bloks.append(self.center_red)
        self.center_orange = CentralBlock(Color.ORANGE) # 6
        self.center_orange.SetSideDirection(self.orange_dir)
        bloks.append(self.center_orange)

    def CreateCorners(self, bloks):
        white_dir = self.white_dir
        yellow_dir = self.yellow_dir
        green_dir = self.green_dir
        blue_dir = self.blue_dir
        red_dir = self.red_dir
        orange_dir = self.orange_dir

        self.coner_wbr = ConerBlock()                   # 7
        self.coner_wbr.SetSideColor(0, Color.WHITE)
        self.coner_wbr.SetSideDirection(0, white_dir)
        self.coner_wbr.SetSideColor(1, Color.BLUE)
        self.coner_wbr.SetSideDirection(1, blue_dir)
        self.coner_wbr.SetSideColor(2, Color.RED)
        self.coner_wbr.SetSideDirection(2, red_dir)
        bloks.append(self.coner_wbr)

        self.coner_wgo = ConerBlock()                   # 8
        self.coner_wgo.SetSideColor(0, Color.WHITE)
        self.coner_wgo.SetSideDirection(0, white_dir)
        self.coner_wgo.SetSideColor(1, Color.GREEN)
        self.coner_wgo.SetSideDirection(1, green_dir)
        self.coner_wgo.SetSideColor(2, Color.ORANGE)
        self.coner_wgo.SetSideDirection(2, orange_dir)
        bloks.append(self.coner_wgo)

        self.coner_wrg = ConerBlock()                   # 9
        self.coner_wrg.SetSideColor(0, Color.WHITE)
        self.coner_wrg.SetSideDirection(0, white_dir)
        self.coner_wrg.SetSideColor(1, Color.RED)
        self.coner_wrg.SetSideDirection(1, red_dir)
        self.coner_wrg.SetSideColor(2, Color.GREEN)
        self.coner_wrg.SetSideDirection(2, green_dir)
        bloks.append(self.coner_wrg)

        self.coner_wob = ConerBlock()                   # 10
        self.coner_wob.SetSideColor(0, Color.WHITE)
        self.coner_wob.SetSideDirection(0, white_dir)
        self.coner_wob.SetSideColor(1, Color.ORANGE)
        self.coner_wob.SetSideDirection(1, orange_dir)
        self.coner_wob.SetSideColor(2, Color.BLUE)
        self.coner_wob.SetSideDirection(2, blue_dir)
        bloks.append(self.coner_wob)

        self.coner_ybr = ConerBlock()                   # 11
        self.coner_ybr.SetSideColor(0, Color.YELLO)
        self.coner_ybr.SetSideDirection(0, yellow_dir)
        self.coner_ybr.SetSideColor(1, Color.BLUE)
        self.coner_ybr.SetSideDirection(1, blue_dir)
        self.coner_ybr.SetSideColor(2, Color.RED)
        self.coner_ybr.SetSideDirection(2, red_dir)
        bloks.append(self.coner_ybr)

        self.coner_ygo = ConerBlock()                   # 12
        self.coner_ygo.SetSideColor(0, Color.YELLO)
        self.coner_ygo.SetSideDirection(0, yellow_dir)
        self.coner_ygo.SetSideColor(1, Color.GREEN)
        self.coner_ygo.SetSideDirection(1, green_dir)
        self.coner_ygo.SetSideColor(2, Color.ORANGE)
        self.coner_ygo.SetSideDirection(2, orange_dir)
        bloks.append(self.coner_ygo)

        self.coner_yrg = ConerBlock()                   # 13
        self.coner_yrg.SetSideColor(0, Color.YELLO)
        self.coner_yrg.SetSideDirection(0, yellow_dir)
        self.coner_yrg.SetSideColor(1, Color.RED)
        self.coner_yrg.SetSideDirection(1, red_dir)
        self.coner_yrg.SetSideColor(2, Color.GREEN)
        self.coner_yrg.SetSideDirection(2, green_dir)
        bloks.append(self.coner_yrg)

        self.coner_yob = ConerBlock()                   # 14
        self.coner_yob.SetSideColor(0, Color.YELLO)
        self.coner_yob.SetSideDirection(0, yellow_dir)
        self.coner_yob.SetSideColor(1, Color.ORANGE)
        self.coner_yob.SetSideDirection(1, orange_dir)
        self.coner_yob.SetSideColor(2, Color.BLUE)
        self.coner_yob.SetSideDirection(2, blue_dir)
        bloks.append(self.coner_yob)

    def CreateEdges(self, bloks):
        white_dir = self.white_dir
        yellow_dir = self.yellow_dir
        green_dir = self.green_dir
        blue_dir = self.blue_dir
        red_dir = self.red_dir
        orange_dir = self.orange_dir
    
        self.edge_wr = EdgeBlock()                     # 15
        self.edge_wr.SetSideColor(0, Color.WHITE)
        self.edge_wr.SetSideDirection(0, white_dir)
        self.edge_wr.SetSideColor(1, Color.RED)
        self.edge_wr.SetSideDirection(1, red_dir)
        bloks.append(self.edge_wr)
        self.edge_wg = EdgeBlock()                     # 16
        self.edge_wg.SetSideColor(0, Color.WHITE)
        self.edge_wg.SetSideDirection(0, white_dir)
        self.edge_wg.SetSideColor(1, Color.GREEN)
        self.edge_wg.SetSideDirection(1, green_dir)
        bloks.append(self.edge_wg)
        self.edge_wo = EdgeBlock()                     # 17
        self.edge_wo.SetSideColor(0, Color.WHITE)
        self.edge_wo.SetSideDirection(0, white_dir)
        self.edge_wo.SetSideColor(1, Color.ORANGE)
        self.edge_wo.SetSideDirection(1, orange_dir)
        bloks.append(self.edge_wo)
        self.edge_wb = EdgeBlock()                     # 18
        self.edge_wb.SetSideColor(0, Color.WHITE)
        self.edge_wb.SetSideDirection(0, white_dir)
        self.edge_wb.SetSideColor(1, Color.BLUE)
        self.edge_wb.SetSideDirection(1, blue_dir)
        bloks.append(self.edge_wb)

        self.edge_yr = EdgeBlock()                     # 19
        self.edge_yr.SetSideColor(0, Color.YELLO)
        self.edge_yr.SetSideDirection(0, yellow_dir)
        self.edge_yr.SetSideColor(1, Color.RED)
        self.edge_yr.SetSideDirection(1, red_dir)
        bloks.append(self.edge_yr)
        self.edge_yg = EdgeBlock()                     # 20
        self.edge_yg.SetSideColor(0, Color.YELLO)
        self.edge_yg.SetSideDirection(0, yellow_dir)
        self.edge_yg.SetSideColor(1, Color.GREEN)
        self.edge_yg.SetSideDirection(1, green_dir)
        bloks.append(self.edge_yg)
        self.edge_yo = EdgeBlock()                     # 21
        self.edge_yo.SetSideColor(0, Color.YELLO)
        self.edge_yo.SetSideDirection(0, yellow_dir)
        self.edge_yo.SetSideColor(1, Color.ORANGE)
        self.edge_yo.SetSideDirection(1, orange_dir)
        bloks.append(self.edge_yo)
        self.edge_yb = EdgeBlock()                     # 22
        self.edge_yb.SetSideColor(0, Color.YELLO)
        self.edge_yb.SetSideDirection(0, yellow_dir)
        self.edge_yb.SetSideColor(1, Color.BLUE)
        self.edge_yb.SetSideDirection(1, blue_dir)
        bloks.append(self.edge_yb)

        self.edge_rg = EdgeBlock()                     # 23
        self.edge_rg.SetSideColor(0, Color.RED)
        self.edge_rg.SetSideDirection(0, red_dir)
        self.edge_rg.SetSideColor(1, Color.GREEN)
        self.edge_rg.SetSideDirection(1, green_dir)
        bloks.append(self.edge_rg)
        self.edge_go = EdgeBlock()                     # 24
        self.edge_go.SetSideColor(0, Color.GREEN)
        self.edge_go.SetSideDirection(0, green_dir)
        self.edge_go.SetSideColor(1, Color.ORANGE)
        self.edge_go.SetSideDirection(1, orange_dir)
        bloks.append(self.edge_go)
        self.edge_ob = EdgeBlock()                     # 25
        self.edge_ob.SetSideColor(0, Color.ORANGE)
        self.edge_ob.SetSideDirection(0, orange_dir)
        self.edge_ob.SetSideColor(1, Color.BLUE)
        self.edge_ob.SetSideDirection(1, blue_dir)
        bloks.append(self.edge_ob)
        self.edge_br = EdgeBlock()                     # 26
        self.edge_br.SetSideColor(0, Color.BLUE)
        self.edge_br.SetSideDirection(0, blue_dir)
        self.edge_br.SetSideColor(1, Color.RED)
        self.edge_br.SetSideDirection(1, red_dir)
        bloks.append(self.edge_br)

def main():
    print(__name__)
    side = Rubik()

if __name__ == '__main__':
    main()