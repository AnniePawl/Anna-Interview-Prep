# Given list of ints, construct product of array of same size such that prod[i] is equal to product of all elements of arr[] except arr[i]


def product_array(nums):
  products_list = []
  product = 1


print(product_array([12,20])) #[20,12]
print(product_array([1,2,3,4])) #[24,12,8,6]