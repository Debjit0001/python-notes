'''
    FUNCTION DEFINITION:
        def func_name(param1, param2...):
            # body of the function
            return val
        # by default, it returns None
            
    FUNCTION CALL:
        func_name(arg1, arg2...)
'''

def calc_avg(nums):
    sum = 0
    for i in nums:
        sum += i
    return sum/len(nums)

print(calc_avg([1, 2, 3, 4, 5]))

# the print function: 
'''
    def print(
        *values: object,
        sep: str | None = " ",
        end: str | None = "\n",
        file: SupportsWrite[str] | None = None,
        flush: Literal[False] = False
    ) -> None: ...
'''


# recursion:
def print_list(nums, i=0):
    if i == len(nums):
        return
    
    print(nums[i], end=" ")
    print_list(nums, i+1)
    
print_list([1, 2, 3, 4, 5])