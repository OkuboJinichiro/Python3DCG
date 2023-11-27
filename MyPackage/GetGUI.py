# 入力ボックスの値取得モジュール
# def GetOption(すべての入力ボックス):
    # データを受け取って戻り値で渡す
    # intやfloatに変換できないもの、使用できない範囲の数値はエラーで返す

def GetOption(ILL_Entry,WS_Entry,CPX_Entry,CPY_Entry,CPZ_Entry,FL_Entry,RX_Entry,RY_Entry,RZ_Entry,CRX_Entry,CRY_Entry,CRZ_Entry):
    # 各入力ボックスのデータを受け取る
    ILL = int(ILL_Entry.get())
    PixelSize = int(WS_Entry.get())
    FL = int(FL_Entry.get())
    CPX = float(CPX_Entry.get())
    CPY = float(CPY_Entry.get())
    CPZ = float(CPZ_Entry.get())
    RX = int(RX_Entry.get())
    RY = int(RY_Entry.get())
    RZ = int(RZ_Entry.get())
    CRX = int(CRX_Entry.get())
    CRY = int(CRY_Entry.get())
    CRZ = int(CRZ_Entry.get())

    # ILLとPixelSizeは0以下の場合エラーとする
    if ILL <= 0 or PixelSize <= 0:
        raise 

    return ILL,PixelSize,CPX,CPY,CPZ,FL,RX,RY,RZ,CRX,CRY,CRZ