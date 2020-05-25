#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ragib
#
# Created:     25/05/2020
# Copyright:   (c) ragib 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
s="My name is Ragib. I am a data science student at Cradiff University"
s1=s.split()
name= "Ragib"
for i in s1:
    if i==name:
        print("Name in string")
    continue