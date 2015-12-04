import sys
import math
import time
import os
# import getopt


numbers = []
encoding = []
decimals = []
dict = {'a' : 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17, 'i': 18,
        'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r': 27, 's': 28,
        't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33, 'y': 34, 'z': 33}


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
    tempfile = 'nsize_output_temp.txt'
    try:
        file = open(vars[0] , "r")
        out = open(vars[1] , "w")
        temp_out = open(tempfile , "w")
        sudoku_puzzle_length = vars[2]
    except IOError as err:
         print 'cannot open file:' , vars[0], err

    # Find the size of each row/column/square


    base = math.sqrt(float(sudoku_puzzle_length));

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
    #for k in numbers:
       # pos_y = (i % int(base))+1
       # if pos_y == 1 and i != 0:
       #     j += 1
       # i += 1
       # pos_x = j+1
       # encoding.append([pos_x , pos_y , k ])
       # if(k != 0):
       #     pass

            # temp_out.write(str(convert_base_n(pos_x, pos_y, ( i ), base)) + " 0\n" )
            # count += 1

    d = 0

    #################
    #MINIMAL ENCODING
    #################
	# Rule 1: There is at least one number in each entry
    for i in range(1,int(base)+1):
        for j in range(1,int(base)+1):
            for k in range(1,int(base)+1):
                temp_out.write(str(convert_base_n(i, j, k, int(base))) + ' ' )
            temp_out.write('0\n')
            count += 1
            
    # Rule 2: Each number appears at most once in each row
    for j in range(1, int(base)+1):
        for k in range(1, int(base)+1):
            for i in range(1 , int(base)):
                for d in range( i + 1 , int(base)+1 ):
                    temp_out.write("-" + str(convert_base_n(i, j, k, int(base))) + " -" + str(convert_base_n(d, j , k, int(base) )) + " 0\n" )
                    count += 1

    # Rule 3: Each number appears at most once in each col
    for i in range(1, int(base)+1):
        for k in range(1, int(base)+1):
            for j in range(1 , int(base)):
                for d in range( j + 1 , int(base)+1 ):
                    temp_out.write("-" + str(convert_base_n(i, j, k, int(base))) + " -" + str(convert_base_n(i, d , k, int(base))) + " 0\n" )
                    count += 1

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
                            temp_out.write("-" + str(convert_base_n(pos_x, pos_y1, k, base)) + " -" + str(convert_base_n(pos_x, pos_y2 ,k, base)) + " 0\n")
                            count += 1

                        for c in range(i+1 , int(math.sqrt(base))+1):
                            for l in range(1, int(math.sqrt(base))+1):
                                pos_x = cord_x*int(math.sqrt(base)) + i
                                pos_x2 = cord_x*int(math.sqrt(base)) + c
                                pos_y1 = cord_y*int(math.sqrt(base)) + j
                                pos_y2 = cord_y*int(math.sqrt(base)) + l
                                temp_out.write("-" + str(convert_base_n(pos_x, pos_y1, k, base)) + " -" + str(convert_base_n(pos_x2, pos_y2 ,k, base)) + " 0\n")
                                count += 1
    
    #################
    #EXTENDED ENCODING
    #################    
    # Rule 5: There is at most one number in each entry
    for i in range(1, int(base)+1):
        for j in range(1, int(base)+1):
            for k in range(1 , int(base)):
                for d in range( k + 1 , int(base)+1 ):
                    temp_out.write("-" + str(convert_base_n(i, j, k, int(base))) + " -" + str(convert_base_n(i, j , d, int(base) )) + " 0\n" )
                    count += 1
                    
                    
    # Rule 6: Each number appears at least once in each row
    for j in range(1,int(base)+1):
        for k in range(1,int(base)+1):
            for i in range(1,int(base)+1):
                temp_out.write(str(convert_base_n(i, j, k, int(base))) + ' ' )
            temp_out.write('0\n')
            count += 1
    
    # Rule 7: Each number appears at least once in each column/square
    for i in range(1,int(base)+1):
        for k in range(1,int(base)+1):
            for j in range(1,int(base)+1):
                temp_out.write(str(convert_base_n(i, j, k, int(base))) + ' ' )
            temp_out.write('0\n')
            count += 1
            
    # Rule 8: Each number appears at least once in each 3x3 sub-grid
    for k in range(1,int(base)+1):
        for d in range(0,int(math.sqrt(base))):
            for l in range(0,int(math.sqrt(base))):
                for i in range(1, int(math.sqrt(base))+1):
                    for j in range(1, int(math.sqrt(base))+1):
                        temp_out.write(str(convert_base_n(i, j, k, int(base))) + ' ' )
		temp_out.write('0\n')
		count += 1
    
    temp_out.close()


    temp_out = open( tempfile , "r")
    # print base
    out.write("p cnf " +  str( int(len(numbers)*base)) + " " + str(count)  + "\n")

    timer = time.time()
    for x in temp_out:
        out.write(x)
    out.close()

    #Send to minisat
    cmd = "./minisat.exe " + str(vars[1]) + " satoutput.txt"
    os.system(cmd)

    #Send to minisat
    call([vars[3], "output.txt", "satoutput.txt"])

    satFile = "satoutput.txt"
    final = "resultsFile.txt"
    final = open( final , 'w')
    satFile = open(satFile , 'r')

    solved = satFile.readline().strip()

    if solved == 'SAT':
        values = satFile.readline()
        split_values = values.split(' ')
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
            print(line + '\n')
            final.write(line + '\n')
    else:
        exit(0)
        pass
        # unsolved




if __name__ == '__main__':
    main()
