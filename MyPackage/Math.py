# 三次元ベクトルクラス
class Vector3:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

# ベクトル同士の加算
def Add3(a,b):
    ans = Vector3(a.x + b.x, a.y+b.y, a.z+b.z)
    return ans

# ベクトル同士の引き算
def Sub3(a,b):
    ans = Vector3(a.x - b.x, a.y-b.y, a.z-b.z)
    return ans

# ベクトルのスカラー倍
def Multi3(a,b):
    ans = Vector3(a.x*b, a.y*b, a.z*b)
    return ans

# ベクトルとスカラーの割り算
def Div3(a,b):
    if b == 0:
        b = 0.1
    ans = Vector3(a.x/b, a.y/b, a.z/b)
    return ans

# 内積計算
def Dot3(a,b):
    return a.x*b.x + a.y*b.y + a.z*b.z

# 外積計算
def Cross3(a,b):
    ans = Vector3(
    a.y*b.z-a.z*b.y,
    a.z*b.x-a.x*b.z,
    a.x*b.y-a.y*b.x
    )
    return ans

# sin表
sinlist = [0,
           0.01, 0.03, 0.05, 0.06, 0.08,
           0.1, 0.12, 0.13, 0.15, 0.17,
           0.19, 0.20, 0.22, 0.24, 0.25,
           0.27, 0.29, 0.3, 0.32, 0.34,
           0.35, 0.37, 0.39, 0.4, 0.42,
           0.43, 0.45, 0.46, 0.48, 0.5,
           0.51, 0.52, 0.54, 0.55, 0.57,
           0.58, 0.6, 0.61, 0.62, 0.64,
           0.65, 0.66, 0.68, 0.69, 0.7,
           0.71, 0.73, 0.74, 0.75, 0.76,
           0.77, 0.78, 0.79, 0.8, 0.81,
           0.82, 0.83, 0.84, 0.85, 0.86,
           0.87, 0.88, 0.89, 0.89, 0.90,
           0.91, 0.92, 0.92, 0.93, 0.93,
           0.94, 0.95, 0.95, 0.96, 0.96,
           0.97, 0.97, 0.97, 0.98, 0.98,
           0.98, 0.99, 0.99, 0.99, 0.99,
           0.99, 0.99, 0.99, 0.99, 1]

# sinの値を返す関数
def sin(Angle):
    global sinlist
    return sinlist[Angle]

# cosの値を返す関数
def cos(Angle):
    global sinlist
    return sinlist[90-Angle]

# 回転量を90度以下に分割
def Angle90(Angle):
    Angle2,Angle3,Angle4 = 0,0,0
    # Angleをプラスにする
    while 1:
        if Angle < 0:
            Angle = Angle + 360
        else:break
    # Angleが0だったら何もしない
    if Angle == 0:
        return Angle,Angle2,Angle3,Angle4
    # Angleを分割
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
    return Angle,Angle2,Angle3,Angle4

# Xの回転行列を計算
def RX(Pos,Angle):
    if Angle == 0:
        return Pos
    NewPos = Vector3(Pos.x,
                     Pos.y*cos(Angle) + Pos.z*-1*sin(Angle),
                     Pos.y*sin(Angle) + Pos.z*cos(Angle))
    return NewPos

# Yの回転行列を計算
def RY(Pos,Angle):
    if Angle == 0:
        return Pos
    NewPos = Vector3(Pos.x*cos(Angle) + Pos.z*sin(Angle),
                     Pos.y,
                     Pos.x*-1*sin(Angle) + Pos.z*cos(Angle))
    return NewPos

# Zの回転行列を計算
def RZ(Pos,Angle):
    if Angle == 0:
        return Pos
    NewPos = Vector3(Pos.x*cos(Angle) + Pos.y*-1*sin(Angle),
                     Pos.x*sin(Angle) + Pos.y*cos(Angle),
                     Pos.z)
    return NewPos