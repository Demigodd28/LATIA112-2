import os
import pandas as pd
import matplotlib.pyplot as plt

def question_1(file, folder):
    # 讀取 CSV 檔案
    df = pd.read_csv(file)   
    # 建立一個新的欄目edu做Medu和Fedu的總和
    df["edu"] = df[["Medu", "Fedu"]].mean(axis=1).fillna(0)
    # 提取平均教育程度、學生期末考成績
    data = df[["edu", "G3"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"父母平均教育程度:{row[0]}\t學生成績:{round(row[1])}")

    ## 建立圖表
    plt.figure()
    # 繪製散點圖
    plt.scatter(data["edu"], data["G3"])
    # 添加標籤和標題
    plt.title('Parental Education Level and Student Final Grade')
    plt.xlabel('Parental Education Level (Average)')
    plt.ylabel('Student Final Grade')

    save_path = os.path.join(folder, 'Question1.png')
    plt.savefig(save_path)

def question_2(file, folder):
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 提取課後空閒時間、與朋友出去玩
    data = df[["freetime", "goout"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"課後空閒時間多寡:{row[0]}\t與朋友出去玩的頻率:{row[1]}")

    # 建立箱形圖
    plt.figure(figsize=(8, 6))
    # 繪製箱形圖
    data.boxplot(column=["freetime", "goout"])
    # 添加標籤和標題
    plt.title('Distribution of Free Time and Going Out with Friends')
    plt.xlabel('Variable')
    plt.ylabel('Frequency')

    save_path = os.path.join(folder, 'Question2.png')
    plt.savefig(save_path)

def question_3(file, folder):
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 建立一個新的欄目alco做Dalc和Dalc的總和
    df['alco'] = df[['Dalc', 'Walc']].sum(axis=1)
    # 提取總喝酒頻率、缺席數
    data = df[["alco", "absences"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"平常喝酒的頻率高低:{row[0]}\t平常到校上學的缺席數:{row[1]}")

    # 建立圖表
    plt.figure(figsize=(8, 6))
    # 繪製散點圖
    plt.scatter(data["alco"], data["absences"], alpha=0.5)
    # 添加標籤和標題
    plt.title('Relationship between Alcohol Consumption and Absences')
    plt.xlabel('Alcohol Consumption')
    plt.ylabel('Absences')

    save_path = os.path.join(folder, 'Question3.png')
    plt.savefig(save_path)

def question_4(file, folder):
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 提取家庭教育支持、學生讀書時間
    data = df[["famsup", "studytime"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"家庭是否提供額外的教育支持:{row['famsup']}\t學生的學習時間:{row['studytime']}")

    # 建立圖表
    plt.figure(figsize=(8, 6))
    # 分組統計
    grouped_data = data.groupby("famsup").mean()
    # 繪製條形圖
    grouped_data.plot(kind="bar", legend=False)
    # 添加標籤和標題
    plt.title('Average Study Time with and without Family Educational Support')
    plt.xlabel('Family Educational Support (Yes/No)')
    plt.ylabel('Average Study Time')

    save_path = os.path.join(folder, 'Question4.png')
    plt.savefig(save_path)

def question_5(file, folder):
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 提取家裡住址、學生成績
    df['grade'] = df[["G1", "G2", "G3"]].mean(axis=1).fillna(0)
    data = df[["address", "grade"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"家裡住址:{row['address']}\t學生學期平均成績:{round(row['grade'], 2)}")

    # 建立圖表
    plt.figure(figsize=(8, 6))
    # 繪製長條圖
    data.groupby('address')['grade'].mean().plot(kind='bar')
    # 添加標籤和標題
    plt.title('Average Grades by Address Type')
    plt.xlabel('Address Type')
    plt.ylabel('Average Grade')

    save_path = os.path.join(folder, 'Question5.png')
    plt.savefig(save_path)

def question_6(file, folder):
    # 讀取 CSV 檔案
    df = pd.read_csv(file)
    # 提取網路、課外學習
    data = df[["internet", "activities"]]
    # 印出資料
    for index, row in data.iterrows():
        print(f"網路接入:{row['internet']}\t課外學習:{row['activities']}")
    
    # 計算每個類別的計數
    counts = data.apply(pd.Series.value_counts)
    # 建立圖表
    plt.figure(figsize=(8, 6))
    # 繪製條形圖
    counts.plot(kind='bar', stacked=True)
    # 添加標籤和標題
    plt.title('Internet Access and Participation in Extracurricular Activities')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.legend(title='Variable')

    save_path = os.path.join(folder, 'Question6.png')
    plt.savefig(save_path)
    
if __name__ == '__main__':
    csv_file = 'student-mat.csv'

    folder_name = f'Pics of analysis'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name) 

    print("學業表現與家庭背景之間的相關性：")
    question_1(csv_file, folder_name)

    print("課後空閒時間多寡與與朋友出去玩的頻率之間的關係：")
    question_2(csv_file, folder_name)

    print("平日喝酒多寡與上課缺席數之關係")
    question_3(csv_file, folder_name)

    print("教育支持與學生學習時間的關係")
    question_4(csv_file, folder_name)

    print("家庭住址是否影響學生的學業表現")
    question_5(csv_file, folder_name)

    print("學生的網路接入是否影響他們的課外學習")
    question_6(csv_file, folder_name)
