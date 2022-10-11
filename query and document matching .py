#!/usr/bin/env python
# coding: utf-8

# In[24]:


ingredients = ['Ambrette Seed','Apple Cinnamon Granola','Arizona Seasoning','Americano Coffee','Baby Abalone','Cadbury Double Decker Chocolate Bar''Campari Tomato','Celery Soup','Chia Meal','Crunch Bars','Cardamom','Giardiniera','Hog Maw','Mccormick Montreal Steak Seasoning','Muesli','Mulberry','Munch Chocolate','Murukku Packet','Mango','Organic Maize','Organic Peruvian Groundcherry','Organic Tartar Cream','Orange Extract','Pickled Cauliflower','Pork Chump Chops','Pork Lungs','Pork Tripe','Peanut Butter','Smokies Sausage','Snickers Spread','Strawberry Gelatin','Salmon','Tomato','Tamarind','Vegan Carob Chips','Vegan Chicken Strips','Vegan Chorizo','Vegan Marshmallow','Vegan Puff Pastry Sheet','Vegan Semisweet Chocolate Chips','Vegan White Cake','Vegetable Stock','Vinegar']
zeros =[0] * len(ingredients) 
dict_ingredients = dict(zip(ingredients,zeros))
article = open('article.txt',"r")
data = article.read()
data_into_list = data.replace('\n',' ').split(' ')
for i in range(0,len(data_into_list)):
    if data_into_list[i] in dict_ingredients.keys():
        dict_ingredients['data_into_list[i]'] = dict_ingredints['data_into_list[i]'] +1
dict_ingredients_f = sorted(dict_ingredients)
print(dict_ingredients_f)


# In[ ]:




