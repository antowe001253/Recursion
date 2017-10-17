## What problem I want to solve -> fibanachi get the number where adding the prebious with the prevoius prevopus number
#---------------INPUT and Output relationship
#0 ->1    BASE CASE
#1-> none+1=1 BASE CASE
#2->1+1=2  2 -> result (0)+result(1)
#3->1+2=3  3 -> result (2)+result(1)  -> f(3)=f(2)+f(1)  f(n)=f(n-1)+f(n-2)
#4->2+3=5
#5->3+5=8
#6->5+8=13

#---------- Design and abstraction -- what tools to use




# --writing your algoruthm and implementation
#   do not write long functions, write in peaces
#  Use assertion to check your input and  conditions
#--- test each -- whe you change a code, back it up first, and write commet where you find a bug
#    check each function -> print entry - output - parameter - middle of the code
#    test the whole code
#---- deep test
#   check for input bounderies and extremes - use assertion to break the code (while testing)


####################recursion
#Until you mee the base case.
#first observe the iput and output and see how they are related, if there is repetition or a pathern
# checf if you have any base case: at n=0 and  n=1
#The program will end when it ran through all the script
# the ideo is to run to recur until the base case
#
#

def fib(n):
    assert isinstance (n,int), "n is not an int"
    if n==0: return 1
    if n==1: return 1
    return fib(n-1)+fib(n-2)


#############################################################
########THE TOWEL OF ##############################
###########################################################
# input and output you nedd to dsign
# f(1,A,B)  1__ -> _1_  move(1,A,B)
#          1                                                                             1
#f(2,A,C)  2__ -> 21_ move(1,A,B) = f(1,A,B) and move(2,A,C) ->_12  and move(1,B,C) = f(1,B,C) -> __2
#f(2,pos,go)->f(1,pos,temp) and move(2,pos,go) and f(1,tmep,go)
#f(n,pos,go)->f(n-1,pos,temp) and move (n,pos,go) and f(n-1,temp,go)

def move(A,B):
    assert len(A)>0, "the array you want to move should not be empty"
    B.append(A.pop)

def f(n,pos,des,temp):
    if n==1: move(pos,des)
    else:
        f(n-1,pos,temp,des)
        move(pos,des)
        f(n-1,temp,des,pos)
    print (pos)
    print (des)
    print (temp)
