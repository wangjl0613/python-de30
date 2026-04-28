import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

plt.rcParams['font.family'] = 'Microsoft JhengHei'  # Windows 繁體中文
plt.rcParams['axes.unicode_minus'] = False   
df = pd.read_csv("Teen_Mental_Health_Dataset.csv")


# print(df.isnull().sum())

# print(df.duplicated())

df = df[df['age']<19]

# print( df[df['age']>=19])

print(df[['daily_social_media_hours','academic_performance']].describe())

# df.to_csv('Teen_Mental_Health_Dataset_backup.csv',index=False)

# sns.regplot(x='daily_social_media_hours', y='academic_performance', data=df)
# plt.title('社交媒體使用時數 vs GPA')
# plt.xlabel('每日使用時數')
# plt.ylabel('GPA')
# plt.show()

correlation = df['sleep_hours'].corr(df['screen_time_before_sleep'])
print(f'相關係數：{correlation:.2f}')



slope, intercept, r_value, p_value, std_err = stats.linregress(
    df['daily_social_media_hours'], 
    df['academic_performance']
)

print(f'R² = {r_value**2:.2f}')   # 解釋力
print(f'p值 = {p_value:.4f}')     # 是否顯著

print("這是練習有改變的地方")