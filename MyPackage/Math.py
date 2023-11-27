# ベクトルの定義と計算をするモジュール
# class Vector3:
    # 三次元ベクトルの構造体
# Add3(),Sub3(),Multi3(),Div():
    # 三次元ベクトルの四則演算(Multiはスカラー倍)
# Dot3(),Cross3():
    # 内積、外積の計算
# sin(),cos():
    # 角度を引数として受け取り、三角関数の値を返す(10度単位)
# RX(),RY(),RZ():
    # 引数の頂点をワールド軸で回転させて返す

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

# sinの値を返す関数
def sin(Angle):
    A = round(Angle,-1)
    if A == 0:
        return 0
    elif A == 10:
        return 0.17
    elif A == 20:
        return 0.34
    elif A == 30:
        return 0.5
    elif A == 40:
        return 0.64
    elif A == 50:
        return 0.76
    elif A == 60:
        return 0.86
    elif A == 70:
        return 0.93
    elif A == 80:
        return 0.98
    elif A == 90:
        return 1

# cosの値を返す関数
def cos(Angle):
    A = round(Angle,-1)
    if A == 0:
        return 1
    elif A == 10:
        return 0.98
    elif A == 20:
        return 0.93
    elif A == 30:
        return 0.86
    elif A == 40:
        return 0.76
    elif A == 50:
        return 0.64
    elif A == 60:
        return 0.5
    elif A == 70:
        return 0.34
    elif A == 80:
        return 0.17
    elif A == 90:
        return 0

# Xの回転行列を計算
def RX(Pos,Angle):
    NewPos = Vector3(Pos.x,
                     Pos.y*cos(Angle) + Pos.z*-1*sin(Angle),
                     Pos.y*sin(Angle) + Pos.z*cos(Angle))
    return NewPos

# Yの回転行列を計算
def RY(Pos,Angle):
    NewPos = Vector3(Pos.x*cos(Angle) + Pos.z*sin(Angle),
                     Pos.y,
                     Pos.x*-1*sin(Angle) + Pos.z*cos(Angle))
    return NewPos

# Zの回転行列を計算
def RZ(Pos,Angle):
    NewPos = Vector3(Pos.x*cos(Angle) + Pos.y*-1*sin(Angle),
                     Pos.x*sin(Angle) + Pos.y*cos(Angle),
                     Pos.z)
    return NewPos