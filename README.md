# Vector2D
Python Class representing a 2D Vector with convenient functions. Math, compare and string operators are overwritten.

# Example
```python
from Vector2D import Vector2D

a = Vector2D(2, 4)
b = Vector2D(1, -1)
c = a + b
print(c == Vector2D(3, 3))
print(c)

# output:
# >> True
# >> [3, 3]
```

# Efficiency
Not quite as fast as tuples, but faster than using Numpy vectors. (see [speed_comparison.py](https://github.com/iMilchshake/Vector2D/blob/master/speed_comparison.py))

