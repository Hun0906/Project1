## 함수(메서드) 선언부
def add_func(n1,n2) :
    result =  n1+n2
    return result

def sub_func(n1,n2) :
    result = n1 - n2
    return result

def mul_func(n1,n2) :
    result = n1 * n2
    return result

def div_func(n1,n2) :
    result = n1 / n2
    return result

## 전역 변수부(인스턴스 변수)
num1,num2,res = 100, 200, 0



## 메인 코드부(메인 메서드)
res = add_func(num1,num2)
print(num1,'+',num2,'=',res)

res = sub_func(num1,num2)
print(num1,'-',num2,'=',res)

res = mul_func(num1,num2)
print(num1,'*',num2,'=',res)

res = div_func(num1,num2)
print(num1,'/',num2,'=',res)
