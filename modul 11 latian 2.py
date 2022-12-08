# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 21:52:15 2022

@author: fariz
"""

class mhs:
    def __init__(self, nama='none', nilai='none'):
        self.nama = nama
        self.nilai= nilai  
    def Displaymhs(self):
        print('the name is',self.nama)
        print('the grade is',self.nilai)
    @property
    def fname(self):
        print('Getting name')
        return self.nama
        return self.nilai        
    @fname.setter
    def cnama(self, value):
        print('data changed to ' + value)
        self.nama = value
    def cnilai(self, value):
        print('data changed to ' + value)
        self.nilai = value
    @fname.deleter
    def fname(self):
        print('Deleting fname')
        del self.nama
        del self.nilai
i=0
name='none'
grade='none'
while i==0:
    print('==== Program ====')
    print('''1. Mendeklarasikan Objek
2. Menampilkan Objek
3. Merubah Nilai Objek
4. Menghapus Objek
5. Keluar Dari Program
===============''')
    rsp1=int(input('Masukan Pilihan Berupa Angka(1/2/3/4/5): '))

    if rsp1==1:
        name=input('Masukan Namamu: ')
        grade=input('Masukan Nilaimu: ')
        std = mhs(name , grade)
    elif rsp1==2:
        std = mhs(name , grade)
        print()
        std.Displaymhs()
        print()
    elif rsp1==3:
        std = mhs(name , grade)
        o=0
        while o==0:
            rsp2=input('apa yang ingin di rubah?[nama/nilai]: ')
            if rsp2.lower()=='nama':
                name=input('Masukan Namamu: ')
                std.cnama=name
                o=1
            elif rsp2.lower()=='nilai':
                grade=input('Masukan Nilaimu: ')
                std.cnilai=grade
                o=1
            else:
                print('Invalid Input!')
    elif rsp1==4:
        std = mhs(name , grade)
        del std.fname
        name='none'
        grade='none'
    elif rsp1==5:
        i=1
    else:
        print("Invalid Input")