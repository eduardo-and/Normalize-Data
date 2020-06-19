# Normalize-Data

**Author:** Eduardo de Andrade;

**Languages/Tools/Frameworks:** Python
 
**Date:** 18/06/2020

**Description:**
The library performs data normalization using two techniques, "0 to 1" and score-z. The function accepts the following entries: list, DataFrame pandas, Series pandas, and numPy array. The format of the output is the same as the input. If the data contains a column (or a 1-dimension array) with string or boolean data, the function will not apply normalization.


### **Run:**
  - #### 1. Move the file normalization.py for inside of your python project and import the library in the file you want to use the library:<br>
              
              import normalization as norm

              
  - #### 2.Use as desired functions. The library contains 2 functions:
    -  ###  **normalizeData(data,opt)**
          **This function performs the recognition of the data type and converts it to list,
     once this it passes the data to the auxiliary function "normalize".**
            
          **Input:** <p>&nbsp; - **data**: list, numPy array, DataFrame or Serie</p>
                     <p>&nbsp; - **opt**: 1(default) to normalize method "1 to 0", or <br>
                    &nbsp;&nbsp;  &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;2 to normalize method score-z.</p>
         **Return:** The same tipe of input.

        
    - ### **normalize(list,opt)**
         **This is a auxiliar function, she performs the normalization in input exclusively of the list type.<br>**
           *Exclusive use of the first function is recommended, as it is auxiliary to the above function*
        
        **Input:**
             <p> &nbsp; - **data**: list</p>
             <p> &nbsp; - **opt**: 1(default) to normalize method "1 to 0", or <br>
              &nbsp;&nbsp;  &nbsp;&nbsp; &nbsp;&nbsp; &nbsp;&nbsp;2 to normalize method score-z.</p>
    
        **Return:** List

         
    
### **Exemples:**
        
  &nbsp;&nbsp; **Import and define the data of different types:**
               
                dataList = [[121,26,23,64,142],[51451,21,515,132,12],['a1',15,'a2',15,'a3']]
                dataFrame = pd.DataFrame(data = [[236,632,12,32],['a12',123,654,25],[12,65,122,36],[152,15,12,32]],columns= ["col1","col2","col3","col4"],index = ["a","b","c","d"])
                dataSerie = pd.Series([2232,2256,2132,1265,3269,1541,3626,1561,6266,1515,1544,3226,2321,3218,6269,3266,6964,6641,6362,6366,1548,2352],name= "test1")
                dataArray = np.array([[3211,612,3262,615,166,6216,62165,61265,6515,15585,61651,1566,6365,5641,623],[2326,632,664,1555,3269,2151,621,3155,6529,2161,6326,32623,1513,1515,3620]])

                dataSet = pd.read_csv("vgsales.csv")

                print("List:\n")
                print(dataList)
                print("\ndataFrame:\n")
                print(dataFrame)
                print("\nSeries:\n")
                print(dataSerie)
                print("\nArray\n")
                print(dataArray)
                print("\nDataSet:\n")
                print(dataSet)

 &nbsp;&nbsp;**Output**:  
                
                
                List:

                [[121, 26, 23, 64, 142], [51451, 21, 515, 132, 12], ['a1', 15, 'a2', 15, 'a3']]

                DataFrame:

                  col1  col2  col3  col4
                a  236   632    12    32
                b  a12   123   654    25
                c   12    65   122    36
                d  152    15    12    32

                Series:

                0     2232
                1     2256
                2     2132
                3     1265
                4     3269
                5     1541
                6     3626
                7     1561
                8     6266
                9     1515
                10    1544
                11    3226
                12    2321
                13    3218
                14    6269
                15    3266
                16    6964
                17    6641
                18    6362
                19    6366
                20    1548
                21    2352
                Name: test1, dtype: int64

                Array

                [[ 3211   612  3262   615   166  6216 62165 61265  6515 15585 61651  1566
                   6365  5641   623]
                 [ 2326   632   664  1555  3269  2151   621  3155  6529  2161  6326 32623
                   1513  1515  3620]]

                DataSet:

                        Rank  ... Global_Sales
                0          1  ...        82.74
                1          2  ...        40.24
                2          3  ...        35.82
                3          4  ...        33.00
                4          5  ...        31.37
                     ...  ...          ...
                16593  16596  ...         0.01
                16594  16597  ...         0.01
                16595  16598  ...         0.01
                16596  16599  ...         0.01
                16597  16600  ...         0.01

                [16598 rows x 11 columns]
                
 &nbsp;&nbsp;  **List normalized with method 1:**
                  
               print("List normalized with method 1:\n")    
               print(norm.normalizeData(dataList,1))
               print("\n")
      
&nbsp;&nbsp;**Output**:

              List normalized with method 1:

              [[0.824, 0.025, 0.0, 0.345, 1.0], [1.0, 0.0, 0.01, 0.002, 0.0], ['a1', 15, 'a2', 15, 'a3']]
  
&nbsp;&nbsp;  **Dataframe normalized with method 2::**
  
           print("Dataframe normalized with method 2:\n")    
           print(norm.normalizeData(dataFrame,2))
           print("\n")
    
   &nbsp;&nbsp;**Output:**
            
            Dataframe normalized with method 2:

                col1   col2   col3   col4
              a  236  1.711 -0.707  0.189
              b  a12 -0.347  1.707 -1.578
              c   12 -0.581 -0.293  1.199
              d  152 -0.783 -0.707  0.189

   
   &nbsp;&nbsp;**Serie normalized with method 1::**
   
          print("Serie normalized with method 1:\n")    
          print(norm.normalizeData(dataSerie,1))
          print("\n")
      
  &nbsp;&nbsp;**Output:**


          Serie normalized with method 1:

            0     0.170
            1     0.174
            2     0.152
            3     0.000
            4     0.352
            5     0.048
            6     0.414
            7     0.052
            8     0.878
            9     0.044
            10    0.049
            11    0.344
            12    0.185
            13    0.343
            14    0.878
            15    0.351
            16    1.000
            17    0.943
            18    0.894
            19    0.895
            20    0.050
            21    0.191
            Name: test1, dtype: float64

  &nbsp;&nbsp; **Array normalized with method 2:**
            
              print("Array normalized with method 2?\n")    
              print(norm.normalizeData(dataArray,2))
              print("\n")
              
   &nbsp;&nbsp;**output:**
                
              Array normalized with method 2

                [[-0.536 -0.647 -0.534 -0.647 -0.667 -0.407  1.994  1.956 -0.394 -0.005
                   1.972 -0.606 -0.401 -0.432 -0.647]
                 [-0.292 -0.512 -0.508 -0.393 -0.17  -0.315 -0.514 -0.185  0.253 -0.314
                   0.227  3.642 -0.398 -0.398 -0.124]]
                         
  &nbsp;&nbsp; **Here we have a exemple dataset(Video Game Sales):**
            
             print(dataSet.head)
             print("\n")
             print("After normalization:")
             dataSet = norm.normalizeData(dataSet,2)
             print(dataSet.head)
   
   &nbsp;&nbsp;**output:**   
   &nbsp;&nbsp; &nbsp;&nbsp; After Normalization:
      ![After](/images/After.png)
      

   &nbsp;&nbsp; &nbsp;&nbsp; Before Normalization:
       ![Before](/images/dataset.png)
              

**To run the examples on your machine, move the description.py and normalization.py file into your project and run description.py.**
