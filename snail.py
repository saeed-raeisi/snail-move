
from time import sleep
from math import sqrt
import sys
import os
from sys import stdout
from os import system


# 21 22 23 24 25
# 20 07 08 09 10
# 19 06 01 02 11
# 18 05 04 03 12
# 17 16 15 14 13 

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"

directions = [
    lambda i, j: (i, j + 1), # Right 0
    lambda i, j: (i + 1, j), # Down  1
    lambda i, j: (i, j - 1), # Left  2
    lambda i, j: (i - 1, j), # Up    3
]

def snail(num):
    # Left
    direction_cnt = 0 
    # Line of matrix
    line = int(sqrt(num)) +1
    # start point
    start =  int(sqrt(num) / 2)

    i, j = start,start
    tmp_i, tmp_j = 0,0
    array = [[0 for x in range(line)] for y in range(line)]     
    array[i][j]=1

    # every direction number 
    number_count = 0
    # count of every number in direction
    change_number = 1
    # count of every change direction
    change_counter = 0
    # call directions
    flag = False
    # 25 -> 5 -> 3 

    for item in range(2,num+1):

        # ----------------------------------------------------------------  print 
        for row in range(0,line):
            for col in range(0,line):
                if array[row][col] != 0:
                    stdout.write(RED)
                    print("{:02d}".format(array[row][col],'red'),end=" ")
                else:
                    stdout.write(BLUE)   
                    print("{:02d}".format(array[row][col]),end=" ")
            print()
        sleep(0.2)
        system('cls')
        # ---------------------------------------------------------------- end 
        # find direction
        direction_func = directions[direction_cnt % 4]
        tmp_i, tmp_j = direction_func(i, j)
        

        i, j = tmp_i, tmp_j  
        # import number
        array[i][j]=item
        # count of this direction number
        number_count += 1

        # check to import more number 
        if change_counter == 2:
            change_number += 1
            change_counter = 0

        # now change direction
        if change_number - number_count == 0 :
            flag = True
            
        # change direction
        if (flag):
            # change path
            direction_cnt +=1
            # count change
            change_counter += 1
            number_count = 0
            flag =False

    return array



if __name__ == '__main__':
    num = input ("Enter the number :")
    snail(int(num))
    stdout.write(RESET)