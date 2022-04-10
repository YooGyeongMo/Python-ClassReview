# 변수
# 저장된 것을 사용하려면?
# 변수의 이름을 적어주면 됨. 변수는 상자와 같다고 생각하면 됨
# 상자에 저장된 값은 수시로 바뀔 수 있다. 그래서 변수(변하는 수) 라고 함
# 데이터를 저장하는 공간 : 변수
# 변수는  컴퓨터의 메모리 공간의 특정 위치에 이름을
# 붙여서 정수, 실수, 문자열 등의 데이터를 저장하는 것

# 저장된 것을 사용하려면?
# 변수의 이름을 적어주면 됨. 변수는 상자와 같다고 생각하면 됨
# 상자에 저장된 값은 수시로 바뀔 수 있다. 그래서 변수(변하는 수) 라고 함

#  프로그래밍 언어에서 =는 변수에 값을 할당한다는 의미
#  만약에 수학의 등호와 같은 역할을 원하면 == 입력

weight = 75.3
weight = 80.6
print(weight)
#  또한 변수는 필요에 따라서 얼마든지 많이 만들 수 있다.

x = 100
y = 200
print(x,y)

#  변수는 여러개 만들 수 있음

x, y, z = 10, 20, 30
print(x,y,z)
#  >>> x, y, z = 10, 20  변수 지정 하지 않으면 생기는 에러
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: not enough values to unpack (expected 3, got 2)

x = y = z = 10
print (x)
#  두 변수의 값을 바꾸려면 다음과 같이 변수를 할당할 때 서로 자리를 바꿔주면 됨
x, y = 10, 20
x, y = y, x
print(x)
# 20
# >>> y
# 10

# 변수에는 숫자 뿐만 아니라 문자열도 넣을 수 있다.
x = 'Hello World'
print(x)

#  프로그래밍 분야에서는 텍스트(Text, 글자) 데이터를 문자열(String) 이라고 함

#  파이썬에서의 문자열은 큰따옴표("...")나 작은따옴표('...')를 이용해서 만든다.

# 문자열은 다음과 같이 덧셈 연산자를 사용할 수 있음. 2개의 문자열을 서로 합하려면 +연산 사용
s1 = 'Hello'
s2 = "World!"
print(s1+s2)
s1 = "100"
s2 = "200"
print(s1+s2)

# 변수는 어떤 종류든 저장가능하다.

# value = 3
# value = 3.14
# value = "Hello"
# value = 'World'

# 선언한 변수를 삭제 할 수도 있다. del 사용

# >>> x = 10
# >>> del x
# >>> x
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'x' is not defined
# >>>

# 빈 변수 만들기
# >>> x = None
# >>> print(x)
# None
# >>> x
# >>>

'''
변수명 규칙
영문자[소문자 (a ~ z) 또는 대문자 (A ~ Z)], 한글, 숫자(0~9), 밑줄문자(_)로 사용하여 선언한다. 단 숫자로 시작하지 않는다.
예) Python_1 (○), 1_Python(×)

중간에 공백을 포함할 수 없다. 

두개 이상의 단어를 사용할 경우에는 밑줄로 연결한다.
예) Final_Exam (○), Final Exam (×)

변수명 규칙
대문자와 소문자가 구분된다.
예) Security와 security는 다른 변수이다.

파이썬의 예약어(keyword)와 함수이름은 사용할 수 없다.
예) if, else, for, while, print 등

의미 있는 단어로 표기하는 것이 좋다.
예) Department_Name (○), a, b (×)

!, @, #, $, %, & 등 특수 기호는 식별자에서 사용할 수 없다.
예) Kim&Lee (×)

식별자 스타일
카멜 표기법(Camel Case): 소문자로 시작, 단어가 달라질 때 첫글자는 대문자. (자바 스타일)
camelVariable, firstName, lastName 

파스칼 표기법(Pascal Case): 단어의 모든 앞 글자를 대문자로 표기
PascalVariable, FirstName, LastName 

헝가리안 표기법(Hungarian Notation): 접두어에 자료형을 붙이는 스타일
strName, bBusy, szName 

스네이크 표기법(Snake Case): 단어 사이에 언더바를 넣는 스타일  (c언어 스타일)
camel_variable, first_name, last_name

'''

# 중요

'''
우리는 변수의 이름을 마음대로 지을 수 있지만 파이썬이 내부적으로 사용하는 예약어는 변수의 이름으로 사용할 수 없다. 예약어를 사용하여 변수를 생성하면 오류가 발생한다. 


>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''

import keyword
print(keyword.kwlist)


speed = 100
my_height =180
# one+two = 3
원주율 = 3.14
# 나의 키 = 175
# for = 20
new_score = 100
# 1st_prize = gold
# global = 100
# name&no = ‘Kim20’

'''
코드 배치
들여쓰기는 공백 4칸을 권장한다.
한 줄은 최대 79자까지 쓸 수 있다.
최상위(top-level) 함수와 클래스 정의 사이에는 2줄을 띄어 쓴다.
클래스 내의 메소드 정의는 위아래로 줄바꿈을 사용하여 구분한다. 

표현식과 구문에서 불필요한 공백은 피한다. 

이름 지정 규칙
변수명에서 _(밑줄)은 위치에 따라 다음과 같은 의미가 있다.
1개의 밑줄로 시작 : 내부적으로 사용되는 변수
1개의 밑줄로 종료 : 파이썬 기본 키워드와 충돌을 피하려고 사용
2개의 밑줄로 시작 : 클래스 속성으로 사용
2개의 밑줄로 종료 : 사용자가 조정할 수 있는 네임스페이스 안의 속성
소문자 L, 대문자 O, 대문자 I는 혼동될 수 있으므로 변수명으로 사용하지 않는다.
모듈(Module) 명은 짧은 소문자로 구성되며 필요하다면 밑줄로 나눈다.
클래스명은 카멜케이스(CamelCase)로 작성한다. 
함수명은 소문자로 구성하되 필요하면 밑줄로 나눈다.
상수(Constant)는 모듈 단위에서만 정의하며 모두 대문자에 필요하다면 밑줄로 나눈다. 
'''

# 예제
'''
함수, 변수 : lowercase_underscore, my_score 
상수 : ALL_CAPS, PI

클래스 : CapitalizeWord
보호(protected) 인스턴스 속성 : _leading_underscore
비공개(private) 인스턴스 속성 : __double_leading_undersocre
'''

##############################################################################

# 자료형
