
"""
AUTHOR: KHALED BADRAN
"""

import pygame 
import buttons 
import random
import time

pygame.init()

# Defining some important constants and variables:-
#############################################
(WIDTH, HEIGHT) = (600, 700)
DISPLAY_SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
OFFSET_HEIGHT_UP = 100

BUTTON_COLOR= TILE_OCCUPIED_COLOR = (4, 30, 66) #Sailor Blue
BUTTON_HOVER_OVER_COLOR= TILE_HOVER_OVER_COLOR = (249, 87, 0) #Orange 
TEXT_COLOR = (249, 87, 0)
BUTTON_TEXT_HOVER_OVER_COLOR = (4, 30, 66)
BUTTON_BORDER_COLOR = (95, 95, 96) #Grey
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
WHITE = (255,255,255)
TILE_WIDTH = 195
TILE_Height = 195
 

x_coordinate_of_buttons = WIDTH/2 - BUTTON_WIDTH//2

background_img = pygame.image.load("images/background.png")
icon_img = pygame.image.load("images/icon.png")
horizontal_line_img = pygame.image.load("images/horizontal_line.png")
vertical_line_img = pygame.image.load("images/vertical_line.png")
x_img = pygame.image.load("images/x.png")
o_img = pygame.image.load("images/o.png")
player_x_img = pygame.image.load("images/player_x.png")
player_o_img = pygame.image.load("images/player_o.png")
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
    play_button = buttons.Button(BUTTON_COLOR, BUTTON_HOVER_OVER_COLOR, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT_COLOR, BUTTON_TEXT_HOVER_OVER_COLOR, "PLAY")
    quit_button = buttons.Button(BUTTON_COLOR, BUTTON_HOVER_OVER_COLOR, 0, 0, BUTTON_WIDTH, BUTTON_HEIGHT, TEXT_COLOR, BUTTON_TEXT_HOVER_OVER_COLOR, "QUIT")

    #fix the position of the buttons based on their sizes:-
    play_button.x = x_coordinate_of_buttons
    play_button.y = HEIGHT/2 

    quit_button.x = x_coordinate_of_buttons
    quit_button.y = play_button.y+BUTTON_HEIGHT+10

    return (play_button, quit_button)


def select_player():  
    player_x_button = buttons.SelectPlayerButton(-300, OFFSET_HEIGHT_UP+3, 300-3, HEIGHT-OFFSET_HEIGHT_UP-5, BUTTON_COLOR, BUTTON_HOVER_OVER_COLOR, player_x_img)
    player_o_button = buttons.SelectPlayerButton(600, OFFSET_HEIGHT_UP+3, 300-3, HEIGHT-OFFSET_HEIGHT_UP-5, BUTTON_COLOR, BUTTON_HOVER_OVER_COLOR, player_o_img)

    while True:
        DISPLAY_SCREEN.blit(background_img, (0, 0))
        pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line

        #to draw the buttons inan animated way
        while player_x_button.x < 0 or player_o_button.x > WIDTH/2:
            DISPLAY_SCREEN.blit(background_img, (0, 0))
            pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            #to draw the playing_field in an animated way in the beginning
            player_x_button.x += 1
            player_o_button.x -= 1
            
            player_x_button.blit(DISPLAY_SCREEN)
            player_o_button.blit(DISPLAY_SCREEN)
            pygame.display.update()

    
        mouse_position = pygame.mouse.get_pos() # get the position of the mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                player_x_button.is_clicked(mouse_position)
                player_o_button.is_clicked(mouse_position)

        player_x_button.blit(DISPLAY_SCREEN, mouse_position)
        player_o_button.blit(DISPLAY_SCREEN, mouse_position)
        pygame.display.update()

        if player_x_button.selected or player_o_button.selected:
            
            if player_x_button.selected:
                player_img = x_img
                computer_img = o_img
            else:
                player_img = o_img
                computer_img = x_img

            while player_x_button.x > 0 or player_o_button.x < WIDTH:
                DISPLAY_SCREEN.blit(background_img, (0, 0))
                pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                #to draw the playing_field in an animated way in the beginning
                player_x_button.x -= 1
                player_o_button.x += 1 
                
                player_x_button.blit(DISPLAY_SCREEN)
                player_o_button.blit(DISPLAY_SCREEN)
                pygame.display.update()

            start_game(player_img, computer_img)


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
                select_player()
            if quit_button.is_clicked(mouse_position, event):
                pygame.quit()


        # change the color of the buttons when the player/user hovers over them.
        if play_button.is_hovered_over(mouse_position):
            play_button.blit_hovered_over(DISPLAY_SCREEN)
        elif quit_button.is_hovered_over(mouse_position):
            quit_button.blit_hovered_over(DISPLAY_SCREEN)

        
        pygame.display.update()


def draw_playing_field(lines, tiles, player_img, computer_img, event=None):

    while lines["horizontal1_x"] <= 0 or lines["horizontal2_x"] >= 0 or lines["vertical1_x"] <= (WIDTH/3) or lines["vertical2_x"] >= (WIDTH/3)*2:
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

        DISPLAY_SCREEN.blit(background_img, (0, 0))
        DISPLAY_SCREEN.blit(horizontal_line_img, (lines["horizontal1_x"], lines["horizontal1_y"]))
        DISPLAY_SCREEN.blit(horizontal_line_img, (lines["horizontal2_x"], lines["horizontal2_y"]))
        DISPLAY_SCREEN.blit(vertical_line_img, (lines["vertical1_x"], lines["vertical1_y"]))
        DISPLAY_SCREEN.blit(vertical_line_img, (lines["vertical2_x"], lines["vertical2_y"]))
        pygame.display.update()

    DISPLAY_SCREEN.blit(background_img, (0, 0))
    pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line
    DISPLAY_SCREEN.blit(horizontal_line_img, (lines["horizontal1_x"], lines["horizontal1_y"]))
    DISPLAY_SCREEN.blit(horizontal_line_img, (lines["horizontal2_x"], lines["horizontal2_y"]))
    DISPLAY_SCREEN.blit(vertical_line_img, (lines["vertical1_x"], lines["vertical1_y"]))
    DISPLAY_SCREEN.blit(vertical_line_img, (lines["vertical2_x"], lines["vertical2_y"]))

    if player_turn(tiles, player_img, event):
        pygame.display.update()
        is_game_over(tiles, player_img)
        computer_turn(tiles, computer_img)
        
    pygame.display.update()
    is_game_over(tiles, player_img)


def player_turn(tiles, player_img, event):
    player_played = False

    mouse_position = pygame.mouse.get_pos() # get the position of the mouse
    if event and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        for tile in tiles.values():
            if tile.is_clicked(mouse_position):
                tile.symbol_img = player_img
                player_played = True

    for tile in tiles.values():
        tile.blit(DISPLAY_SCREEN, mouse_position)
    
    return player_played


def computer_turn(tiles, computer_img):
    while True:
        rand_tile = random.randint(1,9) #because the tiles have the numbers from 1 to 9.
        if not tiles[rand_tile].occupied:
            tiles[rand_tile].symbol_img = computer_img
            tiles[rand_tile].occupied = True
            time.sleep(1)
            break
    
    mouse_position = pygame.mouse.get_pos() # get the position of the mouse
    for tile in tiles.values():
        tile.blit(DISPLAY_SCREEN, mouse_position)


def is_game_over(tiles, player_img):

    for i in range(1, 4):#if one column is completely filled with X or with O. 
        if tiles[i].symbol_img == tiles[i+3].symbol_img == tiles[i+6].symbol_img != None:
            time.sleep(1)
            if tiles[i].symbol_img == player_img:
                start_intro("      YOU WON")
            else:
                start_intro("     YOU LOST")

    for i in range(1,10,3):#if one row is completely filled with X or with O.    
        if tiles[i].symbol_img == tiles[i+1].symbol_img == tiles[i+2].symbol_img != None:
            time.sleep(1)
            if tiles[i].symbol_img == player_img:
                start_intro("      YOU WON")
            else:
                start_intro("     YOU LOST")

    #if one diagonol is completely filled with X or with O.    
    if tiles[1].symbol_img == tiles[5].symbol_img == tiles[9].symbol_img != None:
            time.sleep(1)
            if tiles[1].symbol_img == player_img:
                start_intro("      YOU WON")
            else:
                start_intro("     YOU LOST")

    if tiles[3].symbol_img == tiles[5].symbol_img == tiles[7].symbol_img != None:
            time.sleep(1)
            if tiles[3].symbol_img == player_img:
                start_intro("      YOU WON")
            else:
                start_intro("     YOU LOST")

    for tile in tiles.values(): # if no one won and there is still at least one empty cell, then the game is not over yet. 
        if not tile.occupied:
            return

    time.sleep(1)
    start_intro("      DRAW")        


def start_game(player_img, computer_img):
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
    lines = { #dictionary of the lines
        "horizontal1_x": horizontal1_x,
        "horizontal1_y": horizontal1_y,
        "horizontal2_x": horizontal2_x,
        "horizontal2_y": horizontal2_y, 
        "vertical1_x": vertical1_x,
        "vertical1_y": vertical1_y,
        "vertical2_x": vertical2_x,
        "vertical2_y": vertical2_y
    }

    tiles = { #dictionary of the tiles
        1: buttons.Tile(2, OFFSET_HEIGHT_UP+3, TILE_WIDTH, TILE_Height, TILE_HOVER_OVER_COLOR, TILE_OCCUPIED_COLOR),
        2: buttons.Tile(203, OFFSET_HEIGHT_UP+3, TILE_WIDTH, TILE_Height, TILE_HOVER_OVER_COLOR, TILE_OCCUPIED_COLOR),
        3: buttons.Tile(403, OFFSET_HEIGHT_UP+3, TILE_WIDTH, TILE_Height, TILE_HOVER_OVER_COLOR, TILE_OCCUPIED_COLOR),
        4: buttons.Tile(2, OFFSET_HEIGHT_UP+200+4, TILE_WIDTH, TILE_Height, TILE_HOVER_OVER_COLOR, TILE_OCCUPIED_COLOR),
        5: buttons.Tile(203, OFFSET_HEIGHT_UP+200+4, TILE_WIDTH, TILE_Height, TILE_HOVER_OVER_COLOR, TILE_OCCUPIED_COLOR),
        6: buttons.Tile(403, OFFSET_HEIGHT_UP+200+4, TILE_WIDTH, TILE_Height, TILE_HOVER_OVER_COLOR, TILE_OCCUPIED_COLOR),
        7: buttons.Tile(2, OFFSET_HEIGHT_UP+400+4, TILE_WIDTH, TILE_Height, TILE_HOVER_OVER_COLOR, TILE_OCCUPIED_COLOR),
        8: buttons.Tile(203, OFFSET_HEIGHT_UP+400+4, TILE_WIDTH, TILE_Height, TILE_HOVER_OVER_COLOR, TILE_OCCUPIED_COLOR),
        9: buttons.Tile(403, OFFSET_HEIGHT_UP+400+4, TILE_WIDTH, TILE_Height, TILE_HOVER_OVER_COLOR, TILE_OCCUPIED_COLOR)
    }

    while True:
        DISPLAY_SCREEN.blit(background_img, (0, 0))        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                draw_playing_field(lines, tiles, player_img, computer_img, event)

        draw_playing_field(lines, tiles, player_img, computer_img)

        # print("hiii")
        pygame.display.update()


def main():
    start_intro()


if __name__ == "__main__":  #to avoid runing the game, if this file is imported
    main()
