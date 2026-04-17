def search_articles(keyword, year_from, year_to):
    articles = [
        {
            "title": "Recent Advances in Cybersecurity",
            "authors": "John Smith, Anna Brown",
            "year": 2021,
            "doi": "10.1000/xyz123",
            "abstract": "This article discusses recent advances in cybersecurity.",
            "citations": 45,
            "country": "USA",
            "apa_citation": "Smith, J., & Brown, A. (2021). Recent Advances in Cybersecurity. Journal of Network Research."
        },
        {
            "title": "Cybersecurity in Modern Systems",
            "authors": "Maria Lopez, David Wilson",
            "year": 2023,
            "doi": "10.1000/xyz456",
            "abstract": "This paper analyzes the role of cybersecurity in modern systems.",
            "citations": 32,
            "country": "UK",
            "apa_citation": "Lopez, M., & Wilson, D. (2023). Cybersecurity in Modern Systems. International Journal of Security Studies."
        },
        {
            "title": "Challenges of Cybersecurity",
            "authors": "Emily Johnson, Robert White",
            "year": 2020,
            "doi": "10.1000/xyz789",
            "abstract": "This article explores the main challenges of cybersecurity.",
            "citations": 27,
            "country": "Germany",
            "apa_citation": "Johnson, E., & White, R. (2020). Challenges of Cybersecurity. European Security Review."
        },
        {
            "title": "AI-Based Intrusion Detection Systems",
            "authors": "Laura Green, Mark Hall",
            "year": 2022,
            "doi": "10.1000/xyz101",
            "abstract": "This study examines artificial intelligence techniques for intrusion detection systems.",
            "citations": 51,
            "country": "USA",
            "apa_citation": "Green, L., & Hall, M. (2022). AI-Based Intrusion Detection Systems. Computer Security Journal."
        },
        {
            "title": "Secure Communication Protocols in Distributed Networks",
            "authors": "Carlos Ruiz, Emma Scott",
            "year": 2021,
            "doi": "10.1000/xyz102",
            "abstract": "This article reviews secure communication protocols used in distributed networks.",
            "citations": 39,
            "country": "Spain",
            "apa_citation": "Ruiz, C., & Scott, E. (2021). Secure Communication Protocols in Distributed Networks. Journal of Communication Security."
        },
        {
            "title": "Malware Analysis Techniques for Enterprise Systems",
            "authors": "Kevin Adams, Sophie Turner",
            "year": 2022,
            "doi": "10.1000/xyz103",
            "abstract": "This paper presents modern malware analysis techniques for enterprise systems.",
            "citations": 44,
            "country": "France",
            "apa_citation": "Adams, K., & Turner, S. (2022). Malware Analysis Techniques for Enterprise Systems. Enterprise Security Review."
        },
        {
            "title": "Network Security Trends in Cloud Computing",
            "authors": "Olivia Clark, Daniel Evans",
            "year": 2023,
            "doi": "10.1000/xyz104",
            "abstract": "This article studies network security trends in cloud computing environments.",
            "citations": 36,
            "country": "Canada",
            "apa_citation": "Clark, O., & Evans, D. (2023). Network Security Trends in Cloud Computing. Cloud Systems Journal."
        },
        {
            "title": "Intrusion Detection in IoT Environments",
            "authors": "Nina Walker, Peter Lewis",
            "year": 2020,
            "doi": "10.1000/xyz105",
            "abstract": "This paper investigates intrusion detection in Internet of Things environments.",
            "citations": 29,
            "country": "Germany",
            "apa_citation": "Walker, N., & Lewis, P. (2020). Intrusion Detection in IoT Environments. IoT Security Journal."
        },
        {
            "title": "Secure Network Architectures for Smart Cities",
            "authors": "Helen Young, James Harris",
            "year": 2021,
            "doi": "10.1000/xyz106",
            "abstract": "This article presents secure network architectures for smart cities.",
            "citations": 22,
            "country": "Italy",
            "apa_citation": "Young, H., & Harris, J. (2021). Secure Network Architectures for Smart Cities. Smart Infrastructure Review."
        },
        {
            "title": "Cybersecurity Risk Assessment in Healthcare Networks",
            "authors": "Patricia King, Thomas Baker",
            "year": 2022,
            "doi": "10.1000/xyz107",
            "abstract": "This research focuses on cybersecurity risk assessment in healthcare networks.",
            "citations": 41,
            "country": "USA",
            "apa_citation": "King, P., & Baker, T. (2022). Cybersecurity Risk Assessment in Healthcare Networks. Health Security Journal."
        }
    ]

    keyword = keyword.lower().strip()
    year_from = int(year_from)
    year_to = int(year_to)

    filtered_articles = []

    for article in articles:
        title_match = keyword in article["title"].lower()
        abstract_match = keyword in article["abstract"].lower()

        if (title_match or abstract_match) and year_from <= article["year"] <= year_to:
            filtered_articles.append(article)

    return filtered_articles