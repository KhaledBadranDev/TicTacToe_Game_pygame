
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

SAILOR_BLUE = TILE_OCCUPIED_COLOR = (4, 30, 66) #SAILOR_BLUE
ORANGE = (249, 87, 0) #ORANGE 
GRAY = (95, 95, 96) #GRAY
BLUE = (107,142,35)

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
TILE_WIDTH = 195
TILE_Height = 195
X_COORDINATE_BUTTONS = WIDTH/2 - BUTTON_WIDTH//2  #X_COORDINATE_BUTTONS

background_img = pygame.image.load("images/background.png")
icon_img = pygame.image.load("images/icon.png")
horizontal_line_img = pygame.image.load("images/horizontal_line.png")
vertical_line_img = pygame.image.load("images/vertical_line.png")
x_img = pygame.image.load("images/x.png")
o_img = pygame.image.load("images/o.png")
player_x_img = pygame.image.load("images/player_x.png")
player_o_img = pygame.image.load("images/player_o.png")

pygame.display.set_icon(icon_img)
pygame.display.set_caption("Tic-Tac-Toe")
#############################################

 
def select_player(difficulty): 
    """ to enable the user to select either X or O.
    Args:
        difficulty (str): difficulty level of the game.
    """
    player_x_button = buttons.SelectPlayerButton(-300, OFFSET_HEIGHT_UP+3, 300-3, HEIGHT-OFFSET_HEIGHT_UP-5, SAILOR_BLUE, ORANGE, player_x_img)
    player_o_button = buttons.SelectPlayerButton(600, OFFSET_HEIGHT_UP+3, 300-3, HEIGHT-OFFSET_HEIGHT_UP-5, SAILOR_BLUE, ORANGE, player_o_img)

    while True:
        DISPLAY_SCREEN.blit(background_img, (0, 0))
        pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line

        #to draw the buttons in an animated way
        while player_x_button.x < 0 or player_o_button.x > WIDTH/2:
            DISPLAY_SCREEN.blit(background_img, (0, 0))
            pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            player_x_button.x += 2.5
            player_o_button.x -= 2.5
            
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

                player_x_button.x -= 2.5
                player_o_button.x += 2.5
                
                player_x_button.blit(DISPLAY_SCREEN)
                player_o_button.blit(DISPLAY_SCREEN)
                pygame.display.update()

            start_game(player_img, computer_img, difficulty)


def start_intro(status = ""):
    """start the introduction of the game and show if the user won, lost or draw in the previous game.

    Args:
        status (str): status of the previous game. Either "YOU WoN" or "YOU LOST" or "DRAW". Defaults to "".
    """
    play_button = buttons.Button(SAILOR_BLUE, ORANGE, -400, HEIGHT/2, BUTTON_WIDTH, BUTTON_HEIGHT, ORANGE, SAILOR_BLUE, "PLAY")
    quit_button = buttons.Button(SAILOR_BLUE, ORANGE, WIDTH+200, HEIGHT/2+BUTTON_HEIGHT+10, BUTTON_WIDTH, BUTTON_HEIGHT, ORANGE, SAILOR_BLUE, "QUIT")

    if status: # to blit the status of the previous game if available. 
        font = pygame.font.SysFont("comicsansms", 40)
        rendered_text = font.render(status, 1, BLUE)
        rendered_text_y = HEIGHT
        
        #to draw the status of the previous game in an animated way.
        while rendered_text_y > OFFSET_HEIGHT_UP+20: 
            DISPLAY_SCREEN.blit(background_img, (0, 0))
            pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            rendered_text_y -= 0.8
            DISPLAY_SCREEN.blit(rendered_text, (WIDTH/2-rendered_text.get_width()/2, rendered_text_y))
            pygame.display.update()

    #to draw the buttons in an animated way.
    while play_button.x < X_COORDINATE_BUTTONS or quit_button.x > X_COORDINATE_BUTTONS :
        DISPLAY_SCREEN.blit(background_img, (0, 0))
        pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line
        if status:
            DISPLAY_SCREEN.blit(rendered_text, (WIDTH/2-rendered_text.get_width()/2, rendered_text_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        if play_button.x < X_COORDINATE_BUTTONS:
            play_button.x += 2
        if quit_button.x > X_COORDINATE_BUTTONS:    
            quit_button.x -= 2

        play_button.blit(DISPLAY_SCREEN, GRAY)
        quit_button.blit(DISPLAY_SCREEN, GRAY)
        pygame.display.update()


    run = True
    while run:
        DISPLAY_SCREEN.blit(background_img, (0, 0))
        pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line

        play_button.blit(DISPLAY_SCREEN, GRAY)
        quit_button.blit(DISPLAY_SCREEN, GRAY)

        if status:
            DISPLAY_SCREEN.blit(rendered_text, (WIDTH/2-rendered_text.get_width()/2, rendered_text_y))

        mouse_pos = pygame.mouse.get_pos() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if play_button.is_clicked(mouse_pos, event):
                run = False
                select_difficulty()
            if quit_button.is_clicked(mouse_pos, event):
                pygame.quit()


        # change the color of the buttons when the user hovers over them.
        if play_button.is_hovered_over(mouse_pos):
            play_button.blit_hovered_over(DISPLAY_SCREEN)
        elif quit_button.is_hovered_over(mouse_pos):
            quit_button.blit_hovered_over(DISPLAY_SCREEN)

        pygame.display.update()


def draw_playing_field(lines, tiles, player_img, computer_img, difficulty, event=None):
    """draw the playing field of the game.

    Args:
        lines (dictionary): dictionary of lines for the playing field 
        tiles (dictionary): dictionary of the tiles of the playing field.
        player_img (pygame.image): image of the user either x or o
        computer_img (pygame.image): image of the computer as a player either x or o 
        difficulty (str): difficulty level of the game.
        event (pygame.event): event of pygame. Defaults to None.
    """
    #to draw the lines of the playing field in an animated way.
    while lines["horizontal1_x"] <= 0 or lines["horizontal2_x"] >= 0 or lines["vertical1_x"] <= (WIDTH/3) or lines["vertical2_x"] >= (WIDTH/3)*2:
        DISPLAY_SCREEN.blit(background_img, (0, 0))
        pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if lines["horizontal1_x"] <= 0:
            lines["horizontal1_x"] += 1.2
        if lines["horizontal2_x"] >= 0:
            lines["horizontal2_x"] -= 1.2
        
        if lines["vertical1_x"] <= (WIDTH/3):
            lines["vertical1_x"] += 0.4
        if lines["vertical2_x"] >= (WIDTH/3)*2:
            lines["vertical2_x"] -= 0.4

        DISPLAY_SCREEN.blit(background_img, (0, 0))
        pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line
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
        if difficulty == "easy":
            computer_turn_easy(tiles, computer_img)
        else:
            computer_turn_hard(tiles, computer_img, player_img)
    pygame.display.update()
    is_game_over(tiles, player_img)


def player_turn(tiles, player_img, event):
    """to let the user play.

    Args:
        tiles (dictionary): dictionary of the tiles of the playing field.
        player_img (pygame.image): image of the user either x or o
        event (pygame.event): event of pygame. Defaults to None.

    Returns:
        boolean: return True if the user played and is done with his turn. False otherwise. 
    """
    player_played = False
    
    mouse_position = pygame.mouse.get_pos() # get the position of the mouse
    if event and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        for tile in tiles.values():
            if tile.is_clicked(mouse_position):
                tile.symbol_img = player_img
                player_played = True

    print_tiles(tiles)
    
    return player_played


def computer_turn_easy(tiles, computer_img):
    """let the computer play. The computer will choose a random empty tile.

    Args:
        tiles (dictionary): dictionary of the tiles of the playing field.
        computer_img (pygame.image): image of the computer as a player either x or o 
    """
    while True:
        rand_tile = random.randint(1,9) #because the tiles have the numbers from 1 to 9.
        if not tiles[rand_tile].occupied:
            tiles[rand_tile].symbol_img = computer_img
            tiles[rand_tile].occupied = True
            break
    
    print_tiles(tiles)


def computer_can_win(tiles, computer_img, player_img, current_list):
    """the computer tries to win the game.

    Args:
        tiles (dictionary): dictionary of the tiles of the playing field.
        computer_img (pygame.image): image of the computer as a player either x or o 
        player_img (pygame.image): image of the user either x or o
        current_list (list): list of either a row or a column or a diagonol. 

    Returns:
        boolean: True if the computer could win the game. False otherwise.
    """
    for i in current_list:            
            for j in current_list:            
                if i!=j and tiles[i].symbol_img == tiles[j].symbol_img == computer_img != None:
                    for k in current_list:
                        if k != i and k != j and not tiles[k].occupied:
                            tiles[k].symbol_img = computer_img
                            tiles[k].occupied = True
                            print_tiles(tiles)
                            return True
    return False


def computer_can_defend(tiles, computer_img, player_img, current_list):
    """the computer tries to disable the user from winning the game.

    Args:
        tiles (dictionary): dictionary of the tiles of the playing field.
        computer_img (pygame.image): image of the computer as a player either x or o 
        player_img (pygame.image): image of the user either x or o
        current_list (list): list of either a row or a column or a diagonol. 

    Returns:
        boolean: True if the computer could disable the user from winning the game. False otherwise.
    """
    for i in current_list:            
            for j in current_list:            
                if i!=j and tiles[i].symbol_img == tiles[j].symbol_img == player_img != None:
                    for k in current_list:
                        if k != i and k != j and not tiles[k].occupied:
                            tiles[k].symbol_img = computer_img
                            tiles[k].occupied = True
                            print_tiles(tiles)
                            return True
    return False


def computer_turn_hard(tiles, computer_img, player_img):
    """let the computer play. The computer will try to win the game instaed of choosing a random tile.

    Args:
        tiles (dictionary): dictionary of the tiles of the playing field.
        computer_img (pygame.image): image of the computer as a player either x or o 
        player_img (pygame.image): image of the user either x or o
    """
    #computer tries to win first of all
    for i in range(1, 4):#columns 
        col = [i, i+3, i+6]
        if computer_can_win(tiles, computer_img, player_img, col):
            print_tiles(tiles)
            return

    for i in range(1, 10, 3):#rows 
        row = [i, i+1, i+2]
        if computer_can_win(tiles, computer_img, player_img, row):
            print_tiles(tiles)
            return

    #left diagonol.   
    left_diagonol = [1, 5, 9]
    if computer_can_win(tiles, computer_img, player_img, left_diagonol):
        print_tiles(tiles)
        return

    #right diagonol.   
    right_diagonol = [3, 5, 7]
    if computer_can_win(tiles, computer_img, player_img, right_diagonol):
        print_tiles(tiles)
        return

    #####################################
    #if computer could't win the game, them it tries to disable the user from winning the game.

    for i in range(1, 4):#columns 
        col = [i, i+3, i+6]
        if computer_can_defend(tiles, computer_img, player_img, col):
            print_tiles(tiles)
            return

    for i in range(1, 10, 3):#rows 
        row = [i, i+1, i+2]
        if computer_can_defend(tiles, computer_img, player_img, row):
            print_tiles(tiles)
            return

    #left diagonol.   
    left_diagonol = [1, 5, 9]
    if computer_can_defend(tiles, computer_img, player_img, left_diagonol):
        print_tiles(tiles)
        return

    #right diagonol.   
    right_diagonol = [3, 5, 7]
    if computer_can_defend(tiles, computer_img, player_img, right_diagonol):
        print_tiles(tiles)
        return

    #if the situation is not dangerous and computer can't win and the player can't win as well, then choose a random tile.
    computer_turn_easy(tiles, computer_img)


def print_tiles(tiles):
    """print the tiles of the playing field.

    Args:
        tiles (dictionary): dictionary of the tiles of the playing field.
    """
    mouse_position = pygame.mouse.get_pos() # get the position of the mouse
    for tile in tiles.values():
        tile.blit(DISPLAY_SCREEN, mouse_position)


def is_game_over(tiles, player_img):
    """check whether the game is over or not.
       If it is over, start the introduction again and let the user know if he won, lost or draw.

    Args:
        tiles (dictionary): dictionary of the tiles of the playing field.
        player_img (pygame.image): image of the user either x or o
    """
    for i in range(1, 4):#if one column is completely filled with X or with O. 
        if tiles[i].symbol_img == tiles[i+3].symbol_img == tiles[i+6].symbol_img != None:
            if tiles[i].symbol_img == player_img:
                print_why_game_over(tiles, tiles[i], tiles[i+3], tiles[i+6], "win")
                start_intro("YOU WON")
            else:
                print_why_game_over(tiles, tiles[i], tiles[i+3], tiles[i+6], "lose")
                start_intro("YOU LOST")

    for i in range(1,10,3):#if one row is completely filled with X or with O.    
        if tiles[i].symbol_img == tiles[i+1].symbol_img == tiles[i+2].symbol_img != None:
            if tiles[i].symbol_img == player_img:
                print_why_game_over(tiles, tiles[i], tiles[i+1], tiles[i+2], "win")
                start_intro("YOU WON")
            else:                
                print_why_game_over(tiles, tiles[i], tiles[i+1], tiles[i+2], "lose")
                start_intro("YOU LOST")

    #if one diagonol is completely filled with X or with O.    
    if tiles[1].symbol_img == tiles[5].symbol_img == tiles[9].symbol_img != None:
            if tiles[1].symbol_img == player_img:
                print_why_game_over(tiles, tiles[1],tiles[5], tiles[9], "win")
                start_intro("YOU WON")
            else:
                print_why_game_over(tiles, tiles[1],tiles[5], tiles[9], "lose")
                start_intro("YOU LOST")

    if tiles[3].symbol_img == tiles[5].symbol_img == tiles[7].symbol_img != None:
            if tiles[3].symbol_img == player_img:
                print_why_game_over(tiles, tiles[3], tiles[5], tiles[7], "win")
                start_intro("YOU WON")
            else:
                print_why_game_over(tiles, tiles[3], tiles[5], tiles[7], "lose")
                start_intro("YOU LOST")

    for tile in tiles.values(): # if no one won and there is still at least one empty cell, then the game is not over yet. 
        if not tile.occupied:
            return

    time.sleep(0.3)
    start_intro("DRAW")        


def print_why_game_over(tiles, first_tile, middle_tile, last_tile, state):
    """to show the user why the game is over and how he or the computer won.

    Args:
        tiles (dictionary): dictionary of the tiles of the playing field.
        first_tile (Tile): first_tile of either a row or a column or a diagonol. 
        middle_tile (Tile): middle_tile of either a row or a column or a diagonol. 
        last_tile (Tile): last_tile of either a row or a column or a diagonol. 
        state (str): state of the game. Either "win" or "lose" to indicate whether the player won or not.
    """
    if state == "win":
        color = (50, 200, 100)
    else:
        color = (250, 200, 50)


    first_tile.tile_occupied_color = color
    print_tiles(tiles)
    pygame.display.update()
    time.sleep(0.4)

    middle_tile.tile_occupied_color = color
    print_tiles(tiles)
    pygame.display.update()
    time.sleep(0.4)

    last_tile.tile_occupied_color = color
    print_tiles(tiles)
    pygame.display.update()
    time.sleep(1.2)


def start_game(player_img, computer_img, difficulty):
    """start the game

    Args:
        player_img (pygame.image): image of the user either x or o
        computer_img (pygame.image): image of the computer as a player either x or o 
        difficulty (str): difficulty level of the game.
    """
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
        1: buttons.Tile(2, OFFSET_HEIGHT_UP+3, TILE_WIDTH, TILE_Height, ORANGE, TILE_OCCUPIED_COLOR),
        2: buttons.Tile(203, OFFSET_HEIGHT_UP+3, TILE_WIDTH, TILE_Height, ORANGE, TILE_OCCUPIED_COLOR),
        3: buttons.Tile(403, OFFSET_HEIGHT_UP+3, TILE_WIDTH, TILE_Height, ORANGE, TILE_OCCUPIED_COLOR),
        4: buttons.Tile(2, OFFSET_HEIGHT_UP+200+4, TILE_WIDTH, TILE_Height, ORANGE, TILE_OCCUPIED_COLOR),
        5: buttons.Tile(203, OFFSET_HEIGHT_UP+200+4, TILE_WIDTH, TILE_Height, ORANGE, TILE_OCCUPIED_COLOR),
        6: buttons.Tile(403, OFFSET_HEIGHT_UP+200+4, TILE_WIDTH, TILE_Height, ORANGE, TILE_OCCUPIED_COLOR),
        7: buttons.Tile(2, OFFSET_HEIGHT_UP+400+4, TILE_WIDTH, TILE_Height, ORANGE, TILE_OCCUPIED_COLOR),
        8: buttons.Tile(203, OFFSET_HEIGHT_UP+400+4, TILE_WIDTH, TILE_Height, ORANGE, TILE_OCCUPIED_COLOR),
        9: buttons.Tile(403, OFFSET_HEIGHT_UP+400+4, TILE_WIDTH, TILE_Height, ORANGE, TILE_OCCUPIED_COLOR)
    }

    while True:
        DISPLAY_SCREEN.blit(background_img, (0, 0))        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                draw_playing_field(lines, tiles, player_img, computer_img,difficulty, event)

        draw_playing_field(lines, tiles, player_img, computer_img, difficulty)

        pygame.display.update()


def select_difficulty():
    """enable the user to play the game in different difficulty levels.
    """
    easy_button  = buttons.Button(SAILOR_BLUE, ORANGE, -400, HEIGHT/2, BUTTON_WIDTH, BUTTON_HEIGHT, ORANGE, SAILOR_BLUE, "EASY")
    hard_button  = buttons.Button(SAILOR_BLUE, ORANGE, WIDTH+200, HEIGHT/2+BUTTON_HEIGHT+10, BUTTON_WIDTH, BUTTON_HEIGHT, ORANGE, SAILOR_BLUE, "HARD")

    font = pygame.font.SysFont("comicsansms", 48)
    rendered_text = font.render("SELECT DIFFICULTY", 1, BLUE)
    rendered_text_y = HEIGHT
    
    #to draw the "select difficulty" text in an animated way.
    while rendered_text_y > OFFSET_HEIGHT_UP+20: 
        DISPLAY_SCREEN.blit(background_img, (0, 0))
        pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        rendered_text_y -= 0.8
        DISPLAY_SCREEN.blit(rendered_text, (WIDTH/2-rendered_text.get_width()/2, rendered_text_y))
        pygame.display.update()

    #to draw the buttons in an animated way.
    while easy_button.x < X_COORDINATE_BUTTONS or hard_button.x > X_COORDINATE_BUTTONS :
        DISPLAY_SCREEN.blit(background_img, (0, 0))
        pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line
        DISPLAY_SCREEN.blit(rendered_text, (WIDTH/2-rendered_text.get_width()/2, rendered_text_y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        if easy_button.x < X_COORDINATE_BUTTONS:
            easy_button.x += 2
        if hard_button.x > X_COORDINATE_BUTTONS:    
            hard_button.x -= 2

        easy_button.blit(DISPLAY_SCREEN, GRAY)
        hard_button.blit(DISPLAY_SCREEN, GRAY)
        pygame.display.update()


    run = True
    while run:
        DISPLAY_SCREEN.blit(background_img, (0, 0))
        pygame.draw.line(DISPLAY_SCREEN, (100,0,0), (0,OFFSET_HEIGHT_UP), (WIDTH,OFFSET_HEIGHT_UP), 3) #horizontal line
        DISPLAY_SCREEN.blit(rendered_text, (WIDTH/2-rendered_text.get_width()/2, rendered_text_y))
        easy_button.blit(DISPLAY_SCREEN, GRAY)
        hard_button.blit(DISPLAY_SCREEN, GRAY)

        mouse_pos = pygame.mouse.get_pos() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if easy_button.is_clicked(mouse_pos, event):
                run = False # to stop running the select_difficulty screen
                select_player("easy")
            if hard_button.is_clicked(mouse_pos, event):
                run = False # to stop running the select_difficulty screen
                select_player("hard")


        # change the color of the buttons when the user hovers over them.
        if easy_button.is_hovered_over(mouse_pos):
            easy_button.blit_hovered_over(DISPLAY_SCREEN)
        elif hard_button.is_hovered_over(mouse_pos):
            hard_button.blit_hovered_over(DISPLAY_SCREEN)

        pygame.display.update()


def main():
    start_intro()


if __name__ == "__main__":  #to avoid runing the game, if this file is imported
    main()
