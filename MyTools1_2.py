#The Ver = 1.2
#By 一只屑system32
#(uzjhf-836,Zuowan)
import random,webbrowser,time,sys
class 没有Error(Exception):
    pass
class 结束(Exception):
    pass
if __name__ == "__main__":
    print('呃,这里好像不提供主程序运行服务......')
    if input("不过你要测试吗?"):
        pass
    else:
        raise 没有Error
class Classic_Tools():
    def Right_To_Left(text)->str:
        text = str(text)
        a=''
        for i in text[::-1]:
            a+=i
        return a

    def Right_To_Left_Old(text)->str:
        text = str(text)
        a=""
        for i in range(len(text)):
            a+=text[len(text)-(i+1)]
        return a

    def Base10(Hex:str,Base:int) -> int:
        try:
            return (int(str(Hex),int(Base)))
        except Exception as e:
            print(e)

    def Random_16Hex(num,Not_Zero=True)->str:
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

    def is_prime(num)->str:
        try:
            num=int(num)
            if num<2:
                raise
            if num==2:
                return num,"是质数"
            if num%2==0:
                raise
            for i in range(3,int(num**0.5)+1,2):
                if num%i==0:
                    raise
            return num,"是质数"
        except:
            return num,"不是质数"

    def fib(n:int)->int:
        try:n=int(n)
        except:pass
        a, b = 1, 1
        for i in range(n-1):
            a, b = b, a+b
        return a

    def Factorial(num)->int:
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

    def Summation(num:int)->int:
        try:
            num=int(num)
            if num < 0:
                raise
            return num * (num + 1) // 2
        except:
                pass
    def random_password()->str:
        pwd_text=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
 , "!", "_","$","&","+","=","-"]
        text=""
        for i in range(random.randint(12,20)):
            text+=random.choice(pwd_text)
        return text

    def CountDown(sec):
        try:
            sec=int(sec)
            print(f"当前秒数{sec}秒",flush=True)
            time.sleep(1)
            if sec<=0:
                raise 结束
            else:
                Classic_Tools.CountDown(sec-1)
        except (结束,KeyboardInterrupt,EOFError):
                print("结束")
        except Exception as e:
            print("Error",e)

#=============Easter Egg=============
class Easter_Egg():
    def Egg():
        try:
            while True:
                print("Egg!")
        except:
            Easter_Egg.Egg()

    def RickRoll():
        webbrowser.open_new_tab("https://www.bilibili.com/video/BV1GJ411x7h7/")

    def Not_Run_This_Function():
        print("?")
        time.sleep(1)
        print("不听?")
        time.sleep(1)
        print("好吧,你不听,也没事")
        time.sleep(10)
        print("你还在等?")
        time.sleep(1)
        print("嗯,好吧")
        time.sleep(0.5)
        if input("那我们玩玩?"):
            pass
        else:
            return ''
        a=input("你叫什么名字❓")
        if a == "齐":
            print("哇哇哇")
            print("大神口牙❗️")
        elif a == "一只屑system32":
            print("哇哇哇哇学我?")
        elif "啊啊啊啊啊" in a:
            print("别叫了")
        else:
            print("嗯,没事了")