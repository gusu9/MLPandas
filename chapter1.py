print("hello world")

import pandas as pd

dict_data = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
dict_data[5] = 'e'

print(dict_data)

sr = pd.Series(dict_data)

print(type(dict_data))
print(type(sr))

# print('\n')
print(sr)

list_data = ['Accra', 'Istanbul', 'Addis Ababa', 'Nairobi', 'Seoul']  #list는 library와 달리 key가 없기 때문에 index 값이 순서대로 자동생성

sr_data = pd.Series(list_data)
print(sr_data)

idx = sr_data.index
print(idx)

val = sr_data.values
print(val)

print(sr_data[1])
print(sr[2])

print(sr_data[2:4])

print('\n')
print('\t', sr_data[[1, 2]])

tup_data = ('수한', '1986-12-11', '남', False)
print(tup_data)
print(type(tup_data))
srt = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(srt)

print(srt[1])
print(srt['생년월일'])

print(srt[[2,3]])
print(srt[['성별', '학생여부']])

print(srt[1:3])                     #학생여부 앞까지만 출력
print(srt['생년월일':'학생여부'])       #학생여부까지 출력

