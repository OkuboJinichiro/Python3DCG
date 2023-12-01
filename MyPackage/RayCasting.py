from .Math import *

def RayCast(Cam,face,RayX,RayY):
    # face ([0] = z [1] = y [2] = x [3] = 法線 [4] = 色)

    # 座標0にあるフェースの境目に当たらないようにする    
    if RayX == 0:
        RayX = RayX + 0.00001
    if RayY == 0:
        RayY = RayY + 0.00001

    RayHit = False

    # レイの方向と長さを計算
    Ray = Cam.RotateALL(Vector3(RayX, RayY ,Cam.FocalLength))
    RayVector = Multi3(Ray , Cam.RayLength)
    RayPos = Add3(Cam.Pos,RayVector)

    # フェースの一点からのベクトルを計算
    AtoCam = Sub3(Cam.Pos,face[0])
    AtoRay = Sub3(RayPos,face[0])
    # 法線との内積を計算
    CamDot = Dot3(face[3],AtoCam)
    RayDot = Dot3(face[3],AtoRay)

    # 法線とカメラの角度が90より大きかったら描画しない
    if CamDot < 0:
        return "None",None

    # レイがフェースの無限平面を貫通しているか
    if CamDot*RayDot <= 0:
        CamDotAbs = abs(CamDot)
        RayDotAbs = abs(RayDot)
        # 無限平面と交差する点を計算
        HitPoint = Div3(Add3(Multi3(Cam.Pos,RayDotAbs),Multi3(RayPos ,CamDotAbs)),RayDotAbs + CamDotAbs)
        
        # 外積で交差する点がフェースの内側にいるか判定
        RayHit = True
        for i in range(3):
            Edge = Sub3(face[(i+1)%3],face[i])
            itoHitPoint = Sub3(HitPoint,face[i])
            # 外積を計算
            ExH = Cross3(Edge,itoHitPoint)
            # 内積を計算
            ChackDot = Dot3(face[3],ExH)
            # 外積ベクトルが法線と逆向きだったらフェースの外にある
            if(ChackDot<0):
                RayHit = False
                break

    # return処理
    if RayHit:
        CtoH = Sub3(HitPoint,Cam.Pos)
        h = (CtoH.x*CtoH.x) +  (CtoH.y*CtoH.y) + (CtoH.z * CtoH.z)
        return face[4],h
    else:
        return "None",None