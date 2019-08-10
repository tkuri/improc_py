#!/usr/bin/python
# coding: UTF-8
 
#f = open('01-07_difspe2pp.csv')
#of = open('01-07_difspe2pp_split.csv','w')
f = open('bioskin30_dino128_h_take1.csv')
of = open('bioskin30_dino128_h_take1_test.csv','w')


count = 1

#5行に1行出力する
#split = 5
#split2 = 100000

#11行に1行出力する（上の5行に1行出力される行は出力しない）
#split = 11
#split2 = 5

#10行に1行出力する
#split = 10
#split2 = 100000

#10行に１行以外出力する
#split = 1
#split2 = 10

split = 10
split2 = 100000

line = f.readline()
while line:
#    print(line)
    line = f.readline()
    if count%split == 0:
        if count%split2 != 0:
            of.writelines(line)
    count = count + 1
f.close
of.close