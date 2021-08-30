# Task_1
import os


my_start = ['my_project', 'settings', 'mainapp', 'adminapp', 'authapp']
if os.path.isdir(my_start[0]) == False:
    os.mkdir(my_start[0])
    os.chdir(my_start[0])
    for dir_start in my_start[1:]:
        os.mkdir(dir_start)
    print('folders created')
else:
    print(f'a folder with name: {my_start[0]} alredy exist')