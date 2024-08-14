import sys

def func1():
    print("Function 1 is executed")

def func2():
    print("Function 2 is executed")

def main():
    args = sys.argv[1:]  # 第一个参数是脚本名称，实际参数从sys.argv[1:]开始
    print("Received arguments:", args)
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'func1':
            func1()
        elif command == 'func2':
            func2()
        else:
            print("Unknown command")
    else:
        print("No command provided")

if __name__ == "__main__":
    main()