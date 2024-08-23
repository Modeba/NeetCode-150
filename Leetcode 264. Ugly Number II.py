import pyperclip

def nthUglyNumber(n):
    ugly = [1]
    
    if n <= len(ugly):
        return ugly[n - 1]
    
    i = 0
    while i < n - 1:
        two   = ugly[i] * 2
        three = ugly[i] * 3
        five  = ugly[i] * 5

        if two not in ugly:
            ugly.append(two)
        if three not in ugly:
            ugly.append(three)
        if five not in ugly:
            ugly.append(five)
        
        ugly.sort()
        i += 1
    
    '''with open('zzz.txt','a') as f:
        for u in ugly:
            f.write(str(u) + ', ')'''

    return len(ugly)

print(nthUglyNumber(2000))