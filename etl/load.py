def load_campaign_data(df, connection):
    if df.empty:
        raise ValueError("DataFrame vazio. Nenhum dado para salvar.")

    df.to_sql(
        name="campaign_performance",
        con=connection,
        if_exists="replace",
        index=False
    )

    df.to_csv("output/campaign_performance.csv", index=False)