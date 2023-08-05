from browser import document, window, alert
import random, math


class Games:
  # Variables
  line=600 # cactus start position (right of the screen)
  speed=1 # speed of the cactus
  jumping= False # is the trex jumping
  trex_x=50 # trex x position
  trex_y=200 # trex y position
  trex_height=40  # trrex height
  trex_width=50 #tres width
  game_over = False # is the game over
  score = 0 # current player score
  end = "" # end text string, now its empty because the game is not over
  highScore= 0 # current high score
  topScore="" # end text string to show what the current top score is
  options = [] # how many different cactus picture
  pic = "1" # current cactus pic
  showBird = 1 # show or hide bird
  duck = False # is the trex ducking
  o = 1 # option 1
  # add pics options
  while o < 5:
    options.append(o)
    o = o + 1

  # make the cactus move back each time
  def moveBack(self):
    self.line= self.line -5

  # after the cactus is on the left side, make it appear on the right side of the screen and increase player score by 1, also make the speed higher and choose random cactus from the pics options
  def resetLine(self):
    if(self.line == 0):
      self.score +=1
      self.line =600
      self.speed= self.speed + 0.1
      r = random.randint(0,3)
      self.pic = str(self.options[(r)])
      self.showBird = random.randint(0,5)

  # make the trex jump up
  def jump(self):
    if self.jumping:
      self.trex_y-=5
    if self.trex_y<= 125:
        self.jumping= False
  # make the trex fall back after  done jumping
  def fall(self):
    if not self.jumping and self.trex_y < 220:
      self.trex_y+=5

  # when the user clicks spacebar
  def spaceBar(self):
    if not self.game_over : #spacebar
         if self.trex_y == 220:
           self.jumping = True

  # when the geme restarts after using uses the mouse, it will reset variables to the original values
  def restart(self):
    self.game_over = False
    self.line=600
    self.speed=1
    self.end=""
    self.score=0
    self.topScore=''
    

  # if user loses by not jumping over a cactus or not ducking under a bird, also update high score if user beats it and show the strings for end game
  def endGame(self):
    if(self.showBird == 1):
      if(self.trex_x== self.line and self.duck == False):
        self.line = 0
        self.game_over = True
  
        if (self.score > self.highScore):
          self.highScore = self.score
        self.end = "GAME OVER\n press the mouse to restart"
        self.topScore = "Top score : " + str(self.highScore)
      
    else:
      if(self.trex_x== self.line and self.trex_y >=190):
        self.line = 0
        self.game_over = True
  
        if (self.score > self.highScore):
          self.highScore = self.score
        self.end = "GAME OVER\n press the mouse to restart"
        self.topScore = "Top score : " + str(self.highScore)
  



Game = Games()

def sketch(p):
    # load images
    p.img = {"Left":p.loadImage("Trex1.png"), 
             "Right":p.loadImage("Trex2.png"),
             "Duck":p.loadImage("Trex3.png")}
  
    p.leg = "Left"
    p.frame = 0
    p.catus = {}
    for i in range (1,5):
 
      p.catus[str(i)] = p.loadImage(f'cat{i}.png')
              
    p.clouds = p.loadImage("stars.png")
    p.bird = p.loadImage("bird.png")
    p.showBird = 0

    def setup():

      p.createCanvas(600,300)
      p.frameRate(60)
      p.stroke(225);
      p.imageMode(p.CENTER) 

    def draw():
        if(Game.game_over == False):
          p.frame = p.frame + 1
        p.fill(1000,1000,1000);
      
        p.background(0);
        p.image(p.clouds,  300, 120,     
        600,  200)
      
        p.circle(10,10,50,30)
        p.line(0,240,600,240);
    
        if Game.showBird == 1: # show bird
          p.image(p.bird,math.prod([Game.line, Game.speed]), 195,     
        Game.trex_width,  Game.trex_height )
          

        else: # show cactus
          p.image(p.catus[Game.pic],math.prod([Game.line, Game.speed]), 220,     
        Game.trex_width,  Game.trex_height )

        p.textSize(20);
        p.text(Game.end,200,30); # show end game string
        p.text("Score: " + str(Game.score), 500, 30); # show score
        p.text(Game.topScore, 450,100);
        #draw Trex legs and make it look like its moving by switching between the photos 
        if p.frame == 7 and not p.leg == "Duck":
          p.frame = 0
          if(p.leg == "Left"):
            p.leg = "Right"
          else:
            p.leg = "Left"
          Game.duck = False


        if(p.frame > 30 and  p.leg == "Duck"):
          p.frame = 0
          p.leg = "Right"
          Game.duck = False


        p.image(p.img[p.leg],Game.trex_x, Game.trex_y, Game.trex_width, 
        Game.trex_height)
        
        Game.jump()
        Game.fall()
        Game.moveBack()
        Game.resetLine()
        Game.endGame()

    def keyPressed(self):
      # Spacebar or W to jump
      if p.keyCode == 32 or p.keyCode == 87 :
        p.leg = "Right"
        Game.spaceBar()
      # S to duck
      if(p.keyCode == 83):
       
        if p.leg == "Duck":
          p.leg = "Right"
          Game.duck = False
        else:
          p.leg = "Duck"
          Game.duck = True
      p.frame = 0

        
        
        
    def mousePressed(self):
      #Reset game while keeping the high score
      Game.restart()
   
    
    p.setup = setup
    p.draw = draw
    p.mousePressed = mousePressed
    p.keyPressed = keyPressed



myp5 = window.p5.new(sketch)
