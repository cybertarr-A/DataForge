from bs4 import BeautifulSoup


def extract_title(html: str) -> str | None:
    soup = BeautifulSoup(html, "html.parser")

    if soup.title:
        return soup.title.get_text(strip=True)

    return None