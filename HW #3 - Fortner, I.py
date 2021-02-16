#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 0: Define a dictionary, composed with students name and their grade. marks = {‘Andy’:88, ‘Amy’:66, 'James': 90, 'Jules': 55, 'Arthur': 77}
#Question 1: Using for loop, print out all the students name and their grade.
#Question 2: Of this dictionary, calculate all the student’s mean grade, maximal grade, and minimal grade.
#Question 3: Using for loop or while loop, for all the keys in the dictionary, print out key. However, if ‘J’ appears, stop the loop.
#Question 4: Using for loop or while loop, for all the keys in the dictionary, print out key. However, if ‘J’ appears, skip this key, and continue the loop.
#Question 5: Define a function, when call the function, only need to pass student’s name, your function will return this student’s grade. If the student name does not exit, print you cannot find this student’s name.


# In[3]:


name_grade = {
"Andy":"88",
"Amy":"66",
"James": "90",
"Jules":"55",
"Arthur":"77"}


# In[4]:


print(name_grade)


# In[5]:


for name, grade in name_grade. items():
    print(name, "recieved a", grade)


# In[6]:


grade_book = {            
    'Andy': [88], 
    'Amy': [66],
    'James': [90],  
    'Jules': [55],
    'Arthur': [77]}


# In[7]:


minimum= (min(88,66,90,55,77))


# In[8]:


maximum= (max(88,66,90,55,77))


# In[9]:


all_grades_total = 0
all_grades_count = 0

for name, grades in grade_book.items():
    total = sum(grades)
    print(f'Average for {name} is {total/len(grades):.2f}')
    all_grades_total += total
    all_grades_count += len(grades)
    
print(f"Class's average is: {all_grades_total / all_grades_count:.2f}")
print("Class's minimum is:",minimum)
print("Class's maximum is:",maximum)


# In[10]:


#Question 3: Using for loop or while loop, for all the keys in the dictionary, 
#print out key. However, if ‘J’ appears, stop the loop.


# In[23]:


for name in name_grade:
    if 'J' in name:
        break
    print(name)


# In[12]:


#Question 4: Using for loop or while loop, for all the keys in the dictionary, 
#print out key. However, if ‘J’ appears, 
#skip this key, and continue the loop.


# In[22]:


for name in name_grade:
    if 'J' in name:
        continue
    print(name)


# In[58]:


#Question 5: Define a function, when call the function, only need to pass 
#student’s name, your function will return this student’s grade. If the 
#student name does not exit, print you cannot find this student’s name.


# In[24]:


def print_student(student_name):
    marks= {
"Andy":"88",
"Amy":"66",
"James": "90",
"Jules":"55",
"Arthur":"77"}
    for student in marks:
        if student==student_name:
            print(marks[student])
            break
    else:
        print("Cannot find this student's name")
print_student("Amy")
print_student("Ivy")
print_student("James")

