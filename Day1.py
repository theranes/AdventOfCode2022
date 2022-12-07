#!/usr/bin/env python
# coding: utf-8

# In[150]:


from pathlib import Path
txt = Path('Input/day1.txt').read_text()
list_text=txt.split('\n\n')
list_text=[item.split('\n') for item in list_text]
list_num=[[int(float(item)) for item in line] for line in list_text]
list_sums=[sum(line) for line in list_num]
result=max(list_sums)
print('The elf carring the most calories is carrying '+str(result)+' calories')


# In[ ]:




