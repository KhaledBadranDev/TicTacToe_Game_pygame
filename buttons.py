
"""
AUHTHOR: KHALED BADRAN
"""

import pygame


class Button:

    def __init__(self, button_color, button_hover_over_color, x, y, width, height, text_color, text_hover_over_color = None, text_str=""):
        """ constructor of Button class

        Args:
            button_color ((R,G,B) tuple): color of the button.
            button_hover_over_color ((R,G,B) tuple): temporary color of the button when the user hovers over it with the mouse.
            x (int): x-coordinate of start point of the button.
            y (int): y-coordinate of start point of the button.
            width (int): width of the button.
            height (int): height of the button.
            text_color ((R,G,B) tuple): color of the text inside the button.
            text_hover_over_color ((R,G,B) tuple): temporary color of the text when the user hovers over the button. Default = None.
            text_str (str): text inside the button. Default = "".
        """
        self.button_color = button_color
        self.button_hover_over_color = button_hover_over_color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_color = text_color

        if text_hover_over_color:
            self.text_hover_over_color = text_hover_over_color
        else:
            self.text_hover_over_color =  text_color
 
        self.text_str = text_str


    def blit(self, display_screen, outline_color=None):
        """ draw the button on the display_screen/display_window  

        Args:
            display_screen (pygame.display.set-mode): display_screen/display_window to draw the button on it.
            outline_color  ((R,G,B) tuple): color of the outline-borders of the button
        """
        if outline_color: 
            pygame.draw.rect(display_screen, outline_color,
                             (self.x-3, self.y-3, self.width+5, self.height+5))
        
        pygame.draw.rect(display_screen, self.button_color,
                         (self.x, self.y, self.width, self.height))

        if self.text_str != "": 
            font = pygame.font.Font("freesansbold.ttf", 32)
            text = font.render(self.text_str, True, self.text_color)
            # the text should be in the middle of the button
            text_position = (self.x + (self.width/2 - text.get_width()/2),
                             self.y + (self.height/2 - text.get_height()/2))
            display_screen.blit(text, text_position)


    def is_hovered_over(self, mouse_position):
        """ check whether the user hovers over the button with the mouse or not. 
        Args:
            mouse_position ((x,y) tuple): position of the mouse on the screen.

        Returns:
            boolean: True if the user hovers over the button with the mouse. False otherwise.
        """
        if self.x < mouse_position[0] < self.x+self.width and self.y < mouse_position[1] < self.y+self.height:
            return True
        return False


    def is_clicked(self, mouse_position, event):
        """ check whether the user clicks on the button with the left button of the mouse or not. 
        Args:
            event (pygame.event): event of pygame.
            mouse_position ((x,y) tuple): position of the mouse on the screen.

        Returns:
            boolean: True if the user clicks on the button with the left button of the mouse. False otherwise.
        """
        if self.is_hovered_over(mouse_position):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # if left button of the mouse is clicked
                return True
        return False


    def blit_hovered_over(self, display_screen):
        """ draw the button on the display_screen/display_window, when the user hovers over it with the mouse.

        Args:
            display_screen (pygame.display.set-mode): display_screen/display_window to draw the button on it.
        """
        pygame.draw.rect(display_screen, self.button_hover_over_color,
                         (self.x, self.y, self.width, self.height))

        if self.text_str != "":
            font = pygame.font.Font("freesansbold.ttf", 32)
            text = font.render(self.text_str, True, self.text_hover_over_color)
            # the text should be in the middle of the button
            text_position = (self.x + (self.width/2 - text.get_width()/2),
                             self.y + (self.height/2 - text.get_height()/2))
            display_screen.blit(text, text_position)



class Tile:

    def __init__(self, x, y, width, height, tile_hover_over_color, tile_occupied_color, tile_color = None):
        """ constructor of Tile class

        Args:
            x (int): x-coordinate of start point of the tile.
            y (int): y-coordinate of start point of the tile.
            width (int): width of the tile.
            height (int): height of the tile.
            tile_hover_over_color ((R,G,B) tuple): temporary color of the tile when it is empty and the user hovers over it with the mouse.
            tile_occupied_color ((R,G,B) tuple): color of the tile when it is occupied.
            tile_color ((R,G,B) tuple): color of the tile when it is empty.

        """
        self.occupied = False
        self.symbol_img = None

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.tile_hover_over_color = tile_hover_over_color
        self.tile_occupied_color = tile_occupied_color
        self.tile_color = tile_color


    def blit(self, display_screen, mouse_position):
        """ draw the tile on the display_screen/display_window
            when it is hovered over, when it is empty and when it is occupied.
        Args:
            display_screen (pygame.display.set-mode): display_screen/display_window to draw the tile on it.
            mouse_position ((x,y) tuple): position of the mouse on the screen.
        """
        if self.is_hovered_over(mouse_position)  and self.occupied == False: #if hovered over
            pygame.draw.rect(display_screen, self.tile_hover_over_color, (self.x, self.y, self.width, self.height))
        elif self.occupied: #if occupied
            pygame.draw.rect(display_screen, self.tile_occupied_color, (self.x, self.y, self.width, self.height))
            display_screen.blit(self.symbol_img, (self.x, self.y))

    
    def is_hovered_over(self, mouse_position):
        """ check whether the user hovers over the tile with the mouse or not. 
        Args:
            mouse_position ((x,y) tuple): position of the mouse on the screen.

        Returns:
            boolean: True if the user hovers over the tile with the mouse. False otherwise.
        """
        if self.x < mouse_position[0] < self.x+self.width and self.y < mouse_position[1] < self.y+self.height:
            return True
        return False


    def is_clicked(self, mouse_position):
        """ check whether the user clicks on the tile with the left button of the mouse or not. 
        Args:
            mouse_position ((x,y) tuple): position of the mouse on the screen.

        Returns:
            boolean: True if the user clicks on the tile with the left button of the mouse. False otherwise.
        """ 
        if self.is_hovered_over(mouse_position) and self.occupied == False:
                # if left button of the mouse is clicked
                self.occupied = True
                return True
        return False



class SelectPlayerButton:
    
    def __init__(self, x, y, width, height, button_color, button_hover_over_color, player_img):
        """ constructor of Button class

        Args:
            x (int): x-coordinate of start point of the Button.
            y (int): y-coordinate of start point of the Button.
            width (int): width of the Button.
            height (int): height of the Button.
            button_color ((R,G,B) tuple): color of the Button.
            Button_hover_over_color ((R,G,B) tuple): temporary color of the Button when the user hovers over it with the mouse.
            player_img (pygame.image): image to be blitted on the button
        """
        self.selected = False

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button_color = button_color
        self.button_hover_over_color = button_hover_over_color
        self.player_img = player_img


    def blit(self, display_screen, mouse_position=None):
        """ draw the Button on the display_screen/display_window
            when it is hovered over, when it is empty and when it is occupied.
        Args:
            display_screen (pygame.display.set-mode): display_screen/display_window to draw the Button on it.
            mouse_position ((x,y) tuple): position of the mouse on the screen.
        """
        
        if self.is_hovered_over(mouse_position): #if hovered over
            pygame.draw.rect(display_screen, self.button_hover_over_color, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(display_screen, self.button_color, (self.x, self.y, self.width, self.height))
        
        display_screen.blit(self.player_img, (self.x, self.y))

    
    def is_hovered_over(self, mouse_position):
        """ check whether the user hovers over the Button with the mouse or not. 
        Args:
            mouse_position ((x,y) tuple): position of the mouse on the screen.

        Returns:
            boolean: True if the user hovers over the Button with the mouse. False otherwise.
        """
        if mouse_position:
            if self.x < mouse_position[0] < self.x+self.width and self.y < mouse_position[1] < self.y+self.height:
                return True
        return False


    def is_clicked(self, mouse_position):
        """ check whether the user clicks on the Button with the left button of the mouse or not. 
        Args:
            mouse_position ((x,y) tuple): position of the mouse on the screen.

        Returns:
            boolean: True if the user clicks on the Button with the left button of the mouse. False otherwise.
        """
        if self.is_hovered_over(mouse_position):
                # if left button of the mouse is clicked
                self.selected = True
                self.button_color = self.button_hover_over_color
                return True
        return False
