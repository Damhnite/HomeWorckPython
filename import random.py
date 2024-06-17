import random
import pandas as pd

# Создание списка с данными
lst = ['robot'] * 10 + ['human'] * 10

# Перемешивание списка
random.shuffle(lst)

# Создание DataFrame
data = pd.DataFrame({'whoAmI': lst})

# Преобразование в one hot вид
one_hot = pd.DataFrame()

for category in data['whoAmI'].unique():
    one_hot[category] = (data['whoAmI'] == category).astype(int)

# Объединение one hot столбцов с исходным DataFrame
data = pd.concat([data, one_hot], axis=1)

print(data.head())

