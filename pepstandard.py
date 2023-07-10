
'''  PEP8 code standard '''

def maxProduct(array, n):  #function for find the max product in subarray
    product = array[0]  

    for i in range(n):  
        prod = array[i]  

        for j in range(i + 1, n):  
            product = max(product, prod)  
            prod *= array[j]  

        product = max(product, prod)  
  
    return product  

nums = int(input("enter the array size"))

array = []

for i in range(nums):
    array.append(int(input("enter the value")))

print("The maximum product of subarrays is:", maxProduct(array, nums))  