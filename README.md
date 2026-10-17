# 溶解畫 (dissolving picture)

靈感：IG nell.hobbyart「Make your own dissolving picture」。

## 內容
- `index.html` — 單檔網頁模擬器，圖片已內嵌（base64），直接開啟即可。向上拖黃色拉片換圖。
  預設圖：沒有狗 → 有狗；頁面上可上傳自己的兩張圖。
- `assets/A-no-dog.jpg`、`assets/B-dog.jpg` — 預設兩張圖原檔（插畫版）。
- `print/dissolving-picture-A4.pdf` — A4 列印版（100% 比例）：
  1. 底座片（第一張圖＝沒有狗）
  2. 移動片（第二張圖＝有狗）
  3. 組裝說明
  4. 外框（選用）
- `print/make_pdf.py` — 產生 PDF 的 Python 腳本（需要 Pillow 與 Noto Sans CJK 字型；圖片路徑需自行改）。

## 列印版的來源與限制
切線與尺寸照 Reel 的兩張圖面描出：底座片 16×20 cm、移動片 12×16 cm 加 ≥8 cm 拉片、
7 條 × 1.5 cm、圖面 8×10.5 cm。座標是我從截圖量的，可能有約 1～2 mm 誤差。
Reel 沒有拍出完整穿法，組裝步驟依字幕和成品截圖整理，建議先用影印紙試做。
外框頁是我自己安排的選用頁，不是 Reel 圖面標示。

## 網頁模擬器的限制
網頁的換圖動作是外觀模擬（每條各自上下滑動），不是 Reel 紙條機構的力學模型。

## 2026-10-17 尺寸更新
列印版尺寸已改為依照原作者（Instagram nell.hobbyart）手繪模板截圖上的標示數字：
- 底座片：寬 18 cm（左 2＋1＋2 cm、圖面 8 cm、右 2＋1＋2 cm），高 20 cm（上 3.5 cm、9 列各 1.5 cm、下 3 cm）；左斜切寬 2 cm，右斜切寬 2 cm，右直切位於 15 cm。
- 移動片：與模板一致（寬 12 cm、高 16 cm、拉片 4×8 cm、10 列各 1.5 cm＋底 1 cm、側邊凸耳 4.5～7.5 cm 與 9～12 cm）。
- make_pdf.py 的圖片路徑改為讀取本儲存庫的 assets/。
仍然沒有實際印出來剪貼試做過；側邊凸耳的寬度與右側邊距在截圖上看不清，為推估值。
