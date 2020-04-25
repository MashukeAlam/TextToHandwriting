from tkinter import *
from PIL import Image
import os, os.path
import random
from color_process import Color_Process

_STR_TYPE = ""
end = 0
paper_a4 = Image.new(mode = "RGB", size = (2480, 3508), color=(255, 255, 255))

letter_range = {}
for i in range(26):
    curr_char = chr(65 + i)
    DIR = os.getcwd() + "\\Letters\\" + curr_char + "\\"
    num = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    letter_range[curr_char] = num


root = Tk(className="Handwriter")
root.geometry("300x100")

e = Entry(root, width=100)
e.pack()

def whiten_image():
    global paper_a4
    global _STR_TYPE

    for i in range(paper_a4.size[0]):
        for j in range(paper_a4.size[1]):
            if j > 240:
                break
            if Color_Process().dark_or_what(paper_a4.getpixel((i, j))): paper_a4.putpixel((i, j), (0, 0, 0))
            else: paper_a4.putpixel((i, j), (255, 255, 255))


def writing_on_paper() -> int:
    global _STR_TYPE
    global paper_a4
    startX = 60
    startY = 60
    for c in _STR_TYPE:
        if c == " " :
            startX += 50
            continue
        if c >= "A" and c <= "Z":
            curr_char_img = Image.open(os.getcwd() + "\\Letters\\" + c + ".png")
            curr_char_img = curr_char_img.resize((124, 124))
            paper_a4.paste(curr_char_img, (startX, startY))
        elif c >= "0" and c <= "9":
                curr_char_img = Image.open(os.getcwd() + "\\Letters\\" + c + ".png")
                curr_char_img = curr_char_img.resize((124, 124))
                paper_a4.paste(curr_char_img, (startX, startY))
        else:
            cap_c = c.upper()
            curr_char_img = Image.open(os.getcwd() + "\\Letters\\" + cap_c + "\\" + c + " (" + str(random.randint(1, letter_range[cap_c])) + ").png")
            curr_char_img = curr_char_img.resize((105, 105))
            paper_a4.paste(curr_char_img, (startX, startY + (124 - 105)))

        startX += curr_char_img.size[0]
        # startY += curr_char_img.size[1]


        if startX > 2400:
            startX = 45
            startY += 124 + 60
    return startY

def get_text():
    global _STR_TYPE
    global end
    _STR_TYPE = e.get()
    root.destroy()
    end = writing_on_paper()
sub_btn = Button(root, text="Convert to Handwritten Document", command=get_text)
sub_btn.pack()
root.mainloop()






whiten_image()
paper_a4.save("F:\\final.png")
paper_a4.show()

