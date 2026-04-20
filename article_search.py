import requests


# Transform the author information sent by OpenAlex into readable text
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


# Generate a basic APA citation
def format_apa_citation(authors, year, title):
    if not authors:
        authors = "Unknown author"

    if not year:
        year = "n.d."

    if not title:
        title = "No title"

    return f"{authors} ({year}). {title}."


# Extract country from authors' institutions
def extract_country(authorships):
    countries = set()

    for author_item in authorships:
        for institution in author_item.get("institutions", []):
            country_code = institution.get("country_code")
            if country_code:
                countries.add(country_code)

    if len(countries) == 1:
        return list(countries)[0]
    elif len(countries) > 1:
        return "Multiple"
    else:
        return "Unknown"


# Rebuild abstract text from OpenAlex abstract_inverted_index
def reconstruct_abstract(abstract_inverted_index):
    if not abstract_inverted_index:
        return "No abstract available"

    try:
        word_positions = []

        for word, positions in abstract_inverted_index.items():
            for pos in positions:
                word_positions.append((pos, word))

        word_positions.sort(key=lambda x: x[0])

        abstract_words = [word for _, word in word_positions]
        abstract_text = " ".join(abstract_words).strip()

        return abstract_text if abstract_text else "No abstract available"

    except Exception:
        return "No abstract available"


def search_articles(keyword, year_from, year_to):
    # Clean input values
    keyword = str(keyword).strip()
    year_from = int(year_from)
    year_to = int(year_to)

    url = "https://api.openalex.org/works"

    # Parameters sent to the API
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
            # Title
            title = str(work.get("display_name", "")).strip()
            if not title or len(title) < 8:
                continue

            normalized_title = title.lower()
            if normalized_title in seen_titles:
                continue

            # Publication year
            year = work.get("publication_year")
            if year is None:
                continue

            try:
                year = int(year)
            except (ValueError, TypeError):
                continue

            if not (year_from <= year <= year_to):
                continue

            # Authors
            authorships = work.get("authorships", [])
            authors = format_authors(authorships)

            # Abstract
            abstract = reconstruct_abstract(work.get("abstract_inverted_index"))

            # Citations
            cited_by_count = work.get("cited_by_count", 0)
            try:
                citations = int(cited_by_count)
            except (ValueError, TypeError):
                citations = 0

            # DOI
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
                "country": extract_country(authorships),
                "apa_citation": format_apa_citation(authors, year, title)
            }

            articles.append(article)
            seen_titles.add(normalized_title)

    except requests.RequestException as e:
        print(f"Error while searching OpenAlex API: {e}")

    return articles