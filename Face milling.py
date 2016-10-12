#!/usr/bin/env python2.7

#get inputs- size of machining
length=raw_input('Enter length(x) of cuts you want to make(mm): ')
if length=="":length=100
width=raw_input('Enter width(y) of cuts you want to make(mm): ')
if width=="":width=100
depth=raw_input('Enter depth(z) of material you want to remove(mm): ')
if depth=="":depth=0

#get inputs- size of tool
tool=raw_input('Enter tool diameter(mm): ')
if tool=="":tool=6
tool_o=raw_input('Enter overlap of each pass (0.00-0.99):')
if tool_o=="":tool_o=0.20
cut_d=raw_input('Enter depth for each cut(mm): ')
if cut_d=="":cut_d=tool

#set variables
safez=2.00
x=0.00
y=0.00
z=0.00

#convert input strings to floats
length=float(length)
width=float(width)
depth=float(depth)
tool=float(tool)
tool_o=float(tool_o)
cut_d=float(cut_d)


#produce the Gcode:
print
print
print
print '(###########      Face Milling      ##########)'
print '(tool diameter',tool,')'
print '(depth for each cut=',cut_d,')'
print '(tool overlap=',tool_o,')'
print '(length (x)=',length,')'
print '(width (y)=',width,')'
print '(depth (z)=',depth,')'


print '(M_ start program)'
print 'G21 (mm)'
print 'G17 (xy plane)'
print 'G40 (turns off tool diameter compensation)'
print 'G49 (turns off tool length compensation)'
print 'G54 (coordinate system:tool touch-off)'
print '(G53 (coordinate system: machine coordinates)'
print '(G64 Pn.n Path Blending)'
print 'G80 (turn off canned cycles)'
print 'G90 (distance mode from axis zero)'
print 'G94 (feed rate mode = units per minute)'


print 'F5000 S24000 (Feed and Speed)'
print 'g00 z',safez,'(rapid to safe z)'
print 'M3(start spindle)'

print 'g01 x0 y0 (progress to start of first pass)'
z=z-cut_d
p=0
while z>-depth:
    p=p+1
    print
    print '(**********Pass',p,'**********)'
    print 'g01 z ',z
    while y<width:
        print 'g01 x',x
        print 'g01 y',y
        print 'g01 x',length
        y=y+(tool-(tool*tool_o))
        print 'g01 y',y
        y=y+(tool-(tool*tool_o))
    y=0.00
    print 'g00 z',safez,'(rapid to safe z)'
    print 'g00 x0y0 (rapid to x0 y0 )'
    z=z-cut_d

#final depth pass
if z<-depth:
    z=-depth
    y=0.00
    print 'g01 z',z,'(**********final depth**********)'
    while y<width:
        print 'g01 x',0.00
        print 'g01 y',y
        print 'g01 x',length
        y=y+(tool-(tool*tool_o))
        print 'g01 y',y
        y=y+(tool-(tool*tool_o))

print 'g00 z', safez,'(rapid to safe z)'
print 'M05 (spindle off)'
print 'G91 G28 X0 Y0 Z0 (go to machine home)'
print 'G90 (return to absolute mode)'
print 'M02 (end program)'