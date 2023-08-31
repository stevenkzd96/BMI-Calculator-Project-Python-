#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator
# 
# https://www.calculator.net/bmi-calculator.html

# In[31]:


name = input("Enter your name: ")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

BMI = weight / (height * height)

print(BMI)

if BMI > 0:
    if BMI <= 18.5:
        print(name + ", you are underweight.")
    elif BMI <= 25:
        print(name + ", you are normal weight.")
    elif BMI <= 30:
        print(name + ", you are overweight.")
    elif BMI <= 35:
        print(name + ", you are obese.")
    elif BMI <= 40:
        print(name + ", you are severely obese.")
    else:
        print(name + ", you are morbidly obese.")
else:
    print("Enter valid input.")


# In[9]:


BMI = (weight) / (height * height)


# In[ ]:


#BMI = (weight in Kg) / (height in m x height in m)


# In[ ]:


print(weight)


# In[ ]:


Under 16	Underweight	Minimal
18.5 - 25	Normal Weight	Minimal
25 - 30 	Overweight	Increased
30 - 35 	Obese	High
35 - 40 	Severely Obese	Very High
40 and over 	Morbidly Obese	Extremely High


# In[38]:


if BMI > 0:
    if BMI < 16:
        print(name + ", you are underweight.")
    elif BMI < 25:
        print(name + ", you are normal weight.")
    elif BMI < 30:
        print(name + ", you are overweight.")
    elif BMI < 35:
        print(name + ", you are obese.")
    elif BMI < 40:
        print(name + ", you are severely obese.")
    else:
        print(name + ", you are morbidly obese.")
else:
    print("Enter valid input.")


# In[ ]:





# In[ ]:





# In[ ]:





# # My Own

# In[2]:


weight = input("Enter your weight in Kilograms:")



# In[3]:


print(weight)


# In[18]:


#BMI = (weight in pounds x 703) / (height in inches x height in inches)


# In[21]:


73.5/(1.76*1.76)


# In[ ]:




