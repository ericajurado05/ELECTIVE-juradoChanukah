def TotalNoOfCandles(s):
    candles = s[0]
    days = s[1]
    
    RequiredNoOfCandles = days + ((days * (days + 1))/2)
    print('{0} {1}'.format(candles, int(RequiredNoOfCandles)))

n = int(input())
for i in range(n):
    s = [int(j) for j in input().split()]
    TotalNoOfCandles(s)
