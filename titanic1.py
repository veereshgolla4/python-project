import pandas as pd

data = {
    "PassengerId": list(range(1, 16)),
    "Survived": [1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    "Pclass": [3, 1, 3, 1, 3, 3, 2, 2, 3, 1, 3, 1, 3, 3, 2],
    "Name": [
        "Allen, Miss. Elisabeth W.", "Moran, Mr. James", "McCarthy, Mr. Timothy J.",
        "Bonnell, Miss. Elizabeth", "Palsson, Master. Gosta Leonard", "Johnson, Mrs. Oscar W.",
        "Nasser, Mrs. Nicholas", "Sandstrom, Miss. Marguerite R.", "Bonnell, Miss. Susan",
        "Rice, Master. Eugene", "Montvila, Rev. Juozas", "Goldschmidt, Mr. George B.",
        "Lindblom, Miss. Augusta Charlotta", "Hays, Miss. Margaret Bechstein", "Carter, Miss. Lucile Polk"
    ],
    "Sex": ["female", "male", "male", "female", "male", "female", "female", "female", "female", "male", "male", "male", "female", "female", "female"],
    "Age": [29, 27, 54, 58, 2, 34, 21, 4, 45, 5, 45, 71, 42, 24, 18],
    "SibSp": [0, 0, 0, 0, 3, 1, 1, 1, 0, 4, 0, 0, 1, 0, 1],
    "Parch": [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 2],
    "Ticket": ["24160", "330877", "17463", "113783", "349909", "347742", "237736", "PP 9549", "113783", "382652", "211536", "PC 17601", "250649", "11767", "113760"],
    "Fare": [211.34, 8.05, 51.86, 153.46, 21.07, 23.45, 26.00, 16.70, 153.46, 29.12, 13.00, 120.00, 10.50, 45.00, 56.50],
    "Cabin": ["B5", "", "E46", "C103", "", "", "D36", "G6", "C103", "", "", "C92", "", "B96 B98", ""],
    "Embarked": ["S", "Q", "S", "S", "S", "S", "C", "S", "S", "Q", "S", "C", "S", "C", "S"]
}

df = pd.DataFrame(data)
df.to_csv("titanic.csv", index=False)

print("[OK] titanic.csv has been created successfully!")

