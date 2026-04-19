import requests


def format_authors(authors_list):
    if not authors_list:
        return "Unknown"

    names = []
    for author in authors_list:
        name = author.get("name", "").strip()
        if name:
            names.append(name)

    return ", ".join(names) if names else "Unknown"


def format_apa_citation(authors, year, title):
    if not authors:
        authors = "Unknown author"

    if not year:
        year = "n.d."

    if not title:
        title = "No title"

    return f"{authors} ({year}). {title}."


def search_articles(keyword, year_from, year_to):
    keyword = str(keyword).strip()
    year_from = int(year_from)
    year_to = int(year_to)

    url = "https://api.semanticscholar.org/graph/v1/paper/search"

    params = {
        "query": keyword,
        "limit": 20,
        "fields": "title,authors,year,abstract,citationCount,externalIds,url"
    }

    articles = []
    seen_titles = set()

    try:
        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()

        data = response.json()
        papers = data.get("data", [])

        for paper in papers:
            title = str(paper.get("title", "")).strip()
            if not title or len(title) < 8:
                continue

            normalized_title = title.lower()
            if normalized_title in seen_titles:
                continue

            year = paper.get("year")
            if year is None:
                continue

            try:
                year = int(year)
            except (ValueError, TypeError):
                continue

            if not (year_from <= year <= year_to):
                continue

            authors = format_authors(paper.get("authors", []))

            abstract = paper.get("abstract")
            if not abstract:
                abstract = "No abstract available"

            citations = paper.get("citationCount", 0)
            try:
                citations = int(citations)
            except (ValueError, TypeError):
                citations = 0

            external_ids = paper.get("externalIds", {}) or {}
            doi = external_ids.get("DOI", "N/A")

            article = {
                "title": title,
                "authors": authors,
                "year": year,
                "doi": doi,
                "abstract": abstract,
                "citations": citations,
                "country": "Unknown",
                "apa_citation": format_apa_citation(authors, year, title)
            }

            articles.append(article)
            seen_titles.add(normalized_title)

    except requests.RequestException as e:
        print(f"Error while searching Semantic Scholar API: {e}")

    return articles