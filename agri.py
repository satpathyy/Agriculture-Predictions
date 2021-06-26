# -*- coding: utf-8 -*-
#-----(1) data analysis of agriculture sector -----

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('C:/Users/Jeet Das/Desktop/Major Project - Indian Economy/Project ( Section 1-Indian Economy)/Section-1_Data_sheet/(02)_agriculture.csv',encoding="cp1252")

print("\n------- output data :-----------\n")
print("Agriculture data analysis:")
print("\n-----------------------------------\n")

# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :


print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

#Question – C : State_Name (using GROUP BY method) and no. of states :

state_names = df.groupby(['State_Name'])[['District_Name']].count()
print("---------------------------------")
print("\t states names : ")
print("-------------------------------")
print(state_names)
print("-------------------------------")
count = 0
for row in range(len(state_names)): 
        count = count+1
print("total no. of states = ",count)        
print("-----------------------------\n")


#Question – 1 : Andaman and Nicobar Islands(Detailed analysis) :

print("\n--- State-1: Andaman and Nicobar Islands(Detailed analysis) :-------")
df_andaman = df[df.State_Name == 'Andaman and Nicobar Islands']
df_andaman_dist = df_andaman.groupby(['District_Name'])[['Crop_Year']].count()
print(df_andaman_dist)

print("-----------------------------")
count = 0
for row in range(len(df_andaman_dist)): 
        count = count+1
print("total no. of district in [State-1] Andaman and Nicobar Islands = ",count)        
print("-----------------------------\n")

# crop year in Andaman and Nicobar Islands

print("------ Crop year in Andaman and Nicobar Islands --------")
df_andaman_year = df_andaman.groupby(['Crop_Year'])[['Crop_Year']].count()
print(df_andaman_year)

# crop types in Andaman and Nicobar Islands

print("----- Crop types in Andaman and Nicobar Islands --------")
df_andaman_crop = df_andaman.groupby(['Crop'])[['Crop']].count()
print(df_andaman_crop)

# details of Andaman( [1] Nicobars)

print("------ Details of Andaman( [1] Nicobars) -----------------")
df_andaman_1 = df_andaman[df_andaman.District_Name == 'NICOBARS']

# finding sum of year =( 2000,2001,2002,2003,2004,2005,2006,2010 )

print("---------------------------------")
print("Sum for Crop_Year = 2000")
print("---------------------------------")
df_andaman_1_2000 = df_andaman_1.loc[df_andaman_1['Crop_Year'] == 2000,'Area':'Production']
df_andaman_1_2000_sum = df_andaman_1_2000.sum(axis = 0, skipna = True)
print(df_andaman_1_2000_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2001")
print("---------------------------------")
df_andaman_1_2001 = df_andaman_1.loc[df_andaman_1['Crop_Year'] == 2001,'Area':'Production']
df_andaman_1_2001_sum = df_andaman_1_2001.sum(axis = 0, skipna = True)
print(df_andaman_1_2001_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2002")
print("---------------------------------")
df_andaman_1_2002 = df_andaman_1.loc[df_andaman_1['Crop_Year'] == 2002,'Area':'Production'] 
df_andaman_1_2002_sum = df_andaman_1_2002.sum(axis = 0, skipna = True)
print(df_andaman_1_2002_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2003")
print("---------------------------------")
df_andaman_1_2003 = df_andaman_1.loc[df_andaman_1['Crop_Year'] == 2003,'Area':'Production'] 
df_andaman_1_2003_sum = df_andaman_1_2003.sum(axis = 0, skipna = True)
print(df_andaman_1_2003_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2004")
print("---------------------------------")
df_andaman_1_2004 = df_andaman_1.loc[df_andaman_1['Crop_Year'] == 2004,'Area':'Production'] 
df_andaman_1_2004_sum = df_andaman_1_2004.sum(axis = 0, skipna = True)
print(df_andaman_1_2004_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2005")
print("---------------------------------")
df_andaman_1_2005 = df_andaman_1.loc[df_andaman_1['Crop_Year'] == 2005,'Area':'Production']
df_andaman_1_2005_sum = df_andaman_1_2005.sum(axis = 0, skipna = True)
print(df_andaman_1_2005_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2006")
print("---------------------------------")
df_andaman_1_2006 = df_andaman_1.loc[df_andaman_1['Crop_Year'] == 2006,'Area':'Production'] 
df_andaman_1_2006_sum = df_andaman_1_2006.sum(axis = 0, skipna = True)
print(df_andaman_1_2006_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2010")
print("---------------------------------")
df_andaman_1_2010 = df_andaman_1.loc[df_andaman_1['Crop_Year'] == 2010,'Area':'Production'] 
df_andaman_1_2010_sum = df_andaman_1_2010.sum(axis = 0, skipna = True)
print(df_andaman_1_2010_sum)
print("---------------------------------")


# details of Andaman( [2] NORTH AND MIDDLE ANDAMAN )

print("------ Details of Andaman( [2] NORTH AND MIDDLE ANDAMAN )-----------")
df_andaman_2 = df_andaman[df_andaman.District_Name == 'NORTH AND MIDDLE ANDAMAN']

# finding sum of year =( 2000,2001,2002,2003,2004,2005,2006,2010 )

print("---------------------------------")
print("Sum for Crop_Year = 2000")
print("---------------------------------")
df_andaman_2_2000 = df_andaman_2.loc[df_andaman_2['Crop_Year'] == 2000,'Area':'Production'] 
df_andaman_2_2000_sum = df_andaman_2_2000.sum(axis = 0, skipna = True)
print(df_andaman_2_2000_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2001")
print("---------------------------------")
df_andaman_2_2001 = df_andaman_2.loc[df_andaman_2['Crop_Year'] == 2001,'Area':'Production'] 
df_andaman_2_2001_sum = df_andaman_2_2001.sum(axis = 0, skipna = True)
print(df_andaman_2_2001_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2002")
print("---------------------------------")
df_andaman_2_2002 = df_andaman_2.loc[df_andaman_2['Crop_Year'] == 2002,'Area':'Production'] 
df_andaman_2_2002_sum = df_andaman_2_2002.sum(axis = 0, skipna = True)
print(df_andaman_2_2002_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2003")
print("---------------------------------")
df_andaman_2_2003 = df_andaman_2.loc[df_andaman_2['Crop_Year'] == 2003,'Area':'Production'] 
df_andaman_2_2003_sum = df_andaman_2_2003.sum(axis = 0, skipna = True)
print(df_andaman_2_2003_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2004")
print("---------------------------------")
df_andaman_2_2004 = df_andaman_2.loc[df_andaman_2['Crop_Year'] == 2004,'Area':'Production'] 
df_andaman_2_2004_sum = df_andaman_2_2004.sum(axis = 0, skipna = True)
print(df_andaman_2_2004_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2005")
print("---------------------------------")
df_andaman_2_2005 = df_andaman_2.loc[df_andaman_2['Crop_Year'] == 2005,'Area':'Production'] 
df_andaman_2_2005_sum = df_andaman_2_2005.sum(axis = 0, skipna = True)
print(df_andaman_2_2005_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2006")
print("---------------------------------")
df_andaman_2_2006 = df_andaman_2.loc[df_andaman_2['Crop_Year'] == 2006,'Area':'Production'] 
df_andaman_2_2006_sum = df_andaman_2_2006.sum(axis = 0, skipna = True)
print(df_andaman_2_2006_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2010")
print("---------------------------------")
df_andaman_2_2010 = df_andaman_2.loc[df_andaman_2['Crop_Year'] == 2010,'Area':'Production'] 
df_andaman_2_2010_sum = df_andaman_2_2010.sum(axis = 0, skipna = True)
print(df_andaman_2_2010_sum)
print("---------------------------------")

# details of Andaman( [3] SOUTH ANDAMANS )

print("----- Details of Andaman( [3] SOUTH ANDAMANS )-------")
df_andaman_3 = df_andaman[df_andaman.District_Name == 'SOUTH ANDAMANS']

# finding sum of year =( 2000,2001,2002,2003,2004,2005,2006,2010 )

print("---------------------------------")
print("Sum for Crop_Year = 2000")
print("---------------------------------")
df_andaman_3_2000 = df_andaman_3.loc[df_andaman_3['Crop_Year'] == 2000,'Area':'Production']
df_andaman_3_2000_sum = df_andaman_3_2000.sum(axis = 0, skipna = True)
print(df_andaman_3_2000_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2001")
print("---------------------------------")
df_andaman_3_2001 = df_andaman_3.loc[df_andaman_3['Crop_Year'] == 2001,'Area':'Production']
df_andaman_3_2001_sum = df_andaman_3_2001.sum(axis = 0, skipna = True)
print(df_andaman_3_2001_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2002")
print("---------------------------------")
df_andaman_3_2002 = df_andaman_3.loc[df_andaman_3['Crop_Year'] == 2002,'Area':'Production']
df_andaman_3_2002_sum = df_andaman_3_2002.sum(axis = 0, skipna = True)
print(df_andaman_3_2002_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2003")
print("---------------------------------")
df_andaman_3_2003 = df_andaman_3.loc[df_andaman_3['Crop_Year'] == 2003,'Area':'Production']
df_andaman_3_2003_sum = df_andaman_3_2003.sum(axis = 0, skipna = True)
print(df_andaman_3_2003_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2004")
print("---------------------------------")
df_andaman_3_2004 = df_andaman_3.loc[df_andaman_3['Crop_Year'] == 2004,'Area':'Production']
df_andaman_3_2004_sum = df_andaman_3_2004.sum(axis = 0, skipna = True)
print(df_andaman_3_2004_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2005")
print("---------------------------------")
df_andaman_3_2005 = df_andaman_3.loc[df_andaman_3['Crop_Year'] == 2005,'Area':'Production']
df_andaman_3_2005_sum = df_andaman_3_2005.sum(axis = 0, skipna = True)
print(df_andaman_3_2005_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2006")
print("---------------------------------")
df_andaman_3_2006 = df_andaman_3.loc[df_andaman_3['Crop_Year'] == 2006,'Area':'Production']
df_andaman_3_2006_sum = df_andaman_3_2006.sum(axis = 0, skipna = True)
print(df_andaman_3_2006_sum)
print("---------------------------------")
print("Sum for Crop_Year = 2010")
print("---------------------------------")
df_andaman_3_2010 = df_andaman_3.loc[df_andaman_3['Crop_Year'] == 2010,'Area':'Production']
df_andaman_3_2010_sum = df_andaman_3_2010.sum(axis = 0, skipna = True)
print(df_andaman_3_2010_sum)
print("---------------------------------")


#Question-(2) : Andhra Pradesh

print("\n----- State-2 : Andhra Pradesh ---------")
df_andhra = df[df.State_Name == 'Andhra Pradesh']
df_andhra_dist = df_andhra.groupby(['District_Name'])[['Crop_Year']].count()
print(df_andhra_dist)

# crop year in Andhra Pradesh

df_andhra_year = df_andhra.groupby(['Crop_Year'])[['Crop_Year']].count()
print(df_andhra_year)

# crop types in Andhra Pradesh

df_andhra_crop = df_andhra.groupby(['Crop'])[['Crop']].count()
print(df_andhra_crop)


#details of Andhra( [1] ANANTAPUR )

print("---- Details of Andhra( [1] ANANTAPUR )------")
df_andhra_1 = df_andhra[df_andhra.District_Name == 'ANANTAPUR']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_andhra_1_1997 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 1997,'Area':'Production']
df_andhra_1_1997_sum = df_andhra_1_1997.sum(axis = 0, skipna = True)
print(df_andhra_1_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_andhra_1_1998 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 1998,'Area':'Production']
df_andhra_1_1998_sum = df_andhra_1_1998.sum(axis = 0, skipna = True) 
print(df_andhra_1_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_andhra_1_1999 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 1999,'Area':'Production']
df_andhra_1_1999_sum = df_andhra_1_1999.sum(axis = 0, skipna = True) 
print(df_andhra_1_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_andhra_1_2000 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2000,'Area':'Production']
df_andhra_1_2000_sum = df_andhra_1_2000.sum(axis = 0, skipna = True) 
print(df_andhra_1_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_andhra_1_2001 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2001,'Area':'Production'] 
df_andhra_1_2001_sum = df_andhra_1_2001.sum(axis = 0, skipna = True)
print(df_andhra_1_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_andhra_1_2002 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2002,'Area':'Production']
df_andhra_1_2002_sum = df_andhra_1_2002.sum(axis = 0, skipna = True) 
print(df_andhra_1_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_andhra_1_2003 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2003,'Area':'Production']
df_andhra_1_2003_sum = df_andhra_1_2003.sum(axis = 0, skipna = True) 
print(df_andhra_1_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_andhra_1_2004 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2004,'Area':'Production']
df_andhra_1_2004_sum = df_andhra_1_2004.sum(axis = 0, skipna = True) 
print(df_andhra_1_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_andhra_1_2005 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2005,'Area':'Production']
df_andhra_1_2005_sum = df_andhra_1_2005.sum(axis = 0, skipna = True) 
print(df_andhra_1_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_andhra_1_2006 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2006,'Area':'Production'] 
df_andhra_1_2006_sum = df_andhra_1_2006.sum(axis = 0, skipna = True)
print(df_andhra_1_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_andhra_1_2007 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2007,'Area':'Production']
df_andhra_1_2007_sum = df_andhra_1_2007.sum(axis = 0, skipna = True) 
print(df_andhra_1_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_andhra_1_2008 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2008,'Area':'Production']
df_andhra_1_2008_sum = df_andhra_1_2008.sum(axis = 0, skipna = True) 
print(df_andhra_1_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_andhra_1_2009 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2009,'Area':'Production']
df_andhra_1_2009_sum = df_andhra_1_2009.sum(axis = 0, skipna = True) 
print(df_andhra_1_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_andhra_1_2010 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2010,'Area':'Production'] 
df_andhra_1_2010_sum = df_andhra_1_2010.sum(axis = 0, skipna = True)
print(df_andhra_1_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_andhra_1_2011 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2011,'Area':'Production'] 
df_andhra_1_2011_sum = df_andhra_1_2011.sum(axis = 0, skipna = True)
print(df_andhra_1_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_andhra_1_2012 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2012,'Area':'Production']
df_andhra_1_2012_sum = df_andhra_1_2012.sum(axis = 0, skipna = True) 
print(df_andhra_1_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_andhra_1_2013 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2013,'Area':'Production'] 
df_andhra_1_2013_sum = df_andhra_1_2013.sum(axis = 0, skipna = True)
print(df_andhra_1_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_andhra_1_2014 = df_andhra_1.loc[df_andhra_1['Crop_Year'] == 2014,'Area':'Production']
df_andhra_1_2014_sum = df_andhra_1_2014.sum(axis = 0, skipna = True) 
print(df_andhra_1_2014_sum)
print("---------------------------------")


#details of Andhra( [2] CHITTOOR )

print("---- Details of Andhra( [2] CHITTOOR )--------")
df_andhra_2 = df_andhra[df_andhra.District_Name == 'CHITTOOR']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_andhra_2_1997 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 1997,'Area':'Production']
df_andhra_2_1997_sum = df_andhra_2_1997.sum(axis = 0, skipna = True)
print(df_andhra_2_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_andhra_2_1998 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 1998,'Area':'Production']
df_andhra_2_1998_sum = df_andhra_2_1998.sum(axis = 0, skipna = True) 
print(df_andhra_2_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_andhra_2_1999 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 1999,'Area':'Production']
df_andhra_2_1999_sum = df_andhra_2_1999.sum(axis = 0, skipna = True) 
print(df_andhra_2_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_andhra_2_2000 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2000,'Area':'Production']
df_andhra_2_2000_sum = df_andhra_2_2000.sum(axis = 0, skipna = True) 
print(df_andhra_2_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_andhra_2_2001 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2001,'Area':'Production'] 
df_andhra_2_2001_sum = df_andhra_2_2001.sum(axis = 0, skipna = True)
print(df_andhra_2_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_andhra_2_2002 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2002,'Area':'Production']
df_andhra_2_2002_sum = df_andhra_2_2002.sum(axis = 0, skipna = True) 
print(df_andhra_2_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_andhra_2_2003 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2003,'Area':'Production']
df_andhra_2_2003_sum = df_andhra_2_2003.sum(axis = 0, skipna = True) 
print(df_andhra_2_2003)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_andhra_2_2004 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2004,'Area':'Production']
df_andhra_2_2004_sum = df_andhra_2_2004.sum(axis = 0, skipna = True) 
print(df_andhra_2_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_andhra_2_2005 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2005,'Area':'Production']
df_andhra_2_2005_sum = df_andhra_2_2005.sum(axis = 0, skipna = True) 
print(df_andhra_2_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_andhra_2_2006 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2006,'Area':'Production'] 
df_andhra_2_2006_sum = df_andhra_2_2006.sum(axis = 0, skipna = True)
print(df_andhra_2_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_andhra_2_2007 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2007,'Area':'Production']
df_andhra_2_2007_sum = df_andhra_2_2007.sum(axis = 0, skipna = True) 
print(df_andhra_2_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_andhra_2_2008 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2008,'Area':'Production']
df_andhra_2_2008_sum = df_andhra_2_2008.sum(axis = 0, skipna = True) 
print(df_andhra_2_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_andhra_2_2009 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2009,'Area':'Production']
df_andhra_2_2009_sum = df_andhra_2_2009.sum(axis = 0, skipna = True) 
print(df_andhra_2_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_andhra_2_2010 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2010,'Area':'Production'] 
df_andhra_2_2010_sum = df_andhra_2_2010.sum(axis = 0, skipna = True)
print(df_andhra_2_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_andhra_2_2011 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2011,'Area':'Production'] 
df_andhra_2_2011_sum = df_andhra_2_2011.sum(axis = 0, skipna = True)
print(df_andhra_2_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_andhra_2_2012 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2012,'Area':'Production']
df_andhra_2_2012_sum = df_andhra_2_2012.sum(axis = 0, skipna = True) 
print(df_andhra_2_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_andhra_2_2013 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2013,'Area':'Production'] 
df_andhra_2_2013_sum = df_andhra_2_2013.sum(axis = 0, skipna = True)
print(df_andhra_2_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_andhra_2_2014 = df_andhra_2.loc[df_andhra_2['Crop_Year'] == 2014,'Area':'Production']
df_andhra_2_2014_sum = df_andhra_2_2014.sum(axis = 0, skipna = True) 
print(df_andhra_2_2014_sum)
print("---------------------------------")

#details of Andhra( [3] EAST GODAVARI )

print("------ Details of Andhra( [3] EAST GODAVARI )--------")
df_andhra_3 = df_andhra[df_andhra.District_Name == 'EAST GODAVARI']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_andhra_3_1997 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 1997,'Area':'Production']
df_andhra_3_1997_sum = df_andhra_3_1997.sum(axis = 0, skipna = True)
print(df_andhra_3_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_andhra_3_1998 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 1998,'Area':'Production']
df_andhra_3_1998_sum = df_andhra_3_1998.sum(axis = 0, skipna = True) 
print(df_andhra_3_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_andhra_3_1999 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 1999,'Area':'Production']
df_andhra_3_1999_sum = df_andhra_3_1999.sum(axis = 0, skipna = True) 
print(df_andhra_3_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_andhra_3_2000 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2000,'Area':'Production']
df_andhra_3_2000_sum = df_andhra_3_2000.sum(axis = 0, skipna = True) 
print(df_andhra_3_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_andhra_3_2001 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2001,'Area':'Production'] 
df_andhra_3_2001_sum = df_andhra_3_2001.sum(axis = 0, skipna = True)
print(df_andhra_3_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_andhra_3_2002 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2002,'Area':'Production']
df_andhra_3_2002_sum = df_andhra_3_2002.sum(axis = 0, skipna = True) 
print(df_andhra_3_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_andhra_3_2003 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2003,'Area':'Production']
df_andhra_3_2003_sum = df_andhra_3_2003.sum(axis = 0, skipna = True) 
print(df_andhra_3_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_andhra_3_2004 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2004,'Area':'Production']
df_andhra_3_2004_sum = df_andhra_3_2004.sum(axis = 0, skipna = True) 
print(df_andhra_3_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_andhra_3_2005 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2005,'Area':'Production']
df_andhra_3_2005_sum = df_andhra_3_2005.sum(axis = 0, skipna = True) 
print(df_andhra_3_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_andhra_3_2006 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2006,'Area':'Production'] 
df_andhra_3_2006_sum = df_andhra_3_2006.sum(axis = 0, skipna = True)
print(df_andhra_3_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_andhra_3_2007 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2007,'Area':'Production']
df_andhra_3_2007_sum = df_andhra_3_2007.sum(axis = 0, skipna = True) 
print(df_andhra_3_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_andhra_3_2008 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2008,'Area':'Production']
df_andhra_3_2008_sum = df_andhra_3_2008.sum(axis = 0, skipna = True) 
print(df_andhra_3_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_andhra_3_2009 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2009,'Area':'Production']
df_andhra_3_2009_sum = df_andhra_3_2009.sum(axis = 0, skipna = True) 
print(df_andhra_3_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_andhra_3_2010 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2010,'Area':'Production'] 
df_andhra_3_2010_sum = df_andhra_3_2010.sum(axis = 0, skipna = True)
print(df_andhra_3_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_andhra_3_2011 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2011,'Area':'Production'] 
df_andhra_3_2011_sum = df_andhra_3_2011.sum(axis = 0, skipna = True)
print(df_andhra_3_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_andhra_3_2012 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2012,'Area':'Production']
df_andhra_3_2012_sum = df_andhra_3_2012.sum(axis = 0, skipna = True) 
print(df_andhra_3_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_andhra_3_2013 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2013,'Area':'Production'] 
df_andhra_3_2013_sum = df_andhra_3_2013.sum(axis = 0, skipna = True)
print(df_andhra_3_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_andhra_3_2014 = df_andhra_3.loc[df_andhra_3['Crop_Year'] == 2014,'Area':'Production']
df_andhra_3_2014_sum = df_andhra_3_2014.sum(axis = 0, skipna = True) 
print(df_andhra_3_2014_sum)
print("---------------------------------")

#details of Andhra( [4] GUNTUR )

print("---- Details of Andhra( [4] GUNTUR )-------")
df_andhra_4 = df_andhra[df_andhra.District_Name == 'GUNTUR']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_andhra_4_1997 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 1997,'Area':'Production']
df_andhra_4_1997_sum = df_andhra_4_1997.sum(axis = 0, skipna = True)
print(df_andhra_4_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_andhra_4_1998 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 1998,'Area':'Production']
df_andhra_4_1998_sum = df_andhra_4_1998.sum(axis = 0, skipna = True) 
print(df_andhra_4_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_andhra_4_1999 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 1999,'Area':'Production']
df_andhra_4_1999_sum = df_andhra_4_1999.sum(axis = 0, skipna = True) 
print(df_andhra_4_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_andhra_4_2000 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2000,'Area':'Production']
df_andhra_4_2000_sum = df_andhra_4_2000.sum(axis = 0, skipna = True) 
print(df_andhra_4_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_andhra_4_2001 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2001,'Area':'Production'] 
df_andhra_4_2001_sum = df_andhra_4_2001.sum(axis = 0, skipna = True)
print(df_andhra_4_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_andhra_4_2002 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2002,'Area':'Production']
df_andhra_4_2002_sum = df_andhra_4_2002.sum(axis = 0, skipna = True) 
print(df_andhra_4_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_andhra_4_2003 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2003,'Area':'Production']
df_andhra_4_2003_sum = df_andhra_4_2003.sum(axis = 0, skipna = True) 
print(df_andhra_4_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_andhra_4_2004 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2004,'Area':'Production']
df_andhra_4_2004_sum = df_andhra_4_2004.sum(axis = 0, skipna = True) 
print(df_andhra_4_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_andhra_4_2005 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2005,'Area':'Production']
df_andhra_4_2005_sum = df_andhra_4_2005.sum(axis = 0, skipna = True) 
print(df_andhra_4_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_andhra_4_2006 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2006,'Area':'Production'] 
df_andhra_4_2006_sum = df_andhra_4_2006.sum(axis = 0, skipna = True)
print(df_andhra_4_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_andhra_4_2007 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2007,'Area':'Production']
df_andhra_4_2007_sum = df_andhra_4_2007.sum(axis = 0, skipna = True) 
print(df_andhra_4_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_andhra_4_2008 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2008,'Area':'Production']
df_andhra_4_2008_sum = df_andhra_4_2008.sum(axis = 0, skipna = True) 
print(df_andhra_4_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_andhra_4_2009 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2009,'Area':'Production']
df_andhra_4_2009_sum = df_andhra_4_2009.sum(axis = 0, skipna = True) 
print(df_andhra_4_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_andhra_4_2010 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2010,'Area':'Production'] 
df_andhra_4_2010_sum = df_andhra_4_2010.sum(axis = 0, skipna = True)
print(df_andhra_4_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_andhra_4_2011 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2011,'Area':'Production'] 
df_andhra_4_2011_sum = df_andhra_4_2011.sum(axis = 0, skipna = True)
print(df_andhra_4_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_andhra_4_2012 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2012,'Area':'Production']
df_andhra_4_2012_sum = df_andhra_4_2012.sum(axis = 0, skipna = True) 
print(df_andhra_4_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_andhra_4_2013 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2013,'Area':'Production'] 
df_andhra_4_2013_sum = df_andhra_4_2013.sum(axis = 0, skipna = True)
print(df_andhra_4_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_andhra_4_2014 = df_andhra_4.loc[df_andhra_4['Crop_Year'] == 2014,'Area':'Production']
df_andhra_4_2014_sum = df_andhra_4_2014.sum(axis = 0, skipna = True) 
print(df_andhra_4_2014_sum)
print("---------------------------------")

#details of Andhra( [5] KADAPA )

print("----- Details of Andhra( [5] KADAPA )-------")
df_andhra_5 = df_andhra[df_andhra.District_Name == 'KADAPA']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_andhra_5_1997 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 1997,'Area':'Production']
df_andhra_5_1997_sum = df_andhra_5_1997.sum(axis = 0, skipna = True)
print(df_andhra_5_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_andhra_5_1998 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 1998,'Area':'Production']
df_andhra_5_1998_sum = df_andhra_5_1998.sum(axis = 0, skipna = True) 
print(df_andhra_5_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_andhra_5_1999 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 1999,'Area':'Production']
df_andhra_5_1999_sum = df_andhra_5_1999.sum(axis = 0, skipna = True) 
print(df_andhra_5_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_andhra_5_2000 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2000,'Area':'Production']
df_andhra_5_2000_sum = df_andhra_5_2000.sum(axis = 0, skipna = True) 
print(df_andhra_5_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_andhra_5_2001 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2001,'Area':'Production'] 
df_andhra_5_2001_sum = df_andhra_5_2001.sum(axis = 0, skipna = True)
print(df_andhra_5_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_andhra_5_2002 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2002,'Area':'Production']
df_andhra_5_2002_sum = df_andhra_5_2002.sum(axis = 0, skipna = True) 
print(df_andhra_5_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_andhra_5_2003 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2003,'Area':'Production']
df_andhra_5_2003_sum = df_andhra_5_2003.sum(axis = 0, skipna = True) 
print(df_andhra_5_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_andhra_5_2004 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2004,'Area':'Production']
df_andhra_5_2004_sum = df_andhra_5_2004.sum(axis = 0, skipna = True) 
print(df_andhra_5_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_andhra_5_2005 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2005,'Area':'Production']
df_andhra_5_2005_sum = df_andhra_5_2005.sum(axis = 0, skipna = True) 
print(df_andhra_5_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_andhra_5_2006 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2006,'Area':'Production'] 
df_andhra_5_2006_sum = df_andhra_5_2006.sum(axis = 0, skipna = True)
print(df_andhra_5_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_andhra_5_2007 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2007,'Area':'Production']
df_andhra_5_2007_sum = df_andhra_5_2007.sum(axis = 0, skipna = True) 
print(df_andhra_5_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_andhra_5_2008 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2008,'Area':'Production']
df_andhra_5_2008_sum = df_andhra_5_2008.sum(axis = 0, skipna = True) 
print(df_andhra_5_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_andhra_5_2009 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2009,'Area':'Production']
df_andhra_5_2009_sum = df_andhra_5_2009.sum(axis = 0, skipna = True) 
print(df_andhra_5_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_andhra_5_2010 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2010,'Area':'Production'] 
df_andhra_5_2010_sum = df_andhra_5_2010.sum(axis = 0, skipna = True)
print(df_andhra_5_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_andhra_5_2011 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2011,'Area':'Production'] 
df_andhra_5_2011_sum = df_andhra_5_2011.sum(axis = 0, skipna = True)
print(df_andhra_5_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_andhra_5_2012 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2012,'Area':'Production']
df_andhra_5_2012_sum = df_andhra_5_2012.sum(axis = 0, skipna = True) 
print(df_andhra_5_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_andhra_5_2013 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2013,'Area':'Production'] 
df_andhra_5_2013_sum = df_andhra_5_2013.sum(axis = 0, skipna = True)
print(df_andhra_5_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_andhra_5_2014 = df_andhra_5.loc[df_andhra_5['Crop_Year'] == 2014,'Area':'Production']
df_andhra_5_2014_sum = df_andhra_5_2014.sum(axis = 0, skipna = True) 
print(df_andhra_5_2014_sum)
print("---------------------------------")

#details of Andhra( [6] KRISHNA )

print("------ Details of Andhra( [6] KRISHNA )-------")
df_andhra_6 = df_andhra[df_andhra.District_Name == 'KRISHNA']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_andhra_6_1997 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 1997,'Area':'Production']
df_andhra_6_1997_sum = df_andhra_6_1997.sum(axis = 0, skipna = True)
print(df_andhra_6_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_andhra_6_1998 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 1998,'Area':'Production']
df_andhra_6_1998_sum = df_andhra_6_1998.sum(axis = 0, skipna = True) 
print(df_andhra_6_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_andhra_6_1999 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 1999,'Area':'Production']
df_andhra_6_1999_sum = df_andhra_6_1999.sum(axis = 0, skipna = True) 
print(df_andhra_6_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_andhra_6_2000 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2000,'Area':'Production']
df_andhra_6_2000_sum = df_andhra_6_2000.sum(axis = 0, skipna = True) 
print(df_andhra_6_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_andhra_6_2001 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2001,'Area':'Production'] 
df_andhra_6_2001_sum = df_andhra_6_2001.sum(axis = 0, skipna = True)
print(df_andhra_6_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_andhra_6_2002 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2002,'Area':'Production']
df_andhra_6_2002_sum = df_andhra_6_2002.sum(axis = 0, skipna = True) 
print(df_andhra_6_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_andhra_6_2003 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2003,'Area':'Production']
df_andhra_6_2003_sum = df_andhra_6_2003.sum(axis = 0, skipna = True) 
print(df_andhra_6_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_andhra_6_2004 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2004,'Area':'Production']
df_andhra_6_2004_sum = df_andhra_6_2004.sum(axis = 0, skipna = True) 
print(df_andhra_6_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_andhra_6_2005 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2005,'Area':'Production']
df_andhra_6_2005_sum = df_andhra_6_2005.sum(axis = 0, skipna = True) 
print(df_andhra_6_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_andhra_6_2006 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2006,'Area':'Production'] 
df_andhra_6_2006_sum = df_andhra_6_2006.sum(axis = 0, skipna = True)
print(df_andhra_6_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_andhra_6_2007 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2007,'Area':'Production']
df_andhra_6_2007_sum = df_andhra_6_2007.sum(axis = 0, skipna = True) 
print(df_andhra_6_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_andhra_6_2008 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2008,'Area':'Production']
df_andhra_6_2008_sum = df_andhra_6_2008.sum(axis = 0, skipna = True) 
print(df_andhra_6_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_andhra_6_2009 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2009,'Area':'Production']
df_andhra_6_2009_sum = df_andhra_6_2009.sum(axis = 0, skipna = True) 
print(df_andhra_6_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_andhra_6_2010 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2010,'Area':'Production'] 
df_andhra_6_2010_sum = df_andhra_6_2010.sum(axis = 0, skipna = True)
print(df_andhra_6_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_andhra_6_2011 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2011,'Area':'Production'] 
df_andhra_6_2011_sum = df_andhra_6_2011.sum(axis = 0, skipna = True)
print(df_andhra_6_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_andhra_6_2012 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2012,'Area':'Production']
df_andhra_6_2012_sum = df_andhra_6_2012.sum(axis = 0, skipna = True) 
print(df_andhra_6_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_andhra_6_2013 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2013,'Area':'Production'] 
df_andhra_6_2013_sum = df_andhra_6_2013.sum(axis = 0, skipna = True)
print(df_andhra_6_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_andhra_6_2014 = df_andhra_6.loc[df_andhra_6['Crop_Year'] == 2014,'Area':'Production']
df_andhra_6_2014_sum = df_andhra_6_2014.sum(axis = 0, skipna = True) 
print(df_andhra_6_2014_sum)
print("---------------------------------")

#details of Andhra( [7] KURNOOL)

print("----- Details of Andhra( [7] KURNOOL)------")
df_andhra_7 = df_andhra[df_andhra.District_Name == 'KURNOOL']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_andhra_7_1997 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 1997,'Area':'Production']
df_andhra_7_1997_sum = df_andhra_7_1997.sum(axis = 0, skipna = True)
print(df_andhra_7_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_andhra_7_1998 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 1998,'Area':'Production']
df_andhra_7_1998_sum = df_andhra_7_1998.sum(axis = 0, skipna = True) 
print(df_andhra_7_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_andhra_7_1999 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 1999,'Area':'Production']
df_andhra_7_1999_sum = df_andhra_7_1999.sum(axis = 0, skipna = True) 
print(df_andhra_7_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_andhra_7_2000 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2000,'Area':'Production']
df_andhra_7_2000_sum = df_andhra_7_2000.sum(axis = 0, skipna = True) 
print(df_andhra_7_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_andhra_7_2001 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2001,'Area':'Production'] 
df_andhra_7_2001_sum = df_andhra_7_2001.sum(axis = 0, skipna = True)
print(df_andhra_7_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_andhra_7_2002 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2002,'Area':'Production']
df_andhra_7_2002_sum = df_andhra_7_2002.sum(axis = 0, skipna = True) 
print(df_andhra_7_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_andhra_7_2003 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2003,'Area':'Production']
df_andhra_7_2003_sum = df_andhra_7_2003.sum(axis = 0, skipna = True) 
print(df_andhra_7_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_andhra_7_2004 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2004,'Area':'Production']
df_andhra_7_2004_sum = df_andhra_7_2004.sum(axis = 0, skipna = True) 
print(df_andhra_7_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_andhra_7_2005 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2005,'Area':'Production']
df_andhra_7_2005_sum = df_andhra_7_2005.sum(axis = 0, skipna = True) 
print(df_andhra_7_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_andhra_7_2006 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2006,'Area':'Production'] 
df_andhra_7_2006_sum = df_andhra_7_2006.sum(axis = 0, skipna = True)
print(df_andhra_7_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_andhra_7_2007 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2007,'Area':'Production']
df_andhra_7_2007_sum = df_andhra_7_2007.sum(axis = 0, skipna = True) 
print(df_andhra_7_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_andhra_7_2008 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2008,'Area':'Production']
df_andhra_7_2008_sum = df_andhra_7_2008.sum(axis = 0, skipna = True) 
print(df_andhra_7_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_andhra_7_2009 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2009,'Area':'Production']
df_andhra_7_2009_sum = df_andhra_7_2009.sum(axis = 0, skipna = True) 
print(df_andhra_7_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_andhra_7_2010 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2010,'Area':'Production'] 
df_andhra_7_2010_sum = df_andhra_7_2010.sum(axis = 0, skipna = True)
print(df_andhra_7_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_andhra_7_2011 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2011,'Area':'Production'] 
df_andhra_7_2011_sum = df_andhra_7_2011.sum(axis = 0, skipna = True)
print(df_andhra_7_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_andhra_7_2012 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2012,'Area':'Production']
df_andhra_7_2012_sum = df_andhra_7_2012.sum(axis = 0, skipna = True) 
print(df_andhra_7_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_andhra_7_2013 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2013,'Area':'Production'] 
df_andhra_7_2013_sum = df_andhra_7_2013.sum(axis = 0, skipna = True)
print(df_andhra_7_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_andhra_7_2014 = df_andhra_7.loc[df_andhra_7['Crop_Year'] == 2014,'Area':'Production']
df_andhra_7_2014_sum = df_andhra_7_2014.sum(axis = 0, skipna = True) 
print(df_andhra_7_2014_sum)
print("---------------------------------")

#details of Andhra( [8] PRAKASAM )

print("---- Details of Andhra( [8] PRAKASAM )--------")
df_andhra_8 = df_andhra[df_andhra.District_Name == 'PRAKASAM']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_andhra_8_1997 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 1997,'Area':'Production']
df_andhra_8_1997_sum = df_andhra_8_1997.sum(axis = 0, skipna = True)
print(df_andhra_8_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_andhra_8_1998 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 1998,'Area':'Production']
df_andhra_8_1998_sum = df_andhra_8_1998.sum(axis = 0, skipna = True) 
print(df_andhra_8_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_andhra_8_1999 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 1999,'Area':'Production']
df_andhra_8_1999_sum = df_andhra_8_1999.sum(axis = 0, skipna = True) 
print(df_andhra_8_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_andhra_8_2000 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2000,'Area':'Production']
df_andhra_8_2000_sum = df_andhra_8_2000.sum(axis = 0, skipna = True) 
print(df_andhra_8_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_andhra_8_2001 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2001,'Area':'Production'] 
df_andhra_8_2001_sum = df_andhra_8_2001.sum(axis = 0, skipna = True)
print(df_andhra_8_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_andhra_8_2002 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2002,'Area':'Production']
df_andhra_8_2002_sum = df_andhra_8_2002.sum(axis = 0, skipna = True) 
print(df_andhra_8_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_andhra_8_2003 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2003,'Area':'Production']
df_andhra_8_2003_sum = df_andhra_8_2003.sum(axis = 0, skipna = True) 
print(df_andhra_8_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_andhra_8_2004 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2004,'Area':'Production']
df_andhra_8_2004_sum = df_andhra_8_2004.sum(axis = 0, skipna = True) 
print(df_andhra_8_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_andhra_8_2005 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2005,'Area':'Production']
df_andhra_8_2005_sum = df_andhra_8_2005.sum(axis = 0, skipna = True) 
print(df_andhra_8_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_andhra_8_2006 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2006,'Area':'Production'] 
df_andhra_8_2006_sum = df_andhra_8_2006.sum(axis = 0, skipna = True)
print(df_andhra_8_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_andhra_8_2007 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2007,'Area':'Production']
df_andhra_8_2007_sum = df_andhra_8_2007.sum(axis = 0, skipna = True) 
print(df_andhra_8_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_andhra_8_2008 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2008,'Area':'Production']
df_andhra_8_2008_sum = df_andhra_8_2008.sum(axis = 0, skipna = True) 
print(df_andhra_8_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_andhra_8_2009 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2009,'Area':'Production']
df_andhra_8_2009_sum = df_andhra_8_2009.sum(axis = 0, skipna = True) 
print(df_andhra_8_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_andhra_8_2010 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2010,'Area':'Production'] 
df_andhra_8_2010_sum = df_andhra_8_2010.sum(axis = 0, skipna = True)
print(df_andhra_8_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_andhra_8_2011 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2011,'Area':'Production'] 
df_andhra_8_2011_sum = df_andhra_8_2011.sum(axis = 0, skipna = True)
print(df_andhra_8_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_andhra_8_2012 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2012,'Area':'Production']
df_andhra_8_2012_sum = df_andhra_8_2012.sum(axis = 0, skipna = True) 
print(df_andhra_8_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_andhra_8_2013 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2013,'Area':'Production'] 
df_andhra_8_2013_sum = df_andhra_8_2013.sum(axis = 0, skipna = True)
print(df_andhra_8_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_andhra_8_2014 = df_andhra_8.loc[df_andhra_8['Crop_Year'] == 2014,'Area':'Production']
df_andhra_8_2014_sum = df_andhra_8_2014.sum(axis = 0, skipna = True) 
print(df_andhra_8_2014_sum)
print("---------------------------------")

#details of Andhra( [9] SPSR NELLORE)

print("----- Details of Andhra( [9] SPSR NELLORE)--------")
df_andhra_9 = df_andhra[df_andhra.District_Name == 'SPSR NELLORE']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_andhra_9_1997 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 1997,'Area':'Production']
df_andhra_9_1997_sum = df_andhra_9_1997.sum(axis = 0, skipna = True)
print(df_andhra_9_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_andhra_9_1998 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 1998,'Area':'Production']
df_andhra_9_1998_sum = df_andhra_9_1998.sum(axis = 0, skipna = True) 
print(df_andhra_9_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_andhra_9_1999 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 1999,'Area':'Production']
df_andhra_9_1999_sum = df_andhra_9_1999.sum(axis = 0, skipna = True) 
print(df_andhra_9_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_andhra_9_2000 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2000,'Area':'Production']
df_andhra_9_2000_sum = df_andhra_9_2000.sum(axis = 0, skipna = True) 
print(df_andhra_9_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_andhra_9_2001 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2001,'Area':'Production'] 
df_andhra_9_2001_sum = df_andhra_9_2001.sum(axis = 0, skipna = True)
print(df_andhra_9_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_andhra_9_2002 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2002,'Area':'Production']
df_andhra_9_2002_sum = df_andhra_9_2002.sum(axis = 0, skipna = True) 
print(df_andhra_9_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_andhra_9_2003 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2003,'Area':'Production']
df_andhra_9_2003_sum = df_andhra_9_2003.sum(axis = 0, skipna = True) 
print(df_andhra_9_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_andhra_9_2004 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2004,'Area':'Production']
df_andhra_9_2004_sum = df_andhra_9_2004.sum(axis = 0, skipna = True) 
print(df_andhra_9_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_andhra_9_2005 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2005,'Area':'Production']
df_andhra_9_2005_sum = df_andhra_9_2005.sum(axis = 0, skipna = True) 
print(df_andhra_9_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_andhra_9_2006 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2006,'Area':'Production'] 
df_andhra_9_2006_sum = df_andhra_9_2006.sum(axis = 0, skipna = True)
print(df_andhra_9_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_andhra_9_2007 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2007,'Area':'Production']
df_andhra_9_2007_sum = df_andhra_9_2007.sum(axis = 0, skipna = True) 
print(df_andhra_9_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_andhra_9_2008 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2008,'Area':'Production']
df_andhra_9_2008_sum = df_andhra_9_2008.sum(axis = 0, skipna = True) 
print(df_andhra_9_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_andhra_9_2009 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2009,'Area':'Production']
df_andhra_9_2009_sum = df_andhra_9_2009.sum(axis = 0, skipna = True) 
print(df_andhra_9_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_andhra_9_2010 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2010,'Area':'Production'] 
df_andhra_9_2010_sum = df_andhra_9_2010.sum(axis = 0, skipna = True)
print(df_andhra_9_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_andhra_9_2011 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2011,'Area':'Production'] 
df_andhra_9_2011_sum = df_andhra_9_2011.sum(axis = 0, skipna = True)
print(df_andhra_9_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_andhra_9_2012 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2012,'Area':'Production']
df_andhra_9_2012_sum = df_andhra_9_2012.sum(axis = 0, skipna = True) 
print(df_andhra_9_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_andhra_9_2013 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2013,'Area':'Production'] 
df_andhra_9_2013_sum = df_andhra_9_2013.sum(axis = 0, skipna = True)
print(df_andhra_9_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_andhra_9_2014 = df_andhra_9.loc[df_andhra_9['Crop_Year'] == 2014,'Area':'Production']
df_andhra_9_2014_sum = df_andhra_9_2014.sum(axis = 0, skipna = True) 
print(df_andhra_9_2014_sum)
print("---------------------------------")

#details of Andhra( [10] SRIKAKULAM )

print("---- Details of Andhra( [10] SRIKAKULAM )---------")
df_andhra_10 = df_andhra[df_andhra.District_Name == 'SRIKAKULAM']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_andhra_10_1997 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 1997,'Area':'Production']
df_andhra_10_1997_sum = df_andhra_10_1997.sum(axis = 0, skipna = True)
print(df_andhra_10_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_andhra_10_1998 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 1998,'Area':'Production']
df_andhra_10_1998_sum = df_andhra_10_1998.sum(axis = 0, skipna = True) 
print(df_andhra_10_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_andhra_10_1999 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 1999,'Area':'Production']
df_andhra_10_1999_sum = df_andhra_10_1999.sum(axis = 0, skipna = True) 
print(df_andhra_10_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_andhra_10_2000 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2000,'Area':'Production']
df_andhra_10_2000_sum = df_andhra_10_2000.sum(axis = 0, skipna = True) 
print(df_andhra_10_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_andhra_10_2001 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2001,'Area':'Production'] 
df_andhra_10_2001_sum = df_andhra_10_2001.sum(axis = 0, skipna = True)
print(df_andhra_10_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_andhra_10_2002 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2002,'Area':'Production']
df_andhra_10_2002_sum = df_andhra_10_2002.sum(axis = 0, skipna = True) 
print(df_andhra_10_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_andhra_10_2003 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2003,'Area':'Production']
df_andhra_10_2003_sum = df_andhra_10_2003.sum(axis = 0, skipna = True) 
print(df_andhra_10_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_andhra_10_2004 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2004,'Area':'Production']
df_andhra_10_2004_sum = df_andhra_10_2004.sum(axis = 0, skipna = True) 
print(df_andhra_10_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_andhra_10_2005 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2005,'Area':'Production']
df_andhra_10_2005_sum = df_andhra_10_2005.sum(axis = 0, skipna = True) 
print(df_andhra_10_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_andhra_10_2006 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2006,'Area':'Production'] 
df_andhra_10_2006_sum = df_andhra_10_2006.sum(axis = 0, skipna = True)
print(df_andhra_10_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_andhra_10_2007 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2007,'Area':'Production']
df_andhra_10_2007_sum = df_andhra_10_2007.sum(axis = 0, skipna = True) 
print(df_andhra_10_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_andhra_10_2008 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2008,'Area':'Production']
df_andhra_10_2008_sum = df_andhra_10_2008.sum(axis = 0, skipna = True) 
print(df_andhra_10_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_andhra_10_2009 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2009,'Area':'Production']
df_andhra_10_2009_sum = df_andhra_10_2009.sum(axis = 0, skipna = True) 
print(df_andhra_10_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_andhra_10_2010 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2010,'Area':'Production'] 
df_andhra_10_2010_sum = df_andhra_10_2010.sum(axis = 0, skipna = True)
print(df_andhra_10_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_andhra_10_2011 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2011,'Area':'Production'] 
df_andhra_10_2011_sum = df_andhra_10_2011.sum(axis = 0, skipna = True)
print(df_andhra_10_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_andhra_10_2012 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2012,'Area':'Production']
df_andhra_10_2012_sum = df_andhra_10_2012.sum(axis = 0, skipna = True) 
print(df_andhra_10_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_andhra_10_2013 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2013,'Area':'Production'] 
df_andhra_10_2013_sum = df_andhra_10_2013.sum(axis = 0, skipna = True)
print(df_andhra_10_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_andhra_10_2014 = df_andhra_10.loc[df_andhra_10['Crop_Year'] == 2014,'Area':'Production']
df_andhra_10_2014_sum = df_andhra_10_2014.sum(axis = 0, skipna = True) 
print(df_andhra_10_2014_sum)
print("---------------------------------")

#details of Andhra( [11] VISAKHAPATANAM )

print("----Details of Andhra( [11] VISAKHAPATANAM )----")
df_andhra_11 = df_andhra[df_andhra.District_Name == 'VISAKHAPATANAM']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_andhra_11_1997 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 1997,'Area':'Production']
df_andhra_11_1997_sum = df_andhra_11_1997.sum(axis = 0, skipna = True)
print(df_andhra_11_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_andhra_11_1998 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 1998,'Area':'Production']
df_andhra_11_1998_sum = df_andhra_11_1998.sum(axis = 0, skipna = True) 
print(df_andhra_11_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_andhra_11_1999 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 1999,'Area':'Production']
df_andhra_11_1999_sum = df_andhra_11_1999.sum(axis = 0, skipna = True) 
print(df_andhra_11_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_andhra_11_2000 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2000,'Area':'Production']
df_andhra_11_2000_sum = df_andhra_11_2000.sum(axis = 0, skipna = True) 
print(df_andhra_11_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_andhra_11_2001 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2001,'Area':'Production'] 
df_andhra_11_2001_sum = df_andhra_11_2001.sum(axis = 0, skipna = True)
print(df_andhra_11_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_andhra_11_2002 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2002,'Area':'Production']
df_andhra_11_2002_sum = df_andhra_11_2002.sum(axis = 0, skipna = True) 
print(df_andhra_11_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_andhra_11_2003 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2003,'Area':'Production']
df_andhra_11_2003_sum = df_andhra_11_2003.sum(axis = 0, skipna = True) 
print(df_andhra_11_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_andhra_11_2004 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2004,'Area':'Production']
df_andhra_11_2004_sum = df_andhra_11_2004.sum(axis = 0, skipna = True) 
print(df_andhra_11_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_andhra_11_2005 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2005,'Area':'Production']
df_andhra_11_2005_sum = df_andhra_11_2005.sum(axis = 0, skipna = True) 
print(df_andhra_11_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_andhra_11_2006 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2006,'Area':'Production'] 
df_andhra_11_2006_sum = df_andhra_11_2006.sum(axis = 0, skipna = True)
print(df_andhra_11_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_andhra_11_2007 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2007,'Area':'Production']
df_andhra_11_2007_sum = df_andhra_11_2007.sum(axis = 0, skipna = True) 
print(df_andhra_11_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_andhra_11_2008 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2008,'Area':'Production']
df_andhra_11_2008_sum = df_andhra_11_2008.sum(axis = 0, skipna = True) 
print(df_andhra_11_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_andhra_11_2009 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2009,'Area':'Production']
df_andhra_11_2009_sum = df_andhra_11_2009.sum(axis = 0, skipna = True) 
print(df_andhra_11_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_andhra_11_2010 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2010,'Area':'Production'] 
df_andhra_11_2010_sum = df_andhra_11_2010.sum(axis = 0, skipna = True)
print(df_andhra_11_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_andhra_11_2011 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2011,'Area':'Production'] 
df_andhra_11_2011_sum = df_andhra_11_2011.sum(axis = 0, skipna = True)
print(df_andhra_11_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_andhra_11_2012 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2012,'Area':'Production']
df_andhra_11_2012_sum = df_andhra_11_2012.sum(axis = 0, skipna = True) 
print(df_andhra_11_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_andhra_11_2013 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2013,'Area':'Production'] 
df_andhra_11_2013_sum = df_andhra_11_2013.sum(axis = 0, skipna = True)
print(df_andhra_11_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_andhra_11_2014 = df_andhra_11.loc[df_andhra_11['Crop_Year'] == 2014,'Area':'Production']
df_andhra_11_2014_sum = df_andhra_11_2014.sum(axis = 0, skipna = True) 
print(df_andhra_11_2014_sum)
print("---------------------------------")

#details of Andhra( [12] VIZIANAGARAM )

print("---- Details of Andhra( [12] VIZIANAGARAM )------")
df_andhra_12 = df_andhra[df_andhra.District_Name == 'VIZIANAGARAM']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_andhra_12_1997 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 1997,'Area':'Production']
df_andhra_12_1997_sum = df_andhra_12_1997.sum(axis = 0, skipna = True)
print(df_andhra_12_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_andhra_12_1998 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 1998,'Area':'Production']
df_andhra_12_1998_sum = df_andhra_12_1998.sum(axis = 0, skipna = True) 
print(df_andhra_12_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_andhra_12_1999 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 1999,'Area':'Production']
df_andhra_12_1999_sum = df_andhra_12_1999.sum(axis = 0, skipna = True) 
print(df_andhra_12_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_andhra_12_2000 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2000,'Area':'Production']
df_andhra_12_2000_sum = df_andhra_12_2000.sum(axis = 0, skipna = True) 
print(df_andhra_12_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_andhra_12_2001 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2001,'Area':'Production'] 
df_andhra_12_2001_sum = df_andhra_12_2001.sum(axis = 0, skipna = True)
print(df_andhra_12_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_andhra_12_2002 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2002,'Area':'Production']
df_andhra_12_2002_sum = df_andhra_12_2002.sum(axis = 0, skipna = True) 
print(df_andhra_12_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_andhra_12_2003 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2003,'Area':'Production']
df_andhra_12_2003_sum = df_andhra_12_2003.sum(axis = 0, skipna = True) 
print(df_andhra_12_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_andhra_12_2004 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2004,'Area':'Production']
df_andhra_12_2004_sum = df_andhra_12_2004.sum(axis = 0, skipna = True) 
print(df_andhra_12_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_andhra_12_2005 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2005,'Area':'Production']
df_andhra_12_2005_sum = df_andhra_12_2005.sum(axis = 0, skipna = True) 
print(df_andhra_12_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_andhra_12_2006 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2006,'Area':'Production'] 
df_andhra_12_2006_sum = df_andhra_12_2006.sum(axis = 0, skipna = True)
print(df_andhra_12_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_andhra_12_2007 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2007,'Area':'Production']
df_andhra_12_2007_sum = df_andhra_12_2007.sum(axis = 0, skipna = True) 
print(df_andhra_12_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_andhra_12_2008 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2008,'Area':'Production']
df_andhra_12_2008_sum = df_andhra_12_2008.sum(axis = 0, skipna = True) 
print(df_andhra_12_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_andhra_12_2009 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2009,'Area':'Production']
df_andhra_12_2009_sum = df_andhra_12_2009.sum(axis = 0, skipna = True) 
print(df_andhra_12_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_andhra_12_2010 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2010,'Area':'Production'] 
df_andhra_12_2010_sum = df_andhra_12_2010.sum(axis = 0, skipna = True)
print(df_andhra_12_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_andhra_12_2011 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2011,'Area':'Production'] 
df_andhra_12_2011_sum = df_andhra_12_2011.sum(axis = 0, skipna = True)
print(df_andhra_12_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_andhra_12_2012 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2012,'Area':'Production']
df_andhra_12_2012_sum = df_andhra_12_2012.sum(axis = 0, skipna = True) 
print(df_andhra_12_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_andhra_12_2013 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2013,'Area':'Production'] 
df_andhra_12_2013_sum = df_andhra_12_2013.sum(axis = 0, skipna = True)
print(df_andhra_12_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_andhra_12_2014 = df_andhra_12.loc[df_andhra_12['Crop_Year'] == 2014,'Area':'Production']
df_andhra_12_2014_sum = df_andhra_12_2014.sum(axis = 0, skipna = True) 
print(df_andhra_12_2014_sum)
print("---------------------------------")

#details of Andhra( [13] WEST GODAVARI )

print("----- Details of Andhra( [13] WEST GODAVARI )------")
df_andhra_13 = df_andhra[df_andhra.District_Name == 'WEST GODAVARI']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_andhra_13_1997 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 1997,'Area':'Production']
df_andhra_13_1997_sum = df_andhra_13_1997.sum(axis = 0, skipna = True)
print(df_andhra_13_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_andhra_13_1998 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 1998,'Area':'Production']
df_andhra_13_1998_sum = df_andhra_13_1998.sum(axis = 0, skipna = True) 
print(df_andhra_13_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_andhra_13_1999 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 1999,'Area':'Production']
df_andhra_13_1999_sum = df_andhra_13_1999.sum(axis = 0, skipna = True) 
print(df_andhra_13_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_andhra_13_2000 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2000,'Area':'Production']
df_andhra_13_2000_sum = df_andhra_13_2000.sum(axis = 0, skipna = True) 
print(df_andhra_13_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_andhra_13_2001 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2001,'Area':'Production'] 
df_andhra_13_2001_sum = df_andhra_13_2001.sum(axis = 0, skipna = True)
print(df_andhra_13_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_andhra_13_2002 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2002,'Area':'Production']
df_andhra_13_2002_sum = df_andhra_13_2002.sum(axis = 0, skipna = True) 
print(df_andhra_13_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_andhra_13_2003 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2003,'Area':'Production']
df_andhra_13_2003_sum = df_andhra_13_2003.sum(axis = 0, skipna = True) 
print(df_andhra_13_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_andhra_13_2004 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2004,'Area':'Production']
df_andhra_13_2004_sum = df_andhra_13_2004.sum(axis = 0, skipna = True) 
print(df_andhra_13_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_andhra_13_2005 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2005,'Area':'Production']
df_andhra_13_2005_sum = df_andhra_13_2005.sum(axis = 0, skipna = True) 
print(df_andhra_13_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_andhra_13_2006 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2006,'Area':'Production'] 
df_andhra_13_2006_sum = df_andhra_13_2006.sum(axis = 0, skipna = True)
print(df_andhra_13_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_andhra_13_2007 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2007,'Area':'Production']
df_andhra_13_2007_sum = df_andhra_13_2007.sum(axis = 0, skipna = True) 
print(df_andhra_13_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_andhra_13_2008 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2008,'Area':'Production']
df_andhra_13_2008_sum = df_andhra_13_2008.sum(axis = 0, skipna = True) 
print(df_andhra_13_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_andhra_13_2009 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2009,'Area':'Production']
df_andhra_13_2009_sum = df_andhra_13_2009.sum(axis = 0, skipna = True) 
print(df_andhra_13_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_andhra_13_2010 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2010,'Area':'Production'] 
df_andhra_13_2010_sum = df_andhra_13_2010.sum(axis = 0, skipna = True)
print(df_andhra_13_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_andhra_13_2011 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2011,'Area':'Production'] 
df_andhra_13_2011_sum = df_andhra_13_2011.sum(axis = 0, skipna = True)
print(df_andhra_13_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_andhra_13_2012 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2012,'Area':'Production']
df_andhra_13_2012_sum = df_andhra_13_2012.sum(axis = 0, skipna = True) 
print(df_andhra_13_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_andhra_13_2013 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2013,'Area':'Production'] 
df_andhra_13_2013_sum = df_andhra_13_2013.sum(axis = 0, skipna = True)
print(df_andhra_13_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_andhra_13_2014 = df_andhra_13.loc[df_andhra_13['Crop_Year'] == 2014,'Area':'Production']
df_andhra_13_2014_sum = df_andhra_13_2014.sum(axis = 0, skipna = True) 
print(df_andhra_13_2014_sum)
print("---------------------------------")


#Question-(3) Arunachal Pradesh

print("---- State-3 : Arunachal Pradesh -----")
df_arunachal = df[df.State_Name == 'Arunachal Pradesh']
df_arunachal_dist = df_arunachal.groupby(['District_Name'])[['Crop_Year']].count()
print(df_arunachal_dist)

# crop year in Arunachal Pradesh

print("--- Crop year in Arunachal Pradesh ----")
df_arunachal_year = df_arunachal.groupby(['Crop_Year'])[['Crop_Year']].count()
print(df_arunachal_year)

# crop types in Arunachal Pradesh

print("--- Crop types in Arunachal Pradesh -----")
df_arunachal_crop = df_arunachal.groupby(['Crop'])[['Crop']].count()
print(df_arunachal_crop)

# details of arunachal : [1] ANJAW 

print("---- Details of arunachal : [1] ANJAW ------")
df_arunachal_1 = df_arunachal[df_arunachal.District_Name == 'ANJAW']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_1_1997     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_1_1997_sum = df_arunachal_1_1997.sum(axis = 0, skipna = True)
print(df_arunachal_1_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_1_1998     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_1_1998_sum = df_arunachal_1_1998.sum(axis = 0, skipna = True)
print(df_arunachal_1_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_1_1999     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_1_1999_sum = df_arunachal_1_1999.sum(axis = 0, skipna = True)
print(df_arunachal_1_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_1_2000     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_1_2000_sum = df_arunachal_1_2000.sum(axis = 0, skipna = True)
print(df_arunachal_1_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_1_2001     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_1_2001_sum = df_arunachal_1_2001.sum(axis = 0, skipna = True)
print(df_arunachal_1_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_1_2002     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_1_2002_sum = df_arunachal_1_2002.sum(axis = 0, skipna = True)
print(df_arunachal_1_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_1_2003     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_1_2003_sum = df_arunachal_1_2003.sum(axis = 0, skipna = True)
print(df_arunachal_1_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_1_2004     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_1_2004_sum = df_arunachal_1_2004.sum(axis = 0, skipna = True)
print(df_arunachal_1_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_1_2005     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_1_2005_sum = df_arunachal_1_2005.sum(axis = 0, skipna = True)
print(df_arunachal_1_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_1_2006     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_1_2006_sum = df_arunachal_1_2006.sum(axis = 0, skipna = True)
print(df_arunachal_1_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_1_2007     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_1_2007_sum = df_arunachal_1_2007.sum(axis = 0, skipna = True)
print(df_arunachal_1_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_1_2008     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_1_2008_sum = df_arunachal_1_2008.sum(axis = 0, skipna = True)
print(df_arunachal_1_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_1_2009     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_1_2009_sum = df_arunachal_1_2009.sum(axis = 0, skipna = True)
print(df_arunachal_1_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_1_2010     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_1_2010_sum = df_arunachal_1_2010.sum(axis = 0, skipna = True)
print(df_arunachal_1_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_1_2011     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_1_2011_sum = df_arunachal_1_2011.sum(axis = 0, skipna = True)
print(df_arunachal_1_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_1_2012     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_1_2012_sum = df_arunachal_1_2012.sum(axis = 0, skipna = True)
print(df_arunachal_1_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_1_2013     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_1_2013_sum = df_arunachal_1_2013.sum(axis = 0, skipna = True)
print(df_arunachal_1_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_1_2014     = df_arunachal_1.loc[df_arunachal_1['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_1_2014_sum = df_arunachal_1_2014.sum(axis = 0, skipna = True)
print(df_arunachal_1_2014_sum)
print("---------------------------------")
        
# details of arunachal : [2] CHANGLANG  

print("--- Details of arunachal : [2] CHANGLANG ------")
df_arunachal_2 = df_arunachal[df_arunachal.District_Name == 'CHANGLANG']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_2_1997     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_2_1997_sum = df_arunachal_2_1997.sum(axis = 0, skipna = True)
print(df_arunachal_2_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_2_1998     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_2_1998_sum = df_arunachal_2_1998.sum(axis = 0, skipna = True)
print(df_arunachal_2_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_2_1999     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_2_1999_sum = df_arunachal_2_1999.sum(axis = 0, skipna = True)
print(df_arunachal_2_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_2_2000     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_2_2000_sum = df_arunachal_2_2000.sum(axis = 0, skipna = True)
print(df_arunachal_2_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_2_2001     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_2_2001_sum = df_arunachal_2_2001.sum(axis = 0, skipna = True)
print(df_arunachal_2_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_2_2002     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_2_2002_sum = df_arunachal_2_2002.sum(axis = 0, skipna = True)
print(df_arunachal_2_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_2_2003     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_2_2003_sum = df_arunachal_2_2003.sum(axis = 0, skipna = True)
print(df_arunachal_2_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_2_2004     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_2_2004_sum = df_arunachal_2_2004.sum(axis = 0, skipna = True)
print(df_arunachal_2_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_2_2005     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_2_2005_sum = df_arunachal_2_2005.sum(axis = 0, skipna = True)
print(df_arunachal_2_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_2_2006     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_2_2006_sum = df_arunachal_2_2006.sum(axis = 0, skipna = True)
print(df_arunachal_2_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_2_2007     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_2_2007_sum = df_arunachal_2_2007.sum(axis = 0, skipna = True)
print(df_arunachal_2_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_2_2008     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_2_2008_sum = df_arunachal_2_2008.sum(axis = 0, skipna = True)
print(df_arunachal_2_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_2_2009     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_2_2009_sum = df_arunachal_2_2009.sum(axis = 0, skipna = True)
print(df_arunachal_2_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_2_2010     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_2_2010_sum = df_arunachal_2_2010.sum(axis = 0, skipna = True)
print(df_arunachal_2_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_2_2011     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_2_2011_sum = df_arunachal_2_2011.sum(axis = 0, skipna = True)
print(df_arunachal_2_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_2_2012     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_2_2012_sum = df_arunachal_2_2012.sum(axis = 0, skipna = True)
print(df_arunachal_2_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_2_2013     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_2_2013_sum = df_arunachal_2_2013.sum(axis = 0, skipna = True)
print(df_arunachal_2_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_2_2014     = df_arunachal_2.loc[df_arunachal_2['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_2_2014_sum = df_arunachal_2_2014.sum(axis = 0, skipna = True)
print(df_arunachal_2_2014_sum)
print("---------------------------------")
                                                       
# details of arunachal : [3] DIBANG VALLEY  

print("--- Details of arunachal : [3] DIBANG VALLEY -------- ")
df_arunachal_3 = df_arunachal[df_arunachal.District_Name == 'DIBANG VALLEY']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_3_1997     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_3_1997_sum = df_arunachal_3_1997.sum(axis = 0, skipna = True)
print(df_arunachal_3_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_3_1998     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_3_1998_sum = df_arunachal_3_1998.sum(axis = 0, skipna = True)
print(df_arunachal_3_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_3_1999     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_3_1999_sum = df_arunachal_3_1999.sum(axis = 0, skipna = True)
print(df_arunachal_3_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_3_2000     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_3_2000_sum = df_arunachal_3_2000.sum(axis = 0, skipna = True)
print(df_arunachal_3_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_3_2001     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_3_2001_sum = df_arunachal_3_2001.sum(axis = 0, skipna = True)
print(df_arunachal_3_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_3_2002     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_3_2002_sum = df_arunachal_3_2002.sum(axis = 0, skipna = True)
print(df_arunachal_3_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_3_2003     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_3_2003_sum = df_arunachal_3_2003.sum(axis = 0, skipna = True)
print(df_arunachal_3_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_3_2004     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_3_2004_sum = df_arunachal_3_2004.sum(axis = 0, skipna = True)
print(df_arunachal_3_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_3_2005     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_3_2005_sum = df_arunachal_3_2005.sum(axis = 0, skipna = True)
print(df_arunachal_3_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_3_2006     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_3_2006_sum = df_arunachal_3_2006.sum(axis = 0, skipna = True)
print(df_arunachal_3_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_3_2007     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_3_2007_sum = df_arunachal_3_2007.sum(axis = 0, skipna = True)
print(df_arunachal_3_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_3_2008     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_3_2008_sum = df_arunachal_3_2008.sum(axis = 0, skipna = True)
print(df_arunachal_3_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_3_2009     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_3_2009_sum = df_arunachal_3_2009.sum(axis = 0, skipna = True)
print(df_arunachal_3_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_3_2010     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_3_2010_sum = df_arunachal_3_2010.sum(axis = 0, skipna = True)
print(df_arunachal_3_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_3_2011     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_3_2011_sum = df_arunachal_3_2011.sum(axis = 0, skipna = True)
print(df_arunachal_3_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_3_2012     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_3_2012_sum = df_arunachal_3_2012.sum(axis = 0, skipna = True)
print(df_arunachal_3_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_3_2013     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_3_2013_sum = df_arunachal_3_2013.sum(axis = 0, skipna = True)
print(df_arunachal_3_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_3_2014     = df_arunachal_3.loc[df_arunachal_3['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_3_2014_sum = df_arunachal_3_2014.sum(axis = 0, skipna = True)
print(df_arunachal_3_2014_sum)
print("---------------------------------")
                                    
# details of arunachal : [4] EAST KAMENG 

print("---- Details of arunachal : [4] EAST KAMENG -----")
df_arunachal_4 = df_arunachal[df_arunachal.District_Name == 'EAST KAMENG']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_4_1997     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_4_1997_sum = df_arunachal_4_1997.sum(axis = 0, skipna = True)
print(df_arunachal_4_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_4_1998     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_4_1998_sum = df_arunachal_4_1998.sum(axis = 0, skipna = True)
print(df_arunachal_4_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_4_1999     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_4_1999_sum = df_arunachal_4_1999.sum(axis = 0, skipna = True)
print(df_arunachal_4_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_4_2000     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_4_2000_sum = df_arunachal_4_2000.sum(axis = 0, skipna = True)
print(df_arunachal_4_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_4_2001     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_4_2001_sum = df_arunachal_4_2001.sum(axis = 0, skipna = True)
print(df_arunachal_4_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_4_2002     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_4_2002_sum = df_arunachal_4_2002.sum(axis = 0, skipna = True)
print(df_arunachal_4_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_4_2003     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_4_2003_sum = df_arunachal_4_2003.sum(axis = 0, skipna = True)
print(df_arunachal_4_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_4_2004     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_4_2004_sum = df_arunachal_4_2004.sum(axis = 0, skipna = True)
print(df_arunachal_4_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_4_2005     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_4_2005_sum = df_arunachal_4_2005.sum(axis = 0, skipna = True)
print(df_arunachal_4_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_4_2006     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_4_2006_sum = df_arunachal_4_2006.sum(axis = 0, skipna = True)
print(df_arunachal_4_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_4_2007     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_4_2007_sum = df_arunachal_4_2007.sum(axis = 0, skipna = True)
print(df_arunachal_4_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_4_2008     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_4_2008_sum = df_arunachal_4_2008.sum(axis = 0, skipna = True)
print(df_arunachal_4_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_4_2009     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_4_2009_sum = df_arunachal_4_2009.sum(axis = 0, skipna = True)
print(df_arunachal_4_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_4_2010     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_4_2010_sum = df_arunachal_4_2010.sum(axis = 0, skipna = True)
print(df_arunachal_4_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_4_2011     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_4_2011_sum = df_arunachal_4_2011.sum(axis = 0, skipna = True)
print(df_arunachal_4_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_4_2012     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_4_2012_sum = df_arunachal_4_2012.sum(axis = 0, skipna = True)
print(df_arunachal_4_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_4_2013     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_4_2013_sum = df_arunachal_4_2013.sum(axis = 0, skipna = True)
print(df_arunachal_4_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_4_2014     = df_arunachal_4.loc[df_arunachal_4['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_4_2014_sum = df_arunachal_4_2014.sum(axis = 0, skipna = True)
print(df_arunachal_4_2014_sum)
print("---------------------------------")
                    
# details of arunachal : [5] EAST SIANG 

print("--- Details of arunachal : [5] EAST SIANG -----")
df_arunachal_5 = df_arunachal[df_arunachal.District_Name == 'EAST SIANG']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_5_1997     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_5_1997_sum = df_arunachal_5_1997.sum(axis = 0, skipna = True)
print(df_arunachal_5_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_5_1998     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_5_1998_sum = df_arunachal_5_1998.sum(axis = 0, skipna = True)
print(df_arunachal_5_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_5_1999     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_5_1999_sum = df_arunachal_5_1999.sum(axis = 0, skipna = True)
print(df_arunachal_5_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_5_2000     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_5_2000_sum = df_arunachal_5_2000.sum(axis = 0, skipna = True)
print(df_arunachal_5_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_5_2001     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_5_2001_sum = df_arunachal_5_2001.sum(axis = 0, skipna = True)
print(df_arunachal_5_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_5_2002     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_5_2002_sum = df_arunachal_5_2002.sum(axis = 0, skipna = True)
print(df_arunachal_5_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_5_2003     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_5_2003_sum = df_arunachal_5_2003.sum(axis = 0, skipna = True)
print(df_arunachal_5_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_5_2004     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_5_2004_sum = df_arunachal_5_2004.sum(axis = 0, skipna = True)
print(df_arunachal_5_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_5_2005     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_5_2005_sum = df_arunachal_5_2005.sum(axis = 0, skipna = True)
print(df_arunachal_5_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_5_2006     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_5_2006_sum = df_arunachal_5_2006.sum(axis = 0, skipna = True)
print(df_arunachal_5_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_5_2007     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_5_2007_sum = df_arunachal_5_2007.sum(axis = 0, skipna = True)
print(df_arunachal_5_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_5_2008     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_5_2008_sum = df_arunachal_5_2008.sum(axis = 0, skipna = True)
print(df_arunachal_5_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_5_2009     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_5_2009_sum = df_arunachal_5_2009.sum(axis = 0, skipna = True)
print(df_arunachal_5_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_5_2010     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_5_2010_sum = df_arunachal_5_2010.sum(axis = 0, skipna = True)
print(df_arunachal_5_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_5_2011     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_5_2011_sum = df_arunachal_5_2011.sum(axis = 0, skipna = True)
print(df_arunachal_5_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_5_2012     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_5_2012_sum = df_arunachal_5_2012.sum(axis = 0, skipna = True)
print(df_arunachal_5_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_5_2013     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_5_2013_sum = df_arunachal_5_2013.sum(axis = 0, skipna = True)
print(df_arunachal_5_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_5_2014     = df_arunachal_5.loc[df_arunachal_5['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_5_2014_sum = df_arunachal_5_2014.sum(axis = 0, skipna = True)
print(df_arunachal_5_2014_sum)
print("---------------------------------")
                         
# details of arunachal : [6] KURUNG KUMEY

print("---- Details of arunachal : [6] KURUNG KUMEY-----")
df_arunachal_6 = df_arunachal[df_arunachal.District_Name == 'KURUNG KUMEY']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_6_1997     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_6_1997_sum = df_arunachal_6_1997.sum(axis = 0, skipna = True)
print(df_arunachal_6_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_6_1998     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_6_1998_sum = df_arunachal_6_1998.sum(axis = 0, skipna = True)
print(df_arunachal_6_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_6_1999     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_6_1999_sum = df_arunachal_6_1999.sum(axis = 0, skipna = True)
print(df_arunachal_6_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_6_2000     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_6_2000_sum = df_arunachal_6_2000.sum(axis = 0, skipna = True)
print(df_arunachal_6_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_6_2001     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_6_2001_sum = df_arunachal_6_2001.sum(axis = 0, skipna = True)
print(df_arunachal_6_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_6_2002     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_6_2002_sum = df_arunachal_6_2002.sum(axis = 0, skipna = True)
print(df_arunachal_6_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_6_2003     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_6_2003_sum = df_arunachal_6_2003.sum(axis = 0, skipna = True)
print(df_arunachal_6_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_6_2004     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_6_2004_sum = df_arunachal_6_2004.sum(axis = 0, skipna = True)
print(df_arunachal_6_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_6_2005     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_6_2005_sum = df_arunachal_6_2005.sum(axis = 0, skipna = True)
print(df_arunachal_6_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_6_2006     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_6_2006_sum = df_arunachal_6_2006.sum(axis = 0, skipna = True)
print(df_arunachal_6_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_6_2007     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_6_2007_sum = df_arunachal_6_2007.sum(axis = 0, skipna = True)
print(df_arunachal_6_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_6_2008     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_6_2008_sum = df_arunachal_6_2008.sum(axis = 0, skipna = True)
print(df_arunachal_6_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_6_2009     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_6_2009_sum = df_arunachal_6_2009.sum(axis = 0, skipna = True)
print(df_arunachal_6_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_6_2010     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_6_2010_sum = df_arunachal_6_2010.sum(axis = 0, skipna = True)
print(df_arunachal_6_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_6_2011     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_6_2011_sum = df_arunachal_6_2011.sum(axis = 0, skipna = True)
print(df_arunachal_6_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_6_2012     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_6_2012_sum = df_arunachal_6_2012.sum(axis = 0, skipna = True)
print(df_arunachal_6_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_6_2013     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_6_2013_sum = df_arunachal_6_2013.sum(axis = 0, skipna = True)
print(df_arunachal_6_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_6_2014     = df_arunachal_6.loc[df_arunachal_6['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_6_2014_sum = df_arunachal_6_2014.sum(axis = 0, skipna = True)
print(df_arunachal_6_2014_sum)
print("---------------------------------")
                      
# details of arunachal : [7] LOHIT 

print("----- Details of arunachal : [7] LOHIT -----")
df_arunachal_7 = df_arunachal[df_arunachal.District_Name == 'LOHIT']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_7_1997     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_7_1997_sum = df_arunachal_7_1997.sum(axis = 0, skipna = True)
print(df_arunachal_7_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_7_1998     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_7_1998_sum = df_arunachal_7_1998.sum(axis = 0, skipna = True)
print(df_arunachal_7_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_7_1999     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_7_1999_sum = df_arunachal_7_1999.sum(axis = 0, skipna = True)
print(df_arunachal_7_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_7_2000     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_7_2000_sum = df_arunachal_7_2000.sum(axis = 0, skipna = True)
print(df_arunachal_7_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_7_2001     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_7_2001_sum = df_arunachal_7_2001.sum(axis = 0, skipna = True)
print(df_arunachal_7_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_7_2002     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_7_2002_sum = df_arunachal_7_2002.sum(axis = 0, skipna = True)
print(df_arunachal_7_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_7_2003     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_7_2003_sum = df_arunachal_7_2003.sum(axis = 0, skipna = True)
print(df_arunachal_7_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_7_2004     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_7_2004_sum = df_arunachal_7_2004.sum(axis = 0, skipna = True)
print(df_arunachal_7_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_7_2005     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_7_2005_sum = df_arunachal_7_2005.sum(axis = 0, skipna = True)
print(df_arunachal_7_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_7_2006     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_7_2006_sum = df_arunachal_7_2006.sum(axis = 0, skipna = True)
print(df_arunachal_7_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_7_2007     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_7_2007_sum = df_arunachal_7_2007.sum(axis = 0, skipna = True)
print(df_arunachal_7_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_7_2008     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_7_2008_sum = df_arunachal_7_2008.sum(axis = 0, skipna = True)
print(df_arunachal_7_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_7_2009     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_7_2009_sum = df_arunachal_7_2009.sum(axis = 0, skipna = True)
print(df_arunachal_7_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_7_2010     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_7_2010_sum = df_arunachal_7_2010.sum(axis = 0, skipna = True)
print(df_arunachal_7_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_7_2011     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_7_2011_sum = df_arunachal_7_2011.sum(axis = 0, skipna = True)
print(df_arunachal_7_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_7_2012     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_7_2012_sum = df_arunachal_7_2012.sum(axis = 0, skipna = True)
print(df_arunachal_7_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_7_2013     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_7_2013_sum = df_arunachal_7_2013.sum(axis = 0, skipna = True)
print(df_arunachal_7_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_7_2014     = df_arunachal_7.loc[df_arunachal_7['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_7_2014_sum = df_arunachal_7_2014.sum(axis = 0, skipna = True)
print(df_arunachal_7_2014_sum)
print("---------------------------------")
                                                                                 
# details of arunachal : [8] LONGDING  

print("---- Details of arunachal : [8] LONGDING -------")
df_arunachal_8 = df_arunachal[df_arunachal.District_Name == 'LONGDING']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_8_1997     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_8_1997_sum = df_arunachal_8_1997.sum(axis = 0, skipna = True)
print(df_arunachal_8_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_8_1998     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_8_1998_sum = df_arunachal_8_1998.sum(axis = 0, skipna = True)
print(df_arunachal_8_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_8_1999     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_8_1999_sum = df_arunachal_8_1999.sum(axis = 0, skipna = True)
print(df_arunachal_8_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_8_2000     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_8_2000_sum = df_arunachal_8_2000.sum(axis = 0, skipna = True)
print(df_arunachal_8_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_8_2001     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_8_2001_sum = df_arunachal_8_2001.sum(axis = 0, skipna = True)
print(df_arunachal_8_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_8_2002     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_8_2002_sum = df_arunachal_8_2002.sum(axis = 0, skipna = True)
print(df_arunachal_8_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_8_2003     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_8_2003_sum = df_arunachal_8_2003.sum(axis = 0, skipna = True)
print(df_arunachal_8_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_8_2004     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_8_2004_sum = df_arunachal_8_2004.sum(axis = 0, skipna = True)
print(df_arunachal_8_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_8_2005     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_8_2005_sum = df_arunachal_8_2005.sum(axis = 0, skipna = True)
print(df_arunachal_8_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_8_2006     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_8_2006_sum = df_arunachal_8_2006.sum(axis = 0, skipna = True)
print(df_arunachal_8_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_8_2007     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_8_2007_sum = df_arunachal_8_2007.sum(axis = 0, skipna = True)
print(df_arunachal_8_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_8_2008     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_8_2008_sum = df_arunachal_8_2008.sum(axis = 0, skipna = True)
print(df_arunachal_8_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_8_2009     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_8_2009_sum = df_arunachal_8_2009.sum(axis = 0, skipna = True)
print(df_arunachal_8_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_8_2010     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_8_2010_sum = df_arunachal_8_2010.sum(axis = 0, skipna = True)
print(df_arunachal_8_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_8_2011     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_8_2011_sum = df_arunachal_8_2011.sum(axis = 0, skipna = True)
print(df_arunachal_8_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_8_2012     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_8_2012_sum = df_arunachal_8_2012.sum(axis = 0, skipna = True)
print(df_arunachal_8_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_8_2013     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_8_2013_sum = df_arunachal_8_2013.sum(axis = 0, skipna = True)
print(df_arunachal_8_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_8_2014     = df_arunachal_8.loc[df_arunachal_8['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_8_2014_sum = df_arunachal_8_2014.sum(axis = 0, skipna = True)
print(df_arunachal_8_2014_sum)
print("---------------------------------")
                               
# details of arunachal : [9] LOWER DIBANG VALLEY 

print("----Details of arunachal : [9] LOWER DIBANG VALLEY-------")
df_arunachal_9 = df_arunachal[df_arunachal.District_Name == 'LOWER DIBANG VALLEY']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_9_1997     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_9_1997_sum = df_arunachal_9_1997.sum(axis = 0, skipna = True)
print(df_arunachal_9_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_9_1998     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_9_1998_sum = df_arunachal_9_1998.sum(axis = 0, skipna = True)
print(df_arunachal_9_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_9_1999     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_9_1999_sum = df_arunachal_9_1999.sum(axis = 0, skipna = True)
print(df_arunachal_9_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_9_2000     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_9_2000_sum = df_arunachal_9_2000.sum(axis = 0, skipna = True)
print(df_arunachal_9_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_9_2001     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_9_2001_sum = df_arunachal_9_2001.sum(axis = 0, skipna = True)
print(df_arunachal_9_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_9_2002     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_9_2002_sum = df_arunachal_9_2002.sum(axis = 0, skipna = True)
print(df_arunachal_9_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_9_2003     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_9_2003_sum = df_arunachal_9_2003.sum(axis = 0, skipna = True)
print(df_arunachal_9_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_9_2004     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_9_2004_sum = df_arunachal_9_2004.sum(axis = 0, skipna = True)
print(df_arunachal_9_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_9_2005     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_9_2005_sum = df_arunachal_9_2005.sum(axis = 0, skipna = True)
print(df_arunachal_9_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_9_2006     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_9_2006_sum = df_arunachal_9_2006.sum(axis = 0, skipna = True)
print(df_arunachal_9_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_9_2007     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_9_2007_sum = df_arunachal_9_2007.sum(axis = 0, skipna = True)
print(df_arunachal_9_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_9_2008     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_9_2008_sum = df_arunachal_9_2008.sum(axis = 0, skipna = True)
print(df_arunachal_9_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_9_2009     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_9_2009_sum = df_arunachal_9_2009.sum(axis = 0, skipna = True)
print(df_arunachal_9_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_9_2010     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_9_2010_sum = df_arunachal_9_2010.sum(axis = 0, skipna = True)
print(df_arunachal_9_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_9_2011     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_9_2011_sum = df_arunachal_9_2011.sum(axis = 0, skipna = True)
print(df_arunachal_9_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_9_2012     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_9_2012_sum = df_arunachal_9_2012.sum(axis = 0, skipna = True)
print(df_arunachal_9_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_9_2013     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_9_2013_sum = df_arunachal_9_2013.sum(axis = 0, skipna = True)
print(df_arunachal_9_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_9_2014     = df_arunachal_9.loc[df_arunachal_9['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_9_2014_sum = df_arunachal_9_2014.sum(axis = 0, skipna = True)
print(df_arunachal_9_2014_sum)
print("---------------------------------")

# details of arunachal : [10] LOWER SUBANSIRI 

print("--- Details of arunachal : [10] LOWER SUBANSIRI -----")
df_arunachal_10 = df_arunachal[df_arunachal.District_Name == 'LOWER SUBANSIRI']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_10_1997     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_10_1997_sum = df_arunachal_10_1997.sum(axis = 0, skipna = True)
print(df_arunachal_10_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_10_1998     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_10_1998_sum = df_arunachal_10_1998.sum(axis = 0, skipna = True)
print(df_arunachal_10_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_10_1999     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_10_1999_sum = df_arunachal_10_1999.sum(axis = 0, skipna = True)
print(df_arunachal_10_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_10_2000     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_10_2000_sum = df_arunachal_10_2000.sum(axis = 0, skipna = True)
print(df_arunachal_10_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_10_2001     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_10_2001_sum = df_arunachal_10_2001.sum(axis = 0, skipna = True)
print(df_arunachal_10_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_10_2002     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_10_2002_sum = df_arunachal_10_2002.sum(axis = 0, skipna = True)
print(df_arunachal_10_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_10_2003     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_10_2003_sum = df_arunachal_10_2003.sum(axis = 0, skipna = True)
print(df_arunachal_10_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_10_2004     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_10_2004_sum = df_arunachal_10_2004.sum(axis = 0, skipna = True)
print(df_arunachal_10_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_10_2005     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_10_2005_sum = df_arunachal_10_2005.sum(axis = 0, skipna = True)
print(df_arunachal_10_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_10_2006     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_10_2006_sum = df_arunachal_10_2006.sum(axis = 0, skipna = True)
print(df_arunachal_10_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_10_2007     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_10_2007_sum = df_arunachal_10_2007.sum(axis = 0, skipna = True)
print(df_arunachal_10_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_10_2008     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_10_2008_sum = df_arunachal_10_2008.sum(axis = 0, skipna = True)
print(df_arunachal_10_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_10_2009     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_10_2009_sum = df_arunachal_10_2009.sum(axis = 0, skipna = True)
print(df_arunachal_10_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_10_2010     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_10_2010_sum = df_arunachal_10_2010.sum(axis = 0, skipna = True)
print(df_arunachal_10_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_10_2011     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_10_2011_sum = df_arunachal_10_2011.sum(axis = 0, skipna = True)
print(df_arunachal_10_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_10_2012     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_10_2012_sum = df_arunachal_10_2012.sum(axis = 0, skipna = True)
print(df_arunachal_10_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_10_2013     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_10_2013_sum = df_arunachal_10_2013.sum(axis = 0, skipna = True)
print(df_arunachal_10_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_10_2014     = df_arunachal_10.loc[df_arunachal_10['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_10_2014_sum = df_arunachal_10_2014.sum(axis = 0, skipna = True)
print(df_arunachal_10_2014_sum)
print("---------------------------------")
   
# details of arunachal : [11] NAMSAI 

print("--- Details of arunachal : [11] NAMSAI ----")
df_arunachal_11 = df_arunachal[df_arunachal.District_Name == 'NAMSAI']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_11_1997     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_11_1997_sum = df_arunachal_11_1997.sum(axis = 0, skipna = True)
print(df_arunachal_11_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_11_1998     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_11_1998_sum = df_arunachal_11_1998.sum(axis = 0, skipna = True)
print(df_arunachal_11_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_11_1999     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_11_1999_sum = df_arunachal_11_1999.sum(axis = 0, skipna = True)
print(df_arunachal_11_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_11_2000     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_11_2000_sum = df_arunachal_11_2000.sum(axis = 0, skipna = True)
print(df_arunachal_11_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_11_2001     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_11_2001_sum = df_arunachal_11_2001.sum(axis = 0, skipna = True)
print(df_arunachal_11_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_11_2002     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_11_2002_sum = df_arunachal_11_2002.sum(axis = 0, skipna = True)
print(df_arunachal_11_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_11_2003     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_11_2003_sum = df_arunachal_11_2003.sum(axis = 0, skipna = True)
print(df_arunachal_11_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_11_2004     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_11_2004_sum = df_arunachal_11_2004.sum(axis = 0, skipna = True)
print(df_arunachal_11_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_11_2005     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_11_2005_sum = df_arunachal_11_2005.sum(axis = 0, skipna = True)
print(df_arunachal_11_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_11_2006     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_11_2006_sum = df_arunachal_11_2006.sum(axis = 0, skipna = True)
print(df_arunachal_11_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_11_2007     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_11_2007_sum = df_arunachal_11_2007.sum(axis = 0, skipna = True)
print(df_arunachal_11_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_11_2008     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_11_2008_sum = df_arunachal_11_2008.sum(axis = 0, skipna = True)
print(df_arunachal_11_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_11_2009     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_11_2009_sum = df_arunachal_11_2009.sum(axis = 0, skipna = True)
print(df_arunachal_11_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_11_2010     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_11_2010_sum = df_arunachal_11_2010.sum(axis = 0, skipna = True)
print(df_arunachal_11_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_11_2011     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_11_2011_sum = df_arunachal_11_2011.sum(axis = 0, skipna = True)
print(df_arunachal_11_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_11_2012     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_11_2012_sum = df_arunachal_11_2012.sum(axis = 0, skipna = True)
print(df_arunachal_11_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_11_2013     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_11_2013_sum = df_arunachal_11_2013.sum(axis = 0, skipna = True)
print(df_arunachal_11_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_11_2014     = df_arunachal_11.loc[df_arunachal_11['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_11_2014_sum = df_arunachal_11_2014.sum(axis = 0, skipna = True)
print(df_arunachal_11_2014_sum)
print("---------------------------------")
                                    
# details of arunachal : [12] PAPUM PARE 

print("---- Details of arunachal : [12] PAPUM PARE -----")
df_arunachal_12 = df_arunachal[df_arunachal.District_Name == 'PAPUM PARE']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_12_1997     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_12_1997_sum = df_arunachal_12_1997.sum(axis = 0, skipna = True)
print(df_arunachal_12_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_12_1998     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_12_1998_sum = df_arunachal_12_1998.sum(axis = 0, skipna = True)
print(df_arunachal_12_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_12_1999     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_12_1999_sum = df_arunachal_12_1999.sum(axis = 0, skipna = True)
print(df_arunachal_12_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_12_2000     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_12_2000_sum = df_arunachal_12_2000.sum(axis = 0, skipna = True)
print(df_arunachal_12_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_12_2001     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_12_2001_sum = df_arunachal_12_2001.sum(axis = 0, skipna = True)
print(df_arunachal_12_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_12_2002     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_12_2002_sum = df_arunachal_12_2002.sum(axis = 0, skipna = True)
print(df_arunachal_12_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_12_2003     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_12_2003_sum = df_arunachal_12_2003.sum(axis = 0, skipna = True)
print(df_arunachal_12_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_12_2004     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_12_2004_sum = df_arunachal_12_2004.sum(axis = 0, skipna = True)
print(df_arunachal_12_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_12_2005     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_12_2005_sum = df_arunachal_12_2005.sum(axis = 0, skipna = True)
print(df_arunachal_12_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_12_2006     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_12_2006_sum = df_arunachal_12_2006.sum(axis = 0, skipna = True)
print(df_arunachal_12_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_12_2007     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_12_2007_sum = df_arunachal_12_2007.sum(axis = 0, skipna = True)
print(df_arunachal_12_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_12_2008     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_12_2008_sum = df_arunachal_12_2008.sum(axis = 0, skipna = True)
print(df_arunachal_12_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_12_2009     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_12_2009_sum = df_arunachal_12_2009.sum(axis = 0, skipna = True)
print(df_arunachal_12_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_12_2010     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_12_2010_sum = df_arunachal_12_2010.sum(axis = 0, skipna = True)
print(df_arunachal_12_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_12_2011     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_12_2011_sum = df_arunachal_12_2011.sum(axis = 0, skipna = True)
print(df_arunachal_12_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_12_2012     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_12_2012_sum = df_arunachal_12_2012.sum(axis = 0, skipna = True)
print(df_arunachal_12_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_12_2013     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_12_2013_sum = df_arunachal_12_2013.sum(axis = 0, skipna = True)
print(df_arunachal_12_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_12_2014     = df_arunachal_12.loc[df_arunachal_12['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_12_2014_sum = df_arunachal_12_2014.sum(axis = 0, skipna = True)
print(df_arunachal_12_2014_sum)
print("---------------------------------")
                                    
# details of arunachal : [13] TAWANG

print("--- Details of arunachal : [13] TAWANG ----")
df_arunachal_13 = df_arunachal[df_arunachal.District_Name == 'TAWANG']
                  
# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_13_1997     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_13_1997_sum = df_arunachal_13_1997.sum(axis = 0, skipna = True)
print(df_arunachal_13_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_13_1998     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_13_1998_sum = df_arunachal_13_1998.sum(axis = 0, skipna = True)
print(df_arunachal_13_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_13_1999     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_13_1999_sum = df_arunachal_13_1999.sum(axis = 0, skipna = True)
print(df_arunachal_13_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_13_2000     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_13_2000_sum = df_arunachal_13_2000.sum(axis = 0, skipna = True)
print(df_arunachal_13_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_13_2001     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_13_2001_sum = df_arunachal_13_2001.sum(axis = 0, skipna = True)
print(df_arunachal_13_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_13_2002     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_13_2002_sum = df_arunachal_13_2002.sum(axis = 0, skipna = True)
print(df_arunachal_13_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_13_2003     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_13_2003_sum = df_arunachal_13_2003.sum(axis = 0, skipna = True)
print(df_arunachal_13_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_13_2004     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_13_2004_sum = df_arunachal_13_2004.sum(axis = 0, skipna = True)
print(df_arunachal_13_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_13_2005     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_13_2005_sum = df_arunachal_13_2005.sum(axis = 0, skipna = True)
print(df_arunachal_13_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_13_2006     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_13_2006_sum = df_arunachal_13_2006.sum(axis = 0, skipna = True)
print(df_arunachal_13_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_13_2007     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_13_2007_sum = df_arunachal_13_2007.sum(axis = 0, skipna = True)
print(df_arunachal_13_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_13_2008     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_13_2008_sum = df_arunachal_13_2008.sum(axis = 0, skipna = True)
print(df_arunachal_13_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_13_2009     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_13_2009_sum = df_arunachal_13_2009.sum(axis = 0, skipna = True)
print(df_arunachal_13_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_13_2010     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_13_2010_sum = df_arunachal_13_2010.sum(axis = 0, skipna = True)
print(df_arunachal_13_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_13_2011     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_13_2011_sum = df_arunachal_13_2011.sum(axis = 0, skipna = True)
print(df_arunachal_13_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_13_2012     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_13_2012_sum = df_arunachal_13_2012.sum(axis = 0, skipna = True)
print(df_arunachal_13_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_13_2013     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_13_2013_sum = df_arunachal_13_2013.sum(axis = 0, skipna = True)
print(df_arunachal_13_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_13_2014     = df_arunachal_13.loc[df_arunachal_13['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_13_2014_sum = df_arunachal_13_2014.sum(axis = 0, skipna = True)
print(df_arunachal_13_2014_sum)
print("---------------------------------")
                                                                                                              
# details of arunachal : [14] TIRAP

print("----- Details of arunachal : [14] TIRAP ----")
df_arunachal_14 = df_arunachal[df_arunachal.District_Name == 'TIRAP']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_14_1997     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_14_1997_sum = df_arunachal_14_1997.sum(axis = 0, skipna = True)
print(df_arunachal_14_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_14_1998     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_14_1998_sum = df_arunachal_14_1998.sum(axis = 0, skipna = True)
print(df_arunachal_14_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_14_1999     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_14_1999_sum = df_arunachal_14_1999.sum(axis = 0, skipna = True)
print(df_arunachal_14_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_14_2000     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_14_2000_sum = df_arunachal_14_2000.sum(axis = 0, skipna = True)
print(df_arunachal_14_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_14_2001     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_14_2001_sum = df_arunachal_14_2001.sum(axis = 0, skipna = True)
print(df_arunachal_14_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_14_2002     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_14_2002_sum = df_arunachal_14_2002.sum(axis = 0, skipna = True)
print(df_arunachal_14_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_14_2003     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_14_2003_sum = df_arunachal_14_2003.sum(axis = 0, skipna = True)
print(df_arunachal_14_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_14_2004     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_14_2004_sum = df_arunachal_14_2004.sum(axis = 0, skipna = True)
print(df_arunachal_14_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_14_2005     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_14_2005_sum = df_arunachal_14_2005.sum(axis = 0, skipna = True)
print(df_arunachal_14_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_14_2006     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_14_2006_sum = df_arunachal_14_2006.sum(axis = 0, skipna = True)
print(df_arunachal_14_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_14_2007     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_14_2007_sum = df_arunachal_14_2007.sum(axis = 0, skipna = True)
print(df_arunachal_14_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_14_2008     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_14_2008_sum = df_arunachal_14_2008.sum(axis = 0, skipna = True)
print(df_arunachal_14_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_14_2009     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_14_2009_sum = df_arunachal_14_2009.sum(axis = 0, skipna = True)
print(df_arunachal_14_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_14_2010     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_14_2010_sum = df_arunachal_14_2010.sum(axis = 0, skipna = True)
print(df_arunachal_14_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_14_2011     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_14_2011_sum = df_arunachal_14_2011.sum(axis = 0, skipna = True)
print(df_arunachal_14_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_14_2012     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_14_2012_sum = df_arunachal_14_2012.sum(axis = 0, skipna = True)
print(df_arunachal_14_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_14_2013     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_14_2013_sum = df_arunachal_14_2013.sum(axis = 0, skipna = True)
print(df_arunachal_14_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_14_2014     = df_arunachal_14.loc[df_arunachal_14['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_14_2014_sum = df_arunachal_14_2014.sum(axis = 0, skipna = True)
print(df_arunachal_14_2014_sum)
print("---------------------------------")              
                                                          
# details of arunachal : [15] UPPER SIANG  

print("---- Details of arunachal : [15] UPPER SIANG --- ")
df_arunachal_15 = df_arunachal[df_arunachal.District_Name == 'UPPER SIANG']
             
# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_15_1997     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_15_1997_sum = df_arunachal_15_1997.sum(axis = 0, skipna = True)
print(df_arunachal_15_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_15_1998     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_15_1998_sum = df_arunachal_15_1998.sum(axis = 0, skipna = True)
print(df_arunachal_15_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_15_1999     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_15_1999_sum = df_arunachal_15_1999.sum(axis = 0, skipna = True)
print(df_arunachal_15_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_15_2000     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_15_2000_sum = df_arunachal_15_2000.sum(axis = 0, skipna = True)
print(df_arunachal_15_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_15_2001     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_15_2001_sum = df_arunachal_15_2001.sum(axis = 0, skipna = True)
print(df_arunachal_15_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_15_2002     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_15_2002_sum = df_arunachal_15_2002.sum(axis = 0, skipna = True)
print(df_arunachal_15_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_15_2003     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_15_2003_sum = df_arunachal_15_2003.sum(axis = 0, skipna = True)
print(df_arunachal_15_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_15_2004     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_15_2004_sum = df_arunachal_15_2004.sum(axis = 0, skipna = True)
print(df_arunachal_15_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_15_2005     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_15_2005_sum = df_arunachal_15_2005.sum(axis = 0, skipna = True)
print(df_arunachal_15_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_15_2006     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_15_2006_sum = df_arunachal_15_2006.sum(axis = 0, skipna = True)
print(df_arunachal_15_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_15_2007     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_15_2007_sum = df_arunachal_15_2007.sum(axis = 0, skipna = True)
print(df_arunachal_15_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_15_2008     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_15_2008_sum = df_arunachal_15_2008.sum(axis = 0, skipna = True)
print(df_arunachal_15_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_15_2009     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_15_2009_sum = df_arunachal_15_2009.sum(axis = 0, skipna = True)
print(df_arunachal_15_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_15_2010     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_15_2010_sum = df_arunachal_15_2010.sum(axis = 0, skipna = True)
print(df_arunachal_15_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_15_2011     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_15_2011_sum = df_arunachal_15_2011.sum(axis = 0, skipna = True)
print(df_arunachal_15_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_15_2012     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_15_2012_sum = df_arunachal_15_2012.sum(axis = 0, skipna = True)
print(df_arunachal_15_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_15_2013     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_15_2013_sum = df_arunachal_15_2013.sum(axis = 0, skipna = True)
print(df_arunachal_15_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_15_2014     = df_arunachal_15.loc[df_arunachal_15['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_15_2014_sum = df_arunachal_15_2014.sum(axis = 0, skipna = True)
print(df_arunachal_15_2014_sum)
print("---------------------------------")             
                                      
# details of arunachal : [16] UPPER SUBANSIRI 

print("---- Details of arunachal : [16] UPPER SUBANSIRI ----")
df_arunachal_16 = df_arunachal[df_arunachal.District_Name == 'UPPER SUBANSIRI']
          
# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_16_1997     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_16_1997_sum = df_arunachal_16_1997.sum(axis = 0, skipna = True)
print(df_arunachal_16_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_16_1998     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_16_1998_sum = df_arunachal_16_1998.sum(axis = 0, skipna = True)
print(df_arunachal_16_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_16_1999     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_16_1999_sum = df_arunachal_16_1999.sum(axis = 0, skipna = True)
print(df_arunachal_16_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_16_2000     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_16_2000_sum = df_arunachal_16_2000.sum(axis = 0, skipna = True)
print(df_arunachal_16_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_16_2001     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_16_2001_sum = df_arunachal_16_2001.sum(axis = 0, skipna = True)
print(df_arunachal_16_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_16_2002     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_16_2002_sum = df_arunachal_16_2002.sum(axis = 0, skipna = True)
print(df_arunachal_16_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_16_2003     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_16_2003_sum = df_arunachal_16_2003.sum(axis = 0, skipna = True)
print(df_arunachal_16_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_16_2004     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_16_2004_sum = df_arunachal_16_2004.sum(axis = 0, skipna = True)
print(df_arunachal_16_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_16_2005     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_16_2005_sum = df_arunachal_16_2005.sum(axis = 0, skipna = True)
print(df_arunachal_16_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_16_2006     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_16_2006_sum = df_arunachal_16_2006.sum(axis = 0, skipna = True)
print(df_arunachal_16_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_16_2007     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_16_2007_sum = df_arunachal_16_2007.sum(axis = 0, skipna = True)
print(df_arunachal_16_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_16_2008     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_16_2008_sum = df_arunachal_16_2008.sum(axis = 0, skipna = True)
print(df_arunachal_16_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_16_2009     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_16_2009_sum = df_arunachal_16_2009.sum(axis = 0, skipna = True)
print(df_arunachal_16_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_16_2010     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_16_2010_sum = df_arunachal_16_2010.sum(axis = 0, skipna = True)
print(df_arunachal_16_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_16_2011     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_16_2011_sum = df_arunachal_16_2011.sum(axis = 0, skipna = True)
print(df_arunachal_16_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_16_2012     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_16_2012_sum = df_arunachal_16_2012.sum(axis = 0, skipna = True)
print(df_arunachal_16_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_16_2013     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_16_2013_sum = df_arunachal_16_2013.sum(axis = 0, skipna = True)
print(df_arunachal_16_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_16_2014     = df_arunachal_16.loc[df_arunachal_16['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_16_2014_sum = df_arunachal_16_2014.sum(axis = 0, skipna = True)
print(df_arunachal_16_2014_sum)
print("---------------------------------")
                                                                  
# details of arunachal : [17] WEST KAMENG 

print("------ Details of arunachal : [17] WEST KAMENG ------")
df_arunachal_17 = df_arunachal[df_arunachal.District_Name == 'WEST KAMENG']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_17_1997     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_17_1997_sum = df_arunachal_17_1997.sum(axis = 0, skipna = True)
print(df_arunachal_17_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_17_1998     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_17_1998_sum = df_arunachal_17_1998.sum(axis = 0, skipna = True)
print(df_arunachal_17_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_17_1999     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_17_1999_sum = df_arunachal_17_1999.sum(axis = 0, skipna = True)
print(df_arunachal_17_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_17_2000     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_17_2000_sum = df_arunachal_17_2000.sum(axis = 0, skipna = True)
print(df_arunachal_17_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_17_2001     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_17_2001_sum = df_arunachal_17_2001.sum(axis = 0, skipna = True)
print(df_arunachal_17_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_17_2002     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_17_2002_sum = df_arunachal_17_2002.sum(axis = 0, skipna = True)
print(df_arunachal_17_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_17_2003     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_17_2003_sum = df_arunachal_17_2003.sum(axis = 0, skipna = True)
print(df_arunachal_17_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_17_2004     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_17_2004_sum = df_arunachal_17_2004.sum(axis = 0, skipna = True)
print(df_arunachal_17_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_17_2005     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_17_2005_sum = df_arunachal_17_2005.sum(axis = 0, skipna = True)
print(df_arunachal_17_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_17_2006     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_17_2006_sum = df_arunachal_17_2006.sum(axis = 0, skipna = True)
print(df_arunachal_17_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_17_2007     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_17_2007_sum = df_arunachal_17_2007.sum(axis = 0, skipna = True)
print(df_arunachal_17_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_17_2008     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_17_2008_sum = df_arunachal_17_2008.sum(axis = 0, skipna = True)
print(df_arunachal_17_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_17_2009     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_17_2009_sum = df_arunachal_17_2009.sum(axis = 0, skipna = True)
print(df_arunachal_17_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_17_2010     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_17_2010_sum = df_arunachal_17_2010.sum(axis = 0, skipna = True)
print(df_arunachal_17_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_17_2011     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_17_2011_sum = df_arunachal_17_2011.sum(axis = 0, skipna = True)
print(df_arunachal_17_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_17_2012     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_17_2012_sum = df_arunachal_17_2012.sum(axis = 0, skipna = True)
print(df_arunachal_17_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_17_2013     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_17_2013_sum = df_arunachal_17_2013.sum(axis = 0, skipna = True)
print(df_arunachal_17_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_17_2014     = df_arunachal_17.loc[df_arunachal_17['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_17_2014_sum = df_arunachal_17_2014.sum(axis = 0, skipna = True)
print(df_arunachal_17_2014_sum)
print("---------------------------------")
                  
# details of arunachal : [18] WEST SIANG                 

print("---- Details of arunachal : [18] WEST SIANG -------")
df_arunachal_18 = df_arunachal[df_arunachal.District_Name == 'WEST SIANG']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_arunachal_18_1997     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 1997,'Area':'Production']
df_arunachal_18_1997_sum = df_arunachal_18_1997.sum(axis = 0, skipna = True)
print(df_arunachal_18_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_arunachal_18_1998     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 1998,'Area':'Production']
df_arunachal_18_1998_sum = df_arunachal_18_1998.sum(axis = 0, skipna = True)
print(df_arunachal_18_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_arunachal_18_1999     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 1999,'Area':'Production']
df_arunachal_18_1999_sum = df_arunachal_18_1999.sum(axis = 0, skipna = True)
print(df_arunachal_18_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_arunachal_18_2000     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2000,'Area':'Production']
df_arunachal_18_2000_sum = df_arunachal_18_2000.sum(axis = 0, skipna = True)
print(df_arunachal_18_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_arunachal_18_2001     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2001,'Area':'Production']
df_arunachal_18_2001_sum = df_arunachal_18_2001.sum(axis = 0, skipna = True)
print(df_arunachal_18_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_arunachal_18_2002     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2002,'Area':'Production']
df_arunachal_18_2002_sum = df_arunachal_18_2002.sum(axis = 0, skipna = True)
print(df_arunachal_18_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_arunachal_18_2003     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2003,'Area':'Production']
df_arunachal_18_2003_sum = df_arunachal_18_2003.sum(axis = 0, skipna = True)
print(df_arunachal_18_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_arunachal_18_2004     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2004,'Area':'Production']
df_arunachal_18_2004_sum = df_arunachal_18_2004.sum(axis = 0, skipna = True)
print(df_arunachal_18_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_arunachal_18_2005     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2005,'Area':'Production']
df_arunachal_18_2005_sum = df_arunachal_18_2005.sum(axis = 0, skipna = True)
print(df_arunachal_18_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_arunachal_18_2006     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2006,'Area':'Production']
df_arunachal_18_2006_sum = df_arunachal_18_2006.sum(axis = 0, skipna = True)
print(df_arunachal_18_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_arunachal_18_2007     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2007,'Area':'Production']
df_arunachal_18_2007_sum = df_arunachal_18_2007.sum(axis = 0, skipna = True)
print(df_arunachal_18_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_arunachal_18_2008     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2008,'Area':'Production']
df_arunachal_18_2008_sum = df_arunachal_18_2008.sum(axis = 0, skipna = True)
print(df_arunachal_18_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_arunachal_18_2009     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2009,'Area':'Production']
df_arunachal_18_2009_sum = df_arunachal_18_2009.sum(axis = 0, skipna = True)
print(df_arunachal_18_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_arunachal_18_2010     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2010,'Area':'Production']
df_arunachal_18_2010_sum = df_arunachal_18_2010.sum(axis = 0, skipna = True)
print(df_arunachal_18_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_arunachal_18_2011     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2011,'Area':'Production']
df_arunachal_18_2011_sum = df_arunachal_18_2011.sum(axis = 0, skipna = True)
print(df_arunachal_18_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_arunachal_18_2012     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2012,'Area':'Production']
df_arunachal_18_2012_sum = df_arunachal_18_2012.sum(axis = 0, skipna = True)
print(df_arunachal_18_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_arunachal_18_2013     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2013,'Area':'Production']
df_arunachal_18_2013_sum = df_arunachal_18_2013.sum(axis = 0, skipna = True)
print(df_arunachal_18_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_arunachal_18_2014     = df_arunachal_18.loc[df_arunachal_18['Crop_Year'] == 2014,'Area':'Production']
df_arunachal_18_2014_sum = df_arunachal_18_2014.sum(axis = 0, skipna = True)
print(df_arunachal_18_2014_sum)
print("---------------------------------")


#Question-(4) Assam

print("--- State-4 : Assam -------")
df_assam = df[df.State_Name == 'Assam']
df_assam_dist = df_assam.groupby(['District_Name'])[['Crop_Year']].count()
print(df_assam_dist)

# crop year in Assam

print("---- Crop year in Assam ----")
df_assam_year = df_assam.groupby(['Crop_Year'])[['Crop_Year']].count()
print(df_assam_year)

# crop types in Assam

print("---- Crop types in Assam -----")
df_assam_crop = df_assam.groupby(['Crop'])[['Crop']].count()
print(df_assam_crop)

# details of assam : [1] BAKSA

print("---- Details of assam : [1] BAKSA -----")
df_assam_1 = df_assam[df_assam.District_Name == 'BAKSA']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_1_1997 = df_assam_1.loc[df_assam_1['Crop_Year'] == 1997,'Area':'Production']
df_assam_1_1997_sum = df_assam_1_1997.sum(axis = 0, skipna = True)
print(df_assam_1_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_1_1998 = df_assam_1.loc[df_assam_1['Crop_Year'] == 1998,'Area':'Production']
df_assam_1_1998_sum = df_assam_1_1998.sum(axis = 0, skipna = True) 
print(df_assam_1_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_1_1999 = df_assam_1.loc[df_assam_1['Crop_Year'] == 1999,'Area':'Production']
df_assam_1_1999_sum = df_assam_1_1999.sum(axis = 0, skipna = True) 
print(df_assam_1_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_1_2000 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2000,'Area':'Production']
df_assam_1_2000_sum = df_assam_1_2000.sum(axis = 0, skipna = True) 
print(df_assam_1_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_1_2001 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_1_2001_sum = df_assam_1_2001.sum(axis = 0, skipna = True)
print(df_assam_1_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_1_2002 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2002,'Area':'Production']
df_assam_1_2002_sum = df_assam_1_2002.sum(axis = 0, skipna = True) 
print(df_assam_1_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_1_2003 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2003,'Area':'Production']
df_assam_1_2003_sum = df_assam_1_2003.sum(axis = 0, skipna = True) 
print(df_assam_1_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_1_2004 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2004,'Area':'Production']
df_assam_1_2004_sum = df_assam_1_2004.sum(axis = 0, skipna = True) 
print(df_assam_1_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_1_2005 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2005,'Area':'Production']
df_assam_1_2005_sum = df_assam_1_2005.sum(axis = 0, skipna = True) 
print(df_assam_1_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_1_2006 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_1_2006_sum = df_assam_1_2006.sum(axis = 0, skipna = True)
print(df_assam_1_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_1_2007 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2007,'Area':'Production']
df_assam_1_2007_sum = df_assam_1_2007.sum(axis = 0, skipna = True) 
print(df_assam_1_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_1_2008 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2008,'Area':'Production']
df_assam_1_2008_sum = df_assam_1_2008.sum(axis = 0, skipna = True) 
print(df_assam_1_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_1_2009 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2009,'Area':'Production']
df_assam_1_2009_sum = df_assam_1_2009.sum(axis = 0, skipna = True) 
print(df_assam_1_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_1_2010 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_1_2010_sum = df_assam_1_2010.sum(axis = 0, skipna = True)
print(df_assam_1_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_1_2011 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_1_2011_sum = df_assam_1_2011.sum(axis = 0, skipna = True)
print(df_assam_1_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_1_2012 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2012,'Area':'Production']
df_assam_1_2012_sum = df_assam_1_2012.sum(axis = 0, skipna = True) 
print(df_assam_1_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_1_2013 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_1_2013_sum = df_assam_1_2013.sum(axis = 0, skipna = True)
print(df_assam_1_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_1_2014 = df_assam_1.loc[df_assam_1['Crop_Year'] == 2014,'Area':'Production']
df_assam_1_2014_sum = df_assam_1_2014.sum(axis = 0, skipna = True) 
print(df_assam_1_2014_sum)
print("---------------------------------")
                                        
# details of assam : [2] BARPETA 

print("--- Details of Assam : [2] BARPETA ----")
df_assam_2 = df_assam[df_assam.District_Name == 'BARPETA']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_2_1997 = df_assam_2.loc[df_assam_2['Crop_Year'] == 1997,'Area':'Production']
df_assam_2_1997_sum = df_assam_2_1997.sum(axis = 0, skipna = True)
print(df_assam_2_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_2_1998 = df_assam_2.loc[df_assam_2['Crop_Year'] == 1998,'Area':'Production']
df_assam_2_1998_sum = df_assam_2_1998.sum(axis = 0, skipna = True) 
print(df_assam_2_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_2_1999 = df_assam_2.loc[df_assam_2['Crop_Year'] == 1999,'Area':'Production']
df_assam_2_1999_sum = df_assam_2_1999.sum(axis = 0, skipna = True) 
print(df_assam_2_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_2_2000 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2000,'Area':'Production']
df_assam_2_2000_sum = df_assam_2_2000.sum(axis = 0, skipna = True) 
print(df_assam_2_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_2_2001 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_2_2001_sum = df_assam_2_2001.sum(axis = 0, skipna = True)
print(df_assam_2_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_2_2002 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2002,'Area':'Production']
df_assam_2_2002_sum = df_assam_2_2002.sum(axis = 0, skipna = True) 
print(df_assam_2_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_2_2003 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2003,'Area':'Production']
df_assam_2_2003_sum = df_assam_2_2003.sum(axis = 0, skipna = True) 
print(df_assam_2_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_2_2004 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2004,'Area':'Production']
df_assam_2_2004_sum = df_assam_2_2004.sum(axis = 0, skipna = True) 
print(df_assam_2_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_2_2005 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2005,'Area':'Production']
df_assam_2_2005_sum = df_assam_2_2005.sum(axis = 0, skipna = True) 
print(df_assam_2_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_2_2006 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_2_2006_sum = df_assam_2_2006.sum(axis = 0, skipna = True)
print(df_assam_2_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_2_2007 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2007,'Area':'Production']
df_assam_2_2007_sum = df_assam_2_2007.sum(axis = 0, skipna = True) 
print(df_assam_2_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_2_2008 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2008,'Area':'Production']
df_assam_2_2008_sum = df_assam_2_2008.sum(axis = 0, skipna = True) 
print(df_assam_2_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_2_2009 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2009,'Area':'Production']
df_assam_2_2009_sum = df_assam_2_2009.sum(axis = 0, skipna = True) 
print(df_assam_2_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_2_2010 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_2_2010_sum = df_assam_2_2010.sum(axis = 0, skipna = True)
print(df_assam_2_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_2_2011 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_2_2011_sum = df_assam_2_2011.sum(axis = 0, skipna = True)
print(df_assam_2_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_2_2012 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2012,'Area':'Production']
df_assam_2_2012_sum = df_assam_2_2012.sum(axis = 0, skipna = True) 
print(df_assam_2_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_2_2013 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_2_2013_sum = df_assam_2_2013.sum(axis = 0, skipna = True)
print(df_assam_2_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_2_2014 = df_assam_2.loc[df_assam_2['Crop_Year'] == 2014,'Area':'Production']
df_assam_2_2014_sum = df_assam_2_2014.sum(axis = 0, skipna = True) 
print(df_assam_2_2014_sum)
print("---------------------------------")
                         
# details of assam : [3] BONGAIGAON

print("----- Details of assam : [3] BONGAIGAON -----")
df_assam_3 = df_assam[df_assam.District_Name == 'BONGAIGAON']
         
# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_3_1997 = df_assam_3.loc[df_assam_3['Crop_Year'] == 1997,'Area':'Production']
df_assam_3_1997_sum = df_assam_3_1997.sum(axis = 0, skipna = True)
print(df_assam_3_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_3_1998 = df_assam_3.loc[df_assam_3['Crop_Year'] == 1998,'Area':'Production']
df_assam_3_1998_sum = df_assam_3_1998.sum(axis = 0, skipna = True) 
print(df_assam_3_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_3_1999 = df_assam_3.loc[df_assam_3['Crop_Year'] == 1999,'Area':'Production']
df_assam_3_1999_sum = df_assam_3_1999.sum(axis = 0, skipna = True) 
print(df_assam_3_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_3_2000 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2000,'Area':'Production']
df_assam_3_2000_sum = df_assam_3_2000.sum(axis = 0, skipna = True) 
print(df_assam_3_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_3_2001 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_3_2001_sum = df_assam_3_2001.sum(axis = 0, skipna = True)
print(df_assam_3_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_3_2002 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2002,'Area':'Production']
df_assam_3_2002_sum = df_assam_3_2002.sum(axis = 0, skipna = True) 
print(df_assam_3_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_3_2003 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2003,'Area':'Production']
df_assam_3_2003_sum = df_assam_3_2003.sum(axis = 0, skipna = True) 
print(df_assam_3_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_3_2004 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2004,'Area':'Production']
df_assam_3_2004_sum = df_assam_3_2004.sum(axis = 0, skipna = True) 
print(df_assam_3_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_3_2005 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2005,'Area':'Production']
df_assam_3_2005_sum = df_assam_3_2005.sum(axis = 0, skipna = True) 
print(df_assam_3_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_3_2006 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_3_2006_sum = df_assam_3_2006.sum(axis = 0, skipna = True)
print(df_assam_3_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_3_2007 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2007,'Area':'Production']
df_assam_3_2007_sum = df_assam_3_2007.sum(axis = 0, skipna = True) 
print(df_assam_3_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_3_2008 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2008,'Area':'Production']
df_assam_3_2008_sum = df_assam_3_2008.sum(axis = 0, skipna = True) 
print(df_assam_3_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_3_2009 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2009,'Area':'Production']
df_assam_3_2009_sum = df_assam_3_2009.sum(axis = 0, skipna = True) 
print(df_assam_3_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_3_2010 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_3_2010_sum = df_assam_3_2010.sum(axis = 0, skipna = True)
print(df_assam_3_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_3_2011 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_3_2011_sum = df_assam_3_2011.sum(axis = 0, skipna = True)
print(df_assam_3_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_3_2012 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2012,'Area':'Production']
df_assam_3_2012_sum = df_assam_3_2012.sum(axis = 0, skipna = True) 
print(df_assam_3_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_3_2013 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_3_2013_sum = df_assam_3_2013.sum(axis = 0, skipna = True)
print(df_assam_3_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_3_2014 = df_assam_3.loc[df_assam_3['Crop_Year'] == 2014,'Area':'Production']
df_assam_3_2014_sum = df_assam_3_2014.sum(axis = 0, skipna = True) 
print(df_assam_3_2014_sum)
print("---------------------------------")
                                                                  
# details of assam : [4] CACHAR

print("---- Details of assam : [4] CACHAR ----- ")
df_assam_4 = df_assam[df_assam.District_Name == 'CACHAR']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_4_1997 = df_assam_4.loc[df_assam_4['Crop_Year'] == 1997,'Area':'Production']
df_assam_4_1997_sum = df_assam_4_1997.sum(axis = 0, skipna = True)
print(df_assam_4_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_4_1998 = df_assam_4.loc[df_assam_4['Crop_Year'] == 1998,'Area':'Production']
df_assam_4_1998_sum = df_assam_4_1998.sum(axis = 0, skipna = True) 
print(df_assam_4_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_4_1999 = df_assam_4.loc[df_assam_4['Crop_Year'] == 1999,'Area':'Production']
df_assam_4_1999_sum = df_assam_4_1999.sum(axis = 0, skipna = True) 
print(df_assam_4_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_4_2000 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2000,'Area':'Production']
df_assam_4_2000_sum = df_assam_4_2000.sum(axis = 0, skipna = True) 
print(df_assam_4_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_4_2001 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_4_2001_sum = df_assam_4_2001.sum(axis = 0, skipna = True)
print(df_assam_4_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_4_2002 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2002,'Area':'Production']
df_assam_4_2002_sum = df_assam_4_2002.sum(axis = 0, skipna = True) 
print(df_assam_4_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_4_2003 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2003,'Area':'Production']
df_assam_4_2003_sum = df_assam_4_2003.sum(axis = 0, skipna = True) 
print(df_assam_4_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_4_2004 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2004,'Area':'Production']
df_assam_4_2004_sum = df_assam_4_2004.sum(axis = 0, skipna = True) 
print(df_assam_4_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_4_2005 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2005,'Area':'Production']
df_assam_4_2005_sum = df_assam_4_2005.sum(axis = 0, skipna = True) 
print(df_assam_4_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_4_2006 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_4_2006_sum = df_assam_4_2006.sum(axis = 0, skipna = True)
print(df_assam_4_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_4_2007 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2007,'Area':'Production']
df_assam_4_2007_sum = df_assam_4_2007.sum(axis = 0, skipna = True) 
print(df_assam_4_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_4_2008 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2008,'Area':'Production']
df_assam_4_2008_sum = df_assam_4_2008.sum(axis = 0, skipna = True) 
print(df_assam_4_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_4_2009 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2009,'Area':'Production']
df_assam_4_2009_sum = df_assam_4_2009.sum(axis = 0, skipna = True) 
print(df_assam_4_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_4_2010 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_4_2010_sum = df_assam_4_2010.sum(axis = 0, skipna = True)
print(df_assam_4_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_4_2011 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_4_2011_sum = df_assam_4_2011.sum(axis = 0, skipna = True)
print(df_assam_4_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_4_2012 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2012,'Area':'Production']
df_assam_4_2012_sum = df_assam_4_2012.sum(axis = 0, skipna = True) 
print(df_assam_4_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_4_2013 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_4_2013_sum = df_assam_4_2013.sum(axis = 0, skipna = True)
print(df_assam_4_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_4_2014 = df_assam_4.loc[df_assam_4['Crop_Year'] == 2014,'Area':'Production']
df_assam_4_2014_sum = df_assam_4_2014.sum(axis = 0, skipna = True) 
print(df_assam_4_2014_sum)
print("---------------------------------")                          
                                             
# details of assam : [5] CHIRANG

print("---- Details of assam : [5] CHIRANG -----")
df_assam_5 = df_assam[df_assam.District_Name == 'CHIRANG']
              
# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_5_1997 = df_assam_5.loc[df_assam_5['Crop_Year'] == 1997,'Area':'Production']
df_assam_5_1997_sum = df_assam_5_1997.sum(axis = 0, skipna = True)
print(df_assam_5_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_5_1998 = df_assam_5.loc[df_assam_5['Crop_Year'] == 1998,'Area':'Production']
df_assam_5_1998_sum = df_assam_5_1998.sum(axis = 0, skipna = True) 
print(df_assam_5_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_5_1999 = df_assam_5.loc[df_assam_5['Crop_Year'] == 1999,'Area':'Production']
df_assam_5_1999_sum = df_assam_5_1999.sum(axis = 0, skipna = True) 
print(df_assam_5_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_5_2000 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2000,'Area':'Production']
df_assam_5_2000_sum = df_assam_5_2000.sum(axis = 0, skipna = True) 
print(df_assam_5_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_5_2001 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_5_2001_sum = df_assam_5_2001.sum(axis = 0, skipna = True)
print(df_assam_5_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_5_2002 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2002,'Area':'Production']
df_assam_5_2002_sum = df_assam_5_2002.sum(axis = 0, skipna = True) 
print(df_assam_5_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_5_2003 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2003,'Area':'Production']
df_assam_5_2003_sum = df_assam_5_2003.sum(axis = 0, skipna = True) 
print(df_assam_5_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_5_2004 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2004,'Area':'Production']
df_assam_5_2004_sum = df_assam_5_2004.sum(axis = 0, skipna = True) 
print(df_assam_5_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_5_2005 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2005,'Area':'Production']
df_assam_5_2005_sum = df_assam_5_2005.sum(axis = 0, skipna = True) 
print(df_assam_5_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_5_2006 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_5_2006_sum = df_assam_5_2006.sum(axis = 0, skipna = True)
print(df_assam_5_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_5_2007 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2007,'Area':'Production']
df_assam_5_2007_sum = df_assam_5_2007.sum(axis = 0, skipna = True) 
print(df_assam_5_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_5_2008 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2008,'Area':'Production']
df_assam_5_2008_sum = df_assam_5_2008.sum(axis = 0, skipna = True) 
print(df_assam_5_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_5_2009 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2009,'Area':'Production']
df_assam_5_2009_sum = df_assam_5_2009.sum(axis = 0, skipna = True) 
print(df_assam_5_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_5_2010 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_5_2010_sum = df_assam_5_2010.sum(axis = 0, skipna = True)
print(df_assam_5_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_5_2011 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_5_2011_sum = df_assam_5_2011.sum(axis = 0, skipna = True)
print(df_assam_5_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_5_2012 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2012,'Area':'Production']
df_assam_5_2012_sum = df_assam_5_2012.sum(axis = 0, skipna = True) 
print(df_assam_5_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_5_2013 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_5_2013_sum = df_assam_5_2013.sum(axis = 0, skipna = True)
print(df_assam_5_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_5_2014 = df_assam_5.loc[df_assam_5['Crop_Year'] == 2014,'Area':'Production']
df_assam_5_2014_sum = df_assam_5_2014.sum(axis = 0, skipna = True) 
print(df_assam_5_2014_sum)
print("---------------------------------")
                                                                                    
# details of assam : [6] DARRANG

print("----- Details of assam : [6] DARRANG -----")
df_assam_6 = df_assam[df_assam.District_Name == 'DARRANG']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_6_1997 = df_assam_6.loc[df_assam_6['Crop_Year'] == 1997,'Area':'Production']
df_assam_6_1997_sum = df_assam_6_1997.sum(axis = 0, skipna = True)
print(df_assam_6_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_6_1998 = df_assam_6.loc[df_assam_6['Crop_Year'] == 1998,'Area':'Production']
df_assam_6_1998_sum = df_assam_6_1998.sum(axis = 0, skipna = True) 
print(df_assam_6_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_6_1999 = df_assam_6.loc[df_assam_6['Crop_Year'] == 1999,'Area':'Production']
df_assam_6_1999_sum = df_assam_6_1999.sum(axis = 0, skipna = True) 
print(df_assam_6_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_6_2000 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2000,'Area':'Production']
df_assam_6_2000_sum = df_assam_6_2000.sum(axis = 0, skipna = True) 
print(df_assam_6_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_6_2001 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_6_2001_sum = df_assam_6_2001.sum(axis = 0, skipna = True)
print(df_assam_6_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_6_2002 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2002,'Area':'Production']
df_assam_6_2002_sum = df_assam_6_2002.sum(axis = 0, skipna = True) 
print(df_assam_6_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_6_2003 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2003,'Area':'Production']
df_assam_6_2003_sum = df_assam_6_2003.sum(axis = 0, skipna = True) 
print(df_assam_6_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_6_2004 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2004,'Area':'Production']
df_assam_6_2004_sum = df_assam_6_2004.sum(axis = 0, skipna = True) 
print(df_assam_6_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_6_2005 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2005,'Area':'Production']
df_assam_6_2005_sum = df_assam_6_2005.sum(axis = 0, skipna = True) 
print(df_assam_6_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_6_2006 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_6_2006_sum = df_assam_6_2006.sum(axis = 0, skipna = True)
print(df_assam_6_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_6_2007 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2007,'Area':'Production']
df_assam_6_2007_sum = df_assam_6_2007.sum(axis = 0, skipna = True) 
print(df_assam_6_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_6_2008 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2008,'Area':'Production']
df_assam_6_2008_sum = df_assam_6_2008.sum(axis = 0, skipna = True) 
print(df_assam_6_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_6_2009 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2009,'Area':'Production']
df_assam_6_2009_sum = df_assam_6_2009.sum(axis = 0, skipna = True) 
print(df_assam_6_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_6_2010 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_6_2010_sum = df_assam_6_2010.sum(axis = 0, skipna = True)
print(df_assam_6_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_6_2011 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_6_2011_sum = df_assam_6_2011.sum(axis = 0, skipna = True)
print(df_assam_6_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_6_2012 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2012,'Area':'Production']
df_assam_6_2012_sum = df_assam_6_2012.sum(axis = 0, skipna = True) 
print(df_assam_6_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_6_2013 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_6_2013_sum = df_assam_6_2013.sum(axis = 0, skipna = True)
print(df_assam_6_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_6_2014 = df_assam_6.loc[df_assam_6['Crop_Year'] == 2014,'Area':'Production']
df_assam_6_2014_sum = df_assam_6_2014.sum(axis = 0, skipna = True) 
print(df_assam_6_2014_sum)
print("---------------------------------")              
                                          
# details of assam : [7] DHEMAJI 

print("----- Details of assam : [7] DHEMAJI ----")
df_assam_7 = df_assam[df_assam.District_Name == 'DHEMAJI']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_7_1997 = df_assam_7.loc[df_assam_7['Crop_Year'] == 1997,'Area':'Production']
df_assam_7_1997_sum = df_assam_7_1997.sum(axis = 0, skipna = True)
print(df_assam_7_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_7_1998 = df_assam_7.loc[df_assam_7['Crop_Year'] == 1998,'Area':'Production']
df_assam_7_1998_sum = df_assam_7_1998.sum(axis = 0, skipna = True) 
print(df_assam_7_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_7_1999 = df_assam_7.loc[df_assam_7['Crop_Year'] == 1999,'Area':'Production']
df_assam_7_1999_sum = df_assam_7_1999.sum(axis = 0, skipna = True) 
print(df_assam_7_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_7_2000 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2000,'Area':'Production']
df_assam_7_2000_sum = df_assam_7_2000.sum(axis = 0, skipna = True) 
print(df_assam_7_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_7_2001 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_7_2001_sum = df_assam_7_2001.sum(axis = 0, skipna = True)
print(df_assam_7_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_7_2002 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2002,'Area':'Production']
df_assam_7_2002_sum = df_assam_7_2002.sum(axis = 0, skipna = True) 
print(df_assam_7_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_7_2003 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2003,'Area':'Production']
df_assam_7_2003_sum = df_assam_7_2003.sum(axis = 0, skipna = True) 
print(df_assam_7_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_7_2004 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2004,'Area':'Production']
df_assam_7_2004_sum = df_assam_7_2004.sum(axis = 0, skipna = True) 
print(df_assam_7_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_7_2005 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2005,'Area':'Production']
df_assam_7_2005_sum = df_assam_7_2005.sum(axis = 0, skipna = True) 
print(df_assam_7_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_7_2006 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_7_2006_sum = df_assam_7_2006.sum(axis = 0, skipna = True)
print(df_assam_7_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_7_2007 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2007,'Area':'Production']
df_assam_7_2007_sum = df_assam_7_2007.sum(axis = 0, skipna = True) 
print(df_assam_7_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_7_2008 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2008,'Area':'Production']
df_assam_7_2008_sum = df_assam_7_2008.sum(axis = 0, skipna = True) 
print(df_assam_7_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_7_2009 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2009,'Area':'Production']
df_assam_7_2009_sum = df_assam_7_2009.sum(axis = 0, skipna = True) 
print(df_assam_7_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_7_2010 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_7_2010_sum = df_assam_7_2010.sum(axis = 0, skipna = True)
print(df_assam_7_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_7_2011 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_7_2011_sum = df_assam_7_2011.sum(axis = 0, skipna = True)
print(df_assam_7_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_7_2012 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2012,'Area':'Production']
df_assam_7_2012_sum = df_assam_7_2012.sum(axis = 0, skipna = True) 
print(df_assam_7_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_7_2013 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_7_2013_sum = df_assam_7_2013.sum(axis = 0, skipna = True)
print(df_assam_7_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_7_2014 = df_assam_7.loc[df_assam_7['Crop_Year'] == 2014,'Area':'Production']
df_assam_7_2014_sum = df_assam_7_2014.sum(axis = 0, skipna = True) 
print(df_assam_7_2014_sum)
print("---------------------------------")
                 
# details of assam : [8] DHUBRI

print("---- Details of assam : [8] DHUBRI ------")
df_assam_8 = df_assam[df_assam.District_Name == 'DHUBRI']
                               
# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_8_1997 = df_assam_8.loc[df_assam_8['Crop_Year'] == 1997,'Area':'Production']
df_assam_8_1997_sum = df_assam_8_1997.sum(axis = 0, skipna = True)
print(df_assam_8_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_8_1998 = df_assam_8.loc[df_assam_8['Crop_Year'] == 1998,'Area':'Production']
df_assam_8_1998_sum = df_assam_8_1998.sum(axis = 0, skipna = True) 
print(df_assam_8_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_8_1999 = df_assam_8.loc[df_assam_8['Crop_Year'] == 1999,'Area':'Production']
df_assam_8_1999_sum = df_assam_8_1999.sum(axis = 0, skipna = True) 
print(df_assam_8_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_8_2000 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2000,'Area':'Production']
df_assam_8_2000_sum = df_assam_8_2000.sum(axis = 0, skipna = True) 
print(df_assam_8_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_8_2001 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_8_2001_sum = df_assam_8_2001.sum(axis = 0, skipna = True)
print(df_assam_8_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_8_2002 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2002,'Area':'Production']
df_assam_8_2002_sum = df_assam_8_2002.sum(axis = 0, skipna = True) 
print(df_assam_8_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_8_2003 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2003,'Area':'Production']
df_assam_8_2003_sum = df_assam_8_2003.sum(axis = 0, skipna = True) 
print(df_assam_8_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_8_2004 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2004,'Area':'Production']
df_assam_8_2004_sum = df_assam_8_2004.sum(axis = 0, skipna = True) 
print(df_assam_8_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_8_2005 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2005,'Area':'Production']
df_assam_8_2005_sum = df_assam_8_2005.sum(axis = 0, skipna = True) 
print(df_assam_8_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_8_2006 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_8_2006_sum = df_assam_8_2006.sum(axis = 0, skipna = True)
print(df_assam_8_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_8_2007 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2007,'Area':'Production']
df_assam_8_2007_sum = df_assam_8_2007.sum(axis = 0, skipna = True) 
print(df_assam_8_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_8_2008 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2008,'Area':'Production']
df_assam_8_2008_sum = df_assam_8_2008.sum(axis = 0, skipna = True) 
print(df_assam_8_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_8_2009 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2009,'Area':'Production']
df_assam_8_2009_sum = df_assam_8_2009.sum(axis = 0, skipna = True) 
print(df_assam_8_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_8_2010 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_8_2010_sum = df_assam_8_2010.sum(axis = 0, skipna = True)
print(df_assam_8_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_8_2011 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_8_2011_sum = df_assam_8_2011.sum(axis = 0, skipna = True)
print(df_assam_8_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_8_2012 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2012,'Area':'Production']
df_assam_8_2012_sum = df_assam_8_2012.sum(axis = 0, skipna = True) 
print(df_assam_8_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_8_2013 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_8_2013_sum = df_assam_8_2013.sum(axis = 0, skipna = True)
print(df_assam_8_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_8_2014 = df_assam_8.loc[df_assam_8['Crop_Year'] == 2014,'Area':'Production']
df_assam_8_2014_sum = df_assam_8_2014.sum(axis = 0, skipna = True) 
print(df_assam_8_2014_sum)
print("---------------------------------")                               
                               
# details of assam : [9] DIBRUGARH 

print("----- Details of assam : [9] DIBRUGARH -----")
df_assam_9 = df_assam[df_assam.District_Name == 'DIBRUGARH']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_9_1997 = df_assam_9.loc[df_assam_9['Crop_Year'] == 1997,'Area':'Production']
df_assam_9_1997_sum = df_assam_9_1997.sum(axis = 0, skipna = True)
print(df_assam_9_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_9_1998 = df_assam_9.loc[df_assam_9['Crop_Year'] == 1998,'Area':'Production']
df_assam_9_1998_sum = df_assam_9_1998.sum(axis = 0, skipna = True) 
print(df_assam_9_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_9_1999 = df_assam_9.loc[df_assam_9['Crop_Year'] == 1999,'Area':'Production']
df_assam_9_1999_sum = df_assam_9_1999.sum(axis = 0, skipna = True) 
print(df_assam_9_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_9_2000 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2000,'Area':'Production']
df_assam_9_2000_sum = df_assam_9_2000.sum(axis = 0, skipna = True) 
print(df_assam_9_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_9_2001 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_9_2001_sum = df_assam_9_2001.sum(axis = 0, skipna = True)
print(df_assam_9_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_9_2002 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2002,'Area':'Production']
df_assam_9_2002_sum = df_assam_9_2002.sum(axis = 0, skipna = True) 
print(df_assam_9_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_9_2003 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2003,'Area':'Production']
df_assam_9_2003_sum = df_assam_9_2003.sum(axis = 0, skipna = True) 
print(df_assam_9_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_9_2004 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2004,'Area':'Production']
df_assam_9_2004_sum = df_assam_9_2004.sum(axis = 0, skipna = True) 
print(df_assam_9_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_9_2005 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2005,'Area':'Production']
df_assam_9_2005_sum = df_assam_9_2005.sum(axis = 0, skipna = True) 
print(df_assam_9_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_9_2006 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_9_2006_sum = df_assam_9_2006.sum(axis = 0, skipna = True)
print(df_assam_9_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_9_2007 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2007,'Area':'Production']
df_assam_9_2007_sum = df_assam_9_2007.sum(axis = 0, skipna = True) 
print(df_assam_9_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_9_2008 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2008,'Area':'Production']
df_assam_9_2008_sum = df_assam_9_2008.sum(axis = 0, skipna = True) 
print(df_assam_9_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_9_2009 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2009,'Area':'Production']
df_assam_9_2009_sum = df_assam_9_2009.sum(axis = 0, skipna = True) 
print(df_assam_9_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_9_2010 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_9_2010_sum = df_assam_9_2010.sum(axis = 0, skipna = True)
print(df_assam_9_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_9_2011 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_9_2011_sum = df_assam_9_2011.sum(axis = 0, skipna = True)
print(df_assam_9_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_9_2012 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2012,'Area':'Production']
df_assam_9_2012_sum = df_assam_9_2012.sum(axis = 0, skipna = True) 
print(df_assam_9_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_9_2013 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_9_2013_sum = df_assam_9_2013.sum(axis = 0, skipna = True)
print(df_assam_9_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_9_2014 = df_assam_9.loc[df_assam_9['Crop_Year'] == 2014,'Area':'Production']
df_assam_9_2014_sum = df_assam_9_2014.sum(axis = 0, skipna = True) 
print(df_assam_9_2014_sum)
print("---------------------------------")
                  
# details of assam : [10] DIMA HASAO

print(" --- Details of assam : [10] DIMA HASAO -----")
df_assam_10 = df_assam[df_assam.District_Name == 'DIMA HASAO']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_10_1997 = df_assam_10.loc[df_assam_10['Crop_Year'] == 1997,'Area':'Production']
df_assam_10_1997_sum = df_assam_10_1997.sum(axis = 0, skipna = True)
print(df_assam_10_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_10_1998 = df_assam_10.loc[df_assam_10['Crop_Year'] == 1998,'Area':'Production']
df_assam_10_1998_sum = df_assam_10_1998.sum(axis = 0, skipna = True) 
print(df_assam_10_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_10_1999 = df_assam_10.loc[df_assam_10['Crop_Year'] == 1999,'Area':'Production']
df_assam_10_1999_sum = df_assam_10_1999.sum(axis = 0, skipna = True) 
print(df_assam_10_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_10_2000 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2000,'Area':'Production']
df_assam_10_2000_sum = df_assam_10_2000.sum(axis = 0, skipna = True) 
print(df_assam_10_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_10_2001 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_10_2001_sum = df_assam_10_2001.sum(axis = 0, skipna = True)
print(df_assam_10_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_10_2002 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2002,'Area':'Production']
df_assam_10_2002_sum = df_assam_10_2002.sum(axis = 0, skipna = True) 
print(df_assam_10_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_10_2003 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2003,'Area':'Production']
df_assam_10_2003_sum = df_assam_10_2003.sum(axis = 0, skipna = True) 
print(df_assam_10_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_10_2004 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2004,'Area':'Production']
df_assam_10_2004_sum = df_assam_10_2004.sum(axis = 0, skipna = True) 
print(df_assam_10_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_10_2005 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2005,'Area':'Production']
df_assam_10_2005_sum = df_assam_10_2005.sum(axis = 0, skipna = True) 
print(df_assam_10_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_10_2006 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_10_2006_sum = df_assam_10_2006.sum(axis = 0, skipna = True)
print(df_assam_10_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_10_2007 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2007,'Area':'Production']
df_assam_10_2007_sum = df_assam_10_2007.sum(axis = 0, skipna = True) 
print(df_assam_10_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_10_2008 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2008,'Area':'Production']
df_assam_10_2008_sum = df_assam_10_2008.sum(axis = 0, skipna = True) 
print(df_assam_10_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_10_2009 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2009,'Area':'Production']
df_assam_10_2009_sum = df_assam_10_2009.sum(axis = 0, skipna = True) 
print(df_assam_10_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_10_2010 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_10_2010_sum = df_assam_10_2010.sum(axis = 0, skipna = True)
print(df_assam_10_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_10_2011 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_10_2011_sum = df_assam_10_2011.sum(axis = 0, skipna = True)
print(df_assam_10_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_10_2012 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2012,'Area':'Production']
df_assam_10_2012_sum = df_assam_10_2012.sum(axis = 0, skipna = True) 
print(df_assam_10_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_10_2013 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_10_2013_sum = df_assam_10_2013.sum(axis = 0, skipna = True)
print(df_assam_10_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_10_2014 = df_assam_10.loc[df_assam_10['Crop_Year'] == 2014,'Area':'Production']
df_assam_10_2014_sum = df_assam_10_2014.sum(axis = 0, skipna = True) 
print(df_assam_10_2014_sum)
print("---------------------------------")
       
# details of assam : [11] GOALPARA

print("---- Details of assam : [11] GOALPARA -----")
df_assam_11 = df_assam[df_assam.District_Name == 'GOALPARA']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_11_1997 = df_assam_11.loc[df_assam_11['Crop_Year'] == 1997,'Area':'Production']
df_assam_11_1997_sum = df_assam_11_1997.sum(axis = 0, skipna = True)
print(df_assam_11_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_11_1998 = df_assam_11.loc[df_assam_11['Crop_Year'] == 1998,'Area':'Production']
df_assam_11_1998_sum = df_assam_11_1998.sum(axis = 0, skipna = True) 
print(df_assam_11_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_11_1999 = df_assam_11.loc[df_assam_11['Crop_Year'] == 1999,'Area':'Production']
df_assam_11_1999_sum = df_assam_11_1999.sum(axis = 0, skipna = True) 
print(df_assam_11_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_11_2000 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2000,'Area':'Production']
df_assam_11_2000_sum = df_assam_11_2000.sum(axis = 0, skipna = True) 
print(df_assam_11_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_11_2001 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_11_2001_sum = df_assam_11_2001.sum(axis = 0, skipna = True)
print(df_assam_11_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_11_2002 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2002,'Area':'Production']
df_assam_11_2002_sum = df_assam_11_2002.sum(axis = 0, skipna = True) 
print(df_assam_11_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_11_2003 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2003,'Area':'Production']
df_assam_11_2003_sum = df_assam_11_2003.sum(axis = 0, skipna = True) 
print(df_assam_11_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_11_2004 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2004,'Area':'Production']
df_assam_11_2004_sum = df_assam_11_2004.sum(axis = 0, skipna = True) 
print(df_assam_11_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_11_2005 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2005,'Area':'Production']
df_assam_11_2005_sum = df_assam_11_2005.sum(axis = 0, skipna = True) 
print(df_assam_11_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_11_2006 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_11_2006_sum = df_assam_11_2006.sum(axis = 0, skipna = True)
print(df_assam_11_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_11_2007 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2007,'Area':'Production']
df_assam_11_2007_sum = df_assam_11_2007.sum(axis = 0, skipna = True) 
print(df_assam_11_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_11_2008 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2008,'Area':'Production']
df_assam_11_2008_sum = df_assam_11_2008.sum(axis = 0, skipna = True) 
print(df_assam_11_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_11_2009 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2009,'Area':'Production']
df_assam_11_2009_sum = df_assam_11_2009.sum(axis = 0, skipna = True) 
print(df_assam_11_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_11_2010 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_11_2010_sum = df_assam_11_2010.sum(axis = 0, skipna = True)
print(df_assam_11_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_11_2011 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_11_2011_sum = df_assam_11_2011.sum(axis = 0, skipna = True)
print(df_assam_11_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_11_2012 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2012,'Area':'Production']
df_assam_11_2012_sum = df_assam_11_2012.sum(axis = 0, skipna = True) 
print(df_assam_11_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_11_2013 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_11_2013_sum = df_assam_11_2013.sum(axis = 0, skipna = True)
print(df_assam_11_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_11_2014 = df_assam_11.loc[df_assam_11['Crop_Year'] == 2014,'Area':'Production']
df_assam_11_2014_sum = df_assam_11_2014.sum(axis = 0, skipna = True) 
print(df_assam_11_2014_sum)
print("---------------------------------")
                   
# details of assam : [12] GOLAGHAT

print("---- Details of assam : [12] GOLAGHAT ----")
df_assam_12 = df_assam[df_assam.District_Name == 'GOLAGHAT']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_12_1997 = df_assam_12.loc[df_assam_12['Crop_Year'] == 1997,'Area':'Production']
df_assam_12_1997_sum = df_assam_12_1997.sum(axis = 0, skipna = True)
print(df_assam_12_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_12_1998 = df_assam_12.loc[df_assam_12['Crop_Year'] == 1998,'Area':'Production']
df_assam_12_1998_sum = df_assam_12_1998.sum(axis = 0, skipna = True) 
print(df_assam_12_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_12_1999 = df_assam_12.loc[df_assam_12['Crop_Year'] == 1999,'Area':'Production']
df_assam_12_1999_sum = df_assam_12_1999.sum(axis = 0, skipna = True) 
print(df_assam_12_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_12_2000 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2000,'Area':'Production']
df_assam_12_2000_sum = df_assam_12_2000.sum(axis = 0, skipna = True) 
print(df_assam_12_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_12_2001 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_12_2001_sum = df_assam_12_2001.sum(axis = 0, skipna = True)
print(df_assam_12_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_12_2002 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2002,'Area':'Production']
df_assam_12_2002_sum = df_assam_12_2002.sum(axis = 0, skipna = True) 
print(df_assam_12_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_12_2003 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2003,'Area':'Production']
df_assam_12_2003_sum = df_assam_12_2003.sum(axis = 0, skipna = True) 
print(df_assam_12_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_12_2004 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2004,'Area':'Production']
df_assam_12_2004_sum = df_assam_12_2004.sum(axis = 0, skipna = True) 
print(df_assam_12_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_12_2005 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2005,'Area':'Production']
df_assam_12_2005_sum = df_assam_12_2005.sum(axis = 0, skipna = True) 
print(df_assam_12_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_12_2006 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_12_2006_sum = df_assam_12_2006.sum(axis = 0, skipna = True)
print(df_assam_12_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_12_2007 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2007,'Area':'Production']
df_assam_12_2007_sum = df_assam_12_2007.sum(axis = 0, skipna = True) 
print(df_assam_12_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_12_2008 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2008,'Area':'Production']
df_assam_12_2008_sum = df_assam_12_2008.sum(axis = 0, skipna = True) 
print(df_assam_12_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_12_2009 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2009,'Area':'Production']
df_assam_12_2009_sum = df_assam_12_2009.sum(axis = 0, skipna = True) 
print(df_assam_12_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_12_2010 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_12_2010_sum = df_assam_12_2010.sum(axis = 0, skipna = True)
print(df_assam_12_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_12_2011 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_12_2011_sum = df_assam_12_2011.sum(axis = 0, skipna = True)
print(df_assam_12_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_12_2012 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2012,'Area':'Production']
df_assam_12_2012_sum = df_assam_12_2012.sum(axis = 0, skipna = True) 
print(df_assam_12_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_12_2013 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_12_2013_sum = df_assam_12_2013.sum(axis = 0, skipna = True)
print(df_assam_12_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_12_2014 = df_assam_12.loc[df_assam_12['Crop_Year'] == 2014,'Area':'Production']
df_assam_12_2014_sum = df_assam_12_2014.sum(axis = 0, skipna = True) 
print(df_assam_12_2014_sum)
print("---------------------------------")
                        
# details of assam : [13] HAILAKANDI 

print("---- Details of assam : [13] HAILAKANDI  --------")
df_assam_13 = df_assam[df_assam.District_Name == 'HAILAKANDI']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_13_1997 = df_assam_13.loc[df_assam_13['Crop_Year'] == 1997,'Area':'Production']
df_assam_13_1997_sum = df_assam_13_1997.sum(axis = 0, skipna = True)
print(df_assam_13_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_13_1998 = df_assam_13.loc[df_assam_13['Crop_Year'] == 1998,'Area':'Production']
df_assam_13_1998_sum = df_assam_13_1998.sum(axis = 0, skipna = True) 
print(df_assam_13_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_13_1999 = df_assam_13.loc[df_assam_13['Crop_Year'] == 1999,'Area':'Production']
df_assam_13_1999_sum = df_assam_13_1999.sum(axis = 0, skipna = True) 
print(df_assam_13_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_13_2000 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2000,'Area':'Production']
df_assam_13_2000_sum = df_assam_13_2000.sum(axis = 0, skipna = True) 
print(df_assam_13_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_13_2001 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_13_2001_sum = df_assam_13_2001.sum(axis = 0, skipna = True)
print(df_assam_13_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_13_2002 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2002,'Area':'Production']
df_assam_13_2002_sum = df_assam_13_2002.sum(axis = 0, skipna = True) 
print(df_assam_13_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_13_2003 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2003,'Area':'Production']
df_assam_13_2003_sum = df_assam_13_2003.sum(axis = 0, skipna = True) 
print(df_assam_13_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_13_2004 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2004,'Area':'Production']
df_assam_13_2004_sum = df_assam_13_2004.sum(axis = 0, skipna = True) 
print(df_assam_13_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_13_2005 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2005,'Area':'Production']
df_assam_13_2005_sum = df_assam_13_2005.sum(axis = 0, skipna = True) 
print(df_assam_13_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_13_2006 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_13_2006_sum = df_assam_13_2006.sum(axis = 0, skipna = True)
print(df_assam_13_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_13_2007 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2007,'Area':'Production']
df_assam_13_2007_sum = df_assam_13_2007.sum(axis = 0, skipna = True) 
print(df_assam_13_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_13_2008 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2008,'Area':'Production']
df_assam_13_2008_sum = df_assam_13_2008.sum(axis = 0, skipna = True) 
print(df_assam_13_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_13_2009 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2009,'Area':'Production']
df_assam_13_2009_sum = df_assam_13_2009.sum(axis = 0, skipna = True) 
print(df_assam_13_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_13_2010 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_13_2010_sum = df_assam_13_2010.sum(axis = 0, skipna = True)
print(df_assam_13_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_13_2011 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_13_2011_sum = df_assam_13_2011.sum(axis = 0, skipna = True)
print(df_assam_13_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_13_2012 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2012,'Area':'Production']
df_assam_13_2012_sum = df_assam_13_2012.sum(axis = 0, skipna = True) 
print(df_assam_13_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_13_2013 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_13_2013_sum = df_assam_13_2013.sum(axis = 0, skipna = True)
print(df_assam_13_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_13_2014 = df_assam_13.loc[df_assam_13['Crop_Year'] == 2014,'Area':'Production']
df_assam_13_2014_sum = df_assam_13_2014.sum(axis = 0, skipna = True) 
print(df_assam_13_2014_sum)
print("---------------------------------")

# details of assam : [14] JORHAT

print("---- Details of assam : [14] JORHAT --------")
df_assam_14 = df_assam[df_assam.District_Name == 'JORHAT']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_14_1997 = df_assam_14.loc[df_assam_14['Crop_Year'] == 1997,'Area':'Production']
df_assam_14_1997_sum = df_assam_14_1997.sum(axis = 0, skipna = True)
print(df_assam_14_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_14_1998 = df_assam_14.loc[df_assam_14['Crop_Year'] == 1998,'Area':'Production']
df_assam_14_1998_sum = df_assam_14_1998.sum(axis = 0, skipna = True) 
print(df_assam_14_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_14_1999 = df_assam_14.loc[df_assam_14['Crop_Year'] == 1999,'Area':'Production']
df_assam_14_1999_sum = df_assam_14_1999.sum(axis = 0, skipna = True) 
print(df_assam_14_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_14_2000 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2000,'Area':'Production']
df_assam_14_2000_sum = df_assam_14_2000.sum(axis = 0, skipna = True) 
print(df_assam_14_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_14_2001 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_14_2001_sum = df_assam_14_2001.sum(axis = 0, skipna = True)
print(df_assam_14_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_14_2002 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2002,'Area':'Production']
df_assam_14_2002_sum = df_assam_14_2002.sum(axis = 0, skipna = True) 
print(df_assam_14_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_14_2003 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2003,'Area':'Production']
df_assam_14_2003_sum = df_assam_14_2003.sum(axis = 0, skipna = True) 
print(df_assam_14_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_14_2004 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2004,'Area':'Production']
df_assam_14_2004_sum = df_assam_14_2004.sum(axis = 0, skipna = True) 
print(df_assam_14_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_14_2005 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2005,'Area':'Production']
df_assam_14_2005_sum = df_assam_14_2005.sum(axis = 0, skipna = True) 
print(df_assam_14_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_14_2006 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_14_2006_sum = df_assam_14_2006.sum(axis = 0, skipna = True)
print(df_assam_14_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_14_2007 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2007,'Area':'Production']
df_assam_14_2007_sum = df_assam_14_2007.sum(axis = 0, skipna = True) 
print(df_assam_14_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_14_2008 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2008,'Area':'Production']
df_assam_14_2008_sum = df_assam_14_2008.sum(axis = 0, skipna = True) 
print(df_assam_14_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_14_2009 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2009,'Area':'Production']
df_assam_14_2009_sum = df_assam_14_2009.sum(axis = 0, skipna = True) 
print(df_assam_14_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_14_2010 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_14_2010_sum = df_assam_14_2010.sum(axis = 0, skipna = True)
print(df_assam_14_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_14_2011 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_14_2011_sum = df_assam_14_2011.sum(axis = 0, skipna = True)
print(df_assam_14_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_14_2012 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2012,'Area':'Production']
df_assam_14_2012_sum = df_assam_14_2012.sum(axis = 0, skipna = True) 
print(df_assam_14_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_14_2013 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_14_2013_sum = df_assam_14_2013.sum(axis = 0, skipna = True)
print(df_assam_14_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_14_2014 = df_assam_14.loc[df_assam_14['Crop_Year'] == 2014,'Area':'Production']
df_assam_14_2014_sum = df_assam_14_2014.sum(axis = 0, skipna = True) 
print(df_assam_14_2014_sum)
print("---------------------------------")
                                    
# details of assam : [15] KAMRUP

print("---- Details of assam : [15] KAMRUP -----")
df_assam_15 = df_assam[df_assam.District_Name == 'KAMRUP']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_15_1997 = df_assam_15.loc[df_assam_15['Crop_Year'] == 1997,'Area':'Production']
df_assam_15_1997_sum = df_assam_15_1997.sum(axis = 0, skipna = True)
print(df_assam_15_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_15_1998 = df_assam_15.loc[df_assam_15['Crop_Year'] == 1998,'Area':'Production']
df_assam_15_1998_sum = df_assam_15_1998.sum(axis = 0, skipna = True) 
print(df_assam_15_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_15_1999 = df_assam_15.loc[df_assam_15['Crop_Year'] == 1999,'Area':'Production']
df_assam_15_1999_sum = df_assam_15_1999.sum(axis = 0, skipna = True) 
print(df_assam_15_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_15_2000 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2000,'Area':'Production']
df_assam_15_2000_sum = df_assam_15_2000.sum(axis = 0, skipna = True) 
print(df_assam_15_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_15_2001 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_15_2001_sum = df_assam_15_2001.sum(axis = 0, skipna = True)
print(df_assam_15_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_15_2002 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2002,'Area':'Production']
df_assam_15_2002_sum = df_assam_15_2002.sum(axis = 0, skipna = True) 
print(df_assam_15_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_15_2003 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2003,'Area':'Production']
df_assam_15_2003_sum = df_assam_15_2003.sum(axis = 0, skipna = True) 
print(df_assam_15_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_15_2004 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2004,'Area':'Production']
df_assam_15_2004_sum = df_assam_15_2004.sum(axis = 0, skipna = True) 
print(df_assam_15_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_15_2005 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2005,'Area':'Production']
df_assam_15_2005_sum = df_assam_15_2005.sum(axis = 0, skipna = True) 
print(df_assam_15_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_15_2006 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_15_2006_sum = df_assam_15_2006.sum(axis = 0, skipna = True)
print(df_assam_15_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_15_2007 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2007,'Area':'Production']
df_assam_15_2007_sum = df_assam_15_2007.sum(axis = 0, skipna = True) 
print(df_assam_15_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_15_2008 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2008,'Area':'Production']
df_assam_15_2008_sum = df_assam_15_2008.sum(axis = 0, skipna = True) 
print(df_assam_15_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_15_2009 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2009,'Area':'Production']
df_assam_15_2009_sum = df_assam_15_2009.sum(axis = 0, skipna = True) 
print(df_assam_15_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_15_2010 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_15_2010_sum = df_assam_15_2010.sum(axis = 0, skipna = True)
print(df_assam_15_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_15_2011 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_15_2011_sum = df_assam_15_2011.sum(axis = 0, skipna = True)
print(df_assam_15_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_15_2012 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2012,'Area':'Production']
df_assam_15_2012_sum = df_assam_15_2012.sum(axis = 0, skipna = True) 
print(df_assam_15_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_15_2013 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_15_2013_sum = df_assam_15_2013.sum(axis = 0, skipna = True)
print(df_assam_15_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_15_2014 = df_assam_15.loc[df_assam_15['Crop_Year'] == 2014,'Area':'Production']
df_assam_15_2014_sum = df_assam_15_2014.sum(axis = 0, skipna = True) 
print(df_assam_15_2014_sum)
print("---------------------------------")
                               
# details of assam : [16] KAMRUP METRO 

print("----- Details of assam : [16] KAMRUP METRO ----")
df_assam_16 = df_assam[df_assam.District_Name == 'KAMRUP METRO']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_16_1997 = df_assam_16.loc[df_assam_16['Crop_Year'] == 1997,'Area':'Production']
df_assam_16_1997_sum = df_assam_16_1997.sum(axis = 0, skipna = True)
print(df_assam_16_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_16_1998 = df_assam_16.loc[df_assam_16['Crop_Year'] == 1998,'Area':'Production']
df_assam_16_1998_sum = df_assam_16_1998.sum(axis = 0, skipna = True) 
print(df_assam_16_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_16_1999 = df_assam_16.loc[df_assam_16['Crop_Year'] == 1999,'Area':'Production']
df_assam_16_1999_sum = df_assam_16_1999.sum(axis = 0, skipna = True) 
print(df_assam_16_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_16_2000 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2000,'Area':'Production']
df_assam_16_2000_sum = df_assam_16_2000.sum(axis = 0, skipna = True) 
print(df_assam_16_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_16_2001 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_16_2001_sum = df_assam_16_2001.sum(axis = 0, skipna = True)
print(df_assam_16_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_16_2002 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2002,'Area':'Production']
df_assam_16_2002_sum = df_assam_16_2002.sum(axis = 0, skipna = True) 
print(df_assam_16_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_16_2003 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2003,'Area':'Production']
df_assam_16_2003_sum = df_assam_16_2003.sum(axis = 0, skipna = True) 
print(df_assam_16_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_16_2004 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2004,'Area':'Production']
df_assam_16_2004_sum = df_assam_16_2004.sum(axis = 0, skipna = True) 
print(df_assam_16_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_16_2005 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2005,'Area':'Production']
df_assam_16_2005_sum = df_assam_16_2005.sum(axis = 0, skipna = True) 
print(df_assam_16_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_16_2006 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_16_2006_sum = df_assam_16_2006.sum(axis = 0, skipna = True)
print(df_assam_16_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_16_2007 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2007,'Area':'Production']
df_assam_16_2007_sum = df_assam_16_2007.sum(axis = 0, skipna = True) 
print(df_assam_16_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_16_2008 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2008,'Area':'Production']
df_assam_16_2008_sum = df_assam_16_2008.sum(axis = 0, skipna = True) 
print(df_assam_16_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_16_2009 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2009,'Area':'Production']
df_assam_16_2009_sum = df_assam_16_2009.sum(axis = 0, skipna = True) 
print(df_assam_16_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_16_2010 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_16_2010_sum = df_assam_16_2010.sum(axis = 0, skipna = True)
print(df_assam_16_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_16_2011 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_16_2011_sum = df_assam_16_2011.sum(axis = 0, skipna = True)
print(df_assam_16_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_16_2012 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2012,'Area':'Production']
df_assam_16_2012_sum = df_assam_16_2012.sum(axis = 0, skipna = True) 
print(df_assam_16_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_16_2013 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_16_2013_sum = df_assam_16_2013.sum(axis = 0, skipna = True)
print(df_assam_16_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_16_2014 = df_assam_16.loc[df_assam_16['Crop_Year'] == 2014,'Area':'Production']
df_assam_16_2014_sum = df_assam_16_2014.sum(axis = 0, skipna = True) 
print(df_assam_16_2014_sum)
print("---------------------------------")
   
# details of assam : [17] KARBI ANGLONG

print("---- Details of assam : [17] KARBI ANGLONG -----")
df_assam_17 = df_assam[df_assam.District_Name == 'KARBI ANGLONG']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_17_1997 = df_assam_17.loc[df_assam_17['Crop_Year'] == 1997,'Area':'Production']
df_assam_17_1997_sum = df_assam_17_1997.sum(axis = 0, skipna = True)
print(df_assam_17_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_17_1998 = df_assam_17.loc[df_assam_17['Crop_Year'] == 1998,'Area':'Production']
df_assam_17_1998_sum = df_assam_17_1998.sum(axis = 0, skipna = True) 
print(df_assam_17_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_17_1999 = df_assam_17.loc[df_assam_17['Crop_Year'] == 1999,'Area':'Production']
df_assam_17_1999_sum = df_assam_17_1999.sum(axis = 0, skipna = True) 
print(df_assam_17_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_17_2000 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2000,'Area':'Production']
df_assam_17_2000_sum = df_assam_17_2000.sum(axis = 0, skipna = True) 
print(df_assam_17_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_17_2001 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_17_2001_sum = df_assam_17_2001.sum(axis = 0, skipna = True)
print(df_assam_17_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_17_2002 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2002,'Area':'Production']
df_assam_17_2002_sum = df_assam_17_2002.sum(axis = 0, skipna = True) 
print(df_assam_17_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_17_2003 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2003,'Area':'Production']
df_assam_17_2003_sum = df_assam_17_2003.sum(axis = 0, skipna = True) 
print(df_assam_17_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_17_2004 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2004,'Area':'Production']
df_assam_17_2004_sum = df_assam_17_2004.sum(axis = 0, skipna = True) 
print(df_assam_17_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_17_2005 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2005,'Area':'Production']
df_assam_17_2005_sum = df_assam_17_2005.sum(axis = 0, skipna = True) 
print(df_assam_17_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_17_2006 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_17_2006_sum = df_assam_17_2006.sum(axis = 0, skipna = True)
print(df_assam_17_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_17_2007 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2007,'Area':'Production']
df_assam_17_2007_sum = df_assam_17_2007.sum(axis = 0, skipna = True) 
print(df_assam_17_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_17_2008 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2008,'Area':'Production']
df_assam_17_2008_sum = df_assam_17_2008.sum(axis = 0, skipna = True) 
print(df_assam_17_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_17_2009 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2009,'Area':'Production']
df_assam_17_2009_sum = df_assam_17_2009.sum(axis = 0, skipna = True) 
print(df_assam_17_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_17_2010 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_17_2010_sum = df_assam_17_2010.sum(axis = 0, skipna = True)
print(df_assam_17_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_17_2011 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_17_2011_sum = df_assam_17_2011.sum(axis = 0, skipna = True)
print(df_assam_17_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_17_2012 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2012,'Area':'Production']
df_assam_17_2012_sum = df_assam_17_2012.sum(axis = 0, skipna = True) 
print(df_assam_17_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_17_2013 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_17_2013_sum = df_assam_17_2013.sum(axis = 0, skipna = True)
print(df_assam_17_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_17_2014 = df_assam_17.loc[df_assam_17['Crop_Year'] == 2014,'Area':'Production']
df_assam_17_2014_sum = df_assam_17_2014.sum(axis = 0, skipna = True) 
print(df_assam_17_2014_sum)
print("---------------------------------")
         
# details of assam : [18] KARIMGANJ 

print("---- Details of assam : [18] KARIMGANJ -----")
df_assam_18 = df_assam[df_assam.District_Name == 'KARIMGANJ']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_18_1997 = df_assam_18.loc[df_assam_18['Crop_Year'] == 1997,'Area':'Production']
df_assam_18_1997_sum = df_assam_18_1997.sum(axis = 0, skipna = True)
print(df_assam_18_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_18_1998 = df_assam_18.loc[df_assam_18['Crop_Year'] == 1998,'Area':'Production']
df_assam_18_1998_sum = df_assam_18_1998.sum(axis = 0, skipna = True) 
print(df_assam_18_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_18_1999 = df_assam_18.loc[df_assam_18['Crop_Year'] == 1999,'Area':'Production']
df_assam_18_1999_sum = df_assam_18_1999.sum(axis = 0, skipna = True) 
print(df_assam_18_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_18_2000 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2000,'Area':'Production']
df_assam_18_2000_sum = df_assam_18_2000.sum(axis = 0, skipna = True) 
print(df_assam_18_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_18_2001 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_18_2001_sum = df_assam_18_2001.sum(axis = 0, skipna = True)
print(df_assam_18_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_18_2002 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2002,'Area':'Production']
df_assam_18_2002_sum = df_assam_18_2002.sum(axis = 0, skipna = True) 
print(df_assam_18_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_18_2003 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2003,'Area':'Production']
df_assam_18_2003_sum = df_assam_18_2003.sum(axis = 0, skipna = True) 
print(df_assam_18_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_18_2004 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2004,'Area':'Production']
df_assam_18_2004_sum = df_assam_18_2004.sum(axis = 0, skipna = True) 
print(df_assam_18_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_18_2005 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2005,'Area':'Production']
df_assam_18_2005_sum = df_assam_18_2005.sum(axis = 0, skipna = True) 
print(df_assam_18_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_18_2006 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_18_2006_sum = df_assam_18_2006.sum(axis = 0, skipna = True)
print(df_assam_18_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_18_2007 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2007,'Area':'Production']
df_assam_18_2007_sum = df_assam_18_2007.sum(axis = 0, skipna = True) 
print(df_assam_18_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_18_2008 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2008,'Area':'Production']
df_assam_18_2008_sum = df_assam_18_2008.sum(axis = 0, skipna = True) 
print(df_assam_18_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_18_2009 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2009,'Area':'Production']
df_assam_18_2009_sum = df_assam_18_2009.sum(axis = 0, skipna = True) 
print(df_assam_18_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_18_2010 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_18_2010_sum = df_assam_18_2010.sum(axis = 0, skipna = True)
print(df_assam_18_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_18_2011 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_18_2011_sum = df_assam_18_2011.sum(axis = 0, skipna = True)
print(df_assam_18_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_18_2012 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2012,'Area':'Production']
df_assam_18_2012_sum = df_assam_18_2012.sum(axis = 0, skipna = True) 
print(df_assam_18_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_18_2013 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_18_2013_sum = df_assam_18_2013.sum(axis = 0, skipna = True)
print(df_assam_18_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_18_2014 = df_assam_18.loc[df_assam_18['Crop_Year'] == 2014,'Area':'Production']
df_assam_18_2014_sum = df_assam_18_2014.sum(axis = 0, skipna = True) 
print(df_assam_18_2014_sum)
print("---------------------------------")
                   
# details of assam : [19] KOKRAJHAR 

print("---- Details of assam : [19] KOKRAJHAR ------")
df_assam_19 = df_assam[df_assam.District_Name == 'KOKRAJHAR']
        
# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_19_1997 = df_assam_19.loc[df_assam_19['Crop_Year'] == 1997,'Area':'Production']
df_assam_19_1997_sum = df_assam_19_1997.sum(axis = 0, skipna = True)
print(df_assam_19_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_19_1998 = df_assam_19.loc[df_assam_19['Crop_Year'] == 1998,'Area':'Production']
df_assam_19_1998_sum = df_assam_19_1998.sum(axis = 0, skipna = True) 
print(df_assam_19_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_19_1999 = df_assam_19.loc[df_assam_19['Crop_Year'] == 1999,'Area':'Production']
df_assam_19_1999_sum = df_assam_19_1999.sum(axis = 0, skipna = True) 
print(df_assam_19_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_19_2000 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2000,'Area':'Production']
df_assam_19_2000_sum = df_assam_19_2000.sum(axis = 0, skipna = True) 
print(df_assam_19_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_19_2001 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_19_2001_sum = df_assam_19_2001.sum(axis = 0, skipna = True)
print(df_assam_19_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_19_2002 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2002,'Area':'Production']
df_assam_19_2002_sum = df_assam_19_2002.sum(axis = 0, skipna = True) 
print(df_assam_19_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_19_2003 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2003,'Area':'Production']
df_assam_19_2003_sum = df_assam_19_2003.sum(axis = 0, skipna = True) 
print(df_assam_19_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_19_2004 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2004,'Area':'Production']
df_assam_19_2004_sum = df_assam_19_2004.sum(axis = 0, skipna = True) 
print(df_assam_19_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_19_2005 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2005,'Area':'Production']
df_assam_19_2005_sum = df_assam_19_2005.sum(axis = 0, skipna = True) 
print(df_assam_19_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_19_2006 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_19_2006_sum = df_assam_19_2006.sum(axis = 0, skipna = True)
print(df_assam_19_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_19_2007 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2007,'Area':'Production']
df_assam_19_2007_sum = df_assam_19_2007.sum(axis = 0, skipna = True) 
print(df_assam_19_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_19_2008 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2008,'Area':'Production']
df_assam_19_2008_sum = df_assam_19_2008.sum(axis = 0, skipna = True) 
print(df_assam_19_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_19_2009 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2009,'Area':'Production']
df_assam_19_2009_sum = df_assam_19_2009.sum(axis = 0, skipna = True) 
print(df_assam_19_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_19_2010 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_19_2010_sum = df_assam_19_2010.sum(axis = 0, skipna = True)
print(df_assam_19_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_19_2011 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_19_2011_sum = df_assam_19_2011.sum(axis = 0, skipna = True)
print(df_assam_19_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_19_2012 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2012,'Area':'Production']
df_assam_19_2012_sum = df_assam_19_2012.sum(axis = 0, skipna = True) 
print(df_assam_19_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_19_2013 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_19_2013_sum = df_assam_19_2013.sum(axis = 0, skipna = True)
print(df_assam_19_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_19_2014 = df_assam_19.loc[df_assam_19['Crop_Year'] == 2014,'Area':'Production']
df_assam_19_2014_sum = df_assam_19_2014.sum(axis = 0, skipna = True) 
print(df_assam_19_2014_sum)
print("---------------------------------")
                                                                  
# details of assam : [20] LAKHIMPUR 

print("---- Details of assam : [20] LAKHIMPUR ------")
df_assam_20 = df_assam[df_assam.District_Name == 'LAKHIMPUR']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_20_1997 = df_assam_20.loc[df_assam_20['Crop_Year'] == 1997,'Area':'Production']
df_assam_20_1997_sum = df_assam_20_1997.sum(axis = 0, skipna = True)
print(df_assam_20_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_20_1998 = df_assam_20.loc[df_assam_20['Crop_Year'] == 1998,'Area':'Production']
df_assam_20_1998_sum = df_assam_20_1998.sum(axis = 0, skipna = True) 
print(df_assam_20_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_20_1999 = df_assam_20.loc[df_assam_20['Crop_Year'] == 1999,'Area':'Production']
df_assam_20_1999_sum = df_assam_20_1999.sum(axis = 0, skipna = True) 
print(df_assam_20_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_20_2000 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2000,'Area':'Production']
df_assam_20_2000_sum = df_assam_20_2000.sum(axis = 0, skipna = True) 
print(df_assam_20_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_20_2001 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_20_2001_sum = df_assam_20_2001.sum(axis = 0, skipna = True)
print(df_assam_20_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_20_2002 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2002,'Area':'Production']
df_assam_20_2002_sum = df_assam_20_2002.sum(axis = 0, skipna = True) 
print(df_assam_20_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_20_2003 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2003,'Area':'Production']
df_assam_20_2003_sum = df_assam_20_2003.sum(axis = 0, skipna = True) 
print(df_assam_20_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_20_2004 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2004,'Area':'Production']
df_assam_20_2004_sum = df_assam_20_2004.sum(axis = 0, skipna = True) 
print(df_assam_20_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_20_2005 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2005,'Area':'Production']
df_assam_20_2005_sum = df_assam_20_2005.sum(axis = 0, skipna = True) 
print(df_assam_20_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_20_2006 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_20_2006_sum = df_assam_20_2006.sum(axis = 0, skipna = True)
print(df_assam_20_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_20_2007 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2007,'Area':'Production']
df_assam_20_2007_sum = df_assam_20_2007.sum(axis = 0, skipna = True) 
print(df_assam_20_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_20_2008 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2008,'Area':'Production']
df_assam_20_2008_sum = df_assam_20_2008.sum(axis = 0, skipna = True) 
print(df_assam_20_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_20_2009 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2009,'Area':'Production']
df_assam_20_2009_sum = df_assam_20_2009.sum(axis = 0, skipna = True) 
print(df_assam_20_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_20_2010 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_20_2010_sum = df_assam_20_2010.sum(axis = 0, skipna = True)
print(df_assam_20_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_20_2011 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_20_2011_sum = df_assam_20_2011.sum(axis = 0, skipna = True)
print(df_assam_20_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_20_2012 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2012,'Area':'Production']
df_assam_20_2012_sum = df_assam_20_2012.sum(axis = 0, skipna = True) 
print(df_assam_20_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_20_2013 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_20_2013_sum = df_assam_20_2013.sum(axis = 0, skipna = True)
print(df_assam_20_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_20_2014 = df_assam_20.loc[df_assam_20['Crop_Year'] == 2014,'Area':'Production']
df_assam_20_2014_sum = df_assam_20_2014.sum(axis = 0, skipna = True) 
print(df_assam_20_2014_sum)
print("---------------------------------")
                      
# details of assam : [21] MARIGAON 

print("---- Details of assam : [21] MARIGAON ----")
df_assam_21 = df_assam[df_assam.District_Name == 'MARIGAON']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_21_1997 = df_assam_21.loc[df_assam_21['Crop_Year'] == 1997,'Area':'Production']
df_assam_21_1997_sum = df_assam_21_1997.sum(axis = 0, skipna = True)
print(df_assam_21_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_21_1998 = df_assam_21.loc[df_assam_21['Crop_Year'] == 1998,'Area':'Production']
df_assam_21_1998_sum = df_assam_21_1998.sum(axis = 0, skipna = True) 
print(df_assam_21_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_21_1999 = df_assam_21.loc[df_assam_21['Crop_Year'] == 1999,'Area':'Production']
df_assam_21_1999_sum = df_assam_21_1999.sum(axis = 0, skipna = True) 
print(df_assam_21_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_21_2000 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2000,'Area':'Production']
df_assam_21_2000_sum = df_assam_21_2000.sum(axis = 0, skipna = True) 
print(df_assam_21_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_21_2001 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_21_2001_sum = df_assam_21_2001.sum(axis = 0, skipna = True)
print(df_assam_21_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_21_2002 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2002,'Area':'Production']
df_assam_21_2002_sum = df_assam_21_2002.sum(axis = 0, skipna = True) 
print(df_assam_21_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_21_2003 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2003,'Area':'Production']
df_assam_21_2003_sum = df_assam_21_2003.sum(axis = 0, skipna = True) 
print(df_assam_21_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_21_2004 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2004,'Area':'Production']
df_assam_21_2004_sum = df_assam_21_2004.sum(axis = 0, skipna = True) 
print(df_assam_21_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_21_2005 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2005,'Area':'Production']
df_assam_21_2005_sum = df_assam_21_2005.sum(axis = 0, skipna = True) 
print(df_assam_21_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_21_2006 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_21_2006_sum = df_assam_21_2006.sum(axis = 0, skipna = True)
print(df_assam_21_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_21_2007 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2007,'Area':'Production']
df_assam_21_2007_sum = df_assam_21_2007.sum(axis = 0, skipna = True) 
print(df_assam_21_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_21_2008 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2008,'Area':'Production']
df_assam_21_2008_sum = df_assam_21_2008.sum(axis = 0, skipna = True) 
print(df_assam_21_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_21_2009 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2009,'Area':'Production']
df_assam_21_2009_sum = df_assam_21_2009.sum(axis = 0, skipna = True) 
print(df_assam_21_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_21_2010 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_21_2010_sum = df_assam_21_2010.sum(axis = 0, skipna = True)
print(df_assam_21_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_21_2011 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_21_2011_sum = df_assam_21_2011.sum(axis = 0, skipna = True)
print(df_assam_21_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_21_2012 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2012,'Area':'Production']
df_assam_21_2012_sum = df_assam_21_2012.sum(axis = 0, skipna = True) 
print(df_assam_21_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_21_2013 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_21_2013_sum = df_assam_21_2013.sum(axis = 0, skipna = True)
print(df_assam_21_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_21_2014 = df_assam_21.loc[df_assam_21['Crop_Year'] == 2014,'Area':'Production']
df_assam_21_2014_sum = df_assam_21_2014.sum(axis = 0, skipna = True) 
print(df_assam_21_2014_sum)
print("---------------------------------")
             
# details of assam : [22] NAGAON

print("------ Details of assam : [22] NAGAON ----")
df_assam_22 = df_assam[df_assam.District_Name == 'NAGAON']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_22_1997 = df_assam_22.loc[df_assam_22['Crop_Year'] == 1997,'Area':'Production']
df_assam_22_1997_sum = df_assam_22_1997.sum(axis = 0, skipna = True)
print(df_assam_22_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_22_1998 = df_assam_22.loc[df_assam_22['Crop_Year'] == 1998,'Area':'Production']
df_assam_22_1998_sum = df_assam_22_1998.sum(axis = 0, skipna = True) 
print(df_assam_22_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_22_1999 = df_assam_22.loc[df_assam_22['Crop_Year'] == 1999,'Area':'Production']
df_assam_22_1999_sum = df_assam_22_1999.sum(axis = 0, skipna = True) 
print(df_assam_22_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_22_2000 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2000,'Area':'Production']
df_assam_22_2000_sum = df_assam_22_2000.sum(axis = 0, skipna = True) 
print(df_assam_22_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_22_2001 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_22_2001_sum = df_assam_22_2001.sum(axis = 0, skipna = True)
print(df_assam_22_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_22_2002 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2002,'Area':'Production']
df_assam_22_2002_sum = df_assam_22_2002.sum(axis = 0, skipna = True) 
print(df_assam_22_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_22_2003 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2003,'Area':'Production']
df_assam_22_2003_sum = df_assam_22_2003.sum(axis = 0, skipna = True) 
print(df_assam_22_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_22_2004 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2004,'Area':'Production']
df_assam_22_2004_sum = df_assam_22_2004.sum(axis = 0, skipna = True) 
print(df_assam_22_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_22_2005 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2005,'Area':'Production']
df_assam_22_2005_sum = df_assam_22_2005.sum(axis = 0, skipna = True) 
print(df_assam_22_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_22_2006 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_22_2006_sum = df_assam_22_2006.sum(axis = 0, skipna = True)
print(df_assam_22_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_22_2007 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2007,'Area':'Production']
df_assam_22_2007_sum = df_assam_22_2007.sum(axis = 0, skipna = True) 
print(df_assam_22_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_22_2008 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2008,'Area':'Production']
df_assam_22_2008_sum = df_assam_22_2008.sum(axis = 0, skipna = True) 
print(df_assam_22_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_22_2009 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2009,'Area':'Production']
df_assam_22_2009_sum = df_assam_22_2009.sum(axis = 0, skipna = True) 
print(df_assam_22_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_22_2010 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_22_2010_sum = df_assam_22_2010.sum(axis = 0, skipna = True)
print(df_assam_22_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_22_2011 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_22_2011_sum = df_assam_22_2011.sum(axis = 0, skipna = True)
print(df_assam_22_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_22_2012 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2012,'Area':'Production']
df_assam_22_2012_sum = df_assam_22_2012.sum(axis = 0, skipna = True) 
print(df_assam_22_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_22_2013 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_22_2013_sum = df_assam_22_2013.sum(axis = 0, skipna = True)
print(df_assam_22_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_22_2014 = df_assam_22.loc[df_assam_22['Crop_Year'] == 2014,'Area':'Production']
df_assam_22_2014_sum = df_assam_22_2014.sum(axis = 0, skipna = True) 
print(df_assam_22_2014_sum)
print("---------------------------------")
                        
# details of assam : [23] NALBARI

print("---- Details of assam : [23] NALBARI ------")
df_assam_23 = df_assam[df_assam.District_Name == 'NALBARI']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_23_1997 = df_assam_23.loc[df_assam_23['Crop_Year'] == 1997,'Area':'Production']
df_assam_23_1997_sum = df_assam_23_1997.sum(axis = 0, skipna = True)
print(df_assam_23_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_23_1998 = df_assam_23.loc[df_assam_23['Crop_Year'] == 1998,'Area':'Production']
df_assam_23_1998_sum = df_assam_23_1998.sum(axis = 0, skipna = True) 
print(df_assam_23_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_23_1999 = df_assam_23.loc[df_assam_23['Crop_Year'] == 1999,'Area':'Production']
df_assam_23_1999_sum = df_assam_23_1999.sum(axis = 0, skipna = True) 
print(df_assam_23_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_23_2000 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2000,'Area':'Production']
df_assam_23_2000_sum = df_assam_23_2000.sum(axis = 0, skipna = True) 
print(df_assam_23_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_23_2001 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_23_2001_sum = df_assam_23_2001.sum(axis = 0, skipna = True)
print(df_assam_23_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_23_2002 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2002,'Area':'Production']
df_assam_23_2002_sum = df_assam_23_2002.sum(axis = 0, skipna = True) 
print(df_assam_23_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_23_2003 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2003,'Area':'Production']
df_assam_23_2003_sum = df_assam_23_2003.sum(axis = 0, skipna = True) 
print(df_assam_23_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_23_2004 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2004,'Area':'Production']
df_assam_23_2004_sum = df_assam_23_2004.sum(axis = 0, skipna = True) 
print(df_assam_23_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_23_2005 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2005,'Area':'Production']
df_assam_23_2005_sum = df_assam_23_2005.sum(axis = 0, skipna = True) 
print(df_assam_23_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_23_2006 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_23_2006_sum = df_assam_23_2006.sum(axis = 0, skipna = True)
print(df_assam_23_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_23_2007 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2007,'Area':'Production']
df_assam_23_2007_sum = df_assam_23_2007.sum(axis = 0, skipna = True) 
print(df_assam_23_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_23_2008 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2008,'Area':'Production']
df_assam_23_2008_sum = df_assam_23_2008.sum(axis = 0, skipna = True) 
print(df_assam_23_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_23_2009 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2009,'Area':'Production']
df_assam_23_2009_sum = df_assam_23_2009.sum(axis = 0, skipna = True) 
print(df_assam_23_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_23_2010 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_23_2010_sum = df_assam_23_2010.sum(axis = 0, skipna = True)
print(df_assam_23_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_23_2011 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_23_2011_sum = df_assam_23_2011.sum(axis = 0, skipna = True)
print(df_assam_23_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_23_2012 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2012,'Area':'Production']
df_assam_23_2012_sum = df_assam_23_2012.sum(axis = 0, skipna = True) 
print(df_assam_23_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_23_2013 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_23_2013_sum = df_assam_23_2013.sum(axis = 0, skipna = True)
print(df_assam_23_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_23_2014 = df_assam_23.loc[df_assam_23['Crop_Year'] == 2014,'Area':'Production']
df_assam_23_2014_sum = df_assam_23_2014.sum(axis = 0, skipna = True) 
print(df_assam_23_2014_sum)
print("---------------------------------")
                                    
# details of assam : [24] SIVASAGAR 

print("---- Details of assam : [24] SIVASAGAR ---")
df_assam_24 = df_assam[df_assam.District_Name == 'SIVASAGAR']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_24_1997 = df_assam_24.loc[df_assam_24['Crop_Year'] == 1997,'Area':'Production']
df_assam_24_1997_sum = df_assam_24_1997.sum(axis = 0, skipna = True)
print(df_assam_24_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_24_1998 = df_assam_24.loc[df_assam_24['Crop_Year'] == 1998,'Area':'Production']
df_assam_24_1998_sum = df_assam_24_1998.sum(axis = 0, skipna = True) 
print(df_assam_24_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_24_1999 = df_assam_24.loc[df_assam_24['Crop_Year'] == 1999,'Area':'Production']
df_assam_24_1999_sum = df_assam_24_1999.sum(axis = 0, skipna = True) 
print(df_assam_24_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_24_2000 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2000,'Area':'Production']
df_assam_24_2000_sum = df_assam_24_2000.sum(axis = 0, skipna = True) 
print(df_assam_24_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_24_2001 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_24_2001_sum = df_assam_24_2001.sum(axis = 0, skipna = True)
print(df_assam_24_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_24_2002 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2002,'Area':'Production']
df_assam_24_2002_sum = df_assam_24_2002.sum(axis = 0, skipna = True) 
print(df_assam_24_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_24_2003 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2003,'Area':'Production']
df_assam_24_2003_sum = df_assam_24_2003.sum(axis = 0, skipna = True) 
print(df_assam_24_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_24_2004 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2004,'Area':'Production']
df_assam_24_2004_sum = df_assam_24_2004.sum(axis = 0, skipna = True) 
print(df_assam_24_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_24_2005 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2005,'Area':'Production']
df_assam_24_2005_sum = df_assam_24_2005.sum(axis = 0, skipna = True) 
print(df_assam_24_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_24_2006 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_24_2006_sum = df_assam_24_2006.sum(axis = 0, skipna = True)
print(df_assam_24_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_24_2007 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2007,'Area':'Production']
df_assam_24_2007_sum = df_assam_24_2007.sum(axis = 0, skipna = True) 
print(df_assam_24_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_24_2008 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2008,'Area':'Production']
df_assam_24_2008_sum = df_assam_24_2008.sum(axis = 0, skipna = True) 
print(df_assam_24_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_24_2009 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2009,'Area':'Production']
df_assam_24_2009_sum = df_assam_24_2009.sum(axis = 0, skipna = True) 
print(df_assam_24_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_24_2010 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_24_2010_sum = df_assam_24_2010.sum(axis = 0, skipna = True)
print(df_assam_24_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_24_2011 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_24_2011_sum = df_assam_24_2011.sum(axis = 0, skipna = True)
print(df_assam_24_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_24_2012 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2012,'Area':'Production']
df_assam_24_2012_sum = df_assam_24_2012.sum(axis = 0, skipna = True) 
print(df_assam_24_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_24_2013 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_24_2013_sum = df_assam_24_2013.sum(axis = 0, skipna = True)
print(df_assam_24_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_24_2014 = df_assam_24.loc[df_assam_24['Crop_Year'] == 2014,'Area':'Production']
df_assam_24_2014_sum = df_assam_24_2014.sum(axis = 0, skipna = True) 
print(df_assam_24_2014_sum)
print("---------------------------------")
                              
# details of assam : [25] SONITPUR  

print("----- Details of assam : [25] SONITPUR ----")
df_assam_25 = df_assam[df_assam.District_Name == 'SONITPUR']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_25_1997 = df_assam_25.loc[df_assam_25['Crop_Year'] == 1997,'Area':'Production']
df_assam_25_1997_sum = df_assam_25_1997.sum(axis = 0, skipna = True)
print(df_assam_25_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_25_1998 = df_assam_25.loc[df_assam_25['Crop_Year'] == 1998,'Area':'Production']
df_assam_25_1998_sum = df_assam_25_1998.sum(axis = 0, skipna = True) 
print(df_assam_25_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_25_1999 = df_assam_25.loc[df_assam_25['Crop_Year'] == 1999,'Area':'Production']
df_assam_25_1999_sum = df_assam_25_1999.sum(axis = 0, skipna = True) 
print(df_assam_25_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_25_2000 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2000,'Area':'Production']
df_assam_25_2000_sum = df_assam_25_2000.sum(axis = 0, skipna = True) 
print(df_assam_25_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_25_2001 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_25_2001_sum = df_assam_25_2001.sum(axis = 0, skipna = True)
print(df_assam_25_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_25_2002 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2002,'Area':'Production']
df_assam_25_2002_sum = df_assam_25_2002.sum(axis = 0, skipna = True) 
print(df_assam_25_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_25_2003 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2003,'Area':'Production']
df_assam_25_2003_sum = df_assam_25_2003.sum(axis = 0, skipna = True) 
print(df_assam_25_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_25_2004 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2004,'Area':'Production']
df_assam_25_2004_sum = df_assam_25_2004.sum(axis = 0, skipna = True) 
print(df_assam_25_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_25_2005 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2005,'Area':'Production']
df_assam_25_2005_sum = df_assam_25_2005.sum(axis = 0, skipna = True) 
print(df_assam_25_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_25_2006 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_25_2006_sum = df_assam_25_2006.sum(axis = 0, skipna = True)
print(df_assam_25_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_25_2007 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2007,'Area':'Production']
df_assam_25_2007_sum = df_assam_25_2007.sum(axis = 0, skipna = True) 
print(df_assam_25_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_25_2008 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2008,'Area':'Production']
df_assam_25_2008_sum = df_assam_25_2008.sum(axis = 0, skipna = True) 
print(df_assam_25_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_25_2009 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2009,'Area':'Production']
df_assam_25_2009_sum = df_assam_25_2009.sum(axis = 0, skipna = True) 
print(df_assam_25_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_25_2010 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_25_2010_sum = df_assam_25_2010.sum(axis = 0, skipna = True)
print(df_assam_25_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_25_2011 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_25_2011_sum = df_assam_25_2011.sum(axis = 0, skipna = True)
print(df_assam_25_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_25_2012 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2012,'Area':'Production']
df_assam_25_2012_sum = df_assam_25_2012.sum(axis = 0, skipna = True) 
print(df_assam_25_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_25_2013 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_25_2013_sum = df_assam_25_2013.sum(axis = 0, skipna = True)
print(df_assam_25_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_25_2014 = df_assam_25.loc[df_assam_25['Crop_Year'] == 2014,'Area':'Production']
df_assam_25_2014_sum = df_assam_25_2014.sum(axis = 0, skipna = True) 
print(df_assam_25_2014_sum)
print("---------------------------------")
            
# details of assam : [26] TINSUKIA

print("--- Details of assam : [26] TINSUKIA ---")
df_assam_26 = df_assam[df_assam.District_Name == 'TINSUKIA']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_26_1997 = df_assam_26.loc[df_assam_26['Crop_Year'] == 1997,'Area':'Production']
df_assam_26_1997_sum = df_assam_26_1997.sum(axis = 0, skipna = True)
print(df_assam_26_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_26_1998 = df_assam_26.loc[df_assam_26['Crop_Year'] == 1998,'Area':'Production']
df_assam_26_1998_sum = df_assam_26_1998.sum(axis = 0, skipna = True) 
print(df_assam_26_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_26_1999 = df_assam_26.loc[df_assam_26['Crop_Year'] == 1999,'Area':'Production']
df_assam_26_1999_sum = df_assam_26_1999.sum(axis = 0, skipna = True) 
print(df_assam_26_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_26_2000 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2000,'Area':'Production']
df_assam_26_2000_sum = df_assam_26_2000.sum(axis = 0, skipna = True) 
print(df_assam_26_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_26_2001 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_26_2001_sum = df_assam_26_2001.sum(axis = 0, skipna = True)
print(df_assam_26_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_26_2002 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2002,'Area':'Production']
df_assam_26_2002_sum = df_assam_26_2002.sum(axis = 0, skipna = True) 
print(df_assam_26_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_26_2003 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2003,'Area':'Production']
df_assam_26_2003_sum = df_assam_26_2003.sum(axis = 0, skipna = True) 
print(df_assam_26_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_26_2004 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2004,'Area':'Production']
df_assam_26_2004_sum = df_assam_26_2004.sum(axis = 0, skipna = True) 
print(df_assam_26_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_26_2005 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2005,'Area':'Production']
df_assam_26_2005_sum = df_assam_26_2005.sum(axis = 0, skipna = True) 
print(df_assam_26_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_26_2006 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_26_2006_sum = df_assam_26_2006.sum(axis = 0, skipna = True)
print(df_assam_26_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_26_2007 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2007,'Area':'Production']
df_assam_26_2007_sum = df_assam_26_2007.sum(axis = 0, skipna = True) 
print(df_assam_26_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_26_2008 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2008,'Area':'Production']
df_assam_26_2008_sum = df_assam_26_2008.sum(axis = 0, skipna = True) 
print(df_assam_26_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_26_2009 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2009,'Area':'Production']
df_assam_26_2009_sum = df_assam_26_2009.sum(axis = 0, skipna = True) 
print(df_assam_26_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_26_2010 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_26_2010_sum = df_assam_26_2010.sum(axis = 0, skipna = True)
print(df_assam_26_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_26_2011 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_26_2011_sum = df_assam_26_2011.sum(axis = 0, skipna = True)
print(df_assam_26_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_26_2012 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2012,'Area':'Production']
df_assam_26_2012_sum = df_assam_26_2012.sum(axis = 0, skipna = True) 
print(df_assam_26_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_26_2013 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_26_2013_sum = df_assam_26_2013.sum(axis = 0, skipna = True)
print(df_assam_26_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_26_2014 = df_assam_26.loc[df_assam_26['Crop_Year'] == 2014,'Area':'Production']
df_assam_26_2014_sum = df_assam_26_2014.sum(axis = 0, skipna = True) 
print(df_assam_26_2014_sum)
print("---------------------------------")
               
# details of assam : [27] UDALGURI

print("---- Details of assam : [27] UDALGURI -----")
df_assam_27 = df_assam[df_assam.District_Name == 'UDALGURI']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_assam_27_1997 = df_assam_27.loc[df_assam_27['Crop_Year'] == 1997,'Area':'Production']
df_assam_27_1997_sum = df_assam_27_1997.sum(axis = 0, skipna = True)
print(df_assam_27_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_assam_27_1998 = df_assam_27.loc[df_assam_27['Crop_Year'] == 1998,'Area':'Production']
df_assam_27_1998_sum = df_assam_27_1998.sum(axis = 0, skipna = True) 
print(df_assam_27_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_assam_27_1999 = df_assam_27.loc[df_assam_27['Crop_Year'] == 1999,'Area':'Production']
df_assam_27_1999_sum = df_assam_27_1999.sum(axis = 0, skipna = True) 
print(df_assam_27_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_assam_27_2000 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2000,'Area':'Production']
df_assam_27_2000_sum = df_assam_27_2000.sum(axis = 0, skipna = True) 
print(df_assam_27_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_assam_27_2001 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2001,'Area':'Production'] 
df_assam_27_2001_sum = df_assam_27_2001.sum(axis = 0, skipna = True)
print(df_assam_27_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_assam_27_2002 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2002,'Area':'Production']
df_assam_27_2002_sum = df_assam_27_2002.sum(axis = 0, skipna = True) 
print(df_assam_27_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_assam_27_2003 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2003,'Area':'Production']
df_assam_27_2003_sum = df_assam_27_2003.sum(axis = 0, skipna = True) 
print(df_assam_27_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_assam_27_2004 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2004,'Area':'Production']
df_assam_27_2004_sum = df_assam_27_2004.sum(axis = 0, skipna = True) 
print(df_assam_27_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_assam_27_2005 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2005,'Area':'Production']
df_assam_27_2005_sum = df_assam_27_2005.sum(axis = 0, skipna = True) 
print(df_assam_27_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_assam_27_2006 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2006,'Area':'Production'] 
df_assam_27_2006_sum = df_assam_27_2006.sum(axis = 0, skipna = True)
print(df_assam_27_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_assam_27_2007 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2007,'Area':'Production']
df_assam_27_2007_sum = df_assam_27_2007.sum(axis = 0, skipna = True) 
print(df_assam_27_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_assam_27_2008 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2008,'Area':'Production']
df_assam_27_2008_sum = df_assam_27_2008.sum(axis = 0, skipna = True) 
print(df_assam_27_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_assam_27_2009 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2009,'Area':'Production']
df_assam_27_2009_sum = df_assam_27_2009.sum(axis = 0, skipna = True) 
print(df_assam_27_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_assam_27_2010 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2010,'Area':'Production'] 
df_assam_27_2010_sum = df_assam_27_2010.sum(axis = 0, skipna = True)
print(df_assam_27_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_assam_27_2011 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2011,'Area':'Production'] 
df_assam_27_2011_sum = df_assam_27_2011.sum(axis = 0, skipna = True)
print(df_assam_27_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_assam_27_2012 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2012,'Area':'Production']
df_assam_27_2012_sum = df_assam_27_2012.sum(axis = 0, skipna = True) 
print(df_assam_27_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_assam_27_2013 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2013,'Area':'Production'] 
df_assam_27_2013_sum = df_assam_27_2013.sum(axis = 0, skipna = True)
print(df_assam_27_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_assam_27_2014 = df_assam_27.loc[df_assam_27['Crop_Year'] == 2014,'Area':'Production']
df_assam_27_2014_sum = df_assam_27_2014.sum(axis = 0, skipna = True) 
print(df_assam_27_2014_sum)
print("---------------------------------")

#Question-(5) West Bengal

print("--- State-5 : West Bengal ------")
df_wb = df[df.State_Name == 'West Bengal']
df_wb_dist = df_wb.groupby(['District_Name'])[['Crop_Year']].count()
print(df_wb_dist)

# crop year in West Bengal

print("--- Crop year in West Bengal -----")
df_wb_year = df_wb.groupby(['Crop_Year'])[['Crop_Year']].count()
print(df_wb_year)

# crop types in West Bengal

print("---- Crop Types in West Bengal -----")
df_wb_crop = df_wb.groupby(['Crop'])[['Crop']].count()
print(df_wb_crop)

# details of wb : [1] 24 PARAGANAS NORTH 

print("---- Details of wb : [1] 24 PARAGANAS NORTH ----")
df_wb_1 = df_wb[df_wb.District_Name == '24 PARAGANAS NORTH']
       
# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_1_1997 = df_wb_1.loc[df_wb_1['Crop_Year'] == 1997,'Area':'Production']
df_wb_1_1997_sum = df_wb_1_1997.sum(axis = 0, skipna = True)
print(df_wb_1_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_1_1998 = df_wb_1.loc[df_wb_1['Crop_Year'] == 1998,'Area':'Production']
df_wb_1_1998_sum = df_wb_1_1998.sum(axis = 0, skipna = True) 
print(df_wb_1_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_1_1999 = df_wb_1.loc[df_wb_1['Crop_Year'] == 1999,'Area':'Production']
df_wb_1_1999_sum = df_wb_1_1999.sum(axis = 0, skipna = True) 
print(df_wb_1_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_1_2000 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2000,'Area':'Production']
df_wb_1_2000_sum = df_wb_1_2000.sum(axis = 0, skipna = True) 
print(df_wb_1_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_1_2001 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_1_2001_sum = df_wb_1_2001.sum(axis = 0, skipna = True)
print(df_wb_1_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_1_2002 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2002,'Area':'Production']
df_wb_1_2002_sum = df_wb_1_2002.sum(axis = 0, skipna = True) 
print(df_wb_1_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_1_2003 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2003,'Area':'Production']
df_wb_1_2003_sum = df_wb_1_2003.sum(axis = 0, skipna = True) 
print(df_wb_1_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_1_2004 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2004,'Area':'Production']
df_wb_1_2004_sum = df_wb_1_2004.sum(axis = 0, skipna = True) 
print(df_wb_1_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_1_2005 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2005,'Area':'Production']
df_wb_1_2005_sum = df_wb_1_2005.sum(axis = 0, skipna = True) 
print(df_wb_1_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_1_2006 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_1_2006_sum = df_wb_1_2006.sum(axis = 0, skipna = True)
print(df_wb_1_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_1_2007 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2007,'Area':'Production']
df_wb_1_2007_sum = df_wb_1_2007.sum(axis = 0, skipna = True) 
print(df_wb_1_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_1_2008 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2008,'Area':'Production']
df_wb_1_2008_sum = df_wb_1_2008.sum(axis = 0, skipna = True) 
print(df_wb_1_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_1_2009 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2009,'Area':'Production']
df_wb_1_2009_sum = df_wb_1_2009.sum(axis = 0, skipna = True) 
print(df_wb_1_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_1_2010 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_1_2010_sum = df_wb_1_2010.sum(axis = 0, skipna = True)
print(df_wb_1_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_1_2011 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_1_2011_sum = df_wb_1_2011.sum(axis = 0, skipna = True)
print(df_wb_1_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_1_2012 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2012,'Area':'Production']
df_wb_1_2012_sum = df_wb_1_2012.sum(axis = 0, skipna = True) 
print(df_wb_1_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_1_2013 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_1_2013_sum = df_wb_1_2013.sum(axis = 0, skipna = True)
print(df_wb_1_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_1_2014 = df_wb_1.loc[df_wb_1['Crop_Year'] == 2014,'Area':'Production']
df_wb_1_2014_sum = df_wb_1_2014.sum(axis = 0, skipna = True) 
print(df_wb_1_2014_sum)
print("---------------------------------")       
                     
# details of wb : [2] 24 PARAGANAS SOUTH

print("--- Details of wb : [2] 24 PARAGANAS SOUTH ----")
df_wb_2 = df_wb[df_wb.District_Name == '24 PARAGANAS SOUTH']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_2_1997 = df_wb_2.loc[df_wb_2['Crop_Year'] == 1997,'Area':'Production']
df_wb_2_1997_sum = df_wb_2_1997.sum(axis = 0, skipna = True)
print(df_wb_2_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_2_1998 = df_wb_2.loc[df_wb_2['Crop_Year'] == 1998,'Area':'Production']
df_wb_2_1998_sum = df_wb_2_1998.sum(axis = 0, skipna = True) 
print(df_wb_2_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_2_1999 = df_wb_2.loc[df_wb_2['Crop_Year'] == 1999,'Area':'Production']
df_wb_2_1999_sum = df_wb_2_1999.sum(axis = 0, skipna = True) 
print(df_wb_2_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_2_2000 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2000,'Area':'Production']
df_wb_2_2000_sum = df_wb_2_2000.sum(axis = 0, skipna = True) 
print(df_wb_2_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_2_2001 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_2_2001_sum = df_wb_2_2001.sum(axis = 0, skipna = True)
print(df_wb_2_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_2_2002 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2002,'Area':'Production']
df_wb_2_2002_sum = df_wb_2_2002.sum(axis = 0, skipna = True) 
print(df_wb_2_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_2_2003 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2003,'Area':'Production']
df_wb_2_2003_sum = df_wb_2_2003.sum(axis = 0, skipna = True) 
print(df_wb_2_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_2_2004 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2004,'Area':'Production']
df_wb_2_2004_sum = df_wb_2_2004.sum(axis = 0, skipna = True) 
print(df_wb_2_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_2_2005 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2005,'Area':'Production']
df_wb_2_2005_sum = df_wb_2_2005.sum(axis = 0, skipna = True) 
print(df_wb_2_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_2_2006 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_2_2006_sum = df_wb_2_2006.sum(axis = 0, skipna = True)
print(df_wb_2_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_2_2007 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2007,'Area':'Production']
df_wb_2_2007_sum = df_wb_2_2007.sum(axis = 0, skipna = True) 
print(df_wb_2_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_2_2008 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2008,'Area':'Production']
df_wb_2_2008_sum = df_wb_2_2008.sum(axis = 0, skipna = True) 
print(df_wb_2_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_2_2009 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2009,'Area':'Production']
df_wb_2_2009_sum = df_wb_2_2009.sum(axis = 0, skipna = True) 
print(df_wb_2_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_2_2010 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_2_2010_sum = df_wb_2_2010.sum(axis = 0, skipna = True)
print(df_wb_2_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_2_2011 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_2_2011_sum = df_wb_2_2011.sum(axis = 0, skipna = True)
print(df_wb_2_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_2_2012 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2012,'Area':'Production']
df_wb_2_2012_sum = df_wb_2_2012.sum(axis = 0, skipna = True) 
print(df_wb_2_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_2_2013 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_2_2013_sum = df_wb_2_2013.sum(axis = 0, skipna = True)
print(df_wb_2_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_2_2014 = df_wb_2.loc[df_wb_2['Crop_Year'] == 2014,'Area':'Production']
df_wb_2_2014_sum = df_wb_2_2014.sum(axis = 0, skipna = True) 
print(df_wb_2_2014_sum)
print("---------------------------------")
                                
# details of wb : [3] BANKURA

print("---- Details of wb : [3] BANKURA -----")
df_wb_3 = df_wb[df_wb.District_Name == 'BANKURA']
 
# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_3_1997 = df_wb_3.loc[df_wb_3['Crop_Year'] == 1997,'Area':'Production']
df_wb_3_1997_sum = df_wb_3_1997.sum(axis = 0, skipna = True)
print(df_wb_3_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_3_1998 = df_wb_3.loc[df_wb_3['Crop_Year'] == 1998,'Area':'Production']
df_wb_3_1998_sum = df_wb_3_1998.sum(axis = 0, skipna = True) 
print(df_wb_3_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_3_1999 = df_wb_3.loc[df_wb_3['Crop_Year'] == 1999,'Area':'Production']
df_wb_3_1999_sum = df_wb_3_1999.sum(axis = 0, skipna = True) 
print(df_wb_3_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_3_2000 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2000,'Area':'Production']
df_wb_3_2000_sum = df_wb_3_2000.sum(axis = 0, skipna = True) 
print(df_wb_3_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_3_2001 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_3_2001_sum = df_wb_3_2001.sum(axis = 0, skipna = True)
print(df_wb_3_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_3_2002 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2002,'Area':'Production']
df_wb_3_2002_sum = df_wb_3_2002.sum(axis = 0, skipna = True) 
print(df_wb_3_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_3_2003 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2003,'Area':'Production']
df_wb_3_2003_sum = df_wb_3_2003.sum(axis = 0, skipna = True) 
print(df_wb_3_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_3_2004 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2004,'Area':'Production']
df_wb_3_2004_sum = df_wb_3_2004.sum(axis = 0, skipna = True) 
print(df_wb_3_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_3_2005 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2005,'Area':'Production']
df_wb_3_2005_sum = df_wb_3_2005.sum(axis = 0, skipna = True) 
print(df_wb_3_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_3_2006 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_3_2006_sum = df_wb_3_2006.sum(axis = 0, skipna = True)
print(df_wb_3_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_3_2007 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2007,'Area':'Production']
df_wb_3_2007_sum = df_wb_3_2007.sum(axis = 0, skipna = True) 
print(df_wb_3_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_3_2008 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2008,'Area':'Production']
df_wb_3_2008_sum = df_wb_3_2008.sum(axis = 0, skipna = True) 
print(df_wb_3_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_3_2009 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2009,'Area':'Production']
df_wb_3_2009_sum = df_wb_3_2009.sum(axis = 0, skipna = True) 
print(df_wb_3_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_3_2010 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_3_2010_sum = df_wb_3_2010.sum(axis = 0, skipna = True)
print(df_wb_3_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_3_2011 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_3_2011_sum = df_wb_3_2011.sum(axis = 0, skipna = True)
print(df_wb_3_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_3_2012 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2012,'Area':'Production']
df_wb_3_2012_sum = df_wb_3_2012.sum(axis = 0, skipna = True) 
print(df_wb_3_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_3_2013 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_3_2013_sum = df_wb_3_2013.sum(axis = 0, skipna = True)
print(df_wb_3_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_3_2014 = df_wb_3.loc[df_wb_3['Crop_Year'] == 2014,'Area':'Production']
df_wb_3_2014_sum = df_wb_3_2014.sum(axis = 0, skipna = True) 
print(df_wb_3_2014_sum)
print("---------------------------------")                                     
                                                         
# details of wb : [4] BARDHAMAN 

print("---- Details of wb : [4] BARDHAMAN -----")
df_wb_4 = df_wb[df_wb.District_Name == 'BARDHAMAN']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_4_1997 = df_wb_4.loc[df_wb_4['Crop_Year'] == 1997,'Area':'Production']
df_wb_4_1997_sum = df_wb_4_1997.sum(axis = 0, skipna = True)
print(df_wb_4_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_4_1998 = df_wb_4.loc[df_wb_4['Crop_Year'] == 1998,'Area':'Production']
df_wb_4_1998_sum = df_wb_4_1998.sum(axis = 0, skipna = True) 
print(df_wb_4_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_4_1999 = df_wb_4.loc[df_wb_4['Crop_Year'] == 1999,'Area':'Production']
df_wb_4_1999_sum = df_wb_4_1999.sum(axis = 0, skipna = True) 
print(df_wb_4_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_4_2000 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2000,'Area':'Production']
df_wb_4_2000_sum = df_wb_4_2000.sum(axis = 0, skipna = True) 
print(df_wb_4_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_4_2001 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_4_2001_sum = df_wb_4_2001.sum(axis = 0, skipna = True)
print(df_wb_4_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_4_2002 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2002,'Area':'Production']
df_wb_4_2002_sum = df_wb_4_2002.sum(axis = 0, skipna = True) 
print(df_wb_4_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_4_2003 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2003,'Area':'Production']
df_wb_4_2003_sum = df_wb_4_2003.sum(axis = 0, skipna = True) 
print(df_wb_4_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_4_2004 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2004,'Area':'Production']
df_wb_4_2004_sum = df_wb_4_2004.sum(axis = 0, skipna = True) 
print(df_wb_4_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_4_2005 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2005,'Area':'Production']
df_wb_4_2005_sum = df_wb_4_2005.sum(axis = 0, skipna = True) 
print(df_wb_4_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_4_2006 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_4_2006_sum = df_wb_4_2006.sum(axis = 0, skipna = True)
print(df_wb_4_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_4_2007 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2007,'Area':'Production']
df_wb_4_2007_sum = df_wb_4_2007.sum(axis = 0, skipna = True) 
print(df_wb_4_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_4_2008 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2008,'Area':'Production']
df_wb_4_2008_sum = df_wb_4_2008.sum(axis = 0, skipna = True) 
print(df_wb_4_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_4_2009 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2009,'Area':'Production']
df_wb_4_2009_sum = df_wb_4_2009.sum(axis = 0, skipna = True) 
print(df_wb_4_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_4_2010 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_4_2010_sum = df_wb_4_2010.sum(axis = 0, skipna = True)
print(df_wb_4_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_4_2011 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_4_2011_sum = df_wb_4_2011.sum(axis = 0, skipna = True)
print(df_wb_4_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_4_2012 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2012,'Area':'Production']
df_wb_4_2012_sum = df_wb_4_2012.sum(axis = 0, skipna = True) 
print(df_wb_4_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_4_2013 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_4_2013_sum = df_wb_4_2013.sum(axis = 0, skipna = True)
print(df_wb_4_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_4_2014 = df_wb_4.loc[df_wb_4['Crop_Year'] == 2014,'Area':'Production']
df_wb_4_2014_sum = df_wb_4_2014.sum(axis = 0, skipna = True) 
print(df_wb_4_2014_sum)
print("---------------------------------")
            
# details of wb : [5] BIRBHUM  

print("--- Details of wb : [5] BIRBHUM -----")
df_wb_5 = df_wb[df_wb.District_Name == 'BIRBHUM']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_5_1997 = df_wb_5.loc[df_wb_5['Crop_Year'] == 1997,'Area':'Production']
df_wb_5_1997_sum = df_wb_5_1997.sum(axis = 0, skipna = True)
print(df_wb_5_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_5_1998 = df_wb_5.loc[df_wb_5['Crop_Year'] == 1998,'Area':'Production']
df_wb_5_1998_sum = df_wb_5_1998.sum(axis = 0, skipna = True) 
print(df_wb_5_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_5_1999 = df_wb_5.loc[df_wb_5['Crop_Year'] == 1999,'Area':'Production']
df_wb_5_1999_sum = df_wb_5_1999.sum(axis = 0, skipna = True) 
print(df_wb_5_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_5_2000 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2000,'Area':'Production']
df_wb_5_2000_sum = df_wb_5_2000.sum(axis = 0, skipna = True) 
print(df_wb_5_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_5_2001 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_5_2001_sum = df_wb_5_2001.sum(axis = 0, skipna = True)
print(df_wb_5_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_5_2002 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2002,'Area':'Production']
df_wb_5_2002_sum = df_wb_5_2002.sum(axis = 0, skipna = True) 
print(df_wb_5_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_5_2003 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2003,'Area':'Production']
df_wb_5_2003_sum = df_wb_5_2003.sum(axis = 0, skipna = True) 
print(df_wb_5_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_5_2004 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2004,'Area':'Production']
df_wb_5_2004_sum = df_wb_5_2004.sum(axis = 0, skipna = True) 
print(df_wb_5_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_5_2005 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2005,'Area':'Production']
df_wb_5_2005_sum = df_wb_5_2005.sum(axis = 0, skipna = True) 
print(df_wb_5_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_5_2006 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_5_2006_sum = df_wb_5_2006.sum(axis = 0, skipna = True)
print(df_wb_5_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_5_2007 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2007,'Area':'Production']
df_wb_5_2007_sum = df_wb_5_2007.sum(axis = 0, skipna = True) 
print(df_wb_5_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_5_2008 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2008,'Area':'Production']
df_wb_5_2008_sum = df_wb_5_2008.sum(axis = 0, skipna = True) 
print(df_wb_5_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_5_2009 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2009,'Area':'Production']
df_wb_5_2009_sum = df_wb_5_2009.sum(axis = 0, skipna = True) 
print(df_wb_5_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_5_2010 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_5_2010_sum = df_wb_5_2010.sum(axis = 0, skipna = True)
print(df_wb_5_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_5_2011 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_5_2011_sum = df_wb_5_2011.sum(axis = 0, skipna = True)
print(df_wb_5_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_5_2012 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2012,'Area':'Production']
df_wb_5_2012_sum = df_wb_5_2012.sum(axis = 0, skipna = True) 
print(df_wb_5_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_5_2013 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_5_2013_sum = df_wb_5_2013.sum(axis = 0, skipna = True)
print(df_wb_5_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_5_2014 = df_wb_5.loc[df_wb_5['Crop_Year'] == 2014,'Area':'Production']
df_wb_5_2014_sum = df_wb_5_2014.sum(axis = 0, skipna = True) 
print(df_wb_5_2014_sum)
print("---------------------------------")
                                   
# details of wb : [6] COOCHBEHAR  

print("---- Details of wb : [6] COOCHBEHAR ----- ")
df_wb_6 = df_wb[df_wb.District_Name == 'COOCHBEHAR']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_6_1997 = df_wb_6.loc[df_wb_6['Crop_Year'] == 1997,'Area':'Production']
df_wb_6_1997_sum = df_wb_6_1997.sum(axis = 0, skipna = True)
print(df_wb_6_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_6_1998 = df_wb_6.loc[df_wb_6['Crop_Year'] == 1998,'Area':'Production']
df_wb_6_1998_sum = df_wb_6_1998.sum(axis = 0, skipna = True) 
print(df_wb_6_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_6_1999 = df_wb_6.loc[df_wb_6['Crop_Year'] == 1999,'Area':'Production']
df_wb_6_1999_sum = df_wb_6_1999.sum(axis = 0, skipna = True) 
print(df_wb_6_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_6_2000 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2000,'Area':'Production']
df_wb_6_2000_sum = df_wb_6_2000.sum(axis = 0, skipna = True) 
print(df_wb_6_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_6_2001 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_6_2001_sum = df_wb_6_2001.sum(axis = 0, skipna = True)
print(df_wb_6_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_6_2002 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2002,'Area':'Production']
df_wb_6_2002_sum = df_wb_6_2002.sum(axis = 0, skipna = True) 
print(df_wb_6_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_6_2003 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2003,'Area':'Production']
df_wb_6_2003_sum = df_wb_6_2003.sum(axis = 0, skipna = True) 
print(df_wb_6_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_6_2004 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2004,'Area':'Production']
df_wb_6_2004_sum = df_wb_6_2004.sum(axis = 0, skipna = True) 
print(df_wb_6_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_6_2005 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2005,'Area':'Production']
df_wb_6_2005_sum = df_wb_6_2005.sum(axis = 0, skipna = True) 
print(df_wb_6_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_6_2006 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_6_2006_sum = df_wb_6_2006.sum(axis = 0, skipna = True)
print(df_wb_6_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_6_2007 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2007,'Area':'Production']
df_wb_6_2007_sum = df_wb_6_2007.sum(axis = 0, skipna = True) 
print(df_wb_6_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_6_2008 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2008,'Area':'Production']
df_wb_6_2008_sum = df_wb_6_2008.sum(axis = 0, skipna = True) 
print(df_wb_6_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_6_2009 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2009,'Area':'Production']
df_wb_6_2009_sum = df_wb_6_2009.sum(axis = 0, skipna = True) 
print(df_wb_6_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_6_2010 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_6_2010_sum = df_wb_6_2010.sum(axis = 0, skipna = True)
print(df_wb_6_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_6_2011 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_6_2011_sum = df_wb_6_2011.sum(axis = 0, skipna = True)
print(df_wb_6_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_6_2012 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2012,'Area':'Production']
df_wb_6_2012_sum = df_wb_6_2012.sum(axis = 0, skipna = True) 
print(df_wb_6_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_6_2013 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_6_2013_sum = df_wb_6_2013.sum(axis = 0, skipna = True)
print(df_wb_6_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_6_2014 = df_wb_6.loc[df_wb_6['Crop_Year'] == 2014,'Area':'Production']
df_wb_6_2014_sum = df_wb_6_2014.sum(axis = 0, skipna = True) 
print(df_wb_6_2014_sum)
print("---------------------------------")
                          
# details of wb : [7] DARJEELING

print("--- details of wb : [7] DARJEELING -----")
df_wb_7 = df_wb[df_wb.District_Name == 'DARJEELING']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_7_1997 = df_wb_7.loc[df_wb_7['Crop_Year'] == 1997,'Area':'Production']
df_wb_7_1997_sum = df_wb_7_1997.sum(axis = 0, skipna = True)
print(df_wb_7_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_7_1998 = df_wb_7.loc[df_wb_7['Crop_Year'] == 1998,'Area':'Production']
df_wb_7_1998_sum = df_wb_7_1998.sum(axis = 0, skipna = True) 
print(df_wb_7_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_7_1999 = df_wb_7.loc[df_wb_7['Crop_Year'] == 1999,'Area':'Production']
df_wb_7_1999_sum = df_wb_7_1999.sum(axis = 0, skipna = True) 
print(df_wb_7_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_7_2000 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2000,'Area':'Production']
df_wb_7_2000_sum = df_wb_7_2000.sum(axis = 0, skipna = True) 
print(df_wb_7_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_7_2001 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_7_2001_sum = df_wb_7_2001.sum(axis = 0, skipna = True)
print(df_wb_7_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_7_2002 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2002,'Area':'Production']
df_wb_7_2002_sum = df_wb_7_2002.sum(axis = 0, skipna = True) 
print(df_wb_7_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_7_2003 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2003,'Area':'Production']
df_wb_7_2003_sum = df_wb_7_2003.sum(axis = 0, skipna = True) 
print(df_wb_7_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_7_2004 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2004,'Area':'Production']
df_wb_7_2004_sum = df_wb_7_2004.sum(axis = 0, skipna = True) 
print(df_wb_7_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_7_2005 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2005,'Area':'Production']
df_wb_7_2005_sum = df_wb_7_2005.sum(axis = 0, skipna = True) 
print(df_wb_7_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_7_2006 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_7_2006_sum = df_wb_7_2006.sum(axis = 0, skipna = True)
print(df_wb_7_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_7_2007 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2007,'Area':'Production']
df_wb_7_2007_sum = df_wb_7_2007.sum(axis = 0, skipna = True) 
print(df_wb_7_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_7_2008 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2008,'Area':'Production']
df_wb_7_2008_sum = df_wb_7_2008.sum(axis = 0, skipna = True) 
print(df_wb_7_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_7_2009 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2009,'Area':'Production']
df_wb_7_2009_sum = df_wb_7_2009.sum(axis = 0, skipna = True) 
print(df_wb_7_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_7_2010 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_7_2010_sum = df_wb_7_2010.sum(axis = 0, skipna = True)
print(df_wb_7_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_7_2011 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_7_2011_sum = df_wb_7_2011.sum(axis = 0, skipna = True)
print(df_wb_7_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_7_2012 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2012,'Area':'Production']
df_wb_7_2012_sum = df_wb_7_2012.sum(axis = 0, skipna = True) 
print(df_wb_7_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_7_2013 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_7_2013_sum = df_wb_7_2013.sum(axis = 0, skipna = True)
print(df_wb_7_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_7_2014 = df_wb_7.loc[df_wb_7['Crop_Year'] == 2014,'Area':'Production']
df_wb_7_2014_sum = df_wb_7_2014.sum(axis = 0, skipna = True) 
print(df_wb_7_2014_sum)
print("---------------------------------")
                  
# details of wb : [8] DINAJPUR DAKSHIN

print("--- Details of wb : [8] DINAJPUR DAKSHIN ----")
df_wb_8 = df_wb[df_wb.District_Name == 'DINAJPUR DAKSHIN']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_8_1997 = df_wb_8.loc[df_wb_8['Crop_Year'] == 1997,'Area':'Production']
df_wb_8_1997_sum = df_wb_8_1997.sum(axis = 0, skipna = True)
print(df_wb_8_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_8_1998 = df_wb_8.loc[df_wb_8['Crop_Year'] == 1998,'Area':'Production']
df_wb_8_1998_sum = df_wb_8_1998.sum(axis = 0, skipna = True) 
print(df_wb_8_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_8_1999 = df_wb_8.loc[df_wb_8['Crop_Year'] == 1999,'Area':'Production']
df_wb_8_1999_sum = df_wb_8_1999.sum(axis = 0, skipna = True) 
print(df_wb_8_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_8_2000 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2000,'Area':'Production']
df_wb_8_2000_sum = df_wb_8_2000.sum(axis = 0, skipna = True) 
print(df_wb_8_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_8_2001 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_8_2001_sum = df_wb_8_2001.sum(axis = 0, skipna = True)
print(df_wb_8_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_8_2002 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2002,'Area':'Production']
df_wb_8_2002_sum = df_wb_8_2002.sum(axis = 0, skipna = True) 
print(df_wb_8_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_8_2003 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2003,'Area':'Production']
df_wb_8_2003_sum = df_wb_8_2003.sum(axis = 0, skipna = True) 
print(df_wb_8_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_8_2004 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2004,'Area':'Production']
df_wb_8_2004_sum = df_wb_8_2004.sum(axis = 0, skipna = True) 
print(df_wb_8_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_8_2005 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2005,'Area':'Production']
df_wb_8_2005_sum = df_wb_8_2005.sum(axis = 0, skipna = True) 
print(df_wb_8_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_8_2006 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_8_2006_sum = df_wb_8_2006.sum(axis = 0, skipna = True)
print(df_wb_8_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_8_2007 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2007,'Area':'Production']
df_wb_8_2007_sum = df_wb_8_2007.sum(axis = 0, skipna = True) 
print(df_wb_8_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_8_2008 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2008,'Area':'Production']
df_wb_8_2008_sum = df_wb_8_2008.sum(axis = 0, skipna = True) 
print(df_wb_8_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_8_2009 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2009,'Area':'Production']
df_wb_8_2009_sum = df_wb_8_2009.sum(axis = 0, skipna = True) 
print(df_wb_8_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_8_2010 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_8_2010_sum = df_wb_8_2010.sum(axis = 0, skipna = True)
print(df_wb_8_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_8_2011 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_8_2011_sum = df_wb_8_2011.sum(axis = 0, skipna = True)
print(df_wb_8_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_8_2012 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2012,'Area':'Production']
df_wb_8_2012_sum = df_wb_8_2012.sum(axis = 0, skipna = True) 
print(df_wb_8_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_8_2013 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_8_2013_sum = df_wb_8_2013.sum(axis = 0, skipna = True)
print(df_wb_8_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_8_2014 = df_wb_8.loc[df_wb_8['Crop_Year'] == 2014,'Area':'Production']
df_wb_8_2014_sum = df_wb_8_2014.sum(axis = 0, skipna = True) 
print(df_wb_8_2014_sum)
print("---------------------------------")
             
# details of wb : [9] DINAJPUR UTTAR

df_wb_9 = df_wb[df_wb.District_Name == 'DINAJPUR UTTAR']
print("---- Details of wb : [9] DINAJPUR UTTAR ---")

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_9_1997 = df_wb_9.loc[df_wb_9['Crop_Year'] == 1997,'Area':'Production']
df_wb_9_1997_sum = df_wb_9_1997.sum(axis = 0, skipna = True)
print(df_wb_9_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_9_1998 = df_wb_9.loc[df_wb_9['Crop_Year'] == 1998,'Area':'Production']
df_wb_9_1998_sum = df_wb_9_1998.sum(axis = 0, skipna = True) 
print(df_wb_9_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_9_1999 = df_wb_9.loc[df_wb_9['Crop_Year'] == 1999,'Area':'Production']
df_wb_9_1999_sum = df_wb_9_1999.sum(axis = 0, skipna = True) 
print(df_wb_9_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_9_2000 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2000,'Area':'Production']
df_wb_9_2000_sum = df_wb_9_2000.sum(axis = 0, skipna = True) 
print(df_wb_9_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_9_2001 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_9_2001_sum = df_wb_9_2001.sum(axis = 0, skipna = True)
print(df_wb_9_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_9_2002 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2002,'Area':'Production']
df_wb_9_2002_sum = df_wb_9_2002.sum(axis = 0, skipna = True) 
print(df_wb_9_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_9_2003 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2003,'Area':'Production']
df_wb_9_2003_sum = df_wb_9_2003.sum(axis = 0, skipna = True) 
print(df_wb_9_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_9_2004 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2004,'Area':'Production']
df_wb_9_2004_sum = df_wb_9_2004.sum(axis = 0, skipna = True) 
print(df_wb_9_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_9_2005 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2005,'Area':'Production']
df_wb_9_2005_sum = df_wb_9_2005.sum(axis = 0, skipna = True) 
print(df_wb_9_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_9_2006 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_9_2006_sum = df_wb_9_2006.sum(axis = 0, skipna = True)
print(df_wb_9_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_9_2007 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2007,'Area':'Production']
df_wb_9_2007_sum = df_wb_9_2007.sum(axis = 0, skipna = True) 
print(df_wb_9_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_9_2008 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2008,'Area':'Production']
df_wb_9_2008_sum = df_wb_9_2008.sum(axis = 0, skipna = True) 
print(df_wb_9_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_9_2009 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2009,'Area':'Production']
df_wb_9_2009_sum = df_wb_9_2009.sum(axis = 0, skipna = True) 
print(df_wb_9_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_9_2010 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_9_2010_sum = df_wb_9_2010.sum(axis = 0, skipna = True)
print(df_wb_9_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_9_2011 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_9_2011_sum = df_wb_9_2011.sum(axis = 0, skipna = True)
print(df_wb_9_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_9_2012 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2012,'Area':'Production']
df_wb_9_2012_sum = df_wb_9_2012.sum(axis = 0, skipna = True) 
print(df_wb_9_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_9_2013 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_9_2013_sum = df_wb_9_2013.sum(axis = 0, skipna = True)
print(df_wb_9_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_9_2014 = df_wb_9.loc[df_wb_9['Crop_Year'] == 2014,'Area':'Production']
df_wb_9_2014_sum = df_wb_9_2014.sum(axis = 0, skipna = True) 
print(df_wb_9_2014_sum)
print("---------------------------------")
                    
# details of wb : [10] HOOGHLY  

print("---- Details of wb : [10] HOOGHLY ----")
df_wb_10 = df_wb[df_wb.District_Name == 'HOOGHLY']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_10_1997 = df_wb_10.loc[df_wb_10['Crop_Year'] == 1997,'Area':'Production']
df_wb_10_1997_sum = df_wb_10_1997.sum(axis = 0, skipna = True)
print(df_wb_10_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_10_1998 = df_wb_10.loc[df_wb_10['Crop_Year'] == 1998,'Area':'Production']
df_wb_10_1998_sum = df_wb_10_1998.sum(axis = 0, skipna = True) 
print(df_wb_10_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_10_1999 = df_wb_10.loc[df_wb_10['Crop_Year'] == 1999,'Area':'Production']
df_wb_10_1999_sum = df_wb_10_1999.sum(axis = 0, skipna = True) 
print(df_wb_10_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_10_2000 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2000,'Area':'Production']
df_wb_10_2000_sum = df_wb_10_2000.sum(axis = 0, skipna = True) 
print(df_wb_10_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_10_2001 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_10_2001_sum = df_wb_10_2001.sum(axis = 0, skipna = True)
print(df_wb_10_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_10_2002 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2002,'Area':'Production']
df_wb_10_2002_sum = df_wb_10_2002.sum(axis = 0, skipna = True) 
print(df_wb_10_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_10_2003 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2003,'Area':'Production']
df_wb_10_2003_sum = df_wb_10_2003.sum(axis = 0, skipna = True) 
print(df_wb_10_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_10_2004 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2004,'Area':'Production']
df_wb_10_2004_sum = df_wb_10_2004.sum(axis = 0, skipna = True) 
print(df_wb_10_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_10_2005 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2005,'Area':'Production']
df_wb_10_2005_sum = df_wb_10_2005.sum(axis = 0, skipna = True) 
print(df_wb_10_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_10_2006 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_10_2006_sum = df_wb_10_2006.sum(axis = 0, skipna = True)
print(df_wb_10_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_10_2007 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2007,'Area':'Production']
df_wb_10_2007_sum = df_wb_10_2007.sum(axis = 0, skipna = True) 
print(df_wb_10_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_10_2008 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2008,'Area':'Production']
df_wb_10_2008_sum = df_wb_10_2008.sum(axis = 0, skipna = True) 
print(df_wb_10_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_10_2009 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2009,'Area':'Production']
df_wb_10_2009_sum = df_wb_10_2009.sum(axis = 0, skipna = True) 
print(df_wb_10_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_10_2010 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_10_2010_sum = df_wb_10_2010.sum(axis = 0, skipna = True)
print(df_wb_10_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_10_2011 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_10_2011_sum = df_wb_10_2011.sum(axis = 0, skipna = True)
print(df_wb_10_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_10_2012 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2012,'Area':'Production']
df_wb_10_2012_sum = df_wb_10_2012.sum(axis = 0, skipna = True) 
print(df_wb_10_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_10_2013 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_10_2013_sum = df_wb_10_2013.sum(axis = 0, skipna = True)
print(df_wb_10_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_10_2014 = df_wb_10.loc[df_wb_10['Crop_Year'] == 2014,'Area':'Production']
df_wb_10_2014_sum = df_wb_10_2014.sum(axis = 0, skipna = True) 
print(df_wb_10_2014_sum)
print("---------------------------------")
                                                   
# details of wb : [11] HOWRAH 

print("---- Details of wb : [11] HOWRAH --------")
df_wb_11 = df_wb[df_wb.District_Name == 'HOWRAH']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_11_1997 = df_wb_11.loc[df_wb_11['Crop_Year'] == 1997,'Area':'Production']
df_wb_11_1997_sum = df_wb_11_1997.sum(axis = 0, skipna = True)
print(df_wb_11_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_11_1998 = df_wb_11.loc[df_wb_11['Crop_Year'] == 1998,'Area':'Production']
df_wb_11_1998_sum = df_wb_11_1998.sum(axis = 0, skipna = True) 
print(df_wb_11_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_11_1999 = df_wb_11.loc[df_wb_11['Crop_Year'] == 1999,'Area':'Production']
df_wb_11_1999_sum = df_wb_11_1999.sum(axis = 0, skipna = True) 
print(df_wb_11_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_11_2000 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2000,'Area':'Production']
df_wb_11_2000_sum = df_wb_11_2000.sum(axis = 0, skipna = True) 
print(df_wb_11_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_11_2001 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_11_2001_sum = df_wb_11_2001.sum(axis = 0, skipna = True)
print(df_wb_11_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_11_2002 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2002,'Area':'Production']
df_wb_11_2002_sum = df_wb_11_2002.sum(axis = 0, skipna = True) 
print(df_wb_11_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_11_2003 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2003,'Area':'Production']
df_wb_11_2003_sum = df_wb_11_2003.sum(axis = 0, skipna = True) 
print(df_wb_11_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_11_2004 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2004,'Area':'Production']
df_wb_11_2004_sum = df_wb_11_2004.sum(axis = 0, skipna = True) 
print(df_wb_11_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_11_2005 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2005,'Area':'Production']
df_wb_11_2005_sum = df_wb_11_2005.sum(axis = 0, skipna = True) 
print(df_wb_11_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_11_2006 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_11_2006_sum = df_wb_11_2006.sum(axis = 0, skipna = True)
print(df_wb_11_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_11_2007 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2007,'Area':'Production']
df_wb_11_2007_sum = df_wb_11_2007.sum(axis = 0, skipna = True) 
print(df_wb_11_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_11_2008 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2008,'Area':'Production']
df_wb_11_2008_sum = df_wb_11_2008.sum(axis = 0, skipna = True) 
print(df_wb_11_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_11_2009 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2009,'Area':'Production']
df_wb_11_2009_sum = df_wb_11_2009.sum(axis = 0, skipna = True) 
print(df_wb_11_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_11_2010 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_11_2010_sum = df_wb_11_2010.sum(axis = 0, skipna = True)
print(df_wb_11_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_11_2011 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_11_2011_sum = df_wb_11_2011.sum(axis = 0, skipna = True)
print(df_wb_11_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_11_2012 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2012,'Area':'Production']
df_wb_11_2012_sum = df_wb_11_2012.sum(axis = 0, skipna = True) 
print(df_wb_11_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_11_2013 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_11_2013_sum = df_wb_11_2013.sum(axis = 0, skipna = True)
print(df_wb_11_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_11_2014 = df_wb_11.loc[df_wb_11['Crop_Year'] == 2014,'Area':'Production']
df_wb_11_2014_sum = df_wb_11_2014.sum(axis = 0, skipna = True) 
print(df_wb_11_2014_sum)
print("---------------------------------")
                                          
# details of wb : [12] JALPAIGURI 

print("---- Details of wb : [11] JALPAIGURI -----") 
df_wb_12 = df_wb[df_wb.District_Name == 'JALPAIGURI']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_12_1997 = df_wb_12.loc[df_wb_12['Crop_Year'] == 1997,'Area':'Production']
df_wb_12_1997_sum = df_wb_12_1997.sum(axis = 0, skipna = True)
print(df_wb_12_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_12_1998 = df_wb_12.loc[df_wb_12['Crop_Year'] == 1998,'Area':'Production']
df_wb_12_1998_sum = df_wb_12_1998.sum(axis = 0, skipna = True) 
print(df_wb_12_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_12_1999 = df_wb_12.loc[df_wb_12['Crop_Year'] == 1999,'Area':'Production']
df_wb_12_1999_sum = df_wb_12_1999.sum(axis = 0, skipna = True) 
print(df_wb_12_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_12_2000 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2000,'Area':'Production']
df_wb_12_2000_sum = df_wb_12_2000.sum(axis = 0, skipna = True) 
print(df_wb_12_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_12_2001 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_12_2001_sum = df_wb_12_2001.sum(axis = 0, skipna = True)
print(df_wb_12_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_12_2002 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2002,'Area':'Production']
df_wb_12_2002_sum = df_wb_12_2002.sum(axis = 0, skipna = True) 
print(df_wb_12_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_12_2003 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2003,'Area':'Production']
df_wb_12_2003_sum = df_wb_12_2003.sum(axis = 0, skipna = True) 
print(df_wb_12_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_12_2004 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2004,'Area':'Production']
df_wb_12_2004_sum = df_wb_12_2004.sum(axis = 0, skipna = True) 
print(df_wb_12_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_12_2005 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2005,'Area':'Production']
df_wb_12_2005_sum = df_wb_12_2005.sum(axis = 0, skipna = True) 
print(df_wb_12_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_12_2006 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_12_2006_sum = df_wb_12_2006.sum(axis = 0, skipna = True)
print(df_wb_12_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_12_2007 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2007,'Area':'Production']
df_wb_12_2007_sum = df_wb_12_2007.sum(axis = 0, skipna = True) 
print(df_wb_12_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_12_2008 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2008,'Area':'Production']
df_wb_12_2008_sum = df_wb_12_2008.sum(axis = 0, skipna = True) 
print(df_wb_12_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_12_2009 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2009,'Area':'Production']
df_wb_12_2009_sum = df_wb_12_2009.sum(axis = 0, skipna = True) 
print(df_wb_12_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_12_2010 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_12_2010_sum = df_wb_12_2010.sum(axis = 0, skipna = True)
print(df_wb_12_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_12_2011 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_12_2011_sum = df_wb_12_2011.sum(axis = 0, skipna = True)
print(df_wb_12_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_12_2012 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2012,'Area':'Production']
df_wb_12_2012_sum = df_wb_12_2012.sum(axis = 0, skipna = True) 
print(df_wb_12_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_12_2013 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_12_2013_sum = df_wb_12_2013.sum(axis = 0, skipna = True)
print(df_wb_12_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_12_2014 = df_wb_12.loc[df_wb_12['Crop_Year'] == 2014,'Area':'Production']
df_wb_12_2014_sum = df_wb_12_2014.sum(axis = 0, skipna = True) 
print(df_wb_12_2014_sum)
print("---------------------------------")
                          
# details of wb : [13] MALDAH

print("----- Details of wb : [13] MALDAH -------")
df_wb_13 = df_wb[df_wb.District_Name == 'MALDAH']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_13_1997 = df_wb_13.loc[df_wb_13['Crop_Year'] == 1997,'Area':'Production']
df_wb_13_1997_sum = df_wb_13_1997.sum(axis = 0, skipna = True)
print(df_wb_13_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_13_1998 = df_wb_13.loc[df_wb_13['Crop_Year'] == 1998,'Area':'Production']
df_wb_13_1998_sum = df_wb_13_1998.sum(axis = 0, skipna = True) 
print(df_wb_13_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_13_1999 = df_wb_13.loc[df_wb_13['Crop_Year'] == 1999,'Area':'Production']
df_wb_13_1999_sum = df_wb_13_1999.sum(axis = 0, skipna = True) 
print(df_wb_13_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_13_2000 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2000,'Area':'Production']
df_wb_13_2000_sum = df_wb_13_2000.sum(axis = 0, skipna = True) 
print(df_wb_13_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_13_2001 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_13_2001_sum = df_wb_13_2001.sum(axis = 0, skipna = True)
print(df_wb_13_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_13_2002 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2002,'Area':'Production']
df_wb_13_2002_sum = df_wb_13_2002.sum(axis = 0, skipna = True) 
print(df_wb_13_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_13_2003 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2003,'Area':'Production']
df_wb_13_2003_sum = df_wb_13_2003.sum(axis = 0, skipna = True) 
print(df_wb_13_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_13_2004 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2004,'Area':'Production']
df_wb_13_2004_sum = df_wb_13_2004.sum(axis = 0, skipna = True) 
print(df_wb_13_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_13_2005 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2005,'Area':'Production']
df_wb_13_2005_sum = df_wb_13_2005.sum(axis = 0, skipna = True) 
print(df_wb_13_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_13_2006 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_13_2006_sum = df_wb_13_2006.sum(axis = 0, skipna = True)
print(df_wb_13_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_13_2007 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2007,'Area':'Production']
df_wb_13_2007_sum = df_wb_13_2007.sum(axis = 0, skipna = True) 
print(df_wb_13_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_13_2008 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2008,'Area':'Production']
df_wb_13_2008_sum = df_wb_13_2008.sum(axis = 0, skipna = True) 
print(df_wb_13_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_13_2009 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2009,'Area':'Production']
df_wb_13_2009_sum = df_wb_13_2009.sum(axis = 0, skipna = True) 
print(df_wb_13_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_13_2010 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_13_2010_sum = df_wb_13_2010.sum(axis = 0, skipna = True)
print(df_wb_13_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_13_2011 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_13_2011_sum = df_wb_13_2011.sum(axis = 0, skipna = True)
print(df_wb_13_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_13_2012 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2012,'Area':'Production']
df_wb_13_2012_sum = df_wb_13_2012.sum(axis = 0, skipna = True) 
print(df_wb_13_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_13_2013 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_13_2013_sum = df_wb_13_2013.sum(axis = 0, skipna = True)
print(df_wb_13_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_13_2014 = df_wb_13.loc[df_wb_13['Crop_Year'] == 2014,'Area':'Production']
df_wb_13_2014_sum = df_wb_13_2014.sum(axis = 0, skipna = True) 
print(df_wb_13_2014_sum)
print("---------------------------------")
                                        
# details of wb : [14] MEDINIPUR EAST 

print("----- Details of wb : [14] MEDINIPUR EAST ------")
df_wb_14 = df_wb[df_wb.District_Name == 'MEDINIPUR EAST']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_14_1997 = df_wb_14.loc[df_wb_14['Crop_Year'] == 1997,'Area':'Production']
df_wb_14_1997_sum = df_wb_14_1997.sum(axis = 0, skipna = True)
print(df_wb_14_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_14_1998 = df_wb_14.loc[df_wb_14['Crop_Year'] == 1998,'Area':'Production']
df_wb_14_1998_sum = df_wb_14_1998.sum(axis = 0, skipna = True) 
print(df_wb_14_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_14_1999 = df_wb_14.loc[df_wb_14['Crop_Year'] == 1999,'Area':'Production']
df_wb_14_1999_sum = df_wb_14_1999.sum(axis = 0, skipna = True) 
print(df_wb_14_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_14_2000 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2000,'Area':'Production']
df_wb_14_2000_sum = df_wb_14_2000.sum(axis = 0, skipna = True) 
print(df_wb_14_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_14_2001 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_14_2001_sum = df_wb_14_2001.sum(axis = 0, skipna = True)
print(df_wb_14_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_14_2002 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2002,'Area':'Production']
df_wb_14_2002_sum = df_wb_14_2002.sum(axis = 0, skipna = True) 
print(df_wb_14_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_14_2003 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2003,'Area':'Production']
df_wb_14_2003_sum = df_wb_14_2003.sum(axis = 0, skipna = True) 
print(df_wb_14_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_14_2004 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2004,'Area':'Production']
df_wb_14_2004_sum = df_wb_14_2004.sum(axis = 0, skipna = True) 
print(df_wb_14_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_14_2005 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2005,'Area':'Production']
df_wb_14_2005_sum = df_wb_14_2005.sum(axis = 0, skipna = True) 
print(df_wb_14_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_14_2006 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_14_2006_sum = df_wb_14_2006.sum(axis = 0, skipna = True)
print(df_wb_14_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_14_2007 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2007,'Area':'Production']
df_wb_14_2007_sum = df_wb_14_2007.sum(axis = 0, skipna = True) 
print(df_wb_14_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_14_2008 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2008,'Area':'Production']
df_wb_14_2008_sum = df_wb_14_2008.sum(axis = 0, skipna = True) 
print(df_wb_14_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_14_2009 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2009,'Area':'Production']
df_wb_14_2009_sum = df_wb_14_2009.sum(axis = 0, skipna = True) 
print(df_wb_14_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_14_2010 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_14_2010_sum = df_wb_14_2010.sum(axis = 0, skipna = True)
print(df_wb_14_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_14_2011 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_14_2011_sum = df_wb_14_2011.sum(axis = 0, skipna = True)
print(df_wb_14_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_14_2012 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2012,'Area':'Production']
df_wb_14_2012_sum = df_wb_14_2012.sum(axis = 0, skipna = True) 
print(df_wb_14_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_14_2013 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_14_2013_sum = df_wb_14_2013.sum(axis = 0, skipna = True)
print(df_wb_14_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_14_2014 = df_wb_14.loc[df_wb_14['Crop_Year'] == 2014,'Area':'Production']
df_wb_14_2014_sum = df_wb_14_2014.sum(axis = 0, skipna = True) 
print(df_wb_14_2014_sum)
print("---------------------------------")
                                 
# details of wb : [15] MEDINIPUR WEST 

print("---- Details of wb : [15] MEDINIPUR WEST -------")
df_wb_15 = df_wb[df_wb.District_Name == 'MEDINIPUR WEST']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_15_1997 = df_wb_15.loc[df_wb_15['Crop_Year'] == 1997,'Area':'Production']
df_wb_15_1997_sum = df_wb_15_1997.sum(axis = 0, skipna = True)
print(df_wb_15_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_15_1998 = df_wb_15.loc[df_wb_15['Crop_Year'] == 1998,'Area':'Production']
df_wb_15_1998_sum = df_wb_15_1998.sum(axis = 0, skipna = True) 
print(df_wb_15_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_15_1999 = df_wb_15.loc[df_wb_15['Crop_Year'] == 1999,'Area':'Production']
df_wb_15_1999_sum = df_wb_15_1999.sum(axis = 0, skipna = True) 
print(df_wb_15_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_15_2000 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2000,'Area':'Production']
df_wb_15_2000_sum = df_wb_15_2000.sum(axis = 0, skipna = True) 
print(df_wb_15_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_15_2001 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_15_2001_sum = df_wb_15_2001.sum(axis = 0, skipna = True)
print(df_wb_15_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_15_2002 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2002,'Area':'Production']
df_wb_15_2002_sum = df_wb_15_2002.sum(axis = 0, skipna = True) 
print(df_wb_15_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_15_2003 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2003,'Area':'Production']
df_wb_15_2003_sum = df_wb_15_2003.sum(axis = 0, skipna = True) 
print(df_wb_15_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_15_2004 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2004,'Area':'Production']
df_wb_15_2004_sum = df_wb_15_2004.sum(axis = 0, skipna = True) 
print(df_wb_15_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_15_2005 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2005,'Area':'Production']
df_wb_15_2005_sum = df_wb_15_2005.sum(axis = 0, skipna = True) 
print(df_wb_15_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_15_2006 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_15_2006_sum = df_wb_15_2006.sum(axis = 0, skipna = True)
print(df_wb_15_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_15_2007 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2007,'Area':'Production']
df_wb_15_2007_sum = df_wb_15_2007.sum(axis = 0, skipna = True) 
print(df_wb_15_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_15_2008 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2008,'Area':'Production']
df_wb_15_2008_sum = df_wb_15_2008.sum(axis = 0, skipna = True) 
print(df_wb_15_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_15_2009 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2009,'Area':'Production']
df_wb_15_2009_sum = df_wb_15_2009.sum(axis = 0, skipna = True) 
print(df_wb_15_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_15_2010 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_15_2010_sum = df_wb_15_2010.sum(axis = 0, skipna = True)
print(df_wb_15_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_15_2011 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_15_2011_sum = df_wb_15_2011.sum(axis = 0, skipna = True)
print(df_wb_15_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_15_2012 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2012,'Area':'Production']
df_wb_15_2012_sum = df_wb_15_2012.sum(axis = 0, skipna = True) 
print(df_wb_15_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_15_2013 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_15_2013_sum = df_wb_15_2013.sum(axis = 0, skipna = True)
print(df_wb_15_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_15_2014 = df_wb_15.loc[df_wb_15['Crop_Year'] == 2014,'Area':'Production']
df_wb_15_2014_sum = df_wb_15_2014.sum(axis = 0, skipna = True) 
print(df_wb_15_2014_sum)
print("---------------------------------")
                 
# details of wb : [16] MURSHIDABAD

print("---- Details of wb : [16] MURSHIDABAD ----")
df_wb_16 = df_wb[df_wb.District_Name == 'MURSHIDABAD']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_16_1997 = df_wb_16.loc[df_wb_16['Crop_Year'] == 1997,'Area':'Production']
df_wb_16_1997_sum = df_wb_16_1997.sum(axis = 0, skipna = True)
print(df_wb_16_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_16_1998 = df_wb_16.loc[df_wb_16['Crop_Year'] == 1998,'Area':'Production']
df_wb_16_1998_sum = df_wb_16_1998.sum(axis = 0, skipna = True) 
print(df_wb_16_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_16_1999 = df_wb_16.loc[df_wb_16['Crop_Year'] == 1999,'Area':'Production']
df_wb_16_1999_sum = df_wb_16_1999.sum(axis = 0, skipna = True) 
print(df_wb_16_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_16_2000 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2000,'Area':'Production']
df_wb_16_2000_sum = df_wb_16_2000.sum(axis = 0, skipna = True) 
print(df_wb_16_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_16_2001 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_16_2001_sum = df_wb_16_2001.sum(axis = 0, skipna = True)
print(df_wb_16_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_16_2002 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2002,'Area':'Production']
df_wb_16_2002_sum = df_wb_16_2002.sum(axis = 0, skipna = True) 
print(df_wb_16_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_16_2003 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2003,'Area':'Production']
df_wb_16_2003_sum = df_wb_16_2003.sum(axis = 0, skipna = True) 
print(df_wb_16_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_16_2004 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2004,'Area':'Production']
df_wb_16_2004_sum = df_wb_16_2004.sum(axis = 0, skipna = True) 
print(df_wb_16_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_16_2005 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2005,'Area':'Production']
df_wb_16_2005_sum = df_wb_16_2005.sum(axis = 0, skipna = True) 
print(df_wb_16_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_16_2006 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_16_2006_sum = df_wb_16_2006.sum(axis = 0, skipna = True)
print(df_wb_16_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_16_2007 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2007,'Area':'Production']
df_wb_16_2007_sum = df_wb_16_2007.sum(axis = 0, skipna = True) 
print(df_wb_16_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_16_2008 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2008,'Area':'Production']
df_wb_16_2008_sum = df_wb_16_2008.sum(axis = 0, skipna = True) 
print(df_wb_16_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_16_2009 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2009,'Area':'Production']
df_wb_16_2009_sum = df_wb_16_2009.sum(axis = 0, skipna = True) 
print(df_wb_16_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_16_2010 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_16_2010_sum = df_wb_16_2010.sum(axis = 0, skipna = True)
print(df_wb_16_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_16_2011 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_16_2011_sum = df_wb_16_2011.sum(axis = 0, skipna = True)
print(df_wb_16_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_16_2012 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2012,'Area':'Production']
df_wb_16_2012_sum = df_wb_16_2012.sum(axis = 0, skipna = True) 
print(df_wb_16_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_16_2013 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_16_2013_sum = df_wb_16_2013.sum(axis = 0, skipna = True)
print(df_wb_16_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_16_2014 = df_wb_16.loc[df_wb_16['Crop_Year'] == 2014,'Area':'Production']
df_wb_16_2014_sum = df_wb_16_2014.sum(axis = 0, skipna = True) 
print(df_wb_16_2014_sum)
print("---------------------------------")
                                          
# details of wb : [17] NADIA 

print("---- Details of wb : [17] NADIA -----")
df_wb_17 = df_wb[df_wb.District_Name == 'NADIA']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_17_1997 = df_wb_17.loc[df_wb_17['Crop_Year'] == 1997,'Area':'Production']
df_wb_17_1997_sum = df_wb_17_1997.sum(axis = 0, skipna = True)
print(df_wb_17_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_17_1998 = df_wb_17.loc[df_wb_17['Crop_Year'] == 1998,'Area':'Production']
df_wb_17_1998_sum = df_wb_17_1998.sum(axis = 0, skipna = True) 
print(df_wb_17_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_17_1999 = df_wb_17.loc[df_wb_17['Crop_Year'] == 1999,'Area':'Production']
df_wb_17_1999_sum = df_wb_17_1999.sum(axis = 0, skipna = True) 
print(df_wb_17_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_17_2000 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2000,'Area':'Production']
df_wb_17_2000_sum = df_wb_17_2000.sum(axis = 0, skipna = True) 
print(df_wb_17_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_17_2001 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_17_2001_sum = df_wb_17_2001.sum(axis = 0, skipna = True)
print(df_wb_17_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_17_2002 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2002,'Area':'Production']
df_wb_17_2002_sum = df_wb_17_2002.sum(axis = 0, skipna = True) 
print(df_wb_17_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_17_2003 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2003,'Area':'Production']
df_wb_17_2003_sum = df_wb_17_2003.sum(axis = 0, skipna = True) 
print(df_wb_17_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_17_2004 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2004,'Area':'Production']
df_wb_17_2004_sum = df_wb_17_2004.sum(axis = 0, skipna = True) 
print(df_wb_17_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_17_2005 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2005,'Area':'Production']
df_wb_17_2005_sum = df_wb_17_2005.sum(axis = 0, skipna = True) 
print(df_wb_17_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_17_2006 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_17_2006_sum = df_wb_17_2006.sum(axis = 0, skipna = True)
print(df_wb_17_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_17_2007 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2007,'Area':'Production']
df_wb_17_2007_sum = df_wb_17_2007.sum(axis = 0, skipna = True) 
print(df_wb_17_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_17_2008 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2008,'Area':'Production']
df_wb_17_2008_sum = df_wb_17_2008.sum(axis = 0, skipna = True) 
print(df_wb_17_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_17_2009 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2009,'Area':'Production']
df_wb_17_2009_sum = df_wb_17_2009.sum(axis = 0, skipna = True) 
print(df_wb_17_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_17_2010 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_17_2010_sum = df_wb_17_2010.sum(axis = 0, skipna = True)
print(df_wb_17_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_17_2011 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_17_2011_sum = df_wb_17_2011.sum(axis = 0, skipna = True)
print(df_wb_17_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_17_2012 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2012,'Area':'Production']
df_wb_17_2012_sum = df_wb_17_2012.sum(axis = 0, skipna = True) 
print(df_wb_17_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_17_2013 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_17_2013_sum = df_wb_17_2013.sum(axis = 0, skipna = True)
print(df_wb_17_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_17_2014 = df_wb_17.loc[df_wb_17['Crop_Year'] == 2014,'Area':'Production']
df_wb_17_2014_sum = df_wb_17_2014.sum(axis = 0, skipna = True) 
print(df_wb_17_2014_sum)
print("---------------------------------")
                                               
# details of wb : [18] PURULIA  

print("---- Details of wb : [18] PURULIA -----")
df_wb_18 = df_wb[df_wb.District_Name == 'PURULIA']

# Select rows from year =( 1997 to 2014 ) and all columns between 'Area' and 'Production'

print("---------------------------------")
print("Data for Crop_Year = 1997")
print("---------------------------------")
df_wb_18_1997 = df_wb_18.loc[df_wb_18['Crop_Year'] == 1997,'Area':'Production']
df_wb_18_1997_sum = df_wb_18_1997.sum(axis = 0, skipna = True)
print(df_wb_18_1997_sum)
print("---------------------------------")
print("Data for Crop_Year = 1998")
print("---------------------------------")
df_wb_18_1998 = df_wb_18.loc[df_wb_18['Crop_Year'] == 1998,'Area':'Production']
df_wb_18_1998_sum = df_wb_18_1998.sum(axis = 0, skipna = True) 
print(df_wb_18_1998_sum)
print("---------------------------------")
print("Data for Crop_Year = 1999")
print("---------------------------------")
df_wb_18_1999 = df_wb_18.loc[df_wb_18['Crop_Year'] == 1999,'Area':'Production']
df_wb_18_1999_sum = df_wb_18_1999.sum(axis = 0, skipna = True) 
print(df_wb_18_1999_sum)
print("---------------------------------")
print("Data for Crop_Year = 2000")
print("---------------------------------")
df_wb_18_2000 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2000,'Area':'Production']
df_wb_18_2000_sum = df_wb_18_2000.sum(axis = 0, skipna = True) 
print(df_wb_18_2000_sum)
print("---------------------------------")
print("Data for Crop_Year = 2001")
print("---------------------------------")
df_wb_18_2001 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2001,'Area':'Production'] 
df_wb_18_2001_sum = df_wb_18_2001.sum(axis = 0, skipna = True)
print(df_wb_18_2001_sum)
print("---------------------------------")
print("Data for Crop_Year = 2002")
print("---------------------------------")
df_wb_18_2002 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2002,'Area':'Production']
df_wb_18_2002_sum = df_wb_18_2002.sum(axis = 0, skipna = True) 
print(df_wb_18_2002_sum)
print("---------------------------------")
print("Data for Crop_Year = 2003")
print("---------------------------------")
df_wb_18_2003 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2003,'Area':'Production']
df_wb_18_2003_sum = df_wb_18_2003.sum(axis = 0, skipna = True) 
print(df_wb_18_2003_sum)
print("---------------------------------")
print("Data for Crop_Year = 2004")
print("---------------------------------")
df_wb_18_2004 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2004,'Area':'Production']
df_wb_18_2004_sum = df_wb_18_2004.sum(axis = 0, skipna = True) 
print(df_wb_18_2004_sum)
print("---------------------------------")
print("Data for Crop_Year = 2005")
print("---------------------------------")
df_wb_18_2005 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2005,'Area':'Production']
df_wb_18_2005_sum = df_wb_18_2005.sum(axis = 0, skipna = True) 
print(df_wb_18_2005_sum)
print("---------------------------------")
print("Data for Crop_Year = 2006")
print("---------------------------------")
df_wb_18_2006 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2006,'Area':'Production'] 
df_wb_18_2006_sum = df_wb_18_2006.sum(axis = 0, skipna = True)
print(df_wb_18_2006_sum)
print("---------------------------------")
print("Data for Crop_Year = 2007")
print("---------------------------------")
df_wb_18_2007 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2007,'Area':'Production']
df_wb_18_2007_sum = df_wb_18_2007.sum(axis = 0, skipna = True) 
print(df_wb_18_2007_sum)
print("---------------------------------")
print("Data for Crop_Year = 2008")
print("---------------------------------")
df_wb_18_2008 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2008,'Area':'Production']
df_wb_18_2008_sum = df_wb_18_2008.sum(axis = 0, skipna = True) 
print(df_wb_18_2008_sum)
print("---------------------------------")
print("Data for Crop_Year = 2009")
print("---------------------------------")
df_wb_18_2009 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2009,'Area':'Production']
df_wb_18_2009_sum = df_wb_18_2009.sum(axis = 0, skipna = True) 
print(df_wb_18_2009_sum)
print("---------------------------------")
print("Data for Crop_Year = 2010")
print("---------------------------------")
df_wb_18_2010 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2010,'Area':'Production'] 
df_wb_18_2010_sum = df_wb_18_2010.sum(axis = 0, skipna = True)
print(df_wb_18_2010_sum)
print("---------------------------------")
print("Data for Crop_Year = 2011")
print("---------------------------------")
df_wb_18_2011 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2011,'Area':'Production'] 
df_wb_18_2011_sum = df_wb_18_2011.sum(axis = 0, skipna = True)
print(df_wb_18_2011_sum)
print("---------------------------------")
print("Data for Crop_Year = 2012")
print("---------------------------------")
df_wb_18_2012 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2012,'Area':'Production']
df_wb_18_2012_sum = df_wb_18_2012.sum(axis = 0, skipna = True) 
print(df_wb_18_2012_sum)
print("---------------------------------")
print("Data for Crop_Year = 2013")
print("---------------------------------")
df_wb_18_2013 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2013,'Area':'Production'] 
df_wb_18_2013_sum = df_wb_18_2013.sum(axis = 0, skipna = True)
print(df_wb_18_2013_sum)
print("---------------------------------")
print("Data for Crop_Year = 2014")
print("---------------------------------")
df_wb_18_2014 = df_wb_18.loc[df_wb_18['Crop_Year'] == 2014,'Area':'Production']
df_wb_18_2014_sum = df_wb_18_2014.sum(axis = 0, skipna = True) 
print(df_wb_18_2014_sum)
print("---------------------------------")

# plotting of Andaman( [1] Nicobars) 'Area' and 'Production' 

x = ('2000','2001','2002','2003','2004','2005','2006','2010')

y1 = (df_andaman_1_2000_sum['Area'],
      df_andaman_1_2001_sum['Area'], 
      df_andaman_1_2002_sum['Area'],
      df_andaman_1_2003_sum['Area'],
      df_andaman_1_2004_sum['Area'],
      df_andaman_1_2005_sum['Area'],
      df_andaman_1_2006_sum['Area'],
      df_andaman_1_2010_sum['Area'])

y2 = (df_andaman_1_2000_sum['Production'],
      df_andaman_1_2001_sum['Production'], 
      df_andaman_1_2002_sum['Production'],
      df_andaman_1_2003_sum['Production'],
      df_andaman_1_2004_sum['Production'],
      df_andaman_1_2005_sum['Production'],
      df_andaman_1_2006_sum['Production'],
      df_andaman_1_2010_sum['Production'])                                      

plt.subplot(121)
plt.title('State-1 : Andaman( [1] Nicobars) (Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x,y1)
plt.show

plt.subplot(122)
plt.title('State-1 : Andaman( [1] Nicobars) (production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x,y2)
plt.show()

# plotting of Andaman( [2] NORTH AND MIDDLE ANDAMAN ) 'Area' and 'Production' 

x = ('2000','2001','2002','2003','2004','2005','2006','2010')

y1 = (df_andaman_2_2000_sum['Area'],
      df_andaman_2_2001_sum['Area'], 
      df_andaman_2_2002_sum['Area'],
      df_andaman_2_2003_sum['Area'],
      df_andaman_2_2004_sum['Area'],
      df_andaman_2_2005_sum['Area'],
      df_andaman_2_2006_sum['Area'],
      df_andaman_2_2010_sum['Area'])

y2 = (df_andaman_2_2000_sum['Production'],
      df_andaman_2_2001_sum['Production'], 
      df_andaman_2_2002_sum['Production'],
      df_andaman_2_2003_sum['Production'],
      df_andaman_2_2004_sum['Production'],
      df_andaman_2_2005_sum['Production'],
      df_andaman_2_2006_sum['Production'],
      df_andaman_2_2010_sum['Production'])                                      

plt.subplot(121)
plt.title('State-1 : Andaman( [2] NORTH AND MIDDLE ANDAMAN)(Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x,y1)
plt.show

plt.subplot(122)
plt.title('State-1 : Andaman( [2] NORTH AND MIDDLE ANDAMAN ) (production)')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x,y2)
plt.show()

# plotting of  Andaman( [3] SOUTH ANDAMANS ) 'Area' and 'Production' 

x = ('2000','2001','2002','2003','2004','2005','2006','2010')

y1 = (df_andaman_3_2000_sum['Area'],
      df_andaman_3_2001_sum['Area'], 
      df_andaman_3_2002_sum['Area'],
      df_andaman_3_2003_sum['Area'],
      df_andaman_3_2004_sum['Area'],
      df_andaman_3_2005_sum['Area'],
      df_andaman_3_2006_sum['Area'],
      df_andaman_3_2010_sum['Area'])

y2 = (df_andaman_3_2000_sum['Production'],
      df_andaman_3_2001_sum['Production'], 
      df_andaman_3_2002_sum['Production'],
      df_andaman_3_2003_sum['Production'],
      df_andaman_3_2004_sum['Production'],
      df_andaman_3_2005_sum['Production'],
      df_andaman_3_2006_sum['Production'],
      df_andaman_3_2010_sum['Production'])                                      

plt.subplot(121)
plt.title('State-1 :  Andaman( [3] SOUTH ANDAMANS ) (Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x,y1)
plt.show

plt.subplot(122)
plt.title('State-1 :  Andaman( [3] SOUTH ANDAMANS )(production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x,y2)
plt.show()

# plotting  Andhra( [1] ANANTAPUR )

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_andhra_1_1997_sum['Area'],
      df_andhra_1_1998_sum['Area'],
      df_andhra_1_1999_sum['Area'],
      df_andhra_1_2000_sum['Area'],
      df_andhra_1_2001_sum['Area'], 
      df_andhra_1_2002_sum['Area'],
      df_andhra_1_2003_sum['Area'],
      df_andhra_1_2004_sum['Area'],
      df_andhra_1_2005_sum['Area'],
      df_andhra_1_2006_sum['Area'],
      df_andhra_1_2007_sum['Area'],
      df_andhra_1_2008_sum['Area'],
      df_andhra_1_2009_sum['Area'],
      df_andhra_1_2010_sum['Area'],
      df_andhra_1_2011_sum['Area'],
      df_andhra_1_2012_sum['Area'],
      df_andhra_1_2013_sum['Area'],
      df_andhra_1_2014_sum['Area'])

y22 =(df_andhra_1_1997_sum['Production'],
      df_andhra_1_1998_sum['Production'],
      df_andhra_1_1999_sum['Production'],
      df_andhra_1_2000_sum['Production'],
      df_andhra_1_2001_sum['Production'], 
      df_andhra_1_2002_sum['Production'],
      df_andhra_1_2003_sum['Production'],
      df_andhra_1_2004_sum['Production'],
      df_andhra_1_2005_sum['Production'],
      df_andhra_1_2006_sum['Production'],
      df_andhra_1_2007_sum['Production'],
      df_andhra_1_2008_sum['Production'],
      df_andhra_1_2009_sum['Production'],
      df_andhra_1_2010_sum['Production'],
      df_andhra_1_2011_sum['Production'],
      df_andhra_1_2012_sum['Production'],
      df_andhra_1_2013_sum['Production'],
      df_andhra_1_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-2 : Andhra( [1] ANANTAPUR )(Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-2 : Andhra( [1] ANANTAPUR )(production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()
           
# plotting Andhra( [2] CHITTOOR )

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_andhra_2_1997_sum['Area'],
      df_andhra_2_1998_sum['Area'],
      df_andhra_2_1999_sum['Area'],
      df_andhra_2_2000_sum['Area'],
      df_andhra_2_2001_sum['Area'], 
      df_andhra_2_2002_sum['Area'],
      df_andhra_2_2003_sum['Area'],
      df_andhra_2_2004_sum['Area'],
      df_andhra_2_2005_sum['Area'],
      df_andhra_2_2006_sum['Area'],
      df_andhra_2_2007_sum['Area'],
      df_andhra_2_2008_sum['Area'],
      df_andhra_2_2009_sum['Area'],
      df_andhra_2_2010_sum['Area'],
      df_andhra_2_2011_sum['Area'],
      df_andhra_2_2012_sum['Area'],
      df_andhra_2_2013_sum['Area'],
      df_andhra_2_2014_sum['Area'])

y22 =(df_andhra_2_1997_sum['Production'],
      df_andhra_2_1998_sum['Production'],
      df_andhra_2_1999_sum['Production'],
      df_andhra_2_2000_sum['Production'],
      df_andhra_2_2001_sum['Production'], 
      df_andhra_2_2002_sum['Production'],
      df_andhra_2_2003_sum['Production'],
      df_andhra_2_2004_sum['Production'],
      df_andhra_2_2005_sum['Production'],
      df_andhra_2_2006_sum['Production'],
      df_andhra_2_2007_sum['Production'],
      df_andhra_2_2008_sum['Production'],
      df_andhra_2_2009_sum['Production'],
      df_andhra_2_2010_sum['Production'],
      df_andhra_2_2011_sum['Production'],
      df_andhra_2_2012_sum['Production'],
      df_andhra_2_2013_sum['Production'],
      df_andhra_2_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-2 : Andhra( [2] CHITTOOR )(Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-2 : Andhra( [2] CHITTOOR )(production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting Andhra( [3] EAST GODAVARI )

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_andhra_3_1997_sum['Area'],
      df_andhra_3_1998_sum['Area'],
      df_andhra_3_1999_sum['Area'],
      df_andhra_3_2000_sum['Area'],
      df_andhra_3_2001_sum['Area'], 
      df_andhra_3_2002_sum['Area'],
      df_andhra_3_2003_sum['Area'],
      df_andhra_3_2004_sum['Area'],
      df_andhra_3_2005_sum['Area'],
      df_andhra_3_2006_sum['Area'],
      df_andhra_3_2007_sum['Area'],
      df_andhra_3_2008_sum['Area'],
      df_andhra_3_2009_sum['Area'],
      df_andhra_3_2010_sum['Area'],
      df_andhra_3_2011_sum['Area'],
      df_andhra_3_2012_sum['Area'],
      df_andhra_3_2013_sum['Area'],
      df_andhra_3_2014_sum['Area'])

y22 =(df_andhra_3_1997_sum['Production'],
      df_andhra_3_1998_sum['Production'],
      df_andhra_3_1999_sum['Production'],
      df_andhra_3_2000_sum['Production'],
      df_andhra_3_2001_sum['Production'], 
      df_andhra_3_2002_sum['Production'],
      df_andhra_3_2003_sum['Production'],
      df_andhra_3_2004_sum['Production'],
      df_andhra_3_2005_sum['Production'],
      df_andhra_3_2006_sum['Production'],
      df_andhra_3_2007_sum['Production'],
      df_andhra_3_2008_sum['Production'],
      df_andhra_3_2009_sum['Production'],
      df_andhra_3_2010_sum['Production'],
      df_andhra_3_2011_sum['Production'],
      df_andhra_3_2012_sum['Production'],
      df_andhra_3_2013_sum['Production'],
      df_andhra_3_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-2 : Andhra( [3] EAST GODAVARI )(Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-2 : Andhra( [3] EAST GODAVARI )(production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting Andhra( [4] GUNTUR )

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_andhra_4_1997_sum['Area'],
      df_andhra_4_1998_sum['Area'],
      df_andhra_4_1999_sum['Area'],
      df_andhra_4_2000_sum['Area'],
      df_andhra_4_2001_sum['Area'], 
      df_andhra_4_2002_sum['Area'],
      df_andhra_4_2003_sum['Area'],
      df_andhra_4_2004_sum['Area'],
      df_andhra_4_2005_sum['Area'],
      df_andhra_4_2006_sum['Area'],
      df_andhra_4_2007_sum['Area'],
      df_andhra_4_2008_sum['Area'],
      df_andhra_4_2009_sum['Area'],
      df_andhra_4_2010_sum['Area'],
      df_andhra_4_2011_sum['Area'],
      df_andhra_4_2012_sum['Area'],
      df_andhra_4_2013_sum['Area'],
      df_andhra_4_2014_sum['Area'])

y22 =(df_andhra_4_1997_sum['Production'],
      df_andhra_4_1998_sum['Production'],
      df_andhra_4_1999_sum['Production'],
      df_andhra_4_2000_sum['Production'],
      df_andhra_4_2001_sum['Production'], 
      df_andhra_4_2002_sum['Production'],
      df_andhra_4_2003_sum['Production'],
      df_andhra_4_2004_sum['Production'],
      df_andhra_4_2005_sum['Production'],
      df_andhra_4_2006_sum['Production'],
      df_andhra_4_2007_sum['Production'],
      df_andhra_4_2008_sum['Production'],
      df_andhra_4_2009_sum['Production'],
      df_andhra_4_2010_sum['Production'],
      df_andhra_4_2011_sum['Production'],
      df_andhra_4_2012_sum['Production'],
      df_andhra_4_2013_sum['Production'],
      df_andhra_4_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-2 : Andhra( [4] GUNTUR )(Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-2 : Andhra( [4] GUNTUR )(production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting Andhra( [5] KADAPA )

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_andhra_5_1997_sum['Area'],
      df_andhra_5_1998_sum['Area'],
      df_andhra_5_1999_sum['Area'],
      df_andhra_5_2000_sum['Area'],
      df_andhra_5_2001_sum['Area'], 
      df_andhra_5_2002_sum['Area'],
      df_andhra_5_2003_sum['Area'],
      df_andhra_5_2004_sum['Area'],
      df_andhra_5_2005_sum['Area'],
      df_andhra_5_2006_sum['Area'],
      df_andhra_5_2007_sum['Area'],
      df_andhra_5_2008_sum['Area'],
      df_andhra_5_2009_sum['Area'],
      df_andhra_5_2010_sum['Area'],
      df_andhra_5_2011_sum['Area'],
      df_andhra_5_2012_sum['Area'],
      df_andhra_5_2013_sum['Area'],
      df_andhra_5_2014_sum['Area'])

y22 =(df_andhra_5_1997_sum['Production'],
      df_andhra_5_1998_sum['Production'],
      df_andhra_5_1999_sum['Production'],
      df_andhra_5_2000_sum['Production'],
      df_andhra_5_2001_sum['Production'], 
      df_andhra_5_2002_sum['Production'],
      df_andhra_5_2003_sum['Production'],
      df_andhra_5_2004_sum['Production'],
      df_andhra_5_2005_sum['Production'],
      df_andhra_5_2006_sum['Production'],
      df_andhra_5_2007_sum['Production'],
      df_andhra_5_2008_sum['Production'],
      df_andhra_5_2009_sum['Production'],
      df_andhra_5_2010_sum['Production'],
      df_andhra_5_2011_sum['Production'],
      df_andhra_5_2012_sum['Production'],
      df_andhra_5_2013_sum['Production'],
      df_andhra_5_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-2 : Andhra( [5] KADAPA )(Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-2 : Andhra( [5] KADAPA )(production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting Andhra( [6] KRISHNA )

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_andhra_6_1997_sum['Area'],
      df_andhra_6_1998_sum['Area'],
      df_andhra_6_1999_sum['Area'],
      df_andhra_6_2000_sum['Area'],
      df_andhra_6_2001_sum['Area'], 
      df_andhra_6_2002_sum['Area'],
      df_andhra_6_2003_sum['Area'],
      df_andhra_6_2004_sum['Area'],
      df_andhra_6_2005_sum['Area'],
      df_andhra_6_2006_sum['Area'],
      df_andhra_6_2007_sum['Area'],
      df_andhra_6_2008_sum['Area'],
      df_andhra_6_2009_sum['Area'],
      df_andhra_6_2010_sum['Area'],
      df_andhra_6_2011_sum['Area'],
      df_andhra_6_2012_sum['Area'],
      df_andhra_6_2013_sum['Area'],
      df_andhra_6_2014_sum['Area'])

y22 =(df_andhra_6_1997_sum['Production'],
      df_andhra_6_1998_sum['Production'],
      df_andhra_6_1999_sum['Production'],
      df_andhra_6_2000_sum['Production'],
      df_andhra_6_2001_sum['Production'], 
      df_andhra_6_2002_sum['Production'],
      df_andhra_6_2003_sum['Production'],
      df_andhra_6_2004_sum['Production'],
      df_andhra_6_2005_sum['Production'],
      df_andhra_6_2006_sum['Production'],
      df_andhra_6_2007_sum['Production'],
      df_andhra_6_2008_sum['Production'],
      df_andhra_6_2009_sum['Production'],
      df_andhra_6_2010_sum['Production'],
      df_andhra_6_2011_sum['Production'],
      df_andhra_6_2012_sum['Production'],
      df_andhra_6_2013_sum['Production'],
      df_andhra_6_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-2 : Andhra( [6] KRISHNA )(Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-2 : Andhra( [6] KRISHNA )(production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting Andhra( [7] KURNOOL)

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_andhra_7_1997_sum['Area'],
      df_andhra_7_1998_sum['Area'],
      df_andhra_7_1999_sum['Area'],
      df_andhra_7_2000_sum['Area'],
      df_andhra_7_2001_sum['Area'], 
      df_andhra_7_2002_sum['Area'],
      df_andhra_7_2003_sum['Area'],
      df_andhra_7_2004_sum['Area'],
      df_andhra_7_2005_sum['Area'],
      df_andhra_7_2006_sum['Area'],
      df_andhra_7_2007_sum['Area'],
      df_andhra_7_2008_sum['Area'],
      df_andhra_7_2009_sum['Area'],
      df_andhra_7_2010_sum['Area'],
      df_andhra_7_2011_sum['Area'],
      df_andhra_7_2012_sum['Area'],
      df_andhra_7_2013_sum['Area'],
      df_andhra_7_2014_sum['Area'])

y22 =(df_andhra_7_1997_sum['Production'],
      df_andhra_7_1998_sum['Production'],
      df_andhra_7_1999_sum['Production'],
      df_andhra_7_2000_sum['Production'],
      df_andhra_7_2001_sum['Production'], 
      df_andhra_7_2002_sum['Production'],
      df_andhra_7_2003_sum['Production'],
      df_andhra_7_2004_sum['Production'],
      df_andhra_7_2005_sum['Production'],
      df_andhra_7_2006_sum['Production'],
      df_andhra_7_2007_sum['Production'],
      df_andhra_7_2008_sum['Production'],
      df_andhra_7_2009_sum['Production'],
      df_andhra_7_2010_sum['Production'],
      df_andhra_7_2011_sum['Production'],
      df_andhra_7_2012_sum['Production'],
      df_andhra_7_2013_sum['Production'],
      df_andhra_7_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-2 : Andhra( [7] KURNOOL)(Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-2 : Andhra( [7] KURNOOL)(production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting Andhra( [8] PRAKASAM )

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_andhra_8_1997_sum['Area'],
      df_andhra_8_1998_sum['Area'],
      df_andhra_8_1999_sum['Area'],
      df_andhra_8_2000_sum['Area'],
      df_andhra_8_2001_sum['Area'], 
      df_andhra_8_2002_sum['Area'],
      df_andhra_8_2003_sum['Area'],
      df_andhra_8_2004_sum['Area'],
      df_andhra_8_2005_sum['Area'],
      df_andhra_8_2006_sum['Area'],
      df_andhra_8_2007_sum['Area'],
      df_andhra_8_2008_sum['Area'],
      df_andhra_8_2009_sum['Area'],
      df_andhra_8_2010_sum['Area'],
      df_andhra_8_2011_sum['Area'],
      df_andhra_8_2012_sum['Area'],
      df_andhra_8_2013_sum['Area'],
      df_andhra_8_2014_sum['Area'])

y22 =(df_andhra_8_1997_sum['Production'],
      df_andhra_8_1998_sum['Production'],
      df_andhra_8_1999_sum['Production'],
      df_andhra_8_2000_sum['Production'],
      df_andhra_8_2001_sum['Production'], 
      df_andhra_8_2002_sum['Production'],
      df_andhra_8_2003_sum['Production'],
      df_andhra_8_2004_sum['Production'],
      df_andhra_8_2005_sum['Production'],
      df_andhra_8_2006_sum['Production'],
      df_andhra_8_2007_sum['Production'],
      df_andhra_8_2008_sum['Production'],
      df_andhra_8_2009_sum['Production'],
      df_andhra_8_2010_sum['Production'],
      df_andhra_8_2011_sum['Production'],
      df_andhra_8_2012_sum['Production'],
      df_andhra_8_2013_sum['Production'],
      df_andhra_8_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-2 : Andhra( [8] PRAKASAM )(Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-2 : Andhra( [8] PRAKASAM )(production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting Andhra( [9] SPSR NELLORE)

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_andhra_9_1997_sum['Area'],
      df_andhra_9_1998_sum['Area'],
      df_andhra_9_1999_sum['Area'],
      df_andhra_9_2000_sum['Area'],
      df_andhra_9_2001_sum['Area'], 
      df_andhra_9_2002_sum['Area'],
      df_andhra_9_2003_sum['Area'],
      df_andhra_9_2004_sum['Area'],
      df_andhra_9_2005_sum['Area'],
      df_andhra_9_2006_sum['Area'],
      df_andhra_9_2007_sum['Area'],
      df_andhra_9_2008_sum['Area'],
      df_andhra_9_2009_sum['Area'],
      df_andhra_9_2010_sum['Area'],
      df_andhra_9_2011_sum['Area'],
      df_andhra_9_2012_sum['Area'],
      df_andhra_9_2013_sum['Area'],
      df_andhra_9_2014_sum['Area'])

y22 =(df_andhra_9_1997_sum['Production'],
      df_andhra_9_1998_sum['Production'],
      df_andhra_9_1999_sum['Production'],
      df_andhra_9_2000_sum['Production'],
      df_andhra_9_2001_sum['Production'], 
      df_andhra_9_2002_sum['Production'],
      df_andhra_9_2003_sum['Production'],
      df_andhra_9_2004_sum['Production'],
      df_andhra_9_2005_sum['Production'],
      df_andhra_9_2006_sum['Production'],
      df_andhra_9_2007_sum['Production'],
      df_andhra_9_2008_sum['Production'],
      df_andhra_9_2009_sum['Production'],
      df_andhra_9_2010_sum['Production'],
      df_andhra_9_2011_sum['Production'],
      df_andhra_9_2012_sum['Production'],
      df_andhra_9_2013_sum['Production'],
      df_andhra_9_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-2 : Andhra( [9] SPSR NELLORE)(Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-2 : Andhra( [9] SPSR NELLORE)(production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting Andhra( [10] SRIKAKULAM )

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_andhra_10_1997_sum['Area'],
      df_andhra_10_1998_sum['Area'],
      df_andhra_10_1999_sum['Area'],
      df_andhra_10_2000_sum['Area'],
      df_andhra_10_2001_sum['Area'], 
      df_andhra_10_2002_sum['Area'],
      df_andhra_10_2003_sum['Area'],
      df_andhra_10_2004_sum['Area'],
      df_andhra_10_2005_sum['Area'],
      df_andhra_10_2006_sum['Area'],
      df_andhra_10_2007_sum['Area'],
      df_andhra_10_2008_sum['Area'],
      df_andhra_10_2009_sum['Area'],
      df_andhra_10_2010_sum['Area'],
      df_andhra_10_2011_sum['Area'],
      df_andhra_10_2012_sum['Area'],
      df_andhra_10_2013_sum['Area'],
      df_andhra_10_2014_sum['Area'])

y22 =(df_andhra_10_1997_sum['Production'],
      df_andhra_10_1998_sum['Production'],
      df_andhra_10_1999_sum['Production'],
      df_andhra_10_2000_sum['Production'],
      df_andhra_10_2001_sum['Production'], 
      df_andhra_10_2002_sum['Production'],
      df_andhra_10_2003_sum['Production'],
      df_andhra_10_2004_sum['Production'],
      df_andhra_10_2005_sum['Production'],
      df_andhra_10_2006_sum['Production'],
      df_andhra_10_2007_sum['Production'],
      df_andhra_10_2008_sum['Production'],
      df_andhra_10_2009_sum['Production'],
      df_andhra_10_2010_sum['Production'],
      df_andhra_10_2011_sum['Production'],
      df_andhra_10_2012_sum['Production'],
      df_andhra_10_2013_sum['Production'],
      df_andhra_10_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-2 : Andhra( [10] SRIKAKULAM )(Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-2 : Andhra( [10] SRIKAKULAM )(production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting Andhra( [11] VISAKHAPATANAM )

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_andhra_11_1997_sum['Area'],
      df_andhra_11_1998_sum['Area'],
      df_andhra_11_1999_sum['Area'],
      df_andhra_11_2000_sum['Area'],
      df_andhra_11_2001_sum['Area'], 
      df_andhra_11_2002_sum['Area'],
      df_andhra_11_2003_sum['Area'],
      df_andhra_11_2004_sum['Area'],
      df_andhra_11_2005_sum['Area'],
      df_andhra_11_2006_sum['Area'],
      df_andhra_11_2007_sum['Area'],
      df_andhra_11_2008_sum['Area'],
      df_andhra_11_2009_sum['Area'],
      df_andhra_11_2010_sum['Area'],
      df_andhra_11_2011_sum['Area'],
      df_andhra_11_2012_sum['Area'],
      df_andhra_11_2013_sum['Area'],
      df_andhra_11_2014_sum['Area'])

y22 =(df_andhra_11_1997_sum['Production'],
      df_andhra_11_1998_sum['Production'],
      df_andhra_11_1999_sum['Production'],
      df_andhra_11_2000_sum['Production'],
      df_andhra_11_2001_sum['Production'], 
      df_andhra_11_2002_sum['Production'],
      df_andhra_11_2003_sum['Production'],
      df_andhra_11_2004_sum['Production'],
      df_andhra_11_2005_sum['Production'],
      df_andhra_11_2006_sum['Production'],
      df_andhra_11_2007_sum['Production'],
      df_andhra_11_2008_sum['Production'],
      df_andhra_11_2009_sum['Production'],
      df_andhra_11_2010_sum['Production'],
      df_andhra_11_2011_sum['Production'],
      df_andhra_11_2012_sum['Production'],
      df_andhra_11_2013_sum['Production'],
      df_andhra_11_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-2 : Andhra( [11] VISAKHAPATANAM )(Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-2 : Andhra( [11] VISAKHAPATANAM )(production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting Andhra( [12] VIZIANAGARAM )

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_andhra_12_1997_sum['Area'],
      df_andhra_12_1998_sum['Area'],
      df_andhra_12_1999_sum['Area'],
      df_andhra_12_2000_sum['Area'],
      df_andhra_12_2001_sum['Area'], 
      df_andhra_12_2002_sum['Area'],
      df_andhra_12_2003_sum['Area'],
      df_andhra_12_2004_sum['Area'],
      df_andhra_12_2005_sum['Area'],
      df_andhra_12_2006_sum['Area'],
      df_andhra_12_2007_sum['Area'],
      df_andhra_12_2008_sum['Area'],
      df_andhra_12_2009_sum['Area'],
      df_andhra_12_2010_sum['Area'],
      df_andhra_12_2011_sum['Area'],
      df_andhra_12_2012_sum['Area'],
      df_andhra_12_2013_sum['Area'],
      df_andhra_12_2014_sum['Area'])

y22 =(df_andhra_12_1997_sum['Production'],
      df_andhra_12_1998_sum['Production'],
      df_andhra_12_1999_sum['Production'],
      df_andhra_12_2000_sum['Production'],
      df_andhra_12_2001_sum['Production'], 
      df_andhra_12_2002_sum['Production'],
      df_andhra_12_2003_sum['Production'],
      df_andhra_12_2004_sum['Production'],
      df_andhra_12_2005_sum['Production'],
      df_andhra_12_2006_sum['Production'],
      df_andhra_12_2007_sum['Production'],
      df_andhra_12_2008_sum['Production'],
      df_andhra_12_2009_sum['Production'],
      df_andhra_12_2010_sum['Production'],
      df_andhra_12_2011_sum['Production'],
      df_andhra_12_2012_sum['Production'],
      df_andhra_12_2013_sum['Production'],
      df_andhra_12_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-2 : Andhra( [12] VIZIANAGARAM )(Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-2 : Andhra( [12] VIZIANAGARAM )(production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting Andhra( [13] WEST GODAVARI )

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_andhra_13_1997_sum['Area'],
      df_andhra_13_1998_sum['Area'],
      df_andhra_13_1999_sum['Area'],
      df_andhra_13_2000_sum['Area'],
      df_andhra_13_2001_sum['Area'], 
      df_andhra_13_2002_sum['Area'],
      df_andhra_13_2003_sum['Area'],
      df_andhra_13_2004_sum['Area'],
      df_andhra_13_2005_sum['Area'],
      df_andhra_13_2006_sum['Area'],
      df_andhra_13_2007_sum['Area'],
      df_andhra_13_2008_sum['Area'],
      df_andhra_13_2009_sum['Area'],
      df_andhra_13_2010_sum['Area'],
      df_andhra_13_2011_sum['Area'],
      df_andhra_13_2012_sum['Area'],
      df_andhra_13_2013_sum['Area'],
      df_andhra_13_2014_sum['Area'])

y22 =(df_andhra_13_1997_sum['Production'],
      df_andhra_13_1998_sum['Production'],
      df_andhra_13_1999_sum['Production'],
      df_andhra_13_2000_sum['Production'],
      df_andhra_13_2001_sum['Production'], 
      df_andhra_13_2002_sum['Production'],
      df_andhra_13_2003_sum['Production'],
      df_andhra_13_2004_sum['Production'],
      df_andhra_13_2005_sum['Production'],
      df_andhra_13_2006_sum['Production'],
      df_andhra_13_2007_sum['Production'],
      df_andhra_13_2008_sum['Production'],
      df_andhra_13_2009_sum['Production'],
      df_andhra_13_2010_sum['Production'],
      df_andhra_13_2011_sum['Production'],
      df_andhra_13_2012_sum['Production'],
      df_andhra_13_2013_sum['Production'],
      df_andhra_13_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-2 : Andhra( [13] WEST GODAVARI )(Area)')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-2 : Andhra( [13] WEST GODAVARI )(production )')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()
                                                                                                                                                                                                                                                                                                                                                                                                                          
# plotting of Arunachal Pradesh 'Area' and 'Production'
# plotting  A.P : [1] ANJAW                                                                                                                                                  

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_1_1997_sum['Area'],
      df_arunachal_1_1998_sum['Area'],
      df_arunachal_1_1999_sum['Area'],
      df_arunachal_1_2000_sum['Area'],
      df_arunachal_1_2001_sum['Area'], 
      df_arunachal_1_2002_sum['Area'],
      df_arunachal_1_2003_sum['Area'],
      df_arunachal_1_2004_sum['Area'],
      df_arunachal_1_2005_sum['Area'],
      df_arunachal_1_2006_sum['Area'],
      df_arunachal_1_2007_sum['Area'],
      df_arunachal_1_2008_sum['Area'],
      df_arunachal_1_2009_sum['Area'],
      df_arunachal_1_2010_sum['Area'],
      df_arunachal_1_2011_sum['Area'],
      df_arunachal_1_2012_sum['Area'],
      df_arunachal_1_2013_sum['Area'],
      df_arunachal_1_2014_sum['Area'])

y22 =(df_arunachal_1_1997_sum['Production'],
      df_arunachal_1_1998_sum['Production'],
      df_arunachal_1_1999_sum['Production'],
      df_arunachal_1_2000_sum['Production'],
      df_arunachal_1_2001_sum['Production'], 
      df_arunachal_1_2002_sum['Production'],
      df_arunachal_1_2003_sum['Production'],
      df_arunachal_1_2004_sum['Production'],
      df_arunachal_1_2005_sum['Production'],
      df_arunachal_1_2006_sum['Production'],
      df_arunachal_1_2007_sum['Production'],
      df_arunachal_1_2008_sum['Production'],
      df_arunachal_1_2009_sum['Production'],
      df_arunachal_1_2010_sum['Production'],
      df_arunachal_1_2011_sum['Production'],
      df_arunachal_1_2012_sum['Production'],
      df_arunachal_1_2013_sum['Production'],
      df_arunachal_1_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [1] ANJAW (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [1] ANJAW (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()                                                                                                                                                                                                                                                                                                                                                                                                                                                

# plotting  A.P : [2] CHANGLANG

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_2_1997_sum['Area'],
      df_arunachal_2_1998_sum['Area'],
      df_arunachal_2_1999_sum['Area'],
      df_arunachal_2_2000_sum['Area'],
      df_arunachal_2_2001_sum['Area'], 
      df_arunachal_2_2002_sum['Area'],
      df_arunachal_2_2003_sum['Area'],
      df_arunachal_2_2004_sum['Area'],
      df_arunachal_2_2005_sum['Area'],
      df_arunachal_2_2006_sum['Area'],
      df_arunachal_2_2007_sum['Area'],
      df_arunachal_2_2008_sum['Area'],
      df_arunachal_2_2009_sum['Area'],
      df_arunachal_2_2010_sum['Area'],
      df_arunachal_2_2011_sum['Area'],
      df_arunachal_2_2012_sum['Area'],
      df_arunachal_2_2013_sum['Area'],
      df_arunachal_2_2014_sum['Area'])

y22 =(df_arunachal_2_1997_sum['Production'],
      df_arunachal_2_1998_sum['Production'],
      df_arunachal_2_1999_sum['Production'],
      df_arunachal_2_2000_sum['Production'],
      df_arunachal_2_2001_sum['Production'], 
      df_arunachal_2_2002_sum['Production'],
      df_arunachal_2_2003_sum['Production'],
      df_arunachal_2_2004_sum['Production'],
      df_arunachal_2_2005_sum['Production'],
      df_arunachal_2_2006_sum['Production'],
      df_arunachal_2_2007_sum['Production'],
      df_arunachal_2_2008_sum['Production'],
      df_arunachal_2_2009_sum['Production'],
      df_arunachal_2_2010_sum['Production'],
      df_arunachal_2_2011_sum['Production'],
      df_arunachal_2_2012_sum['Production'],
      df_arunachal_2_2013_sum['Production'],
      df_arunachal_2_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [2] CHANGLANG (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [2] CHANGLANG (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  A.P : [3] DIBANG VALLEY

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_3_1997_sum['Area'],
      df_arunachal_3_1998_sum['Area'],
      df_arunachal_3_1999_sum['Area'],
      df_arunachal_3_2000_sum['Area'],
      df_arunachal_3_2001_sum['Area'], 
      df_arunachal_3_2002_sum['Area'],
      df_arunachal_3_2003_sum['Area'],
      df_arunachal_3_2004_sum['Area'],
      df_arunachal_3_2005_sum['Area'],
      df_arunachal_3_2006_sum['Area'],
      df_arunachal_3_2007_sum['Area'],
      df_arunachal_3_2008_sum['Area'],
      df_arunachal_3_2009_sum['Area'],
      df_arunachal_3_2010_sum['Area'],
      df_arunachal_3_2011_sum['Area'],
      df_arunachal_3_2012_sum['Area'],
      df_arunachal_3_2013_sum['Area'],
      df_arunachal_3_2014_sum['Area'])

y22 =(df_arunachal_3_1997_sum['Production'],
      df_arunachal_3_1998_sum['Production'],
      df_arunachal_3_1999_sum['Production'],
      df_arunachal_3_2000_sum['Production'],
      df_arunachal_3_2001_sum['Production'], 
      df_arunachal_3_2002_sum['Production'],
      df_arunachal_3_2003_sum['Production'],
      df_arunachal_3_2004_sum['Production'],
      df_arunachal_3_2005_sum['Production'],
      df_arunachal_3_2006_sum['Production'],
      df_arunachal_3_2007_sum['Production'],
      df_arunachal_3_2008_sum['Production'],
      df_arunachal_3_2009_sum['Production'],
      df_arunachal_3_2010_sum['Production'],
      df_arunachal_3_2011_sum['Production'],
      df_arunachal_3_2012_sum['Production'],
      df_arunachal_3_2013_sum['Production'],
      df_arunachal_3_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [3] DIBANG VALLEY :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [3] DIBANG VALLEY :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  A.P : [4] EAST KAMENG

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_4_1997_sum['Area'],
      df_arunachal_4_1998_sum['Area'],
      df_arunachal_4_1999_sum['Area'],
      df_arunachal_4_2000_sum['Area'],
      df_arunachal_4_2001_sum['Area'], 
      df_arunachal_4_2002_sum['Area'],
      df_arunachal_4_2003_sum['Area'],
      df_arunachal_4_2004_sum['Area'],
      df_arunachal_4_2005_sum['Area'],
      df_arunachal_4_2006_sum['Area'],
      df_arunachal_4_2007_sum['Area'],
      df_arunachal_4_2008_sum['Area'],
      df_arunachal_4_2009_sum['Area'],
      df_arunachal_4_2010_sum['Area'],
      df_arunachal_4_2011_sum['Area'],
      df_arunachal_4_2012_sum['Area'],
      df_arunachal_4_2013_sum['Area'],
      df_arunachal_4_2014_sum['Area'])

y22 =(df_arunachal_4_1997_sum['Production'],
      df_arunachal_4_1998_sum['Production'],
      df_arunachal_4_1999_sum['Production'],
      df_arunachal_4_2000_sum['Production'],
      df_arunachal_4_2001_sum['Production'], 
      df_arunachal_4_2002_sum['Production'],
      df_arunachal_4_2003_sum['Production'],
      df_arunachal_4_2004_sum['Production'],
      df_arunachal_4_2005_sum['Production'],
      df_arunachal_4_2006_sum['Production'],
      df_arunachal_4_2007_sum['Production'],
      df_arunachal_4_2008_sum['Production'],
      df_arunachal_4_2009_sum['Production'],
      df_arunachal_4_2010_sum['Production'],
      df_arunachal_4_2011_sum['Production'],
      df_arunachal_4_2012_sum['Production'],
      df_arunachal_4_2013_sum['Production'],
      df_arunachal_4_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [4] EAST KAMENG :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [4] EAST KAMENG (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  A.P : [5] EAST SIANG

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_5_1997_sum['Area'],
      df_arunachal_5_1998_sum['Area'],
      df_arunachal_5_1999_sum['Area'],
      df_arunachal_5_2000_sum['Area'],
      df_arunachal_5_2001_sum['Area'], 
      df_arunachal_5_2002_sum['Area'],
      df_arunachal_5_2003_sum['Area'],
      df_arunachal_5_2004_sum['Area'],
      df_arunachal_5_2005_sum['Area'],
      df_arunachal_5_2006_sum['Area'],
      df_arunachal_5_2007_sum['Area'],
      df_arunachal_5_2008_sum['Area'],
      df_arunachal_5_2009_sum['Area'],
      df_arunachal_5_2010_sum['Area'],
      df_arunachal_5_2011_sum['Area'],
      df_arunachal_5_2012_sum['Area'],
      df_arunachal_5_2013_sum['Area'],
      df_arunachal_5_2014_sum['Area'])

y22 =(df_arunachal_5_1997_sum['Production'],
      df_arunachal_5_1998_sum['Production'],
      df_arunachal_5_1999_sum['Production'],
      df_arunachal_5_2000_sum['Production'],
      df_arunachal_5_2001_sum['Production'], 
      df_arunachal_5_2002_sum['Production'],
      df_arunachal_5_2003_sum['Production'],
      df_arunachal_5_2004_sum['Production'],
      df_arunachal_5_2005_sum['Production'],
      df_arunachal_5_2006_sum['Production'],
      df_arunachal_5_2007_sum['Production'],
      df_arunachal_5_2008_sum['Production'],
      df_arunachal_5_2009_sum['Production'],
      df_arunachal_5_2010_sum['Production'],
      df_arunachal_5_2011_sum['Production'],
      df_arunachal_5_2012_sum['Production'],
      df_arunachal_5_2013_sum['Production'],
      df_arunachal_5_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [5] EAST SIANG (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [5] EAST SIANG (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  A.P : [6] KURUNG KUMEY

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_6_1997_sum['Area'],
      df_arunachal_6_1998_sum['Area'],
      df_arunachal_6_1999_sum['Area'],
      df_arunachal_6_2000_sum['Area'],
      df_arunachal_6_2001_sum['Area'], 
      df_arunachal_6_2002_sum['Area'],
      df_arunachal_6_2003_sum['Area'],
      df_arunachal_6_2004_sum['Area'],
      df_arunachal_6_2005_sum['Area'],
      df_arunachal_6_2006_sum['Area'],
      df_arunachal_6_2007_sum['Area'],
      df_arunachal_6_2008_sum['Area'],
      df_arunachal_6_2009_sum['Area'],
      df_arunachal_6_2010_sum['Area'],
      df_arunachal_6_2011_sum['Area'],
      df_arunachal_6_2012_sum['Area'],
      df_arunachal_6_2013_sum['Area'],
      df_arunachal_6_2014_sum['Area'])

y22 =(df_arunachal_6_1997_sum['Production'],
      df_arunachal_6_1998_sum['Production'],
      df_arunachal_6_1999_sum['Production'],
      df_arunachal_6_2000_sum['Production'],
      df_arunachal_6_2001_sum['Production'], 
      df_arunachal_6_2002_sum['Production'],
      df_arunachal_6_2003_sum['Production'],
      df_arunachal_6_2004_sum['Production'],
      df_arunachal_6_2005_sum['Production'],
      df_arunachal_6_2006_sum['Production'],
      df_arunachal_6_2007_sum['Production'],
      df_arunachal_6_2008_sum['Production'],
      df_arunachal_6_2009_sum['Production'],
      df_arunachal_6_2010_sum['Production'],
      df_arunachal_6_2011_sum['Production'],
      df_arunachal_6_2012_sum['Production'],
      df_arunachal_6_2013_sum['Production'],
      df_arunachal_6_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [6] KURUNG KUMEY (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [6] KURUNG KUMEY (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  A.P : [7] LOHIT

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_7_1997_sum['Area'],
      df_arunachal_7_1998_sum['Area'],
      df_arunachal_7_1999_sum['Area'],
      df_arunachal_7_2000_sum['Area'],
      df_arunachal_7_2001_sum['Area'], 
      df_arunachal_7_2002_sum['Area'],
      df_arunachal_7_2003_sum['Area'],
      df_arunachal_7_2004_sum['Area'],
      df_arunachal_7_2005_sum['Area'],
      df_arunachal_7_2006_sum['Area'],
      df_arunachal_7_2007_sum['Area'],
      df_arunachal_7_2008_sum['Area'],
      df_arunachal_7_2009_sum['Area'],
      df_arunachal_7_2010_sum['Area'],
      df_arunachal_7_2011_sum['Area'],
      df_arunachal_7_2012_sum['Area'],
      df_arunachal_7_2013_sum['Area'],
      df_arunachal_7_2014_sum['Area'])

y22 =(df_arunachal_7_1997_sum['Production'],
      df_arunachal_7_1998_sum['Production'],
      df_arunachal_7_1999_sum['Production'],
      df_arunachal_7_2000_sum['Production'],
      df_arunachal_7_2001_sum['Production'], 
      df_arunachal_7_2002_sum['Production'],
      df_arunachal_7_2003_sum['Production'],
      df_arunachal_7_2004_sum['Production'],
      df_arunachal_7_2005_sum['Production'],
      df_arunachal_7_2006_sum['Production'],
      df_arunachal_7_2007_sum['Production'],
      df_arunachal_7_2008_sum['Production'],
      df_arunachal_7_2009_sum['Production'],
      df_arunachal_7_2010_sum['Production'],
      df_arunachal_7_2011_sum['Production'],
      df_arunachal_7_2012_sum['Production'],
      df_arunachal_7_2013_sum['Production'],
      df_arunachal_7_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [7] LOHIT (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [7] LOHIT (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  A.P : [8] LONGDING

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_8_1997_sum['Area'],
      df_arunachal_8_1998_sum['Area'],
      df_arunachal_8_1999_sum['Area'],
      df_arunachal_8_2000_sum['Area'],
      df_arunachal_8_2001_sum['Area'], 
      df_arunachal_8_2002_sum['Area'],
      df_arunachal_8_2003_sum['Area'],
      df_arunachal_8_2004_sum['Area'],
      df_arunachal_8_2005_sum['Area'],
      df_arunachal_8_2006_sum['Area'],
      df_arunachal_8_2007_sum['Area'],
      df_arunachal_8_2008_sum['Area'],
      df_arunachal_8_2009_sum['Area'],
      df_arunachal_8_2010_sum['Area'],
      df_arunachal_8_2011_sum['Area'],
      df_arunachal_8_2012_sum['Area'],
      df_arunachal_8_2013_sum['Area'],
      df_arunachal_8_2014_sum['Area'])

y22 =(df_arunachal_8_1997_sum['Production'],
      df_arunachal_8_1998_sum['Production'],
      df_arunachal_8_1999_sum['Production'],
      df_arunachal_8_2000_sum['Production'],
      df_arunachal_8_2001_sum['Production'], 
      df_arunachal_8_2002_sum['Production'],
      df_arunachal_8_2003_sum['Production'],
      df_arunachal_8_2004_sum['Production'],
      df_arunachal_8_2005_sum['Production'],
      df_arunachal_8_2006_sum['Production'],
      df_arunachal_8_2007_sum['Production'],
      df_arunachal_8_2008_sum['Production'],
      df_arunachal_8_2009_sum['Production'],
      df_arunachal_8_2010_sum['Production'],
      df_arunachal_8_2011_sum['Production'],
      df_arunachal_8_2012_sum['Production'],
      df_arunachal_8_2013_sum['Production'],
      df_arunachal_8_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [8] LONGDING (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [8] LONGDING (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  A.P : [9] LOWER DIBANG VALLEY 

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_9_1997_sum['Area'],
      df_arunachal_9_1998_sum['Area'],
      df_arunachal_9_1999_sum['Area'],
      df_arunachal_9_2000_sum['Area'],
      df_arunachal_9_2001_sum['Area'], 
      df_arunachal_9_2002_sum['Area'],
      df_arunachal_9_2003_sum['Area'],
      df_arunachal_9_2004_sum['Area'],
      df_arunachal_9_2005_sum['Area'],
      df_arunachal_9_2006_sum['Area'],
      df_arunachal_9_2007_sum['Area'],
      df_arunachal_9_2008_sum['Area'],
      df_arunachal_9_2009_sum['Area'],
      df_arunachal_9_2010_sum['Area'],
      df_arunachal_9_2011_sum['Area'],
      df_arunachal_9_2012_sum['Area'],
      df_arunachal_9_2013_sum['Area'],
      df_arunachal_9_2014_sum['Area'])

y22 =(df_arunachal_9_1997_sum['Production'],
      df_arunachal_9_1998_sum['Production'],
      df_arunachal_9_1999_sum['Production'],
      df_arunachal_9_2000_sum['Production'],
      df_arunachal_9_2001_sum['Production'], 
      df_arunachal_9_2002_sum['Production'],
      df_arunachal_9_2003_sum['Production'],
      df_arunachal_9_2004_sum['Production'],
      df_arunachal_9_2005_sum['Production'],
      df_arunachal_9_2006_sum['Production'],
      df_arunachal_9_2007_sum['Production'],
      df_arunachal_9_2008_sum['Production'],
      df_arunachal_9_2009_sum['Production'],
      df_arunachal_9_2010_sum['Production'],
      df_arunachal_9_2011_sum['Production'],
      df_arunachal_9_2012_sum['Production'],
      df_arunachal_9_2013_sum['Production'],
      df_arunachal_9_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [9] LOWER DIBANG VALLEY (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [9] LOWER DIBANG VALLEY (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  A.P : [10] LOWER SUBANSIRI 

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_10_1997_sum['Area'],
      df_arunachal_10_1998_sum['Area'],
      df_arunachal_10_1999_sum['Area'],
      df_arunachal_10_2000_sum['Area'],
      df_arunachal_10_2001_sum['Area'], 
      df_arunachal_10_2002_sum['Area'],
      df_arunachal_10_2003_sum['Area'],
      df_arunachal_10_2004_sum['Area'],
      df_arunachal_10_2005_sum['Area'],
      df_arunachal_10_2006_sum['Area'],
      df_arunachal_10_2007_sum['Area'],
      df_arunachal_10_2008_sum['Area'],
      df_arunachal_10_2009_sum['Area'],
      df_arunachal_10_2010_sum['Area'],
      df_arunachal_10_2011_sum['Area'],
      df_arunachal_10_2012_sum['Area'],
      df_arunachal_10_2013_sum['Area'],
      df_arunachal_10_2014_sum['Area'])

y22 =(df_arunachal_10_1997_sum['Production'],
      df_arunachal_10_1998_sum['Production'],
      df_arunachal_10_1999_sum['Production'],
      df_arunachal_10_2000_sum['Production'],
      df_arunachal_10_2001_sum['Production'], 
      df_arunachal_10_2002_sum['Production'],
      df_arunachal_10_2003_sum['Production'],
      df_arunachal_10_2004_sum['Production'],
      df_arunachal_10_2005_sum['Production'],
      df_arunachal_10_2006_sum['Production'],
      df_arunachal_10_2007_sum['Production'],
      df_arunachal_10_2008_sum['Production'],
      df_arunachal_10_2009_sum['Production'],
      df_arunachal_10_2010_sum['Production'],
      df_arunachal_10_2011_sum['Production'],
      df_arunachal_10_2012_sum['Production'],
      df_arunachal_10_2013_sum['Production'],
      df_arunachal_10_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [10] LOWER SUBANSIRI (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [10] LOWER SUBANSIRI (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  A.P : [11] NAMSAI

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_11_1997_sum['Area'],
      df_arunachal_11_1998_sum['Area'],
      df_arunachal_11_1999_sum['Area'],
      df_arunachal_11_2000_sum['Area'],
      df_arunachal_11_2001_sum['Area'], 
      df_arunachal_11_2002_sum['Area'],
      df_arunachal_11_2003_sum['Area'],
      df_arunachal_11_2004_sum['Area'],
      df_arunachal_11_2005_sum['Area'],
      df_arunachal_11_2006_sum['Area'],
      df_arunachal_11_2007_sum['Area'],
      df_arunachal_11_2008_sum['Area'],
      df_arunachal_11_2009_sum['Area'],
      df_arunachal_11_2010_sum['Area'],
      df_arunachal_11_2011_sum['Area'],
      df_arunachal_11_2012_sum['Area'],
      df_arunachal_11_2013_sum['Area'],
      df_arunachal_11_2014_sum['Area'])

y22 =(df_arunachal_11_1997_sum['Production'],
      df_arunachal_11_1998_sum['Production'],
      df_arunachal_11_1999_sum['Production'],
      df_arunachal_11_2000_sum['Production'],
      df_arunachal_11_2001_sum['Production'], 
      df_arunachal_11_2002_sum['Production'],
      df_arunachal_11_2003_sum['Production'],
      df_arunachal_11_2004_sum['Production'],
      df_arunachal_11_2005_sum['Production'],
      df_arunachal_11_2006_sum['Production'],
      df_arunachal_11_2007_sum['Production'],
      df_arunachal_11_2008_sum['Production'],
      df_arunachal_11_2009_sum['Production'],
      df_arunachal_11_2010_sum['Production'],
      df_arunachal_11_2011_sum['Production'],
      df_arunachal_11_2012_sum['Production'],
      df_arunachal_11_2013_sum['Production'],
      df_arunachal_11_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [11] NAMSAI (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [11] NAMSAI (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  A.P : [12] PAPUM PARE

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_12_1997_sum['Area'],
      df_arunachal_12_1998_sum['Area'],
      df_arunachal_12_1999_sum['Area'],
      df_arunachal_12_2000_sum['Area'],
      df_arunachal_12_2001_sum['Area'], 
      df_arunachal_12_2002_sum['Area'],
      df_arunachal_12_2003_sum['Area'],
      df_arunachal_12_2004_sum['Area'],
      df_arunachal_12_2005_sum['Area'],
      df_arunachal_12_2006_sum['Area'],
      df_arunachal_12_2007_sum['Area'],
      df_arunachal_12_2008_sum['Area'],
      df_arunachal_12_2009_sum['Area'],
      df_arunachal_12_2010_sum['Area'],
      df_arunachal_12_2011_sum['Area'],
      df_arunachal_12_2012_sum['Area'],
      df_arunachal_12_2013_sum['Area'],
      df_arunachal_12_2014_sum['Area'])

y22 =(df_arunachal_12_1997_sum['Production'],
      df_arunachal_12_1998_sum['Production'],
      df_arunachal_12_1999_sum['Production'],
      df_arunachal_12_2000_sum['Production'],
      df_arunachal_12_2001_sum['Production'], 
      df_arunachal_12_2002_sum['Production'],
      df_arunachal_12_2003_sum['Production'],
      df_arunachal_12_2004_sum['Production'],
      df_arunachal_12_2005_sum['Production'],
      df_arunachal_12_2006_sum['Production'],
      df_arunachal_12_2007_sum['Production'],
      df_arunachal_12_2008_sum['Production'],
      df_arunachal_12_2009_sum['Production'],
      df_arunachal_12_2010_sum['Production'],
      df_arunachal_12_2011_sum['Production'],
      df_arunachal_12_2012_sum['Production'],
      df_arunachal_12_2013_sum['Production'],
      df_arunachal_12_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [12] PAPUM PARE (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [12] PAPUM PARE (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  A.P : [13] TAWANG

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_13_1997_sum['Area'],
      df_arunachal_13_1998_sum['Area'],
      df_arunachal_13_1999_sum['Area'],
      df_arunachal_13_2000_sum['Area'],
      df_arunachal_13_2001_sum['Area'], 
      df_arunachal_13_2002_sum['Area'],
      df_arunachal_13_2003_sum['Area'],
      df_arunachal_13_2004_sum['Area'],
      df_arunachal_13_2005_sum['Area'],
      df_arunachal_13_2006_sum['Area'],
      df_arunachal_13_2007_sum['Area'],
      df_arunachal_13_2008_sum['Area'],
      df_arunachal_13_2009_sum['Area'],
      df_arunachal_13_2010_sum['Area'],
      df_arunachal_13_2011_sum['Area'],
      df_arunachal_13_2012_sum['Area'],
      df_arunachal_13_2013_sum['Area'],
      df_arunachal_13_2014_sum['Area'])

y22 =(df_arunachal_13_1997_sum['Production'],
      df_arunachal_13_1998_sum['Production'],
      df_arunachal_13_1999_sum['Production'],
      df_arunachal_13_2000_sum['Production'],
      df_arunachal_13_2001_sum['Production'], 
      df_arunachal_13_2002_sum['Production'],
      df_arunachal_13_2003_sum['Production'],
      df_arunachal_13_2004_sum['Production'],
      df_arunachal_13_2005_sum['Production'],
      df_arunachal_13_2006_sum['Production'],
      df_arunachal_13_2007_sum['Production'],
      df_arunachal_13_2008_sum['Production'],
      df_arunachal_13_2009_sum['Production'],
      df_arunachal_13_2010_sum['Production'],
      df_arunachal_13_2011_sum['Production'],
      df_arunachal_13_2012_sum['Production'],
      df_arunachal_13_2013_sum['Production'],
      df_arunachal_13_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [13] TAWANG (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [13] TAWANG (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  A.P : [14] TIRAP

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_14_1997_sum['Area'],
      df_arunachal_14_1998_sum['Area'],
      df_arunachal_14_1999_sum['Area'],
      df_arunachal_14_2000_sum['Area'],
      df_arunachal_14_2001_sum['Area'], 
      df_arunachal_14_2002_sum['Area'],
      df_arunachal_14_2003_sum['Area'],
      df_arunachal_14_2004_sum['Area'],
      df_arunachal_14_2005_sum['Area'],
      df_arunachal_14_2006_sum['Area'],
      df_arunachal_14_2007_sum['Area'],
      df_arunachal_14_2008_sum['Area'],
      df_arunachal_14_2009_sum['Area'],
      df_arunachal_14_2010_sum['Area'],
      df_arunachal_14_2011_sum['Area'],
      df_arunachal_14_2012_sum['Area'],
      df_arunachal_14_2013_sum['Area'],
      df_arunachal_14_2014_sum['Area'])

y22 =(df_arunachal_14_1997_sum['Production'],
      df_arunachal_14_1998_sum['Production'],
      df_arunachal_14_1999_sum['Production'],
      df_arunachal_14_2000_sum['Production'],
      df_arunachal_14_2001_sum['Production'], 
      df_arunachal_14_2002_sum['Production'],
      df_arunachal_14_2003_sum['Production'],
      df_arunachal_14_2004_sum['Production'],
      df_arunachal_14_2005_sum['Production'],
      df_arunachal_14_2006_sum['Production'],
      df_arunachal_14_2007_sum['Production'],
      df_arunachal_14_2008_sum['Production'],
      df_arunachal_14_2009_sum['Production'],
      df_arunachal_14_2010_sum['Production'],
      df_arunachal_14_2011_sum['Production'],
      df_arunachal_14_2012_sum['Production'],
      df_arunachal_14_2013_sum['Production'],
      df_arunachal_14_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [14] TIRAP (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [14] TIRAP (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  A.P : [15] UPPER SIANG

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_15_1997_sum['Area'],
      df_arunachal_15_1998_sum['Area'],
      df_arunachal_15_1999_sum['Area'],
      df_arunachal_15_2000_sum['Area'],
      df_arunachal_15_2001_sum['Area'], 
      df_arunachal_15_2002_sum['Area'],
      df_arunachal_15_2003_sum['Area'],
      df_arunachal_15_2004_sum['Area'],
      df_arunachal_15_2005_sum['Area'],
      df_arunachal_15_2006_sum['Area'],
      df_arunachal_15_2007_sum['Area'],
      df_arunachal_15_2008_sum['Area'],
      df_arunachal_15_2009_sum['Area'],
      df_arunachal_15_2010_sum['Area'],
      df_arunachal_15_2011_sum['Area'],
      df_arunachal_15_2012_sum['Area'],
      df_arunachal_15_2013_sum['Area'],
      df_arunachal_15_2014_sum['Area'])

y22 =(df_arunachal_15_1997_sum['Production'],
      df_arunachal_15_1998_sum['Production'],
      df_arunachal_15_1999_sum['Production'],
      df_arunachal_15_2000_sum['Production'],
      df_arunachal_15_2001_sum['Production'], 
      df_arunachal_15_2002_sum['Production'],
      df_arunachal_15_2003_sum['Production'],
      df_arunachal_15_2004_sum['Production'],
      df_arunachal_15_2005_sum['Production'],
      df_arunachal_15_2006_sum['Production'],
      df_arunachal_15_2007_sum['Production'],
      df_arunachal_15_2008_sum['Production'],
      df_arunachal_15_2009_sum['Production'],
      df_arunachal_15_2010_sum['Production'],
      df_arunachal_15_2011_sum['Production'],
      df_arunachal_15_2012_sum['Production'],
      df_arunachal_15_2013_sum['Production'],
      df_arunachal_15_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [15] UPPER SIANG (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [15] UPPER SIANG (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  A.P : [16] UPPER SUBANSIRI

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_16_1997_sum['Area'],
      df_arunachal_16_1998_sum['Area'],
      df_arunachal_16_1999_sum['Area'],
      df_arunachal_16_2000_sum['Area'],
      df_arunachal_16_2001_sum['Area'], 
      df_arunachal_16_2002_sum['Area'],
      df_arunachal_16_2003_sum['Area'],
      df_arunachal_16_2004_sum['Area'],
      df_arunachal_16_2005_sum['Area'],
      df_arunachal_16_2006_sum['Area'],
      df_arunachal_16_2007_sum['Area'],
      df_arunachal_16_2008_sum['Area'],
      df_arunachal_16_2009_sum['Area'],
      df_arunachal_16_2010_sum['Area'],
      df_arunachal_16_2011_sum['Area'],
      df_arunachal_16_2012_sum['Area'],
      df_arunachal_16_2013_sum['Area'],
      df_arunachal_16_2014_sum['Area'])

y22 =(df_arunachal_16_1997_sum['Production'],
      df_arunachal_16_1998_sum['Production'],
      df_arunachal_16_1999_sum['Production'],
      df_arunachal_16_2000_sum['Production'],
      df_arunachal_16_2001_sum['Production'], 
      df_arunachal_16_2002_sum['Production'],
      df_arunachal_16_2003_sum['Production'],
      df_arunachal_16_2004_sum['Production'],
      df_arunachal_16_2005_sum['Production'],
      df_arunachal_16_2006_sum['Production'],
      df_arunachal_16_2007_sum['Production'],
      df_arunachal_16_2008_sum['Production'],
      df_arunachal_16_2009_sum['Production'],
      df_arunachal_16_2010_sum['Production'],
      df_arunachal_16_2011_sum['Production'],
      df_arunachal_16_2012_sum['Production'],
      df_arunachal_16_2013_sum['Production'],
      df_arunachal_16_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [16] UPPER SUBANSIRI (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [16] UPPER SUBANSIRI (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show() 
   
# plotting  A.P : [17] WEST KAMENG

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_17_1997_sum['Area'],
      df_arunachal_17_1998_sum['Area'],
      df_arunachal_17_1999_sum['Area'],
      df_arunachal_17_2000_sum['Area'],
      df_arunachal_17_2001_sum['Area'], 
      df_arunachal_17_2002_sum['Area'],
      df_arunachal_17_2003_sum['Area'],
      df_arunachal_17_2004_sum['Area'],
      df_arunachal_17_2005_sum['Area'],
      df_arunachal_17_2006_sum['Area'],
      df_arunachal_17_2007_sum['Area'],
      df_arunachal_17_2008_sum['Area'],
      df_arunachal_17_2009_sum['Area'],
      df_arunachal_17_2010_sum['Area'],
      df_arunachal_17_2011_sum['Area'],
      df_arunachal_17_2012_sum['Area'],
      df_arunachal_17_2013_sum['Area'],
      df_arunachal_17_2014_sum['Area'])

y22 =(df_arunachal_17_1997_sum['Production'],
      df_arunachal_17_1998_sum['Production'],
      df_arunachal_17_1999_sum['Production'],
      df_arunachal_17_2000_sum['Production'],
      df_arunachal_17_2001_sum['Production'], 
      df_arunachal_17_2002_sum['Production'],
      df_arunachal_17_2003_sum['Production'],
      df_arunachal_17_2004_sum['Production'],
      df_arunachal_17_2005_sum['Production'],
      df_arunachal_17_2006_sum['Production'],
      df_arunachal_17_2007_sum['Production'],
      df_arunachal_17_2008_sum['Production'],
      df_arunachal_17_2009_sum['Production'],
      df_arunachal_17_2010_sum['Production'],
      df_arunachal_17_2011_sum['Production'],
      df_arunachal_17_2012_sum['Production'],
      df_arunachal_17_2013_sum['Production'],
      df_arunachal_17_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [17] WEST KAMENG (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [17] WEST KAMENG (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show() 
   
# plotting  A.P : [18] WEST SIANG 

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_arunachal_18_1997_sum['Area'],
      df_arunachal_18_1998_sum['Area'],
      df_arunachal_18_1999_sum['Area'],
      df_arunachal_18_2000_sum['Area'],
      df_arunachal_18_2001_sum['Area'], 
      df_arunachal_18_2002_sum['Area'],
      df_arunachal_18_2003_sum['Area'],
      df_arunachal_18_2004_sum['Area'],
      df_arunachal_18_2005_sum['Area'],
      df_arunachal_18_2006_sum['Area'],
      df_arunachal_18_2007_sum['Area'],
      df_arunachal_18_2008_sum['Area'],
      df_arunachal_18_2009_sum['Area'],
      df_arunachal_18_2010_sum['Area'],
      df_arunachal_18_2011_sum['Area'],
      df_arunachal_18_2012_sum['Area'],
      df_arunachal_18_2013_sum['Area'],
      df_arunachal_18_2014_sum['Area'])

y22 =(df_arunachal_18_1997_sum['Production'],
      df_arunachal_18_1998_sum['Production'],
      df_arunachal_18_1999_sum['Production'],
      df_arunachal_18_2000_sum['Production'],
      df_arunachal_18_2001_sum['Production'], 
      df_arunachal_18_2002_sum['Production'],
      df_arunachal_18_2003_sum['Production'],
      df_arunachal_18_2004_sum['Production'],
      df_arunachal_18_2005_sum['Production'],
      df_arunachal_18_2006_sum['Production'],
      df_arunachal_18_2007_sum['Production'],
      df_arunachal_18_2008_sum['Production'],
      df_arunachal_18_2009_sum['Production'],
      df_arunachal_18_2010_sum['Production'],
      df_arunachal_18_2011_sum['Production'],
      df_arunachal_18_2012_sum['Production'],
      df_arunachal_18_2013_sum['Production'],
      df_arunachal_18_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-3 : A.P : [18] WEST SIANG (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-3 : A.P : [18] WEST SIANG (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()
   
# plotting of Assam 'Area' and 'Production'                                                                                                                 
# plotting  Assam : [1] BAKSA                                           
                                               
x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_1_1997_sum['Area'],
      df_assam_1_1998_sum['Area'],
      df_assam_1_1999_sum['Area'],
      df_assam_1_2000_sum['Area'],
      df_assam_1_2001_sum['Area'], 
      df_assam_1_2002_sum['Area'],
      df_assam_1_2003_sum['Area'],
      df_assam_1_2004_sum['Area'],
      df_assam_1_2005_sum['Area'],
      df_assam_1_2006_sum['Area'],
      df_assam_1_2007_sum['Area'],
      df_assam_1_2008_sum['Area'],
      df_assam_1_2009_sum['Area'],
      df_assam_1_2010_sum['Area'],
      df_assam_1_2011_sum['Area'],
      df_assam_1_2012_sum['Area'],
      df_assam_1_2013_sum['Area'],
      df_assam_1_2014_sum['Area'])

y22 =(df_assam_1_1997_sum['Production'],
      df_assam_1_1998_sum['Production'],
      df_assam_1_1999_sum['Production'],
      df_assam_1_2000_sum['Production'],
      df_assam_1_2001_sum['Production'], 
      df_assam_1_2002_sum['Production'],
      df_assam_1_2003_sum['Production'],
      df_assam_1_2004_sum['Production'],
      df_assam_1_2005_sum['Production'],
      df_assam_1_2006_sum['Production'],
      df_assam_1_2007_sum['Production'],
      df_assam_1_2008_sum['Production'],
      df_assam_1_2009_sum['Production'],
      df_assam_1_2010_sum['Production'],
      df_assam_1_2011_sum['Production'],
      df_assam_1_2012_sum['Production'],
      df_assam_1_2013_sum['Production'],
      df_assam_1_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [1] BAKSA (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [1] BAKSA (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show() 

# plotting  Assam : [2] BARPETA

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_2_1997_sum['Area'],
      df_assam_2_1998_sum['Area'],
      df_assam_2_1999_sum['Area'],
      df_assam_2_2000_sum['Area'],
      df_assam_2_2001_sum['Area'], 
      df_assam_2_2002_sum['Area'],
      df_assam_2_2003_sum['Area'],
      df_assam_2_2004_sum['Area'],
      df_assam_2_2005_sum['Area'],
      df_assam_2_2006_sum['Area'],
      df_assam_2_2007_sum['Area'],
      df_assam_2_2008_sum['Area'],
      df_assam_2_2009_sum['Area'],
      df_assam_2_2010_sum['Area'],
      df_assam_2_2011_sum['Area'],
      df_assam_2_2012_sum['Area'],
      df_assam_2_2013_sum['Area'],
      df_assam_2_2014_sum['Area'])

y22 =(df_assam_2_1997_sum['Production'],
      df_assam_2_1998_sum['Production'],
      df_assam_2_1999_sum['Production'],
      df_assam_2_2000_sum['Production'],
      df_assam_2_2001_sum['Production'], 
      df_assam_2_2002_sum['Production'],
      df_assam_2_2003_sum['Production'],
      df_assam_2_2004_sum['Production'],
      df_assam_2_2005_sum['Production'],
      df_assam_2_2006_sum['Production'],
      df_assam_2_2007_sum['Production'],
      df_assam_2_2008_sum['Production'],
      df_assam_2_2009_sum['Production'],
      df_assam_2_2010_sum['Production'],
      df_assam_2_2011_sum['Production'],
      df_assam_2_2012_sum['Production'],
      df_assam_2_2013_sum['Production'],
      df_assam_2_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [2] BARPETA (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [2] BARPETA (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [3] BONGAIGAON

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_3_1997_sum['Area'],
      df_assam_3_1998_sum['Area'],
      df_assam_3_1999_sum['Area'],
      df_assam_3_2000_sum['Area'],
      df_assam_3_2001_sum['Area'], 
      df_assam_3_2002_sum['Area'],
      df_assam_3_2003_sum['Area'],
      df_assam_3_2004_sum['Area'],
      df_assam_3_2005_sum['Area'],
      df_assam_3_2006_sum['Area'],
      df_assam_3_2007_sum['Area'],
      df_assam_3_2008_sum['Area'],
      df_assam_3_2009_sum['Area'],
      df_assam_3_2010_sum['Area'],
      df_assam_3_2011_sum['Area'],
      df_assam_3_2012_sum['Area'],
      df_assam_3_2013_sum['Area'],
      df_assam_3_2014_sum['Area'])

y22 =(df_assam_3_1997_sum['Production'],
      df_assam_3_1998_sum['Production'],
      df_assam_3_1999_sum['Production'],
      df_assam_3_2000_sum['Production'],
      df_assam_3_2001_sum['Production'], 
      df_assam_3_2002_sum['Production'],
      df_assam_3_2003_sum['Production'],
      df_assam_3_2004_sum['Production'],
      df_assam_3_2005_sum['Production'],
      df_assam_3_2006_sum['Production'],
      df_assam_3_2007_sum['Production'],
      df_assam_3_2008_sum['Production'],
      df_assam_3_2009_sum['Production'],
      df_assam_3_2010_sum['Production'],
      df_assam_3_2011_sum['Production'],
      df_assam_3_2012_sum['Production'],
      df_assam_3_2013_sum['Production'],
      df_assam_3_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [3] BONGAIGAON (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [3] BONGAIGAON (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [4] CACHAR

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_4_1997_sum['Area'],
      df_assam_4_1998_sum['Area'],
      df_assam_4_1999_sum['Area'],
      df_assam_4_2000_sum['Area'],
      df_assam_4_2001_sum['Area'], 
      df_assam_4_2002_sum['Area'],
      df_assam_4_2003_sum['Area'],
      df_assam_4_2004_sum['Area'],
      df_assam_4_2005_sum['Area'],
      df_assam_4_2006_sum['Area'],
      df_assam_4_2007_sum['Area'],
      df_assam_4_2008_sum['Area'],
      df_assam_4_2009_sum['Area'],
      df_assam_4_2010_sum['Area'],
      df_assam_4_2011_sum['Area'],
      df_assam_4_2012_sum['Area'],
      df_assam_4_2013_sum['Area'],
      df_assam_4_2014_sum['Area'])

y22 =(df_assam_4_1997_sum['Production'],
      df_assam_4_1998_sum['Production'],
      df_assam_4_1999_sum['Production'],
      df_assam_4_2000_sum['Production'],
      df_assam_4_2001_sum['Production'], 
      df_assam_4_2002_sum['Production'],
      df_assam_4_2003_sum['Production'],
      df_assam_4_2004_sum['Production'],
      df_assam_4_2005_sum['Production'],
      df_assam_4_2006_sum['Production'],
      df_assam_4_2007_sum['Production'],
      df_assam_4_2008_sum['Production'],
      df_assam_4_2009_sum['Production'],
      df_assam_4_2010_sum['Production'],
      df_assam_4_2011_sum['Production'],
      df_assam_4_2012_sum['Production'],
      df_assam_4_2013_sum['Production'],
      df_assam_4_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [4] CACHAR (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [4] CACHAR (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [5] CHIRANG

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_5_1997_sum['Area'],
      df_assam_5_1998_sum['Area'],
      df_assam_5_1999_sum['Area'],
      df_assam_5_2000_sum['Area'],
      df_assam_5_2001_sum['Area'], 
      df_assam_5_2002_sum['Area'],
      df_assam_5_2003_sum['Area'],
      df_assam_5_2004_sum['Area'],
      df_assam_5_2005_sum['Area'],
      df_assam_5_2006_sum['Area'],
      df_assam_5_2007_sum['Area'],
      df_assam_5_2008_sum['Area'],
      df_assam_5_2009_sum['Area'],
      df_assam_5_2010_sum['Area'],
      df_assam_5_2011_sum['Area'],
      df_assam_5_2012_sum['Area'],
      df_assam_5_2013_sum['Area'],
      df_assam_5_2014_sum['Area'])

y22 =(df_assam_5_1997_sum['Production'],
      df_assam_5_1998_sum['Production'],
      df_assam_5_1999_sum['Production'],
      df_assam_5_2000_sum['Production'],
      df_assam_5_2001_sum['Production'], 
      df_assam_5_2002_sum['Production'],
      df_assam_5_2003_sum['Production'],
      df_assam_5_2004_sum['Production'],
      df_assam_5_2005_sum['Production'],
      df_assam_5_2006_sum['Production'],
      df_assam_5_2007_sum['Production'],
      df_assam_5_2008_sum['Production'],
      df_assam_5_2009_sum['Production'],
      df_assam_5_2010_sum['Production'],
      df_assam_5_2011_sum['Production'],
      df_assam_5_2012_sum['Production'],
      df_assam_5_2013_sum['Production'],
      df_assam_5_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [5] CHIRANG (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [5] CHIRANG (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [6] DARRANG

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_6_1997_sum['Area'],
      df_assam_6_1998_sum['Area'],
      df_assam_6_1999_sum['Area'],
      df_assam_6_2000_sum['Area'],
      df_assam_6_2001_sum['Area'], 
      df_assam_6_2002_sum['Area'],
      df_assam_6_2003_sum['Area'],
      df_assam_6_2004_sum['Area'],
      df_assam_6_2005_sum['Area'],
      df_assam_6_2006_sum['Area'],
      df_assam_6_2007_sum['Area'],
      df_assam_6_2008_sum['Area'],
      df_assam_6_2009_sum['Area'],
      df_assam_6_2010_sum['Area'],
      df_assam_6_2011_sum['Area'],
      df_assam_6_2012_sum['Area'],
      df_assam_6_2013_sum['Area'],
      df_assam_6_2014_sum['Area'])

y22 =(df_assam_6_1997_sum['Production'],
      df_assam_6_1998_sum['Production'],
      df_assam_6_1999_sum['Production'],
      df_assam_6_2000_sum['Production'],
      df_assam_6_2001_sum['Production'], 
      df_assam_6_2002_sum['Production'],
      df_assam_6_2003_sum['Production'],
      df_assam_6_2004_sum['Production'],
      df_assam_6_2005_sum['Production'],
      df_assam_6_2006_sum['Production'],
      df_assam_6_2007_sum['Production'],
      df_assam_6_2008_sum['Production'],
      df_assam_6_2009_sum['Production'],
      df_assam_6_2010_sum['Production'],
      df_assam_6_2011_sum['Production'],
      df_assam_6_2012_sum['Production'],
      df_assam_6_2013_sum['Production'],
      df_assam_6_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [6] DARRANG (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [6] DARRANG (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [7] DHEMAJI

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_7_1997_sum['Area'],
      df_assam_7_1998_sum['Area'],
      df_assam_7_1999_sum['Area'],
      df_assam_7_2000_sum['Area'],
      df_assam_7_2001_sum['Area'], 
      df_assam_7_2002_sum['Area'],
      df_assam_7_2003_sum['Area'],
      df_assam_7_2004_sum['Area'],
      df_assam_7_2005_sum['Area'],
      df_assam_7_2006_sum['Area'],
      df_assam_7_2007_sum['Area'],
      df_assam_7_2008_sum['Area'],
      df_assam_7_2009_sum['Area'],
      df_assam_7_2010_sum['Area'],
      df_assam_7_2011_sum['Area'],
      df_assam_7_2012_sum['Area'],
      df_assam_7_2013_sum['Area'],
      df_assam_7_2014_sum['Area'])

y22 =(df_assam_7_1997_sum['Production'],
      df_assam_7_1998_sum['Production'],
      df_assam_7_1999_sum['Production'],
      df_assam_7_2000_sum['Production'],
      df_assam_7_2001_sum['Production'], 
      df_assam_7_2002_sum['Production'],
      df_assam_7_2003_sum['Production'],
      df_assam_7_2004_sum['Production'],
      df_assam_7_2005_sum['Production'],
      df_assam_7_2006_sum['Production'],
      df_assam_7_2007_sum['Production'],
      df_assam_7_2008_sum['Production'],
      df_assam_7_2009_sum['Production'],
      df_assam_7_2010_sum['Production'],
      df_assam_7_2011_sum['Production'],
      df_assam_7_2012_sum['Production'],
      df_assam_7_2013_sum['Production'],
      df_assam_7_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [7] DHEMAJI (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [7] DHEMAJI (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [8] DHUBRI

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_8_1997_sum['Area'],
      df_assam_8_1998_sum['Area'],
      df_assam_8_1999_sum['Area'],
      df_assam_8_2000_sum['Area'],
      df_assam_8_2001_sum['Area'], 
      df_assam_8_2002_sum['Area'],
      df_assam_8_2003_sum['Area'],
      df_assam_8_2004_sum['Area'],
      df_assam_8_2005_sum['Area'],
      df_assam_8_2006_sum['Area'],
      df_assam_8_2007_sum['Area'],
      df_assam_8_2008_sum['Area'],
      df_assam_8_2009_sum['Area'],
      df_assam_8_2010_sum['Area'],
      df_assam_8_2011_sum['Area'],
      df_assam_8_2012_sum['Area'],
      df_assam_8_2013_sum['Area'],
      df_assam_8_2014_sum['Area'])

y22 =(df_assam_8_1997_sum['Production'],
      df_assam_8_1998_sum['Production'],
      df_assam_8_1999_sum['Production'],
      df_assam_8_2000_sum['Production'],
      df_assam_8_2001_sum['Production'], 
      df_assam_8_2002_sum['Production'],
      df_assam_8_2003_sum['Production'],
      df_assam_8_2004_sum['Production'],
      df_assam_8_2005_sum['Production'],
      df_assam_8_2006_sum['Production'],
      df_assam_8_2007_sum['Production'],
      df_assam_8_2008_sum['Production'],
      df_assam_8_2009_sum['Production'],
      df_assam_8_2010_sum['Production'],
      df_assam_8_2011_sum['Production'],
      df_assam_8_2012_sum['Production'],
      df_assam_8_2013_sum['Production'],
      df_assam_8_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [8] DHUBRI (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [8] DHUBRI (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [9] DIBRUGARH

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_9_1997_sum['Area'],
      df_assam_9_1998_sum['Area'],
      df_assam_9_1999_sum['Area'],
      df_assam_9_2000_sum['Area'],
      df_assam_9_2001_sum['Area'], 
      df_assam_9_2002_sum['Area'],
      df_assam_9_2003_sum['Area'],
      df_assam_9_2004_sum['Area'],
      df_assam_9_2005_sum['Area'],
      df_assam_9_2006_sum['Area'],
      df_assam_9_2007_sum['Area'],
      df_assam_9_2008_sum['Area'],
      df_assam_9_2009_sum['Area'],
      df_assam_9_2010_sum['Area'],
      df_assam_9_2011_sum['Area'],
      df_assam_9_2012_sum['Area'],
      df_assam_9_2013_sum['Area'],
      df_assam_9_2014_sum['Area'])

y22 =(df_assam_9_1997_sum['Production'],
      df_assam_9_1998_sum['Production'],
      df_assam_9_1999_sum['Production'],
      df_assam_9_2000_sum['Production'],
      df_assam_9_2001_sum['Production'], 
      df_assam_9_2002_sum['Production'],
      df_assam_9_2003_sum['Production'],
      df_assam_9_2004_sum['Production'],
      df_assam_9_2005_sum['Production'],
      df_assam_9_2006_sum['Production'],
      df_assam_9_2007_sum['Production'],
      df_assam_9_2008_sum['Production'],
      df_assam_9_2009_sum['Production'],
      df_assam_9_2010_sum['Production'],
      df_assam_9_2011_sum['Production'],
      df_assam_9_2012_sum['Production'],
      df_assam_9_2013_sum['Production'],
      df_assam_9_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [9] DIBRUGARH (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [9] DIBRUGARH (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [10] DIMA HASAO

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_10_1997_sum['Area'],
      df_assam_10_1998_sum['Area'],
      df_assam_10_1999_sum['Area'],
      df_assam_10_2000_sum['Area'],
      df_assam_10_2001_sum['Area'], 
      df_assam_10_2002_sum['Area'],
      df_assam_10_2003_sum['Area'],
      df_assam_10_2004_sum['Area'],
      df_assam_10_2005_sum['Area'],
      df_assam_10_2006_sum['Area'],
      df_assam_10_2007_sum['Area'],
      df_assam_10_2008_sum['Area'],
      df_assam_10_2009_sum['Area'],
      df_assam_10_2010_sum['Area'],
      df_assam_10_2011_sum['Area'],
      df_assam_10_2012_sum['Area'],
      df_assam_10_2013_sum['Area'],
      df_assam_10_2014_sum['Area'])

y22 =(df_assam_10_1997_sum['Production'],
      df_assam_10_1998_sum['Production'],
      df_assam_10_1999_sum['Production'],
      df_assam_10_2000_sum['Production'],
      df_assam_10_2001_sum['Production'], 
      df_assam_10_2002_sum['Production'],
      df_assam_10_2003_sum['Production'],
      df_assam_10_2004_sum['Production'],
      df_assam_10_2005_sum['Production'],
      df_assam_10_2006_sum['Production'],
      df_assam_10_2007_sum['Production'],
      df_assam_10_2008_sum['Production'],
      df_assam_10_2009_sum['Production'],
      df_assam_10_2010_sum['Production'],
      df_assam_10_2011_sum['Production'],
      df_assam_10_2012_sum['Production'],
      df_assam_10_2013_sum['Production'],
      df_assam_10_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [10] DIMA HASAO (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [10] DIMA HASAO (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [11] GOALPARA

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_11_1997_sum['Area'],
      df_assam_11_1998_sum['Area'],
      df_assam_11_1999_sum['Area'],
      df_assam_11_2000_sum['Area'],
      df_assam_11_2001_sum['Area'], 
      df_assam_11_2002_sum['Area'],
      df_assam_11_2003_sum['Area'],
      df_assam_11_2004_sum['Area'],
      df_assam_11_2005_sum['Area'],
      df_assam_11_2006_sum['Area'],
      df_assam_11_2007_sum['Area'],
      df_assam_11_2008_sum['Area'],
      df_assam_11_2009_sum['Area'],
      df_assam_11_2010_sum['Area'],
      df_assam_11_2011_sum['Area'],
      df_assam_11_2012_sum['Area'],
      df_assam_11_2013_sum['Area'],
      df_assam_11_2014_sum['Area'])

y22 =(df_assam_11_1997_sum['Production'],
      df_assam_11_1998_sum['Production'],
      df_assam_11_1999_sum['Production'],
      df_assam_11_2000_sum['Production'],
      df_assam_11_2001_sum['Production'], 
      df_assam_11_2002_sum['Production'],
      df_assam_11_2003_sum['Production'],
      df_assam_11_2004_sum['Production'],
      df_assam_11_2005_sum['Production'],
      df_assam_11_2006_sum['Production'],
      df_assam_11_2007_sum['Production'],
      df_assam_11_2008_sum['Production'],
      df_assam_11_2009_sum['Production'],
      df_assam_11_2010_sum['Production'],
      df_assam_11_2011_sum['Production'],
      df_assam_11_2012_sum['Production'],
      df_assam_11_2013_sum['Production'],
      df_assam_11_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [11] GOALPARA (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [11] GOALPARA (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [12] GOLAGHAT

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_12_1997_sum['Area'],
      df_assam_12_1998_sum['Area'],
      df_assam_12_1999_sum['Area'],
      df_assam_12_2000_sum['Area'],
      df_assam_12_2001_sum['Area'], 
      df_assam_12_2002_sum['Area'],
      df_assam_12_2003_sum['Area'],
      df_assam_12_2004_sum['Area'],
      df_assam_12_2005_sum['Area'],
      df_assam_12_2006_sum['Area'],
      df_assam_12_2007_sum['Area'],
      df_assam_12_2008_sum['Area'],
      df_assam_12_2009_sum['Area'],
      df_assam_12_2010_sum['Area'],
      df_assam_12_2011_sum['Area'],
      df_assam_12_2012_sum['Area'],
      df_assam_12_2013_sum['Area'],
      df_assam_12_2014_sum['Area'])

y22 =(df_assam_12_1997_sum['Production'],
      df_assam_12_1998_sum['Production'],
      df_assam_12_1999_sum['Production'],
      df_assam_12_2000_sum['Production'],
      df_assam_12_2001_sum['Production'], 
      df_assam_12_2002_sum['Production'],
      df_assam_12_2003_sum['Production'],
      df_assam_12_2004_sum['Production'],
      df_assam_12_2005_sum['Production'],
      df_assam_12_2006_sum['Production'],
      df_assam_12_2007_sum['Production'],
      df_assam_12_2008_sum['Production'],
      df_assam_12_2009_sum['Production'],
      df_assam_12_2010_sum['Production'],
      df_assam_12_2011_sum['Production'],
      df_assam_12_2012_sum['Production'],
      df_assam_12_2013_sum['Production'],
      df_assam_12_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [12] GOLAGHAT (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [12] GOLAGHAT (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [13] HAILAKANDI

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_13_1997_sum['Area'],
      df_assam_13_1998_sum['Area'],
      df_assam_13_1999_sum['Area'],
      df_assam_13_2000_sum['Area'],
      df_assam_13_2001_sum['Area'], 
      df_assam_13_2002_sum['Area'],
      df_assam_13_2003_sum['Area'],
      df_assam_13_2004_sum['Area'],
      df_assam_13_2005_sum['Area'],
      df_assam_13_2006_sum['Area'],
      df_assam_13_2007_sum['Area'],
      df_assam_13_2008_sum['Area'],
      df_assam_13_2009_sum['Area'],
      df_assam_13_2010_sum['Area'],
      df_assam_13_2011_sum['Area'],
      df_assam_13_2012_sum['Area'],
      df_assam_13_2013_sum['Area'],
      df_assam_13_2014_sum['Area'])

y22 =(df_assam_13_1997_sum['Production'],
      df_assam_13_1998_sum['Production'],
      df_assam_13_1999_sum['Production'],
      df_assam_13_2000_sum['Production'],
      df_assam_13_2001_sum['Production'], 
      df_assam_13_2002_sum['Production'],
      df_assam_13_2003_sum['Production'],
      df_assam_13_2004_sum['Production'],
      df_assam_13_2005_sum['Production'],
      df_assam_13_2006_sum['Production'],
      df_assam_13_2007_sum['Production'],
      df_assam_13_2008_sum['Production'],
      df_assam_13_2009_sum['Production'],
      df_assam_13_2010_sum['Production'],
      df_assam_13_2011_sum['Production'],
      df_assam_13_2012_sum['Production'],
      df_assam_13_2013_sum['Production'],
      df_assam_13_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [13] HAILAKANDI (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [13] HAILAKANDI (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [14] JORHAT

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_14_1997_sum['Area'],
      df_assam_14_1998_sum['Area'],
      df_assam_14_1999_sum['Area'],
      df_assam_14_2000_sum['Area'],
      df_assam_14_2001_sum['Area'], 
      df_assam_14_2002_sum['Area'],
      df_assam_14_2003_sum['Area'],
      df_assam_14_2004_sum['Area'],
      df_assam_14_2005_sum['Area'],
      df_assam_14_2006_sum['Area'],
      df_assam_14_2007_sum['Area'],
      df_assam_14_2008_sum['Area'],
      df_assam_14_2009_sum['Area'],
      df_assam_14_2010_sum['Area'],
      df_assam_14_2011_sum['Area'],
      df_assam_14_2012_sum['Area'],
      df_assam_14_2013_sum['Area'],
      df_assam_14_2014_sum['Area'])

y22 =(df_assam_14_1997_sum['Production'],
      df_assam_14_1998_sum['Production'],
      df_assam_14_1999_sum['Production'],
      df_assam_14_2000_sum['Production'],
      df_assam_14_2001_sum['Production'], 
      df_assam_14_2002_sum['Production'],
      df_assam_14_2003_sum['Production'],
      df_assam_14_2004_sum['Production'],
      df_assam_14_2005_sum['Production'],
      df_assam_14_2006_sum['Production'],
      df_assam_14_2007_sum['Production'],
      df_assam_14_2008_sum['Production'],
      df_assam_14_2009_sum['Production'],
      df_assam_14_2010_sum['Production'],
      df_assam_14_2011_sum['Production'],
      df_assam_14_2012_sum['Production'],
      df_assam_14_2013_sum['Production'],
      df_assam_14_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [14] JORHAT (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [14] JORHAT(Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [15] KAMRUP

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_15_1997_sum['Area'],
      df_assam_15_1998_sum['Area'],
      df_assam_15_1999_sum['Area'],
      df_assam_15_2000_sum['Area'],
      df_assam_15_2001_sum['Area'], 
      df_assam_15_2002_sum['Area'],
      df_assam_15_2003_sum['Area'],
      df_assam_15_2004_sum['Area'],
      df_assam_15_2005_sum['Area'],
      df_assam_15_2006_sum['Area'],
      df_assam_15_2007_sum['Area'],
      df_assam_15_2008_sum['Area'],
      df_assam_15_2009_sum['Area'],
      df_assam_15_2010_sum['Area'],
      df_assam_15_2011_sum['Area'],
      df_assam_15_2012_sum['Area'],
      df_assam_15_2013_sum['Area'],
      df_assam_15_2014_sum['Area'])

y22 =(df_assam_15_1997_sum['Production'],
      df_assam_15_1998_sum['Production'],
      df_assam_15_1999_sum['Production'],
      df_assam_15_2000_sum['Production'],
      df_assam_15_2001_sum['Production'], 
      df_assam_15_2002_sum['Production'],
      df_assam_15_2003_sum['Production'],
      df_assam_15_2004_sum['Production'],
      df_assam_15_2005_sum['Production'],
      df_assam_15_2006_sum['Production'],
      df_assam_15_2007_sum['Production'],
      df_assam_15_2008_sum['Production'],
      df_assam_15_2009_sum['Production'],
      df_assam_15_2010_sum['Production'],
      df_assam_15_2011_sum['Production'],
      df_assam_15_2012_sum['Production'],
      df_assam_15_2013_sum['Production'],
      df_assam_15_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [15] KAMRUP (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [15] KAMRUP (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [16] KAMRUP METRO

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_16_1997_sum['Area'],
      df_assam_16_1998_sum['Area'],
      df_assam_16_1999_sum['Area'],
      df_assam_16_2000_sum['Area'],
      df_assam_16_2001_sum['Area'], 
      df_assam_16_2002_sum['Area'],
      df_assam_16_2003_sum['Area'],
      df_assam_16_2004_sum['Area'],
      df_assam_16_2005_sum['Area'],
      df_assam_16_2006_sum['Area'],
      df_assam_16_2007_sum['Area'],
      df_assam_16_2008_sum['Area'],
      df_assam_16_2009_sum['Area'],
      df_assam_16_2010_sum['Area'],
      df_assam_16_2011_sum['Area'],
      df_assam_16_2012_sum['Area'],
      df_assam_16_2013_sum['Area'],
      df_assam_16_2014_sum['Area'])

y22 =(df_assam_16_1997_sum['Production'],
      df_assam_16_1998_sum['Production'],
      df_assam_16_1999_sum['Production'],
      df_assam_16_2000_sum['Production'],
      df_assam_16_2001_sum['Production'], 
      df_assam_16_2002_sum['Production'],
      df_assam_16_2003_sum['Production'],
      df_assam_16_2004_sum['Production'],
      df_assam_16_2005_sum['Production'],
      df_assam_16_2006_sum['Production'],
      df_assam_16_2007_sum['Production'],
      df_assam_16_2008_sum['Production'],
      df_assam_16_2009_sum['Production'],
      df_assam_16_2010_sum['Production'],
      df_assam_16_2011_sum['Production'],
      df_assam_16_2012_sum['Production'],
      df_assam_16_2013_sum['Production'],
      df_assam_16_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [16] KAMRUP METRO (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [16] KAMRUP METRO (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show() 
   
# plotting  Assam : [17] KARBI ANGLONG

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_17_1997_sum['Area'],
      df_assam_17_1998_sum['Area'],
      df_assam_17_1999_sum['Area'],
      df_assam_17_2000_sum['Area'],
      df_assam_17_2001_sum['Area'], 
      df_assam_17_2002_sum['Area'],
      df_assam_17_2003_sum['Area'],
      df_assam_17_2004_sum['Area'],
      df_assam_17_2005_sum['Area'],
      df_assam_17_2006_sum['Area'],
      df_assam_17_2007_sum['Area'],
      df_assam_17_2008_sum['Area'],
      df_assam_17_2009_sum['Area'],
      df_assam_17_2010_sum['Area'],
      df_assam_17_2011_sum['Area'],
      df_assam_17_2012_sum['Area'],
      df_assam_17_2013_sum['Area'],
      df_assam_17_2014_sum['Area'])

y22 =(df_assam_17_1997_sum['Production'],
      df_assam_17_1998_sum['Production'],
      df_assam_17_1999_sum['Production'],
      df_assam_17_2000_sum['Production'],
      df_assam_17_2001_sum['Production'], 
      df_assam_17_2002_sum['Production'],
      df_assam_17_2003_sum['Production'],
      df_assam_17_2004_sum['Production'],
      df_assam_17_2005_sum['Production'],
      df_assam_17_2006_sum['Production'],
      df_assam_17_2007_sum['Production'],
      df_assam_17_2008_sum['Production'],
      df_assam_17_2009_sum['Production'],
      df_assam_17_2010_sum['Production'],
      df_assam_17_2011_sum['Production'],
      df_assam_17_2012_sum['Production'],
      df_assam_17_2013_sum['Production'],
      df_assam_17_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [17] KARBI ANGLONG (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [17] KARBI ANGLONG (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [18] KARIMGANJ 

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_18_1997_sum['Area'],
      df_assam_18_1998_sum['Area'],
      df_assam_18_1999_sum['Area'],
      df_assam_18_2000_sum['Area'],
      df_assam_18_2001_sum['Area'], 
      df_assam_18_2002_sum['Area'],
      df_assam_18_2003_sum['Area'],
      df_assam_18_2004_sum['Area'],
      df_assam_18_2005_sum['Area'],
      df_assam_18_2006_sum['Area'],
      df_assam_18_2007_sum['Area'],
      df_assam_18_2008_sum['Area'],
      df_assam_18_2009_sum['Area'],
      df_assam_18_2010_sum['Area'],
      df_assam_18_2011_sum['Area'],
      df_assam_18_2012_sum['Area'],
      df_assam_18_2013_sum['Area'],
      df_assam_18_2014_sum['Area'])

y22 =(df_assam_18_1997_sum['Production'],
      df_assam_18_1998_sum['Production'],
      df_assam_18_1999_sum['Production'],
      df_assam_18_2000_sum['Production'],
      df_assam_18_2001_sum['Production'], 
      df_assam_18_2002_sum['Production'],
      df_assam_18_2003_sum['Production'],
      df_assam_18_2004_sum['Production'],
      df_assam_18_2005_sum['Production'],
      df_assam_18_2006_sum['Production'],
      df_assam_18_2007_sum['Production'],
      df_assam_18_2008_sum['Production'],
      df_assam_18_2009_sum['Production'],
      df_assam_18_2010_sum['Production'],
      df_assam_18_2011_sum['Production'],
      df_assam_18_2012_sum['Production'],
      df_assam_18_2013_sum['Production'],
      df_assam_18_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [18] KARIMGANJ (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [18] KARIMGANJ (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [19] KOKRAJHAR 

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_19_1997_sum['Area'],
      df_assam_19_1998_sum['Area'],
      df_assam_19_1999_sum['Area'],
      df_assam_19_2000_sum['Area'],
      df_assam_19_2001_sum['Area'], 
      df_assam_19_2002_sum['Area'],
      df_assam_19_2003_sum['Area'],
      df_assam_19_2004_sum['Area'],
      df_assam_19_2005_sum['Area'],
      df_assam_19_2006_sum['Area'],
      df_assam_19_2007_sum['Area'],
      df_assam_19_2008_sum['Area'],
      df_assam_19_2009_sum['Area'],
      df_assam_19_2010_sum['Area'],
      df_assam_19_2011_sum['Area'],
      df_assam_19_2012_sum['Area'],
      df_assam_19_2013_sum['Area'],
      df_assam_19_2014_sum['Area'])

y22 =(df_assam_19_1997_sum['Production'],
      df_assam_19_1998_sum['Production'],
      df_assam_19_1999_sum['Production'],
      df_assam_19_2000_sum['Production'],
      df_assam_19_2001_sum['Production'], 
      df_assam_19_2002_sum['Production'],
      df_assam_19_2003_sum['Production'],
      df_assam_19_2004_sum['Production'],
      df_assam_19_2005_sum['Production'],
      df_assam_19_2006_sum['Production'],
      df_assam_19_2007_sum['Production'],
      df_assam_19_2008_sum['Production'],
      df_assam_19_2009_sum['Production'],
      df_assam_19_2010_sum['Production'],
      df_assam_19_2011_sum['Production'],
      df_assam_19_2012_sum['Production'],
      df_assam_19_2013_sum['Production'],
      df_assam_19_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [19] KOKRAJHAR (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [19] KOKRAJHAR  (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [20] LAKHIMPUR 

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_20_1997_sum['Area'],
      df_assam_20_1998_sum['Area'],
      df_assam_20_1999_sum['Area'],
      df_assam_20_2000_sum['Area'],
      df_assam_20_2001_sum['Area'], 
      df_assam_20_2002_sum['Area'],
      df_assam_20_2003_sum['Area'],
      df_assam_20_2004_sum['Area'],
      df_assam_20_2005_sum['Area'],
      df_assam_20_2006_sum['Area'],
      df_assam_20_2007_sum['Area'],
      df_assam_20_2008_sum['Area'],
      df_assam_20_2009_sum['Area'],
      df_assam_20_2010_sum['Area'],
      df_assam_20_2011_sum['Area'],
      df_assam_20_2012_sum['Area'],
      df_assam_20_2013_sum['Area'],
      df_assam_20_2014_sum['Area'])

y22 =(df_assam_20_1997_sum['Production'],
      df_assam_20_1998_sum['Production'],
      df_assam_20_1999_sum['Production'],
      df_assam_20_2000_sum['Production'],
      df_assam_20_2001_sum['Production'], 
      df_assam_20_2002_sum['Production'],
      df_assam_20_2003_sum['Production'],
      df_assam_20_2004_sum['Production'],
      df_assam_20_2005_sum['Production'],
      df_assam_20_2006_sum['Production'],
      df_assam_20_2007_sum['Production'],
      df_assam_20_2008_sum['Production'],
      df_assam_20_2009_sum['Production'],
      df_assam_20_2010_sum['Production'],
      df_assam_20_2011_sum['Production'],
      df_assam_20_2012_sum['Production'],
      df_assam_20_2013_sum['Production'],
      df_assam_20_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [20] LAKHIMPUR (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [20] LAKHIMPUR (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [21] MARIGAON 

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_21_1997_sum['Area'],
      df_assam_21_1998_sum['Area'],
      df_assam_21_1999_sum['Area'],
      df_assam_21_2000_sum['Area'],
      df_assam_21_2001_sum['Area'], 
      df_assam_21_2002_sum['Area'],
      df_assam_21_2003_sum['Area'],
      df_assam_21_2004_sum['Area'],
      df_assam_21_2005_sum['Area'],
      df_assam_21_2006_sum['Area'],
      df_assam_21_2007_sum['Area'],
      df_assam_21_2008_sum['Area'],
      df_assam_21_2009_sum['Area'],
      df_assam_21_2010_sum['Area'],
      df_assam_21_2011_sum['Area'],
      df_assam_21_2012_sum['Area'],
      df_assam_21_2013_sum['Area'],
      df_assam_21_2014_sum['Area'])

y22 =(df_assam_21_1997_sum['Production'],
      df_assam_21_1998_sum['Production'],
      df_assam_21_1999_sum['Production'],
      df_assam_21_2000_sum['Production'],
      df_assam_21_2001_sum['Production'], 
      df_assam_21_2002_sum['Production'],
      df_assam_21_2003_sum['Production'],
      df_assam_21_2004_sum['Production'],
      df_assam_21_2005_sum['Production'],
      df_assam_21_2006_sum['Production'],
      df_assam_21_2007_sum['Production'],
      df_assam_21_2008_sum['Production'],
      df_assam_21_2009_sum['Production'],
      df_assam_21_2010_sum['Production'],
      df_assam_21_2011_sum['Production'],
      df_assam_21_2012_sum['Production'],
      df_assam_21_2013_sum['Production'],
      df_assam_21_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [21] MARIGAON (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [21] MARIGAON (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [22] NAGAON

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_22_1997_sum['Area'],
      df_assam_22_1998_sum['Area'],
      df_assam_22_1999_sum['Area'],
      df_assam_22_2000_sum['Area'],
      df_assam_22_2001_sum['Area'], 
      df_assam_22_2002_sum['Area'],
      df_assam_22_2003_sum['Area'],
      df_assam_22_2004_sum['Area'],
      df_assam_22_2005_sum['Area'],
      df_assam_22_2006_sum['Area'],
      df_assam_22_2007_sum['Area'],
      df_assam_22_2008_sum['Area'],
      df_assam_22_2009_sum['Area'],
      df_assam_22_2010_sum['Area'],
      df_assam_22_2011_sum['Area'],
      df_assam_22_2012_sum['Area'],
      df_assam_22_2013_sum['Area'],
      df_assam_22_2014_sum['Area'])

y22 =(df_assam_22_1997_sum['Production'],
      df_assam_22_1998_sum['Production'],
      df_assam_22_1999_sum['Production'],
      df_assam_22_2000_sum['Production'],
      df_assam_22_2001_sum['Production'], 
      df_assam_22_2002_sum['Production'],
      df_assam_22_2003_sum['Production'],
      df_assam_22_2004_sum['Production'],
      df_assam_22_2005_sum['Production'],
      df_assam_22_2006_sum['Production'],
      df_assam_22_2007_sum['Production'],
      df_assam_22_2008_sum['Production'],
      df_assam_22_2009_sum['Production'],
      df_assam_22_2010_sum['Production'],
      df_assam_22_2011_sum['Production'],
      df_assam_22_2012_sum['Production'],
      df_assam_22_2013_sum['Production'],
      df_assam_22_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [22] NAGAON (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show()

plt.subplot(122)
plt.title('State-4 : Assam : [22] NAGAON (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [23] NALBARI

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_23_1997_sum['Area'],
      df_assam_23_1998_sum['Area'],
      df_assam_23_1999_sum['Area'],
      df_assam_23_2000_sum['Area'],
      df_assam_23_2001_sum['Area'], 
      df_assam_23_2002_sum['Area'],
      df_assam_23_2003_sum['Area'],
      df_assam_23_2004_sum['Area'],
      df_assam_23_2005_sum['Area'],
      df_assam_23_2006_sum['Area'],
      df_assam_23_2007_sum['Area'],
      df_assam_23_2008_sum['Area'],
      df_assam_23_2009_sum['Area'],
      df_assam_23_2010_sum['Area'],
      df_assam_23_2011_sum['Area'],
      df_assam_23_2012_sum['Area'],
      df_assam_23_2013_sum['Area'],
      df_assam_23_2014_sum['Area'])

y22 =(df_assam_23_1997_sum['Production'],
      df_assam_23_1998_sum['Production'],
      df_assam_23_1999_sum['Production'],
      df_assam_23_2000_sum['Production'],
      df_assam_23_2001_sum['Production'], 
      df_assam_23_2002_sum['Production'],
      df_assam_23_2003_sum['Production'],
      df_assam_23_2004_sum['Production'],
      df_assam_23_2005_sum['Production'],
      df_assam_23_2006_sum['Production'],
      df_assam_23_2007_sum['Production'],
      df_assam_23_2008_sum['Production'],
      df_assam_23_2009_sum['Production'],
      df_assam_23_2010_sum['Production'],
      df_assam_23_2011_sum['Production'],
      df_assam_23_2012_sum['Production'],
      df_assam_23_2013_sum['Production'],
      df_assam_23_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [23] NALBARI (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [23] NALBARI (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [24] SIVASAGAR 

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_24_1997_sum['Area'],
      df_assam_24_1998_sum['Area'],
      df_assam_24_1999_sum['Area'],
      df_assam_24_2000_sum['Area'],
      df_assam_24_2001_sum['Area'], 
      df_assam_24_2002_sum['Area'],
      df_assam_24_2003_sum['Area'],
      df_assam_24_2004_sum['Area'],
      df_assam_24_2005_sum['Area'],
      df_assam_24_2006_sum['Area'],
      df_assam_24_2007_sum['Area'],
      df_assam_24_2008_sum['Area'],
      df_assam_24_2009_sum['Area'],
      df_assam_24_2010_sum['Area'],
      df_assam_24_2011_sum['Area'],
      df_assam_24_2012_sum['Area'],
      df_assam_24_2013_sum['Area'],
      df_assam_24_2014_sum['Area'])

y22 =(df_assam_24_1997_sum['Production'],
      df_assam_24_1998_sum['Production'],
      df_assam_24_1999_sum['Production'],
      df_assam_24_2000_sum['Production'],
      df_assam_24_2001_sum['Production'], 
      df_assam_24_2002_sum['Production'],
      df_assam_24_2003_sum['Production'],
      df_assam_24_2004_sum['Production'],
      df_assam_24_2005_sum['Production'],
      df_assam_24_2006_sum['Production'],
      df_assam_24_2007_sum['Production'],
      df_assam_24_2008_sum['Production'],
      df_assam_24_2009_sum['Production'],
      df_assam_24_2010_sum['Production'],
      df_assam_24_2011_sum['Production'],
      df_assam_24_2012_sum['Production'],
      df_assam_24_2013_sum['Production'],
      df_assam_24_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [24] SIVASAGAR (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [24] SIVASAGAR (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [25] SONITPUR

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_25_1997_sum['Area'],
      df_assam_25_1998_sum['Area'],
      df_assam_25_1999_sum['Area'],
      df_assam_25_2000_sum['Area'],
      df_assam_25_2001_sum['Area'], 
      df_assam_25_2002_sum['Area'],
      df_assam_25_2003_sum['Area'],
      df_assam_25_2004_sum['Area'],
      df_assam_25_2005_sum['Area'],
      df_assam_25_2006_sum['Area'],
      df_assam_25_2007_sum['Area'],
      df_assam_25_2008_sum['Area'],
      df_assam_25_2009_sum['Area'],
      df_assam_25_2010_sum['Area'],
      df_assam_25_2011_sum['Area'],
      df_assam_25_2012_sum['Area'],
      df_assam_25_2013_sum['Area'],
      df_assam_25_2014_sum['Area'])

y22 =(df_assam_25_1997_sum['Production'],
      df_assam_25_1998_sum['Production'],
      df_assam_25_1999_sum['Production'],
      df_assam_25_2000_sum['Production'],
      df_assam_25_2001_sum['Production'], 
      df_assam_25_2002_sum['Production'],
      df_assam_25_2003_sum['Production'],
      df_assam_25_2004_sum['Production'],
      df_assam_25_2005_sum['Production'],
      df_assam_25_2006_sum['Production'],
      df_assam_25_2007_sum['Production'],
      df_assam_25_2008_sum['Production'],
      df_assam_25_2009_sum['Production'],
      df_assam_25_2010_sum['Production'],
      df_assam_25_2011_sum['Production'],
      df_assam_25_2012_sum['Production'],
      df_assam_25_2013_sum['Production'],
      df_assam_25_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [25] SONITPUR (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [25] SONITPUR (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [26] TINSUKIA

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_26_1997_sum['Area'],
      df_assam_26_1998_sum['Area'],
      df_assam_26_1999_sum['Area'],
      df_assam_26_2000_sum['Area'],
      df_assam_26_2001_sum['Area'], 
      df_assam_26_2002_sum['Area'],
      df_assam_26_2003_sum['Area'],
      df_assam_26_2004_sum['Area'],
      df_assam_26_2005_sum['Area'],
      df_assam_26_2006_sum['Area'],
      df_assam_26_2007_sum['Area'],
      df_assam_26_2008_sum['Area'],
      df_assam_26_2009_sum['Area'],
      df_assam_26_2010_sum['Area'],
      df_assam_26_2011_sum['Area'],
      df_assam_26_2012_sum['Area'],
      df_assam_26_2013_sum['Area'],
      df_assam_26_2014_sum['Area'])

y22 =(df_assam_26_1997_sum['Production'],
      df_assam_26_1998_sum['Production'],
      df_assam_26_1999_sum['Production'],
      df_assam_26_2000_sum['Production'],
      df_assam_26_2001_sum['Production'], 
      df_assam_26_2002_sum['Production'],
      df_assam_26_2003_sum['Production'],
      df_assam_26_2004_sum['Production'],
      df_assam_26_2005_sum['Production'],
      df_assam_26_2006_sum['Production'],
      df_assam_26_2007_sum['Production'],
      df_assam_26_2008_sum['Production'],
      df_assam_26_2009_sum['Production'],
      df_assam_26_2010_sum['Production'],
      df_assam_26_2011_sum['Production'],
      df_assam_26_2012_sum['Production'],
      df_assam_26_2013_sum['Production'],
      df_assam_26_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [26] TINSUKIA (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [26] TINSUKIA (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  Assam : [27] UDALGURI

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_assam_27_1997_sum['Area'],
      df_assam_27_1998_sum['Area'],
      df_assam_27_1999_sum['Area'],
      df_assam_27_2000_sum['Area'],
      df_assam_27_2001_sum['Area'], 
      df_assam_27_2002_sum['Area'],
      df_assam_27_2003_sum['Area'],
      df_assam_27_2004_sum['Area'],
      df_assam_27_2005_sum['Area'],
      df_assam_27_2006_sum['Area'],
      df_assam_27_2007_sum['Area'],
      df_assam_27_2008_sum['Area'],
      df_assam_27_2009_sum['Area'],
      df_assam_27_2010_sum['Area'],
      df_assam_27_2011_sum['Area'],
      df_assam_27_2012_sum['Area'],
      df_assam_27_2013_sum['Area'],
      df_assam_27_2014_sum['Area'])

y22 =(df_assam_27_1997_sum['Production'],
      df_assam_27_1998_sum['Production'],
      df_assam_27_1999_sum['Production'],
      df_assam_27_2000_sum['Production'],
      df_assam_27_2001_sum['Production'], 
      df_assam_27_2002_sum['Production'],
      df_assam_27_2003_sum['Production'],
      df_assam_27_2004_sum['Production'],
      df_assam_27_2005_sum['Production'],
      df_assam_27_2006_sum['Production'],
      df_assam_27_2007_sum['Production'],
      df_assam_27_2008_sum['Production'],
      df_assam_27_2009_sum['Production'],
      df_assam_27_2010_sum['Production'],
      df_assam_27_2011_sum['Production'],
      df_assam_27_2012_sum['Production'],
      df_assam_27_2013_sum['Production'],
      df_assam_27_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-4 : Assam : [27] UDALGURI (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-4 : Assam : [27] UDALGURI (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting of West Bengal 'Area' and 'Production'

# plotting  wb : [1] 24 PARAGANAS NORTH 
                                  
x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_1_1997_sum['Area'],
      df_wb_1_1998_sum['Area'],
      df_wb_1_1999_sum['Area'],
      df_wb_1_2000_sum['Area'],
      df_wb_1_2001_sum['Area'], 
      df_wb_1_2002_sum['Area'],
      df_wb_1_2003_sum['Area'],
      df_wb_1_2004_sum['Area'],
      df_wb_1_2005_sum['Area'],
      df_wb_1_2006_sum['Area'],
      df_wb_1_2007_sum['Area'],
      df_wb_1_2008_sum['Area'],
      df_wb_1_2009_sum['Area'],
      df_wb_1_2010_sum['Area'],
      df_wb_1_2011_sum['Area'],
      df_wb_1_2012_sum['Area'],
      df_wb_1_2013_sum['Area'],
      df_wb_1_2014_sum['Area'])

y22 =(df_wb_1_1997_sum['Production'],
      df_wb_1_1998_sum['Production'],
      df_wb_1_1999_sum['Production'],
      df_wb_1_2000_sum['Production'],
      df_wb_1_2001_sum['Production'], 
      df_wb_1_2002_sum['Production'],
      df_wb_1_2003_sum['Production'],
      df_wb_1_2004_sum['Production'],
      df_wb_1_2005_sum['Production'],
      df_wb_1_2006_sum['Production'],
      df_wb_1_2007_sum['Production'],
      df_wb_1_2008_sum['Production'],
      df_wb_1_2009_sum['Production'],
      df_wb_1_2010_sum['Production'],
      df_wb_1_2011_sum['Production'],
      df_wb_1_2012_sum['Production'],
      df_wb_1_2013_sum['Production'],
      df_wb_1_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [1] 24 PARAGANAS NORTH(Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [1] 24 PARAGANAS NORTH(Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [2] 24 PARAGANAS SOUTH

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_2_1997_sum['Area'],
      df_wb_2_1998_sum['Area'],
      df_wb_2_1999_sum['Area'],
      df_wb_2_2000_sum['Area'],
      df_wb_2_2001_sum['Area'], 
      df_wb_2_2002_sum['Area'],
      df_wb_2_2003_sum['Area'],
      df_wb_2_2004_sum['Area'],
      df_wb_2_2005_sum['Area'],
      df_wb_2_2006_sum['Area'],
      df_wb_2_2007_sum['Area'],
      df_wb_2_2008_sum['Area'],
      df_wb_2_2009_sum['Area'],
      df_wb_2_2010_sum['Area'],
      df_wb_2_2011_sum['Area'],
      df_wb_2_2012_sum['Area'],
      df_wb_2_2013_sum['Area'],
      df_wb_2_2014_sum['Area'])

y22 =(df_wb_2_1997_sum['Production'],
      df_wb_2_1998_sum['Production'],
      df_wb_2_1999_sum['Production'],
      df_wb_2_2000_sum['Production'],
      df_wb_2_2001_sum['Production'], 
      df_wb_2_2002_sum['Production'],
      df_wb_2_2003_sum['Production'],
      df_wb_2_2004_sum['Production'],
      df_wb_2_2005_sum['Production'],
      df_wb_2_2006_sum['Production'],
      df_wb_2_2007_sum['Production'],
      df_wb_2_2008_sum['Production'],
      df_wb_2_2009_sum['Production'],
      df_wb_2_2010_sum['Production'],
      df_wb_2_2011_sum['Production'],
      df_wb_2_2012_sum['Production'],
      df_wb_2_2013_sum['Production'],
      df_wb_2_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [2] 24 PARAGANAS SOUTH(Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [2] 24 PARAGANAS SOUTH(Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [3] BANKURA

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_3_1997_sum['Area'],
      df_wb_3_1998_sum['Area'],
      df_wb_3_1999_sum['Area'],
      df_wb_3_2000_sum['Area'],
      df_wb_3_2001_sum['Area'], 
      df_wb_3_2002_sum['Area'],
      df_wb_3_2003_sum['Area'],
      df_wb_3_2004_sum['Area'],
      df_wb_3_2005_sum['Area'],
      df_wb_3_2006_sum['Area'],
      df_wb_3_2007_sum['Area'],
      df_wb_3_2008_sum['Area'],
      df_wb_3_2009_sum['Area'],
      df_wb_3_2010_sum['Area'],
      df_wb_3_2011_sum['Area'],
      df_wb_3_2012_sum['Area'],
      df_wb_3_2013_sum['Area'],
      df_wb_3_2014_sum['Area'])

y22 =(df_wb_3_1997_sum['Production'],
      df_wb_3_1998_sum['Production'],
      df_wb_3_1999_sum['Production'],
      df_wb_3_2000_sum['Production'],
      df_wb_3_2001_sum['Production'], 
      df_wb_3_2002_sum['Production'],
      df_wb_3_2003_sum['Production'],
      df_wb_3_2004_sum['Production'],
      df_wb_3_2005_sum['Production'],
      df_wb_3_2006_sum['Production'],
      df_wb_3_2007_sum['Production'],
      df_wb_3_2008_sum['Production'],
      df_wb_3_2009_sum['Production'],
      df_wb_3_2010_sum['Production'],
      df_wb_3_2011_sum['Production'],
      df_wb_3_2012_sum['Production'],
      df_wb_3_2013_sum['Production'],
      df_wb_3_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [3] BANKURA (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [3] BANKURA (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [4] BARDHAMAN 

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_4_1997_sum['Area'],
      df_wb_4_1998_sum['Area'],
      df_wb_4_1999_sum['Area'],
      df_wb_4_2000_sum['Area'],
      df_wb_4_2001_sum['Area'], 
      df_wb_4_2002_sum['Area'],
      df_wb_4_2003_sum['Area'],
      df_wb_4_2004_sum['Area'],
      df_wb_4_2005_sum['Area'],
      df_wb_4_2006_sum['Area'],
      df_wb_4_2007_sum['Area'],
      df_wb_4_2008_sum['Area'],
      df_wb_4_2009_sum['Area'],
      df_wb_4_2010_sum['Area'],
      df_wb_4_2011_sum['Area'],
      df_wb_4_2012_sum['Area'],
      df_wb_4_2013_sum['Area'],
      df_wb_4_2014_sum['Area'])

y22 =(df_wb_4_1997_sum['Production'],
      df_wb_4_1998_sum['Production'],
      df_wb_4_1999_sum['Production'],
      df_wb_4_2000_sum['Production'],
      df_wb_4_2001_sum['Production'], 
      df_wb_4_2002_sum['Production'],
      df_wb_4_2003_sum['Production'],
      df_wb_4_2004_sum['Production'],
      df_wb_4_2005_sum['Production'],
      df_wb_4_2006_sum['Production'],
      df_wb_4_2007_sum['Production'],
      df_wb_4_2008_sum['Production'],
      df_wb_4_2009_sum['Production'],
      df_wb_4_2010_sum['Production'],
      df_wb_4_2011_sum['Production'],
      df_wb_4_2012_sum['Production'],
      df_wb_4_2013_sum['Production'],
      df_wb_4_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [4] BARDHAMAN (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [4] BARDHAMAN (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [5] BIRBHUM 

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_5_1997_sum['Area'],
      df_wb_5_1998_sum['Area'],
      df_wb_5_1999_sum['Area'],
      df_wb_5_2000_sum['Area'],
      df_wb_5_2001_sum['Area'], 
      df_wb_5_2002_sum['Area'],
      df_wb_5_2003_sum['Area'],
      df_wb_5_2004_sum['Area'],
      df_wb_5_2005_sum['Area'],
      df_wb_5_2006_sum['Area'],
      df_wb_5_2007_sum['Area'],
      df_wb_5_2008_sum['Area'],
      df_wb_5_2009_sum['Area'],
      df_wb_5_2010_sum['Area'],
      df_wb_5_2011_sum['Area'],
      df_wb_5_2012_sum['Area'],
      df_wb_5_2013_sum['Area'],
      df_wb_5_2014_sum['Area'])

y22 =(df_wb_5_1997_sum['Production'],
      df_wb_5_1998_sum['Production'],
      df_wb_5_1999_sum['Production'],
      df_wb_5_2000_sum['Production'],
      df_wb_5_2001_sum['Production'], 
      df_wb_5_2002_sum['Production'],
      df_wb_5_2003_sum['Production'],
      df_wb_5_2004_sum['Production'],
      df_wb_5_2005_sum['Production'],
      df_wb_5_2006_sum['Production'],
      df_wb_5_2007_sum['Production'],
      df_wb_5_2008_sum['Production'],
      df_wb_5_2009_sum['Production'],
      df_wb_5_2010_sum['Production'],
      df_wb_5_2011_sum['Production'],
      df_wb_5_2012_sum['Production'],
      df_wb_5_2013_sum['Production'],
      df_wb_5_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [5] BIRBHUM (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [5] BIRBHUM (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [6] COOCHBEHAR

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_6_1997_sum['Area'],
      df_wb_6_1998_sum['Area'],
      df_wb_6_1999_sum['Area'],
      df_wb_6_2000_sum['Area'],
      df_wb_6_2001_sum['Area'], 
      df_wb_6_2002_sum['Area'],
      df_wb_6_2003_sum['Area'],
      df_wb_6_2004_sum['Area'],
      df_wb_6_2005_sum['Area'],
      df_wb_6_2006_sum['Area'],
      df_wb_6_2007_sum['Area'],
      df_wb_6_2008_sum['Area'],
      df_wb_6_2009_sum['Area'],
      df_wb_6_2010_sum['Area'],
      df_wb_6_2011_sum['Area'],
      df_wb_6_2012_sum['Area'],
      df_wb_6_2013_sum['Area'],
      df_wb_6_2014_sum['Area'])

y22 =(df_wb_6_1997_sum['Production'],
      df_wb_6_1998_sum['Production'],
      df_wb_6_1999_sum['Production'],
      df_wb_6_2000_sum['Production'],
      df_wb_6_2001_sum['Production'], 
      df_wb_6_2002_sum['Production'],
      df_wb_6_2003_sum['Production'],
      df_wb_6_2004_sum['Production'],
      df_wb_6_2005_sum['Production'],
      df_wb_6_2006_sum['Production'],
      df_wb_6_2007_sum['Production'],
      df_wb_6_2008_sum['Production'],
      df_wb_6_2009_sum['Production'],
      df_wb_6_2010_sum['Production'],
      df_wb_6_2011_sum['Production'],
      df_wb_6_2012_sum['Production'],
      df_wb_6_2013_sum['Production'],
      df_wb_6_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [6] COOCHBEHAR (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [6] COOCHBEHAR (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [7] DARJEELING

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_7_1997_sum['Area'],
      df_wb_7_1998_sum['Area'],
      df_wb_7_1999_sum['Area'],
      df_wb_7_2000_sum['Area'],
      df_wb_7_2001_sum['Area'], 
      df_wb_7_2002_sum['Area'],
      df_wb_7_2003_sum['Area'],
      df_wb_7_2004_sum['Area'],
      df_wb_7_2005_sum['Area'],
      df_wb_7_2006_sum['Area'],
      df_wb_7_2007_sum['Area'],
      df_wb_7_2008_sum['Area'],
      df_wb_7_2009_sum['Area'],
      df_wb_7_2010_sum['Area'],
      df_wb_7_2011_sum['Area'],
      df_wb_7_2012_sum['Area'],
      df_wb_7_2013_sum['Area'],
      df_wb_7_2014_sum['Area'])

y22 =(df_wb_7_1997_sum['Production'],
      df_wb_7_1998_sum['Production'],
      df_wb_7_1999_sum['Production'],
      df_wb_7_2000_sum['Production'],
      df_wb_7_2001_sum['Production'], 
      df_wb_7_2002_sum['Production'],
      df_wb_7_2003_sum['Production'],
      df_wb_7_2004_sum['Production'],
      df_wb_7_2005_sum['Production'],
      df_wb_7_2006_sum['Production'],
      df_wb_7_2007_sum['Production'],
      df_wb_7_2008_sum['Production'],
      df_wb_7_2009_sum['Production'],
      df_wb_7_2010_sum['Production'],
      df_wb_7_2011_sum['Production'],
      df_wb_7_2012_sum['Production'],
      df_wb_7_2013_sum['Production'],
      df_wb_7_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [7] DARJEELING (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [7] DARJEELING (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [8] DINAJPUR DAKSHIN

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_8_1997_sum['Area'],
      df_wb_8_1998_sum['Area'],
      df_wb_8_1999_sum['Area'],
      df_wb_8_2000_sum['Area'],
      df_wb_8_2001_sum['Area'], 
      df_wb_8_2002_sum['Area'],
      df_wb_8_2003_sum['Area'],
      df_wb_8_2004_sum['Area'],
      df_wb_8_2005_sum['Area'],
      df_wb_8_2006_sum['Area'],
      df_wb_8_2007_sum['Area'],
      df_wb_8_2008_sum['Area'],
      df_wb_8_2009_sum['Area'],
      df_wb_8_2010_sum['Area'],
      df_wb_8_2011_sum['Area'],
      df_wb_8_2012_sum['Area'],
      df_wb_8_2013_sum['Area'],
      df_wb_8_2014_sum['Area'])

y22 =(df_wb_8_1997_sum['Production'],
      df_wb_8_1998_sum['Production'],
      df_wb_8_1999_sum['Production'],
      df_wb_8_2000_sum['Production'],
      df_wb_8_2001_sum['Production'], 
      df_wb_8_2002_sum['Production'],
      df_wb_8_2003_sum['Production'],
      df_wb_8_2004_sum['Production'],
      df_wb_8_2005_sum['Production'],
      df_wb_8_2006_sum['Production'],
      df_wb_8_2007_sum['Production'],
      df_wb_8_2008_sum['Production'],
      df_wb_8_2009_sum['Production'],
      df_wb_8_2010_sum['Production'],
      df_wb_8_2011_sum['Production'],
      df_wb_8_2012_sum['Production'],
      df_wb_8_2013_sum['Production'],
      df_wb_8_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [8] DINAJPUR DAKSHIN (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [8] DINAJPUR DAKSHIN (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [9] DINAJPUR UTTAR

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_9_1997_sum['Area'],
      df_wb_9_1998_sum['Area'],
      df_wb_9_1999_sum['Area'],
      df_wb_9_2000_sum['Area'],
      df_wb_9_2001_sum['Area'], 
      df_wb_9_2002_sum['Area'],
      df_wb_9_2003_sum['Area'],
      df_wb_9_2004_sum['Area'],
      df_wb_9_2005_sum['Area'],
      df_wb_9_2006_sum['Area'],
      df_wb_9_2007_sum['Area'],
      df_wb_9_2008_sum['Area'],
      df_wb_9_2009_sum['Area'],
      df_wb_9_2010_sum['Area'],
      df_wb_9_2011_sum['Area'],
      df_wb_9_2012_sum['Area'],
      df_wb_9_2013_sum['Area'],
      df_wb_9_2014_sum['Area'])

y22 =(df_wb_9_1997_sum['Production'],
      df_wb_9_1998_sum['Production'],
      df_wb_9_1999_sum['Production'],
      df_wb_9_2000_sum['Production'],
      df_wb_9_2001_sum['Production'], 
      df_wb_9_2002_sum['Production'],
      df_wb_9_2003_sum['Production'],
      df_wb_9_2004_sum['Production'],
      df_wb_9_2005_sum['Production'],
      df_wb_9_2006_sum['Production'],
      df_wb_9_2007_sum['Production'],
      df_wb_9_2008_sum['Production'],
      df_wb_9_2009_sum['Production'],
      df_wb_9_2010_sum['Production'],
      df_wb_9_2011_sum['Production'],
      df_wb_9_2012_sum['Production'],
      df_wb_9_2013_sum['Production'],
      df_wb_9_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [9] DINAJPUR UTTAR (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [9] DINAJPUR UTTAR (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [10] HOOGHLY

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_10_1997_sum['Area'],
      df_wb_10_1998_sum['Area'],
      df_wb_10_1999_sum['Area'],
      df_wb_10_2000_sum['Area'],
      df_wb_10_2001_sum['Area'], 
      df_wb_10_2002_sum['Area'],
      df_wb_10_2003_sum['Area'],
      df_wb_10_2004_sum['Area'],
      df_wb_10_2005_sum['Area'],
      df_wb_10_2006_sum['Area'],
      df_wb_10_2007_sum['Area'],
      df_wb_10_2008_sum['Area'],
      df_wb_10_2009_sum['Area'],
      df_wb_10_2010_sum['Area'],
      df_wb_10_2011_sum['Area'],
      df_wb_10_2012_sum['Area'],
      df_wb_10_2013_sum['Area'],
      df_wb_10_2014_sum['Area'])

y22 =(df_wb_10_1997_sum['Production'],
      df_wb_10_1998_sum['Production'],
      df_wb_10_1999_sum['Production'],
      df_wb_10_2000_sum['Production'],
      df_wb_10_2001_sum['Production'], 
      df_wb_10_2002_sum['Production'],
      df_wb_10_2003_sum['Production'],
      df_wb_10_2004_sum['Production'],
      df_wb_10_2005_sum['Production'],
      df_wb_10_2006_sum['Production'],
      df_wb_10_2007_sum['Production'],
      df_wb_10_2008_sum['Production'],
      df_wb_10_2009_sum['Production'],
      df_wb_10_2010_sum['Production'],
      df_wb_10_2011_sum['Production'],
      df_wb_10_2012_sum['Production'],
      df_wb_10_2013_sum['Production'],
      df_wb_10_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [10] HOOGHLY (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [10] HOOGHLY (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [11] HOWRAH 

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_11_1997_sum['Area'],
      df_wb_11_1998_sum['Area'],
      df_wb_11_1999_sum['Area'],
      df_wb_11_2000_sum['Area'],
      df_wb_11_2001_sum['Area'], 
      df_wb_11_2002_sum['Area'],
      df_wb_11_2003_sum['Area'],
      df_wb_11_2004_sum['Area'],
      df_wb_11_2005_sum['Area'],
      df_wb_11_2006_sum['Area'],
      df_wb_11_2007_sum['Area'],
      df_wb_11_2008_sum['Area'],
      df_wb_11_2009_sum['Area'],
      df_wb_11_2010_sum['Area'],
      df_wb_11_2011_sum['Area'],
      df_wb_11_2012_sum['Area'],
      df_wb_11_2013_sum['Area'],
      df_wb_11_2014_sum['Area'])

y22 =(df_wb_11_1997_sum['Production'],
      df_wb_11_1998_sum['Production'],
      df_wb_11_1999_sum['Production'],
      df_wb_11_2000_sum['Production'],
      df_wb_11_2001_sum['Production'], 
      df_wb_11_2002_sum['Production'],
      df_wb_11_2003_sum['Production'],
      df_wb_11_2004_sum['Production'],
      df_wb_11_2005_sum['Production'],
      df_wb_11_2006_sum['Production'],
      df_wb_11_2007_sum['Production'],
      df_wb_11_2008_sum['Production'],
      df_wb_11_2009_sum['Production'],
      df_wb_11_2010_sum['Production'],
      df_wb_11_2011_sum['Production'],
      df_wb_11_2012_sum['Production'],
      df_wb_11_2013_sum['Production'],
      df_wb_11_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [11] HOWRAH (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [11] HOWRAH (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [12] JALPAIGURI

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_12_1997_sum['Area'],
      df_wb_12_1998_sum['Area'],
      df_wb_12_1999_sum['Area'],
      df_wb_12_2000_sum['Area'],
      df_wb_12_2001_sum['Area'], 
      df_wb_12_2002_sum['Area'],
      df_wb_12_2003_sum['Area'],
      df_wb_12_2004_sum['Area'],
      df_wb_12_2005_sum['Area'],
      df_wb_12_2006_sum['Area'],
      df_wb_12_2007_sum['Area'],
      df_wb_12_2008_sum['Area'],
      df_wb_12_2009_sum['Area'],
      df_wb_12_2010_sum['Area'],
      df_wb_12_2011_sum['Area'],
      df_wb_12_2012_sum['Area'],
      df_wb_12_2013_sum['Area'],
      df_wb_12_2014_sum['Area'])

y22 =(df_wb_12_1997_sum['Production'],
      df_wb_12_1998_sum['Production'],
      df_wb_12_1999_sum['Production'],
      df_wb_12_2000_sum['Production'],
      df_wb_12_2001_sum['Production'], 
      df_wb_12_2002_sum['Production'],
      df_wb_12_2003_sum['Production'],
      df_wb_12_2004_sum['Production'],
      df_wb_12_2005_sum['Production'],
      df_wb_12_2006_sum['Production'],
      df_wb_12_2007_sum['Production'],
      df_wb_12_2008_sum['Production'],
      df_wb_12_2009_sum['Production'],
      df_wb_12_2010_sum['Production'],
      df_wb_12_2011_sum['Production'],
      df_wb_12_2012_sum['Production'],
      df_wb_12_2013_sum['Production'],
      df_wb_12_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [12] JALPAIGURI (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [12] JALPAIGURI (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [13] MALDAH

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_13_1997_sum['Area'],
      df_wb_13_1998_sum['Area'],
      df_wb_13_1999_sum['Area'],
      df_wb_13_2000_sum['Area'],
      df_wb_13_2001_sum['Area'], 
      df_wb_13_2002_sum['Area'],
      df_wb_13_2003_sum['Area'],
      df_wb_13_2004_sum['Area'],
      df_wb_13_2005_sum['Area'],
      df_wb_13_2006_sum['Area'],
      df_wb_13_2007_sum['Area'],
      df_wb_13_2008_sum['Area'],
      df_wb_13_2009_sum['Area'],
      df_wb_13_2010_sum['Area'],
      df_wb_13_2011_sum['Area'],
      df_wb_13_2012_sum['Area'],
      df_wb_13_2013_sum['Area'],
      df_wb_13_2014_sum['Area'])

y22 =(df_wb_13_1997_sum['Production'],
      df_wb_13_1998_sum['Production'],
      df_wb_13_1999_sum['Production'],
      df_wb_13_2000_sum['Production'],
      df_wb_13_2001_sum['Production'], 
      df_wb_13_2002_sum['Production'],
      df_wb_13_2003_sum['Production'],
      df_wb_13_2004_sum['Production'],
      df_wb_13_2005_sum['Production'],
      df_wb_13_2006_sum['Production'],
      df_wb_13_2007_sum['Production'],
      df_wb_13_2008_sum['Production'],
      df_wb_13_2009_sum['Production'],
      df_wb_13_2010_sum['Production'],
      df_wb_13_2011_sum['Production'],
      df_wb_13_2012_sum['Production'],
      df_wb_13_2013_sum['Production'],
      df_wb_13_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [13] MALDAH (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [13] MALDAH (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [14] MEDINIPUR EAST

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_14_1997_sum['Area'],
      df_wb_14_1998_sum['Area'],
      df_wb_14_1999_sum['Area'],
      df_wb_14_2000_sum['Area'],
      df_wb_14_2001_sum['Area'], 
      df_wb_14_2002_sum['Area'],
      df_wb_14_2003_sum['Area'],
      df_wb_14_2004_sum['Area'],
      df_wb_14_2005_sum['Area'],
      df_wb_14_2006_sum['Area'],
      df_wb_14_2007_sum['Area'],
      df_wb_14_2008_sum['Area'],
      df_wb_14_2009_sum['Area'],
      df_wb_14_2010_sum['Area'],
      df_wb_14_2011_sum['Area'],
      df_wb_14_2012_sum['Area'],
      df_wb_14_2013_sum['Area'],
      df_wb_14_2014_sum['Area'])

y22 =(df_wb_14_1997_sum['Production'],
      df_wb_14_1998_sum['Production'],
      df_wb_14_1999_sum['Production'],
      df_wb_14_2000_sum['Production'],
      df_wb_14_2001_sum['Production'], 
      df_wb_14_2002_sum['Production'],
      df_wb_14_2003_sum['Production'],
      df_wb_14_2004_sum['Production'],
      df_wb_14_2005_sum['Production'],
      df_wb_14_2006_sum['Production'],
      df_wb_14_2007_sum['Production'],
      df_wb_14_2008_sum['Production'],
      df_wb_14_2009_sum['Production'],
      df_wb_14_2010_sum['Production'],
      df_wb_14_2011_sum['Production'],
      df_wb_14_2012_sum['Production'],
      df_wb_14_2013_sum['Production'],
      df_wb_14_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [14] MEDINIPUR EAST (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [14] MEDINIPUR EAST (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [15] MEDINIPUR WEST

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_15_1997_sum['Area'],
      df_wb_15_1998_sum['Area'],
      df_wb_15_1999_sum['Area'],
      df_wb_15_2000_sum['Area'],
      df_wb_15_2001_sum['Area'], 
      df_wb_15_2002_sum['Area'],
      df_wb_15_2003_sum['Area'],
      df_wb_15_2004_sum['Area'],
      df_wb_15_2005_sum['Area'],
      df_wb_15_2006_sum['Area'],
      df_wb_15_2007_sum['Area'],
      df_wb_15_2008_sum['Area'],
      df_wb_15_2009_sum['Area'],
      df_wb_15_2010_sum['Area'],
      df_wb_15_2011_sum['Area'],
      df_wb_15_2012_sum['Area'],
      df_wb_15_2013_sum['Area'],
      df_wb_15_2014_sum['Area'])

y22 =(df_wb_15_1997_sum['Production'],
      df_wb_15_1998_sum['Production'],
      df_wb_15_1999_sum['Production'],
      df_wb_15_2000_sum['Production'],
      df_wb_15_2001_sum['Production'], 
      df_wb_15_2002_sum['Production'],
      df_wb_15_2003_sum['Production'],
      df_wb_15_2004_sum['Production'],
      df_wb_15_2005_sum['Production'],
      df_wb_15_2006_sum['Production'],
      df_wb_15_2007_sum['Production'],
      df_wb_15_2008_sum['Production'],
      df_wb_15_2009_sum['Production'],
      df_wb_15_2010_sum['Production'],
      df_wb_15_2011_sum['Production'],
      df_wb_15_2012_sum['Production'],
      df_wb_15_2013_sum['Production'],
      df_wb_15_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [15] MEDINIPUR WEST (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [15] MEDINIPUR WEST (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show() 
   
# plotting  wb : [16] MURSHIDABAD

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_16_1997_sum['Area'],
      df_wb_16_1998_sum['Area'],
      df_wb_16_1999_sum['Area'],
      df_wb_16_2000_sum['Area'],
      df_wb_16_2001_sum['Area'], 
      df_wb_16_2002_sum['Area'],
      df_wb_16_2003_sum['Area'],
      df_wb_16_2004_sum['Area'],
      df_wb_16_2005_sum['Area'],
      df_wb_16_2006_sum['Area'],
      df_wb_16_2007_sum['Area'],
      df_wb_16_2008_sum['Area'],
      df_wb_16_2009_sum['Area'],
      df_wb_16_2010_sum['Area'],
      df_wb_16_2011_sum['Area'],
      df_wb_16_2012_sum['Area'],
      df_wb_16_2013_sum['Area'],
      df_wb_16_2014_sum['Area'])

y22 =(df_wb_16_1997_sum['Production'],
      df_wb_16_1998_sum['Production'],
      df_wb_16_1999_sum['Production'],
      df_wb_16_2000_sum['Production'],
      df_wb_16_2001_sum['Production'], 
      df_wb_16_2002_sum['Production'],
      df_wb_16_2003_sum['Production'],
      df_wb_16_2004_sum['Production'],
      df_wb_16_2005_sum['Production'],
      df_wb_16_2006_sum['Production'],
      df_wb_16_2007_sum['Production'],
      df_wb_16_2008_sum['Production'],
      df_wb_16_2009_sum['Production'],
      df_wb_16_2010_sum['Production'],
      df_wb_16_2011_sum['Production'],
      df_wb_16_2012_sum['Production'],
      df_wb_16_2013_sum['Production'],
      df_wb_16_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [16] MURSHIDABAD (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [16] MURSHIDABAD (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [17] NADIA

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_17_1997_sum['Area'],
      df_wb_17_1998_sum['Area'],
      df_wb_17_1999_sum['Area'],
      df_wb_17_2000_sum['Area'],
      df_wb_17_2001_sum['Area'], 
      df_wb_17_2002_sum['Area'],
      df_wb_17_2003_sum['Area'],
      df_wb_17_2004_sum['Area'],
      df_wb_17_2005_sum['Area'],
      df_wb_17_2006_sum['Area'],
      df_wb_17_2007_sum['Area'],
      df_wb_17_2008_sum['Area'],
      df_wb_17_2009_sum['Area'],
      df_wb_17_2010_sum['Area'],
      df_wb_17_2011_sum['Area'],
      df_wb_17_2012_sum['Area'],
      df_wb_17_2013_sum['Area'],
      df_wb_17_2014_sum['Area'])

y22 =(df_wb_17_1997_sum['Production'],
      df_wb_17_1998_sum['Production'],
      df_wb_17_1999_sum['Production'],
      df_wb_17_2000_sum['Production'],
      df_wb_17_2001_sum['Production'], 
      df_wb_17_2002_sum['Production'],
      df_wb_17_2003_sum['Production'],
      df_wb_17_2004_sum['Production'],
      df_wb_17_2005_sum['Production'],
      df_wb_17_2006_sum['Production'],
      df_wb_17_2007_sum['Production'],
      df_wb_17_2008_sum['Production'],
      df_wb_17_2009_sum['Production'],
      df_wb_17_2010_sum['Production'],
      df_wb_17_2011_sum['Production'],
      df_wb_17_2012_sum['Production'],
      df_wb_17_2013_sum['Production'],
      df_wb_17_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [17] NADIA (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [17] NADIA (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()

# plotting  wb : [18] PURULIA  

x1 = ('1997','1998','1999','2000','2001','2002','2003','2004','2005',
     '2006','2007','2008','2009','2010','2011','2012','2013','2014')

y11 =(df_wb_18_1997_sum['Area'],
      df_wb_18_1998_sum['Area'],
      df_wb_18_1999_sum['Area'],
      df_wb_18_2000_sum['Area'],
      df_wb_18_2001_sum['Area'], 
      df_wb_18_2002_sum['Area'],
      df_wb_18_2003_sum['Area'],
      df_wb_18_2004_sum['Area'],
      df_wb_18_2005_sum['Area'],
      df_wb_18_2006_sum['Area'],
      df_wb_18_2007_sum['Area'],
      df_wb_18_2008_sum['Area'],
      df_wb_18_2009_sum['Area'],
      df_wb_18_2010_sum['Area'],
      df_wb_18_2011_sum['Area'],
      df_wb_18_2012_sum['Area'],
      df_wb_18_2013_sum['Area'],
      df_wb_18_2014_sum['Area'])

y22 =(df_wb_18_1997_sum['Production'],
      df_wb_18_1998_sum['Production'],
      df_wb_18_1999_sum['Production'],
      df_wb_18_2000_sum['Production'],
      df_wb_18_2001_sum['Production'], 
      df_wb_18_2002_sum['Production'],
      df_wb_18_2003_sum['Production'],
      df_wb_18_2004_sum['Production'],
      df_wb_18_2005_sum['Production'],
      df_wb_18_2006_sum['Production'],
      df_wb_18_2007_sum['Production'],
      df_wb_18_2008_sum['Production'],
      df_wb_18_2009_sum['Production'],
      df_wb_18_2010_sum['Production'],
      df_wb_18_2011_sum['Production'],
      df_wb_18_2012_sum['Production'],
      df_wb_18_2013_sum['Production'],
      df_wb_18_2014_sum['Production'])                                      

plt.subplot(121)
plt.title('State-5 : wb : [18] PURULIA (Area) :')
plt.xlabel('year -->')
plt.ylabel('area -->')                                                                      
plt.plot(x1,y11)
plt.show

plt.subplot(122)
plt.title('State-5 : wb : [18] PURULIA (Production) :')
plt.xlabel('year -->')
plt.ylabel('production -->')
plt.plot(x1,y22)
plt.show()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
