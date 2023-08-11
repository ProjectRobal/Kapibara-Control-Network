'''
 Base class for objects.

'''

class BaseObject:
    def __init__(self) -> None:
        pass

    def draw(self,view,offset:tuple[int,int]):
        raise NotImplementedError

    def on_mouse_cord(self,mouse_cord:tuple[int,int]):
        pass

    def mouse_click(self,mouse_cord:tuple[int,int]):
        pass
    
    def mouse_relased(self):
        pass