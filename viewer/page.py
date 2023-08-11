'''

Abstract class used by viewer to initialize scene.

'''

from .baseobject import BaseObject

class Page:
    def __init__(self,objects:list[BaseObject],network) -> None:
        '''
        objects - a object input list from viewer
        network - a target network
        '''
        object.clear()