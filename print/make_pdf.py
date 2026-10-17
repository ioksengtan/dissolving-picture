from PIL import Image,ImageDraw,ImageFont
import math
u='/root/.claude/uploads/8de53d9a-267b-5a79-bccd-5262458cb891/'
S=300/2.54
def c(x):return int(round(x*S))
PW,PH=c(21),c(29.7)
def font(pt,b=False):return ImageFont.truetype('/usr/share/fonts/opentype/noto/NotoSansCJK-%s.ttc'%('Bold' if b else 'Regular'),int(pt*300/72))
def cover(p,w,h):
    im=Image.open(p).convert('RGB');s=max(w/im.width,h/im.height)
    im=im.resize((int(im.width*s)+1,int(im.height*s)+1),Image.LANCZOS)
    l=(im.width-w)//2;t=(im.height-h)//2;return im.crop((l,t,l+w,t+h))
A=cover(u+'beed938d-image.png',c(8),c(10.5))   # base: no dog
B=cover(u+'f8afd086-image.png',c(8),c(10.5))   # moving: dog
RED=(215,25,35);GREY=(150,150,150)
def poly(d,pts,ox,oy,col=RED,w=7,close=False):
    P=[(c(ox+x),c(oy+y)) for x,y in pts]
    if close:P.append(P[0])
    d.line(P,fill=col,width=w,joint='curve')
def dashed(d,pts,ox,oy,col=GREY,w=3):
    P=[(c(ox+x),c(oy+y)) for x,y in pts]+[(c(ox+pts[0][0]),c(oy+pts[0][1]))]
    for a,b in zip(P,P[1:]):
        L=math.hypot(b[0]-a[0],b[1]-a[1]);n=int(L//40)+1
        for i in range(n):
            t0=i*40/L;t1=min(1,(i*40+22)/L)
            d.line([(a[0]+(b[0]-a[0])*t0,a[1]+(b[1]-a[1])*t0),(a[0]+(b[0]-a[0])*t1,a[1]+(b[1]-a[1])*t1)],fill=col,width=w)
def T(d,x,y,s,pt=10,b=False,col=(50,50,50),a='la'):d.text((c(x),c(y)),s,font=font(pt,b),fill=col,anchor=a)
# ---- page 1 base piece (16 x 20 cm)
p1=Image.new('RGB',(PW,PH),'white');d=ImageDraw.Draw(p1)
ox,oy=2.5,5.0
p1.paste(A,(c(ox+4),c(oy+5)))
dashed(d,[(0,0),(16,0),(16,20),(0,20)],ox,oy)
for k in range(8):
    yk=5+1.5*k
    poly(d,[(3,yk+1.5),(4,yk),(12,yk),(14,yk-1.5)],ox,oy)
poly(d,[(14,3.5),(14,14)],ox,oy)
d.rectangle([c(ox+1.9),c(oy+9.5),c(ox+2.2),c(oy+15.5)],outline=RED,width=7)
T(d,10.5,1.4,'底座片 BASE PIECE（第一張圖）',15,True,a='ma')
T(d,10.5,2.4,'粗紅線＝裁切　圖面在 8×10.5 cm 區域內　印 A4・100% 比例',10,col=(90,90,90),a='ma')
T(d,10.5,3.2,'灰色虛線＝紙張邊界（16×20 cm，可不裁）',9,col=(130,130,130),a='ma')
T(d,10.5,26.6,'細長直槽（左）= 側邊槽，長 6 cm',9,col=(110,110,110),a='ma')
# ---- page 2 moving piece
p2=Image.new('RGB',(PW,PH),'white');d=ImageDraw.Draw(p2)
ox,oy=4.5,9.5
p2.paste(B,(c(ox+2),c(oy+4.5)))
body=[(0,0),(4,0),(4,-8),(8,-8),(8,0),(12,0),(12,4.5),(12.7,4.5),(12.7,7.5),(12,7.5),(12,16),(0,16),(0,12),(-0.75,12),(-0.75,9),(0,9)]
# white fill outside image, paper background
poly(d,body,ox,oy,close=True)
for k in range(7):
    sy=1.5+1.5*k
    poly(d,[(1,sy),(2,sy+1.5),(10,sy+3),(11,sy+4.5)],ox,oy)
T(d,ox+6,oy-4,'拉片',16,True,col=(90,90,90),a='mm')
d.line([(c(ox+6),c(oy-2.5)),(c(ox+6),c(oy-6.8))],fill=(90,90,90),width=8)
T(d,10.5,26.2,'移動片 MOVING PIECE（第二張圖）',15,True,a='ma')
T(d,10.5,27.1,'粗紅線＝裁切　圖面 8×10.5 cm　拉片至少 8 cm　印 A4・100% 比例',10,col=(90,90,90),a='ma')
T(d,10.5,27.8,'斜切只跨一格；左右凸出的小耳朵是紙上原有的形狀，不要剪掉',9,col=(130,130,130),a='ma')
# ---- page 3 instructions
p3=Image.new('RGB',(PW,PH),'white');d=ImageDraw.Draw(p3)
T(d,1.5,1.5,'溶解畫 組裝說明',20,True)
steps=['依 Reel（IG nell.hobbyart）的圖面與字幕整理。尺寸為 Reel 圖面上的手寫數字。',
'',
'1. 兩頁都印在 A4（100%）。底座片和移動片各用一張 A4。紙不要太薄，',
'    拉片部分建議對折加強（Reel：double over the paper）。',
'2. 底座片：沿粗紅線切出 8 條斜口橫切與右側直切，左側細槽也切開。',
'3. 移動片：沿外框紅線剪下（含拉片與兩側小耳朵），再沿 7 條斜線切開。',
'4. 把移動片穿過底座片的橫切口，拉片留在外面（框的外側）。',
'5. 用膠帶把底座片鬆開的紙片黏牢，但不要蓋住紙需要滑動穿過的地方（Reel 字幕）。',
'6. 拉動拉片，畫面從第一張圖換成第二張圖。',
'',
'注意：Reel 沒有拍出每一步的穿法細節（紙條穿過哪幾個切口、正反面），',
'上面第 4 步是依字幕和成品照片整理，實際穿法請對照 Reel 的第 5～8 張截圖，',
'建議先用影印紙試做一次再用正式圖。']
y=3.2
for s in steps:
    T(d,1.5,y,s,11);y+=0.85
d.text((c(10.5),c(21)),'一開始 (第一張圖)　　　拉動後 (第二張圖)',font=font(11),fill=(70,70,70),anchor='mm')
th1=cover(u+'beed938d-image.png',c(5),c(6.6));th2=cover(u+'f8afd086-image.png',c(5),c(6.6))
p3.paste(th1,(c(3.2),c(22)));p3.paste(th2,(c(12.8),c(22)))
# ---- page 4 optional frame
p4=Image.new('RGB',(PW,PH),(59,35,21));d=ImageDraw.Draw(p4)
for y in range(0,PH,c(0.35)):d.line([(0,y),(PW,y)],fill=(66,40,25),width=2)
wx,wy=6.5,9.0
d.rectangle([c(wx),c(wy),c(wx+8),c(wy+10.5)],fill='white');
poly(d,[(wx,wy),(wx+8,wy),(wx+8,wy+10.5),(wx,wy+10.5)],0,0,close=True,w=6)
sx0,sx1=wx+2,wx+6
d.rectangle([c(sx0-0.2),c(wy-2.3),c(sx1+0.2),c(wy-1.8)],fill='white')
poly(d,[(sx0-0.2,wy-2.3),(sx1+0.2,wy-2.3),(sx1+0.2,wy-1.8),(sx0-0.2,wy-1.8)],0,0,close=True,w=5)
T(d,10.5,2.0,'外框（選用）',15,True,col=(235,215,190),a='ma')
T(d,10.5,3.0,'依 Reel 的外框概念：窗 8×10.5 cm，上方開一條細縫讓拉片穿出',10,col=(210,185,160),a='ma')
T(d,10.5,3.8,'底座片疊在框後方，圖面對準窗；窗位置為我自己安排，不是 Reel 圖面標示',9,col=(190,165,140),a='ma')
T(d,10.5,24.5,'印在厚卡紙。沿紅線切掉白色的窗與上方細縫。',10,col=(210,185,160),a='ma')
p1.save('dissolving-picture-A4.pdf','PDF',resolution=300,save_all=True,append_images=[p2,p3,p4])
for i,p in enumerate([p1,p2,p3,p4],1):p.resize((PW//4,PH//4)).save('q%d.jpg'%i)
