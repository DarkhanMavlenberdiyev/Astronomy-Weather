

def sum_up_target(lis,target):
	if lis[0]+lis[len(lis)-1]==target:
		return lis[0],lis[len(lis)-1]
	if lis[0]+lis[len(lis)-1]>target:
		return sum_up_target(lis[:-1],target)
	return sum_up_target(lis[1:],target)


def find_peak(lis):
	left = 0
	right = len(lis)-1
	middle = len(lis)//2
	while(left<right-1):

		if lis[middle]<lis[middle+1]:
			left=middle+1
			middle = len(lis[left:])//2
			print(middle)
		elif lis[middle]>lis[middle+1]:
			right=middle
			middle = len(lis[:right])//2
			print(middle)
			break
			
	return left

def min_sub_sum(lis,target):
	lis2 = []
	lis2.append(lis[0])
	for i in range(1,len(lis)):
		lis2.append(lis2[-1]+lis[i])
	

lis = [2,5,12, 15, 16, 20, 21, 23]
lis2 = [4,2,5,6,8,3,1]
lis3 = [2,3,1,2,4,3]
print(min_sub_sum(lis3,7))