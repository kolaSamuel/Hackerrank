#!/bin/python

import sys

def traderProfit(k, n, A):
    # Complete this function
    rows= []
    for _ in xrange(n):rows.append([0])
    rows[n-1].append(0)
    rowMax =[0]*n
    for i in xrange(n):
        for j in xrange(i+1,n):rows[i].append(A[j]-A[i])
        rowMax[i]=max(rows[i][1:])
    rows[n-1].pop(0)
    k=n//2 if k >n//2 else k
    return maxInstance(rows,rowMax,k)

def maxInstance(rows,rowMax,k,maxProfit = 0):
    if len(rows):
        profit = max(rowMax)
        if profit<=0:return 0
        if k==1:return profit
        for i in xrange(len(rows)):
            #print 'row search',i
            for j in xrange(1,len(rows[i])):
                profit = rows[i][j]+maxInstance(rows[j+i+1:],rowMax[j+i+1:],k-1)
                #print 'i,j,profit',i,j,profit
                maxProfit = max(profit,maxProfit)
                #print 'MAX so far',maxProfit
    return maxProfit
if __name__ == "__main__":
    q = int(raw_input().strip())
    for a0 in xrange(q):
        k = int(raw_input().strip())
        n = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))
        result = traderProfit(k, n, arr)
        #print 'The answer is:'
        print result

