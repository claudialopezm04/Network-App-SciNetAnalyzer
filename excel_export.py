import pandas as pd
import os

def export_to_excel(articles, filename="results/articles.xlsx"):
    os.makedirs("results", exist_ok=True)

    df = pd.DataFrame(articles)
    df.to_excel(filename, index=False)

    return filename