from pygame import *

font.init()
font = font.Font('Sakura Blossom.ttf', 36)#Если не хотим шрифт, то пишем None
lose1 = font.render('First PLAYER LOSE!', True, (180,0,0))
lose2 = font.render('Second PLAYER LOSE!', True, (180,0,0))

ball = GameSprite()

while game:



    ball.reset()
