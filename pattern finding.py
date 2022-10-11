#!/usr/bin/env python
# coding: utf-8

# In[19]:


def multiplyList (myList):
    result = 1
    for x in myList:
        result = result * x
    return result


# In[21]:


input_list = list(input())
input_list = list(map(int,input_list))
output_list = []
n = len(input_list)
i =0
while i < n:
    removed_element = input_list[0]
    input_list.remove(input_list[0])
    output_list.append(multiplyList(input_list))
    input_list.append(removed_element)
    i +=1
print(output_list)
print(input_list)
    
    


# In[ ]:





# In[ ]:





# In[ ]:




