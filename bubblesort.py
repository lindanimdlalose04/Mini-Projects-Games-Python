#bubblesort
#the first loop wants to go to the end, start at 0 till 5
#next iteratio 0 to 4, 0 to 3 
nums = [5,3,8,6,7,2]


def sort(nums):
    for i in range(len(nums)-1,0,-1):    #start at 0 so-1,reach till 0, and go backwards -1        #first question is how many times do i do this, second is in which what do i do this 
        for j in range (i):
            if nums[j]>nums[j+1]:       #if first value(j) is greater than second value(j+1) then swapd
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1]= temp



sort(nums)
print(nums)