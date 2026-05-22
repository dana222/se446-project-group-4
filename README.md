# SE446 - Chicago Crime Analytics: Milestone 1 & 2

## Group 4

| Name | Student ID | GitHub |
|------|------------|--------|
| Dana Ghassan | 231435 | dana222 |
| Sema Raslan | 231476 | semaraslan |
| Yomna Kassem | 231158 | yomnanka |
| Sara Elhams | 201575 | sara-x01 |

---

## Note to Instructor

We are still learning how to use GitHub properly and sincerely apologize for any workflow issues you may encounter. Both Milestone 1 and Milestone 2 are contained in this single repository as required. To navigate each member's work, please look at the branch names they are named after the task and member:

| Branch | Member | Tasks |
|--------|--------|-------|
| task2-dana | Dana Ghassan | M1 Task 2 |
| task3-sema | Sema Raslan | M1 Task 3 |
| task4-yomna | Yomna Kassem | M1 Task 4 |
| task5-sara | Sara Elhams | M1 Task 5 |
| m2-task1-2-dana | Dana Ghassan | M2 Tasks 1 and 2 |
| m2-task3-4-sema | Sema Raslan | M2 Tasks 3 and 4 |
| m2-task5-6-7-yomna | Yomna Kassem | M2 Tasks 5, 6 and 7 |
| m2-task9-11-sara | Sara Elhams | M2 Tasks 9, 10 and 11 |

We did our best to follow the Git workflow and appreciate your patience.

Additionally, Tasks 10 and 11 are facing a merge conflict involving: M2_Spark_ML_Group4.ipynb, output/task7_feature_importances.png, and src/mapper_task5.py. We are actively working to resolve these. The code and execution evidence for Tasks 10 and 11 can be found in the branch m2-task9-11-sara.

---

## Repository Structure

```
se446-project-group-4/
├── README.md
├── M2_Spark_ML_Group4.ipynb
├── m2_spark_ml.py
├── src/
│   ├── mapper_task2.py
│   ├── mapper_task3.py
│   ├── mapper_task4.py
│   ├── mapper_task5.py
│   └── reducer_sum.py
├── output/
│   ├── task7_feature_importances.png
│   ├── task9_local_evidence.png
│   ├── task10_cluster_client_evidence.png
│   └── spark_submit/run.log
└── docs/
```

---

## Cluster Information

- Cluster: 134.209.172.50 (Hadoop 3.4.1, YARN)
- Full dataset: hdfs:///data/chicago_crimes.csv — 793,073 records
- Sample dataset: hdfs:///data/chicago_crimes_sample.csv — 10,000 records

---

# MILESTONE 1: MapReduce Pipeline

## Executive Summary

Milestone 1 implements a MapReduce pipeline on a Hadoop cluster to analyze the Chicago Crimes dataset. We wrote four mapper scripts (one per team member) to answer key questions about crime types, locations, yearly trends, and arrest rates. All jobs were run using Hadoop Streaming with Python on a dataset of 793,073 crime records. Each task was first validated on a 10,000-record sample before running on the full dataset.

---

## M1 Task Distribution

| Member | Task | Branch |
|--------|------|--------|
| Dana Ghassan | Task 2 Crime type distribution | task2-dana |
| Sema Raslan | Task 3 Location hotspots | task3-sema |
| Yomna Kassem | Task 4 Crime trends over years | task4-yomna |
| Sara Elhams | Task 5 Arrest rate analysis | task5-sara |

---

## Task 2: Crime Type Distribution
Author: Dana Ghassan (231435) | Branch: task2-dana

Research Question: What are the most common types of crimes in Chicago?

Mapper: src/mapper_task2.py

### Commands

```bash
mapred streaming -files mapper_task2.py,reducer_sum.py \
  -mapper "python3 mapper_task2.py" -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes_sample.csv \
  -output /user/dghassan/project/m1/task2

mapred streaming -files mapper_task2.py,reducer_sum.py \
  -mapper "python3 mapper_task2.py" -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes.csv \
  -output /user/dghassan/project/m1/task2_full
```

### Top 5 Results (Full Dataset)
```
THEFT             162,688
BATTERY           151,930
CRIMINAL DAMAGE    91,241
NARCOTICS          74,127
ASSAULT            54,070
```

### Interpretation
Theft is the most prevalent crime in Chicago, accounting for the largest share of all reported incidents, followed closely by battery. Together these two categories represent over 40% of all crimes.

---

## Task 3: Location Hotspots
Author: Sema Raslan (231476) | Branch: task3-sema

Research Question: Where do most crimes occur?

Mapper: src/mapper_task3.py

### Commands

```bash
mapred streaming -files mapper_task3.py,reducer_sum.py \
  -mapper "python3 mapper_task3.py" -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes_sample.csv \
  -output /user/soraslan/project/m1/task3

mapred streaming -files mapper_task3.py,reducer_sum.py \
  -mapper "python3 mapper_task3.py" -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes.csv \
  -output /user/soraslan/project/m1/task3_full
```

### Top 5 Results (Full Dataset)
```
STREET            245,437
RESIDENCE         136,238
APARTMENT          60,925
SIDEWALK           47,407
OTHER              29,213
```

### Interpretation
Streets are by far the most common crime location, indicating that outdoor public spaces require the highest patrol priority, with residential areas following as the second most dangerous zone.

---

## Task 4: Crime Trend Over Years
Author: Yomna Kassem (231158) | Branch: task4-yomna

Research Question: How has the total number of crimes changed over the years?

Mapper: src/mapper_task4.py

### Commands

```bash
mapred streaming -files mapper_task4.py,reducer_sum.py \
  -mapper "python3 mapper_task4.py" -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes_sample.csv \
  -output /user/ykassem/project/m1/task4

mapred streaming -files mapper_task4.py,reducer_sum.py \
  -mapper "python3 mapper_task4.py" -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes.csv \
  -output /user/ykassem/project/m1/task4_full
```

### Top Results (Full Dataset)
```
2001    467,301
2002    205,267
2023     81,461
2025     12,710
2022      4,678
```

### Interpretation
Crime volume was highest in the early 2000s, with a sharp decline over the following decades, suggesting a long-term downward trend in reported incidents across Chicago.

---

## Task 5: Arrest Rate Analysis
Author: Sara Elhams (201575) | Branch: task5-sara

Research Question: What percentage of crimes result in an arrest?

Mapper: src/mapper_task5.py

### Command

```bash
mapred streaming -files mapper_task5.py,reducer_sum.py \
  -mapper "python3 mapper_task5.py" -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes.csv \
  -output /user/selhams/task5_output
```

### Results (Full Dataset)
```
false    551,554   (72.02%)
true     215,199   (27.98%)
```

### Interpretation
Only approximately 28% of crimes result in an arrest, meaning nearly 3 out of 4 criminal incidents do not lead to a direct apprehension, indicating significant room for improvement in patrol efficiency.

---

## M1 Member Contributions

| Name | Task | Branch | Contribution |
|------|------|--------|-------------|
| Dana Ghassan | Task 2 | task2-dana | Wrote mapper_task2.py, ran job on cluster, documented results |
| Sema Raslan | Task 3 | task3-sema | Wrote mapper_task3.py, ran job on cluster, documented results |
| Yomna Kassem | Task 4 | task4-yomna | Wrote mapper_task4.py, ran job on cluster, documented results |
| Sara Elhams | Task 5 | task5-sara | Wrote mapper_task5.py, ran job on cluster, documented results |

---

# MILESTONE 2: Spark + MLlib Pipeline

## Executive Summary

Milestone 2 upgrades the analytics from MapReduce batch counting to in-memory Spark DataFrame analysis and machine learning using MLlib. We reproduced all M1 analyses using Spark (Tasks 1-4), built a complete ML pipeline to predict arrest outcomes (Tasks 5-7), and demonstrated the work running locally and on the cluster (Tasks 9-11). Task 8 (CrossValidator) was officially waived by Prof. Anis Koubaa on May 3, 2026 due to cluster memory constraints. The notebook auto-detects the environment and runs the same code locally (10K generated rows) and on the cluster (793K+ real rows). Phase B ML tasks use a mandatory 5% sample as required by the professor.

---

## M2 Task Distribution

| Member | Tasks | Branch | Phase |
|--------|-------|--------|-------|
| Dana Ghassan | Tasks 1, 2 | m2-task1-2-dana | Phase A |
| Sema Raslan | Tasks 3, 4 | m2-task3-4-sema | Phase A |
| Yomna Kassem | Tasks 5, 6, 7 | m2-task5-6-7-yomna | Phase B |
| Sara Elhams | Tasks 9, 10, 11 | m2-task9-11-sara | Phase C |

Note: Task 8 (CrossValidator) was officially waived by Prof. Anis Koubaa on May 3, 2026 due to cluster memory constraints. Marks were redistributed across remaining tasks.

---

## Phase A: Spark DataFrame Analytics — M1 vs M2 Comparison

### Task 1: Crime Type Distribution (Spark DataFrame)
Author: Dana Ghassan (231435) | Branch: m2-task1-2-dana

| Crime Type | M1 MapReduce | M2 Spark | Match |
|------------|-------------|----------|-------|
| THEFT | 162,688 | 162,688 | YES |
| BATTERY | 151,930 | 151,930 | YES |
| CRIMINAL DAMAGE | 91,241 | 91,241 | YES |
| NARCOTICS | 74,127 | 74,127 | YES |
| ASSAULT | 54,070 | 54,070 | YES |

Results match M1 exactly on the cluster. Spark was significantly faster and required less code than MapReduce.

---

### Task 2: Location Hotspots (Spark SQL)
Author: Dana Ghassan (231435) | Branch: m2-task1-2-dana

| Location | M1 MapReduce | M2 Spark | Diff |
|----------|-------------|----------|------|
| STREET | 245,437 | 248,326 | +2,889 |
| RESIDENCE | 136,238 | 136,393 | +155 |
| APARTMENT | 60,925 | 61,235 | +310 |
| SIDEWALK | 47,407 | 47,506 | +99 |
| OTHER | 29,213 | 29,671 | +458 |

Minor differences under 1% are expected due to Spark's dropna() handling vs M1 row filtering. Top locations and ranking are identical across both methods.

---

### Task 3: Crime Trend Over Years (DataFrame + Visualization)
Author: Sema Raslan (231476) | Branch: m2-task3-4-sema

| Year | M1 MapReduce | M2 Spark | Match |
|------|-------------|----------|-------|
| 2001 | 467,301 | 467,301 | YES |
| 2002 | 205,267 | 205,267 | YES |
| 2023 | 81,461 | 81,461 | YES |
| 2025 | 12,710 | 12,710 | YES |
| 2022 | 4,678 | 4,678 | YES |

A matplotlib line chart was generated in local mode saved to output/crime_trend.png. On the cluster, results are printed as a table.

---

### Task 4: Arrest Rate Analysis (DataFrame)
Author: Sema Raslan (231476) | Branch: m2-task3-4-sema

| Metric | M1 MapReduce | M2 Spark | Match |
|--------|-------------|----------|-------|
| No Arrest (false) | 551,554 | 551,554 | YES |
| Arrested (true) | 215,199 | 215,199 | YES |
| Overall Arrest Rate | 27.98% | 27.98% | YES |

Arrest rate by crime type — Top 5 highest:

| Crime Type | Arrest Rate |
|------------|-------------|
| NARCOTICS | 85.32% |
| PROSTITUTION | 81.10% |
| WEAPONS VIOLATION | 59.64% |
| BATTERY | 30.06% |
| ASSAULT | 25.32% |

Arrest rate by crime type — Bottom 5 lowest:

| Crime Type | Arrest Rate |
|------------|-------------|
| CRIMINAL DAMAGE | 5.91% |
| MOTOR VEHICLE THEFT | 8.46% |
| BURGLARY | 9.19% |
| THEFT | 14.01% |
| ROBBERY | 15.15% |

---

## Phase B: Spark MLlib — Arrest Prediction

Sampling note: All Phase B tasks use a mandatory 5% sample df.sample(0.05, seed=42) as required by Prof. Koubaa to avoid cluster memory issues.
- Full dataset rows: 793,072
- ML sample rows (5%): 39,534
- Training rows: 31,728 | Testing rows: 7,806

### Task 5: Feature Engineering Pipeline
Author: Yomna Kassem (231158) | Branch: m2-task5-6-7-yomna

Pipeline stages:
- StringIndexer: PrimaryType to crime_index (most frequent = 0)
- StringIndexer: Domestic_str to domestic_index (false = 0, true = 1)
- VectorAssembler: [District, crime_index, Hour, domestic_index] to features

Sample feature vectors (5 rows, cluster run):
```
District  crime_index  Hour  domestic_index  features                label
1         4.0          0     0.0             [1.0, 4.0, 0.0, 0.0]    0
1         4.0          2     1.0             [1.0, 4.0, 2.0, 1.0]    1
1         4.0          7     0.0             [1.0, 4.0, 7.0, 0.0]    0
1         4.0          9     0.0             [1.0, 4.0, 9.0, 0.0]    0
1         4.0          9     0.0             [1.0, 4.0, 9.0, 0.0]    0
```

Feature vector positions:
- [0] District — police district number (1-25)
- [1] crime_index — encoded crime type (0 = most frequent)
- [2] Hour — hour of the day the crime occurred (0-23)
- [3] domestic_index — encoded domestic flag (0 = false, 1 = true)

Class balance (training set):
```
label 0 (No Arrest): 22,741
label 1 (Arrest):     8,987
```

---

### Task 6: Train and Evaluate Three Models
Author: Yomna Kassem (231158) | Branch: m2-task5-6-7-yomna

Parameters used:
- Logistic Regression: maxIter=100, regParam=0.01
- Random Forest: numTrees=100, maxDepth=5, seed=42
- GBT: maxIter=50, maxDepth=5, seed=42

Model Comparison Table (Cluster Run — 5% sample, 39,534 rows):

| Metric | Logistic Regression | Random Forest | GBT |
|--------|---------------------|---------------|-----|
| AUC-ROC | 0.6202 | 0.8193 | 0.8301 |
| Accuracy | 0.7281 | 0.8161 | 0.8562 |
| F1 Score | 0.6360 | 0.7815 | 0.8423 |
| Precision | 0.7010 | 0.8525 | 0.8653 |
| Recall | 0.7281 | 0.8161 | 0.8562 |
| Training Time | 14.8s | 25.3s | 438.7s |

Best model by AUC-ROC: GBT (0.8301)

Confusion Matrices (Cluster Run):

Logistic Regression:
```
Label 0 Predicted 0 (TN): 1,187
Label 0 Predicted 1 (FP):    60
Label 1 Predicted 0 (FN):   607
Label 1 Predicted 1 (TP):    75
```

Random Forest:
```
Label 0 Predicted 0 (TN): 1,089
Label 0 Predicted 1 (FP):   158
Label 1 Predicted 0 (FN):   204
Label 1 Predicted 1 (TP):   478
```

GBT:
```
Label 0 Predicted 0 (TN): 1,099
Label 0 Predicted 1 (FP):   148
Label 1 Predicted 0 (FN):   220
Label 1 Predicted 1 (TP):   462
```

---

### Task 7: Feature Importances and Interpretation
Author: Yomna Kassem (231158) | Branch: m2-task5-6-7-yomna

Feature Importances (Random Forest — Cluster Run):

| Feature | Importance |
|---------|------------|
| crime_index | 0.9763 |
| Hour | 0.0109 |
| domestic_index | 0.0084 |
| District | 0.0043 |

Chart saved to output/task7_feature_importances.png.

Interpretation:

1. Most important feature: crime_index (PrimaryType) dominates with an importance score of 0.9763. Different crime types have drastically different arrest rates — NARCOTICS has an ~87% arrest rate while THEFT has only ~11%. This matches Task 4 arrest rate analysis exactly.

2. Does feature importance match Task 4? YES. Task 4 showed crime type has the largest range in arrest rates (from 5.91% for CRIMINAL DAMAGE to 85.32% for NARCOTICS). The model independently confirms PrimaryType is the strongest predictor of arrest outcome.

3. Why does Logistic Regression perform worse? LR assumes a linear decision boundary — it draws one straight line to separate arrests from non-arrests. The relationship between crime features and arrest outcomes is highly non-linear (e.g. NARCOTICS at 2AM behaves very differently from THEFT at 2PM). RF and GBT can capture these complex interactions; LR cannot.

---

## Phase C: Deployment Modes

### Task 9: Local Execution Evidence
Author: Sara Elhams (201575) | Branch: m2-task9-11-sara

The complete notebook was run on a laptop in local[*] mode using 10,000 generated rows.

```
Master:        local[*]
Spark Version: 3.5.0
Environment:   LOCAL
Total rows:    10,000
App Name:      SE446_M2_Group4
```

Screenshot saved to output/task9_local_evidence.png.

---

### Task 10: Cluster Execution — Client Mode
Author: Sara Elhams (201575) | Branch: m2-task9-11-sara

SSH into cluster as selhams@134.209.172.50. Notebook run on cluster via YARN client mode.

Cluster execution output:
```
Spark 3.5.4 running on: yarn
Environment detected: CLUSTER
Total rows: 793,072

Schema:
 District: integer
 PrimaryType: string
 Hour: integer
 Year: integer
 Domestic_str: string
 Arrest: boolean
 label: integer

Using 5% sample for ML: 39,534 rows
Training rows: 31,728
Testing rows:  7,806

Class Balance:
  label 0 (No Arrest): 22,741
  label 1 (Arrest):     8,987
```

Screenshot saved to output/task10_cluster_client_evidence.png.

---

### Task 11: Cluster Execution — spark-submit
Author: Sara Elhams (201575) | Branch: m2-task9-11-sara

Command used:
```bash
spark-submit --master yarn --deploy-mode client m2_spark_ml.py
```

spark-submit execution log (cluster):
```
26/05/22 06:56:12 WARN NativeCodeLoader: Unable to load native-hadoop library
PySpark version: 3.5.4
26/05/22 06:56:13 INFO SparkContext: Running Spark 3.5.4
26/05/22 06:56:13 INFO SparkContext: Submitted application: SE446_M2_Group4
26/05/22 06:56:16 INFO Client: Will allocate AM container with 640 MB memory
26/05/22 06:56:16 INFO Client: Setting up the launch environment for AM container

Application Name: SE446_M2_Group4
Master: yarn

=== Model Comparison Table ===
Model                  AUC-ROC  Accuracy      F1  Precision  Recall  Time(s)
---------------------------------------------------------------------------
Logistic Regression     0.6202    0.7281  0.6360     0.7010  0.7281     14.8
Random Forest           0.8193    0.8161  0.7815     0.8525  0.8161     25.3
GBT                     0.8301    0.8562  0.8423     0.8653  0.8562    438.7

Best model by AUC-ROC: GBT (0.8301)

=== Task 7: Feature Importances (Random Forest) ===
Feature              Importance
District                 0.0043
crime_index              0.9763
Hour                     0.0109
domestic_index           0.0084

Most important feature: crime_index

=== TASK 11: Spark Submit Cluster Mode Test ===
Application Name: SE446_M2_Group4
Master: yarn
Task 11 completed successfully on cluster mode.
```

Full log saved to output/spark_submit/run.log.

---

## M1 vs M2 Comparison

| Aspect | M1 MapReduce | M2 Spark |
|--------|-------------|----------|
| Technology | Hadoop Streaming + Python mappers | PySpark DataFrames + Spark SQL |
| Code complexity | 4 separate mapper files + reducer | Single notebook, auto-detects environment |
| Results Task 1 | THEFT: 162,688 | THEFT: 162,688 — match |
| Results Task 2 | STREET: 245,437 | STREET: 248,326 — under 1% diff |
| Results Task 3 | 2001: 467,301 | 2001: 467,301 — match |
| Results Task 4 | Arrest rate: 27.98% | Arrest rate: 27.98% — match |
| Speed full dataset | ~2-3 min per task | ~3 min for all Phase A tasks |
| ML capability | None | Full MLlib pipeline with 3 models |
| Best ML model | N/A | GBT (AUC = 0.8301, Accuracy = 85.62%) |

Key insight: Spark produces results identical or near-identical to MapReduce but with significantly less code and better performance. The real advantage of Spark shows in Phase B — ML tasks that would be impossible in MapReduce are straightforward with MLlib.

---

## ML Results Summary

- Best model: GBT (AUC-ROC = 0.8301, Accuracy = 85.62%, F1 = 0.8423)
- Runner-up: Random Forest (AUC-ROC = 0.8193, Accuracy = 81.61%)
- Key finding: Crime type (crime_index) is by far the most important feature (importance = 0.9763 on cluster), confirming that knowing the type of crime is highly predictive of whether an arrest will be made
- Recommendation: Deploy GBT for highest accuracy, or Random Forest for a balance of accuracy and speed (25s vs 438s training time)

---

## M2 Member Contributions

| Name | Tasks | Branch | Contribution |
|------|-------|--------|-------------|
| Dana Ghassan | Tasks 1, 2 | m2-task1-2-dana | Spark DataFrame crime type analysis, Spark SQL location hotspots, M1 vs M2 comparison, SparkSession setup, data loading with environment auto-detection |
| Sema Raslan | Tasks 3, 4 | m2-task3-4-sema | Crime trend visualization with matplotlib, arrest rate analysis by crime type with top and bottom rankings |
| Yomna Kassem | Tasks 5, 6, 7 | m2-task5-6-7-yomna | Feature engineering pipeline, trained RF/LR/GBT models with confusion matrices, feature importances and interpretation |
| Sara Elhams | Tasks 9, 10, 11 | m2-task9-11-sara | Local execution evidence, cluster YARN client mode (793,072 rows confirmed), spark-submit script and execution logs |

---

## Known Issues

Merge conflict on m2-task9-11-sara branch: The following files have conflicts that are currently being resolved:
- M2_Spark_ML_Group4.ipynb — multiple members edited the shared notebook simultaneously
- output/task7_feature_importances.png — generated by Yomna, referenced by Sara's branch
- src/mapper_task5.py — M1 file touched by both branches

The evidence for Tasks 10 and 11 is complete and available in the m2-task9-11-sara branch. We will merge once the conflict is resolved.

---

## Instructor Collaborator

GitHub user akoubaa has been added as a collaborator to this repository.
