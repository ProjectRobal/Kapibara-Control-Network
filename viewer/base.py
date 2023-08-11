'''
A file with base elements like labels, rect, or number nodes.

'''

from .baseobject import BaseObject
from pygame import Rect
import pygame


class Label(BaseObject):
    def __init__(self,rect:Rect,text:str,text_color:tuple[int,int,int],color:tuple[int,int,int]=None) -> None:
        super().__init__()
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
        self.texty_scale=0.5
    
    def draw(self,view:pygame.Surface):

        if self.color is not None:
            pygame.draw.rect(view,self.color,self.rect)

        font_height=int(self.rect.height*self.texty_scale)

        font = pygame.font.Font('viewer/fonts/arial.ttf', font_height)

        text=font.render(self.text,True,self.text_color)

        textRect=text.get_rect()

        textRect.center=self.rect.center

        view.blit(text,textRect)


class Rectangle(BaseObject):
    def __init__(self,rect:Rect,color:tuple[int,int,int]) -> None:
        super().__init__()
        '''
        rect - a object that will define geoemetry and hitbox of button
        text - a text that will be displayed on button
        color - a color of the rect
        text_color - a color of the text
        '''
        self.rect=rect
        self.color=color
    
    def draw(self,view:pygame.Surface):

        pygame.draw.rect(view,self.color,self.rect)



