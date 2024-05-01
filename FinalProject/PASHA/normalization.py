import pandas as pd

BRIDGE_POOR = 'Bridges, poor'
BRIDGE_FAIR = 'Bridges, fair'
BRIDGE_GOOD = 'Bridges, good'
TOTAL_BRIDGES = 'Total bridges'

NORMALIZE_BY_TOTAL_BRIDGES_VALUE = 'normalize_by_total_bridges_value'
NORMALIZE_BY_POPULATION_VALUE = 'normalize_by_population_value'


def main():
    df = pd.read_csv('../data/data.csv')
    print(df.head())
    normalize_by_total_bridges(df.copy(deep=True))
    normalize_by_population(df.copy(deep=True))


"""
Normalization by Total Bridges
Objective: This technique aims to normalize the condition of bridges (poor, fair, good) based on the total number of 
    bridges in each county for a given year. This approach helps in understanding the proportion of bridges in each 
    condition relative to the total bridge infrastructure within the same region and time frame.

Method:

Filter Data: The data is filtered to include only the relevant bridge conditions and the total number of bridges.
Group Data: Data is grouped by 'County' and 'Year' to ensure that normalization is contextually relevant.
Compute Total Bridges: For each group, the total number of bridges is computed. If the data is missing, a default 
    value of 1 is used to avoid division by zero, assuming minimal infrastructure presence.
Normalize: Each bridge condition's count is divided by the total number of bridges in the corresponding group. This 
    results in a normalized value representing the fraction of bridges in each condition relative to the total bridges.
"""


def normalize_by_total_bridges(df):
    filter_conditions = [BRIDGE_POOR, BRIDGE_GOOD, BRIDGE_FAIR, TOTAL_BRIDGES]
    df = df[df['Variable'].isin(filter_conditions)]
    df[NORMALIZE_BY_TOTAL_BRIDGES_VALUE] = None

    grouped = df.groupby(['County', 'Year'])
    total_bridges = grouped.apply(lambda x: x.loc[x['Variable'] == TOTAL_BRIDGES, 'Value'].iloc[0] if not x.loc[
        x['Variable'] == TOTAL_BRIDGES, 'Value'].empty else 1)

    # Normalize values
    conditions = [BRIDGE_POOR, BRIDGE_FAIR, BRIDGE_GOOD]
    for condition in conditions:
        df.loc[df['Variable'] == condition, NORMALIZE_BY_TOTAL_BRIDGES_VALUE] = df.apply(
            lambda row: row['Value'] / total_bridges.loc[row['County'], row['Year']] if row[
                                                                                            'Variable'] == condition else
            row[NORMALIZE_BY_TOTAL_BRIDGES_VALUE],
            axis=1)

    df.to_csv(f'../data/{NORMALIZE_BY_TOTAL_BRIDGES_VALUE}.csv', index=False)


"""
Normalization by Population
Objective: This method normalizes the bridge data by the population of the respective county and year. The rationale is
    to understand the bridge conditions in relation to the population size, providing insight into infrastructure
     adequacy or challenges faced by different population sizes.

Method:

Extract Population Data: Population data is identified and extracted based on the 'Demographics' category and
    'Population' description.
Create Population Map: A mapping of population values to each county and year is created for quick reference.
Filter Data: As with the total bridges, the data is filtered to focus only on relevant entries.
Normalize: Bridge conditions are normalized by dividing the number of bridges in each condition by the population of
    the respective county and year. A default population value of 1 is used where data is missing to maintain
     consistency.
"""


def normalize_by_population(df):
    # Extract population data
    population_data = df[(df['Category'] == 'Demographics') & (df['Variable'] == 'Population')]

    # Create a mapping of population to County and Year
    population_map = population_data.set_index(['County', 'Year'])['Value']

    filter_conditions = [BRIDGE_POOR, BRIDGE_GOOD, BRIDGE_FAIR, TOTAL_BRIDGES]
    df = df[df['Variable'].isin(filter_conditions)]

    # Initialize 'Normalized_Value' column
    df[NORMALIZE_BY_POPULATION_VALUE] = None  # Initialize the column with None values

    # Normalize values by population
    conditions = [BRIDGE_POOR, BRIDGE_FAIR, BRIDGE_GOOD, TOTAL_BRIDGES]
    for condition in conditions:
        df.loc[df['Variable'] == condition, NORMALIZE_BY_POPULATION_VALUE] = df.apply(
            lambda row: row['Value'] / population_map.get((row['County'], row['Year']), 1) if row[
                                                                                                  'Variable'] == condition else
            row[NORMALIZE_BY_POPULATION_VALUE],
            axis=1)

    df.to_csv(f'../data/{NORMALIZE_BY_POPULATION_VALUE}.csv', index=False)


if __name__ == "__main__":
    main()
