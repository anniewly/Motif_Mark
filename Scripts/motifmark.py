#!bin/bash/python3

import argparse
from helpers import *

def get_args():
    parser = argparse.ArgumentParser(description="TD")
    parser.add_argument("-f", help="input fasta file", required=True)
    parser.add_argument("-m", help = "input motif file", required=True)
    return parser.parse_args()

args = get_args()

file = args.f
mfile = args.m

width=1000
height=1000
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)
context.set_line_width(1)
context.rectangle(0, 0, width, height)
context.set_source_rgb(1, 1, 1)
context.fill()

with open(file,'r') as f, open(mfile,'r') as mf:
    mfs = [s.strip("\n") for s in mf]
    sequence=''
    counter=0
    clist=[255,0,0,0,255,0,0,0,255,255,0,255]
    for line in f:
        line = line.strip('\n')
        if line[0] == ">" and sequence != '':
            intronpos = ons(sequence).cap_region()
            ons(sequence).draw(25*counter*2+40,context)
            context.move_to(25, 25*counter*2+40-15)
            context.set_font_size(17)
            context.select_font_face("Arial",cairo.FONT_SLANT_NORMAL,cairo.FONT_WEIGHT_NORMAL)
            context.set_source_rgb(0,0,0)
            context.show_text(str(header))
            for index,i in enumerate(mfs):
                # print(index,i)
                motifposition = motif(sequence,i).find_motif()
                # print(motif(sequence,i).m,(clist[index*3],clist[index*3+1],clist[index*3+2]),motifposition)
                # print(i,motifposition,len(motifposition[1]))
                motif(sequence,i).draw(25*counter*2+40,context)
                # print(clist[index*3],clist[index*3+1],clist[index*3+2])
                context.set_source_rgb(clist[index*3],clist[index*3+1],clist[index*3+2])
                context.stroke()

                # print(clist[index*3],clist[index*3+1],clist[index*3+2])
            sequence=''
            header = line
            counter+=1
            
        elif line[0] == ">" and sequence == '':
            header = line
        else:
            sequence += line

    intronpos = ons(sequence).cap_region()
    ons(sequence).draw(25*counter*2+40,context)
    context.move_to(25, 25*counter*2+40-15)
    context.set_font_size(17)
    context.select_font_face("Arial",cairo.FONT_SLANT_NORMAL,cairo.FONT_WEIGHT_NORMAL)
    context.set_source_rgb(0,0,0)
    context.show_text(str(header))
    for index,i in enumerate(mfs):
            motifposition = motif(sequence,i).find_motif()
            # print(i,motifposition,len(motifposition[1]))
            motif(sequence,i).draw(25*counter*2+40,context)
            context.set_source_rgb(clist[index*3],clist[index*3+1],clist[index*3+2])
            context.stroke()
            # print(motif(sequence,i).m,(clist[index*3],clist[index*3+1],clist[index*3+2]),motifposition)
x_legend = 25
y_legend = 25*counter*3+40-15
context.rectangle(x_legend,y_legend,150,100)
context.set_source_rgb(0,0,0)
context.stroke()

for index,i in enumerate(mfs):
    context.rectangle(x_legend+20,y_legend+20*(index+1)-10,15,13)
    context.set_source_rgb(clist[index*3],clist[index*3+1],clist[index*3+2])
    context.stroke()
    context.move_to(x_legend+20+20, y_legend+20*(index+1)-10+13)
    context.set_font_size(15)
    context.select_font_face("Arial",cairo.FONT_SLANT_NORMAL,cairo.FONT_WEIGHT_NORMAL)
    context.set_source_rgb(0,0,0)
    context.show_text(str(i))
# legend_line_length = 35
# count = 1
# for i in range(3):
# for j in range(len(color_palette[i])):
# ctx.move_to(x_legend + 5, y_legend + (count*15))
# ctx.line_to(x_legend + legend_line_length, y_legend + (count*15))
# if i == 0:
# ctx.set_source_rgb(color_palette[i][j],0,0)
# if i == 1:
# ctx.set_source_rgb(0,color_palette[i][j],0)
# if i == 2:
# ctx.set_source_rgb(0,0,color_palette[i][j])
# ctx.set_line_width(3)
# ctx.stroke()





        # if ">" in line and sequence != []:
        #     seqstr= ''.join(sequence)
        #     print(seqstr)
        #     for i in mfs:
        #         motifposition = motif(seqstr,i).find_motif()
        #         # print(i,motifposition,len(motifposition[1]))
        #     sequence=[]
        #     continue
        # elif ">" not in line:
        #     # print(line)
        #     sequence.append(line)
    # while True:
    #     header = f.readline()
    #     if header == '':
    #         break
    #     sequence = f.readline()
    #     p = ons(sequence).cap_region()
    #     for i in mfs:
    #         motifposition = motif(sequence,i).find_motif()
    #         # print(seq)
    #         print(i,motifposition,len(motifposition[1]))

context.stroke()
surface.write_to_png("example.png") 