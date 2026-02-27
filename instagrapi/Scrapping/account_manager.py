from instagr import InstagramScraper

# Initialize Database Scraper
scraper = InstagramScraper(
    db_host="localhost",
    db_name="magang",
    db_user="postgres",
    db_password="indojayaraya",
    headless=True,
)

# Add accounts
scraper.add_account(
    username="rosyidcoc",
    password="@Indojayaraya1945",
    tags=["primary", "research"],
    notes="Main research account",
)
