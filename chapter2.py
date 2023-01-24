#dataframe 데이터프레임: 2차원 배열
import pandas as pd

dict_data = {'c0':[1,2,3,4], 'c1':[5,6,7,8], 'c2':[9,10,11,12], 'c3':[13,14,15,16], 'c4':[17,18,19,20]}
df=pd.DataFrame(dict_data)

print(dict_data)
print(type(dict_data))
print(type(df))
print(df)

dfs = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                   index = ['준서', '예은'],
                   columns=['나이', '성별', '학교'])

print(dfs)

print(dfs.index)
print(dfs.columns)

# change index and columns
dfs.index = ['학생1', '학생2']
dfs.columns = ['연령', '성별', '소속']

print(dfs)
print(dfs.index)
print(dfs.columns)

dfs.rename(index={'학생1':'사람1'}, inplace=True)
print(dfs)
dfs.rename(index={'학생2':'사람2'}, inplace=True)
print(dfs)

exam_data = {'수학': [90,80,70], '영어': [98,89,95],
            '음악': [85,95,100], '체육': [100,90,90]}

dfe = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print('\n')
print(dfe)

dfe2 = dfe[:]
print(dfe2)
dfe2.drop(['우현'], axis = 0, inplace =True)
print(dfe2)

dfe3=dfe[:]
dfe3.drop(['우현', '인아'], axis = 0, inplace=True)
print('\n')
print(dfe3)
print('\n')
dfe4=dfe[:]
dfe4=dfe4.drop(['우현', '서준'])
print(dfe4)

dfe5 = dfe[:]

dfe5.drop('수학', axis=1, inplace=True)
print(dfe5)

dfe6 = dfe[:]
dfe6.drop(['영어', '음악'], axis=1, inplace=True)
print(dfe6)

label1 = dfe.loc['서준']
position1 = dfe.iloc[0]
print(label1)
print(position1)

label2 = dfe.loc[['서준','우현']]     #대괄호 두개
position2 = dfe.iloc[[0,1]]     #대괄호 두개
label3 = dfe.loc['서준':'우현']     #대괄호 한개
position3 = dfe.iloc[0:2]       #대괄호 한개
print("label2")
print(label2)
print("position2")
print(position2)
print('label3')
print(label3)
print('position3')
print(position3)


exam_data_name = {'이름': ['서준', '우현', '인아', '수한', '현정', '은지', '원준', '수민', '보성', '성원'],
                  '수학': [90, 80, 70, 75, 80, 90, 100, 95, 80, 85],
                  '영어': [98, 89, 95, 90, 95, 90, 90, 80, 70, 75],
                  '음악': [85, 95, 100, 90, 95, 100, 80, 70, 80, 85],
                  '체육': [100, 90, 90, 80, 70, 80, 90, 95, 95, 90]}

dfen = pd.DataFrame(exam_data_name)
print('\n')
print(dfen)
print(type(dfen))
math1 = dfen['수학']

print('\n')
print("Math1")
print(math1)
print(type(math1))
print('\n')

eng = dfen.영어
print("English")
print(eng)

core = dfen[['수학', '영어']]
print('\n')
print(core)
print(type(core))

cul = dfen[['음악', '체육']]
print('\n')
print(cul)
print(type(cul))

ncore = dfen[['이름', '수학', '영어']]
print('\n')
print(ncore)
print(type(ncore))

math2 = dfen[['수학']]
print('\n')
print(math2)
print(type(math2))

print('\n')
print(dfen)
print('\n')

print(dfen.iloc[::2])

print('\n')
print(dfen.iloc[:6:-2])

print(dfen)

dfen.set_index('이름', inplace=True)
a = dfen.loc['수한', '수학']
print(a)

print(dfen.iloc[0:2,2:4])