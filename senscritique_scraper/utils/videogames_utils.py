import logging
from . import row_utils

logger = logging.getLogger(__name__)


def get_videogames_infos_from_row(row):
    return {
        "Rank": row_utils.get_rank(row),
        "Title": row_utils.get_title(row),
        "URL": row_utils.get_url(row),
        "Original Title": row_utils.get_original_title(row),
        "Year": row_utils.get_year(row),
        "Release Date": row_utils.get_videogames_release_date(row),
        "Picture URL": row_utils.get_picture_url(row),
        "Genre": row_utils.get_videogames_genre(row),
        "Producer": row_utils.get_producer(row),
        "Platforms": row_utils.get_platfoms(row),
        "Description": row_utils.get_description(row),
        "Average Rating": row_utils.get_average_rating(row),
        "Number of Ratings": row_utils.get_number_of_ratings(row),
    }


def get_order_videogames_columns():
    return [
        "Rank",
        "Title",
        "Average Rating",
        "Number of Ratings",
        "URL",
        "Original Title",
        "Year",
        "Release Date",
        "Number of Seasons",
        "Picture URL",
        "Genre",
        "Producer",
        "Description",
    ]
