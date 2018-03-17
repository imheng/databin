#-*- coding:UTF-8 -*-
'''本文件用于将原始图片中的车牌图片统一放入Only_car_Folder文件夹'''
import os
import pandas as pd
import sys
import xlrd
import shutil

pic_dir = 'E:\\考务与学分管理\\四六级\\2017-2018第二学期\\2017照片信息各班'
pic_des = 'E:\\考务与学分管理\\四六级\\2017-2018第二学期\\2017'

roll=pd.read_excel("2017级学生学籍信息.xlsx")

def ext_comp(file):
    (filepath,tempfilename) = os.path.split(file)
    (shotname,extension) = os.path.splitext(tempfilename)
    #print(extension)
    if str.lower(extension) !='.jpg':
        return True
def do_copy(file):
    (filepath,tempfilename) = os.path.split(file)
    (shotname,extension) = os.path.splitext(tempfilename)
    print(filepath)

def bianli(rootDir):
    for root,dirs,files in os.walk(rootDir):
        for file in files:
            if not ext_comp(os.path.join(root,file)):
                #do_copy(os.path.join(root,file))
                #print(file)
                (filepath,tempfilename) = os.path.split(file)
                (shotname,extension) = os.path.splitext(tempfilename)
                s = roll.loc[roll['学号']==shotname,['身份证号']]
                shutil.copyfile(os.path.join(root,file),os.path.join(pic_des,s.iloc[0].values[0]+extension))
                print('copying...',shotname)
            
        for dir in dirs:
            bianli(dir)

bianli(pic_dir)
