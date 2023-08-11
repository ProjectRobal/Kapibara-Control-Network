'''

Abstract class used by viewer to initialize scene.

'''

from .baseobject import BaseObject

class Page:
    def __init__(self,object:list[BaseObject]) -> None:
        '''
        A object input list from viewer
        '''
        object.clear()