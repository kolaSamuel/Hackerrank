# Enter your code here. Read input from STDIN. Print output to STDOUT
import urllib
opener = urllib.URLopener()
myurl = "https://hr-testcases-us-east-1.s3.amazonaws.com/2335/input15.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1511960060&Signature=0sfR7zqsoh1hieWd7rf4pFLFgM4%3D&response-content-type=text%2Fplain"
myfile = opener.open(myurl)
outfile = open('Test.txt','w')

def specialArray(string):
    result = []
    prev = string[0]
    count = 0
    for x in string:
        if x == prev:
            count+=1
        else:
            result.append((prev,count))
            count = 1
            prev = x
    result.append((prev,count))
    #for +1 comparison
    result.append(('a',0))
    return result

def fill(array,value):
    x,i = value
    for _ in xrange(i):
        array.append(x)

def select(A,B,x,y,i,j):
    if A[x+1][0]< A[x][0]:#or B[y+1][0] >= A[x+1][0]:#or (B[y+1][0] == A[x+1][0] and A):
        fill(result,A[i])
        i+=1
    else:
        fill(result,B[j])
        j+=1
    return(i,j)
        
n = int(myfile.readline().strip())       
for _ in xrange(n):
    A = specialArray(myfile.readline().strip())
    B = specialArray(myfile.readline().strip())      
    a = len(A)-1
    b = len(B)-1
    i,j = 0,0
    result = bytearray()
    while i < a and j < b:
##        if _ == 4:
##            if len(result) > 9 and len(result) < 11:
##                print i,j
##                print A[:10]#A[i-1],A[i],A[i+1],A[i+2],A[i+3]
##                print B[:10]#B[j-1],B[j],B[j+1],B[j+2],B[j+3]
##                print result
##                print
        if A[i][0] < B[j][0]:
            fill(result,A[i])
            i+=1
        elif A[i][0] > B[j][0]:
            fill(result,B[j])
            j+=1
        else:
            if A[i][1] < B[j][1]:
                i,j = select(A,B,i,j,i,j)
            elif A[i][1] == B[j][1]:
                for k in xrange(min(a-i,b-j)):
                    if A[i+k] != B[j+k]:
                        break
                _i,_j = i+k,j+k
##                if len(result) > 0 and len(result) < 2 and _ == 4:
##                    print k,a,b,i,j
##                    print A[i]
##                    print A[_i],A[_i+1]
##                    print B[_j],B[_j+1]
##                    print
                if A[_i][0] < B[_j][0]:
                    fill(result,A[i])
                    i+=1
                elif A[_i][0] > B[_j][0]:
                    fill(result,B[j])
                    j+=1
                elif A[_i][1] < B[_j][1]:
                    i,j = select(A,B,_i,_j,i,j)
                elif A[_i][1] > B[_j][1]:
                    j,i = select(B,A,_j,_i,j,i)
                elif A[_i+1][0] < B[_j+1][0]:
                    fill(result,A[i])
                    i+=1
                else:
                    fill(result,B[j])
                    j+=1
                    
            else:
                j,i = select(B,A,j,i,j,i)
##    if _ == 4:
##        print len(result),a,b,i,j
##        print A[i-3:]
##        print B[j:10]
    for k in xrange(i,a):fill(result,A[k])
    for k in xrange(j,b):fill(result,B[k])
    print >>outfile,result
outfile.close()
infile = open('Test.txt','r')
myurl = "https://hr-testcases-us-east-1.s3.amazonaws.com/2335/output15.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1511960064&Signature=c6L9VJOBnibiQJM%2FMeZUBqObYsY%3D&response-content-type=text%2Fplain"
ansFile = opener.open(myurl)

for _ in xrange(n):
    mysol = infile.readline().strip()
    sol = ansFile.readline().strip()
    if mysol == sol:
        print _,'correct'
    else:
        print _,'fail',len(sol),len(mysol)
        for i in xrange(len(sol)):
            if sol[i] != mysol[i]:
                print i
                print sol[i-10:i+10],'\n',mysol[i-10:i+10]
                break
infile.close()
