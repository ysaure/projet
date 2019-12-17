from tkinter import *
from PIL import Image

#
pingy=Image.open("pingy.png")
pingy.save("pingy1.png")

#
def effacer():
    can2.delete(ALL)
    original=Image.open("pingy.png")
    original.save("pingy1.png")
    photo2 = PhotoImage(file ="pingy1.png")
    can2.create_image(200,200,image=photo2)
   

#
def transformation1():
    original=Image.open("pingy1.png")
    nouvelleImage=Image.new("RGBA",(original.size[0],original.size[1]))

    pixels=original.load()
    nouveauxpixels=nouvelleImage.load()

    for i in range (original.size[0]):
        for j in range (original.size[1]):
            nouveauxpixels[i,j]=pixels[original.size[0]-i-1,original.size[1]-j-1]

    nouvelleImage.save("pingy1.png")
    photo2 = PhotoImage(file ="pingy1.png")
    can2.delete(ALL)
    can2.create_image(200,200,image=photo2)
    fen1.mainloop()

def transformation2():
     original=Image.open("pingy1.png")
     nouvelleImage=Image.new("RGBA",(original.size[0],original.size[1]))
     pixels=original.load()
     nouveauxpixels=nouvelleImage.load()


     for i in range (original.size[0]):
        for j in range (original.size[1]):
            nouveauxpixels[i,j]=pixels[original.size[0]-i-1,j]
     nouvelleImage.save("pingy1.png")
     photo2 = PhotoImage(file ="pingy1.png")
     can2.delete(ALL)
     can2.create_image(200,200,image=photo2)
     fen1.mainloop()


fen1 = Tk()
fen1.geometry("500x500")

#Indique le texte sur les boutons et donc ce que
txt1 = Label(fen1, text ='Choisissez une transformation')
boutonT1=Button(fen1, text="Transformation 1", command=transformation1)
boutonT2=Button(fen1, text="Transformation 2", command=transformation2)
boutonF=Button(fen1, text="Fermer", command=fen1.destroy)
boutonE=Button(fen1, text="Effacer", command=effacer)

can2 = Canvas(fen1, width =400, height =400, bg ='white')
photo2 = PhotoImage(file ="pingy1.png")
can2.create_image(200,200,image=photo2)

# "pady" indique la position de l'image;
#"row" indique la position, le niveau, de haut en bas, des boutons,sur le cadrant
#"column" indique la position, de droite à gauche,des boutons sur le cadrant
#"sticky" est une etiquette , indique la position des boutons

txt1.grid(pady=10,row=1, column =1, sticky=N)
boutonT1.grid(padx=60, pady=10,row =2, column =1,sticky=W)
boutonT2.grid(padx=60, pady=10,row =2, column =1,sticky=E)
boutonE.grid(padx=10, pady=10,row =3, column =2)
boutonF.grid(padx=10, pady=10,row =4, column =2,sticky=N)
can2.grid(row =3, column =1, rowspan =2, padx =10)

#
fen1.mainloop()
