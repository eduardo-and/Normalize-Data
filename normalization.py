#The library performs the normalization in a panda dataframes,Panda Series, NumPy arrays and lists, using the method of 0 and 1 or score-z.

import pandas as pd
import numpy as np
import math


#The function performs the normalization of data, the accepted types of input are list, pandas DataFrame, pandas Series and numPy lists.
def normalizeData(data,tp=1): 
    def verifyNumeric(data):
        flag=0
        for x in data:
            if(type(x)==str or type(x)==bool):
                flag+=1
                return False
        return True
        
    def desmenber(data,tp,esc=1): #Type 1 = dataframe #Type 2 = list
        if(tp==1):
            size = data.shape[1]
            
            col = data.columns
            indx= data.index
            indx= indx.tolist()
            
            if(size==1): 
                temp = data[col[0]]
                temp = normalize(temp.tolist(),esc)
                new = pd.DataFrame(data= temp,index=indx,columns=col)
                return new        
            for x in range(size):
                
                if(not verifyNumeric(data[col[x]])):
                    if(x==0):
                        new = pd.DataFrame(data = data[col[0]],index = indx,columns = [col[0]])
                        continue
                    else:
                        new.insert(loc = x, value = data[col[x]],column = col[x])
                else:
                    
                    li = data[col[x]]
                                    
                    temp = normalize(li.tolist(),esc)
                    if(x==0):
                        new = pd.DataFrame(temp,index = indx ,columns=[col[0]])
                    else:
                        new.insert(loc = x,value = temp,column= col[x])    
          
        if(tp==2):
            size = len(data)
            new = []
            
            if(size==1): 
                return normalize(data.tolist(),esc)
                
            for x in range(size):
                
                if(not verifyNumeric(data[x])):
                    if(x==0):
                        new.append(temp)
                    else:
                        new.append(data[x])
                else:
                         
                    temp = normalize(data[x],esc)
                    if(x==0):
                        new.append(temp)
                    else:
                        new.append(temp)
            
        return new
    
        
    if(type(data) == list): 
        if(len(data)==0): return False
        try:
            if(len(data[0])): return desmenber(data,2,tp)  
        except:
            return normalize(data,tp)
        
            
    elif(isinstance(data,pd.core.frame.DataFrame)): 
        if(data.empty): return False
        
        return desmenber(data,1,tp)
    
    elif(isinstance(data,pd.core.series.Series)):  
        if(data.empty): return False
        
        temp = pd.Series(normalize(data,tp),name=data.name,index=data.index)
        
        return temp
                        
    elif(isinstance(data,np.ndarray)):  
        if(data.ndim==0): return False
        data= data.tolist()
        try:
            if(len(data[0])): return np.array(desmenber(data,2,tp))  
        except:
            return np.array(normalize(data,tp))    
          
    else: return False


#The function performs normalization on lists
def normalize(data,tp=1):
    def average(data):
        av = 0
        for x in data:
            av += x

        av = av/len(data)
        return av
   
    # Calculate Standart Deviation of list
    def dP(data, avg):
        # Calculate the variance of list
        def variance(data, avg):
            sum_uni = 0
            for val in data:
                sum_uni += (val-avg)**2

            V = sum_uni/len(data)
            return V

        return math.sqrt(variance(data, avg))
   
    #Performs the normalization with score-z
    def scoreZ(data,dp,avg):
                    
        new = [round((x-avg)/dp,3) for x in data]
                
        return new
 
    
    if(tp==1):
        data_min=min(data)
        data_max=max(data)
        min_max=data_max-data_min
        new = [ round((x-data_min)/min_max,3) for x in data]
        return new 
    
    else:
        avg = average(data)
        return scoreZ(data,dP(data,avg),avg)        
                        




    


