# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:00:54 2020

@author: Vahid
"""

from LIPRO import *

G1 = np.insert(polygon(1,50),2,0,axis=1)
G1 = Transform(G1,90,0,0,0,0,0)
S1 = np.array(polygon(1,50)) + [-1,0]
part1 = sweep(S1,S1,G1)
part1_ver = Transform(part1[0],0,0,0,0,0,1)

G2 = np.insert(polygon(1,50),2,0,axis=1)
G2 = Transform(G2,0,90,90,0,0,0)
S2 = np.array(polygon(1,50,90)) + [0,1]
part2 = sweep(S2,S2,G2)
part2_ver = Transform(part2[0],0,0,0,0,0,3)

#savestl('ring',part1_ver,part1[1])
#savestl('ring2',part2_ver,part2[1])