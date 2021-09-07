import json
import pandas as pd
from hanspell import spell_checker


def spell_checked_df(df):
    spell_list = []
    print(len(df))
    for i in range(len(df)):
        try:
            spell_list.append(spell_checker.check(df['title'][i]).checked)
        except json.decoder.JSONDecodeError:
            spell_list.append("json.decoder.JSONDecodeError")
        print(i, spell_list[i])

    df['spell'] = spell_list

    df.to_csv("data/spell_checked.csv", mode='w', index=False)


df = pd.read_csv('data/synonym_checked.csv',
                 low_memory=False)  # sample.csv 파일 읽기

spell_checked_df(df)
