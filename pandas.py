import pandas as pd
list = ['k','a','v','y','a']
res = pd.Series(list)
print(res)

#0    k
#1    a
#2    v
#3    y
#4    a
#dtype: object


import pandas as pd
import numpy as np
data = np.array(['k','a','v','y','a'])
ser = pd.Series(data,index=[10,11,12,13,14])
print(ser)

#10    k
#11    a
#12    v
#13    y
#14    a
#dtype: object



import pandas as pd
dict = {'name':'kavya','age':23,'designation':'software Engineer'}
ser = pd.Series(dict)
print(ser)


#name                       kavya
#age                           23
#designation    software Engineer
#dtype: object

import pandas as pd
list = ['kavya','divya','mom','dad']
ser = pd.DataFrame(list)
print(ser)

#       0
#0  kavya
#1  divya
#2    mom
#3    dad


import pandas as pd
dict ={'Name':['kavya','divya'],'age':[20,23]}
ser = pd.DataFrame(dict)
print(ser)

#    Name  age
#0  kavya   20
#1  divya   23


import pandas as pd
dict ={'Name':['kavya','divya','priya'],'age':[20,23,24],'Qualification':['BTech','MTech','mbbs']}
df = pd.DataFrame(dict)
print(df[['Name','Qualification']])

 #   Name Qualification
#0  kavya         BTech
#1  divya         MTech
#2  priya          mbbs

import pandas as pd
dict ={'Name':['kavya','divya','priya'],'age':[20,23,24],'Qualification':['BTech','MTech','mbbs']}
ser = pd.DataFrame(dict)
print(ser.loc[0])# to get the index value

import pandas as pd
dict ={'Name':['kavya','divya','priya'],'age':[20,23,24],'Qualification':['BTech','MTech','mbbs']}
ser = pd.DataFrame(dict)
print(ser.loc[0:2])

 #   Name  age Qualification
#0  kavya   20         BTech
#1  divya   23         MTech
#2  priya   24          mbbs

import pandas as pd
import numpy as np
column = ['a','b','c','d']
index = ['A','B','C','D']
df = pd.DataFrame(np.random.rand(4,4),columns=column,index=index)
print(df)

 #       a         b         c         d
#A  0.843980  0.396616  0.490448  0.119916
#B  0.556837  0.886320  0.814478  0.127378
#C  0.803807  0.440287  0.770701  0.842211
#D  0.253803  0.941137  0.968572  0.999391


import pandas as pd
import numpy as np
column = ['a','b','c','d']
indexs = ['A','B','C','D']
df = pd.DataFrame(np.random.rand(4,4),columns = column,index = indexs)
print(df)
print(df.reindex(['w','x','y','z']))


import pandas as pd
import numpy as np
column = ['a','b','c','d']
indexs = ['A','B','C','D']
df = pd.DataFrame(np.random.rand(4,4),columns = column,index = indexs)
print(df)
df1 = df.drop(['A','B'])
print(df1)

 #      a         b         c         d
#C  0.851839  0.448729  0.835584  0.574311
#D  0.183852  0.411755  0.333205  0.805348

import pandas as pd
import numpy as np

dict ={'Name':['kavya','divya','priya'],'age':[20,23,24],'Qualification':['BTech','MTech','mbbs']}
ser = pd.DataFrame(dict)
ser1=ser['Name']
print(ser1)#it prints only the particular column

#0    kavya
#1    divya
#2    priya
#Name: Name, dtype: object

import pandas as pd
df = pd.read_csv(f"#paste the location of csv file")
print(df.describe())

import pandas as pd
df = pd.read_csv(f"{"C:\\Users\\KAVYA JAMMALAMUDI\\Downloads\\world population.csv"}")
print(df.describe())


 #            Rank  2022 Population  ...  Growth Rate  World Population Percentage
#count  234.000000     2.340000e+02  ...   234.000000                   234.000000
#mean   117.500000     3.407441e+07  ...     1.009577                     0.427051
#std     67.694165     1.367664e+08  ...     0.013385                     1.714977
#min      1.000000     5.100000e+02  ...     0.912000                     0.000000
#25%     59.250000     4.197385e+05  ...     1.001775                     0.010000
#50%    117.500000     5.559944e+06  ...     1.007900                     0.070000
#75%    175.750000     2.247650e+07  ...     1.016950                     0.280000
#max    234.000000     1.425887e+09  ...     1.069100                    17.880000

#[8 rows x 13 columns]


import pandas as pd
df = pd.read_csv(f"{"C:\\Users\\KAVYA JAMMALAMUDI\\Downloads\\world population.csv"}")
print(df.isnull())



#      Rank   CCA3  ...  Growth Rate  World Population Percentage
#0    False  False  ...        False                        False
#1    False  False  ...        False                        False
#2    False  False  ...        False                        False
#3    False  False  ...        False                        False
#4    False  False  ...        False                        False
#..     ...    ...  ...          ...                          ...
#229  False  False  ...        False                        False
#230  False  False  ...        False                        False
#231  False  False  ...        False                        False
#232  False  False  ...        False                        False
#233  False  False  ...        False                        False

#[234 rows x 17 columns]



import pandas as pd
df = pd.read_csv(f"{"C:\\Users\\KAVYA JAMMALAMUDI\\Downloads\\world population.csv"}")
print(df.info())# it indictaes the memory,datatype etc etc details


import pandas as pd
df = pd.read_csv(f"{"C:\\Users\\KAVYA JAMMALAMUDI\\Downloads\\world population.csv"}")
print(df.nunique())# counts the number of unique elements


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(f"{"C:\\Users\\KAVYA JAMMALAMUDI\\Downloads\\world population.csv"}")
print(df.plot())
plt.show()# it will plot the graph

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(f"{"C:\\Users\\KAVYA JAMMALAMUDI\\Downloads\\world population.csv"}")
print(df.plot(kind = 'bar'))
plt.show()


import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(f"{"C:\\Users\\KAVYA JAMMALAMUDI\\Downloads\\world population.csv"}")
print(df.plot(kind = 'line',title = "world population",xlabel ='population',ylabel = 'people'))
plt.show()



