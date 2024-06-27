import pygame
import random
import tkinter as tk
import time
import os

root = tk.Tk()

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

pygame.init()

res = (width,height)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Hangman")
background = (202, 228, 241)
screen.fill(background)
pygame.display.flip()

EasyImage = pygame.image.load("easy_button.png").convert_alpha() 
MediumImage = pygame.image.load("medium_button.png").convert_alpha()
HardImage = pygame.image.load("hard_button.png").convert_alpha()
FirstLifeLost = pygame.image.load("1st_life_lost.png").convert_alpha()
SecondLifeLost = pygame.image.load("2nd_life_lost.png").convert_alpha()
ThirdLifeLost = pygame.image.load("3rd_life_lost.png").convert_alpha()
FourthLifeLost = pygame.image.load("4th_life_lost.png").convert_alpha()
FifthLifeLost = pygame.image.load("5th_life_lost.png").convert_alpha()
SixthAndEigthLivesLost = pygame.image.load("6th_and_8th_lives_lost.png").convert_alpha()
SeventhAndNinthLivesLost = pygame.image.load("7th_and_9th_lost.png").convert_alpha()
Cross = pygame.image.load("end_of_game.png").convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def draw_button(self):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

def blit_img(img, x, y):
    screen.blit(img, (x,y))
  
ButtonScale = 0.5
EasyButton = Button(0,0, EasyImage, ButtonScale)
MediumButton = Button(120,0, MediumImage, ButtonScale)
HardButton = Button(240,0,HardImage, ButtonScale)

input_rect = pygame.Rect(760,440,140,32)
colour_active = pygame.Color("lightskyblue3")
colour_passive = pygame.Color("chartreuse4")
colour = colour_passive

lives = 10
user_text = ""
base_font = pygame.font.Font(None, 32)
EndMessage = "You have run out of lives"
LivesUpdate = "Lives remaining: ", lives
WinMessage = "You have successfully guessed the word"
y_of_underscores = 0
y_of_lives = 0
DisplayableWordToGuess = ""
GuessedLetters = []
CurrentGuess = ""
 

i = 0
index = []
running = True
AllowInputs = False
active = False
while running:

    if EasyButton.draw_button():
        with open("easy.txt", "r") as file:
            ListOfWords = []
            for line in file:
                ListOfWords.append(line)
        WordIndex = random.randint(0,6)
        WordToGuess = ListOfWords[WordIndex]
        print(WordToGuess) #Remove @ end
        ArrayOfUnderscores = ["_","_","_","_"]
        draw_text(str(ArrayOfUnderscores), base_font, (0,0,0),460, y_of_underscores)
        draw_text(str(LivesUpdate), base_font,(0,0,0),1030, y_of_lives)
        y_of_lives = y_of_lives + 25
        AllowInputs = True

                    
    if MediumButton.draw_button():
        with open("medium.txt", "r") as file:
            ListOfWords = []
            for line in file:
                ListOfWords.append(line)
        WordIndex = random.randint(0,6)
        WordToGuess = ListOfWords[WordIndex]
        print(WordToGuess) #Remove @ end
        ArrayOfUnderscores = ["_","_","_","_","_","_","_"]
        draw_text(str(ArrayOfUnderscores), base_font, (0,0,0),460, y_of_underscores)
        draw_text(str(LivesUpdate), base_font,(0,0,0),1030, y_of_lives)
        y_of_lives = y_of_lives + 25
        AllowInputs = True
        
    if HardButton.draw_button():
        with open("hard.txt", "r") as file:
            ListOfWords = []
            for line in file:
                ListOfWords.append(line)
        WordIndex = random.randint(0,6)
        WordToGuess = ListOfWords[WordIndex]
        print(WordToGuess) #Remove @ end
        ArrayOfUnderscores = ["_","_","_","_","_","_","_","_","_","_"]
        draw_text(str(ArrayOfUnderscores), base_font,(0,0,0),460, y_of_underscores)
        draw_text(str(LivesUpdate), base_font,(0,0,0),1030, y_of_lives)
        y_of_lives = y_of_lives + 25
        AllowInputs = True

    pygame.display.flip()

    
    for event in pygame.event.get():
            
        if AllowInputs:
             if event.type == pygame.MOUSEBUTTONDOWN:
                 if input_rect.collidepoint(event.pos):
                      active = True
                 else:
                     active = False
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_BACKSPACE:
                     user_text = user_text[:-1]
                 else:
                   user_text += event.unicode
                 while len(user_text) > 1:
                     user_text = user_text[:-1]
                 if event.key == pygame.K_RETURN:
                     if user_text in GuessedLetters:
                         draw_text(("You have already guessed this, try again"), base_font, (0,0,0),900, y_of_lives)
                         y_of_lives = y_of_lives + 25
                         break
                     if WordToGuess.count(user_text) == 1:
                        GuessedLetters.append(user_text)
                        index = WordToGuess.index(user_text)
                        ArrayOfUnderscores[index] = user_text
                        y_of_underscores = y_of_underscores + 25
                        draw_text(str(ArrayOfUnderscores), base_font, (0,0,0),460,y_of_underscores)
                        CurrentGuess = ""
                        for i in range (0, len(ArrayOfUnderscores)):
                                  CurrentGuess = CurrentGuess + ArrayOfUnderscores[i]
                                  i = i + 1
                        if (CurrentGuess + "\n")== WordToGuess:
                            draw_text((WinMessage), base_font, (0,0,0),760, 500)
                            pygame.display.flip()
                            time.sleep(5)
                            os._exit(0)
                                        
                     if WordToGuess.count(user_text) > 1:
                         GuessedLetters.append(user_text)
                         for i in range (0, len(WordToGuess)):
                            if WordToGuess[i] == user_text:
                                ArrayOfUnderscores[i] = user_text
                                y_of_underscores = y_of_underscores + 25
                                draw_text(str(ArrayOfUnderscores), base_font, (0,0,0),460,y_of_underscores)
                         i = i + 1
                         CurrentGuess = ""
                         for i in range (0, len(ArrayOfUnderscores)):
                                  CurrentGuess = CurrentGuess + ArrayOfUnderscores[i]
                                  i = i + 1
                         if (CurrentGuess + "\n") == WordToGuess:
                            draw_text((WinMessage), base_font, (0,0,0),760, 500)
                            pygame.display.flip()
                            time.sleep(5)
                            os._exit(0)
                     if WordToGuess.count(user_text) == 0:
                        GuessedLetters.append(user_text)
                        lives = lives - 1
                        if lives == 9:
                            blit_img(FirstLifeLost, 60, 220) #1st pole
                        elif lives == 8:
                            blit_img(SecondLifeLost, 60, 220) #line at the top
                        elif lives == 7:
                            blit_img(ThirdLifeLost, 440, 220)#rope
                        elif lives == 6:
                            blit_img(FourthLifeLost, 320, 350)  #head
                        elif lives == 5:
                            blit_img(FifthLifeLost, 390, 550)#body
                        elif lives == 4:
                            blit_img(SixthAndEigthLivesLost,320,565) #left arm
                        elif lives == 3:
                            blit_img(SeventhAndNinthLivesLost,390,565) # right arm
                        elif lives == 2:
                            blit_img(SixthAndEigthLivesLost, 325, 695) # left leg
                        elif lives == 1:
                            blit_img(SeventhAndNinthLivesLost, 385,695)#right leg
                     if lives == 0:
                        blit_img(Cross, 0, 220)
                        LivesUpdate = "Lives remaining: ", lives
                        draw_text(str(LivesUpdate), base_font,(0,0,0),1030, y_of_lives)
                        y_of_lives = y_of_lives + 25
                        draw_text(str(EndMessage), base_font, (0,0,0),760, 500)
                        y_of_lives = y_of_lives + 25
                        if len(ArrayOfUnderscores) == 4:
                            DisplayableWordToGuess = WordToGuess[0:4]
                        elif len(ArrayOfUnderscores) == 7:
                            DisplayableWordToGuess = WordToGuess[0:7]
                        elif len(ArrayOfUnderscores) == 10:
                            DisplayableWordToGuess = WordToGuess[0:10]
                        Solution = "The word was", DisplayableWordToGuess
                        draw_text(str(Solution), base_font,(0,0,0),900, y_of_lives)
                        pygame.display.flip()
                        time.sleep(5)
                        os._exit(0)
                        
                     LivesUpdate = "Lives remaining: ", lives
                     draw_text(str(LivesUpdate), base_font,(0,0,0),1030, y_of_lives)          
                     y_of_lives = y_of_lives + 25
                     
                                                             
        if active:
            colour = colour_active
        else:
            colour = colour_passive

        pygame.draw.rect(screen, colour, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (760, 440))
        input_rect.w = max(100, text_surface.get_width()+10)
        pygame.display.flip()
            
        if event.type == pygame.QUIT:
            running = False
            exit()

  


        
            
