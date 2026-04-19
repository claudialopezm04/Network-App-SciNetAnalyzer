import pandas as pd
import os

def export_to_excel(articles, output_folder, keyword, year_from, year_to, timestamp):
    os.makedirs(output_folder, exist_ok=True)

    safe_keyword = keyword.replace(" ", "_").lower()
    filename = os.path.join(
        output_folder,
        f"{safe_keyword}_{year_from}_{year_to}_{timestamp}.xlsx"
    )

    df = pd.DataFrame(articles)
    df.to_excel(filename, index=False)

    return filename