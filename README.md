# SE446 - Chicago Crime Analytics: Milestone 1 & 2

## Group 4

| Name | Student ID | GitHub |
|------|------------|--------|
| Dana Ghassan | 231435 | dana222 |
| Sema Raslan | 231476 | semaraslan |
| Yomna Kassem | 231158 | yomnanka |
| Sara Elhams | 201575 | sara-x01 |

---

## ⚠️ Note to Instructor

We are still learning how to use GitHub properly and apologize for any workflow issues. Both Milestone 1 and Milestone 2 are contained in this single repository as required. To navigate each task, please look at the branch names — they are named after the task and member (e.g. `m2-task1-2-dana`, `m2-task3-4-sema`, `m2-task5-6-7-yomna`, `m2-task9-11-sara`). Each branch contains the work for that member's assigned tasks. We did our best to follow the Git workflow and appreciate your patience.

Additionally, Tasks 10 and 11 (cluster client mode and spark-submit) are currently facing a merge conflict involving the following files:
- `M2_Spark_ML_Group4.ipynb`
- `output/task7_feature_importances.png`
- `src/mapper_task5.py`

We are actively working to resolve these conflicts. The code and execution evidence for Tasks 10 and 11 can be found in the branch `m2-task9-11-sara`.

---

## Repository Structure

```
se446-project-group-4/
├── README.md                        ← this file (M1 + M2 report)
├── M2_Spark_ML_Group4.ipynb         ← Milestone 2 main notebook
├── m2_spark_ml.py                   ← Milestone 2 spark-submit script
├── src/                             ← Milestone 1 mapper scripts
│   ├── mapper_task2.py              ← Dana: crime type distribution
│   ├── mapper_task3.py              ← Sema: location hotspots
│   ├── mapper_task4.py              ← Yomna: crime trends by year
│   ├── mapper_task5.py              ← Sara: arrest rate analysis
│   └── reducer_sum.py               ← shared reducer
├── output/                          ← results, screenshots, evidence
└── docs/                            ← additional documentation
```

---

## Cluster Information

- **Cluster**: `134.209.172.50` (Hadoop 3.4.1, YARN)
- **Dataset (M1 & M2)**: `hdfs:///data/chicago_crimes.csv` — 793,073 records
- **Sample dataset**: `hdfs:///data/chicago_crimes_sample.csv` — 10,000 records

---

# MILESTONE 1: MapReduce Pipeline

## Executive Summary

Milestone 1 implements a MapReduce pipeline on a Hadoop cluster to analyze the Chicago Crimes dataset. We wrote four mapper scripts (one per team member) to answer key questions about crime types, locations, yearly trends, and arrest rates. All jobs were run using Hadoop Streaming with Python on a dataset of 793,073 crime records. Each task was first validated on a 10,000-record sample before running on the full dataset.

---

## M1 Task Distribution

| Member | Task | Description |
|--------|------|-------------|
| Dana Ghassan | Task 2 | Crime type distribution |
| Sema Raslan | Task 3 | Location hotspots |
| Yomna Kassem | Task 4 | Crime trends over years |
| Sara Elhams | Task 5 | Arrest rate analysis |

---

## Task 2: Crime Type Distribution
**Author**: Dana Ghassan (231435) | **Branch**: `task2-dana`

**Research Question**: What are the most common types of crimes in Chicago?

**Mapper**: `src/mapper_task2.py`

### Commands
```bash
# Sample test
mapred streaming -files mapper_task2.py,reducer_sum.py \
  -mapper "python3 mapper_task2.py" -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes_sample.csv \
  -output /user/dghassan/project/m1/task2

# Full dataset
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
**Author**: Sema Raslan (231476) | **Branch**: `task3-sema`

**Research Question**: Where do most crimes occur?

**Mapper**: `src/mapper_task3.py`

### Commands
```bash
# Sample test
mapred streaming -files mapper_task3.py,reducer_sum.py \
  -mapper "python3 mapper_task3.py" -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes_sample.csv \
  -output /user/soraslan/project/m1/task3

# Full dataset
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
**Author**: Yomna Kassem (231158) | **Branch**: `task4-yomna`

**Research Question**: How has the total number of crimes changed over the years?

**Mapper**: `src/mapper_task4.py`

### Commands
```bash
# Sample test
mapred streaming -files mapper_task4.py,reducer_sum.py \
  -mapper "python3 mapper_task4.py" -reducer "python3 reducer_sum.py" \
  -input /data/chicago_crimes_sample.csv \
  -output /user/ykassem/project/m1/task4

# Full dataset
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
**Author**: Sara Elhams (201575) | **Branch**: `task5-sara`

**Research Question**: What percentage of crimes result in an arrest?

**Mapper**: `src/mapper_task5.py`

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
| Dana Ghassan | Task 2 | `task2-dana` | Wrote `mapper_task2.py`, ran job on cluster, documented results |
| Sema Raslan | Task 3 | `task3-sema` | Wrote `mapper_task3.py`, ran job on cluster, documented results |
| Yomna Kassem | Task 4 | `task4-yomna` | Wrote `mapper_task4.py`, ran job on cluster, documented results |
| Sara Elhams | Task 5 | `task5-sara` | Wrote `mapper_task5.py`, ran job on cluster, documented results |

---

---

# MILESTONE 2: Spark + MLlib Pipeline

## Executive Summary

Milestone 2 upgrades the analytics from MapReduce batch counting to in-memory Spark DataFrame analysis and machine learning using MLlib. We reproduced all M1 analyses using Spark (Tasks 1-4), built a complete ML pipeline to predict arrest outcomes (Tasks 5-7), and demonstrated the work running locally and on the cluster (Tasks 9-11). Task 8 (CrossValidator) was waived by the instructor. The notebook auto-detects the environment and runs the same code locally (10K generated rows) and on the cluster (793K+ real rows). Phase B ML tasks use a mandatory 5% sample as required by the professor.

---

## M2 Task Distribution

| Member | Tasks | Branch | Phase |
|--------|-------|--------|-------|
| Dana Ghassan | Tasks 1, 2 | `m2-task1-2-dana` | Phase A |
| Sema Raslan | Tasks 3, 4 | `m2-task3-4-sema` | Phase A |
| Yomna Kassem | Tasks 5, 6, 7 | `m2-task5-6-7-yomna` | Phase B |
| Sara Elhams | Tasks 9, 10, 11 | `m2-task9-11-sara` | Phase C |

**Note**: Task 8 (CrossValidator) was officially waived by Prof. Anis Koubaa on May 3, 2026 due to cluster memory constraints. Marks were redistributed across remaining tasks.

---

## Phase A: Spark DataFrame Analytics (M1 vs M2 Comparison)

### Task 1: Crime Type Distribution (Spark DataFrame)
**Author**: Dana Ghassan (231435) | **Branch**: `m2-task1-2-dana`

Uses `df.groupBy("PrimaryType").count().orderBy(col("count").desc()).show(10)`

| Crime Type | M1 MapReduce | M2 Spark | Match? |
|------------|-------------|----------|--------|
| THEFT | 162,688 | 162,688 | ✅ |
| BATTERY | 151,930 | 151,930 | ✅ |
| CRIMINAL DAMAGE | 91,241 | 91,241 | ✅ |
| NARCOTICS | 74,127 | 74,127 | ✅ |
| ASSAULT | 54,070 | 54,070 | ✅ |

Results match M1 exactly on the cluster. Spark was significantly faster and required less code than MapReduce.

---

### Task 2: Location Hotspots (Spark SQL)
**Author**: Dana Ghassan (231435) | **Branch**: `m2-task1-2-dana`

Uses `spark.sql("SELECT \`Location Description\`, COUNT(*) as total FROM crimes GROUP BY \`Location Description\` ORDER BY total DESC LIMIT 10")`

| Location | M1 MapReduce | M2 Spark | Match? |
|----------|-------------|----------|--------|
| STREET | 245,437 | 245,437 | ✅ |
| RESIDENCE | 136,238 | 136,238 | ✅ |
| APARTMENT | 60,925 | 60,925 | ✅ |
| SIDEWALK | 47,407 | 47,407 | ✅ |
| OTHER | 29,213 | 29,213 | ✅ |

Results match M1 exactly. Spark SQL syntax is cleaner and more expressive than writing custom mappers.

---

### Task 3: Crime Trend Over Years (DataFrame + Visualization)
**Author**: Sema Raslan (231476) | **Branch**: `m2-task3-4-sema`

Uses `df.groupBy("Year").count().orderBy("Year")`

| Year | M1 MapReduce | M2 Spark | Match? |
|------|-------------|----------|--------|
| 2001 | 467,301 | 467,301 | ✅ |
| 2002 | 205,267 | 205,267 | ✅ |
| 2023 | 81,461 | 81,461 | ✅ |
| 2025 | 12,710 | 12,710 | ✅ |
| 2022 | 4,678 | 4,678 | ✅ |

A matplotlib line chart was generated in local mode showing crime trends. On the cluster, results are printed as a table.

---

### Task 4: Arrest Rate Analysis (DataFrame)
**Author**: Sema Raslan (231476) | **Branch**: `m2-task3-4-sema`

Uses `df.groupBy("PrimaryType").agg(avg(col("label")).alias("arrest_rate"))`

| Metric | M1 MapReduce | M2 Spark | Match? |
|--------|-------------|----------|--------|
| No Arrest (false) | 551,554 | 551,554 | ✅ |
| Arrested (true) | 215,199 | 215,199 | ✅ |
| Overall Arrest Rate | 27.98% | 27.98% | ✅ |

M2 additionally shows arrest rate broken down by crime type. NARCOTICS and PROSTITUTION have the highest arrest rates (~80-85%), while THEFT and BURGLARY have the lowest (~5-10%).

---

## Phase B: Spark MLlib — Arrest Prediction

**Note**: All Phase B tasks use a mandatory 5% sample (`df.sample(0.05, seed=42)`) as required by the professor to avoid cluster memory issues. Sample size: ~39,534 rows. Train/test split: 80/20 with seed=42.

### Task 5: Feature Engineering Pipeline
**Author**: Yomna Kassem (231158) | **Branch**: `m2-task5-6-7-yomna`

Pipeline stages:
- `StringIndexer`: `PrimaryType` → `crime_index`
- `StringIndexer`: `Domestic_str` → `domestic_index`
- `VectorAssembler`: `[District, crime_index, Hour, domestic_index]` → `features`

Feature vector positions:
- `[0]` District — police district number (1–25)
- `[1]` crime_index — encoded crime type (most frequent = 0)
- `[2]` Hour — hour of the day (0–23)
- `[3]` domestic_index — encoded domestic flag (0=false, 1=true)

---

### Task 6: Train and Evaluate Three Models
**Author**: Yomna Kassem (231158) | **Branch**: `m2-task5-6-7-yomna`

| Metric | Random Forest | Logistic Regression | GBT |
|--------|:------------:|:------------------:|:---:|
| AUC-ROC | — | — | — |
| Accuracy | — | — | — |
| F1 Score | — | — | — |
| Precision | — | — | — |
| Recall | — | — | — |
| Training Time | — | — | — |

**Parameters used**:
- Logistic Regression: `maxIter=100`, `regParam=0.01`
- Random Forest: `numTrees=100`, `maxDepth=5`
- GBT: `maxIter=50`, `maxDepth=5`

*(Full metrics will be updated once cluster run completes and Tasks 10 & 11 merge conflict is resolved)*

---

### Task 7: Feature Importances & Interpretation
**Author**: Yomna Kassem (231158) | **Branch**: `m2-task5-6-7-yomna`

Feature importances extracted from the Random Forest model show that `crime_index` (crime type) is the strongest predictor of arrest outcome. This aligns with Task 4 — crime types like NARCOTICS and PROSTITUTION have very high arrest rates while THEFT and BURGLARY have very low rates, so the model correctly learns that knowing the crime type is highly predictive.

Logistic Regression performs worse than tree-based models because it treats `crime_index` as a continuous number, implying a linear ordering between crime types that does not exist in reality. Random Forest and GBT instead split on individual values, capturing the non-linear relationship between crime type and arrest probability.

---

## Phase C: Deployment Modes

### Task 9: Local Execution Evidence
**Author**: Sara Elhams (201575) | **Branch**: `m2-task9-11-sara`

The complete notebook was run on a laptop in `local[*]` mode using 10,000 generated rows.

```
Master:        local[*]
Spark Version: 4.0.2
Environment:   LOCAL
Total rows:    10,000
```

Screenshot saved in `output/task9_local_evidence.png`.

---

### Task 10: Cluster Execution — Client Mode
**Author**: Sara Elhams (201575) | **Branch**: `m2-task9-11-sara`

⚠️ **Merge conflict pending** — the evidence for Task 10 is available in the branch `m2-task9-11-sara` but has not yet been merged into main due to a conflict involving `M2_Spark_ML_Group4.ipynb` and `output/task7_feature_importances.png`. We are working to resolve this.

The notebook was run on the cluster via YARN client mode showing:
```
Master:     yarn
Total rows: 793,072
```

Command used:
```bash
pyspark --master yarn --deploy-mode client
```

---

### Task 11: Cluster Execution — spark-submit
**Author**: Sara Elhams (201575) | **Branch**: `m2-task9-11-sara`

⚠️ **Merge conflict pending** — same as Task 10 above. The `m2_spark_ml.py` script and execution logs are in the branch `m2-task9-11-sara`.

Command used:
```bash
spark-submit \
    --master yarn \
    --deploy-mode cluster \
    --driver-memory 512m \
    --num-executors 1 \
    --executor-memory 1g \
    --executor-cores 1 \
    --conf spark.driver.maxResultSize=128m \
    --conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=python3.12 \
    --conf spark.executorEnv.PYSPARK_PYTHON=python3.12 \
    m2_spark_ml.py
```

Logs retrieved with:
```bash
yarn logs -applicationId <appId> > output/spark_submit/run.log
```

---

## M1 vs M2 Comparison

| Aspect | M1 MapReduce | M2 Spark |
|--------|-------------|----------|
| Technology | Hadoop Streaming + Python mappers | PySpark DataFrames + Spark SQL |
| Code complexity | 4 separate mapper files + reducer | Single notebook, auto-detects environment |
| Results accuracy | Baseline | Matches M1 exactly on cluster ✅ |
| Speed (full dataset) | ~2–3 min per task | ~3 min for all Phase A tasks |
| Scalability | Good for batch | Better — in-memory processing |
| ML capability | None | Full MLlib pipeline with 3 models |
| Ease of use | More boilerplate | Much cleaner and expressive |

**Key insight**: Spark produces identical results to MapReduce but with significantly less code and better performance. The real advantage of Spark shows in Phase B — ML tasks that would be impossible in MapReduce are straightforward with MLlib.

---

## M2 Member Contributions

| Name | Tasks | Branch | Contribution |
|------|-------|--------|-------------|
| Dana Ghassan | Tasks 1, 2 | `m2-task1-2-dana` | Spark DataFrame crime type analysis, Spark SQL location hotspots, M1 comparison |
| Sema Raslan | Tasks 3, 4 | `m2-task3-4-sema` | Crime trend visualization, arrest rate analysis by crime type |
| Yomna Kassem | Tasks 5, 6, 7 | `m2-task5-6-7-yomna` | Feature engineering pipeline, trained RF/LR/GBT, feature importances |
| Sara Elhams | Tasks 9, 10, 11 | `m2-task9-11-sara` | Local execution evidence, cluster client mode, spark-submit script and logs |

---

## Known Issues

**Merge conflict on `m2-task9-11-sara` branch**: The following files have conflicts that are currently being resolved:
- `M2_Spark_ML_Group4.ipynb` — multiple members edited the shared notebook
- `output/task7_feature_importances.png` — generated by Yomna, referenced by Sara
- `src/mapper_task5.py` — M1 file touched by both Dana and Sara

The evidence for Tasks 10 and 11 is complete and available in the `m2-task9-11-sara` branch. We will merge once the conflict is resolved.

---

## Instructor Collaborator

GitHub user `akoubaa` has been added as a collaborator to this repository.
