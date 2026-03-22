import pandas as pd
from data.mock_campaign_data import get_mock_campaign_data


def extract_campaign_data():
    raw_data = get_mock_campaign_data()
    df = pd.DataFrame(raw_data)
    return df