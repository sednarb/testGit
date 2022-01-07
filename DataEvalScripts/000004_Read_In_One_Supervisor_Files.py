#!/usr/bin/env python
# coding: utf-8

#000004_Read_In_One_Supervisor_Files.py
#Script Purpose: Read in a Data File with 25 Repetition and create an overview plot that is saved as graphic and generate a csv export
#of the test summary
#Creator: Lucy Ruediger, 05 Nov 2021 
#Last changed: 05 Nov 2021, 16:41:00

# In[00]:

#Locate Data to be evaluated

import os
path = "C:\00RepositoryGIT\testtools\DataEvalPanda"
print(path)
#os.chdir(path)

# Check current working directory.
retval = os.getcwd()
print ("Current working directory %s" % retval)

import random
import pandas as pd

def read_header_and_data(file_name):
    delim = ";"
    d = {}
    
    with open(file_name, "r") as fobj:
        for line in fobj:
            # consider line-endings ???
            line = line.strip()
            if line.startswith("#"):
                if line == "#DATA":
                    break            
                continue
            line_parts = line.split(delim)
            k = line_parts[0]
            v = None
            if len(line_parts) > 1:
                v = line_parts[1]
            d[k] = v
        data = pd.read_csv(fobj,sep=";",skipinitialspace=True,parse_dates=[1,2])

    return d, data
    
irand = random.randint(0,1)
#print(irand)
f= open(r"Output\Result.txt","w+")
if irand == 0:
    f.write("Passed")
if irand == 1:
    f.write("failed")
f.close()


# In[00]:

header_1, data_1 = read_header_and_data(r"Input\1\ISO_10360-5_2020-EDITION_SINGLES_SAMPLE_210504_1005.TXT")
#header_2, data_2 = read_header_and_data(r"ISO_10360-5_2020-EDITION_SPHERE_SCAN_THP_SAMPLE_210419_1245.TXT")

# In[00]:
# Only needed if more than one data sets are evaluated

#for k1,v1 in header_1.items():
#    v2 = header_2[k1]
#    if not (v1 == v2):
#        print(f"Key: {k1}, Value 1: {v1} - Value 2: {v2}")


# In[00]:
    
#Summary of descriptive statistics"

#Statistical summary of all columns
stat_summary_data1= data_1.describe()
stat_summary_data1.to_csv('Output\Data1_Summary_Stat_Everything.CSV')

#Extraction of the form error column
stat_summary_data1_Form= data_1['FORM.ERR'].describe()
stat_summary_data1_Form.to_csv('Output\Data1_Summary_Stat_Form_Error_Only.CSV')

# In[23]:
    
#Preparation for the graphical ouput
    
import matplotlib.pyplot as plt
#import seaborn as sns

#data_1['FORM.ERR'].plot()

ax1 = plt.subplot(131)
ax1.plot(data_1['FORM.ERR'])

str1 = 'Form Error'
str2 = 'Machine Serial #'
str3 = header_1['CMM_SN']
str4 = header_1['DATE']
str5 = header_1['TIME']

res1 = f'{str1} \n'
res2 = f'{str2} {str3} \n {str4} {str5}'
#res2 = f'{str2} {str3}'
#print("Appending multiple strings using f-string:\n")
#print(res)

ax1.set_title(res1)

#ax1.set_title("Form Error [μm]")
ax1.set_xlabel("Sample Nr.")
ax1.set_ylabel("[μm]")

#ax1.margins(0.05)           # Default margin is 0.05, value 0 means fit
#ax1.plot(t1, f(t1))

# In[24]:
#form_err_fig, axs = plt.subplots(ncols = 2, figsize=(13, 4))  

ax2 = plt.subplot(132)
ax2.set_title(res2)
ax2.boxplot(data_1['FORM.ERR'])

#sns.boxplot(y=data_1['FORM.ERR'], ax=axs[0])
#sns.boxplot(y=data_2['FORM.ERR'], ax=axs[1]) #            ,showfliers=False)

ax3=plt.subplot(133)
ax3.axis('off')

#Generate a dataframe for plotting the rounded boxplot values, only needed for generating a graphic
df = stat_summary_data1_Form.to_frame()
dfr = df.round(3)

# In[26]:
#ax3.table(cellText=df.describe(), colLabels=df.columns, rowLabels=index)

ax3.table(cellText=dfr.values,colLabels=["FORM.ERR"],rowLabels=["count","mean","std","min","25%","50%","75%","max"],loc="center",colWidths=[0.5, 0.5])

#plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.tight_layout()

plt.savefig('Output\ISO_10360-5_2020 Single Samples.png')

# In[27]:
    
#Playgound of data import
#data_1.head()

# In[27]:
#data_1.columns

# In[28]:
#data_1.DATE

# In[29]:
data_1.dtypes

# In[30]:

colnames=['Key', 'Value'] 
#user1 = pd.read_csv('dataset/1.csv', names=colnames, header=None)

dfb = pd.read_csv(
    filepath_or_buffer=r"Input\1\ISO_10360-5_2020-EDITION_SINGLES_SAMPLE_210504_1005.TXT",names=colnames,
    sep=";",
    nrows=84,
    comment='#',
    index_col=0
)

# In[31]:
dfb.head()

# In[32]:
dfb.loc['PRG_VERSION']


# In[ ]:




