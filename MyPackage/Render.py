from .Math import *
from .RayCasting import *
import tkinter as tk

# レンダリング関数
def Rendering(canvas,WindowSize,Cam,Obj,ILL):
    canvas.delete("all")
    MaxX = int(WindowSize.x/WindowSize.z)
    MaxY = int(WindowSize.y/WindowSize.z)
    # 各ピクセルごとにチェック
    for y in range(MaxY):
        # 走査線を指定された数スキップ
        if y % ILL == 0:
            for x in range(MaxX):
                # どのフェースとも当たらなかったときの色
                Color = "black"
                # Zバッファ用
                FrontFacePos = 99999999
                
                # 各フェースをチェック
                for f in Obj.faces:
                    HitColor,HitPos = RayCast(Cam, f, -1*(WindowSize.x/20) + (x*(WindowSize.x/MaxX/10)), (WindowSize.y/20)- (y*(WindowSize.y/MaxY/10)))
                    # HitColorがNoneの時はフェースに当たってない
                    if HitColor != "None":
                        # 当たったフェースが一番手前ならフェースの色を入れる
                        if HitPos < FrontFacePos:
                            FrontFacePos = HitPos
                            Color = HitColor
                # 描画
                canvas.create_rectangle(x*WindowSize.z,y*WindowSize.z,x*WindowSize.z+WindowSize.z,y*WindowSize.z+WindowSize.z,fill=Color,width=0)