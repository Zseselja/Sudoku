import sys
# import getopt


numbers = []
encoding = []
decimals = []

propostional_var = []

def build_cluase():
    pass
# need to build cluases
#

def convter_base_nine(x,y,z):
  return (x-1)*81 + (y-1)*9 + (z-1) + 1


# program starts here
def main():
    vars = 0;
    try:
        vars = sys.argv[1:]
    except IOError as err:
        print 'cannot open argv'
        # print help information and exit:+
        print str(err) # will print something like "option -a not recognized"


    #
    # opening file with Sudoku number input inside
    #
    file = ''

    try:
        file = open(vars[0] , "r")
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
    i = 0
    j = 0
    # encode position of number into list
    for k in numbers:
        posy = i % 9
        if posy == 0 and i != 0:
            j += 1
        i += 1
        posx = j
        encoding.append([posx , posy , k ])
    # print encoding
    d = 1
    count = 0
    for x in encoding:
        if x[2] != 0:
            decimals.append(d)
            count += 1
        else:
            decimals.append(-d)
        d += 1
    print decimals

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