import tkinter as tk

# ウィンドウの初期化関数
def WindowMaker(WinX,WinY):
    # ウィンドウの設定
    root = tk.Tk()
    root.title("3DCG")
    root.geometry(str(WinX) + "x" + str(WinY+200))
    root.resizable(width=False, height=False)
    
    # レンダリング画面とボタン等を置く親キャンパス
    BG_Frame = tk.Frame(root,bg="White")
    BG_Frame.pack(fill=tk.BOTH,expand=True)
    
    # レンダリング画面のキャンパス
    canvas = tk.Canvas(BG_Frame,bg="black",width= WinX,height=WinY)
    canvas.pack(side=tk.TOP)

    # rootとキャンパスを返す
    return root,canvas,BG_Frame

# GUIの初期化関数
def GUIMaker(BG_Frame,WS,ILL,CP,FL):
    # レンダリングボタンの設定
    RenderingButton = tk.Button(BG_Frame,text="レンダリング\n(Enter)",
                                font=("MS明朝","20","bold"),
                                bg="Red",activebackground="darkred",
                                relief="solid",padx=10,pady=60)
    RenderingButton.pack(side=tk.RIGHT,padx=10)

    BOXPos = 40
    SubPos = 125

    # 画質設定入力ボックス
    RenXPos = 10
    RenT_text = tk.Label(text="画質設定",bg="white",anchor=tk.W,font=("MS明朝","12","bold"))
    RenT_text.place(x=RenXPos, y=WS.y+10,width=200)
    Rensub_text = tk.Label(text="※レンダリング時間に影響があります",bg="white",anchor=tk.W,font=("MS明朝","8"))
    Rensub_text.place(x=RenXPos, y=WS.y+SubPos,width=200)

    ILL_text = tk.Label(text="走査線間隔：",bg="white",anchor=tk.W,font=("MS明朝","10"))
    ILL_text.place(x=RenXPos, y=WS.y+BOXPos,width=200)
    ILL_Entry = tk.Entry(bg="#F0F0F0",width=10)
    ILL_Entry.place(x=RenXPos+95, y=WS.y+BOXPos)
    ILL_Entry.insert(index=tk.END,string=ILL)

    WS_text = tk.Label(text="ピクセルサイズ：",bg="white",anchor=tk.W,font=("MS明朝","10"))
    WS_text.place(x=RenXPos, y=WS.y+BOXPos+20,width=200)
    WS_Entry = tk.Entry(bg="#F0F0F0",width=10)
    WS_Entry.place(x=RenXPos+95, y=WS.y+BOXPos+20)
    WS_Entry.insert(index=tk.END,string=WS.z)

    # カメラ設定入力ボックス
    CamXPos = RenXPos+200
    CT_text = tk.Label(text="カメラ設定",bg="white",anchor=tk.W,font=("MS明朝","12","bold"))
    CT_text.place(x=CamXPos, y=WS.y+10,width=200)
    Csub_text = tk.Label(text="※ワールド軸で計算します",bg="white",anchor=tk.W,font=("MS明朝","8"))
    Csub_text.place(x=CamXPos, y=WS.y+SubPos,width=400)

    CPX_text = tk.Label(text="X座標：",bg="white",anchor=tk.W,font=("MS明朝","10"))
    CPX_text.place(x=CamXPos, y=WS.y+BOXPos,width=200)
    CPX_Entry = tk.Entry(bg="#F0F0F0",width=10)
    CPX_Entry.place(x=CamXPos +85, y=WS.y+BOXPos)
    CPX_Entry.insert(index=tk.END,string=CP.x)

    CPY_text = tk.Label(text="Y座標：",bg="white",anchor=tk.W,font=("MS明朝","10"))
    CPY_text.place(x=CamXPos, y=WS.y+BOXPos+20,width=200)
    CPY_Entry = tk.Entry(bg="#F0F0F0",width=10)
    CPY_Entry.place(x=CamXPos +85, y=WS.y+BOXPos+20)
    CPY_Entry.insert(index=tk.END,string=CP.y)

    CPZ_text = tk.Label(text="Z座標：",bg="white",anchor=tk.W,font=("MS明朝","10"))
    CPZ_text.place(x=CamXPos, y=WS.y+BOXPos+40,width=200)
    CPZ_Entry = tk.Entry(bg="#F0F0F0",width=10)
    CPZ_Entry.place(x=CamXPos +85, y=WS.y+BOXPos+40)
    CPZ_Entry.insert(index=tk.END,string=CP.z)

    FL_text = tk.Label(text="焦点距離：",bg="white",anchor=tk.W,font=("MS明朝","10"))
    FL_text.place(x=CamXPos, y=WS.y+BOXPos+60,width=200)
    FL_Entry = tk.Entry(bg="#F0F0F0",width=10)
    FL_Entry.place(x=CamXPos +85, y=WS.y+BOXPos+60)
    FL_Entry.insert(index=tk.END,string=FL)

    # カメラ回転
    CamRXPos = CamXPos + 165
    CRX_text = tk.Label(text="X軸回転：",bg="white",anchor=tk.W,font=("MS明朝","10"))
    CRX_text.place(x=CamRXPos, y=WS.y+BOXPos,width=200)
    CRX_Entry = tk.Entry(bg="#F0F0F0",width=10)
    CRX_Entry.place(x=CamRXPos +70, y=WS.y+BOXPos)
    CRX_Entry.insert(index=tk.END,string="0")

    CRY_text = tk.Label(text="Y軸回転：",bg="white",anchor=tk.W,font=("MS明朝","10"))
    CRY_text.place(x=CamRXPos, y=WS.y+BOXPos+20,width=200)
    CRY_Entry = tk.Entry(bg="#F0F0F0",width=10)
    CRY_Entry.place(x=CamRXPos +70, y=WS.y+BOXPos+20)
    CRY_Entry.insert(index=tk.END,string="0")

    CRZ_text = tk.Label(text="Z軸回転：",bg="white",anchor=tk.W,font=("MS明朝","10"))
    CRZ_text.place(x=CamRXPos, y=WS.y+BOXPos+40,width=200)
    CRZ_Entry = tk.Entry(bg="#F0F0F0",width=10)
    CRZ_Entry.place(x=CamRXPos +70, y=WS.y+BOXPos+40)
    CRZ_Entry.insert(index=tk.END,string="0")


    # 回転情報入力ボックス
    ObjectRotatePos = CamRXPos + 175
    Rtitle_text = tk.Label(text="オブジェクト",bg="white",anchor=tk.W,font=("MS明朝","12","bold"))
    Rtitle_text.place(x=ObjectRotatePos, y=WS.y+10,width=150)
    Rsub_text = tk.Label(text="※ X→Y→Zの順に計算されます",bg="white",anchor=tk.W,font=("MS明朝","8"))
    Rsub_text.place(x=ObjectRotatePos, y=WS.y+SubPos,width=150)

    RX_text = tk.Label(text="X軸回転：",bg="white",anchor=tk.W,font=("MS明朝","10"))
    RX_text.place(x=ObjectRotatePos, y=WS.y+BOXPos,width=150)
    RX_Entry = tk.Entry(bg="#F0F0F0",width=10)
    RX_Entry.place(x=ObjectRotatePos + 65, y=WS.y+BOXPos)
    RX_Entry.insert(index=tk.END,string="0")

    RY_text = tk.Label(text="Y軸回転：",bg="white",anchor=tk.W,font=("MS明朝","10"))
    RY_text.place(x=ObjectRotatePos, y=WS.y+BOXPos+20,width=150)
    RY_Entry = tk.Entry(bg="#F0F0F0",width=10)
    RY_Entry.place(x=ObjectRotatePos + 65, y=WS.y+BOXPos+20)
    RY_Entry.insert(index=tk.END,string="0")

    RZ_text = tk.Label(text="Z軸回転：",bg="white",anchor=tk.W,font=("MS明朝","10"))
    RZ_text.place(x=ObjectRotatePos, y=WS.y+BOXPos+40,width=150)
    RZ_Entry = tk.Entry(bg="#F0F0F0",width=10)
    RZ_Entry.place(x=ObjectRotatePos + 65, y=WS.y+BOXPos+40)
    RZ_Entry.insert(index=tk.END,string="0")

    text = tk.Label(text="※レンダリングボタンを押して下さい",font=("MS明朝","12","bold"),bg="white",anchor=tk.W)
    text.place(x=RenXPos, y=WS.y+170,width=550)

    # すべてのGUIを返す
    return RenderingButton,ILL_Entry,WS_Entry,CPX_Entry,CPY_Entry,CPZ_Entry,FL_Entry,RX_Entry,RY_Entry,RZ_Entry,text,CRX_Entry,CRY_Entry,CRZ_Entry


# ウィンドウサイズを設定できるウィンドウ
def StartWindow():
    WindowOptionRoot = tk.Tk()
    WindowOptionRoot.title("ウィンドウ設定")
    WindowOptionRoot.geometry("300x150")

    # 行ごとにフレームを作成
    BoxFlame = tk.Frame(width=50)
    ButtonFlame = tk.Frame(width=30)

    # 説明文
    text = tk.Label(text="ウィンドウサイズを指定してください\n(幅1000px以上 高さ600px以上)")
    # 幅設定
    WinX_text = tk.Label(BoxFlame,text="幅：")
    WinX_Entry = tk.Entry(BoxFlame,width=3,justify="right")
    WinX_Entry.insert(index=tk.END,string="10")
    WinX_00 = tk.Label(BoxFlame,text="00px")
    # 高さ設定
    WinY_text = tk.Label(BoxFlame,text="高さ：")
    WinY_Entry = tk.Entry(BoxFlame,width=3,justify="right")
    WinY_Entry.insert(index=tk.END,string="7")
    WinY_00 = tk.Label(BoxFlame,text="00px")
    # 決定ボタン
    Button = tk.Button(ButtonFlame,text="決定")
    Error = tk.Label(ButtonFlame,text=" ")

    # ウィジットの配置
    text.place(rely=0.1,relx=0.5,anchor=tk.N)
    WinX_text.grid(column=0,row=0,padx=3)
    WinX_Entry.grid(column=1,row=0)
    WinX_00.grid(column=2,row=0)
    WinY_text.grid(column=3,row=0,padx=3)
    WinY_Entry.grid(column=4,row=0)
    WinY_00.grid(column=5,row=0)
    BoxFlame.place(relx=0.5,rely=0.5,anchor=tk.N)
    Button.grid(column=0,row=2, padx=5)
    Error.grid(column=1,row=2, padx=5)
    ButtonFlame.place(relx=0.5,rely=0.9,anchor=tk.S)

    return WindowOptionRoot,WinX_Entry,WinY_Entry,Button,Error