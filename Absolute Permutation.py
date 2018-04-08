for _ in xrange(input()):
    n,k = map(int,raw_input().strip().split(' '))
    
    numbers = [ i for i in range(1,n+1)]
    _numbers = set(numbers)
    result = [0]*n
  
    done = 0
    count = 1
    error = -1
    
    if(k > int(n/2) or (n%2 == 1 and k%2 == 1)):
        done = 1   
    if(k == 0):
        done = 1
        result = [ i for i in range(1,n+1)]     
    while(done == 0 and len(_numbers) > 0):
        while 1:
            if count in _numbers:break
            count+=1
        x1 = k + count
        x2 = count - k
        check2 = 0
        
        if (x2 in _numbers):
            check2 = 1             
        if((x2 <= 0 or x1 < x2 or check2 == 0) and x1 in _numbers):
            x = x1
            _numbers.remove(x)
            _numbers.remove(count)
            result[count - 1] = x
            result[x - 1] = count     
        elif(check2 == 1):
            x = x2
            _numbers.remove(x)
            _numbers.remove(count)
            result[count - 1] = x
            result[x - 1] = count   
        else:
            done = 1
    if(len(_numbers)> 0 and k > 0):
        print(error)      
    else:
        combined = (' '.join(str(i) for i in result))
        print(combined)
