import pandas as pd

data = {
    'Ученик': ['Алексей', 'Борис', 'Владимир', 'Галина', 'Дмитрий', 'Елена', 'Жанна', 'Иван', 'Ксения', 'Лариса'],
    'Математика': [5, 4, 4, 5, 5, 4, 5, 3, 4, 5],
    'Физика': [4, 5, 5, 5, 4, 5, 5, 3, 5, 5],
    'Химия': [3, 5, 5, 5, 4, 5, 5, 3, 4,4],
    'Литература': [5, 3, 4, 3, 4, 4, 5, 3, 4, 5],
    'История': [3, 5, 5, 3, 4, 5, 5, 3, 4, 5]
}

df = pd.DataFrame(data)

print("Первые несколько строк DataFrame:")
print(df.head())

mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print("\nQ1 для оценок по математике:", Q1_math)
print("Q3 для оценок по математике:", Q3_math)
print("IQR для оценок по математике:", IQR_math)

std_dev = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_dev)
