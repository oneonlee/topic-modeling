import pandas as pd
from konlpy.tag import Okt
from hanspell import spell_checker


def save_tokenizationed_df(df):
    token_list = []
    for i in range(len(df)):
        token_list.append(title_tokenization(df, i))
        print(token_list[i])

    df['token'] = token_list

    df.to_csv("data/tokeniztioned.csv", mode='w', index=False)


def title_tokenization(df, idx):
    return " ".join(okt.nouns(df['spell'][idx]))


okt = Okt()

df = pd.read_csv('data/spell_checked.csv',
                 low_memory=False)  # sample.csv 파일 읽기

save_tokenizationed_df(df)

print(df['token'])


# print(okt.morphs(df['title'][21]))  # 형태소 추출
# print(okt.pos(df['title'][21]))  # 품사 태깅(Part-of-speech tagging)
# print(type(okt.nouns(df['title'][2])))  # 명사 추출
