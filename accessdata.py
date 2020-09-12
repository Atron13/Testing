#python 3.6.9

if __name__=="__main__":
    total=int(input())
    for i in range(total):
        number,budget = input().split()
        house=[]
        house = [int(house) for house in input().split()] 
        #print("Number of list is: ", house)
        temp=int(budget)
        house.sort()
        t=0
        #print(house)
        for i in range(int(number)):
            if((temp>house[i])|(temp==house[i])):
                temp=temp-house[i]
                t=t+1
        print(t)     
#1
#4 100
#20 90 40 90 


test case
3
4 100
20 90 40 90
4 50
30 30 10 10
3 300
999 999 999
