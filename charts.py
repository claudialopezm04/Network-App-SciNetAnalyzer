import matplotlib.pyplot as plt
import os

def generate_charts(articles):
    os.makedirs("results", exist_ok=True)

    # -------------------------------
    # Chart 1: Articles by year
    # -------------------------------
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
    plt.savefig("results/articles_by_year.png")
    plt.close()

    # -------------------------------
    # Chart 2: Articles by country
    # -------------------------------
    countries = {}
    for article in articles:
        country = article["country"]
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
    plt.savefig("results/articles_by_country.png")
    plt.close()

    # -------------------------------
    # Chart 3: Citations per article
    # -------------------------------
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
    plt.savefig("results/citations_per_article.png")
    plt.close()

    return [
        "results/articles_by_year.png",
        "results/articles_by_country.png",
        "results/citations_per_article.png"
    ]