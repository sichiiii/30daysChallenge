#https://www.codewars.com/kata/55143152820d22cdf00001bb/train/python  
def count_nines(n):
    tmp, c, nines = n,1,0
    while tmp > 0:
        d = tmp % 10
        tmp //=10
        nines += tmp*c
        if d == 9:
            nines += n%c + 1
        c*=10
    return nines

       # thanks to Vladimir M. because i dont give a shit how to avoid timeout error, my attempts were too slow:

       def count_nines(n):
            nines = 0
            if n == 9:
                return 1
            for i in range(0, n+1):
                nines += len(str(i).split('9')) - 1
            return nines
      
      
       def count_nines(n):
            count = 0
            for i in range(0, n+1):
                while i > 1:
                    if (i % 10) == 9:
                        count+=1
                    i //= 10
            return count
          
       def count_nines(n):
            count = 0
            for i in range(0, n+1):
                for j in str(i):
                    if j == '9':
                        count+=1
            return count
      

    
