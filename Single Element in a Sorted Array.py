class Solution:
    def singleNonDuplicate(self,nums):
        low=0
        high=len(nums)-1
        mid=0
        if(high==0):
            print(nums[0])
        elif(nums[0]!=nums[1]):
            print(nums[0])
        elif(nums[high]!=nums[high-1]):
            print(nums[high])

        while(low<=high):
            mid=low+(high-low)//2
            if(nums[mid]!=nums[mid+1] and nums[mid]!=nums[mid-1]):
                return nums[mid]
            
            else:
                high=mid-1
        print(-1)
            
                

t=Solution()
num=[1,2,1]
t.singleNonDuplicate(num)
