#!/usr/bin/env python3
"""
简单的 Hello World 程序
用于演示 Cloud Build + SonarCloud 集成
"""

def hello_world():
    """返回 Hello World 消息"""
    return "Hello, World!"

def main():
    """主函数"""
    message = hello_world()
    print(message)
    return 0

if __name__ == "__main__":
    main()