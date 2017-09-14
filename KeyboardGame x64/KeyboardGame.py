
import pygame
import pygame.mixer
import random
import time
from pygame.locals import *
from threading import Thread
import threading


# Shuffles the Keyboard letters to start the game
def my_shuffle(array):
    newarray = array[:]
    random.shuffle(newarray)
    return newarray

# Renders the Keyboard in the default or shuffled format
class Keyboard(object):

    def __init__(self, gameDisplay, letterslist):
        gameDisplay.blit(dirImg[letterslist[0]], [145, 100])
        gameDisplay.blit(dirImg[letterslist[1]], [196, 100])
        gameDisplay.blit(dirImg[letterslist[2]], [247, 100])
        gameDisplay.blit(dirImg[letterslist[3]], [298, 100])
        gameDisplay.blit(dirImg[letterslist[4]], [349, 100])
        gameDisplay.blit(dirImg[letterslist[5]], [400, 100])
        gameDisplay.blit(dirImg[letterslist[6]], [451, 100])
        gameDisplay.blit(dirImg[letterslist[7]], [502, 100])
        gameDisplay.blit(dirImg[letterslist[8]], [553, 100])
        gameDisplay.blit(dirImg[letterslist[9]], [604, 100])
        gameDisplay.blit(dirImg[letterslist[10]], [170, 151])
        gameDisplay.blit(dirImg[letterslist[11]], [221, 151])
        gameDisplay.blit(dirImg[letterslist[12]], [272, 151])
        gameDisplay.blit(dirImg[letterslist[13]], [323, 151])
        gameDisplay.blit(dirImg[letterslist[14]], [374, 151])
        gameDisplay.blit(dirImg[letterslist[15]], [425, 151])
        gameDisplay.blit(dirImg[letterslist[16]], [476, 151])
        gameDisplay.blit(dirImg[letterslist[17]], [527, 151])
        gameDisplay.blit(dirImg[letterslist[18]], [578, 151])
        gameDisplay.blit(dirImg[letterslist[19]], [221, 202])
        gameDisplay.blit(dirImg[letterslist[20]], [272, 202])
        gameDisplay.blit(dirImg[letterslist[21]], [323, 202])
        gameDisplay.blit(dirImg[letterslist[22]], [374, 202])
        gameDisplay.blit(dirImg[letterslist[23]], [425, 202])
        gameDisplay.blit(dirImg[letterslist[24]], [476, 202])
        gameDisplay.blit(dirImg[letterslist[25]], [527, 202])
        pygame.display.update()


# Renders the timer
def timer(gameDisplay, numberText):
    largeText = pygame.font.SysFont('comicsansms', 80)
    text = str(numberText)
    TextSurf, TextRect = text_objects(text, largeText, numcolor)
    TextRect.center = (400, 400)
    gameDisplay.blit(imgTile, [330, 330])
    pygame.display.update()
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

# Renders the HelpPage
def helpPage(gamedisplay):

    gamedisplay.fill(supercolor)
    gamedisplay.blit(imgDIRECT, [0, 0])
    pygame.display.update()
    gameExit = False

    while not gameExit:
        mouse2 = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):

                    if 480 > mouse2[0] > 300:
                        if 570 > mouse2[1] > 500:
                            return ()

        if 480 > mouse2[0] > 300:
            if 570 > mouse2[1] > 500:
                gamedisplay.blit(imgBackAc, [300, 500])
                pygame.display.update()
            else:
                gamedisplay.blit(imgBackDe, [300, 500])
                pygame.display.update()
        else :
            gamedisplay.blit(imgBackDe, [300, 500])
            pygame.display.update()


# Renders the main screen
def colorfill(gameDisplay, a, letlist):
    if a == 1:
        gameDisplay.fill(supercolor)
        gameDisplay.blit(imgtip2, [190, 280])
        gameDisplay.blit(imgHelpDe, [20, 510])
        gameDisplay.blit(imgStartDe, [300, 400])
        keyboard = Keyboard(gameDisplay, letlist)
        pygame.display.update()
    else:
        if a == 2:
            gameDisplay.fill(supercolor)
            gameDisplay.blit(imgtip3, [217, 280])
            pygame.display.update()
        keyboard = Keyboard(gameDisplay, letlist)
    return ()


def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return (
     textSurface, textSurface.get_rect())


def GameScreen():
    pygame.init()
    gamedisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Keyboard Game')
    mediumText = pygame.font.SysFont('comicsansms', 40)
    gameExit = False
    colorfill(gamedisplay, 1, letters)
    while not gameExit:
        
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            elif event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0): # TRIGGER ON LEFT CLICK ONLY
                    ## ON START BUTTON CLICKED ##
                    if 480 > mouse[0] > 300:
                        if 470 > mouse[1] > 400:
                            StartGame(gamedisplay)
                    ## ON HELP BUTTON CLICKED ##
                    elif 90 > mouse[0] > 20:
                        if 580 > mouse[1] > 510:
                            helpPage(gamedisplay)
                            colorfill(gamedisplay, 1, letters)
                            pygame.display.update()

        # START BUTTON
        if 480 > mouse[0] > 300:
            if 470 > mouse[1] > 400:
                gamedisplay.blit(imgStartAc, [300, 400])
                pygame.display.update()
            else:
                gamedisplay.blit(imgStartDe, [300, 400])
                pygame.display.update()
        else :
            gamedisplay.blit(imgStartDe, [300, 400])
            pygame.display.update()
        #BUTTON
        if 90 > mouse[0] > 20 :
            if 580 > mouse[1] > 510:
                gamedisplay.blit(imgHelpAc, [20, 510])
                pygame.display.update()
            else:
                gamedisplay.blit(imgHelpDe, [20, 510])
                pygame.display.update()
        else :
            gamedisplay.blit(imgHelpDe, [20, 510])
            pygame.display.update()

    quit()


def StartGame(gamedisplay):

    colorfill(gamedisplay, 2, letters2)
    for i in range(15, -1, -1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                continue

        timer(gamedisplay, i)
        pygame.display.update()
        if i == 0:
            Guess(gamedisplay)
        time.sleep(1)

# RENDERS THE RANDOM WORD PICKED ##
def drawRandWord(word, display):
    xlen = 20
    for i in range(0, len(word), 1):
        display.blit(dirLetterNeutral[word[i]], [xlen, 100])
        pygame.display.update()
        xlen += 61


def oklet(letter, pos, display):
    display.blit(dirLetterCor[letter], [pos * 61 + 20, 100])
    pygame.display.update()


def wronglet(letter, pos, display):
    display.blit(dirLetterWrong[letter], [pos * 61 + 20, 100])
    pygame.display.update()

# Draws the winning or losing animation
def drawStick(display, result):

    if result == 1:
        for i in range(1, 31, 1):
            clock.tick(20)
            display.blit(imgTile, [280, 180])
            display.blit(dirStickWon[i], [150, 50])
            pygame.display.update()

    else:
        for i in range(1, 32, 1):
            clock.tick(20)
            display.blit(imgTile, [280, 180])
            display.blit(dirStickLost[i], [150, 50])
            pygame.display.update()

def Guess(gamedisplay):
    dirKeyboard = {letters2[0]: pygame.K_q,
     letters2[1]: pygame.K_w,
     letters2[2]: pygame.K_e,
     letters2[3]: pygame.K_r,
     letters2[4]: pygame.K_t,
     letters2[5]: pygame.K_y,
     letters2[6]: pygame.K_u,
     letters2[7]: pygame.K_i,
     letters2[8]: pygame.K_o,
     letters2[9]: pygame.K_p,
     letters2[10]: pygame.K_a,
     letters2[11]: pygame.K_s,
     letters2[12]: pygame.K_d,
     letters2[13]: pygame.K_f,
     letters2[14]: pygame.K_g,
     letters2[15]: pygame.K_h,
     letters2[16]: pygame.K_j,
     letters2[17]: pygame.K_k,
     letters2[18]: pygame.K_l,
     letters2[19]: pygame.K_z,
     letters2[20]: pygame.K_x,
     letters2[21]: pygame.K_c,
     letters2[22]: pygame.K_v,
     letters2[23]: pygame.K_b,
     letters2[24]: pygame.K_n,
     letters2[25]: pygame.K_m
     }
    words = [
     'YOLO', 'SWAG', 'LOL', 'HASHTAG', 'ARCHITECT', 'MAP', 'HIPSTER', 'SELFIE', 'SCHOOL', 'MUSIC', 'GAME','CHILD','COMPUTER','TEA','VOLCANO', 'KNIGHT', 'PRINCESS','JEDI']

    gamedisplay.fill(supercolor)
    pygame.display.update()
    gameExit = False
    random.shuffle(words)
    pickedWord = words[0]
    drawRandWord(pickedWord, gamedisplay)
    mouse = pygame.mouse.get_pos()
    currentletter = 0
    enable = 1
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                # RESTART THE GAME BY SHUFFLING AGAIN ##
                if event.key == K_BACKSPACE:
                    random.shuffle(letters2)
                    StartGame(gamedisplay)
            if event.type == pygame.KEYDOWN and currentletter < len(pickedWord):
                if event.key == dirKeyboard[pickedWord[currentletter]] and enable == 1:
                    oklet(pickedWord[currentletter], currentletter, gamedisplay)
                    currentletter += 1
                    if currentletter == len(pickedWord):
                        thread = Thread(target = drawStick, args = (gamedisplay,1, ))
                        thread.start()
                        pygame.display.update()
                        enable = 0
                elif event.key == K_SPACE:
                    currentletter = 0
                    enable = 1
                    gamedisplay.fill(supercolor)
                    random.shuffle(words)
                    pickedWord = words[0]
                    drawRandWord(pickedWord, gamedisplay)
                    pygame.display.update()
                else:
                    wronglet(pickedWord[currentletter], currentletter, gamedisplay)
                    enable = 0
                    thread = Thread(target = drawStick, args = (gamedisplay,0, ))
                    thread.start()
                    pygame.display.update()
            if event.type == MOUSEBUTTONDOWN and currentletter < len(pickedWord):
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if 530 > mouse[0] > 230:
                        if 520 > mouse[1] > 450:
                            currentletter = 0
                            enable = 1
                            gamedisplay.fill(supercolor)
                            drawRandWord(pickedWord, gamedisplay)
                            pygame.display.update()

        mouse = pygame.mouse.get_pos()
        if 530 > mouse[0] > 230:
            if 520 > mouse[1] > 450:
                gamedisplay.blit(imgTryAgainAc, [230, 450])
                pygame.display.update()
            else:
                gamedisplay.blit(imgTryAgainDe, [230, 450])
                pygame.display.update()
        else :
            gamedisplay.blit(imgTryAgainDe, [230, 450])
            pygame.display.update()

    pygame.quit()
    quit()


threadActive = False
white = (255, 255, 255)
black = (0, 0, 0)
supercolor = (32, 31, 41)
butbrightcolor = (102, 102, 222)
butcolor = (171, 171, 224)
numcolor = (171, 171, 224)
imgTile = pygame.image.load('img\\tile.png')
imgA = pygame.image.load('img\\A.png')
imgB = pygame.image.load('img\\B.png')
imgC = pygame.image.load('img\\C.png')
imgD = pygame.image.load('img\\D.png')
imgE = pygame.image.load('img\\E.png')
imgF = pygame.image.load('img\\F.png')
imgG = pygame.image.load('img\\G.png')
imgH = pygame.image.load('img\\H.png')
imgI = pygame.image.load('img\\I.png')
imgJ = pygame.image.load('img\\J.png')
imgK = pygame.image.load('img\\K.png')
imgL = pygame.image.load('img\\L.png')
imgM = pygame.image.load('img\\M.png')
imgN = pygame.image.load('img\\N.png')
imgO = pygame.image.load('img\\O.png')
imgP = pygame.image.load('img\\P.png')
imgQ = pygame.image.load('img\\Q.png')
imgR = pygame.image.load('img\\R.png')
imgS = pygame.image.load('img\\S.png')
imgT = pygame.image.load('img\\T.png')
imgU = pygame.image.load('img\\U.png')
imgV = pygame.image.load('img\\V.png')
imgW = pygame.image.load('img\\W.png')
imgX = pygame.image.load('img\\X.png')
imgY = pygame.image.load('img\\Y.png')
imgZ = pygame.image.load('img\\Z.png')
imgAneutral = pygame.image.load('img\\Aneutral.png')
imgBneutral = pygame.image.load('img\\Bneutral.png')
imgCneutral = pygame.image.load('img\\Cneutral.png')
imgDneutral = pygame.image.load('img\\Dneutral.png')
imgEneutral = pygame.image.load('img\\Eneutral.png')
imgFneutral = pygame.image.load('img\\Fneutral.png')
imgGneutral = pygame.image.load('img\\Gneutral.png')
imgHneutral = pygame.image.load('img\\Hneutral.png')
imgIneutral = pygame.image.load('img\\Ineutral.png')
imgJneutral = pygame.image.load('img\\Jneutral.png')
imgKneutral = pygame.image.load('img\\Kneutral.png')
imgLneutral = pygame.image.load('img\\Lneutral.png')
imgMneutral = pygame.image.load('img\\Mneutral.png')
imgNneutral = pygame.image.load('img\\Nneutral.png')
imgOneutral = pygame.image.load('img\\Oneutral.png')
imgPneutral = pygame.image.load('img\\Pneutral.png')
imgQneutral = pygame.image.load('img\\Qneutral.png')
imgRneutral = pygame.image.load('img\\Rneutral.png')
imgSneutral = pygame.image.load('img\\Sneutral.png')
imgTneutral = pygame.image.load('img\\Tneutral.png')
imgUneutral = pygame.image.load('img\\Uneutral.png')
imgVneutral = pygame.image.load('img\\Vneutral.png')
imgWneutral = pygame.image.load('img\\Wneutral.png')
imgXneutral = pygame.image.load('img\\Xneutral.png')
imgYneutral = pygame.image.load('img\\Yneutral.png')
imgZneutral = pygame.image.load('img\\Zneutral.png')
imgAcor = pygame.image.load('img\\Acor.png')
imgBcor = pygame.image.load('img\\Bcor.png')
imgCcor = pygame.image.load('img\\Ccor.png')
imgDcor = pygame.image.load('img\\Dcor.png')
imgEcor = pygame.image.load('img\\Ecor.png')
imgFcor = pygame.image.load('img\\Fcor.png')
imgGcor = pygame.image.load('img\\Gcor.png')
imgHcor = pygame.image.load('img\\Hcor.png')
imgIcor = pygame.image.load('img\\Icor.png')
imgJcor = pygame.image.load('img\\Jcor.png')
imgKcor = pygame.image.load('img\\Kcor.png')
imgLcor = pygame.image.load('img\\Lcor.png')
imgMcor = pygame.image.load('img\\Mcor.png')
imgNcor = pygame.image.load('img\\Ncor.png')
imgOcor = pygame.image.load('img\\Ocor.png')
imgPcor = pygame.image.load('img\\Pcor.png')
imgQcor = pygame.image.load('img\\Qcor.png')
imgRcor = pygame.image.load('img\\Rcor.png')
imgScor = pygame.image.load('img\\Scor.png')
imgTcor = pygame.image.load('img\\Tcor.png')
imgUcor = pygame.image.load('img\\Ucor.png')
imgVcor = pygame.image.load('img\\Vcor.png')
imgWcor = pygame.image.load('img\\Wcor.png')
imgXcor = pygame.image.load('img\\Xcor.png')
imgYcor = pygame.image.load('img\\Ycor.png')
imgZcor = pygame.image.load('img\\Zcor.png')
imgAwrong = pygame.image.load('img\\Awrong.png')
imgBwrong = pygame.image.load('img\\Bwrong.png')
imgCwrong = pygame.image.load('img\\Cwrong.png')
imgDwrong = pygame.image.load('img\\Dwrong.png')
imgEwrong = pygame.image.load('img\\Ewrong.png')
imgFwrong = pygame.image.load('img\\Fwrong.png')
imgGwrong = pygame.image.load('img\\Gwrong.png')
imgHwrong = pygame.image.load('img\\Hwrong.png')
imgIwrong = pygame.image.load('img\\Iwrong.png')
imgJwrong = pygame.image.load('img\\Jwrong.png')
imgKwrong = pygame.image.load('img\\Kwrong.png')
imgLwrong = pygame.image.load('img\\Lwrong.png')
imgMwrong = pygame.image.load('img\\Mwrong.png')
imgNwrong = pygame.image.load('img\\Nwrong.png')
imgOwrong = pygame.image.load('img\\Owrong.png')
imgPwrong = pygame.image.load('img\\Pwrong.png')
imgQwrong = pygame.image.load('img\\Qwrong.png')
imgRwrong = pygame.image.load('img\\Rwrong.png')
imgSwrong = pygame.image.load('img\\Swrong.png')
imgTwrong = pygame.image.load('img\\Twrong.png')
imgUwrong = pygame.image.load('img\\Uwrong.png')
imgVwrong = pygame.image.load('img\\Vwrong.png')
imgWwrong = pygame.image.load('img\\Wwrong.png')
imgXwrong = pygame.image.load('img\\Xwrong.png')
imgYwrong = pygame.image.load('img\\Ywrong.png')
imgZwrong = pygame.image.load('img\\Zwrong.png')
imgwon1 = pygame.image.load('img\\won1.png')
imgwon2 = pygame.image.load('img\\won2.png')
imgwon3 = pygame.image.load('img\\won3.png')
imgwon4 = pygame.image.load('img\\won4.png')
imgwon5 = pygame.image.load('img\\won5.png')
imgwon6 = pygame.image.load('img\\won6.png')
imgwon7 = pygame.image.load('img\\won7.png')
imgwon8 = pygame.image.load('img\\won8.png')
imgwon9 = pygame.image.load('img\\won9.png')
imgwon10 = pygame.image.load('img\\won10.png')
imgwon11 = pygame.image.load('img\\won11.png')
imgwon12 = pygame.image.load('img\\won12.png')
imgwon13 = pygame.image.load('img\\won13.png')
imgwon14 = pygame.image.load('img\\won14.png')
imgwon15 = pygame.image.load('img\\won15.png')
imgwon16 = pygame.image.load('img\\won16.png')
imgwon17 = pygame.image.load('img\\won17.png')
imgwon18 = pygame.image.load('img\\won18.png')
imgwon19 = pygame.image.load('img\\won19.png')
imgwon20 = pygame.image.load('img\\won20.png')
imgwon21 = pygame.image.load('img\\won21.png')
imgwon22 = pygame.image.load('img\\won22.png')
imgwon23 = pygame.image.load('img\\won23.png')
imgwon24 = pygame.image.load('img\\won24.png')
imgwon25 = pygame.image.load('img\\won25.png')
imgwon26 = pygame.image.load('img\\won26.png')
imgwon27 = pygame.image.load('img\\won27.png')
imgwon28 = pygame.image.load('img\\won28.png')
imgwon29 = pygame.image.load('img\\won29.png')
imgwon30 = pygame.image.load('img\\won30.png')
imgwon31 = pygame.image.load('img\\won31.png')
imglost1 = pygame.image.load('img\\lost1.png')
imglost2 = pygame.image.load('img\\lost2.png')
imglost3 = pygame.image.load('img\\lost3.png')
imglost4 = pygame.image.load('img\\lost4.png')
imglost5 = pygame.image.load('img\\lost5.png')
imglost6 = pygame.image.load('img\\lost6.png')
imglost7 = pygame.image.load('img\\lost7.png')
imglost8 = pygame.image.load('img\\lost8.png')
imglost9 = pygame.image.load('img\\lost9.png')
imglost10 = pygame.image.load('img\\lost10.png')
imglost11 = pygame.image.load('img\\lost11.png')
imglost12 = pygame.image.load('img\\lost12.png')
imglost13 = pygame.image.load('img\\lost13.png')
imglost14 = pygame.image.load('img\\lost14.png')
imglost15 = pygame.image.load('img\\lost15.png')
imglost16 = pygame.image.load('img\\lost16.png')
imglost17 = pygame.image.load('img\\lost17.png')
imglost18 = pygame.image.load('img\\lost18.png')
imglost19 = pygame.image.load('img\\lost19.png')
imglost20 = pygame.image.load('img\\lost20.png')
imglost21 = pygame.image.load('img\\lost21.png')
imglost22 = pygame.image.load('img\\lost22.png')
imglost23 = pygame.image.load('img\\lost23.png')
imglost24 = pygame.image.load('img\\lost24.png')
imglost25 = pygame.image.load('img\\lost25.png')
imglost26 = pygame.image.load('img\\lost26.png')
imglost27 = pygame.image.load('img\\lost27.png')
imglost28 = pygame.image.load('img\\lost28.png')
imglost29 = pygame.image.load('img\\lost29.png')
imglost30 = pygame.image.load('img\\lost30.png')
imglost31 = pygame.image.load('img\\lost31.png')
imglost32 = pygame.image.load('img\\lost32.png')
imgStartAc = pygame.image.load('img\\StartAc.png')
imgStartDe = pygame.image.load('img\\StartDe.png')
imgTryAgainAc = pygame.image.load('img\\TryAgainAc.png')
imgTryAgainDe = pygame.image.load('img\\TryAgainDe.png')
imgDIRECT = pygame.image.load('img\\DIRECT.png')
imgHelpAc = pygame.image.load('img\\HelpAc.png')
imgHelpDe = pygame.image.load('img\\HelpDe.png')
imgBackDe = pygame.image.load('img\\BackDe.png')
imgBackAc = pygame.image.load('img\\BackAc.png')

letters = [
 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
letters2 = my_shuffle(letters)
imgtip2 = pygame.image.load('img\\tip2.png')
imgtip3 = pygame.image.load('img\\tip3.png')
clock = pygame.time.Clock()
result = 99
pygame.mixer.pre_init(44100, 16, 2, 4096)
dirStickWon = {1: imgwon1,
 2: imgwon2,
 3: imgwon3,
 4: imgwon4,
 5: imgwon5,
 6: imgwon6,
 7: imgwon7,
 8: imgwon8,
 9: imgwon9,
 10: imgwon10,
 11: imgwon11,
 12: imgwon12,
 13: imgwon13,
 14: imgwon14,
 15: imgwon15,
 16: imgwon16,
 17: imgwon17,
 18: imgwon18,
 19: imgwon19,
 20: imgwon20,
 21: imgwon21,
 22: imgwon22,
 23: imgwon23,
 24: imgwon24,
 25: imgwon25,
 26: imgwon26,
 27: imgwon27,
 28: imgwon28,
 29: imgwon29,
 30: imgwon30,
 31: imgwon31
 }
dirStickLost = {1: imglost1,
 2: imglost2,
 3: imglost3,
 4: imglost4,
 5: imglost5,
 6: imglost6,
 7: imglost7,
 8: imglost8,
 9: imglost9,
 10: imglost10,
 11: imglost11,
 12: imglost12,
 13: imglost13,
 14: imglost14,
 15: imglost15,
 16: imglost16,
 17: imglost17,
 18: imglost18,
 19: imglost19,
 20: imglost20,
 21: imglost21,
 22: imglost22,
 23: imglost23,
 24: imglost24,
 25: imglost25,
 26: imglost26,
 27: imglost27,
 28: imglost28,
 29: imglost29,
 30: imglost30,
 31: imglost31,
 32: imglost32
 }
dirImg = {'A': imgA,
 'B': imgB,
 'C': imgC,
 'D': imgD,
 'E': imgE,
 'F': imgF,
 'G': imgG,
 'H': imgH,
 'I': imgI,
 'J': imgJ,
 'K': imgK,
 'L': imgL,
 'M': imgM,
 'N': imgN,
 'O': imgO,
 'P': imgP,
 'Q': imgQ,
 'R': imgR,
 'S': imgS,
 'T': imgT,
 'U': imgU,
 'V': imgV,
 'W': imgW,
 'X': imgX,
 'Y': imgY,
 'Z': imgZ
 }
dirLetterNeutral = {'A': imgAneutral,
 'B': imgBneutral,
 'C': imgCneutral,
 'D': imgDneutral,
 'E': imgEneutral,
 'F': imgFneutral,
 'G': imgGneutral,
 'H': imgHneutral,
 'I': imgIneutral,
 'J': imgJneutral,
 'K': imgKneutral,
 'L': imgLneutral,
 'M': imgMneutral,
 'N': imgNneutral,
 'O': imgOneutral,
 'P': imgPneutral,
 'Q': imgQneutral,
 'R': imgRneutral,
 'S': imgSneutral,
 'T': imgTneutral,
 'U': imgUneutral,
 'V': imgVneutral,
 'W': imgWneutral,
 'X': imgXneutral,
 'Y': imgYneutral,
 'Z': imgZneutral
 }
dirLetterCor = {'A': imgAcor,
 'B': imgBcor,
 'C': imgCcor,
 'D': imgDcor,
 'E': imgEcor,
 'F': imgFcor,
 'G': imgGcor,
 'H': imgHcor,
 'I': imgIcor,
 'J': imgJcor,
 'K': imgKcor,
 'L': imgLcor,
 'M': imgMcor,
 'N': imgNcor,
 'O': imgOcor,
 'P': imgPcor,
 'Q': imgQcor,
 'R': imgRcor,
 'S': imgScor,
 'T': imgTcor,
 'U': imgUcor,
 'V': imgVcor,
 'W': imgWcor,
 'X': imgXcor,
 'Y': imgYcor,
 'Z': imgZcor
 }
dirLetterWrong = {'A': imgAwrong,
 'B': imgBwrong,
 'C': imgCwrong,
 'D': imgDwrong,
 'E': imgEwrong,
 'F': imgFwrong,
 'G': imgGwrong,
 'H': imgHwrong,
 'I': imgIwrong,
 'J': imgJwrong,
 'K': imgKwrong,
 'L': imgLwrong,
 'M': imgMwrong,
 'N': imgNwrong,
 'O': imgOwrong,
 'P': imgPwrong,
 'Q': imgQwrong,
 'R': imgRwrong,
 'S': imgSwrong,
 'T': imgTwrong,
 'U': imgUwrong,
 'V': imgVwrong,
 'W': imgWwrong,
 'X': imgXwrong,
 'Y': imgYwrong,
 'Z': imgZwrong
 }

GameScreen()
