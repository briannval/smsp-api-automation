from datetime import timedelta

import requests

import config


def date_range(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)


def create_post_body(kpi, current_date):
    if kpi in config.PERIOD_API_ENDPOINTS:
        return {
            "today_date": current_date,
            "rolling_years": config.DEFAULT_ROLLING_YEARS,
            "rolling_months": config.DEFAULT_ROLLING_MONTHS,
            "rolling_days": config.DEFAULT_ROLLING_DAYS,
        }
    return {"today_date": current_date}


def post_to_kpi_api(url, body, kpi, current_date):
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=body, headers=headers)
    if response.status_code == 200:
        print(f"Success for {kpi} on {current_date}")
    else:
        print(f"Failed for {kpi} on {current_date}")
    print(f"Response text: {response.text}")
