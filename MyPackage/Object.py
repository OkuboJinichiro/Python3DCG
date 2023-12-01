try:
    from .Math import *
except:
    from Math import *

class OBJ:
    def __init__(self):
        # オブジェクトの頂点
        self.posA = Vector3(0,35,0)
        self.posB = Vector3(0,0,-25)
        self.posC = Vector3(-25,0,25)
        self.posD = Vector3(25,0,25)

        # Z軸のグリッドの頂点
        FloorY = 0
        self.posF1A = Vector3(-50,FloorY,-100)
        self.posF1B = Vector3(-55,FloorY,100)
        self.posF1C = Vector3(-50,FloorY,100)

        self.posF2A = Vector3(50,FloorY,-100)
        self.posF2B = Vector3(45,FloorY,100)
        self.posF2C = Vector3(50,FloorY,100)

        self.posF3A = Vector3(2,FloorY,-100)
        self.posF3B = Vector3(-3,FloorY,100)
        self.posF3C = Vector3(2,FloorY,100)

        # X軸のグリッドの頂点
        self.posFX1A = Vector3(100,FloorY,2)
        self.posFX1B = Vector3(-100,FloorY,-3)
        self.posFX1C = Vector3(-100,FloorY,2)

        self.posFX2A = Vector3(100,FloorY,50)
        self.posFX2B = Vector3(-100,FloorY,50)
        self.posFX2C = Vector3(-100,FloorY,55)

        self.posFX3A = Vector3(100,FloorY,-50)
        self.posFX3B = Vector3(-100,FloorY,-50)
        self.posFX3C = Vector3(-100,FloorY,-45)
  
        # オブジェクトのフェースの情報
        self.face1_N = Cross3(Sub3(self.posB,self.posA),Sub3(self.posC,self.posA))
        self.face1 = [self.posA, self.posB, self.posC, self.face1_N, "#FFFFFF"]
        self.face2_N = Cross3(Sub3(self.posD,self.posA),Sub3(self.posB,self.posA))
        self.face2 = [self.posA, self.posD, self.posB, self.face2_N, "#FF0000"]
        self.face3_N = Cross3(Sub3(self.posD,self.posB),Sub3(self.posC,self.posB))
        self.face3 = [self.posB, self.posD, self.posC, self.face3_N, "#00FF00"]
        self.face4_N = Cross3(Sub3(self.posC,self.posA),Sub3(self.posD,self.posA))
        self.face4 = [self.posA, self.posC, self.posD, self.face4_N, "#0000FF"]

        # Z軸のグリッドのフェースの情報
        self.faceF1_N = Cross3(Sub3(self.posF1B,self.posF1A),Sub3(self.posF1C,self.posF1A))
        self.faceF1 = [self.posF1A, self.posF1B, self.posF1C, self.faceF1_N, "#F0F0F0"]
        self.faceF2_N = Cross3(Sub3(self.posF2B,self.posF2A),Sub3(self.posF2C,self.posF2A))
        self.faceF2 = [self.posF2A, self.posF2B, self.posF2C, self.faceF2_N, "#F0F0F0"]
        self.faceF3_N = Cross3(Sub3(self.posF3B,self.posF3A),Sub3(self.posF3C,self.posF3A))
        self.faceF3 = [self.posF3A, self.posF3B, self.posF3C, self.faceF3_N, "#F0F0F0"]

        # X軸のグリッドのフェースの情報
        self.faceFX1_N = Cross3(Sub3(self.posFX1B,self.posFX1A),Sub3(self.posFX1C,self.posFX1A))
        self.faceFX1 = [self.posFX1A, self.posFX1B, self.posFX1C, self.faceFX1_N, "#F0F0F0"]
        self.faceFX2_N = Cross3(Sub3(self.posFX2B,self.posFX2A),Sub3(self.posFX2C,self.posFX2A))
        self.faceFX2 = [self.posFX2A, self.posFX2B, self.posFX2C, self.faceFX2_N, "#F0F0F0"]
        self.faceFX3_N = Cross3(Sub3(self.posFX3B,self.posFX3A),Sub3(self.posFX3C,self.posFX3A))
        self.faceFX3 = [self.posFX3A, self.posFX3B, self.posFX3C, self.faceFX3_N, "#F0F0F0"]

        # すべてのフェースのリスト
        self.faces = [self.face1, self.face2,self.face3,self.face4,self.faceF1,self.faceF2,self.faceF3,self.faceFX1,self.faceFX2,self.faceFX3]

    # オブジェクトを回転
    def RotateALL(self,AngleX,AngleY,AngleZ):
        # X回転
        # 角度を90度以下に分割
        Angle,Angle2,Angle3,Angle4 = Angle90(AngleX)
        Angles = [Angle,Angle2,Angle3,Angle4]
        # 回転処理
        for i in Angles:
            if i == 0:
                continue
            # 角度が0じゃなかったら各頂点を回転
            self.posA = RX(self.posA,i)
            self.posB = RX(self.posB,i)
            self.posC = RX(self.posC,i)
            self.posD = RX(self.posD,i)

        # Y回転
        # 角度を90度以下に分割
        Angle,Angle2,Angle3,Angle4 = Angle90(AngleY)
        Angles = [Angle,Angle2,Angle3,Angle4]
        # 回転処理
        for i in Angles:
            if i == 0:
                continue
            # 角度が0じゃなかったら各頂点を回転
            self.posA = RY(self.posA,i)
            self.posB = RY(self.posB,i)
            self.posC = RY(self.posC,i)
            self.posD = RY(self.posD,i)

        # Z回転
        # 角度を90度以下に分割
        Angle,Angle2,Angle3,Angle4 = Angle90(AngleZ)
        Angles = [Angle,Angle2,Angle3,Angle4]
        # 回転処理
        for i in Angles:
            if i == 0:
                continue
            # 角度が0じゃなかったら各頂点を回転
            self.posA = RZ(self.posA,i)
            self.posB = RZ(self.posB,i)
            self.posC = RZ(self.posC,i)
            self.posD = RZ(self.posD,i)

        # フェース情報を更新
        self.face1_N = Cross3(Sub3(self.posB,self.posA),Sub3(self.posC,self.posA))
        self.face1 = [self.posA, self.posB, self.posC, self.face1_N, "#FFFFFF"]
        self.face2_N = Cross3(Sub3(self.posD,self.posA),Sub3(self.posB,self.posA))
        self.face2 = [self.posA, self.posD, self.posB, self.face2_N, "#FF0000"]
        self.face3_N = Cross3(Sub3(self.posD,self.posB),Sub3(self.posC,self.posB))
        self.face3 = [self.posB, self.posD, self.posC, self.face3_N, "#00FF00"]
        self.face4_N = Cross3(Sub3(self.posC,self.posA),Sub3(self.posD,self.posA))
        self.face4 = [self.posA, self.posC, self.posD, self.face4_N, "#0000FF"]

        self.faces[0:4] = [self.face1, self.face2,self.face3,self.face4]