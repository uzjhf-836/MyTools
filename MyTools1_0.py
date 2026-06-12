#The Ver = 1.0
#By 一只屑system32
#(uzjhf-836,Zuowan)
import random
class 没有Error(Exception):
    pass

if __name__ == "__main__":
    print('呃,这里好像不提供主程序运行服务......')
    if input("不过你要测试吗?"):
        pass
    else:
        raise 没有Error
def Right_To_Left(text):
    text = str(text)
    a=''
    for i in text[::-1]:
        a+=i
    return a

def Right_To_Left_Old(text):
    text = str(text)
    a=""
    for i in range(len(text)):
        a+=text[len(text)-(i+1)]

def Base10(Hex:str,Base:int) -> None:
    try:
        return (int(str(Hex),int(Base)))
    except Exception as e:
        print(e)

def Egg ():
    try:
        while True:
            print("Egg!")
    except:
        Egg()

def Random_16Hex(num,Not_Zero=True):
    HexNum=["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    if not Not_Zero:
        HexNum.insert(0,"0")
    try:
        a=''
        num=int(num)
        for i in range(num):
            if i == 1 and Not_Zero:
                HexNum.insert(0,0)
            a+=random.choice(HexNum)
        return a
    except Exception as e:
        print("错误",e)

def is_prime(num):
    try:
        num=int(num)
        if num<2:
            raise
        if num==2:
            return num,"是质数"
            return
        if num%2==0:
            raise
        for i in range(3,int(num**0.5)+1,2):
            if num%i==0:
                raise
        return num,"是质数"
    except:
        return num,"不是质数"

def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a

def Factorial(num):
    try:
        if num < 0:
            raise
        num=int(num)
        num2=1
        for i in range(2,num+1):
            num2*=i
        return num2
    except:
        pass

def Summation(num):
    try:
        if num < 0:
            raise
        return num * (num + 1) // 2
    except:
        pass