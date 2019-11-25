import cv2

project_root = '/Users/tao/Documents/GitHub/1st-DL-CVMarathon/homework/' 
img_path = 'data/lena.png'
img_path = project_root+img_path
print(img_path)

# 以彩色圖片的方式載入
img = cv2.imread(img_path, cv2.IMREAD_COLOR)

# 以灰階圖片的方式載入
img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# 為了要不斷顯示圖片，所以使用一個迴圈
while True:
    # 顯示彩圖
    cv2.imshow('bgr', img)
    # 顯示灰圖
    cv2.imshow('gray', img_gray)

    # 直到按下 ESC 鍵才會自動關閉視窗結束程式
    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        break