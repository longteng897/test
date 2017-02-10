import sys
import re
import math


#z=math.asin(1/2)
#y=z*180/math.pi
#y=math.sin(math.radians(30))
#print(y)
for x in range(1,1000000):
#    print(x)
    if x%1==0:
        if x%2 == 1:        
            if x%3==0:
                if x%4==1:
                    if x%5==4:
                        if x%6==3:
                            if x%7==0:
                                if x%8==1:
                                    if x%9==0:
                                        print(x)
                                        continue
                                    else:
                                        continue
                                else:
                                    continue                            
                            else:
                                continue
                        else:
                            continue
                    else:
                        continue            
                else:
                    continue
            else:
                continue