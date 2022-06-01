import pandas as pd

# 1. To know which region had the lowest average price for conventionally grown avocados each year,
#   and know the same information for organic avocados.
# 2. To know which region had the highest average price for both types of avocado for each given year.
# 3. To know the lowest all-time price for both conventionally grown and organic avocados,
#   and to know the highest price as well.


def filter_by_year(df, year):
    return df.query("year == @year").drop(columns="year")


def get_average_by_year(df):
    averages = {}
    years = df.year.unique()

    for year in years:
        averages_for_year = filter_by_year(df, year).groupby("region").mean()
        averages.update(({year: averages_for_year}))

    return averages


def min_max_prices_by_year(avg_dict):
    print("Highest prices and the region by year")
    for year, data in avg_dict.items():
        highest_value = data.price.max()
        location = data.query("price == @highest_value").index[0]
        print(f"{year}: ${highest_value:.2f} in {location}.")
    print()

    print("Lowest prices and the region by year")
    for year, data in avg_dict.items():
        lowest_value = data.price.min()
        location = data.query("price == @lowest_value").index[0]
        print(f"{year}: ${lowest_value:.2f} in {location}.")
    print()


with open("avocado.csv", "r") as avocado_file:
    avo_data = pd.read_csv(avocado_file).rename(columns={"AveragePrice": "price"})

avo_data = avo_data[["year", "region", "price", "type"]]

conventional_prices = avo_data.query("type == 'conventional'").copy()
conventional_prices.drop(columns="type", inplace=True)
conventional_averages = get_average_by_year(conventional_prices)

organic_prices = avo_data.query("type == 'organic'").copy()
organic_prices.drop(columns="type", inplace=True)
organic_averages = get_average_by_year(organic_prices)

print("-" * 100)

print("Conventional Avocados")
min_max_prices_by_year(conventional_averages)

print("-" * 100)

print("Organic Avocados")
min_max_prices_by_year(organic_averages)

print("-" * 100)

# highest and lowest all-time
# conventional
highest_all_time_conventional = conventional_prices.price.max()
print(f"Highest price of conventional avocados of all time: ${highest_all_time_conventional:.2f}")
lowest_all_time_conventional = conventional_prices.price.min()
print(f"Lowest price of conventional avocados of all time: ${lowest_all_time_conventional:.2f}")

# organic
highest_all_time_organic = organic_prices.price.max()
print(f"Highest price of organic avocados of all time: ${highest_all_time_organic:.2f}")
lowest_all_time_organic = organic_prices.price.min()
print(f"Lowest price of organic avocados of all time: ${lowest_all_time_organic:.2f}")

print("-" * 100)
