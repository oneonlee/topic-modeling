import re
import pandas as pd

df = pd.read_csv('data/sample.csv', encoding='cp949',
                 low_memory=False)  # sample.csv 파일 읽기

df = df[df['name'].notna()]  # 'name'열이 'NA'인 것 지우기
df = df[['title', '개월']]
title_index = [i for i in range(len(df['title']))]
df = df.set_index(pd.Index(title_index))  # index 재구성

syn_df = pd.read_csv('data/momsholic_synonym_sample.csv')

syn_df = syn_df[syn_df['동의어1'].notna()]  # '동의어1'의 행 중 값이 없는 행은 삭제

syn_df = syn_df[['n', '동의어1']]

len_syn = len(syn_df['동의어1'])
syn_index = [i for i in range(len_syn)]
syn_df = syn_df.set_index(pd.Index(syn_index))  # index 재구성

# for i in range(len_syn):
#
#     df['title'].replace(to_replace=syn_df.loc[i]["n"],
#                         value=syn_df.loc[i]["동의어1"], inplace=True)

# df.replace(to_replace="젖꼭지", value="wjwRhrwl", inplace=True)

len_df = len(df)
for i in range(len_df):
    for j in range(len(syn_df['동의어1'])):
        df['title'][i] = re.sub(
            syn_df.loc[j]["n"], syn_df.loc[j]["동의어1"], df['title'][i])
    print(f"{i} of {len_df}")

df.to_csv("data/synonym_checked.csv", mode='w', index=False)

print(df['title'])
