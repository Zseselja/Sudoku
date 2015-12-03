import sys
import math
# import getopt


numbers = []
encoding = []
decimals = []

propostional_var = []

def build_cluase():
    pass
# need to build clauses
#

def convert_base_n(x,y,z, base):
  return (x-1)*base*base + (y-1)*base + (z-1) + 1

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
    base = math.sqrt(sudoku_puzzle_length);

    # parse file into ints
    for x in file.read(int(sudoku_puzzle_length)):
        for i in x:
            numbers.append(int(i))

    # right now we only want to take in input of 81 ints long
    if len(numbers) != int(sudoku_puzzle_length):
        exit(0)
    # print numbers
    i = 0 # i is the row number
    j = 0 # j is the col
    # encode position of number into list
    count = 0

    #Rule to add in prefilled entry clauses
    for k in numbers:
        pos_y = (i % base)+1
        if pos_y == 0 and i != 0:
            j += 1
        i += 1
        pos_x = j+1
        encoding.append([pos_x , pos_y , k ])
        if(k != 0):
            pass

            # temp_out.write(str(convert_base_n(pos_x, pos_y, ( i ), base)) + " 0\n" )
            # count += 1

    d = 0
    print encoding

	# Rule 1: There is at least one number in each entry
    for i in range(1,base+1):
        for j in range(1,base+1):
            for k in range(1,base+1):
                temp_out.write(str(convert_base_n(i, j, k, base)) + ' ' )
            temp_out.write('0\n')
            count += 1
    # Rule 2: Each number appears at most once in each row
    for j in range(1, base+1):
        for k in range(1, base+1):
            for i in range(1 , base):
                for d in range( i + 1 , base+1 ):
                    temp_out.write("-" + str(convert_base_n(i, j, k, base)) + " -" + str(convert_base_n(d, j , k, base)) + " 0\n" )
                    count += 1

    # Rule 3: Each number appears at most once in each col
    for i in range(1, base+1):
        for k in range(1, base+1):
            for j in range(1 , base):
                for d in range( j + 1 , base+1 ):
                    temp_out.write("-" + str(convert_base_n(i, j, k, base)) + " -" + str(convert_base_n(i, d , k, base)) + " 0\n" )
                    count += 1

    # Rule 4: Each number appears at most once in a 3x3 sub grid
    for k in range(1, base+1):
        for cord_x in range(0 , math.sqrt(base)):
            for cord_y in range(0 , math.sqrt(base)):
                for i in range( 1 , math.sqrt(base)+1):
                    for j in range(1 , math.sqrt(base)+1):

                        for c in range(j+1, math.sqrt(base)+1):
                            pos_x = cord_x*math.sqrt(base) + i
                            pos_y1 = cord_y*math.sqrt(base) + j
                            pos_y2 = cord_y*math.sqrt(base) + c
                            temp_out.write("-" + str(convert_base_n(pos_x, pos_y1, k, base)) + " -" + str(convert_base_n(pos_x, pos_y2 ,k, base)) + " 0\n")
                            count += 1

                        for c in range(i+1 , math.sqrt(base)+1):
                            for l in range(1, math.sqrt(base)+1):
                                pos_x = cord_x*math.sqrt(base) + i
                                pos_x2 = cord_x*math.sqrt(base) + c
                                pos_y1 = cord_y*math.sqrt(base) + j
                                pos_y2 = cord_y*math.sqrt(base) + l
                                temp_out.write("-" + str(convert_base_n(pos_x, pos_y1, k, base)) + " -" + str(convert_base_n(pos_x2, pos_y2 ,k, base)) + " 0\n")
                                count += 1

    temp_out.close()
    tempFile = 'output_temp.txt'
    temp_out = open( tempFile , "r")
    out.write("p cnf " +  str( len(numbers)*base) + " " + str(count)  + "\n")
    for x in temp_out:
        out.write(x)


    # out.close()
    # out = open(vars[1], "r")
    #
    # for x in out:
    #     for i in x:
    #         numbers.append(i)
    #
    # print max(numbers) ,
    #
    #
    # for x in encoding:
    #     if x[2] != 0:
    #         decimals.append(d)
    #         count += 1
    #     else:
    #         decimals.append(-d)
    #     d += 1
    # print decimals

    # var_num = 81
    # cluase_num = 0
    # output = 'p cnf'





# For example the CNF formula (x1 V x3 V x4) ^ (:x1 V x2) ^ (:x3 V :x4) would
# be given by the following le:
# c A sample file
# p cnf 4 3
# 1 3 4 0
# -1 2 0
# -3 -4 0

# and


# ( 1 3 4 )
# ( -1 2 )
# ( -3 -4 )



if __name__ == '__main__':
    main()