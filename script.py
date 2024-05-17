from datetime import datetime

import config
import utils

"""
USAGE FOR SMSP ONLY
"""


def main():
    for API_ENDPOINT in config.API_ENDPOINTS:
        print(f"Running for {API_ENDPOINT}")
        for date in utils.date_range(
            config.START_DATE,
            config.END_DATE,
        ):
            date_string = date.strftime("%Y-%m-%d")

            post_body = utils.create_post_body(
                API_ENDPOINT,
                date_string,
            )

            utils.post_to_kpi_api(
                config.LOCALHOST_URL + API_ENDPOINT,  # url
                post_body,  # body result
                API_ENDPOINT,  # endpoint of API
                date_string,  # today_date
            )
        print(f"Ended for {API_ENDPOINT}")


main()
