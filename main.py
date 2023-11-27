import tkinter as tk # GUI作成用
import time # 時間計測用
from MyPackage import WindowMaker,StartWindow,Rendering,Vector3,Camera,OBJ,GUIMaker,GetOption

RenderingNow = False

def main():
# ===== 初期化処理 =====
    ILL = 2 # 走査線間隔
    WS = Vector3(1000,500,4) # 幅,高さ,ピクセルサイズ
    MCam = Camera(Pos=Vector3(0,25,-100),RayLength=150,FocalLength = 60)
    MainOBJ = OBJ()

    # ウィンドウサイズの設定用ウィンドウ
    WindowOptionRoot,WinX_Entry,WinY_Entry,Button,Error = StartWindow()
    class MyException(Exception):
        pass # 入力されたサイズに対するエラー
    def GetButton():
        try:
            inx = int(WinX_Entry.get()) * 100
            iny = (int(WinY_Entry.get()) * 100)
            if inx < 1000:
                raise MyException("幅が小さすぎます")
            elif iny < 600:
                raise MyException("高さが小さすぎます")
            WS.x = inx
            WS.y = iny - 200
            WindowOptionRoot.destroy()
        except MyException as e:
            Error["text"] = e
        except:
            Error["text"] = "入力エラー"
    Button["command"] = GetButton
    WindowOptionRoot.mainloop()

    # メインのウィンドウを作成
    root,canvas,BG_canvas = WindowMaker(WS.x,WS.y)
    RenderingButton,ILL_Entry,WS_Entry,CPX_Entry,CPY_Entry,CPZ_Entry,FL_Entry,RX_Entry,RY_Entry,RZ_Entry,text,CRX_Entry,CRY_Entry,CRZ_Entry = GUIMaker(BG_canvas,WS,ILL,MCam.Pos,MCam.FocalLength)

# ===== レンダリングボタンの処理 =====
    def RenderingButtonDown(event = "NULL"):
        global RenderingNow
        if not RenderingNow:
            RenderingNow = True
            text["text"] = "※レンダリング中..."
            RenderingButton["state"] = tk.DISABLED
            RenderingButton["bg"] = "#505050"
            root.after(50,Render)
    def Render():
        # 入力された数字を受け取る
        try:
            ILL,WS.z,MCam.Pos.x,MCam.Pos.y,MCam.Pos.z,MCam.FocalLength,RX,RY,RZ,MCam.Rotate.x,MCam.Rotate.y,MCam.Rotate.z = GetOption(ILL_Entry,WS_Entry,CPX_Entry,CPY_Entry,CPZ_Entry,FL_Entry,RX_Entry,RY_Entry,RZ_Entry,CRX_Entry,CRY_Entry,CRZ_Entry)
        except:
            text["text"] = "※入力エラー:「Readme.txt」を読み適切な数字を入力してください"
            root.after(1000,RenderingButtonCT)
            return

        # オブジェクトを回転
        if RX!=0:MainOBJ.RotateX(Angle=RX)
        if RY!=0:MainOBJ.RotateY(Angle=RY)
        if RZ!=0:MainOBJ.RotateZ(Angle=RZ)

        # レンダリング
        start = time.time()
        Rendering(canvas,WS,MCam,MainOBJ,ILL = ILL)
        RenTime = time.time() - start
        text["text"] = "※レンダリング時間:" + str(round(RenTime,2)) + "秒"

        # 回転の入力ボックスをクリア
        RX_Entry.delete(0,tk.END)
        RX_Entry.insert(tk.END,"0")
        RY_Entry.delete(0,tk.END)
        RY_Entry.insert(tk.END,"0")
        RZ_Entry.delete(0,tk.END)
        RZ_Entry.insert(tk.END,"0")

        # ボタンを復活
        root.after(round(RenTime*700),RenderingButtonCT)
    def RenderingButtonCT():
        global RenderingNow
        RenderingButton["state"] = tk.NORMAL
        RenderingButton["bg"] = "red"
        RenderingNow = False
    RenderingButton["command"] = RenderingButtonDown
    root.bind("<Return>",func=RenderingButtonDown)

    root.mainloop()

if __name__ == "__main__":
    main()