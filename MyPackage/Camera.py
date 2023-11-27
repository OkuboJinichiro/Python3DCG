# カメラクラスのモジュール
# def __init__(カメラ座標,レイの長さ,焦点距離):
    # カメラの初期化
# def RotateALL(回転前のレイベクトル): 
    # レイをselfの回転情報に合わせて変換

from .Math import *

# カメラクラス
class Camera:
    # 初期化
    def __init__(self,Pos,RayLength,FocalLength):
        self.Pos = Pos
        self.RayLength = RayLength
        self.FocalLength = FocalLength
        self.Rotate = Vector3(0,0,0)
    # レイの方向変換
    def RotateALL(self,RayVector):
        # X回転
        Angle = self.Rotate.x
        while 1:
            if Angle < 0:
                Angle = Angle + 360
            else:break
        Angle2,Angle3,Angle4 = 0,0,0
        if Angle / 90 > 1:
            A = Angle%360
            if A <= 90:
                Angle = A
            elif A <= 180:
                Angle = 90
                Angle2 = A-90
            elif A <= 270:
                Angle = 90
                Angle2 = 90
                Angle3 = A-180
            elif A <= 360:
                Angle = 90
                Angle2 = 90
                Angle3 = 90
                Angle4 = A-270
        Angles = [Angle,Angle2,Angle3,Angle4]
        for i in Angles:
            RayVector = RX(RayVector,i)

        # Y回転
        Angle = self.Rotate.y
        while 1:
            if Angle < 0:
                Angle = Angle + 360
            else:break
        Angle2,Angle3,Angle4 = 0,0,0
        if Angle / 90 > 1:
            A = Angle%360
            if A <= 90:
                Angle = A
            elif A <= 180:
                Angle = 90
                Angle2 = A-90
            elif A <= 270:
                Angle = 90
                Angle2 = 90
                Angle3 = A-180
            elif A <= 360:
                Angle = 90
                Angle2 = 90
                Angle3 = 90
                Angle4 = A-270
        Angles = [Angle,Angle2,Angle3,Angle4]
        for i in Angles:
            RayVector = RY(RayVector,i)

        # Z回転
        Angle = self.Rotate.z
        while 1:
            if Angle < 0:
                Angle = Angle + 360
            else:break
        Angle2,Angle3,Angle4 = 0,0,0
        if Angle / 90 > 1:
            A = Angle%360
            if A <= 90:
                Angle = A
            elif A <= 180:
                Angle = 90
                Angle2 = A-90
            elif A <= 270:
                Angle = 90
                Angle2 = 90
                Angle3 = A-180
            elif A <= 360:
                Angle = 90
                Angle2 = 90
                Angle3 = 90
                Angle4 = A-270
        Angles = [Angle,Angle2,Angle3,Angle4]
        for i in Angles:
            RayVector = RZ(RayVector,i)

        return RayVector