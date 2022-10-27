from tkinter import *   # 파일 편집기를 사용할 수 잇는 라이브러리 선언
from tkinter.filedialog import *


# 이미지를 불러오는 함수 선언
def func_open():
    filename = askopenfilename(parent=window, filetypes=(("GIF파일", "*gif"), ("모든파일", "*.*")))
    photo = PhotoImage(file=filename)
    pLabel.config(image=photo)
    pLabel.image = photo

# 종료 함수 선언
def func_exit():
    window.quit()
    window.destroy()


window = Tk()  # window에 tk선언
window.geometry("500x500")  # 크기
window.title("사진 출력")    # 제목
photo = PhotoImage()        # 사진 출력
pLabel = Label(window, image=photo)  

pLabel.pack(expand=1, anchor=CENTER)   # 창은 하나, 가운데 정렬

mainMenu = Menu(window)  # 메뉴
window.config(menu=mainMenu)    #윈도우의 구성은 메인메뉴


fileMenu = Menu(mainMenu)   
mainMenu.add_cascade(label= "파일", menu=fileMenu)        # 상위 메뉴의 이름(큰 목록)
fileMenu.add_command(label="파일 열기", command=func_open)      # 함수 파일 열기  (하위 메뉴)

fileMenu.add_separator() # 칸 나누기
fileMenu.add_command(label="프로그램 종료", command=func_exit)  # 함수 파일 닫기   (하위 메뉴)
window.mainloop()





