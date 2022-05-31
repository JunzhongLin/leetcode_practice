class Solution:
    def maximumSwap(self, num):
        a = list(map(int, str(num)))
        last = {x: i for i,x in enumerate(a)}
        for i,x in enumerate(a):
            for d in range(9,x,-1):
                if d in last:
                    if last[d]>i:
                        a[last[d]],a[i]=a[i],a[last[d]]
                        return int(''.join(map(str,a)))
        return num