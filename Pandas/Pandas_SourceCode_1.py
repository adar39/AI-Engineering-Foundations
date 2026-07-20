"""
================================================================================
                    PANDAS COMPLETE MASTERY HANDBOOK (Part - 01)
                    Introduction to Series & DataFrames
================================================================================

Pandas = Panel Data / Python Data Analysis Library

Why Pandas?
-----------
✔ The premier data manipulation and analysis tool built on top of NumPy.
✔ Introduces key structural objects: Series (1D) and DataFrames (2D tables).
✔ Seamlessly handles heterogeneous data types across columns.
✔ Built-in label-based indexing, alignment, dropping, and boolean slicing.
"""

import numpy as np
import pandas as pd

# ==============================================================================
# 1. PANDAS SERIES: INITIALIZATION AND CUSTOM INDEXING
# ==============================================================================

print("--- 1. Pandas Series Fundamentals ---")

"""
A Series is a one-dimensional labeled array capable of holding any data type. 
It consists of an axis labels array (called index) and the actual data values.
"""

# A. Initializing a Series from a Raw NumPy Array (Default Numeric Indexing)
numpy_raw_data = np.array([2, 4, 1, 6])
default_series = pd.Series(numpy_raw_data)

print("Default Indexed Series:\n", default_series)
"""
Output:
0    2
1    4
2    1
3    6
dtype: int64
"""

# B. Initializing a Series with Custom Explicit String Indices
custom_string_indices = np.array(['a', 'b', 'c', 'd'])
labeled_series = pd.Series(numpy_raw_data, index=custom_string_indices)

print("\nCustom Labeled Series:\n", labeled_series)
"""
Output:
a    2
b    4
c    1
d    6
dtype: int64
"""

# C. Initializing a Series Direct from a Standard Python Dictionary
dictionary_source = {'a': 11, 'b': 12, 'c': 13}
dictionary_series = pd.Series(dictionary_source)

print("\nSeries Built from Dictionary:\n", dictionary_series)
"""
Output:
a    11
b    12
c    13
dtype: int64
"""


# ==============================================================================
# 2. DATAFRAME CREATION MECHANICS: CONSTRUCTORS
# ==============================================================================

print("\n--- 2. DataFrame Construction Blueprints ---")

"""
A DataFrame is a two-dimensional tabular data structure with rows and columns. 
Think of it like an optimized, programmatic SQL table or Excel spreadsheet.
"""

# A. Method 1: Creating a DataFrame from a Dictionary of Aligned Lists
student_dictionary_table = {
    "Name": ["Adar", "Jahid", "Dipto"],
    "ID": [39, 25, 34],
    "CGPA": [3.30, 4.00, 3.70]
}
df_from_dict = pd.DataFrame(student_dictionary_table)

print("DataFrame From Dictionary Structure:\n", df_from_dict)
"""
Output:
    Name  ID  CGPA
0   Adar  39   3.3
1  Jahid  25   4.0
2  Dipto  34   3.7
"""

# B. Method 2: Creating a DataFrame from a Nested List with Explicit Column Headers
student_nested_list = [
    ["Adar", 39, 3.30],
    ["Jahid", 25, 4.00],
    ["Dipto", 34, 3.70]
]
column_headers = ["Name", "ID", "CGPA"] 
df_student_profile = pd.DataFrame(student_nested_list, columns=column_headers)

print("\nDataFrame From Nested List & Custom Column Headings:\n", df_student_profile)
"""
Output:
    Name  ID  CGPA
0   Adar  39   3.3
1  Jahid  25   4.0
2  Dipto  34   3.7
"""


# ==============================================================================
# 3. COLUMN EXTRACTION, SELECTION, AND MUTATION PIPELINES
# ==============================================================================

print("\n--- 3. Column Manipulations and Axis Dropping ---")

# A. Extracting a Sub-DataFrame via Single-Column and Multi-Column Selection List
single_column_selection = df_student_profile["Name"]
print("Isolated Target Columns Selection:\n", single_column_selection)
"""
Output: 
0   Adar   
1  Jahid   
2  Dipto   
"""

multi_column_selection = df_student_profile[["Name", "CGPA"]]
print("Isolated Target Columns Selection:\n", multi_column_selection)
"""
Output:
    Name  CGPA
0   Adar   3.3
1  Jahid   4.0
2  Dipto   3.7
"""

# B. Dynamically Appending/Mutating a New Column Feature
df_student_profile["Age"] = [23, 24, 22]
print("\nDataFrame After Column Feature Inflation:\n", df_student_profile)
"""
Output:
    Name  ID  CGPA  Age
0   Adar  39   3.3   23
1  Jahid  25   4.0   24
2  Dipto  34   3.7   22
"""

# C. Dropping Features: Temporary Copy vs. Inplace Permanent Overwrites
# Using axis=1 explicitly flags target targets as COLUMNS. 
# Using axis=0 explicitly flags targets as ROWS.

# 1. Non-destructive drop (Returns a modified copy, parent layout is unchanged)
df_temporary_drop = df_student_profile.drop('Age', axis=1)
print("\nReturned Copy DataFrame (Age Column Dropped):\n", df_temporary_drop)
print("Parent Target DataFrame (Still Retains Age Column):\n", df_student_profile)

# 2. Destructive drop (Modifies the memory footprint permanently using inplace=True)
df_student_profile.drop('Age', axis=1, inplace=True)
print("\nParent DataFrame After Inplace Dropping (Age Extinguished Permanently):\n", df_student_profile)
"""
Output:
    Name  ID  CGPA
0   Adar  39   3.3
1  Jahid  25   4.0
2  Dipto  34   3.7
"""

# 3. Batch Dropping Multiple Columns Simultaneous
df_multi_dropped = df_student_profile.drop(['ID', 'CGPA'], axis=1)
print("\nBatch Column Drop Execution Output:\n", df_multi_dropped)
"""
Output:
    Name
0   Adar
1  Jahid
2  Dipto
"""

# 4. Row Elimination via Axis Zero
df_row_dropped = df_student_profile.drop(0, axis=0)
print("\nRow Index [0] Dropped Output:\n", df_row_dropped)
"""
Output:
    Name  ID  CGPA
1  Jahid  25   4.0
2  Dipto  34   3.7
"""


# ==============================================================================
# 4. LOCATION INDEXING METRICS (.loc vs .iloc)
# ==============================================================================

print("\n--- 4. Advanced Row Retrieval Operations via loc and iloc ---")

"""
- .loc: Label-Based index selection. Accesses data points using literal named indices/labels.
- .iloc: Integer-Position Based selection. Accesses data points via zero-indexed integer slots.
"""

# A. Label Slicing Row extractions
print("Single Row Extraction Label-Based (.loc[0]):\n", df_student_profile.loc[0])
"""
Output:
Name    Adar
ID        39
CGPA     3.3
Name: 0, dtype: object
"""       

print("\nBatch Multi-Row Label Selection List (.loc[[0, 1]]):\n", df_student_profile.loc[[0, 1]])   # Grabs rows matching index labels 0 and 1
"""
Output:
    Name  ID  CGPA
0   Adar  39   3.3
1  Jahid  25   4.0
"""

# B. Absolute Positional Integer Indexing Row extraction
print("\nAbsolute Integer Position Extraction (.iloc[2]):\n", df_student_profile.iloc[2]) # Grabs the actual 3rd row layout entry
"""
Output:
Name    Dipto
ID         34
CGPA      3.7
Name: 2, dtype: object
"""

# C. Dual-Axis Intersection Selection Queries (Slicing Specific Grid Quadrants)
# Syntax: dataframe.loc[row_labels][column_labels]
sub_grid_intersection = df_student_profile.loc[[1, 2]][["ID", "CGPA"]]
print("\nQuadrant Segment Intersection Lookup Result:\n", sub_grid_intersection)
"""
Output:
    ID  CGPA
1   25   4.0
2   34   3.7
"""


# ==============================================================================
# 5. MULTI-CRITERIA CONDITIONAL FILTERING PIPELINES
# ==============================================================================

print("\n--- 5. Vectorized Multi-Criteria Boolean Filtering ---")

# Constructing a clean composite master dataframe profile
master_table_source = [
    ["Adar", 39, 3.30, 23],
    ["Jahid", 25, 4.00, 24],
    ["Dipto", 34, 3.70, 22]
]
master_column_labels = ["Name", "ID", "CGPA", "Age"] 
df_master_profile = pd.DataFrame(master_table_source, columns=master_column_labels)

# Executing strict vectorized conditional evaluation masking:
# Condition 1: Age metric column must evaluate strictly greater than 23
# Condition 2: CGPA performance column must evaluate strictly greater than 3.5
# Combined with the vector logical AND operator '&'
conditional_mask_filter = (df_master_profile["Age"] > 23) & (df_master_profile["CGPA"] > 3.5)
filtered_data_pipeline  = df_master_profile[conditional_mask_filter]

print("Final Evaluated Data Extraction via Vectorized Masking:\n", filtered_data_pipeline)
"""
Output:
    Name  ID  CGPA  Age
1  Jahid  25   4.0   24
"""


"""
================================================================================
                    PANDAS COMPLETE MASTERY HANDBOOK (Part - 02)
                      Advanced Missing Data Cleaning Engines
================================================================================

Topics Covered:
---------------
✔ Missing Value Detection Systems (.isna, .sum, .any)
✔ Structural Row Elimination Rules (.dropna with dynamic thresholds)
✔ Uniform Blank Overwrites & Value Filling (.fillna)
✔ Smart Target Pipeline Replacements (Column-Specific Mapped Refills)
✔ Analytical Data Imputation Systems (Automated Statistical Means)
"""

import numpy as np
import pandas as pd

# ==============================================================================
# 1. ESTABLISHING THE UNCLEAN TARGET DATAFRAME
# ==============================================================================

# Generating an imperfect sample dataset containing raw NaN values
unclean_data_source = {
    "A": [1, 2, 3, 4, 5],
    "B": [1, 2, 3, 4, 5],
    "C": [1, 2, 3, np.nan, np.nan],
    "D": [1, np.nan, np.nan, np.nan, 5]
}

df_dirty = pd.DataFrame(unclean_data_source)
print("--- 1. Original Unclean Data Profile ---")
print(df_dirty)
"""
Output:
   A  B    C    D
0  1  1  1.0  1.0
1  2  2  2.0  NaN
2  3  3  3.0  NaN
3  4  4  NaN  NaN
4  5  5  NaN  5.0
"""


# ==============================================================================
# 2. MISSING DATA AUDITING & DETECTION SCHEMAS
# ==============================================================================

print("\n--- 2. Auditing Structural Missing Gaps ---")

# A. Element-wise Boolean Mask Generation (.isna)
# Evaluates every matrix grid element, flags missing elements as True
# If NAN, then true
boolean_null_mask = df_dirty.isna()
print("Element-Wise Null Boolean Matrix:\n", boolean_null_mask)
"""
Output:
       A      B      C      D
0  False  False  False  False
1  False  False  False   True
2  False  False  False   True
3  False  False   True   True
4  False  False   True  False
"""

# B. Aggregated Vertical Frequency Metrics (.isna().sum())
# Automatically counts and displays total missing records down column channels
column_null_counts = df_dirty.isna().sum()
print("\nMissing Values Count Quantities Per Column:\n", column_null_counts)
"""
Output:
A    0
B    0
C    2
D    3
dtype: int64
"""

# C. Structural Boolean Existence Verification Flags (.isna().any())
# Instantly alerts engineers if a column profile contains *at least one* blank cell
column_null_presence = df_dirty.isna().any()
print("\nGlobal Null Presence Flag Interceptions:\n", column_null_presence)
"""
Output: 
A    False
B    False
C     True
D     True
dtype: bool
"""


# ==============================================================================
# 3. ROW ELIMINATION WITH DYNAMIC THRESHOLDS (.dropna)
# ==============================================================================

print("\n--- 3. Dropna Elimination Mechanics ---")

# A. Standard Aggressive Drop Execution (Drops row if ANY element is NaN)
df_aggressive_drop = df_dirty.dropna()
print("Aggressive Rows Dropped (Only Pristine Records Kept):\n", df_aggressive_drop)
"""
Output:
   A  B    C    D
0  1  1  1.0  1.0
"""

# B. Using 'thresh' to Control Tolerance Limits
# 'thresh=x' sets a strict condition: rows MUST have at least 'x' NON-NAN elements to survive.

# 1. Lenient Threshold Rule (Requires at least 1 valid data cell to save row)
df_lenient_drop = df_dirty.dropna(thresh=1)
print("\nDropped Rows Using Threshold = 1 (Lenient):\n", df_lenient_drop)
"""
Output:
   A  B    C    D
0  1  1  1.0  1.0
1  2  2  2.0  NaN
2  3  3  3.0  NaN
3  4  4  NaN  NaN
4  5  5  NaN  5.0
"""

# 2. Unattainable Threshold Rule (Row dropped because no row has 5 valid cells)
df_over_strict_drop = df_dirty.dropna(thresh=5)
print("\nDropped Rows Using Threshold = 5 (Impossible Criteria Matrix):\n", df_over_strict_drop)
"""
Output:
Empty DataFrame
Columns: [A, B, C, D]
Index: []
"""


# ==============================================================================
# 4. STATIC & TARGET-MAPPED REPLACEMENT PIPELINES (.fillna)
# ==============================================================================

print("\n--- 4. Data Fillna Imputation Routines ---")

# A. Global Uniform Value Replacement
# Replaces every single encountered NaN value with a single static string fallback
df_blank_filled = df_dirty.fillna("NANA")
print("Globally Substituted Static Strings Layout:\n", df_blank_filled)
"""
Output:
   A  B     C     D
0  1  1   1.0   1.0
1  2  2   2.0  NANA
2  3  3   3.0  NANA
3  4  4  NANA  NANA
4  5  5  NANA   5.0
"""

# B. Precise Target Column Mapping Strategy
# Maps unique fallback replacement configurations cleanly for specific columns
column_replacement_map = {'A': 0, 'B': 100, 'C': 300, 'D': 400}
df_mapped_fill = df_dirty.fillna(value=column_replacement_map)

print("\nPrecisely Mapped Imputation Output:\n", df_mapped_fill)
"""
Output:
   A  B      C      D
0  1  1    1.0    1.0
1  2  2    2.0  400.0
2  3  3    3.0  400.0
3  4  4  300.0  400.0
4  5  5  300.0    5.0
"""


# ==============================================================================
# 5. AUTOMATED STATISTICAL MEAN IMPUTATION
# ==============================================================================

print("\n--- 5. Automated Statistical Performance Mean Imputation ---")

"""
Imputing data with columns' respective statistical averages prevents loss 
of statistical volume while keeping downstream data distributions stable.
"""

# Dynamically calculates mathematical means for each independent numerical column 
# and automatically injects them back directly into matching column missing slots
df_imputed_mean = df_dirty.fillna(df_dirty.mean())

print("Final Automated Analytical Columns Mean Overwrite:\n", df_imputed_mean)
"""
Output:
   A  B    C    D
0  1  1  1.0  1.0
1  2  2  2.0  2.333333 -> Column D Mean Override
2  3  3  3.0  2.333333 -> Column D Mean Override
3  4  4  2.0  2.333333 -> Column C & D Mean Override Mixture
4  5  5  2.0  5.0
"""



"""
================================================================================
                    PANDAS COMPLETE MASTERY HANDBOOK (Part - 03)
                     Data Merging, Concatenation, & Joins
================================================================================

Topics Covered:
---------------
✔ Relational Database Merges (pd.merge: Inner, Outer, Left, Right)
✔ Axis-Based DataFrame Concatenation (pd.concat along Rows and Columns)
✔ Index-Based Data Combining Mechanics (.join engine configurations)
"""

import numpy as np
import pandas as pd

# ==============================================================================
# SETUP: PREPARING THE PRIMARY DATA LAYOUTS
# ==============================================================================

# Creating relational master dictionaries for relational joining models
employees_data = {
    'emp-id': [1, 2, 3, 4, 5],
    'name': ['John', 'Anna', 'Peter', 'Linda', 'Bob'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR']
}
salaries_data = {
    'emp-id': [1, 2, 3, 16, 17],
    'salary': [60000, 80000, 65000, 70000, 90000],
    'bonus': [5000, 10000, 7000, 8000, 12000]
}

df_employees = pd.DataFrame(employees_data)
df_salaries = pd.DataFrame(salaries_data)

print("--- Data Layout Framework Profiles ---")
print("Employees DataFrame (Left):\n", df_employees)
print("\nSalaries DataFrame (Right):\n", df_salaries)


# ==============================================================================
# 1. SQL-STYLE DATABASE MERGING (pd.merge)
# ==============================================================================

print("\n--- 1. Relational Database Merging Mechanics ---")

# A. Default Implicit Intersection Merge (Defaults to inner match on common keys)
df_default_merge = pd.merge(df_employees, df_salaries)
print("Default Merge (Implicit Keys Match):\n", df_default_merge)
"""
Output:
   emp-id   name department  salary  bonus
0       1   John         HR   60000   5000
1       2   Anna         IT   80000  10000
2       3  Peter    Finance   65000   7000
"""

# B. Explicit Inner Merge (how='inner')
# Intersects keys; keeps rows ONLY where the key exists in BOTH DataFrames.
df_inner = pd.merge(df_employees, df_salaries, on="emp-id", how='inner')
print("\nExplicit Inner Merge Match:\n", df_inner)

# C. Full Outer Merge (how='outer')
# Unions keys; retains ALL records from both dataframes, filling mismatches with NaN.
df_outer = pd.merge(df_employees, df_salaries, on="emp-id", how='outer')
print("\nFull Outer Union Merge:\n", df_outer)
"""
Output:
   emp-id   name department   salary    bonus
0       1   John         HR  60000.0   5000.0
...
5      16    NaN        NaN  70000.0   8000.0
6      17    NaN        NaN  90000.0  12000.0
"""

# D. Left Directional Merge (how='left')
# Keeps ALL rows from the Left DataFrame; pulls matching elements from the Right DataFrame.
df_left = pd.merge(df_employees, df_salaries, on="emp-id", how='left')
print("\nLeft Directional Join Merge:\n", df_left)
"""
Output:
   emp-id   name department   salary    bonus
3       4  Linda         IT      NaN      NaN
4       5    Bob         HR      NaN      NaN
"""

# E. Right Directional Merge (how='right')
# Keeps ALL rows from the Right DataFrame; pulls matching elements from the Left DataFrame.
df_right = pd.merge(df_employees, df_salaries, on="emp-id", how='right')
print("\nRight Directional Join Merge:\n", df_right)
"""
Output:
   emp-id   name department  salary  bonus
3      16    NaN        NaN   70000   8000
4      17    NaN        NaN   90000  12000
"""


# ==============================================================================
# 2. AXIS-BASED STRUCTURAL CONCATENATION (pd.concat)
# ==============================================================================

print("\n--- 2. Structural Stacking via pd.concat ---")

"""
pd.concat joins data assets along a specific physical grid axis direction.
- axis=0 (Rows): Stacks tables vertically on top of each other.
- axis=1 (Columns): Aligns tables horizontally side-by-side.
"""

component_a = {
    'A': ['a0', 'a1', 'a3'],
    'B': ['b0', 'b1', 'b3'], 
    'C': ['c0', 'c1', 'c3']
}
component_b = {
    'A': ['a4', 'a5', 'a6'],
    'B': ['b4', 'b5', 'b6'], 
    'C': ['c4', 'c5', 'c6']
}
df_comp1 = pd.DataFrame(component_a)
df_comp2 = pd.DataFrame(component_b)

# A. Vertical Row Stacking (axis=0)
df_v_concat = pd.concat([df_comp1, df_comp2])
print("Vertical Concat Row Stacking (axis=0):\n", df_v_concat)
"""
Output:
    A   B   C
0  a0  b0  c0
...
2  a6  b6  c6
"""

# B. Horizontal Column Alignment Stacking (axis=1)
df_h_concat = pd.concat([df_comp1, df_comp2], axis=1)
print("\nHorizontal Concat Column Stacking (axis=1):\n", df_h_concat)
"""
Output:
    A   B   C   A   B   C
0  a0  b0  c0  a4  b4  c4
1  a1  b1  c1  a5  b5  c5
2  a3  b3  c3  a6  b6  c6
"""


# ==============================================================================
# 3. INDEX-BASED MATRIX MERGING (DataFrame.join)
# ==============================================================================

print("\n--- 3. Labeled Index-Based Join Operations ---")

"""
The .join() method links two DataFrames based primarily on their Index keys 
rather than explicitly named columns. It is cleaner and faster when combining 
datasets that are already aligned by custom indices.
"""

index_data_x = {"Name": ['Alice', 'Bob', 'Charlie']}
index_data_y = {"score": [85, 90, 75]}

df_indexed_x = pd.DataFrame(index_data_x, index=[1, 2, 3])
df_indexed_y = pd.DataFrame(index_data_y, index=[2, 3, 4])

# A. Outer Join Configuration (Combines all indices, fills gaps with NaN)
df_join_outer = df_indexed_x.join(df_indexed_y, how='outer')
print("Index Outer Join Extraction:\n", df_join_outer)
"""
Output:
      Name  score
1    Alice    NaN
2      Bob   85.0
3  Charlie   90.0
4      NaN   75.0
"""

# B. Inner Join Configuration (Keeps only matching index rows)
df_join_inner = df_indexed_x.join(df_indexed_y, how='inner')
print("\nIndex Inner Join Extraction:\n", df_join_inner)
"""
Output:
      Name  score
2      Bob     85
3  Charlie     90
"""



"""
================================================================================
                    PANDAS COMPLETE MASTERY HANDBOOK (Part - 04)
                       Data Aggregations & GroupBy Mechanics
================================================================================

Topics Covered:
---------------
✔ The Split-Apply-Combine Lifecycles (.groupby)
✔ Multi-Axis Structured Aggregations (Grouping via Categorical Columns)
✔ Multi-Level Hierarchical Grouping Pipelines (Multi-Key Grouping Lists)
✔ Descriptive Statistical Summary Metrics (Standalone Aggregations)
✔ Descriptive Matrix Profiling Operations (.agg Mathematical Bundles)
"""

import numpy as np
import pandas as pd

# ==============================================================================
# SETUP: INITIALIZING MASTER TRANSACTION RECORDS
# ==============================================================================

transaction_records = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Store': ['S1', 'S1', 'S2', 'S2', 'S1', 'S2', 'S2', 'S1'],
    'Sales': [100, 200, 150, 250, 120, 180, 200, 300],
    'Quantity': [10, 15, 12, 18, 8, 20, 15, 25],
    'Date': pd.date_range('2023-01-01', periods=8)
}

df_sales_ledger = pd.DataFrame(transaction_records)
print("--- Base Transaction Ledger Profiles ---")
print(df_sales_ledger)
"""
Output:
  Category Store  Sales  Quantity       Date
0        A    S1    100        10 2023-01-01
1        B    S1    200        15 2023-01-02
2        A    S2    150        12 2023-01-03
3        B    S2    250        18 2023-01-04
4        A    S1    120         8 2023-01-05
5        B    S2    180        20 2023-01-06
6        A    S2    200        15 2023-01-07
7        B    S1    300        25 2023-01-08
"""


# ==============================================================================
# 1. GROUPBY ITERATION: DECONSTRUCTING THE SPLIT STAGE
# ==============================================================================

print("\n--- 1. GroupBy Split Validation Loop ---")

"""
When executing .groupby(), Pandas partitions the data rows behind the scenes 
based on matching element keys (Split Phase) before any math calculations run.
"""

# Splitting the master data map using the unique items inside the 'Category' column
grouped_by_category = df_sales_ledger.groupby('Category')

# Iterating across the group engine returns the unique Key (i) and matching Sub-DataFrame (v)
for group_key, sub_dataframe in grouped_by_category:
    print(f"Active Extracted Group Key: [{group_key}]")
    print(sub_dataframe)
    print("-" * 45)
"""
Output:
Active Extracted Group Key: [A]
  Category Store  Sales  Quantity       Date
0        A    S1    100        10 2023-01-01
2        A    S2    150        12 2023-01-03
4        A    S1    120         8 2023-01-05
6        A    S2    200        15 2023-01-07
---------------------------------------------
Active Extracted Group Key: [B]
  Category Store  Sales  Quantity       Date
1        B    S1    200        15 2023-01-02
3        B    S2    250        18 2023-01-04
5        B    S2    180        20 2023-01-06
7        B    S1    300        25 2023-01-08
---------------------------------------------
"""


# ==============================================================================
# 2. SINGLE-COLUMN CATEGORICAL AGGREGATIONS
# ==============================================================================

print("\n--- 2. Single-Column Group Aggregations ---")

"""
Syntax Model: dataframe.groupby('Key_Column')['Target_Value_Column'].math_function()
This extracts specific segments and bundles summaries into a single series vector.
"""

category_sales_totals = df_sales_ledger.groupby('Category')['Sales'].sum()
print("Accumulated Sum of Sales per Category Group:\n", category_sales_totals)
"""
Output:
Category
A    570
B    930
Name: Sales, dtype: int64
"""


# ==============================================================================
# 3. MULTI-LEVEL HIERARCHICAL GROUPING PIPELINES
# ==============================================================================

print("\n--- 3. Multi-Level Hierarchical Grouping ---")

"""
By passing a list of distinct columns into the grouping engine, you generate 
a multi-layered MultiIndex row layout framework tracking combinations across variables.
"""

multi_level_sales_totals = df_sales_ledger.groupby(['Category', 'Store'])['Sales'].sum()
print("Hierarchical Sum of Sales per Category-Store Grid Combination:\n", multi_level_sales_totals)
"""
Output:
Category  Store
A         S1       220
          S2       350
B         S1       500
          S2       430
Name: Sales, dtype: int64
"""


# ==============================================================================
# 4. DATA SERIES MATRICES AND PROFILE MATRICES (.agg)
# ==============================================================================

print("\n--- 4. Standalone and Bundled Aggregation Profiles ---")

# A. Standard isolated analytical operations over flat vectors
flat_sales_average = df_sales_ledger['Sales'].mean()
print(f"Global Mathematical Average Sales Scalar: {flat_sales_average}") # Output: 187.5

# B. Multi-Metric Descriptive Performance Bundles (.agg())
# Passing a list of statistical functions directly computes multiple metrics at once,
# building a comprehensive summary matrix panel from a raw data column.
sales_comprehensive_profile = df_sales_ledger['Sales'].agg(['sum', 'mean', 'min', 'max', 'count', 'std', 'median'])

print("\nComprehensive Bundled Summary Calculations Matrix:\n", sales_comprehensive_profile)
"""
Output:
sum       1500.000000
mean       187.500000
min        100.000000
max        300.000000
count        8.000000
std         66.062741
median     190.000000
Name: Sales, dtype: float64
"""



"""
================================================================================
                    PANDAS COMPLETE MASTERY HANDBOOK (Part - 05)
                        Pivot Tables & Crosstab Engines
================================================================================

Topics Covered:
---------------
✔ DateTime Metadata Extraction Methods (.dt.month_name & .dt.quarter)
✔ Multi-Dimensional Matrix Reshaping via pd.pivot_table()
✔ Custom Operational Aggregations ('median', 'mean' over multiple values)
✔ Categorical Structural Frequency Auditing via pd.crosstab()
"""

import numpy as np
import pandas as pd

# Setting seed value to lock down static synthetic value distributions
np.random.seed(42)

# ==============================================================================
# SETUP: DATETIME INFLATION AND SOURCE DATAFRAME GENERATION
# ==============================================================================

raw_ledger_data = {
    'Date': pd.date_range('2023-01-01', periods=20),
    'Product': ['A', 'B', 'C', 'D'] * 5,
    'Region': ['East', 'West', 'North', 'South'] * 5,
    'Sales': np.random.randint(100, 1000, 20),
    'Units': np.random.randint(10, 100, 20),
    'Rep': ['John', 'Mary', 'Bob', 'Alice'] * 5
}

df_source = pd.DataFrame(raw_ledger_data)

# Extracting temporal string characteristics from Series timestamp elements via .dt accessor
df_source['Month'] = df_source['Date'].dt.month_name()
df_source['Quarter'] = 'Q' + df_source['Date'].dt.quarter.astype(str)

print("--- 1. Inflated Master Dataset View ---")
print(df_source.head(5))
"""
Output: 
--- 1. Inflated Master Dataset View ---
        Date Product Region  Sales  Units    Rep    Month Quarter
0 2023-01-01       A   East    202     31   John  January      Q1
1 2023-01-02       B   West    535     62   Mary  January      Q1
2 2023-01-03       C  North    960     11    Bob  January      Q1
3 2023-01-04       D  South    370     97  Alice  January      Q1
4 2023-01-05       A   East    206     39   John  January      Q1
"""


# ==============================================================================
# 1. THE RESHAPING ENGINE: PANDAS PIVOT TABLES (pd.pivot_table)
# ==============================================================================

print("\n--- 2. Structural Reshaping via Pivot Tables ---")

"""
CRITICAL COMPREHENSION RULES:
-----------------------------
1. 'index':   Determines the row labels of the final reshaped matrix table.
2. 'columns': Determines the column headings of the final reshaped matrix table.
3. 'values':  The target numeric measurement columns being aggregated.
4. 'aggfunc': Mathematical engine used to compress matching data groups (defaults to 'mean').

Data Integrity Requirement:
---------------------------
The column assigned to 'values' must strictly contain numeric data. 
Passing non-numeric columns like strings, names, or text labels into a 
mathematical 'aggfunc' framework will throw an explicit handling Exception.
"""

# A. Reshaping with a Custom Single Aggregation Metric ('median')
pivot_median_sales = pd.pivot_table(
    data=df_source,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="median"
)

print("Pivot Table: Median Sales across Product x Region Matrix:\n", pivot_median_sales)
"""
Output:
Product      A      B      C      D
Region                             
East     537.0    NaN    NaN    NaN
North      NaN    NaN  544.0    NaN
South      NaN    NaN    NaN  562.0
West       NaN  548.0    NaN    NaN

Note: NaN (Not a Number) values represent empty slots where no transactional matching rows 
existed for that specific row/column structural intersection path.
"""

# B. Multi-Value Multi-Layered Dimension Reshaping
# Passing a list of numeric features generates a hierarchically structured multi-index column layout grid
pivot_multi_metric = pd.pivot_table(
    data=df_source,
    values=['Sales', 'Units'],
    index='Region',
    columns='Product',
    aggfunc='mean'
)

print("\nHierarchical Pivot Table: Mean Metrics Matrix Across Product-Region Axises:\n", pivot_multi_metric)
"""
Output:
         Sales                      Units                  
Product      A      B      C      D     A     B     C     D
Region                                                     
East     584.0    NaN    NaN    NaN  44.6   NaN   NaN   NaN
North      NaN    NaN  470.8    NaN   NaN   NaN  53.2   NaN
South      NaN    NaN    NaN  556.8   NaN   NaN   NaN  58.2
West       NaN  554.4    NaN    NaN   NaN  45.4   NaN   NaN
"""


# ==============================================================================
# 2. CATEGORICAL FREQUENCY ANALYSES (pd.crosstab)
# ==============================================================================

print("\n--- 3. Frequency Distribution via Contingency Tables ---")

"""
pd.crosstab() computes a frequency contingency map that displays the raw element 
co-occurrence counts across distinct structural groupings or categories.
"""

# Tabulates interaction event volumes between regions and products
contingency_frequency_matrix = pd.crosstab(
    index=df_source['Region'],
    columns=df_source['Product']
)

print("Frequency Count Crosstab Matrix Allocation:\n", contingency_frequency_matrix)
"""
Output:
Product  A  B  C  D
Region             
East     5  0  0  0
North    0  0  5  0
South    0  0  0  5
West     0  5  0  0
"""



"""
================================================================================
                    PANDAS COMPLETE MASTERY HANDBOOK (Part - 06)
                     Metadata Auditing & Custom Function Mapping
================================================================================

Topics Covered:
---------------
✔ Structural Shape Verification Attributes (.shape)
✔ Information and Memory Overhead Audits (.info())
✔ Summary Distribution Matrices (.describe())
✔ Vectorized Series Column Transformations
✔ Functional Row/Element Custom Transformations (.apply via Vectorized Lambdas)
"""

import numpy as np
import pandas as pd

# ==============================================================================
# SETUP: PREPARING THE CORE METRIC DATAFRAME
# ==============================================================================

# Initializing base aligned analytical data assets
base_metrics_source = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
}

df_metrics = pd.DataFrame(base_metrics_source)
print("--- Base Matrix Entry View ---")
print(df_metrics)
"""
Output:
   A   B    C
0  1  10  100
1  2  20  200
2  3  30  300
3  4  40  400
4  5  50  500
"""


# ==============================================================================
# 1. STRUCTURAL META AUDITING (.shape, .info, .describe)
# ==============================================================================

print("\n--- 1. Structural Meta Auditing Pipelines ---")

# A. Dimensional Boundary Verification Tuple (.shape)
# Returns a strict dimensional count snapshot format: (Total Rows, Total Columns)
print(f"DataFrame Shape Demarcation Boundaries: {df_metrics.shape}") # Output: (5, 3)

# B. Internal System Architecture and Memory Diagnostics Summary (.info())
# Instantly prints structural index ranges, column non-null data volume counts, 
# explicit type assignments (dtypes), and runtime memory block footprints.
print("\nSystem Architecture Diagnostic Summary:")
df_metrics.info()
"""
Output:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   A       5 non-null      int64
 1   B       5 non-null      int64
 2   C       5 non-null      int64
dtypes: int64(3)
memory usage: 252.0 bytes
"""

# C. Summary Distribution Statistical Matrix (.describe())
# Provides key descriptive statistical breakdowns over numeric elements, 
# automatically calculating averages, standard deviations, and quartile cutoffs.
print("\nSummary Distribution Statistical Calculations Matrix:\n", df_metrics.describe())
"""
Output:
              A          B           C
count  5.000000   5.000000    5.000000
mean   3.000000  30.000000  300.000000
std    1.581139  15.811388  158.113883
min    1.000000  10.000000  100.000000
25%    2.000000  20.000000  200.000000
50%    3.000000  30.000000  300.000000
75%    4.000000  40.000000  400.000000
max    5.000000  50.000000  500.000000
"""


# ==============================================================================
# 2. IN-PLACE VECTORIZED ELEMENT BROADCASTING
# ==============================================================================

print("\n--- 2. Vectorized Column Modifications ---")

"""
Just like NumPy arrays, Pandas Series execute vectorized math natively. 
Adding a scalar to a Series broadcasts the operation across all row elements instantly.
"""

# Overwriting existing Column 'A' data elements by broadcasting an addition operation
df_metrics['A'] = df_metrics['A'] + 10

print("Mutated Broadcasted Column 'A' Extraction:\n", df_metrics['A'])
"""
Output:
0    11
1    12
2    13
3    14
4    15
Name: A, dtype: int64
"""


# ==============================================================================
# 3. CUSTOM ELEMENT MAPPING OPERATIONS (.apply via Lambdas)
# ==============================================================================

print("\n--- 3. Custom Function Mapping Engines ---")

"""
The .apply() method lets you run custom data transformations across rows or columns.
When paired with an inline lambda function, it maps a custom operation over each 
element in a data channel without slow, explicit Python loops.
"""

# Generating a new Column 'D' feature vector by isolating Column 'B' elements
# and squaring each value via an inline anonymous lambda function pipeline
df_metrics['D'] = df_metrics["B"].apply(lambda individual_element : individual_element ** 2)

print("Final Mutated DataFrame State Matrix with Custom Mapped Inflation:\n", df_metrics)
"""
Output:
    A   B    C     D
0  11  10  100   100
1  12  20  200   400
2  13  30  300   900
3  14  40  400  1600
4  15  50  500  2500
"""



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
# Output: Isolated Country: India | Labeled Capital Capital: New Delhi


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
