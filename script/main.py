if __name__ == "__main__":
    json_file = "/Users/jheongry/Documents/GitHub/billiegene/data/dataset0.json"
    parsed_df = parse_data(json_file)
    aggregated_df = aggregate_data(parsed_df)
    aggregated_df.to_csv('rf_aggregated2.csv', index=False)
    print("Aggregated data saved to 'rf_aggregated2.csv'")