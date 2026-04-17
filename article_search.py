def search_articles(keyword, year_from, year_to):
    articles = [
        {
            "title": f"Recent Advances in {keyword}",
            "authors": "John Smith, Anna Brown",
            "year": 2021,
            "doi": "10.1000/xyz123",
            "abstract": f"This article discusses recent advances in {keyword}.",
            "citations": 45,
            "country": "USA",
            "apa_citation": f"Smith, J., & Brown, A. (2021). Recent Advances in {keyword}. Journal of Network Research."
        },
        {
            "title": f"{keyword} in Modern Systems",
            "authors": "Maria Lopez, David Wilson",
            "year": 2023,
            "doi": "10.1000/xyz456",
            "abstract": f"This paper analyzes the role of {keyword} in modern systems.",
            "citations": 32,
            "country": "UK",
            "apa_citation": f"Lopez, M., & Wilson, D. (2023). {keyword} in Modern Systems. International Journal of Security Studies."
        },
        {
            "title": f"Challenges of {keyword}",
            "authors": "Emily Johnson, Robert White",
            "year": 2020,
            "doi": "10.1000/xyz789",
            "abstract": f"This article explores the main challenges of {keyword}.",
            "citations": 27,
            "country": "Germany",
            "apa_citation": f"Johnson, E., & White, R. (2020). Challenges of {keyword}. European Security Review."
        }
    ]

    filtered_articles = []

    for article in articles:
        if int(year_from) <= article["year"] <= int(year_to):
            filtered_articles.append(article)

    return filtered_articles