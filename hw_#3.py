# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 17:50:05 2022

@author: LocalAdmin
"""
import os

adrr = os.getcwd()
files = os.listdir(os.chdir(f'{adrr}\sorted'))
result_file_name = 'result_file.txt'


def amount_lines(files, result_file_name):
    count_dict = {}
    for i in files:
        if i != result_file_name:
            count = 0
            with open(i, 'r', encoding='utf-8') as f:
                for line in f:
                    count += 1
                count_dict[i] = count
    return count_dict

def result_file(files_per_lines, result_file_name):
    sorted_values = sorted(list(files_per_lines.values()))
    res_file = open(result_file_name, 'w', encoding='utf-8')
    for i in sorted_values:
        for file, len_file in files_per_lines.items():
            if len_file == i:
                res_file.write(file + '\n')
                res_file.write(str(len_file) + '\n')
                with open(file, 'r', encoding='utf-8') as f:
                    for line in f:
                        res_file.write(line + '\n')
    return res_file
                        

files_per_lines = amount_lines(files, result_file_name)
result_file(files_per_lines, result_file_name)





    
