#!/usr/bin/env python3
"""
简单的 Hello World 程序
用于演示 Cloud Build + SonarCloud 集成
"""

import os
import subprocess

def hello_world():
    """返回 Hello World 消息"""
    return "Hello, World!"

def vulnerable_function(user_input):
    """故意添加的安全漏洞函数"""
    # 安全问题1: SQL注入风险
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"
    
    # 安全问题2: 命令注入风险
    os.system("echo " + user_input)
    
    # 安全问题3: 使用eval()执行用户输入
    result = eval(user_input)
    
    return query, result

def code_quality_issues():
    """故意添加的代码质量问题"""
    # 问题1: 未使用的变量
    unused_variable = "This is never used"
    
    # 问题2: 重复的代码
    if True:
        print("Duplicate code block 1")
        print("This is duplicated")
        print("More duplicate content")
    
    if False:
        print("Duplicate code block 2") 
        print("This is duplicated")
        print("More duplicate content")
    
    # 问题3: 复杂的函数（高圈复杂度）
    x = 10
    if x > 5:
        if x > 8:
            if x > 9:
                if x == 10:
                    print("Too many nested ifs")

def main():
    """主函数"""
    message = hello_world()
    print(message)
    
    # 调用有问题的函数
    vulnerable_function("'; DROP TABLE users; --")
    code_quality_issues()
    
    # 硬编码的密码
    password = "admin123"
    api_key = "sk-1234567890abcdef"
    
    return 0

if __name__ == "__main__":
    main()