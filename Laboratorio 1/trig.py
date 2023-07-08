import math

class trig:

    def __init__(self):
        self.pi= math.pi
    
    
    def seno(self):
        return math.sin(self.pi)
    
    
    def coseno(self):
        return math.cos(self.pi)
    
    
    def tangente(self):
        return math.tan(self.pi)
    
    def guardar(self,time,informacion):
        archivo=open("log.txt","a")
        self.time=time
        archivo.write("\n"+"----------------------------------")
        archivo.write("\n"+informacion+"\n"+"Fecha y hora de operacion:"+"\n"+str(self.time))