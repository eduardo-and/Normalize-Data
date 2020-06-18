import normalization as norm
import pandas as pd
import numpy as np
#
# The library performs data normalization using two techniques, 0 and 1 and score-z. The function accepts the following entries: list, DataFrame pandas,
#  Series pandas, and numPy array. The format of the output is the same as the input. If the data contains a column (or a 1-dimension array) with string
#  or boolean data, the function will not apply normalization.
#
# 
# Functions:

# The library has two functions:
#
#  1# normalizeData(data,opt)
#     This function performs the recognition of the data type and converts it to list,
#     once this it passes the data to the auxiliary function "normalize".

    #   data: list,numPy array, DataFrame or Serie
    #   opt: 1(default) to normalize method 1 and 0, or
    #        2 to normalize method score-z.
    #
    #   return: the same tipe of input
#   
#
#  2# normalize(list,opt)
#     This is a auxiliar function, she performs the normalization in input exclusively of the list type.
#     Exclusive use of the first function is recommended, as it is auxiliary to the above function
        
    #     data: list
    #     opt: 1(default) to normalize method 1 and 0, or
    #          2 to normalize method score-z.
    #
    #     return: list
    
    
dataList = [[121,26,23,64,142],[51451,21,515,132,12],['a1',15,'a2',15,'a3']]
dataFrame = pd.DataFrame(data = [[236,632,12,32],['a12',123,654,25],[12,65,122,36],[152,15,12,32]],columns= ["col1","col2","col3","col4"],index = ["a","b","c","d"])
dataSerie = pd.Series([2232,2256,2132,1265,3269,1541,3626,1561,6266,1515,1544,3226,2321,3218,6269,3266,6964,6641,6362,6366,1548,2352],name= "test1")
dataArray = np.array([[3211,612,3262,615,166,6216,62165,61265,6515,15585,61651,1566,6365,5641,623],[2326,632,664,1555,3269,2151,621,3155,6529,2161,6326,32623,1513,1515,3620]])

dataSet = pd.read_csv("vgsales.csv")

print("List normalized with method 1:\n")    
print(norm.normalizeData(dataList,1))
print("\n")
print("Dataframe normalized with method 2:\n")    
print(norm.normalizeData(dataFrame,2))
print("\n")
print("Serie normalized with method 1:\n")    
print(norm.normalizeData(dataSerie,1))
print("\n")
print("Array normalized with method 2\n")    
print(norm.normalizeData(dataArray,2))
print("\n")
print("Here we have a exemple dataset(Video Game Sales )\n:")
print(dataSet.head)
print("\n")
print("After normalization:")
dataSet = norm.normalizeData(dataSet,2)
print(dataSet.head)
