from vpython import *
import time

from pygame import mixer
mixer.init()
mixer.music.load('wow.mp3')
mixer.music.play()
time.sleep(5)

mysphere=sphere(colour=color.white,radius=1,pos=vector(0,2.5,0))
mycylinder=cylinder(colour=color.white,radius=1,axis=vector(0,2.5,0))
rounddisc=cylinder(colour=color.white,radius=1.1,axis=vector(0,.5,0))
myledlegs=box(pos=vector(-.75,-1,0),size=vector(.1,3,.1),color=vector(.2,.2,.2))
myledlegs=box(pos=vector(.75,-1,0),size=vector(.1,4,.1),color=vector(.2,.2,.2))
time.sleep(2)
while True:
    mycylinder.color=vector(1,0,0)
    mysphere.color=vector(1,0,0)
    rounddisc.color=vector(1,0,0)
    time.sleep(2)
    
    mycylinder.color=vector(0,1,0)
    mysphere.color=vector(0,1,0)
    rounddisc.color=vector(0,1,0)
    time.sleep(2)
    mycylinder.color=vector(0,0,1)
    mysphere.color=vector(0,0,1)
    rounddisc.color=vector(0,0,1)
    time.sleep(2)
    print('done')