from graph import *

# Заливка всего окна 500х600
brushColor("White")
rectangle(0,0,500,600)

#Голова
penColor("Black")
brushColor("Yellow")
circle(250, 300, 150)

#Глаза
brushColor("Red")
circle(180, 250, 40)
circle(320, 250, 32)
brushColor("Black")
circle(180, 250, 10)
circle(320, 250, 10)

#Брови и рот
polygon([(140, 140), (150, 130), (240, 240), (235,250), (140, 140)])
rectangle(170, 350, 330, 370)

polygon([(270, 240), (275, 245), (390, 165), (380, 140), (270, 240)])

run() 