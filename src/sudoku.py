import sys
# import getopt


numbers = []
encoding = []
decimals = []

propostional_var = []

def build_cluase():
    pass
# need to build clauses
#

def convert_base_nine(x,y,z):
  return (x-1)*81 + (y-1)*9 + (z-1) + 1

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
    try:
        file = open(vars[0] , "r")
        out = open(vars[1] , "w")
    except IOError as err:
         print 'cannot open file:' , vars[0], err

    # parse file into ints
    for x in file:
        for i in x:
            numbers.append(int(i))

    # right now we only want to take in input of 81 ints long
    if len(numbers) != 81:
        exit(0)
    # print numbers
    i = 0 # i is the row number
    j = 0 # j is the col
    # encode position of number into list
    for k in numbers:
        pos_y = i % 9
        if pos_y == 0 and i != 0:
            j += 1
        i += 1
        pos_x = j
        encoding.append([pos_x , pos_y , k ])
    print encoding
    d = 1
    count = 0
	
	# Rule 1: There is at least one number in each entry
    for i in range(1,10):
		for j in range(1,10):
			for k in range(1,10):
				out.write(str(convert_base_nine(i, j, k)) + " 0\n" )
			count += 1
			
    # Rule 2: Each number appears at most once in each row
    for j in range(1, 10):
        for k in range(1, 10):
            for i in range(1 , 9):
                for d in range( i + 1 , 10 ):
                    out.write("-" + str(convert_base_nine(i, j, k)) + " -" + str(convert_base_nine(d, j , k)) + " 0\n" )
                    count += 1

    # Rule 3: Each number appears at most once in each col
    for i in range(1, 10):
        for k in range(1, 10):
            for j in range(1 , 9):
                for d in range( j + 1 , 10 ):
                    out.write("-" + str(convert_base_nine(i, j, k)) + " -" + str(convert_base_nine(i, d , k)) + " 0\n" )
                    count += 1

    # Rule 4: Each number appears at most once in a 3x3 sub grid
    for k in range(1, 10):
        for cord_x in range(0 , 3):
            for cord_y in range(0  ,3):
                for i in range( 1 , 4 ):
                    for j in range(1 , 4):

                        for c in range(j+1, 4):
                            pos_x = cord_x*3 + i
                            pos_y1 = cord_y*3 + j
                            pos_y2 = cord_y*3 + k
                            pos_z = k
                            out.write("-" + str(convert_base_nine(pos_x, pos_y1, pos_z)) + " -" + str(convert_base_nine(pos_x, pos_y2 ,pos_z)) + " 0\n")
                            count += 1
                            pass

                        for c in range(i+1 , 4):
                            pos_x = cord_x*3 + i
                            pos_x2 = cord_x*3 + c
                            pos_y1 = cord_y*3 + j
                            pos_y2 = cord_y*3 + 1
                            pos_z = k
                            out.write("-" + str(convert_base_nine(pos_x, pos_y1, pos_z)) + " -" + str(convert_base_nine(pos_x2, pos_y2 ,pos_z)) + " 0\n")
                            count += 1
                            pass

                    out.write("-" + str(convert_base_nine(i, j, k)) + " -" + str(convert_base_nine(i, d , k)) + " 0\n" )
                    count += 1

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

    var_num = 81
    cluase_num = 0
    output = 'p cnf'





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