#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import json
data=pd.read_json(r"C:\Users\0017TS744\Desktop\DS\details.json")

result=data[data["Key Skills"].str.contains("Python")]
print(len(result))
# Filter python objects with list comprehensions


# Transform python object back into json


# Show json

             


# In[30]:


import pandas as pd
import json
data=pd.read_json(r"C:\Users\0017TS744\Desktop\DS\details.json")

result=data[data["Location"].str.contains("Seattle")]
print(len(result))
# Filter python objects with list comprehensions


# Transform python object back into json


# Show json

             

