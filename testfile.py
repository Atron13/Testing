#python 3.6.9

if __name__ == "__main__":
    total=int(input())
    n, k, p = [int(n) for n in input().split()]
    #n k p
    #n number of line
    #k number of item beauty
    #p number of plates
    stack=[]
    for i in range(n):
        demo=[]
        demo = [int(demo) for demo in input().split()]
        stack[i]=demo
        
    for i in range(n):
        print(stack[0])
        print(stack[1])
    #for i in range(n):
        #newstack="stack"+str(i)
        #print(newstack)
        #newstack=[1,2,3]
        #print(newstack)
    
    #for i in range(n):
        #stack[i] = [int(stack[i]) for stack[i] in input().split()]
        
test case
2
2 4 5
1 2 3
4 5 6

2
2 4 5
10 10 100 30
80 50 10 50
3 2 3
80 80
15 50
20 10

output

Case #1: 250
Case #2: 180
