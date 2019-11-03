def drop_unused_columns(df):
    # Drop unused columns
    df = df.drop(
        [
            "id",
            "age",
            "age_month",
            "layout",
            "material",
            "direction",
            "neighbor",
            "line_1",
            "station_1",
            "duration_1",
            "line_2",
            "station_2",
            "duration_2",
            "is_bus_2",
            "line_3",
            "station_3",
            "duration_3",
            "is_bus_3",
            "address_1",
            "address_2",
            "address_3",
            "address_1_2",
        ],
        axis=1,
    )
    return df
