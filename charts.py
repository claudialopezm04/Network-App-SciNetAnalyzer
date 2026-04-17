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

    plt.figure(figsize=(8, 5))
    plt.bar(years.keys(), years.values())
    plt.title("Distribution of Articles by Publication Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Articles")
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

    plt.figure(figsize=(8, 5))
    plt.bar(countries.keys(), countries.values())
    plt.title("Distribution of Articles by Country")
    plt.xlabel("Country")
    plt.ylabel("Number of Articles")
    plt.tight_layout()
    plt.savefig("results/articles_by_country.png")
    plt.close()

    # -------------------------------
    # Chart 3: Citations per article
    # -------------------------------
    titles = [article["title"] for article in articles]
    citations = [article["citations"] for article in articles]

    plt.figure(figsize=(10, 5))
    plt.bar(titles, citations)
    plt.title("Number of Citations per Article")
    plt.xlabel("Article")
    plt.ylabel("Citations")
    plt.xticks(rotation=20, ha="right")
    plt.tight_layout()
    plt.savefig("results/citations_per_article.png")
    plt.close()

    return [
        "results/articles_by_year.png",
        "results/articles_by_country.png",
        "results/citations_per_article.png"
    ]