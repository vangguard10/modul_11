# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:13:06 2022

@author: fariz
"""


class student:
    stdCount = 0
    
    def __init__(self, name, nim, akt):
        self.name=name
        self.nim=nim
        self.akt=akt
        student.stdCount+=1
        
    def displayStudent(self):
        print(f'''
Nama: {self.name}
NIM: {self.nim}
Angkatan: {self.akt}
''')

name=input('Nama: ')
nim=input('NIM: ')
akt=input('Angkatan: ')

std=student(name, nim, akt)
std.displayStudent()
print("total student: %d" % student.stdCount)