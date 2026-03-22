def transform_campaign_data(df):
    df = df.copy()

    df["CTR"] = df.apply(
        lambda x: x["clicks"] / x["impressions"] if x["impressions"] > 0 else 0,
        axis=1
    )

    df["CPC"] = df.apply(
        lambda x: x["cost"] / x["clicks"] if x["clicks"] > 0 else 0,
        axis=1
    )

    df["CPA"] = df.apply(
        lambda x: x["cost"] / x["conversions"] if x["conversions"] > 0 else 0,
        axis=1
    )

    df["conversion_rate"] = df.apply(
        lambda x: x["conversions"] / x["clicks"] if x["clicks"] > 0 else 0,
        axis=1
    )

    df["ROI"] = df.apply(
        lambda x: ((x["conversions"] * 50) - x["cost"]) / x["cost"] if x["cost"] > 0 else 0,
        axis=1
    )

    return df