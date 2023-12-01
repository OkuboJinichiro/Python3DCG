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
        # 角度を90度以下に分割
        Angle,Angle2,Angle3,Angle4 = Angle90(Angle)
        Angles = [Angle,Angle2,Angle3,Angle4]
        for i in Angles:
            if i == 0:
                continue
            # 角度が0じゃなかったら各頂点を回転
            RayVector = RX(RayVector,i)

        # Y回転
        Angle = self.Rotate.y
        # 角度を90度以下に分割
        Angle,Angle2,Angle3,Angle4 = Angle90(Angle)
        Angles = [Angle,Angle2,Angle3,Angle4]
        for i in Angles:
            if i == 0:
                continue
            # 角度が0じゃなかったら各頂点を回転
            RayVector = RY(RayVector,i)

        # Z回転
        Angle = self.Rotate.z
        # 角度を90度以下に分割
        Angle,Angle2,Angle3,Angle4 = Angle90(Angle)
        Angles = [Angle,Angle2,Angle3,Angle4]
        for i in Angles:
            if i == 0:
                continue
            # 角度が0じゃなかったら各頂点を回転
            RayVector = RZ(RayVector,i)

        return RayVector