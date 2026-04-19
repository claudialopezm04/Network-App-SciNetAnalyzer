import requests


def format_authors(authorships):
    if not authorships:
        return "Unknown"

    names = []
    for author_item in authorships:
        author_info = author_item.get("author", {})
        name = author_info.get("display_name", "").strip()
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

    url = "https://api.openalex.org/works"

    params = {
        "search": keyword,
        "filter": f"from_publication_date:{year_from}-01-01,to_publication_date:{year_to}-12-31",
        "per-page": 10
    }

    headers = {
        "User-Agent": "SciNetAnalyzer/1.0"
    }

    articles = []
    seen_titles = set()

    try:
        response = requests.get(url, params=params, headers=headers, timeout=20)
        response.raise_for_status()

        data = response.json()
        works = data.get("results", [])

        for work in works:
            title = str(work.get("display_name", "")).strip()
            if not title or len(title) < 8:
                continue

            normalized_title = title.lower()
            if normalized_title in seen_titles:
                continue

            year = work.get("publication_year")
            if year is None:
                continue

            try:
                year = int(year)
            except (ValueError, TypeError):
                continue

            authors = format_authors(work.get("authorships", []))

            abstract = "No abstract available"
            if work.get("abstract_inverted_index"):
                abstract = "Abstract available in source data"

            cited_by_count = work.get("cited_by_count", 0)
            try:
                citations = int(cited_by_count)
            except (ValueError, TypeError):
                citations = 0

            doi = work.get("doi", "N/A")
            if doi and doi != "N/A":
                doi = doi.replace("https://doi.org/", "")

            article = {
                "title": title,
                "authors": authors,
                "year": year,
                "doi": doi if doi else "N/A",
                "abstract": abstract,
                "citations": citations,
                "country": "Unknown",
                "apa_citation": format_apa_citation(authors, year, title)
            }

            articles.append(article)
            seen_titles.add(normalized_title)

    except requests.RequestException as e:
        print(f"Error while searching OpenAlex API: {e}")

    return articles