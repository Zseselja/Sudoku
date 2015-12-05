import sys
import math
import time
import os
import pycosat


pycoList = []
numbers = []
encoding = []
decimals = []
dict = {'a' : 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18,
        'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28,
        't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 33}


def build_cluase():
    pass
# need to build clauses
#

def convert_base_n(x,y,z, base):
  return int((x-1)*base*base + (y-1)*base + (z-1) + 1)

#---------------------------------------------
# 				program starts here
#---------------------------------------------
def main():
    vars = 0
    try:
        vars = sys.argv[1:]
    except IOError as err:
        print 'cannot open argv'
        # print help information and exit:+
        print str(err) # will print something like "option -a not recognized"


    #---------------------------------------------
    # opening file with Sudoku number input inside
    #---------------------------------------------
    file = ''
    out = ''
    # tempfile = 'nsize_output_temp.txt'
    try:
        file = open(vars[0] , "r")
        out = open(vars[1] , "w")
        # temp_out = open(tempfile , "w")
        sudoku_puzzle_length = vars[2]
    except IOError as err:
         print 'cannot open file:' , vars[0], err

    # Find the size of each row/column/square


    base = math.sqrt(float(sudoku_puzzle_length))
    base = int(base)
    # parse file into ints
    for x in file.read(int(sudoku_puzzle_length)):
        for i in x:
            if i == '\n':
                continue
            else:
                value = dict.get(i)
                # print value
                if value == None:
                     numbers.append(int(i))
                else:
                    numbers.append(value)
                # print i



    # right now we only want to take in input of 81 ints long
    if len(numbers) != int(sudoku_puzzle_length):
        print 'Didnt read right...'
        print 'Make sure the \\n are out of the input'
        exit(0)
    # print numbers
    i = 0 # i is the row number
    j = 0 # j is the col
    # encode position of number into list
    count = 0

    #Rule to add in prefilled entry clauses

    for k in numbers:
        sublist = []
        pos_y = (i % int(base))+1
        if pos_y == 1 and i != 0:
            j += 1
        i += 1
        pos_x = j+1
        encoding.append([pos_x , pos_y , k ])
        if(k != 0):
            pass
            sublist.append(convert_base_n(pos_x, pos_y, int(k), base))
            pycoList.append(sublist)
            # temp_out.write(str(convert_base_n(pos_x, pos_y, ( i ), base)) + " 0\n" )
            # count += 1

    # print pycoList
    d = 0
    # print encoding

	# Rule 1: There is at least one number in each entry
    for i in range(1,int(base)+1):
        # sublist = []
        for j in range(1,int(base)+1):
            sublist = []
            for k in range(1,int(base)+1):
                sublist.append(convert_base_n(i, j, k, int(base)))
            pycoList.append(sublist)
            count += 1
    # Rule 2: Each number appears at most once in each row
    for j in range(1, int(base)+1):
        for k in range(1, int(base)+1):
            for i in range(1 , int(base)):
                for d in range( i + 1 , int(base)+1 ):
                    sublist = []
                    sublist.append(-1*convert_base_n(i, j, k, int(base)))
                    sublist.append(-1*convert_base_n(d, j, k, int(base)))
                    pycoList.append(sublist)

    # Rule 3: Each number appears at most once in each col
    for i in range(1, int(base)+1):
        for k in range(1, int(base)+1):
            for j in range(1 , int(base)):
                for d in range( j + 1 , int(base)+1 ):
                    sublist = []
                    sublist.append(-1*convert_base_n(i, j, k, int(base)))
                    sublist.append(-1*convert_base_n(i, d, k, int(base)))
                    pycoList.append(sublist)


    # Rule 4: Each number appears at most once in a 3x3 sub grid
    for k in range(1, int(base)+1):
        for cord_x in range(0 , int(math.sqrt(base))):
            for cord_y in range(0 , int(math.sqrt(base))):
                for i in range( 1 , int(math.sqrt(base))+1):
                    for j in range(1 , int(math.sqrt(base))+1):

                        for c in range(j+1, int(math.sqrt(base))+1):
                            pos_x = cord_x*int(math.sqrt(base)) + i
                            pos_y1 = cord_y*int(math.sqrt(base)) + j
                            pos_y2 = cord_y*int(math.sqrt(base)) + c
                            sublist = []
                            sublist.append(-1*convert_base_n(pos_x, pos_y1, k, base))
                            sublist.append(-1*convert_base_n(pos_x, pos_y2 ,k, base))
                            pycoList.append(sublist)

                        for c in range(i+1 , int(math.sqrt(base))+1):
                            for l in range(1, int(math.sqrt(base))+1):
                                pos_x = cord_x*int(math.sqrt(base)) + i
                                pos_x2 = cord_x*int(math.sqrt(base)) + c
                                pos_y1 = cord_y*int(math.sqrt(base)) + j
                                pos_y2 = cord_y*int(math.sqrt(base)) + l
                                sublist = []
                                sublist.append(-1*convert_base_n(pos_x, pos_y1, k, base))
                                sublist.append(-1*convert_base_n(pos_x2, pos_y2 ,k, base))
                                pycoList.append(sublist)

    # print pycoList
    pycoReturn = pycosat.solve(pycoList)

    final = "resultsFile.txt"
    final = open( final , 'w')
    # satFile = open(satFile , 'r')
    #
    # solved = satFile.readline().strip()
    #
    #

    # if solved == 'SAT':
    values = ''
    i = 0
    for k in pycoReturn:
        i += 1
        if (i != len(pycoReturn)): values = values + str(k) + ' '
        else : values = values + str(k)
    # values = ''.join(str(k) for k in pycoReturn)
    # print values
    split_values = values.split(' ')
    # print split_values
    for a in range((len(split_values))):
        split_values[a] = int(split_values[a])
    final.write("Solved Puzzle: \n")
    for x in range(0 , int(base)):
        line = ''
        for y in range(0 , int(base)):
            for z in range( 0 , int(base)):
                 if(split_values[x*(int(base*base)) + int(base)*y + z] >= 0):
                     line = line + str(z+1) + ' '
                     break
        # print(line + '\n')
        final.write(line + '\n')

    exit(0)





if __name__ == '__main__':
    main()
