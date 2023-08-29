import numpy as np


class TrendBuffer:
    def __init__(self,size:int) -> None:
        self.buffer:np.ndarray=np.zeros(size,dtype=np.float32)
        self.ptr:int=0
        self.timeseries:np.ndarray=np.arange(size,dtype=np.int32)


    def push(self,x:float):

        if self.ptr==len(self.buffer):
            self.ptr=0

        self.buffer[self.ptr]=x
        self.ptr+=1
    
    def trendline(self)->float:
        output=np.polyfit(self.timeseries,self.buffer,1)
        
        return output[0]

