import sys
import os.path

def usage():
    print ("usage) python splitdata.py filename")

def splitdata(fname, ofname, split1, split2):
    f = open(fname)
    of = open(ofname, 'w')

    count = 1
    line = f.readline()
    of.writelines(line) #first line is label, so write
    while line:
        line = f.readline()
        if count%split1 == 0:
            if count%split2 != 0:
                of.writelines(line)
        count = count + 1
    f.close
    of.close


if __name__ == '__main__':
    args = sys.argv

    if(len(args) !=2 ):        
        usage()
        quit()


    train_fname = os.path.splitext(args[1])[0] + '_train.csv'
    test_fname = os.path.splitext(args[1])[0] + '_test.csv'

    #10行に１行以外出力する
    splitdata(args[1], train_fname, 1, 10)

    #10行に1行出力する
    splitdata(args[1], test_fname, 10, 100000)
