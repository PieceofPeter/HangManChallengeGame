import pygame, sys, random
from timeit import default_timer as timer

# display settings
fps = 30
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# colours for later use
black = (0, 0, 0)
white = (255, 255, 255)
lightred = (255, 165, 145)
darklightred = (255, 97, 81)
lightblue = (126, 178, 255)
darklightblue = (42, 129, 255)
lightgrey = (192, 192, 192)

textBoxSpace = 5
textBoxNumber = 0

# intro menu
def intro(x, y):
    colour = (0, 0, 0)
    screen.fill((255, 255, 255))
    introText = pygame.font.SysFont("comicsansms", 32)
    text = introText.render("HANGMAN", True, colour) # caption and titles for intro
    text2 = introText.render("Luke & Liam", True, colour)
    text3 = introText.render("Press Space to Continue....", True, colour)
    screen.blit(text, ((x / 1.8) - 1, y)) # blits it onto screen
    screen.blit(text2, ((x / 1.8) - 40, (y + 70)))
    screen.blit(text3, ((x - 365), (y + 300)))
    pygame.display.update()

def button(word, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # code for button and button pressed
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    buttonText = pygame.font.SysFont("comicsansms", 20)
    buttonTextSurf = buttonText.render(word, True, white)
    buttonTextRect = buttonTextSurf.get_rect()
    buttonTextRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(buttonTextSurf, buttonTextRect)

# code for the End Game pop up
def newGame():
    global textBoxSpace, textBoxNumber, end, start
    end = timer()
    timeTaken = (end - start) # calculates time
    textBoxSpace = 5
    textBoxNumber = 0
    message = "Time taken: " + str(round(timeTaken)) + "s"
    word_find = 'The Word Was: ' + str(pick)
    while True: # quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        button("Yes", (width / 2) - 50, 420, 100, 50, darklightred, lightred, hangman) # end game yes and no
        button("No", (width / 2) - 50, 500, 100, 50, darklightred, lightred, quitGame)

        # title
        largeText = pygame.font.SysFont("comicsansms", 55)
        TextSurf = largeText.render("New Game?", True, darklightred)
        TextRect = TextSurf.get_rect()
        TextRect.center = (width / 2, height / 2)
        screen.blit(TextSurf, TextRect)

        # the message
        textSurf = largeText.render(message, True, darklightred)
        textRect = textSurf.get_rect()
        textRect.center = (width / 2, 200)
        screen.blit(textSurf, textRect)

        # displays word
        textSurf = largeText.render(word_find, True, darklightred)
        textRect = textSurf.get_rect()
        textRect.center = (width / 2, 100)
        screen.blit(textSurf, textRect)

        pygame.display.update()
        clock.tick(fps)

# quits out of game
def quitGame():
    pygame.quit()
    sys.exit()

# code to use for displaying text
def textObjects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# clock to track time
def main():
    global clock, screen, play
    play = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    # caption
    pygame.display.set_caption("Hangman by Luke and Liam")

    # runs until quit
    while True:
        hangman()

# code for placing a letter on the board
def placeLetter(letter):
    global pick, pickSplit
    space = 10
    wordSpace = 0
    while wordSpace < len(pick):
        text = pygame.font.SysFont('comicsansms', 40)
        if letter in pickSplit[wordSpace]: # splits into letters and put it into a list
            textSurf = text.render(letter, True, black)
            textRect = textSurf.get_rect()
            textRect.center = (((150) + space), (200))
            screen.blit(textSurf, textRect)
        wordSpace += 1
        space += 60

    pygame.display.update()
    clock.tick(fps)

# box that used letters are in
def textBoxLetter(letter):
    global textBoxSpace, textBoxNumber
    # code for displaying different ROWS of letters instead of going outside of box
    if textBoxNumber <= 5:
        text = pygame.font.SysFont("comicsansms", 40)
        textSurf = text.render(letter, True, black)
        textRect = textSurf.get_rect()
        textRect.center = (((105) + textBoxSpace), (350))
        screen.blit(textSurf, textRect)

    # row 2
    elif textBoxNumber <= 10:
        text = pygame.font.SysFont("comicsansms", 40)
        textSurf = text.render(letter, True, black)
        textRect = textSurf.get_rect()
        textRect.center = (((105) + textBoxSpace), (400))
        screen.blit(textSurf, textRect)

    elif textBoxNumber <= 15:
        text = pygame.font.SysFont("comicsansms", 40)
        textSurf = text.render(letter, True, black)
        textRect = textSurf.get_rect()
        textRect.center = (((105) + textBoxSpace), (450))
        screen.blit(textSurf, textRect)

    # row 3
    elif textBoxNumber <= 20:
        text = pygame.font.SysFont("comicsansms", 40)
        textSurf = text.render(letter, True, black)
        textRect = textSurf.get_rect()
        textRect.center = (((105) + textBoxSpace), (500))
        screen.blit(textSurf, textRect)

    pygame.display.update()
    clock.tick(fps)

# main code
def hangman():
    global textBoxSpace, textBoxNumber
    textBoxSpace = 5
    textBoxNumber = 0

    while play == True:
        # event grab quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(white)
        space = 10
        textBoxSpace = 5

        # difficulty and buttons
        text = pygame.font.SysFont("comicsansms", 20)
        textSurf = text.render("CHOOSE DIFFICULTY", True, black)
        textRect = textSurf.get_rect()
        textRect.center = ((width / 2), (height / 2))
        screen.blit(textSurf, textRect)

        # button displays
        button("Hard", 150, 450, 150, 100, black, lightgrey, Hard)
        button("Insane", 550, 450, 150, 100, black, lightgrey, Insane)
        button("Easy", 150, 50, 150, 100, black, lightgrey, Easy)
        button("Medium", 550, 50, 150, 100, black, lightgrey, Medium)

        pygame.display.update()
        clock.tick(fps)

# MAIN game code
def hangmanGame(catagory, title):
    global pause, pick, pickSplit, textBoxSpace, textBoxNumber, start
    start = timer()
    chances = 8
    pick = random.choice(catagory)
    pickSplit = [pick[i:i + 1] for i in range(0, len(pick), 1)]

    screen.fill(white)

    wordSpace = 0
    space = 10
    # code for the spaces and leng of the word
    while wordSpace < len(pick):
        text = pygame.font.SysFont("comicsansms", 40)
        textSurf1 = text.render("_", True, black)
        textRect1 = textSurf1.get_rect()
        textRect1.center = (((150) + space), (200))
        screen.blit(textSurf1, textRect1)
        space = space + 60
        wordSpace += 1

    guesses = ''
    gamePlay = True
    while gamePlay == True:
        guessLett = ''

        # sounds
        yes = pygame.mixer.Sound('yes.mp3')
        pygame.mixer.Sound.set_volume(yes,0.6)

        no = pygame.mixer.Sound('no.mp3')
        pygame.mixer.Sound.set_volume(no,0.6)

        # code for the rows
        if textBoxNumber == 5:
            textBoxSpace = 5
        if textBoxNumber == 10:
            textBoxSpace = 5
        if textBoxNumber == 15:
            textBoxSpace = 5

        # displayes chances in top right
        pygame.draw.rect(screen, white, [550, 20, 200, 20])
        text = pygame.font.SysFont("comicsansms", 20)
        textSurf = text.render(("Chances: %s" % chances), False, black)
        textRect = textSurf.get_rect()
        textRect.topright = (700, 20)
        screen.blit(textSurf, textRect)

        textTitle = pygame.font.SysFont("comicsansms", 40)
        textTitleSurf = textTitle.render(title, True, black)
        textTitleRect = textTitleSurf.get_rect()
        textTitleRect.center = ((width / 2), 50)
        screen.blit(textTitleSurf, textTitleRect)
        pygame.draw.rect(screen, black, [100, 300, 250, 250], 2)

        # code for drawing the hangman and different things that come with it
        if chances == 8:
            pygame.draw.rect(screen, black, [450, 550, 100, 10])
            pygame.draw.rect(screen, black, [550, 550, 100, 10])
            pygame.draw.rect(screen, black, [650, 550, 100, 10])
            pygame.draw.rect(screen, black, [500, 450, 10, 100])
            pygame.draw.rect(screen, black, [500, 350, 10, 100])
            pygame.draw.rect(screen, black, [500, 250, 10, 100])
            pygame.draw.rect(screen, black, [500, 250, 150, 10])
            pygame.draw.rect(screen, black, [600, 250, 100, 10])
            pygame.draw.rect(screen, black, [600, 250, 10, 50])
            pygame.draw.line(screen, black, [505, 505], [550, 550], 10)
            pygame.draw.line(screen, black, [550, 250], [505, 295], 10)
            pygame.draw.line(screen, black, [505, 505], [460, 550], 10)

        # drawing actual hangman
        elif chances == 7:
            pygame.draw.circle(screen, black, [605, 325], 30)
        elif chances == 6:
            pygame.draw.rect(screen, black, [600, 350, 10, 60])
        elif chances == 5:
            pygame.draw.rect(screen, black, [600, 410, 10, 60])
        elif chances == 4:
            pygame.draw.line(screen, black, [605, 375], [550, 395], 10)
        elif chances == 3:
            pygame.draw.line(screen, black, [605, 375], [650, 395], 10)
        elif chances == 2:
            pygame.draw.line(screen, black, [605, 465], [550, 485], 10)
        elif chances == 1:
            pygame.draw.line(screen, black, [605, 465], [650, 485], 10)

        # backbutton and highlight
        button("Back", 50, 50, 100, 50, black, lightgrey, hangman)

        # different events that can happen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                failed = 0

                # CODE FOR ALL LETTERS TO BE PLACED, BE CORRECT, BE WRONG AND PLAY SOUND
                if event.key == pygame.K_a:
                    # letter a
                    guessLett = guessLett + 'a'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('a')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('a')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_b:
                    # letter b
                    guessLett = guessLett + 'b'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('b')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('b')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_c:
                    # letter c
                    guessLett = guessLett + 'c'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('c')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('c')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_d:
                    # letter d
                    guessLett = guessLett + 'd'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('d')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('d')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_e:
                    # letter e
                    guessLett = guessLett + 'e'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('e')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('e')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_f:
                    # letter f
                    guessLett = guessLett + 'f'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('f')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('f')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_g:
                    # letter g
                    guessLett = guessLett + 'g'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('g')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('g')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_h:
                    # letter h
                    guessLett = guessLett + 'h'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('h')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('h')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_i:
                    # letter i
                    guessLett = guessLett + 'i'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('i')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('i')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_j:
                    # letter j
                    guessLett = guessLett + 'j'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('j')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('j')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_k:
                    # letter k
                    guessLett = guessLett + 'k'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('k')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('k')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_l:
                    # letter l
                    guessLett = guessLett + 'l'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('l')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('l')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_m:
                    # letter m
                    guessLett = guessLett + 'm'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('m')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('m')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_n:
                    # letter n
                    guessLett = guessLett + 'n'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('n')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('n')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_o:
                    # letter o
                    guessLett = guessLett + 'o'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('o')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('o')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_p:
                    # letter p
                    guessLett = guessLett + 'p'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('p')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('p')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_q:
                    # letter q
                    guessLett = guessLett + 'q'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('q')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('q')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_r:
                    # letter r
                    guessLett = guessLett + 'r'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('r')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('r')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_s:
                    # letter s
                    guessLett = guessLett + 's'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('s')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('s')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_t:
                    # letter t
                    guessLett = guessLett + 't'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('t')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('t')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_u:
                    # letter u
                    guessLett = guessLett + 'u'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('u')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('u')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_v:
                    # letter v
                    guessLett = guessLett + 'v'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('v')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('v')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_w:
                    # letter w
                    guessLett = guessLett + 'w'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('w')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('w')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_x:
                    # letter x
                    guessLett = guessLett + 'x'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('x')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('x')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_y:
                    # letter y
                    guessLett = guessLett + 'y'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('y')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('y')

                    if chances == 0:
                        newGame()

                if event.key == pygame.K_z:
                    # letter z
                    guessLett = guessLett + 'z'
                    guesses += guessLett

                    for char in pick:
                        if char not in guesses:
                            failed += 1

                    if guessLett in pick:
                        pygame.mixer.Sound.play(yes)
                        placeLetter('z')

                    if failed == 0:
                        newGame()

                    if guessLett not in pick:
                        textBoxSpace += 40
                        textBoxNumber += 1
                        chances = chances - 1
                        pygame.mixer.Sound.play(no)
                        textBoxLetter('z')

                    if chances == 0:
                        newGame()

        pygame.display.update()
        clock.tick(fps)

    pygame.display.update()
    clock.tick(fps)

# different difficulites
def Insane():
    insane = []
    # each of these are text files that scan and put all the words from them into a list
    with open('insane.txt', 'r') as file:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                # displaying the words
                word2 = word.lower() # changes to all lower case
                insane.append(word2)

    title = "Insane"
    hangmanGame(insane, title)

def Hard():
    # hard text file
    hard = []
    with open('hard.txt', 'r') as file:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                # displaying the words
                hard.append(word)

    title = "Hard"
    hangmanGame(hard, title)


def Medium():
    # med text file
    med = []
    with open('medium.txt', 'r') as file:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                # displaying the words
                med.append(word)

    title = "Medium"
    hangmanGame(med, title)

def Easy():
    # easy text file
    easy = []
    with open('easy.txt', 'r') as file:
        # reading each line
        for line in file:
            # reading each word
            for word in line.split():
                # displaying the words
                easy.append(word)

    title = "Easy"
    hangmanGame(easy, title)

# main code
if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # space to go to game
                    pygame.mixer.music.load('main.mp3') # music
                    pygame.mixer.music.set_volume(0.2)
                    pygame.mixer.music.play(-1)
                    main() # main game func

            if event.type == pygame.QUIT: # quits game
                running = False

        intro(600, 175) # splashcreen co-ordinates
