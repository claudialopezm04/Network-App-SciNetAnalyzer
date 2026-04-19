import pandas as pd
import os
from datetime import datetime

def export_to_excel(articles, keyword, year_from, year_to):
    os.makedirs("results", exist_ok=True)

    safe_keyword = keyword.replace(" ", "_").lower()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"results/{safe_keyword}_{year_from}_{year_to}_{timestamp}.xlsx"

    df = pd.DataFrame(articles)
    df.to_excel(filename, index=False)

    return filename