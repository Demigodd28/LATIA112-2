import pandas as pd

def question_1(file):
    df = pd.read_csv(file)
    school = df.groupby('學校名稱')[['男生計', '女生計']].sum()

    school['男生比例(%)'] = (school['男生計'] / (school['男生計'] + school['女生計'])) * 100
    school['女生比例(%)'] = (school['女生計'] / (school['男生計'] + school['女生計'])) * 100
    for index, row in school.iterrows():
        print(f"{index}:")
        print(f"男生比例 {row['男生比例(%)']:.2f}%")
        print(f"女生比例 {row['女生比例(%)']:.2f}%")
        print("-"*20)

def question_2(file):
    df = pd.read_csv(file)
    grouped = df.groupby(['學校名稱', '等級別'])
    
    # 確保 '總計' 欄位存在
    total_count = grouped['總計'].sum().reset_index()

    bachelor = total_count[total_count['等級別'] == 'B 學士']
    master = total_count[total_count['等級別'].isin(['M 碩士', 'D 博士'])]  

    merged = pd.merge(bachelor, master, on='學校名稱', suffixes=('_大學部', '_研究所')) 
    merged['大學部比例'] = merged['總計_大學部'] / (merged['總計_大學部'] + merged['總計_研究所']) * 100
    merged['研究所比例'] = merged['總計_研究所'] / (merged['總計_大學部'] + merged['總計_研究所']) * 100

    for index, row in merged.iterrows():
        print(f"{row['學校名稱']} 大學部比例: {row['大學部比例']:.2f}%")
        print(f"{row['學校名稱']} 研究所比例: {row['研究所比例']:.2f}%")
        print("-"*20)

def question_3(file):
    df = pd.read_csv(file)
    school = df.groupby(['學校名稱', '日間∕進修別'])

    total_count = school['總計'].sum().reset_index()  # 重設索引以確保 total_count 是 DataFrame

    day = total_count.loc[total_count['日間∕進修別'] == 'D 日']
    night = total_count.loc[total_count['日間∕進修別'] == 'N 職']

    merged = pd.merge(day, night, on=['學校名稱'], suffixes=('_日間部', '_進修別'))
    merged['日間部比例'] = merged['總計_日間部'] / (merged['總計_進修別'] + merged['總計_日間部']) * 100
    merged['夜間部比例'] = merged['總計_進修別'] / (merged['總計_進修別'] + merged['總計_日間部']) * 100

    for index, row in merged.iterrows():
        print(f"{row['學校名稱']} 日間部比例: {row['日間部比例']:.2f}%")
        print(f"{row['學校名稱']} 夜間部比例: {row['夜間部比例']:.2f}%")
        print("-" * 20)



if __name__ == "__main__":
    csv_file = './112_student.csv'

    print("第一題:各大學的男女分佈？\n")
    question_1(csv_file)

    print("第二題:各大學大學部與研究所人數比？\n")
    question_2(csv_file)

    print("第三題:各大學日間部及夜間部的人數比？\n")
    question_3(csv_file)
