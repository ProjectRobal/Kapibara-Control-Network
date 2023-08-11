'''
    A class that realized button function it execute action when clicked,pressed or released
'''

from pygame import Rect
import pygame
from .baseobject import BaseObject


class Button(BaseObject):
    def __init__(self,rect:Rect,text:str,color:tuple[int,int,int],text_color:tuple[int,int,int]) -> None:
        super(Button,self).__init__()
        '''
        rect - a object that will define geoemetry and hitbox of button
        text - a text that will be displayed on button
        color - a color of the rect
        text_color - a color of the text
        '''
        
        self.rect=rect
        self.text=text
        self.color=color
        self.text_color=text_color
        self.texty_scale=0.1
        self.highligh_color=(255-color[0],255-color[1],255-color[2])

        self.on_click=None
        self.on_click_arg=None
        self._overlaped=False
        self.clicked=False

    def draw(self,view:pygame.Surface):

        if self._overlaped:
            color=self.color
        else:
            color=self.highligh_color

        pygame.draw.rect(view,color,self.rect)

        font_height=int(self.rect.height*self.texty_scale)

        font = pygame.font.Font('/usr/share/fonts/truetype/Sarai/Sarai.ttf', font_height)

        text=font.render(self.text,True,self.text_color)

        textRect=text.get_rect()

        textRect.center=self.rect.center

        view.blit(text,textRect)

    def on_mouse_cord(self,mouse_cord:tuple[int,int]):
        self._overlaped=self.rect.collidepoint(mouse_cord[0],mouse_cord[1])

    def mouse_click(self,mouse_cord:tuple[int,int]):
        if self.clicked or self.on_click is None:
            return
        
        if self.rect.collidepoint(mouse_cord[0],mouse_cord[1]):
            self.on_click(self.on_click_arg)
            self.clicked=True
    
    def mouse_relased(self):
        self.clicked=False
