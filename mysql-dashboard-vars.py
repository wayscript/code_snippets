import math
import statistics

scores = variables[ 'scores' ]
print(scores)

scores = [float(i) for i in scores]
print(scores)

max = max(scores)
min = min(scores)
standard_deviation = statistics.stdev(scores)

variables[ 'max' ] = max
variables[ 'min' ] = min
variables[ 'stand_deviation' ] = round(standard_deviation, 2)
