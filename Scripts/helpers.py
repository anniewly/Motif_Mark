#!bin/bash/python3

import cairo
import re

class ons:
    def __init__(self,seq):
        #seq is a string
        self.seq = seq
        self.seqlen = len(seq)
        self.positions=[]
   

    def cap_region(self):
        i=0
        while i < self.seqlen:
            if self.seq[i].isupper():
                start=i
                i+=1
                while self.seq[i].isupper():
                    i+=1
                    if i >= self.seqlen:
                        # i+=1
                        break
                end=i-1
                self.positions.append((start,end))
            i+=1
        return self.positions
        # for i in range(len(seq)):
        #     while is.upper(seq[i]):
        #         positions.append(i)
        # return positions
    def draw(self,ycoord,context):
        
        context.move_to(25,ycoord)
        for i in self.cap_region():
            context.line_to(i[0]+25,ycoord)
            context.rectangle(i[0]+25,ycoord-4, i[1]-i[0],8)
            context.move_to(i[1]+25,ycoord)
            # context.line_to(self.seqlen,25)
            # context.fill()
        context.line_to(self.seqlen+25,ycoord)
        context.set_source_rgb(0,0,0)
        context.stroke()   
        # surface.finish()


class motif:
    def __init__(self,seq,m):
        #m is a string of a motif
        self.seq = seq
        self.m = m  
        self.mlen=len(m)

    def find_motif(self):
        self.seq= self.seq.upper()
        self.m = self.m.upper()
        self.m = self.m.replace("N","[ACGT]")
        self.m = self.m.replace("X","[ACGT]")
        self.m = self.m.replace("V","[ACG]")
        self.m = self.m.replace("H","[ACT]")
        self.m = self.m.replace("D","[AGT]")
        self.m = self.m.replace("B","[CGT]")
        self.m = self.m.replace("M","[AC]")
        self.m = self.m.replace("R","[AG]")
        self.m = self.m.replace("W","[AT]")
        self.m = self.m.replace("S","[CG]")
        self.m = self.m.replace("Y","[CT]")
        self.m = self.m.replace("K","[GT]")
        # self.m = self.m.replace("N","[ACGTacgt]")
        # self.m = self.m.replace("X","[ACGTacgt]")
        # self.m = self.m.replace("V","[ACGacg]")
        # self.m = self.m.replace("H","[ACTact]")
        # self.m = self.m.replace("D","[AGTagt]")
        # self.m = self.m.replace("B","[CGTcgt]")
        # self.m = self.m.replace("M","[ACac]")
        # self.m = self.m.replace("R","[AGag]")
        # self.m = self.m.replace("W","[ATat]")
        # self.m = self.m.replace("S","[CGcg]")
        # self.m = self.m.replace("Y","[CTct]")
        # self.m = self.m.replace("K","[GTgt]")
        # self.m = self.m.replace("n","[ACGTacgt]")
        # self.m = self.m.replace("x","[ACGTacgt]")
        # self.m = self.m.replace("v","[ACGacg]")
        # self.m = self.m.replace("h","[ACTact]")
        # self.m = self.m.replace("d","[AGTagt]")
        # self.m = self.m.replace("b","[CGTcgt]")
        # self.m = self.m.replace("m","[ACac]")
        # self.m = self.m.replace("r","[AGag]")
        # self.m = self.m.replace("w","[ATat]")
        # self.m = self.m.replace("s","[CGcg]")
        # self.m = self.m.replace("y","[CTct]")
        # self.m = self.m.replace("k","[GTgt]")
        # self.m = self.m.replace("u","t")
        self.m = self.m.replace("U","T")
        self.m = '(?='+str(self.m)+')'

        mp=[]
        # print(self.m)
        for match in re.finditer(self.m,self.seq):
            mp.append((match.start(0),match.start()+self.mlen-1))
            # mp.append((match.start(0),match.end(1)))

        return (mp)
    
    def draw(self,ycoord,context):
        for j in (self.find_motif()):
            # print(i[0])
            context.rectangle(j[0]+25,ycoord-4, j[1]-j[0],8)
            
        # surface.finish()

        

# class draw:
#     def __init__(self,seq,m,ycoord):
#         #m is a string of a motif
#         self.seq = seq
#         self.m = m  
#         self.mlen=len(m)
#         self.ycoord = ycoord

#     width=700+20
#     height=80
#     surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
#     context = cairo.Context(surface)
#     context.set_line_width(1)

#     context.rectangle(0, 0, width, height)
#     context.set_source_rgb(1, 1, 1)
#     context.fill()

#     context.move_to(25,self.ycoord)
#         for i in self.cap_region():
#             context.line_to(i[0]+25,self.ycoord)
#             context.rectangle(i[0]+25,ycoord-3, i[1]-i[0]+25,ycoord+3)
#             context.move_to(i[1]+25,ycoord)
#             # context.line_to(self.seqlen,25)
#             # context.fill()
#         context.line_to(self.seqlen,ycoord)
#         context.set_source_rgb(0,0,0)   
#         # surface.finish()



    