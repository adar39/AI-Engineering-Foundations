"""
================================================================================
                     NUMPY COMPLETE MASTERY HANDBOOK (Part - 01)
                           Introduction to NumPy Arrays
================================================================================

NumPy = Numerical Python

Why NumPy?
-----------
✔ Faster than normal Python lists due to contiguous C-level memory storage.
✔ Uses significantly less memory allocations.
✔ Supports native optimized vector operations without loops.
✔ Serves as the absolute structural bedrock for Machine Learning, Data Science,
  Artificial Intelligence, Deep Learning, and Computer Vision frameworks.

Installation:
--------------
pip install numpy

Import & Community Standard Convention:
---------------------------------------
np is the standard alias used across all scientific computation pipelines.
"""

import numpy as np

# ==============================================================================
# 1. NORMAL PYTHON LIST (HETEROGENEOUS STORAGE)
# ==============================================================================

# Python lists are generic containers that can store completely different data types 
# together in memory, adding pointer validation overhead.

a_list = [1, 2, 3.5, "adar"]

print("--- 1. Python List Example ---")
print("Python List Content:")
print(a_list)

print("\nIndividual Data Types Inside List:")
print(type(a_list[0]), type(a_list[1]), type(a_list[2]), type(a_list[3]))

"""
Output:
-------
Python List Content:
[1, 2, 3.5, 'adar']

Individual Data Types Inside List:
<class 'int'> <class 'int'> <class 'float'> <class 'str'>
"""


# ==============================================================================
# 2. NUMPY ARRAY (HOMOGENEOUS STRUCTURE & COERCION RULES)
# ==============================================================================

"""
The Golden Homogeneity Rule:
----------------------------
A NumPy array stores ONLY one single uniform data type.

If different data types are provided simultaneously to np.array(), NumPy will 
automatically run type coercion/upcasting to implicitly convert all elements 
to a single common compatible data type.
"""

a_array = np.array([1, 2, 3.5, "adar"])

print("\n--- 2. NumPy Array Homogeneity Coercion ---")
print("NumPy Array Content:")
print(a_array)

print("\nCoerced Data Types:")
print(type(a_array[0]), type(a_array[1]), type(a_array[2]), type(a_array[3]))

"""
Output:
-------
NumPy Array Content:
['1' '2' '3.5' 'adar']

Coerced Data Types:
<class 'numpy.str_'> <class 'numpy.str_'> <class 'numpy.str_'> <class 'numpy.str_'>

Explanation:
------------
Because one element is an explicit string ("adar"), NumPy dynamically converts
every numerical element into a uniform string type ('numpy.str_') to guarantee
contiguous structure layout benefits.
"""


# ==============================================================================
# COMPREHENSIVE COMPARISON: PYTHON LIST VS NUMPY ARRAY
# ==============================================================================

"""
Python List
------------
✔ Can store multiple completely unrelated data types together.
✔ Slower execution speeds due to non-contiguous object pointer scattering.
✔ More total memory consumption footprint.
✔ General-purpose system data collection container.

NumPy Array
------------
✔ Stores exactly one single uniform structural data type.
✔ Highly optimized vectorized processing speeds.
✔ Significantly less memory usage footprint.
✔ Highly engineered for pure raw numerical computation loops.
"""


# ==============================================================================
# 3. UNDERSTANDING DIMENSIONS: VECTORS (1D ARRAYS)
# ==============================================================================

"""
Definition:
-----------
A Vector is a one-dimensional (1D) array structure.

Mathematical Notation:
----------------------
Vector = (x₁, x₂, x₃, ..., xₙ)

Machine Learning Real-World Representation:
------------------------------------------
Feature maps, weights, and input variable vectors are standardly represented 
using 1D NumPy arrays.
"""

vector = np.array([10, 20, 30])

print("\n--- 3. One-Dimensional Vector Output ---")
print("Vector:")
print(vector)

"""
Output:
-------
Vector:
[10 20 30]

Dimension Structural Blueprint:
------------------------------
Dimension count : 1D
Shape tuple     : (n,)     -> Example: (3,)
Example layout  : [1, 2, 3]
"""


# ==============================================================================
# 4. UNDERSTANDING DIMENSIONS: MATRICES (2D ARRAYS)
# ==============================================================================

"""
Definition:
-----------
A Matrix is a two-dimensional (2D) array arranged into explicit Rows x Columns.

Example Structural Grid:
------------------------
[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]

Structural breakdown:
Rows Count    = 3
Columns Count = 3
Target Shape  = (3, 3)
"""

matrix_raw_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n--- 4. Two-Dimensional Matrix Representation ---")
print("Normal Python Matrix Representation:")
print(matrix_raw_list)

matrix_numpy = np.array(matrix_raw_list)

print("\nConverted NumPy Matrix Output:")
print(matrix_numpy)

"""
Output:
-------
Normal Python Matrix Representation:
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Converted NumPy Matrix Output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Dimension Structural Blueprint:
------------------------------
Dimension count : 2D
Shape tuple     : (rows, columns) -> Example: (3, 3)
Example layout  : [[1 2]
                   [3 4]]
"""


# ==============================================================================
# 5. INITIALIZATION ROUTINES & BUILT-IN DATA GENERATORS
# ==============================================================================

print("\n--- 5. Built-in Array Generators ---")

# A. np.arange(start, stop, step) -> stop value is strictly exclusive
b_range = np.arange(1, 11, 2)
print("np.arange(1, 11, 2) Output:", b_range)
# Output: [1 3 5 7 9]

# B. Initializing 1D Placeholders (zeros and ones)
z1 = np.zeros(5)
o1 = np.ones(4)
print("1D Zeros Array:", z1)
print("1D Ones Array:", o1)
"""
Output: 
1D Zeros Array: [0. 0. 0. 0. 0.] 
1D Ones Array: [1. 1. 1. 1.]
"""
 
# C. Initializing 2D Placeholders (zeros and ones via tuple dimensions)
z2 = np.zeros((3, 4))
o2 = np.ones((4, 3))
print("2D Zeros Array (3,4):\n", z2)
print("2D Ones Array (4,3):\n", o2)
"""
Output:
2D Zeros Array (3,4): 
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]

2D Ones Array (4,3):
 [[1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]
  [1. 1. 1.]]
"""

# D. np.linspace(start, stop, total_samples) -> Creates evenly separated fractional arrays
arr_linspace = np.linspace(0, 1, 10)
print("np.linspace(0, 1, 10) Output:\n", arr_linspace)
"""
Output: 
[0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556
 0.66666667 0.77777778 0.88888889 1.        ]
"""


# ==============================================================================
# 6. RANDOM DISTRIBUTION MODULE MECHANICS (np.random)
# ==============================================================================

print("\n--- 6. Random Distribution Generations ---")

# A. np.random.rand(n) -> Uniform Distribution values across range interval [0.0, 1.0)
r_rand = np.random.rand(10)
print("Uniform Random Distribution (rand):\n", r_rand)
"""
Sample Output: 
Uniform Random Distribution (rand):
[0.6546978  0.04831917 0.46087693 0.62757427 0.28907373 0.70612929
 0.15811973 0.25587871 0.74017266 0.94991956]
"""

# B. np.random.randn(n) -> Standard Normal/Gaussian Distribution values (Mean=0, Std=1)
r_randn = np.random.randn(10)
print("Standard Normal Distribution (randn):\n", r_randn)
"""
Sample Output:
Standard Normal Distribution (randn): 
[-1.55141137  0.18434036 -0.27196987  0.36330761 -1.573442    0.63949546
 -1.0751431   1.96990055  0.28587829 -1.31326601]
"""

# C. np.random.randint(low, high) -> Returns a single random baseline integer scalar
r_int_single = np.random.randint(10, 20)
print("Single Isolated Random Integer:", r_int_single)
# Sample Output: Single Isolated Random Integer: 15

# D. np.random.randint(low, high, total_size) -> Returns an array filled with random integers
r_int_array = np.random.randint(10, 20, 10)
print("Random Integer Array Sequence:", r_int_array)
# Sample Output: Random Integer Array Sequence: [14 11 14 12 14 12 14 19 13 11]


# ==============================================================================
# 7. STRUCTURAL ATTRIBUTES, STATISTICAL REDUCTIONS, & RESHAPING
# ==============================================================================

print("\n--- 7. Array Attributes & Analytical Operations ---")

# Setup Base Matrix
arr_base = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Base Matrix Target Layout:\n", arr_base)
"""
Sample Output: 
Base Matrix Target Layout:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

# Structural Matrix Attributes
print("Matrix Shape Attribute (.shape):", arr_base.shape) # Output: (3, 3)
print("Matrix Total Size Count (.size):", arr_base.size)  # Output: 9
print("Matrix Internal Data Type (.dtype):", arr_base.dtype) # Output: int64 (or int32 depending on system architectures)

# Built-in Analysis Methods
print("Minimum Value Found (.min()):", arr_base.min())     # Output: 1
print("Maximum Value Found (.max()):", arr_base.max())     # Output: 9
print("Cumulative Grand Sum (.sum()):", arr_base.sum())     # Output: 45
print("Arithmetic Mean (.mean()):", arr_base.mean())       # Output: 5.0
print("Standard Deviation (.std()):", arr_base.std())         # Output: 2.581988897471611
print("Index Position of Max (.argmax()):", arr_base.argmax()) # Output: 8 (Flattened Index reference mapping)
print("Index Position of Min (.argmin()):", arr_base.argmin()) # Output: 0 (Flattened Index reference mapping)

# Axis-Specific Matrix Transformations
# axis=1 maps operations horizontally (Summing along rows)
print("Horizontal Sum across Rows (axis=1):", np.sum(arr_base, axis=1)) # Output: [ 6 15 24]
# axis=0 maps operations vertically (Summing down columns)
print("Vertical Sum down Columns (axis=0):", np.sum(arr_base, axis=0)) # Output: [12 15 18]

# Reshaping Data Dimensions
# Total item count must always evaluate identically when reshaping structural configurations.
arr_flat = np.arange(5, 35)
print("\nOriginal 1D Vector Block (Size 30):\n", arr_flat)
"""
Output: [ 5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34]
"""

arr_grid = arr_flat.reshape(6, 5)
print("Reshaped 2D Matrix (6 Rows x 5 Columns):\n", arr_grid)
"""
Output: 
Reshaped 2D Matrix (6 Rows x 5 Columns):
[[ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]
 [25 26 27 28 29]
 [30 31 32 33 34]]
"""


# ==============================================================================
# 8. INDEXING AND SLICING TECHNIQUES (1D VECTORS)
# ==============================================================================

print("\n--- 8. 1D Vector Indexing and Slicing ---")

arr_vec = np.arange(11, 21)
print("Target 1D Array Sequence:\n", arr_vec)
# Output: [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print("Slice [3:8]:", arr_vec[3:8])   # Index 3 to index 7 -> Output: [14 15 16 17 18]
print("Slice [:5]:", arr_vec[:5])    # Start to index 4   -> Output: [11 12 13 14 15]
print("Slice [3:]:", arr_vec[3:])    # Index 3 to the end -> Output: [14 15 16 17 18 19 20]
print("Slice [3::2]:", arr_vec[3::2]) # Index 3 to end step 2 -> Output: [14 16 18 20]


# ==============================================================================
# 9. ADVANCED MULTI-DIMENSIONAL INDEXING AND SLICING (2D MATRICES)
# ==============================================================================

print("\n--- 9. 2D Matrix Indexing and Slicing ---")

arr_matrix_source = np.arange(1, 31).reshape(6, 5)
print("Target Reference Matrix Layout (6,5):\n", arr_matrix_source)
"""
Sample Output:
Target Reference Matrix Layout (6,5):
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]
 [26 27 28 29 30]]
"""

# Extracting a whole unique horizontal index line row block
print("Extract Row 5 (arr[5]):", arr_matrix_source[5]) # Output: [26 27 28 29 30]

# Extracting a solitary scalar coordinate intercept value: matrix[row, column]
print("Extract Specific Intercept (arr[2, 3]):", arr_matrix_source[2, 3]) # Output: 14

# Slicing a specific Sub-Matrix section layout block
print("Sub-Matrix Slice Window (arr[0:2, 1:3]):\n", arr_matrix_source[0:2, 1:3])
"""
Sample Output:
Sub-Matrix Slice Window (arr[0:2, 1:3]): 
[[2 3]
 [7 8]]
"""

# Slicing bottom corner boundary structures
print("Corner Sub-Matrix Slice (arr[3:, 3:]):\n", arr_matrix_source[3:, 3:])
"""
Sample Output: 
Corner Sub-Matrix Slice (arr[3:, 3:]):
[[19 20]
 [24 25]
 [29 30]]
"""

# Extracting a standalone distinct structural vertical column strip
print("Extract Single Vertical Column (arr[:, 2]):", arr_matrix_source[:, 2])
# Output: [ 3  8 13 18 23 28]


# ==============================================================================
# 10. BOOLEAN INDEXING PIPELINES (CONDITIONAL DATA FILTERING)
# ==============================================================================

print("\n--- 10. Logical Masking & Boolean Indexing ---")

arr_filter_target = np.arange(11, 21)
print("Target Array Sequence for filtering:\n", arr_filter_target) 
# Output: [11 12 13 14 15 16 17 18 19 20]

# Generating the logical evaluating mask (Evaluates true if item mod 2 matches 0)
bool_index_mask = arr_filter_target % 2 == 0
print("Generated Boolean Logical Mask:\n", bool_index_mask)
# Output: [False  True False  True False  True False  True False  True]

# Injecting conditions natively as array indices to extract matching positions
arr_filtered_output = arr_filter_target[bool_index_mask]
print("Final Filtered Matrix Elements Output:", arr_filtered_output)
# Output: [12 14 16 18 20]



"""
================================================================================
                    NUMPY COMPLETE MASTERY HANDBOOK (Part - 02)
                        Advanced Array Operations & Mechanics
================================================================================

Topics Covered:
---------------
✔ Element-wise Arithmetic Operations
✔ NumPy Broadcasting Mechanics (vs. Python Loop Overheads)
✔ Memory Reference View Assignment vs. Deep Object Copying
✔ Matrix Multiplication Rules (Element-wise vs. Dot Product)
✔ Matrix Transposition
✔ Structural Joining: Vertical, Horizontal, and Column Stacking
✔ Structural Slicing: Horizontal and Vertical Array Splitting
"""
# ==============================================================================
# 1. ELEMENT-WISE ARITHMETIC OPERATIONS
# ==============================================================================

print("--- 1. Element-wise Arithmetic Operations ---")

# Initializing primary data arrays
array_alpha = np.array([1, 2, 3, 4, 5])
array_beta  = np.array([6, 7, 8, 9, 10])

# Native arithmetic operations apply instantly to matching index positions
print("Addition (+):      ", array_alpha + array_beta)   # Output: [ 7  9 11 13 15]
print("Subtraction (-):   ", array_alpha - array_beta)   # Output: [-5 -5 -5 -5 -5]
print("Multiplication (*):", array_alpha * array_beta)   # Output: [ 6 14 24 36 50]
print("Division (/):      ", array_alpha / array_beta)   # Output: [0.16666667 0.28571429 0.375 0.44444444 0.5]
print("Floor Division (//):", array_alpha // array_beta) # Output: [0 0 0 0 0]
print("Exponentiation (**):", array_alpha ** array_beta) # Output: [1 128 6561 262144 9765625]


# ==============================================================================
# 2. NUMPY BROADCASTING MECHANICS
# ==============================================================================

print("\n--- 2. NumPy Broadcasting Operations ---")

"""
Broadcasting describes how NumPy treats arrays with different shapes during 
arithmetic operations. Subject to certain constraints, the smaller array is 
'broadcast' across the larger array so that they have compatible shapes.
"""

# A. Standard Python Loop Approach (High Overhead, Slow)
python_list = [1, 2, 3, 4, 5]
for index in range(0, len(python_list)):
    python_list[index] = python_list[index] + 10
print("Python Loop Output:        ", python_list) 
# Output: [11, 12, 13, 14, 15]

# B. NumPy Vectorized Broadcasting Approach (Highly Optimized, Fast)
numpy_list_array = np.array([1, 2, 3, 4, 5])
numpy_list_array = numpy_list_array + 10  # The scalar value 10 is stretched/broadcasted
print("NumPy Broadcasted Vector:  ", numpy_list_array) 
# Output: [11 12 13 14 15]

# C. Multi-Dimensional Array Broadcasting
# Stretches the scalar value 10 across all structural rows and columns simultaneously
matrix_grid = np.arange(1, 31).reshape(5, 6)
matrix_grid_broadcasted = matrix_grid + 10
print("\nReshaped 2D Matrix Broadcasted (+10):\n", matrix_grid_broadcasted)
"""
Sample Output: 
Reshaped 2D Matrix Broadcasted (+10):
[[11 12 13 14 15 16]
 [17 18 19 20 21 22]
 [23 24 25 26 27 28]
 [29 30 31 32 33 34]
 [35 36 37 38 39 40]]
"""


# ==============================================================================
# 3. MEMORY MANAGEMENT: SLICES, SHARED REFERENCES, AND DEEP COPIES
# ==============================================================================

print("\n--- 3. Memory Allocation: References vs. Deep Copies ---")

# A. Temporary Slice Evaluations
source_array = np.arange(1, 20)
print("Base Source Array:\n", source_array)

array_slice = source_array[:5]
array_slice = array_slice + 10 
print("Evaluated Isolated Slice (+10):", array_slice) # Output: [11 12 13 14 15]

# Inline evaluations do not alter the root values if reassigned safely
print("Inline Operation Evaluation:   ", source_array[4:6] * 10) # Output: [50 60]
print("Source Array Verification:      ", source_array) 
# Output unchanged: [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]

# B. Shared Reference Assignment (Shallow View Pointer)
# Warning: Modifying the view variable directly alters the parent storage container array
shared_view_reference = source_array
shared_view_reference[0] = 99

print("\nModified Shared Reference View:", shared_view_reference)
print("Parent Source Array (ALTERED): ", source_array)
# Both show 99 at index position 0 because they point to the exact same block in memory.

# C. Deep Object Copy Allocation (.copy())
# Safe approach: Disconnects memory addresses completely to build a standalone array object
independent_copy_array = source_array.copy()
independent_copy_array[0] = 55

print("\nModified Independent Copy Array:", independent_copy_array) # Index 0 becomes 55
print("Parent Source Array (UNTOUCHED):", source_array)           # Index 0 remains 99


# ==============================================================================
# 4. MATRIX MULTIPLICATION MECHANICS & TRANSPOSITION
# ==============================================================================

print("\n--- 4. Matrix Multiplication and Transposition ---")

# Initialize basic test matrices
matrix_factor_a = np.arange(1, 5).reshape(2, 2)
matrix_factor_b = np.arange(5, 9).reshape(2, 2)

print("Matrix Factor A:\n", matrix_factor_a) # [[1 2], [3 4]]
print("Matrix Factor B:\n", matrix_factor_b) # [[5 6], [7 8]]

# A. Element-wise Multiplication (Hadamard Product)
# Warning: This simply multiplies elements occupying matching position coordinates (* operator)
print("\nElement-wise Matrix Multiplication (Hadamard):\n", matrix_factor_a * matrix_factor_b)
"""
Output: 
[[ 5 12]
 [21 32]]
"""

# B. True Linear Algebra Matrix Dot Product
# Uses row-by-column combinations. Use either the '@' operator or 'np.dot()'
print("\nTrue Matrix Dot Product (@ Operator):\n", matrix_factor_a @ matrix_factor_b)
print("True Matrix Dot Product (np.dot):\n", np.dot(matrix_factor_a, matrix_factor_b))
"""
Output for both: 
[[19 22]
 [43 50]]
"""

# C. Matrix Transposition (.T)
# Flips columns to rows and rows to columns across the diagonal axis line
print("\nTransposed Matrix Factor A (.T):\n", matrix_factor_a.T)
"""
Output: 
[[1 3]
 [2 4]]
"""


# ==============================================================================
# 5. STRUCTURAL COMBINATIONS (STACKING MECHANICS)
# ==============================================================================

print("\n--- 5. Matrix Stacking Configurations ---")

# Set up vector components
vector_omega = np.arange(1, 5) # [1 2 3 4]
vector_psi   = np.arange(5, 9) # [5 6 7 8]

# A. Vertical Stacking (np.vstack) -> Combines arrays vertically as rows
vertical_stack_result = np.vstack((vector_omega, vector_psi))
print("Vertical Stack Layout (np.vstack):\n", vertical_stack_result)
"""
Output:
Vertical Stack Layout (np.vstack): 
[[1 2 3 4]
 [5 6 7 8]]
"""

# B. Horizontal Stacking (np.hstack) -> Links sequences end-to-end flatly
horizontal_stack_result = np.hstack((vector_omega, vector_psi))
print("Horizontal Stack Layout (np.hstack):", horizontal_stack_result) 
# Output: Horizontal Stack Layout (np.hstack): [1 2 3 4 5 6 7 8]

# C. Column Stacking (np.column_stack) -> Pairs matching index sequences side-by-side as distinct columns
column_stack_result = np.column_stack((vector_omega, vector_psi))
print("Column Stack Layout (np.column_stack):\n", column_stack_result)
"""
Output: 
Column Stack Layout (np.column_stack):
[[1 5]
 [2 6]
 [3 7]
 [4 8]]
"""


# ==============================================================================
# 6. STRUCTURAL SEGREGATION (ARRAY SPLITTING MECHANICS)
# ==============================================================================

print("\n--- 6. Array Splitting Operations ---")

# Setup Base Multi-Dimensional Data Matrix
split_source_matrix = np.arange(16).reshape(4, 4)
print("Target Matrix for Splitting (4,4):\n", split_source_matrix)
"""
Output: 
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
"""

# A. Horizontal Splitting (np.hsplit) -> Cuts columns vertically, segmenting data sections horizontally
print("\nHorizontal Split Segments (np.hsplit into 4 sections):")
horizontal_split_slices = np.hsplit(split_source_matrix, 4)
for position, data_slice in enumerate(horizontal_split_slices):
    print(f"Slice Section [{position}]:\n", data_slice)
"""
Output:
Slice Section [0]:
 [[ 0]
  [ 4]
  [ 8]
  [12]]
 ... up to Section [3]
"""

# B. Vertical Splitting (np.vsplit) -> Cuts across rows, creating segmented row stacking layouts
print("\nVertical Split Segments (np.vsplit into 2 sections):")
vertical_split_slices = np.vsplit(split_source_matrix, 2)
for position, data_slice in enumerate(vertical_split_slices):
    print(f"Slice Section [{position}]:\n", data_slice)
"""
Output: 
Slice Section [0]:
 [[0 1 2 3]
  [4 5 6 7]]
Slice Section [1]:
 [[ 8  9 10 11]
  [12 13 14 15]]
"""



"""
================================================================================
                    NUMPY COMPLETE MASTERY HANDBOOK (Part - 03)
                     Advanced Data Cleaning & Logical Pipelines
================================================================================

Topics Covered:
---------------
✔ Handling Missing Data and Infinity Values (NaN & Inf)
✔ Conditional Element Mapping via Vectorized Logic (np.where)
✔ Complex Multi-Condition Logic Masking (&, |, ~)
✔ Identification Pipelines (np.unique, np.any, np.all)
✔ Positional Index Sorting and Data Reordering (np.sort & np.argsort)
"""

import numpy as np

# ==============================================================================
# 1. THE IMPERFECT DATA TOOLKIT: MANAGING NaN AND INF VALUES
# ==============================================================================

print("--- 1. Handling Missing Data (NaN) and Infinity (Inf) ---")

"""
Real-world datasets frequently contain broken data metrics:
- np.nan: 'Not a Number' (used as a placeholder for missing or corrupt data).
- np.inf: Representing infinite values (e.g., resulting from division by zero).

Warning: Standard aggregations like .sum() or .mean() will fail and return 'nan' 
if the array contains a single NaN value. Special 'nan-safe' operations must be used.
"""

corrupt_dataset = np.array([10.0, 20.0, np.nan, 40.0, np.inf])
print("Raw Corrupt Dataset Collection:", corrupt_dataset)

# Detecting missing or extreme scalar locations via boolean check masks
print("Is there a NaN element present? ", np.isnan(corrupt_dataset))
print("Is there an Inf element present?", np.isinf(corrupt_dataset))

# Isolating data by dropping missing entries completely using inverted boolean masking
clean_data_mask = ~np.isnan(corrupt_dataset) & ~np.isinf(corrupt_dataset)
print("Filtered Completely Clean Data: ", corrupt_dataset[clean_data_mask])

# Executing Nan-Safe Aggregations
nan_array = np.array([5, 10, np.nan, 15])
print("\nStandard Mean on NaN array (Fails): ", nan_array.mean())    # Output: nan
print("Nan-Safe Mean Aggregation (Succeeds):", np.nanmean(nan_array)) # Output: 10.0


# ==============================================================================
# 2. VECTORIZED CONDITIONALS VIA np.where()
# ==============================================================================

print("\n--- 2. Conditional Mapping Using np.where ---")

"""
np.where() works exactly like an optimized ternary expression or an 'if-else' switch:
Syntax: np.where(condition, value_if_true, value_if_false)
"""

raw_scores = np.array([45, 82, 61, 30, 95, 74])

# Dynamically map all values to categorical string labels based on a condition
grade_labels = np.where(raw_scores >= 60, "PASS", "FAIL")

print("Original Raw Test Scores:", raw_scores)
print("Vectorized Class Grading: ", grade_labels)
# Output: ['FAIL' 'PASS' 'PASS' 'FAIL' 'PASS' 'PASS']

# Use Case B: Keep original element values if true, otherwise cap values at a lower boundary
clamped_scores = np.where(raw_scores >= 50, raw_scores, 50)
print("Clamped Scores (Floor 50):", clamped_scores)


# ==============================================================================
# 3. ADVANCED MULTI-CRITERIA CONDITIONAL MASKING
# ==============================================================================

print("\n--- 3. Multi-Criteria Conditional Masking ---")

"""
When writing conditions over full NumPy structures, standard Python keywords 
(and, or, not) do not function because they assess truthiness for the whole object.
Instead, use bitwise vectorized logical operations:
- &  = Logical AND
- |  = Logical OR
- ~  = Logical NOT
"""

age_metrics = np.array([12, 25, 42, 19, 65, 31, 8])

# Extract elements that are greater than or equal to 18 AND strictly less than 60
adult_mask = (age_metrics >= 18) & (age_metrics < 60)
print("Extracted Active Adult Ages:", age_metrics[adult_mask]) 
# Output: [25 42 19 31]


# ==============================================================================
# 4. GLOBAL IDENTIFICATION AND TRUTH-VALUE PIPELINES
# ==============================================================================

print("\n--- 4. Global Structural Inspections ---")

experimental_trials = np.array([5, 5, 2, 8, 2, 9, 5, 12, 8])

# A. Extract unique occurrences and value frequencies
unique_elements, element_frequencies = np.unique(experimental_trials, return_counts=True)
print("Unique Items Found inside Data: ", unique_elements)     # Output: [ 2  5  8  9 12]
print("Matching Count Item Frequencies:", element_frequencies) # Output: [2 3 2 1 1]

# B. Truth-Value Evaluation Rules
binary_evaluations = np.array([False, True, False, False])

print("Are ANY evaluations True inside the structure? ", np.any(binary_evaluations)) # Output: True
print("Are ALL evaluations True inside the structure?", np.all(binary_evaluations))  # Output: False


# ==============================================================================
# 5. DATA REORDERING MECHANICS: SORT VS ARG_SORT
# ==============================================================================

print("\n--- 5. Positional Value Sorting Routines ---")

# Setup unorganized array target
unord_vector = np.array([80, 20, 50, 10, 90])

# A. Standard Sorting (Returns a new sorted copy of values)
sorted_vector = np.sort(unord_vector)
print("Directly Sorted Values Output:", sorted_vector) # Output: [10 20 50 80 90]

# B. Index Sorting Positional Extraction via np.argsort()
"""
CRITICAL CONCEPT: np.argsort() does not sort values directly. Instead, it returns 
the index locations of the elements in the order they would appear if sorted.
This is highly useful for matching items across different aligned datasets.
"""
sorting_index_positions = np.argsort(unord_vector)
print("Original Source Vector:       ", unord_vector)
print("Indices required to sort data:", sorting_index_positions) 
# Output: [3 1 2 0 4] (Index 3 has the lowest value '10', Index 4 has the highest value '90')

# Reconstructing arrays dynamically using the index sorting positions map
print("Reordered Vector Evaluation:  ", unord_vector[sorting_index_positions])



"""
================================================================================
                    NUMPY COMPLETE MASTERY HANDBOOK (Part - 04)
                     Advanced Mathematical Tools & Benchmarking
================================================================================

Topics Covered:
---------------
✔ Universal Functions (ufuncs) for Accelerated Math
✔ Linear Algebra System Solvers (np.linalg)
✔ Array Flattening Layouts (flatten vs ravel)
✔ Memory footprint and Speed Benchmarking vs. Standard Python Loops
"""

import numpy as np
import time
import sys

# ==============================================================================
# 1. UNIVERSAL FUNCTIONS (ufuncs) FOR SCALED TRIG & MATH
# ==============================================================================

print("--- 1. Universal Functions (ufuncs) ---")

"""
NumPy 'ufuncs' are highly optimized mathematical functions that execute directly 
on underlying C arrays. They automatically apply element-wise over large data ranges.
"""

angles_radians = np.array([0, np.pi/4, np.pi/2, np.pi])

print("Sine Wave Transformations:   ", np.sin(angles_radians))
print("Cosine Wave Transformations: ", np.cos(angles_radians))

numerical_values = np.array([1.0, 2.71828, 10.0, 100.0])
print("Natural Logarithm (ln):      ", np.log(numerical_values))
print("Base-10 Logarithm (log10):   ", np.log10(numerical_values))
print("Square Root Vector Calculation:", np.sqrt(numerical_values))


# ==============================================================================
# 2. ELEMENTARY LINEAR ALGEBRA ENGINE (np.linalg)
# ==============================================================================

print("\n--- 2. Linear Algebra System Matrix Solvers ---")

"""
NumPy provides a dedicated 'np.linalg' submodule designed to solve simultaneous 
algebra equations, calculate matrix determinants, and compute matrix inverses.
"""

# Solving the linear equation system: 
# 2x + 3y = 8
# 1x + 2y = 5
coefficients_matrix = np.array([[2, 3], [1, 2]])
constants_vector    = np.array([8, 5])

# Calculate matrix inverse manually
matrix_inverse = np.linalg.inv(coefficients_matrix)
print("Calculated Matrix Inverse:\n", matrix_inverse)

# Solve the equation system natively
solution_vector = np.linalg.solve(coefficients_matrix, constants_vector)
print(f"Equations System Solution Results -> x: {solution_vector[0]}, y: {solution_vector[1]}")
# Output: x: 1.0, y: 2.0


# ==============================================================================
# 3. COLLAPSING DIMENSIONS: FLATTEN VS RAVEL MECHANICS
# ==============================================================================

print("\n--- 3. Multi-Dimensional Array Flattening Mechanics ---")

"""
Both functions compress multi-dimensional grids into a single 1D vector sequence, 
but they manage your system's memory completely differently:
- .flatten(): Creates a deep, independent physical data copy. Safe, but uses more memory.
- .ravel(): Creates a shared reference pointer view. Faster, uses minimal memory.
"""

base_grid = np.array([[1, 2], [3, 4]])

# A. Modifying a Flattened Array Copy
flattened_array = base_grid.flatten()
flattened_array[0] = 999
print("Source Grid (Untouched by .flatten()):\n", base_grid) # Index 0 stays 1

# B. Modifying a Raveled Array Reference View
raveled_array = base_grid.ravel()
raveled_array[0] = 999
print("Source Grid (ALTERED by .ravel()):\n", base_grid)    # Index 0 becomes 999!


# ==============================================================================
# 4. PERFORMANCE BENCHMARKING: PYTHON LOOPS VS NUMPY VECTORS
# ==============================================================================

print("\n--- 4. Real-World Execution Profiling Benchmarks ---")

# Setup large data target sizes
DATA_ELEMENT_SIZE = 1_000_000

# Allocate Standard Python Lists
python_list_x = list(range(DATA_ELEMENT_SIZE))
python_list_y = list(range(DATA_ELEMENT_SIZE))

# Allocate Identical NumPy Arrays
numpy_array_x = np.arange(DATA_ELEMENT_SIZE)
numpy_array_y = np.arange(DATA_ELEMENT_SIZE)

# A. Measure Memory Resource Allocation Footprint
python_list_bytes = sys.getsizeof(python_list_x) + sum(sys.getsizeof(item) for item in python_list_x)
numpy_array_bytes = numpy_array_x.nbytes

print(f"Total Memory Consumption (Python List): {python_list_bytes / (1024**2):.2f} MB")
print(f"Total Memory Consumption (NumPy Array): {numpy_array_bytes / (1024**2):.2f} MB")

# B. Measure Calculation Speed Performance
# Python Loop Profile Time
start_time_python = time.time()
python_list_result = [x + y for x, y in zip(python_list_x, python_list_y)]
end_time_python = time.time()
execution_duration_python = end_time_python - start_time_python

# NumPy Vectorized Profile Time
start_time_numpy = time.time()
numpy_array_result = numpy_array_x + numpy_array_y
end_time_numpy = time.time()
execution_duration_numpy = end_time_numpy - start_time_numpy

print(f"Execution Duration Time (Python Loop):  {execution_duration_python:.5f} seconds")
print(f"Execution Duration Time (NumPy Vector): {execution_duration_numpy:.5f} seconds")
print(f"--> NumPy Vectorized Processing is roughly {execution_duration_python / max(execution_duration_numpy, 1e-6):.1f}x Faster!")



"""
================================================================================
                    NUMPY COMPLETE MASTERY HANDBOOK (Part - 05)
                Structural Data Mutations & Vector Expansion Rules
================================================================================

Topics Covered:
---------------
✔ Precise Control over Data Types (Explicit Castings via .astype)
✔ Artificial Vector Dimensional Inflation (np.newaxis & np.expand_dims)
✔ Array Dimension Dropping & Compression Mechanics (.squeeze)
✔ Intercepting and Filtering Multi-Dimensional Coordinate Locations (np.argwhere)
✔ Value Clamping and Capping Operations (np.clip)
"""

import numpy as np

# ==============================================================================
# 1. PRECISION CONTROL: EXPLICIT TYPE CASTINGS (.astype)
# ==============================================================================

print("--- 1. Memory and Type Casting Overrides ---")

"""
While NumPy manages upcasting automatically, you often need to manually overwrite 
or demote precision types explicitly to save GPU memory space or match ML data tensors.
"""

floating_measurements = np.array([1.9, 2.4, 5.8, 9.1])
print("Original Raw Data Type:", floating_measurements.dtype) # Output: float64

# Force drop decimal values by casting directly into native integers
cast_integers = floating_measurements.astype(np.int32)
print("Manually Casted Array:", cast_integers)          # Output: [1 2 5 9] (Truncated, not rounded)
print("New Active Data Type: ", cast_integers.dtype)      # Output: int32


# ==============================================================================
# 2. DIMENSIONAL INFLATION MECHANICS: GENERATING HIGHER DIMENSIONS
# ==============================================================================

print("\n--- 2. Artificially Inflating Matrix Dimensions ---")

"""
Deep learning packages often expect inputs to include explicit batch dimensions. 
You can transform a simple 1D vector into a complex 2D column or row matrix without 
overwriting data using 'np.newaxis' or 'np.expand_dims'.
"""

base_vector = np.array([10, 20, 30]) # Shape is flat: (3,)
print("Original Vector Shape Layout:", base_vector.shape)

# A. Transform into a Row Matrix structure: (1, 3)
row_matrix_view = base_vector[np.newaxis, :]
print("Row Matrix Configuration Shape:", row_matrix_view.shape) # Output: (1, 3)

# B. Transform into a Column Matrix structure: (3, 1)
column_matrix_view = base_vector[:, np.newaxis]
print("Column Matrix Configuration Shape:\n", column_matrix_view.shape) # Output: (3, 1)

# C. Utilizing the functional expand wrapper routine
expanded_tensor_dimension = np.expand_dims(base_vector, axis=0)
print("np.expand_dims (axis=0) Shape Target:", expanded_tensor_dimension.shape) # Output: (1, 3)


# ==============================================================================
# 3. DIMENSIONAL STRIPPING: COMPRESSING UNUSED AXES (.squeeze)
# ==============================================================================

print("\n--- 3. Compression and Squeezing Extra Dimensions ---")

"""
Opposite of expansion: deletes single-element dimensions (dimensions where size == 1) 
to flatten down data processing channels cleanly.
"""

bloated_matrix_tensor = np.array([[[10], [20], [30]]]) 
print("Complex Layer Matrix Shape:", bloated_matrix_tensor.shape) # Output: (1, 3, 1)

# Compress structural single-axes out of memory layout completely
streamlined_vector = bloated_matrix_tensor.squeeze()
print("Squeezed Target Vector Output:", streamlined_vector)       # Output: [10 20 30]
print("Streamlined Vector Shape Layout:", streamlined_vector.shape) # Output: (3,)


# ==============================================================================
# 4. MULTI-DIMENSIONAL COORDINATE EXTRACTIONS (np.argwhere)
# ==============================================================================

print("\n--- 4. Extracting Absolute Coordinate Mappings ---")

"""
While .argmax() works on flattened indices, np.argwhere() returns the exact 
Row and Column coordinate intercepts matching your condition.
"""

feature_grid_map = np.array([
    [0, 15,  0],
    [0,  0, 42],
    [8,  0,  0]
])

# Find coordinates where numbers are strictly greater than zero
nonzero_coordinates = np.argwhere(feature_grid_map > 0)
print("Discovered Absolute Coordinate Intercept Pairs (Row, Col):\n", nonzero_coordinates)
"""
Output:
[[0 1]  -> Pointing to value 15
 [1 2]  -> Pointing to value 42
 [2 0]] -> Pointing to value 8
"""


# ==============================================================================
# 5. DATA STABILIZATION AND VALUE CLAMPING (np.clip)
# ==============================================================================

print("\n--- 5. Vector Outlier Clamping Pipelines ---")

"""
np.clip() forces outlier data into a strict minimum/maximum boundary.
Any value below the min becomes the min, and any value above the max becomes the max.
This prevents exploding gradients in machine learning frameworks.
"""

raw_sensor_inputs = np.array([-15, 4, 12, 98, 35, -2, 50])

# Enforce strict boundary rules: values must remain between 0 and 40
stabilized_signals = np.clip(raw_sensor_inputs, a_min=0, a_max=40)
print("Original Input Values:   ", raw_sensor_inputs)
print("Stabilized Clamped Output:", stabilized_signals)
# Output: [ 0  4 12 40 35  0 40]
