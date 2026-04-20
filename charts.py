import matplotlib.pyplot as plt
import os
import pycountry


def get_country_name(code):
    if not code:
        return "Unknown"

    if code == "Unknown":
        return "Unknown"

    if code == "Multiple":
        return "Multiple Countries"

    try:
        country = pycountry.countries.get(alpha_2=code.upper())
        if country:
            return country.name
    except Exception:
        pass

    return code


def generate_charts(articles, output_folder, keyword, year_from, year_to, timestamp):
    os.makedirs(output_folder, exist_ok=True)

    safe_keyword = keyword.replace(" ", "_").lower()

    year_chart = os.path.join(
        output_folder,
        f"{safe_keyword}_{year_from}_{year_to}_articles_by_year_{timestamp}.png"
    )
    country_chart = os.path.join(
        output_folder,
        f"{safe_keyword}_{year_from}_{year_to}_articles_by_country_{timestamp}.png"
    )
    citations_chart = os.path.join(
        output_folder,
        f"{safe_keyword}_{year_from}_{year_to}_citations_per_article_{timestamp}.png"
    )

    # Chart 1: Articles by year
    years = {}
    for article in articles:
        year = article["year"]
        years[year] = years.get(year, 0) + 1

    sorted_years = dict(sorted(years.items()))

    plt.figure(figsize=(9, 5))
    plt.bar(
        sorted_years.keys(),
        sorted_years.values(),
        color="steelblue",
        edgecolor="black"
    )
    plt.title("Distribution of Articles by Publication Year", fontsize=14, fontweight="bold")
    plt.xlabel("Year", fontsize=11)
    plt.ylabel("Number of Articles", fontsize=11)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(year_chart)
    plt.close()

    # Chart 2: Articles by country
    countries = {}
    for article in articles:
        country = get_country_name(article["country"])
        countries[country] = countries.get(country, 0) + 1

    sorted_countries = dict(sorted(countries.items(), key=lambda item: item[1], reverse=True))

    plt.figure(figsize=(9, 5))
    plt.bar(
        sorted_countries.keys(),
        sorted_countries.values(),
        color="mediumseagreen",
        edgecolor="black"
    )
    plt.title("Distribution of Articles by Country", fontsize=14, fontweight="bold")
    plt.xlabel("Country", fontsize=11)
    plt.ylabel("Number of Articles", fontsize=11)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(country_chart)
    plt.close()

    # Chart 3: Citations per article
    titles = [article["title"] for article in articles]
    citations = [article["citations"] for article in articles]

    plt.figure(figsize=(11, 6))
    plt.bar(
        titles,
        citations,
        color="salmon",
        edgecolor="black"
    )
    plt.title("Number of Citations per Article", fontsize=14, fontweight="bold")
    plt.xlabel("Article", fontsize=11)
    plt.ylabel("Citations", fontsize=11)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(citations_chart)
    plt.close()

    return [year_chart, country_chart, citations_chart]