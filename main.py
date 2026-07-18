"""
================================================================================
                    PANDAS COMPLETE MASTERY HANDBOOK (Part - 07)
                      Advanced Text Parsing & Feature Ingestion
================================================================================

Topics Covered:
---------------
✔ Production File Ingestion Engines (pd.read_csv with Raw String Paths)
✔ Dynamic Feature Extraction Pipelines via Targeted Text Loops
✔ Element-wise String Sanitization Metaprogramming (.str.replace)
✔ Architectural Data Type Casting Configurations (.astype)
✔ Logical Boolean Filtering Matrix Isolations (Max Metric Identifications)
"""

import numpy as np
import pandas as pd

# ==============================================================================
# 1. FILE INGESTION & MASTER ARCHITECTURE DATA SNAPSHOT
# ==============================================================================

print("--- 1. Production Storage File Ingestion ---")

# Ingesting raw local unstructured tabular files using raw string literal 'r' paths
# to bypass operating system escape characters safely
df_anime = pd.read_csv(r'5) Pandas_Anime.csv')

# Inspecting the top 5 records of our initial ingestion matrix
print("\nBase Top 5 Records Grid View:")
print(df_anime.head(5))
"""
Output: 
Base Top 5 Records Grid View:
   Rank                                              Title  Score
0     1  Fullmetal Alchemist: BrotherhoodTV (64 eps)Apr...   9.10
1     2  Steins;GateTV (24 eps)Apr 2011 - Sep 20112,473...   9.07
2     3  Bleach: Sennen Kessen-henTV (13 eps)Oct 2022 -...   9.06
3     4  Gintama°TV (51 eps)Apr 2015 - Mar 2016605,113 ...   9.06
4     5  Shingeki no Kyojin Season 3 Part 2TV (10 eps)A...   9.05
"""

# Verifying individual element positioning values using label-based lookup properties (.loc)
print("\nIsolating Target Row Index 3 Text Data String:")
print(df_anime.loc[3]['Title']) 
# Output: Gintama°TV (51 eps)Apr 2015 - Mar 2016605,113 members


# ==============================================================================
# 2. FEATURE EXTRACTION STAGE 1: EPISODE COUNT SEGMENTATION
# ==============================================================================

print("\n--- 2. Custom Element Text Parsing: Episode Extraction ---")

def extract_episode_metadata(target_text_string):
    """
    Scans a raw unformatted text stream row element to capture and isolate
    the text character sequence nested exclusively inside standard parentheses.
    """
    capture_active = False
    extracted_buffer = ""
    
    for character in target_text_string:
        if character == ')':
            capture_active = False
        if capture_active == True:
            extracted_buffer = extracted_buffer + character
        if character == '(':
            capture_active = True
            
    return extracted_buffer

# Executing structural feature inflation by mapping our custom parser engine
# across the 'Title' Series column lanes using functional element mapping (.apply)
df_anime['Episodes'] = df_anime['Title'].apply(extract_episode_metadata)

print("\nInflated Matrix with Isolated Episode Text Elements:")
print(df_anime[['Title', 'Episodes']].head(5))
"""
Output:
Inflated Matrix with Isolated Episode Text Elements:
                                               Title Episodes
0  Fullmetal Alchemist: BrotherhoodTV (64 eps)Apr...   64 eps
1  Steins;GateTV (24 eps)Apr 2011 - Sep 20112,473...   24 eps
2  Bleach: Sennen Kessen-henTV (13 eps)Oct 2022 -...   13 eps
3  Gintama°TV (51 eps)Apr 2015 - Mar 2016605,113 ...   51 eps
4  Shingeki no Kyojin Season 3 Part 2TV (10 eps)A...   10 eps
"""

# ==============================================================================
# 3. DATA CLEANING & EXPLICIT DTYPE CASTING CONVERSIONS
# ==============================================================================

print("\n--- 3. Element Sanitization & Data Type Casting ---")

# Removing non-numeric string labels via vectorized string character replacements
df_anime['Episodes'] = df_anime['Episodes'].str.replace(" eps", "")

# Converting string metadata representations into pure structural mathematical integers (.astype)
df_anime['Episodes'] = df_anime['Episodes'].astype(int)

print("\nSanitized Numeric Data Frames Type Verification Summary:")
print(df_anime[['Title', 'Episodes']].dtypes)
"""
Output: 
Sanitized Numeric Data Frames Type Verification Summary:
Title       object
Episodes     int64
dtype: object
"""

# ==============================================================================
# 4. ADVANCED PATTERN EXTRACTION: DATE RANGE SEGMENTATION
# ==============================================================================

print("\n--- 4. Complex Feature Isolation: Extracting Time Ranges ---")

def extract_time_metadata(target_text_string):
    """
    Parses unformatted cell strings to isolate the temporal date sequences.
    Finds the closing parenthesis boundary and extracts the tracking date ranges 
    running up to the dynamic 'members' string sequence cutoff point.
    """
    # Locating precise text boundary indices inside the data channel
    parenthesis_close_index = target_text_string.find(')')
    member_keyword_index = target_text_string.find('members')
    
    # If the structural string boundary markers are not detected, return a safe fallback value
    if parenthesis_close_index == -1 or member_keyword_index == -1:
        return np.nan
        
    # Slicing the exact target string subset residing between the structural boundaries
    raw_date_segment = target_text_string[parenthesis_close_index + 1 : member_keyword_index]
    
    # Cleaning up trailing numbers leftover from user count metadata blocks
    cleaned_date_segment = ""
    for character in raw_date_segment:
        # Stop tracking the string immediately if it hits the user membership count digits
        if character.isdigit() and not cleaned_date_segment[-1:].isdigit() and not cleaned_date_segment[-4:].strip().replace("-","").isdigit():
            # Looks ahead to check if the integer belongs to a calendar year string sequence
            pass 
        cleaned_date_segment = cleaned_date_segment + character
        
    # Final trim to eliminate any numeric overflows or structural artifacts
    import re
    # Match patterns like 'Apr 2009 - Jul 2010' specifically, truncating garbage metadata trailing behind it
    date_match = re.search(r'[A-Za-z]{3}\s+\d{4}\s*-\s*[A-Za-z]{3}\s+\d{4}', cleaned_date_segment)
    if date_match:
        return date_match.group(0)
        
    # Secondary match pattern rule for unique single-day movie premiere dates (e.g., 'Jan 2021 - Jan 2021')
    movie_match = re.search(r'[A-Za-z]{3}\s+\d{4}', cleaned_date_segment)
    if movie_match:
        return movie_match.group(0)
        
    return cleaned_date_segment.strip()

# Inflating the DataFrame with the extracted temporal tracking schedules 
df_anime['Time_Range'] = df_anime['Title'].apply(extract_time_metadata)

print("\nDataFrame View with Labeled Clean Matrix Intersections:")
print(df_anime[['Title', 'Episodes', 'Time_Range']].head(5))
"""
Output: 
DataFrame View with Labeled Clean Matrix Intersections:
                                               Title  Episodes           Time_Range
0  Fullmetal Alchemist: BrotherhoodTV (64 eps)Apr...        64  Apr 2009 - Jul 2010
1  Steins;GateTV (24 eps)Apr 2011 - Sep 20112,473...        24  Apr 2011 - Sep 2011
2  Bleach: Sennen Kessen-henTV (13 eps)Oct 2022 -...        13  Oct 2022 - Dec 2022
3  Gintama°TV (51 eps)Apr 2015 - Mar 2016605,113 ...        51  Apr 2015 - Mar 2016
4  Shingeki no Kyojin Season 3 Part 2TV (10 eps)A...        10  Apr 2019 - Jul 2019
"""

# ==============================================================================
# 5. DATA CRITERIA FILTERS: HIGHEST SCORE METRIC IDENTIFICATION
# ==============================================================================

print("\n--- 5. Target Boolean Mask Profiling Queries ---")

# Creating a boolean conditional evaluation array comparing row entries against the max score vector
boolean_maximum_mask = df_anime['Score'] == df_anime['Score'].max()

# Filtering the data frame matrix using the mask vector to isolate target values
highest_rated_anime_titles = df_anime[boolean_maximum_mask]['Title']

print("\nIsolating Title Record Hosting the Maximum Numerical Score Metric:")
print(highest_rated_anime_titles)
"""
Output: 
Isolating Title Record Hosting the Maximum Numerical Score Metric:
0    Fullmetal Alchemist: BrotherhoodTV (64 eps)Apr...
Name: Title, dtype: object
"""



"""
================================================================================
                    PANDAS COMPLETE MASTERY HANDBOOK (Part - 08)
                     Advanced Data Auditing, Filtering, & Sorting
================================================================================

Topics Covered:
---------------
✔ Structural Boundary Diagnostics & Metadata Extraction (.shape, .columns)
✔ High-Performance Sorting Architectures (.sort_values, ascending=False)
✔ Categorical Value Distribution Audits (.value_counts(), .count())
✔ Conditional Positional Slicing Indexing (.nlargest(), .iloc[])
✔ Advanced Missing Vector Profiling (.isna().sum())
✔ Custom String Token Scanning Pipelines (.apply() Vector Optimization)
✔ Multi-Level Regional Condition Segment Filtering (Boolean Mask Unions)
"""

import numpy as np
import pandas as pd

# ==============================================================================
# SETUP: PREPARING MOCK COMPRESSED METRIC DATAFRAME ASSET FOR TESTING
# ==============================================================================


print("--- 1. Ingestion & Initial Boundary Auditing ---")
# Reading unstructured data files using standardized file system ingestion engines

df = pd.read_csv("6) Countries.csv") 

# A. Tracking strict horizontal and vertical dimensional array boundaries (.shape)
print(f"Data Grid Shape Vector: {df.shape}") # Output : Data Grid Shape Vector: (194, 64)

# B. Tracking explicit structural field keys (.columns)
print(f"Extracted Structural Table Features Array: {list(df.columns)}")
"""
Output:
Extracted Structural Table Features Array: ['country', 'country_long', 'currency', 'capital_city', 'region', 'continent', 'demonym', 'latitude', 'longitude', 'agricultural_land', 'forest_area', 'land_area', 'rural_land', 'urban_land', 'central_government_debt_pct_gdp', 'expense_pct_gdp', 'gdp', 'inflation', 'self_employed_pct', 'tax_revenue_pct_gdp', 'unemployment_pct', 'vulnerable_employment_pct', 'electricity_access_pct', 'alternative_nuclear_energy_pct', 'electricty_production_coal_pct', 'electricty_production_hydroelectric_pct', 'electricty_production_gas_pct', 'electricty_production_nuclear_pct', 'electricty_production_oil_pct', 'electricty_production_renewable_pct', 'energy_imports_pct', 'fossil_energy_consumption_pct', 'renewable_energy_consumption_pct', 'co2_emissions', 'methane_emissions', 'nitrous_oxide_emissions', 'greenhouse_other_emissions', 'urban_population_under_5m', 'health_expenditure_pct_gdp', 'health_expenditure_capita', 'hospital_beds', 'hiv_incidence', 'suicide_rate', 'armed_forces', 'internally_displaced_persons', 'military_expenditure_pct_gdp', 'birth_rate', 'death_rate', 'fertility_rate', 'internet_pct', 'life_expectancy', 'net_migration', 'population_female', 'population_male', 'population', 'women_parliament_seats_pct', 'rural_population', 'urban_population', 'press', 'democracy_score', 'democracy_type', 'median_age', 'political_leader', 'title']
"""

# ==============================================================================
# 2. GLOBAL MAXIMUM VALUE METRIC FILTERS
# ==============================================================================

print("\n--- 2. Global Metric Maximum Isolations ---")

"""
Boolean masks identify records matching precise criteria. By comparing a series 
to its absolute maximum value, we filter the dataframe to expose the peak record.
"""

# Generating structural boolean indicator filters mapping maximum population sets
boolean_max_pop_mask = df['population'] == df['population'].max()
print(boolean_max_pop_mask)
'''
Output:
0      False
1      False
2      False
3      False
4      False
       ...  
189    False
190    False
191    False
192    False
193    False
Name: population, Length: 194, dtype: bool
'''

# A. Isolating the complete descriptive horizontal row profile matching the criteria
df_max_pop_record = df[boolean_max_pop_mask]
print("Complete Record for Highest Populated Global Entity:\n", df_max_pop_record)
"""
Output: 
Complete Record for Highest Populated Global Entity:
    country       country_long      currency capital_city         region continent  ... press  democracy_score    democracy_type  median_age  political_leader           title
75   India  Republic of India  Indian rupee    New Delhi  Southern Asia      Asia  ...  1.71             7.23  Flawed democracy        23.9     Narendra Modi  Prime Minister
"""

# B. Extracting targeted text series attributes via single-column lane isolations
peak_country_name = df[boolean_max_pop_mask]['country'].values[0]
peak_capital_city = df[boolean_max_pop_mask]['capital_city'].values[0]

print(f"Isolated Country: {peak_country_name} | Labeled Capital Capital: {peak_capital_city}")
# Output: Isolated Country: India | Labeled Capital: New Delhi


# ==============================================================================
# 3. QUANTILE STRUCTURAL SORTING & SUBSET PROCESSING
# ==============================================================================

print("\n--- 3. Performance Vector Sorting Structures ---")

"""
Sorting rows by a numeric metric arranges data cleanly. By disabling ascending sort,
the highest scores rise to the top, allowing easy extraction of the peak records.
"""

# Re-indexing rows permanently in-place by a target numeric vector in descending layout order
df.sort_values(by='democracy_score', ascending=False, inplace=True)

# Slicing the top 5 records of our sorted framework to extract the target subset lane
top_democracy_entities = df['country'].head(5)
print("Top 5 Countries Sorted by Democratic Index Performance Matrix:\n", top_democracy_entities)
"""
Output: 
Top 5 Countries Sorted by Democratic Index Performance Matrix:
 127         Norway
74         Iceland
164         Sweden
122    New Zealand
46         Denmark
Name: country, dtype: object
"""


# ==============================================================================
# 4. CATEGORICAL CROSS-DISTRIBUTION AUDITS
# ==============================================================================

print("\n--- 4. Categorical Frequency Distribution Profiles ---")

"""
Value count engines summarize unique categorical values. Running mathematical
aggregations on these summary blocks uncovers distribution statistics instantly.
"""

# Calculating unique value distribution frequencies down a target column series
regional_frequency_counts = df['region'].value_counts()
print("Total Item Volume Frequency Distribution Over Regional Groupings:\n", regional_frequency_counts)

# Evaluating the absolute aggregate number of distinct regional group entries
total_distinct_regions = df['region'].value_counts().count()
print(f"Total Isolated Regional Groups Present inside DataFrame: {total_distinct_regions}")
"""
Output: 
Total Item Volume Frequency Distribution Over Regional Groupings:
 region
Western Asia                 17
Eastern Africa               17
Western Africa               16
Southern Europe              15
Caribbean                    13
South America                12
South-Eastern Asia           11
Middle Africa                10
Eastern Europe               10
Northern Europe              10
Southern Asia                 9
Western Europe                9
Central America               8
Northern Africa               6
Southern Africa               5
Eastern Asia                  5
Central Asia                  5
Micronesia                    5
Melanesia                     4
Polynesia                     3
Australia and New Zealand     2
Northern America              2
Name: count, dtype: int64


Total Isolated Regional Groups Present inside DataFrame: 22
"""


# ==============================================================================
# 5. REGIONAL SUBSET MASKING INTERSECTIONS
# ==============================================================================

print("\n--- 5. Regional Mask Intersections ---")

# A. Isolating value distribution frequency totals matching a tracking label string
eastern_europe_count = df['region'].value_counts()['Eastern Europe']
print(f"Total Numerical Volume Frequency Mapping to 'Eastern Europe': {eastern_europe_count}")
# Output: Total Numerical Volume Frequency Mapping to 'Eastern Europe': 10

# B. Generating a boolean condition filter array targeting a specific region string
boolean_eastern_europe_mask = df['region'] == "Eastern Europe"

# C. Extracting complete records and target sub-column attributes matching the condition
df_eastern_europe = df[boolean_eastern_europe_mask]
eastern_europe_countries = df[boolean_eastern_europe_mask]['country']

print("\nExtracted Eastern European Tabular Sub-Matrix Intersection View:\n", df_eastern_europe) 
"""
Output:
Extracted Eastern European Tabular Sub-Matrix Intersection View:
              country          country_long  ...      political_leader           title
43    Czech Republic        Czech Republic  ...          Andrej Babiš  Prime Minister
151  Slovak Republic       Slovak Republic  ...                   NaN             NaN
24          Bulgaria  Republic of Bulgaria  ...         Boyko Borisov  Prime Minister
136           Poland    Republic of Poland  ...    Mateusz Morawiecki  Prime Minister
73           Hungary               Hungary  ...          Viktor Orbán  Prime Minister
139          Romania               Romania  ...        Klaus Iohannis       President
111          Moldova   Republic of Moldova  ...             Ion Chicu  Prime Minister
181          Ukraine               Ukraine  ...    Volodymyr Zelensky       President
14           Belarus   Republic of Belarus  ...  Alexander Lukashenko       President
140           Russia    Russian Federation  ...        Vladimir Putin       President
"""

 
print("\nIsolated Country Series Listing:\n", eastern_europe_countries)
"""
Output: 
Isolated Country Series Listing:
 43      Czech Republic
151    Slovak Republic
24            Bulgaria
136             Poland
73             Hungary
139            Romania
111            Moldova
181            Ukraine
14             Belarus
140             Russia
Name: country, dtype: object
"""

# ==============================================================================
# 6. RELATIVE POSITION POSITION DATA SLICING (.nlargest)
# ==============================================================================

print("\n--- 6. Relational Coordinate Slicing Via nlargest Pipelines ---")

"""
Finding values at specific ranks can trigger indexing errors if rows are out of order.
Combining .nlargest() with position-based slicing (.iloc) isolates specific ranks perfectly.
"""

# Isolating the exact numerical threshold representing the 2nd largest value position
target_second_highest_value = df['population'].nlargest(2).iloc[1]

# Generating a boolean mask tracking row items matching our precise target threshold value
boolean_second_pop_mask = df['population'] == target_second_highest_value

# Extracting the target feature value associated with the verified data record
target_leader_identity = df[boolean_second_pop_mask]['political_leader'].values[0]
print(f"Political Leader of the 2nd Highest Populated Entity (India Reference Check): {target_leader_identity}")
# Output: Political Leader of the 2nd Highest Populated Entity (India Reference Check): Xi Jinping

# ==============================================================================
# 7. NULL MASK FREQUENCY SEARCHES
# ==============================================================================

print("\n--- 7. Missing Value Matrix Profile Tracking ---")

# Mapping an element-wise boolean null verification layout tracking vector (.isna())
print("Element-wise Null Boolean Mask Matrix Tracking:\n", df['political_leader'].isna().head(5))
"""
Output: 
Element-wise Null Boolean Mask Matrix Tracking:
127    False
74     False
164    False
122    False
46     False
Name: political_leader, dtype: bool
"""


# Isolating data segments matching the mask to run rapid record accumulation counts
total_unverified_leaders_count = df[df['political_leader'].isna()]['country'].count()
print(f"Total Tracked Entity Rows Hosting Unverified/Unknown Political Leaders: {total_unverified_leaders_count}")
# Output: Total Tracked Entity Rows Hosting Unverified/Unknown Political Leaders: 7

# ==============================================================================
# 8. STRING TOKEN OPERATIONS VIA CUSTOM MAPPING LOOPS
# ==============================================================================

print("\n--- 8. Text Token Analysis and Pattern Auditing ---")

"""
Standard text loops can use global counters to track patterns across rows.
Pandas processes these cleanly using custom element mapping functions (.apply).
"""

# Initializing global tracking variable assets
global_matching_keyword_counter = 0

def scan_text_token_patterns(target_input_text):
    """
    Evaluates individual row text records to detect target string combinations, 
    updating tracking counters whenever a match is validated.
    """
    global global_matching_keyword_counter
    
    # Standardizing incoming text streams to lowercase to avoid case-sensitivity misses
    if 'republic' in str(target_input_text).lower():
        global_matching_keyword_counter += 1
        
    return target_input_text

# Processing text parsing patterns across columns via functional element mapping (.apply)
df['country_long'].apply(scan_text_token_patterns)
print(f"Total Validated Country Titles Hosting the Token 'republic': {global_matching_keyword_counter}")
# Output: Total Validated Country Titles Hosting the Token 'republic': 125

# ==============================================================================
# 9. DUAL-CONDITIONAL REGIONAL MAX FILTERS
# ==============================================================================

print("\n--- 9. Segmented Intersections: Regional Maximum Filters ---")

"""
To isolate maximum metrics within specific regions, first generate a separate 
regional sub-dataframe. Then, evaluate maximum attributes within that filtered subset.
"""

# A. Isolating a targeted geographic segment to build a regional sub-dataframe
boolean_africa_continent_mask = df['continent'] == 'Africa'
df_african_continent_segment = df[boolean_africa_continent_mask]
print("Isolated Regional African Segment Sub-DataFrame:\n", df_african_continent_segment)
"""
Output: 
Isolated Regional African Segment Sub-DataFrame:
                       country                                  country_long  ...               political_leader                              title
108                 Mauritius                         Republic of Mauritius  ...               Pravind Jugnauth                     Prime Minister
27                 Cabo Verde                        Republic of Cabo Verde  ...                            NaN                                NaN
21                   Botswana                          Republic of Botswana  ...              Mokgweetsi Masisi                          President
155              South Africa                      Republic of South Africa  ...                Cyril Ramaphosa                          President
94                    Lesotho                            Kingdom of Lesotho  ...                    Tom Thabane                     Prime Minister
64                      Ghana                             Republic of Ghana  ...                Nana Akufo-Addo                          President
176                   Tunisia                           Republic of Tunisia  ...                     Kaïs Saïed                          President
118                   Namibia                           Republic of Namibia  ...                   Hage Geingob                          President
146                   Senegal                           Republic of Senegal  ...                     Macky Sall                          President
17                      Benin                             Republic of Benin  ...                  Patrice Talon                          President
192                    Zambia                            Republic of Zambia  ...                    Edgar Lungu                          President
101                    Malawi                            Republic of Malawi  ...                Peter Mutharika                          President
104                      Mali                              Republic of Mali  ...         Ibrahim Boubacar Keïta                          President
168                  Tanzania                   United Republic of Tanzania  ...                  John Magufuli                          President
95                    Liberia                           Republic of Liberia  ...                    George Weah                          President
100                Madagascar                        Republic of Madagascar  ...                Andry Rajoelina                          President
180                    Uganda                            Republic of Uganda  ...                Yoweri Museveni                          President
86                      Kenya                             Republic of Kenya  ...                 Uhuru Kenyatta                          President
115                   Morocco                            Kingdom of Morocco  ...                    Mohammed VI                               King
25               Burkina Faso                                  Burkina Faso  ...     Roch Marc Christian Kaboré                          President
149              Sierra Leone                      Republic of Sierra Leone  ...               Julius Maada Bio                          President
125                   Nigeria                   Federal Republic of Nigeria  ...               Muhammadu Buhari                          President
171                The Gambia                        Republic of The Gambia  ...                   Adama Barrow                          President
39              Côte d'Ivoire                     Republic of Côte d'Ivoire  ...              Alassane Ouattara                          President
116                Mozambique                        Republic of Mozambique  ...                   Filipe Nyusi                          President
107                Mauritania                Islamic Republic of Mauritania  ...         Mohamed Ould Ghazouani                          President
124                     Niger                             Republic of Niger  ...             Mahamadou Issoufou                          President
36                    Comoros                          Union of the Comoros  ...                Azali Assoumani                          President
4                      Angola                   People's Republic of Angola  ...                  João Lourenço                          President
61                      Gabon                             Gabonese Republic  ...              Ali Bongo Ondimba                          President
2                     Algeria       People's Democratic Republic of Algeria  ...           Abdelmadjid Tebboune                          President
51                      Egypt                        Arab Republic of Egypt  ...           Abdel Fattah el-Sisi                          President
57                   Ethiopia       Federal Democratic Republic of Ethiopia  ...                     Abiy Ahmed                     Prime Minister
141                    Rwanda                            Republic of Rwanda  ...                    Paul Kagame                          President
37                      Congo                             Republic of Congo  ...           Denis Sassou Nguesso                          President
29                   Cameroon                          Republic of Cameroon  ...                      Paul Biya                          President
193                  Zimbabwe                          Republic of Zimbabwe  ...             Emmerson Mnangagwa                          President
68                     Guinea                            Republic of Guinea  ...                    Alpha Condé                          President
173                      Togo                              Republic of Togo  ...               Faure Gnassingbé                          President
56                   Eswatini                           Kingdom of Eswatini  ...                     Mswati III                               King
47                   Djibouti                          Republic of Djibouti  ...            Ismaïl Omar Guelleh                          President
54                    Eritrea                              State of Eritrea  ...                 Isaias Afwerki                          President
26                    Burundi                           Republic of Burundi  ...              Pierre Nkurunziza                          President
96                      Libya     Socialist People's Libyan Arab Jamahiriya  ...                Fayez al-Sarraj                     Prime Minister
162                     Sudan                         Republic of the Sudan  ...         Abdel Fattah al-Burhan  Leader of the Sovereignty Council
69              Guinea-Bissau                     Republic of Guinea-Bissau  ...           Umaro Sissoco Embaló                          President
53          Equatorial Guinea                 Republic of Equatorial Guinea  ...  Teodoro Obiang Nguema Mbasogo                          President
32                       Chad                              Republic of Chad  ...                    Idriss Déby                          President
31   Central African Republic                      Central African Republic  ...      Faustin-Archange Touadéra                          President
45            Dem. Rep. Congo              Democratic Republic of the Congo  ...               Félix Tshisekedi                          President
144     São Tomé and Principe  Democratic Republic of São Tomé and Principe  ...              Evaristo Carvalho                          President
148                Seychelles                        Republic of Seychelles  ...                    Danny Faure                          President
156               South Sudan                       Republic of South Sudan  ...            Salva Kiir Mayardit                          President
154                   Somalia                    Somali Democratic Republic  ...              Hassan Ali Khayre                     Prime Minister
"""

# B. Isolating row items matching the maximum value inside the sub-dataframe
boolean_african_peak_pop_mask = df_african_continent_segment['population'] == df_african_continent_segment['population'].max()

# C. Extracting the final targeted row matrix and individual text attribute locations
peak_african_record = df_african_continent_segment[boolean_african_peak_pop_mask]
peak_african_country_name = df_african_continent_segment[boolean_african_peak_pop_mask]['country'].values[0]

print("\nHighest Populated African Entity Row Summary View:\n", peak_african_record)
print(f"\nFinal Isolated Country Target Value: {peak_african_country_name}")
"""
Output: 
Highest Populated African Entity Row Summary View:
      country                 country_long        currency capital_city          region  ... democracy_score democracy_type  median_age  political_leader      title
125  Nigeria  Federal Republic of Nigeria  Nigerian naira        Abuja  Western Africa  ...            4.44  Hybrid regime        13.2  Muhammadu Buhari  President


Final Isolated Country Target Value: Nigeria
"""
