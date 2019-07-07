"""
  Created by Amor on 2018-10-12
  将ipynb的文件转换成md文件的脚本
"""
import os
import subprocess

__author__ = '骆杨'


def make_to_md(f):
    subprocess.run(['jupyter', 'nbconvert', '--to', 'markdown', f])


def get_ipynb():
    ipynb_list = []
    _file_list = os.walk('./')
    _file_list = next(_file_list)
    for item in _file_list[2]:
        _file = item.split('.')
        if _file[1] == 'ipynb':
            ipynb_list.append(item)
    return ipynb_list


if __name__ == '__main__':
    file_list = get_ipynb()
    for file in file_list:
        make_to_md(file)
