from tkinter import * 
import time
import threading

from PIL import Image, ImageTk


# defining all vadiables
chickenc = 0
featherc = 0
bloodc = 0
meatc = 0
fluffc = 0
waterc = 0
dirtc = 0
ironc = 0
humanc = 0
knifec = 0
fluffwc = 0
coins = 0
ironwc = 0
dirtwc = 0
waterwc = 0


# all the workers for the game

def fluffworkerr():
    global fluffwc
    global fluffc
    while True:
        fluffc += 1
        if fluffwc == 1:
            time.sleep(2.5)
            fluff_label2.config(text=fluffc)
        elif fluffwc == 2:
            time.sleep(2)
            fluff_label2.config(text=fluffc)
        elif fluffwc == 3:
            time.sleep(1.5)
            fluff_label2.config(text=fluffc)
        elif fluffwc == 4:
            time.sleep(1)
            fluff_label2.config(text=fluffc)
        elif fluffwc == 5:
            time.sleep(0.5)
            fluff_label2.config(text=fluffc)
            
def dirtworkerr():
    global dirtwc
    global dirtc
    while True:
        dirtc += 1
        if dirtwc == 1:
            time.sleep(2.5)
            dirt_label2.config(text=dirtc)
        elif dirtwc == 2:
            time.sleep(2)
            dirt_label2.config(text=dirtc)
        elif dirtwc == 3:
            time.sleep(1.5)
            dirt_label2.config(text=dirtc)
        elif dirtwc == 4:
            time.sleep(1)
            dirt_label2.config(text=dirtc)
        elif dirtwc == 5:
            time.sleep(0.5)
            dirt_label2.config(text=dirtc)
            
def waterworkerr():
    global waterwc
    global waterc
    while True:
        waterc += 1
        if waterwc == 1:
            time.sleep(2.5)
            water_label2.config(text=waterc)
        elif waterwc == 2:
            time.sleep(2)
            water_label2.config(text=waterc)
        elif waterwc == 3:
            time.sleep(1.5)
            water_label2.config(text=waterc)
        elif waterwc == 4:
            time.sleep(1)
            water_label2.config(text=waterc)
        elif waterwc == 5:
            time.sleep(0.5)
            water_label2.config(text=waterc)
            
def ironworkerr():
    global ironwc
    global ironc
    while True:
        ironc += 1
        if ironwc == 1:
            time.sleep(2.5)
            iron_label2.config(text=ironc)
        elif ironwc == 2:
            time.sleep(2)
            iron_label2.config(text=ironc)
        elif ironwc == 3:
            time.sleep(1.5)
            iron_label2.config(text=ironc)
        elif ironwc == 4:
            time.sleep(1)
            iron_label2.config(text=ironc)
        elif ironwc == 5:
            time.sleep(0.5)
            iron_label2.config(text=ironc)
            
    

def buyironworker():
    global coins
    global ironwc
    if coins >= 50:
        if ironwc > 5:
            message.config(text = 'you have already reached the max amount of iron workers')   
        else:
            coins -=50
            ironwc += 1
            coin_label2.config(text=coins)
            ironw_label2.config(text=ironwc)
            message.config(text = 'congrats on buying a iron worker!')
            threading.Thread(target=ironworkerr).start()
    else:
        message.config(text = 'not enough cins for this item :(')
        
def buyfeatherworker():
    global coins
    global fluffwc
    if coins >= 50:
        if fluffwc > 5:
            message.config(text = 'you have already reached the max amount of fluff workers')   
        else:
            coins -=50
            fluffwc += 1
            coin_label2.config(text=coins)
            fluffw_label2.config(text=fluffwc)
            message.config(text = 'congrats on buying a fluff worker!')
            threading.Thread(target=fluffworkerr).start()
    else:
        message.config(text = 'not enough coins for this item :(')
        
def buywaterworker():
    global coins
    global waterwc
    if coins >= 50:
        if waterwc > 5:
            message.config(text = 'you have already reached the max amount of water workers')   
        else:
            coins -=50
            waterwc += 1
            coin_label2.config(text=coins)
            waterw_label2.config(text=waterwc)
            message.config(text = 'congrats on buying a water worker!')
            threading.Thread(target=waterworkerr).start()
    else:
        message.config(text = 'not enough coins for this item :(')
        
def buydirtworker():
    global coins
    global dirtwc
    if coins >= 50:
        if dirtwc > 5:
            message.config(text = 'you have already reached the max amount of dirt workers')   
        else:
            coins -=50
            dirtwc += 1
            coin_label2.config(text=coins)
            dirtw_label2.config(text=dirtwc)
            message.config(text = 'congrats on buying a dirt worker!')
            threading.Thread(target=dirtworkerr).start()
    else:
        message.config(text = 'not enough cins for this item :(')

def sellchicken():
    global coins
    global chickenc
    if chickenc >= 1:
        chickenc -= 1
        coins += 50
        chicken_label2.config(text=chickenc)
        coin_label2.config(text=coins)
        message.config(text = 'one chickn sold for 50 coins')

    
    
def chickeng():
    global chickenc
    global featherc
    global bloodc
    global meatc
    if featherc >= 10 and bloodc >= 10 and meatc >= 10:
      featherc -= 10
      bloodc -=10
      meatc -=10
      chickenc += 1
      chicken_label2.config(text=chickenc)
      feathers_label2.config(text=featherc)
      blood_label2.config(text=bloodc)
      meat_label2.config(text=meatc)
      message.config(text = 'congrats on buying a chicken!')
    else:
        message.config(text = 'not enough recources to buy :(')
      

      
def featherg():
    global featherc
    global fluffc
    if fluffc >= 20:
        fluffc -= 20
        featherc += 1
        feathers_label2.config(text=featherc)
        fluff_label2.config(text=fluffc)
        message.config(text = 'congrats on buying a feather!')
    else:
        message.config(text = 'not enough recources to buy this item')
        
def bloodg():
    global bloodc
    global ironc
    if ironc >= 20:
        ironc -= 20
        bloodc += 1
        blood_label2.config(text=bloodc)
        iron_label2.config(text=ironc)
        message.config(text = 'congrats on buying a blood!')
    else:
        message.config(text = 'not enough recources to buy this item')
    
def meatg():
    global meatc
    global humanc
    global knifec
    if humanc >=5 and knifec >= 1:
        humanc -= 5
        knifec -= 1
        meatc += 1
        meat_label2.config(text=meatc)
        knife_label2.config(text=knifec)
        human_label2.config(text=humanc)
        message.config(text = 'congrats on buying a meat!')
    else:
        message.config(text = 'not enough recources to buy this item')

        
    
def fluffg():
    global fluffc
    fluffc += 1
    fluff_label2.config(text=fluffc)
    message.config(text = 'one fluff gained')

def waterg():
    global waterc
    waterc += 1
    water_label2.config(text=waterc)
    message.config(text = 'one water gained')

def dirtg():
    global dirtc
    dirtc += 1
    dirt_label2.config(text=dirtc)
    message.config(text = 'one dirt gained')

def irong():
    global ironc
    ironc += 1
    iron_label2.config(text=ironc)
    message.config(text = 'one iron gained')
def humang():
    global humanc
    global dirtc
    global waterc
    if dirtc >= 5 and waterc >= 5:
        dirtc -= 5
        water -= 5
        humanc += 1
        human_label2.config(text=humanc)
        water_label2.config(text=waterc)
        dirt_label2.config(text=dirtc)
        message.config(text = 'one human has been created')
    else:
        message.config(text = 'not enough recources to buy this item')

def knifeg():
    global knifec
    knifec += 1
    knife_label2.config(text=knifec)
    message.config(text = 'one knife gained')

window = Tk()


# chickenpic2 = PhotoImage(file='lordchicken.png')
def finished():
    
    global chickenc
    if chickenc >= 20:
       won = Toplevel()
       chickenwinner = Label(won, image=chickenpic2)
       winneryeah = Label (won, text='CONGRATS U HAVE WON')
       chickenwinner.grid(row=0, column=0)
       winneryeah.grid(row=1, column=0)
    else: message.config(text = 'not enough chickens to finish the game')



# Load the image
img = Image.open("lordchicken.png")

# Resize the image
new_width = 300
new_height = 250
img = img.resize((new_width, new_height), Image.ANTIALIAS)

# Convert the image to a PhotoImage object and display it in a Label widget
chickenpic = ImageTk.PhotoImage(img)

# Load the image
img2 = Image.open("lordchicken.png")

# Resize the image
new_width2 = 1000
new_height2 = 720
img2 = img2.resize((new_width2, new_height2), Image.ANTIALIAS)

# Convert the image to a PhotoImage object and display it in a Label widget
chickenpic2 = ImageTk.PhotoImage(img2)
ww=40
hh=40
bloodpt = Image.open("blood.png")
bloodpt = bloodpt.resize((ww, hh), Image.ANTIALIAS)
bbb = ImageTk.PhotoImage(bloodpt)


coinspt = Image.open("coins.png")
dirtpt = Image.open("dirt.png")
dirtworkpt = Image.open("dirtw.png")
featherpt = Image.open("feather.png")
flufpt = Image.open("fluf.png")
flufworkpt = Image.open("fluffw.png")
ironpt = Image.open("iron.png")
ironworkpt = Image.open("ironw.png")
knifept = Image.open("knife.png")
manpt = Image.open("man.png")
meatpt = Image.open("meat.png")
waterpt = Image.open("water.png")
waterwpt = Image.open("waterw.png")
chickenpt = Image.open("chicken.png")

coinspt = coinspt.resize((ww, hh), Image.ANTIALIAS)
dirtpt = dirtpt.resize((ww, hh), Image.ANTIALIAS)
dirtworkpt = dirtworkpt.resize((ww, hh), Image.ANTIALIAS)
featherpt = featherpt.resize((ww, hh), Image.ANTIALIAS)
flufpt = flufpt.resize((ww, hh), Image.ANTIALIAS)
flufworkpt = flufworkpt.resize((ww, hh), Image.ANTIALIAS)
ironpt = ironpt.resize((ww, hh), Image.ANTIALIAS)
ironworkpt = ironworkpt.resize((ww, hh), Image.ANTIALIAS)
knifept = knifept.resize((ww, hh), Image.ANTIALIAS)
manpt = manpt.resize((ww, hh), Image.ANTIALIAS)
meatpt = meatpt.resize((ww, hh), Image.ANTIALIAS)
waterpt = waterpt.resize((ww, hh), Image.ANTIALIAS)
waterwpt = waterwpt.resize((ww, hh), Image.ANTIALIAS)
chickenpt = chickenpt.resize((ww, hh), Image.ANTIALIAS)

ccc = ImageTk.PhotoImage(coinspt)
ddd = ImageTk.PhotoImage(dirtpt)
ddi = ImageTk.PhotoImage(dirtworkpt)
fff = ImageTk.PhotoImage(featherpt)
ffw = ImageTk.PhotoImage(flufpt)
flf = ImageTk.PhotoImage(flufworkpt)
iii = ImageTk.PhotoImage(ironpt)
iiiw = ImageTk.PhotoImage(ironworkpt)
kkk = ImageTk.PhotoImage(knifept)
mmm = ImageTk.PhotoImage(manpt)
mma = ImageTk.PhotoImage(meatpt)
www = ImageTk.PhotoImage(waterpt)
wwww = ImageTk.PhotoImage(waterwpt)
cch = ImageTk.PhotoImage(chickenpt)




finishgame = Button(window, image=chickenpic, command = finished)
finishgame.grid(row=1, column=1)
chicken = Button(window, image=cch, command=chickeng)
chicken.grid(row=11, column=2)
deathers = Button(window,  image=fff,  command=featherg)
deathers.grid(row=10, column=2)
blood = Button(window, image=bbb , command=bloodg)
blood.grid(row=9, column=2)
meat = Button(window, image=mma, command=meatg)
meat.grid(row=12, column=2)
human = Button(window, image=mmm, command=humang)
human.grid(row=13, column=2)
fluff = Button(window, image=ffw, command=fluffg)
fluff.grid(row=2, column=1)
water = Button(window, image=www , command=waterg)
water.grid(row=3, column=1)
dirt = Button(window,image=ddd, command=dirtg)
dirt.grid(row=5, column=1)
iron = Button(window, image=iii, command=irong)
iron.grid(row=4, column=1)
knife = Button(window, image=kkk, command=knifeg)
knife.grid(row=6, column=1)

# worker buttons to purchase from

workerlabell = Label(window, text='click on a worker to hire them')
workerlabell.grid(row=7,column=1)

fluffworker = Button(window, image=flf, command=buyfeatherworker)
fluffworker.grid(row=9, column=1)
ironworker = Button(window, image=iiiw, command=buyironworker)
ironworker.grid(row=11, column=1)
dirtworker = Button(window, image=ddi, command=buydirtworker)
dirtworker.grid(row=12, column=1)
waterworker = Button(window, image=wwww, command=buywaterworker)
waterworker.grid(row=10, column=1)
selllechicken = Button(window, image=ccc, command = sellchicken)
selllechicken.grid(row=1, column=2)

chicken_label = Label(window, image=cch)
chicken_label2 = Label(window, text=chickenc)

chicken_label.grid(row=11,column=6)
chicken_label2.grid(row=11,column=7)

feathers_label = Label(window, image=fff)
feathers_label2 = Label(window, text=featherc)

feathers_label.grid(row=10,column=6)
feathers_label2.grid(row=10,column=7)

blood_label = Label(window, image=bbb)
blood_label2 = Label(window, text=bloodc)

blood_label.grid(row=9,column=6)
blood_label2.grid(row=9,column=7)

meat_label = Label(window, image=mma)
meat_label2 = Label(window, text=meatc)

meat_label.grid(row=12,column=6)
meat_label2.grid(row=12,column=7)

fluff_label = Label(window, image=ffw)
fluff_label2 = Label(window, text=fluffc)

fluff_label.grid(row=2,column=6)
fluff_label2.grid(row=2,column=7)

water_label = Label(window, image=www)
water_label2 = Label(window, text=waterc)

water_label.grid(row=3,column=6)
water_label2.grid(row=3,column=7)

dirt_label = Label(window, image=ddd)
dirt_label2 = Label(window, text=dirtc)

dirt_label.grid(row=5,column=6)
dirt_label2.grid(row=5,column=7)

iron_label = Label(window, image=iii)
iron_label2 = Label(window, text=ironc)

iron_label.grid(row=4,column=6)
iron_label2.grid(row=4,column=7)

human_label = Label(window, image=mmm)
human_label2 = Label(window, text=humanc)

human_label.grid(row=13,column=6)
human_label2.grid(row=13,column=7)

knife_label = Label(window, image=kkk)
knife_label2 = Label(window, text=knifec)

knife_label.grid(row=6,column=6)
knife_label2.grid(row=6,column=7)

buylabel = Label(window, text='sell one chick for 50 coins')
buylabel.grid(row=0,column=2)

coin_label =Label(window, image=ccc)
coin_label2 = Label(window, text=coins)

coin_label.grid(row=1,column=6)
coin_label2.grid(row=1,column=7)

game_instructions = Label(window, text='to win the game, collect 20 chickens and give them to the lord chicken.' +
                          '\n'+
                          ' ( once 20 chickens have been collected, click on lord chicken to complete the game)')
game_instructions.grid(row=0,column=0)

#labels/indicators for the recource amount/inventory
coinin = Label(window, text = 'coins -->')
flufin= Label(window, text = 'fluff -->')
waterin=Label(window, text = 'water -->')
ironin=Label(window, text = 'iron -->')
dirtin=Label(window, text = 'dirt -->')
knifein=Label(window, text = 'knife -->')
bloodin=Label(window, text = 'blood -->')
featherin=Label(window, text = 'feather -->')
chickenin=Label(window, text = 'chicken -->')
meatin=Label(window, text = 'meat -->')
humanin=Label(window, text = 'human -->')

coinin.grid(row=1, column=5)
flufin.grid(row=2, column=5)
waterin.grid(row=3, column=5)
ironin.grid(row=4, column=5)
dirtin.grid(row=5, column=5)
knifein.grid(row=6, column=5)
bloodin.grid(row=9, column=5)
featherin.grid(row=10, column=5)
chickenin.grid(row=11, column=5)
meatin.grid(row=12, column=5)
humanin.grid(row=13, column=5)

fluffw_label = Label(window, image=flf)
fluffw_label2 = Label(window, text=fluffwc)

fluffw_label.grid(row=7,column=0)
fluffw_label2.grid(row=8,column=0)

ironw_label = Label(window, image=iiiw)
ironw_label2 = Label(window, text=ironwc)

ironw_label.grid(row=11,column=0)
ironw_label2.grid(row=12,column=0)

dirtw_label = Label(window, image=ddi)
dirtw_label2 = Label(window, text=dirtwc)

dirtw_label.grid(row=13,column=0)
dirtw_label2.grid(row=14,column=0)

waterw_label = Label(window, image=wwww)
waterw_label2 = Label(window, text=waterwc)

waterw_label.grid(row=9,column=0)
waterw_label2.grid(row=10,column=0)

message = Label(window, text='collect recources by tapping on buttons.')
message.grid(row=1,column=0)

workerinstructions = Label(window, text='get workers to automatically collect recources (max 5 per recource)' )
workerinstructions.grid(row=2, column=0)

wrk1 = Label(window, text = 'iron = 50 gold')
wrk2 = Label(window, text = 'fluff = 50 gold')
wrk3 = Label(window, text = 'dirt = 100 gold')
wrk4 = Label(window, text = 'water = 100 gold')
wrk1.grid(row=3,column=0)
wrk2.grid(row=4,column=0)
wrk3.grid(row=5,column=0)
wrk4.grid(row=6,column=0)



prices = Label(window, text = 'prices')
inst1 = Label(window, text = 'meat - 5 human + 1 knife.')
inst2 = Label(window, text = 'blood - 20 iron.')
inst3 = Label(window, text = 'human - 5 dirt + 5 water')
inst4 = Label(window, text = 'feather - 20 fluff.')
inst5 = Label(window, text = 'chicken - 10 feathers + 10 blood + 10 meat')
inst1.grid(row=3,column=2)
inst2.grid(row=4,column=2)
inst3.grid(row=5,column=2)
inst4.grid(row=6,column=2)
inst5.grid(row=7,column=2)
prices.grid(row=2,column=2)

window.mainloop()
