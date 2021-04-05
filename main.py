
"""
AUTHOR: KHALED BADRAN
"""

import pygame 
import button 

pygame.init()

# Defining some important constants and variables:-
#############################################
(WIDTH, HEIGHT) = (600, 700)
DISPLAY_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
OFFSET_HEIGHT_UP = 100

BUTTON_COLOR = (4, 30, 66) #Sailor Blue
BUTTON_HOVER_OVER_COLOR = (249, 87, 0) #Orange 
TEXT_COLOR = (249, 87, 0)
BUTTON_TEXT_HOVER_OVER_COLOR = (4, 30, 66)
BUTTON_BORDER_COLOR = (95, 95, 96) #Grey
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
WHITE = (255,255,255)

x_coordinate_of_buttons = WIDTH/2 - BUTTON_WIDTH//2

background_img = pygame.image.load("images/background.png")
icon_img = pygame.image.load("images/icon.png")
horizontal_line_img = pygame.image.load("images/horizontal_line.png")
vertical_line_img = pygame.image.load("images/vertical_line.png")

#############################################

pygame.display.set_icon(icon_img)
pygame.display.set_caption("Tic-tac-toe")


def blit_text(txt: str, font_size, pos, color):
    """ to draw a text on the display_screen/display_window.
    Args:
        txt (str): text to be blitted
        font_size (int): size of the font.
        pos ((int,int) tuple): position of the text to be blitted.
        color ((R,G,B) tuple): color of the text
    """
    font = pygame.font.Font("freesansbold.ttf", font_size)
    text = font.render(txt, True, color)
    DISPLAY_SCREEN.blit(text, pos)


def craete_introduction_buttons():
    """ create the PLAY button and QUIT button 
    Returns: 
        Tuple: tuple of the created buttons 
    """    
    play_button = button.Button(BUTTON_COLOR, BUTTON_HOVER_OVER_COLOR, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT_COLOR, BUTTON_TEXT_HOVER_OVER_COLOR, "PLAY")
    quit_button = button.Button(BUTTON_COLOR, BUTTON_HOVER_OVER_COLOR, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT_COLOR, BUTTON_TEXT_HOVER_OVER_COLOR, "QUIT")

    #fix the position of the buttons based on their sizes:-
    play_button.x = x_coordinate_of_buttons
    play_button.y = HEIGHT/2 

    quit_button.x = x_coordinate_of_buttons
    quit_button.y = play_button.y+BUTTON_HEIGHT+10

    return (play_button, quit_button)


def start_intro(status = ""):
    (play_button, quit_button) = craete_introduction_buttons()

    run = True
    while run:
        DISPLAY_SCREEN.blit(background_img, (0, 0))
        play_button.blit(DISPLAY_SCREEN, BUTTON_BORDER_COLOR)
        quit_button.blit(DISPLAY_SCREEN, BUTTON_BORDER_COLOR)
        
        mouse_position = pygame.mouse.get_pos() # get the position of the mouse
        if status: # to blit the current score and best score  
            height_for_txt = HEIGHT/3  
            blit_text(status, 25, (WIDTH/2-100, height_for_txt), WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if play_button.is_clicked(mouse_position, event):
                run = False # to stop running the introductory screen
                start_game()
            if quit_button.is_clicked(mouse_position, event):
                pygame.quit()


        # change the color of the buttons when the player/user hovers over them.
        if play_button.is_hovered_over(mouse_position):
            play_button.blit_hovered_over(DISPLAY_SCREEN)
        elif quit_button.is_hovered_over(mouse_position):
            quit_button.blit_hovered_over(DISPLAY_SCREEN)

        
        pygame.display.update()


def draw_playing_field(lines):

    run_animation = True
    while run_animation:
        DISPLAY_SCREEN.blit(background_img, (0, 0))
        pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        #to draw the playing_field in an animated way in the beginning
        if lines["horizontal1_x"] < 0:
            lines["horizontal1_x"] += 0.6
        if lines["horizontal2_x"] > 0:
            lines["horizontal2_x"] -= 0.6
        
        if lines["vertical1_x"] < (WIDTH/3):
            lines["vertical1_x"] += 0.2
        if lines["vertical2_x"] > (WIDTH/3)*2:
            lines["vertical2_x"] -= 0.2

        DISPLAY_SCREEN.blit(horizontal_line_img, (lines["horizontal1_x"], lines["horizontal1_y"]))
        DISPLAY_SCREEN.blit(horizontal_line_img, (lines["horizontal2_x"], lines["horizontal2_y"]))
        DISPLAY_SCREEN.blit(vertical_line_img, (lines["vertical1_x"], lines["vertical1_y"]))
        DISPLAY_SCREEN.blit(vertical_line_img, (lines["vertical2_x"], lines["vertical2_y"]))

        if lines["horizontal1_x"] >= 0 and lines["horizontal2_x"] <= 0 and lines["vertical1_x"] >= (WIDTH/3) and lines["vertical2_x"] <= (WIDTH/3)*2:
            run_animation = False

        pygame.display.update()


def start_game():
    #horizontal lines
    horizontal1_x = -600 # first horizontal line. It comes from the left side
    horizontal1_y = OFFSET_HEIGHT_UP + ((HEIGHT-OFFSET_HEIGHT_UP)/3)
    horizontal2_x = WIDTH # second horizontal line. It comes from the right side
    horizontal2_y = horizontal1_y + ((HEIGHT-OFFSET_HEIGHT_UP)/3)
    #vertical lines
    vertical1_x = 0 # first vertical line. It comes from the left side
    vertical1_y = OFFSET_HEIGHT_UP
    vertical2_x = WIDTH # second vertical line. It comes from the right side
    vertical2_y = OFFSET_HEIGHT_UP
    lines = { #dictionat of the lines
        "horizontal1_x": horizontal1_x,
        "horizontal1_y": horizontal1_y,
        "horizontal2_x": horizontal2_x,
        "horizontal2_y": horizontal2_y, 
        "vertical1_x": vertical1_x,
        "vertical1_y": vertical1_y,
        "vertical2_x": vertical2_x,
        "vertical2_y": vertical2_y
    }
    
    while True:
        DISPLAY_SCREEN.blit(background_img, (0, 0))

        pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        draw_playing_field(lines)
        pygame.display.update()


def main():
    start_intro()


if __name__ == "__main__":  #to avoid runing the game, if this file is imported
    main()
