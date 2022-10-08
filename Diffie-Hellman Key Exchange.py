import time
p='00:9f:db:8b:8a:00:45:44:f0:04:5f:17:37:d0:ba:\
2e:0b:27:4c:df:1a:9f:58:82:18:fb:43:53:16:a1:\
6e:37:41:71:fd:19:d8:d8:f3:7c:39:bf:86:3f:d6:\
0e:3e:30:06:80:a3:03:0c:6e:4c:37:57:d0:8f:70:\
e6:aa:87:10:33'.translate({ord(':') : None})
prime=int(p,base=16)
base=2
def ProcessTime(func):
    def warp(tar,e,b=2):
        start=time.process_time()
        ret=func(e,b)
        print(f"{tar}={ret} T={time.process_time()-start} secs")
        return ret
    return warp
@ProcessTime
def Compute(e,b=2):
    ret=1
    while e!=0:
        if e&1:
            ret=(ret*b)%prime
        e>>=1
        b=(b**2)%prime
    return ret
while(True):
  try:
    a=int(input('a:'),16)
    b=int(input('b:'),16)
    break
  except:
    print('enter hex')
    pass
A=Compute('A',a)
B=Compute('B',b)
Compute('KA',a,B)
Compute('KB',b,A)