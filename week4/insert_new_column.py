import pandas as pd


def insert_private_or_public(df):
    type_list = [] # 建立空字串

    for i in df['學校名稱']:
        if ('國立' in i) or ('市立' in i):
            type_list.append('國立')
        else:
            type_list.append('私立')

    df['公私立'] = type_list # 將 Dataframe 新增「公私立」column
    
    return df

def insert_city_name(df):
    city_list = []

    for i in df['縣市名稱']:
        city_list.append(i[3:])

    df['縣市名'] = city_list

    return df

def insert_area(df):
    city_to_area = {'臺北市':'北部',
         '新北市':'北部',
         '基隆市':'北部',
         '新竹市':'北部',
         '桃園市':'北部',
         '新竹縣':'北部',
         '宜蘭縣':'北部',
         '臺中市':'中部',
         '苗栗縣':'中部',
         '彰化縣':'中部',
         '南投縣':'中部',
         '雲林縣':'中部',
         '高雄市':'南部',
         '臺南市':'南部',
         '嘉義市':'南部',
         '嘉義縣':'南部',
         '屏東縣':'南部',
         '澎湖縣':'南部',
         '花蓮縣':'東部',
         '臺東縣':'東部',
         '金門縣':'福建省'}

    df['區域'] = df['縣市名'].map(city_to_area)
    return df

def main():
    old_csv = "week2/112_student.csv"
    new_csv = "week4/112_students_tf.csv"
    
    df = pd.read_csv(old_csv)
    
    df = insert_private_or_public(df)
    # print(df)
    df = insert_city_name(df)
    # print(df)
    
    df = insert_area(df)
    print(df)
    
    df.to_csv(new_csv, index=False)

if __name__ == "__main__":
    pd.set_option('display.max_rows', None)
    main()

