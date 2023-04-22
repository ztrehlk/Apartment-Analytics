from redfin_scraper import RedfinScraper
import pandas as pd


def listing_redfin_scraper(city_list: list[str], zip_database_path: str) -> pd.DataFrame:
    """
    Scrapes real estate listings data from the Redfin website for a 
    list of cities and returns the data as a Pandas DataFrame.

    Args:
        city_list (list[str]):      A list of strings that contains the names of the cities 
                                    for which you want to scrape real estate listings data.

        zip_database_path (str):    A string that specifies the file path to the ZIP code 
                                    database file that the scraper will use.

    Returns:
        pd.DataFrame:               A Pandas DataFrame that contains the real estate listings 
                                    data for all the cities in the `city_list` parameter.
    """


    # set up the scraper package
    scraper = RedfinScraper()
    scraper.setup(zip_database_path=zip_database_path)

    # starting empty dataframe to concatenate on
    listing_df = pd.DataFrame()

    # loop through each city to gather its listing info
    for city in city_list:
        city_df = scraper.scrape(city_states=[city])
        listing_df = pd.concat([listing_df, city_df])

    # drop instances of duplicates
    listing_df.drop_duplicates(inplace=True)

    return listing_df