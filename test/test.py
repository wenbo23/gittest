import sys
import os

# 将第一个gittest目录添加到sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# 导入第二个gittest目录下的hi模块
import gittest.hi as ghi


ghi.my_hi()