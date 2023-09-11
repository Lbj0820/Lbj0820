from openpyxl import Workbook
from openpyxl.drawing.image import image
wb = Workbook()
ws = wb.active

# 절대경로 지정
img = image("sample_img.png")
# 절대경로 지정
# img = image("img/sample_img.png")


#c3 위치에 img.png 파일으 이미지를 삼입
ws.add_image(img, "C3")