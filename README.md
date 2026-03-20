# SE446 - Milestone 1: Chicago Crime Analytics with MapReduce

## Group 4

| Name | Student ID |
|------|------------|
| Dana Ghassan | 231435|
| Sema Raslan |231476 |
| Yomna Kassem |231158 |
| Sara Elhams |201575 |

## Executive Summary
This project implements a MapReduce pipeline on a Hadoop cluster to analyze the Chicago Crimes dataset. We wrote four mapper scripts to answer key questions about crime types, locations, yearly trends, and arrest rates. All jobs were run using Hadoop Streaming with Python scripts on a dataset of 793,073 crime records.

## Task 2: Crime Type Distribution

### Command
```
mapred streaming -files mapper_task2.py,reducer_sum.py -mapper "python3 mapper_task2.py" -reducer "python3 reducer_sum.py" -input /data/chicago_crimes.csv -output /user/dghassan/project/m1/task2_full
```

### Top 5 Results
```
THEFT          162688
BATTERY        151930
CRIMINAL DAMAGE 91241
NARCOTICS       74127
ASSAULT         54070
```

### Interpretation
Theft is the most prevalent crime in Chicago, accounting for the largest share of all reported incidents, followed closely by battery.

## Task 3: Location Hotspots

### Command
```
mapred streaming -files mapper_task3.py,reducer_sum.py -mapper "python3 mapper_task3.py" -reducer "python3 reducer_sum.py" -input /data/chicago_crimes.csv -output /user/dghassan/project/m1/task3_full
```

### Top 5 Results
```
STREET          245437
RESIDENCE       136238
APARTMENT        60925
SIDEWALK         47407
OTHER            29213
```

### Interpretation
Streets are the most common crime location, suggesting that outdoor public spaces require the highest patrol presence.

## Task 4: Year Trend

### Command
```
mapred streaming -files mapper_task4.py,reducer_sum.py -mapper "python3 mapper_task4.py" -reducer "python3 reducer_sum.py" -input /data/chicago_crimes.csv -output /user/dghassan/project/m1/task4_full
```

### Top 5 Results
```
2001    467301
2002    205267
2023     81461
2025     12710
2022      4678
```

### Interpretation
Crime volume was highest in 2001-2002, showing a significant decline over the following two decades.

## Task 5: Arrest Analysis

### Command
```
mapred streaming -files mapper_task5.py,reducer_sum.py -mapper "python3 mapper_task5.py" -reducer "python3 reducer_sum.py" -input /data/chicago_crimes.csv -output /user/dghassan/project/m1/task5_full
```

### Top 5 Results
```
false    551554
true     215199
```

### Interpretation
Only 28% of crimes result in an arrest, indicating that the majority of criminal incidents do not lead to apprehension.

## Member Contributions

| Member | Task | Contribution |
|--------|------|--------------|
| Dana Ghassan | Task 2 | Wrote mapper_task2.py, ran job on cluster |
| Sema Raslan | Task 3 | Wrote mapper_task3.py, ran job on cluster |
| Yomna Kassem | Task 4 | Wrote mapper_task4.py, ran job on cluster |
| Sara Elhams | Task 5 | Wrote mapper_task5.py, ran job on cluster |
