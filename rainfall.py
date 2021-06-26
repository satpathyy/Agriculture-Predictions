# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_csv ('/home/jeet/Desktop/Rainfall_data.csv',encoding="cp1252")

print("\n------- output data :-----------\n")
print("Rainfall Data Analysis (1901 to 2017):")
print("\n-----------------------------------\n")

# Question – A : get row and column numbers 

print("Dimension of the data frame = ",df.shape)

# Question – B : print column names :

print('--------------------------------------------\n')
print('Column names as follows :\n')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

#--- Main operation ------

sub_div_name = df.groupby(['SUBDIVISION'])[['YEAR']].count()

print("---------------------------------")
print("\t Subdivisions : ")
print("-------------------------------")
print(sub_div_name)
print("-------------------------------")
count = 0
for row in range(len(sub_div_name)):
              count = count+1

print("total no. of subdivisions = ",count)        
print("-----------------------------\n")


 
# [01] Andaman & Nicobar Islands
# [02] Arunachal Pradesh 
# [03] Assam & Meghalaya 
# [04] Bihar                         
# [05] Chhattisgarh
                     
plt.title('[ Set - 1 ] Rainfall in India ( 1901 - 2017) : ')
plt.xlabel("year--- >")
plt.ylabel("growth --- >")
    
df_andaman = df[df.SUBDIVISION == 'Andaman & Nicobar Islands']
plt.plot(df_andaman['YEAR'],df_andaman['ANNUAL'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[1] Andaman & Nicobar Islands ")
 
df_arunachal = df[df.SUBDIVISION == 'Arunachal Pradesh']                       
plt.plot(df_arunachal['YEAR'],df_arunachal['ANNUAL'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[2] Arunachal Pradesh")
            
df_assam = df[df.SUBDIVISION == 'Assam & Meghalaya']
plt.plot(df_assam['YEAR'],df_assam['ANNUAL'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[3] Assam & Meghalaya")

df_bihar = df[df.SUBDIVISION == 'Bihar']
plt.plot(df_bihar['YEAR'],df_bihar['ANNUAL'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[4] Bihar")

df_chattishgarh = df[df.SUBDIVISION == 'Chhattisgarh']
plt.plot(df_chattishgarh['YEAR'],df_chattishgarh['ANNUAL'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[5] Chattishgarh")

plt.legend()
plt.show()


# [06] Coastal Andhra Pradesh               117
# [07] Coastal Karnataka                    117
# [08] East Madhya Pradesh                  117
# [09] East Rajasthan                       117
# [10] East Uttar Pradesh                   117

plt.title('[ Set - 2 ] Rainfall in India ( 1901 - 2017) : ')
plt.xlabel("year --- >")
plt.ylabel("growth --- >")
    
df_andhra = df[df.SUBDIVISION == 'Coastal Andhra Pradesh']
plt.plot(df_andhra['YEAR'],df_andhra['ANNUAL'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[6] Coastal Andhra Pradesh ")
 
df_karnataka = df[df.SUBDIVISION == 'Coastal Karnataka']                       
plt.plot(df_karnataka['YEAR'],df_karnataka['ANNUAL'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[7] Coastal Karnataka")
            
df_e_Madhya = df[df.SUBDIVISION == 'East Madhya Pradesh']
plt.plot(df_e_Madhya['YEAR'],df_e_Madhya['ANNUAL'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[8] East Madhya Pradesh")

df_e_Raj = df[df.SUBDIVISION == 'East Rajasthan']
plt.plot(df_e_Raj['YEAR'],df_e_Raj['ANNUAL'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[9] East Rajasthan")

df_e_UP = df[df.SUBDIVISION == 'East Uttar Pradesh']
plt.plot(df_e_UP['YEAR'],df_e_UP['ANNUAL'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[10] East Uttar Pradesh")

plt.legend()
plt.show()

# [11] Gangetic West Bengal                 117
# [12] Gujarat Region                       117
# [13] Haryana Delhi & Chandigarh           117
# [14] Himachal Pradesh                     117
# [15] Jammu & Kashmir                      117

plt.title('[ Set - 3 ] Rainfall in India ( 1901 - 2017) : ')
plt.xlabel("year --- >")
plt.ylabel("growth --- >")
    
df_gwb = df[df.SUBDIVISION == 'Gangetic West Bengal']
plt.plot(df_gwb['YEAR'],df_gwb['ANNUAL'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[11] Gangetic West Bengal ")
 
df_gr = df[df.SUBDIVISION == 'Gujarat Region']                       
plt.plot(df_gr['YEAR'],df_gr['ANNUAL'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[12] Gujarat Region")
            
df_hdc = df[df.SUBDIVISION == 'Haryana Delhi & Chandigarh']
plt.plot(df_hdc['YEAR'],df_hdc['ANNUAL'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[13] Haryana Delhi & Chandigarh")

df_hp = df[df.SUBDIVISION == 'Himachal Pradesh ']
plt.plot(df_hp['YEAR'],df_hp['ANNUAL'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[14] Himachal Pradesh")

df_jk = df[df.SUBDIVISION == 'Jammu & Kashmir']
plt.plot(df_jk['YEAR'],df_jk['ANNUAL'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[15] Jammu & Kashmir")

plt.legend()
plt.show()

# [16] Jharkhand                            117
# [17] Kerala                               117
# [18] Konkan & Goa                         117
# [19] Lakshadweep                          116
# [20] Madhya Maharashtra                   117

plt.title('[ Set - 4 ] Rainfall in India ( 1901 - 2017) : ')
plt.xlabel("year --- >")
plt.ylabel("growth --- >")
    
df_jhar = df[df.SUBDIVISION == 'Jharkhand']
plt.plot(df_jhar['YEAR'],df_jhar['ANNUAL'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[16] Jharkhand ")
 
df_kerala = df[df.SUBDIVISION == 'Kerala']                       
plt.plot(df_kerala['YEAR'],df_kerala['ANNUAL'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[17] Kerala ")
            
df_kg = df[df.SUBDIVISION == 'Konkan & Goa']
plt.plot(df_kg['YEAR'],df_kg['ANNUAL'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[18] Konkan & Goa ")

df_lak = df[df.SUBDIVISION == 'Lakshadweep']
plt.plot(df_lak['YEAR'],df_lak['ANNUAL'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[19] Lakshadweep")

df_mam = df[df.SUBDIVISION == 'Madhya Maharashtra']
plt.plot(df_mam['YEAR'],df_mam['ANNUAL'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[20] Madhya Maharashtra")

plt.legend()
plt.show()

# [21] Matathwada                           117
# [22] Naga Mani Mizo Tripura               117
# [23] North Interior Karnataka             117
# [24] Orissa                               117
# [25] Punjab                               117

plt.title('[ Set - 5 ] Rainfall in India ( 1901 - 2017) : ')
plt.xlabel("year --- >")
plt.ylabel("growth --- >")
    
df_mat = df[df.SUBDIVISION == 'Matathwada']
plt.plot(df_mat['YEAR'],df_mat['ANNUAL'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[21] Matathwada ")
 
df_naga = df[df.SUBDIVISION == 'Naga Mani Mizo Tripura']                       
plt.plot(df_naga['YEAR'],df_naga['ANNUAL'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[22] Naga Mani Mizo Tripura ")
            
df_nik = df[df.SUBDIVISION == 'North Interior Karnataka']
plt.plot(df_nik['YEAR'],df_nik['ANNUAL'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[23] North Interior Karnataka")

df_ori = df[df.SUBDIVISION == 'Orissa']
plt.plot(df_ori['YEAR'],df_ori['ANNUAL'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[24] Orissa")

df_pun = df[df.SUBDIVISION == 'Punjab']
plt.plot(df_pun['YEAR'],df_pun['ANNUAL'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[25] Punjab ")

plt.legend()
plt.show()

# [26] Rayalseema                           117
# [27] Saurashtra & Kutch                   117
# [28] South Interior Karnataka             117
# [29] Sub Himalayan West Bengal & Sikkim   117
# [30] Tamil Nadu                           117

plt.title('[ Set - 6 ] Rainfall in India ( 1901 - 2017) : ')
plt.xlabel("year --- >")
plt.ylabel("growth --- >")
    
df_raya = df[df.SUBDIVISION == 'Rayalseema']
plt.plot(df_raya['YEAR'],df_raya['ANNUAL'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[26] Rayalseema ")
 
df_sk = df[df.SUBDIVISION == 'Saurashtra & Kutch']                       
plt.plot(df_sk['YEAR'],df_sk['ANNUAL'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[27] Saurashtra & Kutch ")
            
df_sik = df[df.SUBDIVISION == 'South Interior Karnataka']
plt.plot(df_sik['YEAR'],df_sik['ANNUAL'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[28] South Interior Karnataka")

df_shwb = df[df.SUBDIVISION == 'Sub Himalayan West Bengal & Sikkim']
plt.plot(df_shwb['YEAR'],df_shwb['ANNUAL'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[29] Sub Himalayan West Bengal & Sikkim")

df_tn = df[df.SUBDIVISION == 'Tamil Nadu']
plt.plot(df_tn['YEAR'],df_tn['ANNUAL'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[30] Tamil Nadu ")

plt.legend()
plt.show()

# [31] Telangana                            117
# [32] Uttarakhand                          117
# [33] Vidarbha                             117
# [34] West Madhya Pradesh                  117
# [35] West Rajasthan                       117
# [36] West Uttar Pradesh                   117

plt.title('[ Set - 7 ] Rainfall in India ( 1901 - 2017) : ')
plt.xlabel("year --- >")
plt.ylabel("growth --- >")
    
df_tel = df[df.SUBDIVISION == 'Telangana']
plt.plot(df_tel['YEAR'],df_tel['ANNUAL'],
            marker=7,
            markersize=10,
            linestyle='dashed',
            label="[31] Telangana")
 
df_utt = df[df.SUBDIVISION == 'Uttarakhand']                       
plt.plot(df_utt['YEAR'],df_utt['ANNUAL'],
            marker='*',
            markersize=10,
            linestyle='dashed',
            label="[32] Uttarakhand")
            
df_vid = df[df.SUBDIVISION == 'Vidarbha']
plt.plot(df_vid['YEAR'],df_vid['ANNUAL'],
            marker='+',
            markersize=10,
            linestyle='dashed',
            label="[33] Vidarbha ")

df_wmp = df[df.SUBDIVISION == 'West Madhya Pradesh']
plt.plot(df_wmp['YEAR'],df_wmp['ANNUAL'],
            marker='X',
            markersize=10,
            linestyle='dashed',
            label="[34] West Madhya Pradesh")

df_wr = df[df.SUBDIVISION == 'West Rajasthan']
plt.plot(df_wr['YEAR'],df_wr['ANNUAL'],
            marker="o",
            markersize=10,
            linestyle='dashed',
            label="[35] West Rajasthan")
 
df_wup = df[df.SUBDIVISION == 'West Uttar Pradesh']                       
plt.plot(df_wup['YEAR'],df_wup['ANNUAL'],
            marker=4,
            markersize=10,
            linestyle='dashed',
            label="[36]West Uttar Pradesh")            

plt.legend()
plt.show()