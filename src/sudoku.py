import sys
# import getopt


numbers = []
encoding = []


def main():
    vars = 0;
    try:
        vars = sys.argv[1:]
    except IOError as err:
        print 'cannot open argv'
        # print help information and exit:+
        print str(err) # will print something like "option -a not recognized"

    # if ((vars[2] == "size:")
    #     if(vars == type<int>)




    file = open(vars[0] , "r")
    for x in file:
        for i in x:
            numbers.append(i)


    print numbers
    num = 81
    i = 0
    j = 0



    for x in numbers:
        posx = i % 9
        if posx == 0:
            j += 1
        i += 1
        posy = j
        encoding.append([posx , posy , x ])




# For example the CNF formula (x1 V x3 V x4) ^ (:x1 V x2) ^ (:x3 V :x4) would
# be given by the following le:
# c A sample file
# p cnf 4 3
# 1 3 4 0
# -1 2 0
# -3 -4 0
#




if __name__ == '__main__':
    main()