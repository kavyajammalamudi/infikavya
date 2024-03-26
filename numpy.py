import numpy as np

arr = np.array([1, 2, 3, 4],ndmin=5)
print(arr)
print(type(arr))
print(arr.ndim)
print(arr.shape)
print(arr.dtype)
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

#[[[[[1 2 3 4]]]]]
#<class 'numpy.ndarray'>
#5
#(1, 1, 1, 1, 4)
#int32
#[[1 2 3]
 #[4 5 6]]


import numpy as np
arr = np.array([[1,2,3,4],[4,6,8,10]])
print(arr*arr)
print(arr+arr)
print(arr-arr)
print(arr/arr)
print(arr%arr)
print(arr**arr)


#[[  1   4   9  16]
 #[ 16  36  64 100]]
#[[ 2  4  6  8]
 #[ 8 12 16 20]]
#[[0 0 0 0]
 #[0 0 0 0]]
#[[1. 1. 1. 1.]
# [1. 1. 1. 1.]]
#[[0 0 0 0]
 #[0 0 0 0]]
#[[         1          4         27        256]
# [       256      46656   16777216 1410065408]]


import numpy as np
arr = np.array([[1,2,3,4],[4,6,8,10]])
arr1 =np.random.rand(1,2,3)
print(arr1)

#[[[0.01583431 0.49236264 0.58439451]
  #[0.9484546  0.756985   0.95207125]]]



import numpy as np
arr = np.array([[1,2,3,4],[4,6,8,10]])
arr1 =np.arange(1,10)
print(arr1)
#[1 2 3 4 5 6 7 8 9]



import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[1:5])
#[2 3 4 5]




import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[0:5])
#[1 2 3 4 5]


import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[4:])
#[5 6 7 8]

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[:7])
#[1 2 3 4 5 6 7]


import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[-3:-1])#output:[6,7]



import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[-3:])#output:[6,7,8]




import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[:-1])#output:[1,2,3,4,5,6,7]



import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[1:5:2])#op:[2,4]


import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[::-1])#op:[8,7,6,5,4,3,2,1]



import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[::-2])#op:[8,6,4,2]


import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[::2])#op:[1 3 5 7]


import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
print(arr[::3])#op:[1 4 7]


import numpy as np
arr = np.arr([[1,2,3] #row 0th,[4,5,6] #row 1st,[7,8,9]]#row 2nd)
print(arr)
print(arr[1:2,0:2])
#1:2..#rows selection i.e, it selects 1st row last row is excluded i.e,,2nd ])
#0:2...#it selects 0th and 1st column
#output is [4,5]





import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])# 1 indicates rows and 1:4 columns
#1th dimension index 1 to 4#op:7,8,9




import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0,1:4])#op:2,3,4



import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:0,4])#op:[]


import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:1,4])#op:[5]



import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2,4])#op:[5 10]


import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:3,4])#op:[5 10]


import numpy as np
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:4,4])#op:[5 10]

#3 -d
import numpy as np
arr = np.arr([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)
print(arr[1:,1:,1:3])
output: [11,12]

#(::,::,::)one is layer 2nd row and 3rd coumn
#here 1 to 6 is at 0th layer and 7 to 12 is at 1st layer
# task is to get 11 and 12
# so 11 and 12 present at 1st layer ,,,select layer 1 i.e,,1:
#1st index layer
#1: 1st layer
#1:1st row
#1:3 to select 11 and 12


import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)
print(arr[1:,:,1:])
#output:[[[ 8  9]
 #       [11 12]]]


import numpy as np

# Create a sample array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Reshape the array to a different shape
reshaped_arr = arr.reshape((3, 2))  # Reshaping to a 3x2 array
print("Original array:")
print(arr)
print("\nReshaped array:")
print(reshaped_arr)





