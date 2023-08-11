'''
 Base class for objects.

'''

class BaseObject:
    def __init__(self) -> None:
        pass

    def draw(self,view):
        raise NotImplementedError

    def on_mouse_cord(self,mouse_cord:tuple[int,int]):
        raise NotImplementedError()

    def mouse_click(self,mouse_cord:tuple[int,int]):
        raise NotImplementedError()
    
    def mouse_relased(self):
        raise NotImplementedError()