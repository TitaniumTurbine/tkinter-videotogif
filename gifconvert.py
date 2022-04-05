#video to gif (challenge 60)
#the module moviepy is required for this to work
#ImageMagick also needs to be installed

#import modules
from tkinter import *
from tkinter import filedialog
from moviepy.editor import *

#tell moviepy where the imagemagick software is located
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.0.10-Q16\magick.exe"})


def time_symetrize(clip):
    return concatenate([clip, clip.fx( vfx.time_mirror )])

#gif creation procedure
#collects all of the settings the user has set and uses them to convert the video into a gif the way that they have chosen
#is run whenever the user clicks the "Create Gif" button
def createGif():
    #collect settings
    F = gui.filename
    sizeval = gifScale.get()
    speedval = gifSpeed.get()
    textval = int(textSize.get())
    name = gifName.get()
    startM = gifStartM.get()
    endM = gifEndM.get()
    startS = gifStartS.get()
    endS = gifEndS.get()
    framerate = int(giffps.get())
    font = textFont.get()
    top = topText.get()
    middle = middleText.get()
    bottom = bottomText.get()
    tcolour = textColour.get()
    tS = tSvar.get()
    #set where the clip starts and ends, set the resolution as a percentage of the original, set the playback speed as a percentage of the original
    clip = (VideoFileClip(F).subclip((int(startM),float(startS)),(int(endM),float(endS)))).resize(float(float(sizeval)/100)).speedx(float(float(speedval)/100))
    if tS == 1:
        #make the clip with time symmetry
        clip = (VideoFileClip(F).subclip((int(startM),float(startS)),(int(endM),float(endS)))).resize(float(float(sizeval)/100)).speedx(float(float(speedval)/100)).fx(time_symetrize)

    #add text to the clip
    if font != "" and textval != "":
        if top != "":
            #add the top text to the top of the clip
            text = TextClip(top, fontsize=textval, font=font, color=(str(tcolour))).set_pos(("top")).set_duration(clip.duration)
            clip = CompositeVideoClip([clip, text])
        if middle != "":
            #add the middle text to the middle of the clip
            text = TextClip(middle, fontsize=textval, font=font, color=(str(tcolour))).set_pos(("center")).set_duration(clip.duration)
            clip = CompositeVideoClip([clip, text])
        if bottom != "":
            #add the bottom text to the bottom of the clip
            text = TextClip(bottom, fontsize=textval, font=font, color=(str(tcolour))).set_pos(("bottom")).set_duration(clip.duration)
            clip = CompositeVideoClip([clip, text])
    #create the gif file
    clip.write_gif(name + ".gif", fps=framerate)
    
#file selection procedure
#opens a window where the user can browse their computer to find a video file they want to use
#is run whenever the user clicks the "Select File" button
def openFile():
    gui.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file")
    selectedfile = Label(gui, text=str(gui.filename))
    selectedfile.grid(row=0, column=1, columnspan=3)

#create the window for the gui
gui = Tk()
gui.title("Video To Gif Converter")#set the title of the window
gui.iconbitmap("icon.ico")#set the icon of the window

#this section creates text in the gui which labels all of the inputs
L1 = Label(gui, text="Gif Scale % :")
L1.grid(row=1, column=0)

L2 = Label(gui, text="Gif Name:")
L2.grid(row=2, column=2)

L3 = Label(gui, text="Gif Start Mins:")
L3.grid(row=2, column=0)

L4 = Label(gui, text="Gif Start Secs:")
L4.grid(row=3, column=0)

L5 = Label(gui, text="Gif End Mins:")
L5.grid(row=4, column=0)

L6 = Label(gui, text="Gif End Secs:")
L6.grid(row=5, column=0)

L7 = Label(gui, text="Gif FPS:")
L7.grid(row=3, column=2)

L8 = Label(gui, text="Gif Speed % :")
L8.grid(row=1, column=2)

L9 = Label(gui, text="Text Size:")
L9.grid(row=1, column=4)

L10 = Label(gui, text="Text Font:")
L10.grid(row=2, column=4)

L11 = Label(gui, text="Text Colour:")
L11.grid(row=3, column=4)

L12 = Label(gui, text="Top Text:")
L12.grid(row=4, column=4)

L13 = Label(gui, text="Middle Text:")
L13.grid(row=5, column=4)

L14 = Label(gui, text="Bottom Text:")
L14.grid(row=6, column=4)

L15 = Label(gui, text="Time Symmetry:")
L15.grid(row=4, column=2)

#this section creates all of the inputs in the gui, consisting of sliders, buttons, text inputs and a check box
gifScale = Scale(gui, from_=1, to=100, orient="horizontal", length=200)
gifScale.grid(row=1, column=1)

gifSpeed = Spinbox(gui, from_=1, to=50000)
gifSpeed.grid(row=1, column=3)

textSize = Spinbox(gui, from_=1, to=100)
textSize.grid(row=1, column=5)

gifName = Entry(gui, width=10, bg="light grey")
gifName.grid(row=2, column=3)

gifStartM = Entry(gui, width=10, bg="light grey")
gifStartM.grid(row=2, column=1)
gifStartM.insert(0,"0")

gifStartS = Entry(gui, width=10, bg="light grey")
gifStartS.grid(row=3, column=1)
gifStartS.insert(0,"00.0")

gifEndM = Entry(gui, width=10, bg="light grey")
gifEndM.grid(row=4, column=1)
gifEndM.insert(0,"0")

gifEndS = Entry(gui, width=10, bg="light grey")
gifEndS.grid(row=5, column=1)
gifEndS.insert(0,"00.0")

giffps = Entry(gui, width=10, bg="light grey")
giffps.grid(row=3, column=3)

textFont = Entry(gui, width=10, bg="light grey")
textFont.grid(row=2, column=5)

textColour = Entry(gui, width=10, bg="light grey")
textColour.grid(row=3, column=5)

topText = Entry(gui, width=10, bg="light grey")
topText.grid(row=4, column=5)

middleText = Entry(gui, width=10, bg="light grey")
middleText.grid(row=5, column=5)

bottomText = Entry(gui, width=10, bg="light grey")
bottomText.grid(row=6, column=5)

tSvar = IntVar()
timeSymmetry = Checkbutton(gui, variable=tSvar)
timeSymmetry.grid(row=4, column=3)

'''
file = Button(gui, text="Select File", command=lambda : openFile())
file.grid(row=0, column=0)
'''

create = Button(gui, text="Create Gif", command=lambda : createGif())
create.grid(row=7, column=3)

menubar = Menu(gui)
file = Menu(menubar, tearoff=0)
file.add_command(label="Open", command=lambda : openFile())
menubar.add_cascade(label="File", menu=file)
gui.config(menu=menubar)


gui.mainloop()
