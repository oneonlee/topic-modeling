import pandas as pd
df = pd.read_csv('data/tokeniztioned.csv',
                 low_memory=False)  # sample.csv 파일 읽기

token_list = []
index_list = []
for i in range(len(df['token'])):
    index_list.append(i)
    try:
        token_list += df['token'][i].split()
        # print(f"{i} of {len(df['token'])}")
    except AttributeError:  # token이 없는 경우 예외처리
        print(f"ERROR!\n{i} : {df['token'][i]}")

print(f"중복 제거 전 : {len(token_list)}개")
token_list = list(set(token_list))
print(f"중복 제거 후 : {len(token_list)}개")

print("making matrix_df!")
matrix_df = pd.DataFrame(index=index_list, columns=token_list)

print("nan to 0")
matrix_df = matrix_df.fillna(0)
for col in range(len(matrix_df.columns)):
    print(f"{col} of {len(matrix_df.columns)} : {matrix_df.columns[col]}")
    for idx in matrix_df.index:
        try:
            cnt = df['token'][idx].split().count(matrix_df.columns[col])
            matrix_df[matrix_df.columns[col]][idx] = cnt
        except AttributeError:  # token이 없는 경우 예외처리
            pass

print("saving matrix_df!")
matrix_df.to_csv("data/matrix.csv", mode='w')

print(matrix_df)
