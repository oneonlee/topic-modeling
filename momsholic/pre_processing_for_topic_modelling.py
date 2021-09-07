# !pip install nltk
# !pip install konlpy # include beautifulsoup4, numpy, etc
# !pip install git+https://github.com/ssut/py-hanspell.git
# !pip install pandas
# !pip install matplotlib

# "jpype._jvmfinder.JVMNotFoundException: No JVM shared library file (libjli.dylib) found. Try setting up the JAVA_HOME environment variable properly."
# 오류 발생 시,
# 오라클 JDK 다운로드 사이트에서 OS에 맞는 jdk를 다운받아 설치한다.

import pandas as pd
from konlpy.tag import Okt
from hanspell import spell_checker


def spell_checked_df(df):
    spell_list = []
    print(len(df))
    for i in range(43762, len(df)):
        spell_list.append(spell_checker.check(df['title'][i]).checked)
        print(i, spell_list[i])

    df['spell'] = spell_list

    df.to_csv("data/spell_checked.csv", mode='w')


def save_tokenizationed_df(df):
    token_list = []
    for i in range(len(df)):
        token_list.append(title_tokenization(df, i))
        print(token_list[i])

    df['token'] = token_list

    df.to_csv("data/tokeniztioned.csv", mode='w')


def title_tokenization(df, idx):
    # return df['title'].replace([df['title'][idx]], " ".join(
    #     okt.nouns(df['title'][idx])))

    return " ".join(okt.nouns(df['title'][idx]))


okt = Okt()

df = pd.read_csv('data/sample.csv', encoding='cp949',
                 low_memory=False)  # sample.csv 파일 읽기
# terms_df = pd.read_csv('data/internet_terms.csv', encoding='cp949')


df = df[df['name'].notna()]  # 'name'열이 'NA'인 것 지우기
df = df[['title', '개월']]
title_index = [i for i in range(len(df['title']))]
df = df.set_index(pd.Index(title_index))  # index 재구성

spell_checked_df(df)
# save_tokenizationed_df(df)

# print(df['token'])


# print(okt.morphs(df['title'][21]))  # 형태소 추출
# print(okt.pos(df['title'][21]))  # 품사 태깅(Part-of-speech tagging)
# print(type(okt.nouns(df['title'][2])))  # 명사 추출

# print(df)
# print(df.columns)  # 열 출력

# 전처리 - 동의어처리
# 조선생님꺼랑 비교
