
num=int(input())

num_list=[]
for i in range(num):
    a=int(input())
    num_list.append(a)




if(sum(num_list)/len(num_list)>=(sum(num_list)//len(num_list))+0.5):
    print(sum(num_list)//len(num_list)+1)
else:
    print(sum(num_list) // len(num_list) )

num_list.sort()

print(num_list[num//2])

print(num_list[-1]-num_list[0])

