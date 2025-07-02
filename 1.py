
name = 'GopiRam'

print(name[-1:-6:-2])

print(name[1:5:2])



# ## Python String Slicing: Understanding Empty Results with Negative Indices

# When working with string slicing in Python, you might encounter an empty result even when it seems like you should be selecting characters. A common scenario for this is when using negative indices in a way that goes against the default slicing direction.

# Consider the following:

# ```python
# name = 'GopiRam'
# print(name[-1:-5])
# ```

# The output of `print(name[-1:-5])` will be an **empty string**.

# ### Why does this happen?

# Python string slicing uses the format `[start:end:step]`. When the `step` is not specified (meaning it defaults to `+1`), Python expects to slice from left to right.

# 1.  **`start = -1`**: This refers to the last character of the string ('m').
# 2.  **`end = -5`**: This refers to the character at index 'p' (the fifth character from the end).

# Since you're starting at index `-1` (the rightmost part) and trying to slice towards index `-5` (further to the left) with a default positive step, the slice has no elements to include. Python's slicing mechanism won't automatically reverse direction for you.

# ### How to get a result when slicing "backwards"?

# If you intend to slice from right to left, you **must** specify a negative `step`. For example, to get 'maR' from 'GopiRam' (starting from 'm', moving left, and stopping before 'i'):

# ```python
# name = 'GopiRam'
# print(name[-1:-5:-1]) # Output: 'maR'
# ```

# Remember, for a default positive step, your `start` index generally needs to be less than your `end` index to yield a non-empty slice.
