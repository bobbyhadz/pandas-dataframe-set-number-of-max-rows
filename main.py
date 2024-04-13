# Pandas: Set the number of max Rows shown in a DataFrame

import pandas as pd

# 👇️ set max rows to 600
pd.set_option('display.max_rows', 600)

# 👇️ or show all Rows (Unlimited)
# pd.set_option('display.max_rows', None)

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan', 'Ethan'],
    'experience': [1, 1, 5, 7, 7],
    'salary': [175.1, 180.2, 190.3, 205.4, 210.5],
})

print(df)