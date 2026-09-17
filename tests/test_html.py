from collectors.http import fetch_url


def test_fetch_url():
    assert callable(fetch_url)

    
from processors.html import extract_title


def test_extract_title():
    html = """
    <html>
        <head>
            <title>Example Company</title>
        </head>
        <body>
            Hello
        </body>
    </html>
    """

    assert extract_title(html) == "Example Company"