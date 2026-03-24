# SE446 - Milestone 1: Chicago Crime Analytics with MapReduce

## Group 4

| Name | Student ID |
|------|------------|
| Dana Ghassan | 231435|
| Sema Raslan | 231476|
| Yomna Kassem | 231158|
| Sara Elhams | 201575|

## Executive Summary

This project implements a MapReduce pipeline on a Hadoop cluster to analyze the Chicago Crimes dataset. We wrote four mapper scripts (one per team member) to answer key questions about crime types, locations, yearly trends, and arrest rates. All jobs were run using Hadoop Streaming with Python on a dataset of 793,073 crime records. Each task was first validated on a 10,000-record sample before running on the full dataset.

---

## Task 2: Crime Type Distribution

**Research Question**: What are the most common types of crimes in Chicago?

### Mapper: `src/mapper_task2.py`

### Command (Sample Test)
```bash
mapred streaming -files mapper_task2.py,reducer_sum.py -mapper "python3 mapper_task2.py" -reducer "python3 reducer_sum.py" -input /data/chicago_crimes_sample.csv -output /user/dghassan/project/m1/task2
```

### Command (Full Dataset)
```bash
mapred streaming -files mapper_task2.py,reducer_sum.py -mapper "python3 mapper_task2.py" -reducer "python3 reducer_sum.py" -input /data/chicago_crimes.csv -output /user/dghassan/project/m1/task2_full
```

### Top 5 Results (Full Dataset)
```
THEFT             162688
BATTERY           151930
CRIMINAL DAMAGE    91241
NARCOTICS          74127
ASSAULT            54070
```

### Interpretation
Theft is the most prevalent crime in Chicago, accounting for the largest share of all reported incidents, followed closely by battery — together these two categories represent over 40% of all crimes.

### Full Execution Log

```
dghassan@master-node:~$ cat > mapper_task2.py << 'EOF'
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split(',')
    if len(parts) <= 5:
        continue
    if parts[0] == 'ID':
        continue
    crime_type = parts[5]
    print(f"{crime_type}\t1")
EOF

dghassan@master-node:~$ mapred streaming -files mapper_task2.py,reducer_sum.py -mapper "python3 mapper_task2.py" -reducer "python3 reducer_sum.py" -input /data/chicago_crimes_sample.csv -output /user/dghassan/project/m1/task2
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob15194390713880043587.jar tmpDir=null
2026-03-20 01:50:24,134 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-20 01:50:24,489 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-20 01:50:25,034 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/dghassan/.staging/job_1771402826595_0098
2026-03-20 01:50:26,920 INFO mapred.FileInputFormat: Total input files to process : 1
2026-03-20 01:50:27,622 INFO mapreduce.JobSubmitter: number of splits:2
2026-03-20 01:50:28,668 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0098
2026-03-20 01:50:28,668 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-03-20 01:50:29,028 INFO conf.Configuration: resource-types.xml not found
2026-03-20 01:50:29,028 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-03-20 01:50:29,169 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0098
2026-03-20 01:50:29,252 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0098/
2026-03-20 01:50:29,255 INFO mapreduce.Job: Running job: job_1771402826595_0098
2026-03-20 01:50:44,904 INFO mapreduce.Job: Job job_1771402826595_0098 running in uber mode : false
2026-03-20 01:50:44,906 INFO mapreduce.Job:  map 0% reduce 0%
2026-03-20 01:51:04,733 INFO mapreduce.Job:  map 100% reduce 0%
2026-03-20 01:51:16,752 INFO mapreduce.Job:  map 100% reduce 100%
2026-03-20 01:51:19,530 INFO mapreduce.Job: Job job_1771402826595_0098 completed successfully
2026-03-20 01:51:19,791 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=159339
		FILE: Number of bytes written=1261832
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=2391502
		HDFS: Number of bytes written=541
		HDFS: Number of read operations=11
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
		Total time spent by all maps in occupied slots (ms)=66736
		Total time spent by all reduces in occupied slots (ms)=18664
		Total time spent by all map tasks (ms)=33368
		Total time spent by all reduce tasks (ms)=9332
		Total vcore-milliseconds taken by all map tasks=33368
		Total vcore-milliseconds taken by all reduce tasks=9332
		Total megabyte-milliseconds taken by all map tasks=17084416
		Total megabyte-milliseconds taken by all reduce tasks=4777984
	Map-Reduce Framework
		Map input records=10001
		Map output records=10000
		Map output bytes=139333
		Map output materialized bytes=159345
		Input split bytes=212
		Combine input records=0
		Combine output records=0
		Reduce input groups=29
		Reduce shuffle bytes=159345
		Reduce input records=10000
		Reduce output records=29
		Spilled Records=20000
		Shuffled Maps =2
		Failed Shuffles=0
		Merged Map outputs=2
		GC time elapsed (ms)=585
		CPU time spent (ms)=3730
		Physical memory (bytes) snapshot=639725568
		Virtual memory (bytes) snapshot=6558765056
		Total committed heap usage (bytes)=348094464
		Peak Map Physical memory (bytes)=247119872
		Peak Map Virtual memory (bytes)=2184937472
		Peak Reduce Physical memory (bytes)=147001344
		Peak Reduce Virtual memory (bytes)=2190131200
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters
		Bytes Read=2391290
	File Output Format Counters
		Bytes Written=541
2026-03-20 01:51:19,797 INFO streaming.StreamJob: Output directory: /user/dghassan/project/m1/task2

dghassan@master-node:~$ hdfs dfs -cat /user/dghassan/project/m1/task2/part-00000
ARSON	21
ASSAULT	878
BATTERY	1728
BURGLARY	316
CONCEALED CARRY LICENSE VIOLATION	6
CRIM SEXUAL ASSAULT	4
CRIMINAL DAMAGE	1062
CRIMINAL SEXUAL ASSAULT	107
CRIMINAL TRESPASS	153
DECEPTIVE PRACTICE	799
GAMBLING	1
HOMICIDE	44
HUMAN TRAFFICKING	2
INTERFERENCE WITH PUBLIC OFFICER	26
INTIMIDATION	5
KIDNAPPING	5
LIQUOR LAW VIOLATION	6
MOTOR VEHICLE THEFT	948
NARCOTICS	159
OBSCENITY	1
OFFENSE INVOLVING CHILDREN	137
OTHER OFFENSE	586
PROSTITUTION	6
PUBLIC PEACE VIOLATION	34
ROBBERY	508
SEX OFFENSE	96
STALKING	24
THEFT	2054
WEAPONS VIOLATION	284

dghassan@master-node:~$ mapred streaming -files mapper_task2.py,reducer_sum.py -mapper "python3 mapper_task2.py" -reducer "python3 reducer_sum.py" -input /data/chicago_crimes.csv -output /user/dghassan/project/m1/task2_full
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob59351546870918415.jar tmpDir=null
2026-03-20 05:41:33,769 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-20 05:41:34,048 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-20 05:41:34,457 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/dghassan/.staging/job_1771402826595_0103
2026-03-20 05:41:35,970 INFO mapred.FileInputFormat: Total input files to process : 1
2026-03-20 05:41:36,012 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-03-20 05:41:36,014 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-03-20 05:41:36,662 INFO mapreduce.JobSubmitter: number of splits:2
2026-03-20 05:41:37,514 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0103
2026-03-20 05:41:37,515 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-03-20 05:41:37,818 INFO conf.Configuration: resource-types.xml not found
2026-03-20 05:41:37,819 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-03-20 05:41:37,903 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0103
2026-03-20 05:41:37,941 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0103/
2026-03-20 05:41:37,943 INFO mapreduce.Job: Running job: job_1771402826595_0103
2026-03-20 05:41:54,691 INFO mapreduce.Job: Job job_1771402826595_0103 running in uber mode : false
2026-03-20 05:41:54,693 INFO mapreduce.Job:  map 0% reduce 0%
2026-03-20 05:42:20,665 INFO mapreduce.Job:  map 50% reduce 0%
2026-03-20 05:42:21,896 INFO mapreduce.Job:  map 100% reduce 0%
2026-03-20 05:42:34,245 INFO mapreduce.Job:  map 100% reduce 100%
2026-03-20 05:42:37,170 INFO mapreduce.Job: Job job_1771402826595_0103 completed successfully
2026-03-20 05:42:37,471 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=11798790
		FILE: Number of bytes written=24540719
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=181964998
		HDFS: Number of bytes written=690
		HDFS: Number of read operations=11
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
		Total time spent by all maps in occupied slots (ms)=94030
		Total time spent by all reduces in occupied slots (ms)=20960
		Total time spent by all map tasks (ms)=47015
		Total time spent by all reduce tasks (ms)=10480
		Total vcore-milliseconds taken by all map tasks=47015
		Total vcore-milliseconds taken by all reduce tasks=10480
		Total megabyte-milliseconds taken by all map tasks=24071680
		Total megabyte-milliseconds taken by all reduce tasks=5365760
	Map-Reduce Framework
		Map input records=793074
		Map output records=793072
		Map output bytes=10212640
		Map output materialized bytes=11798796
		Input split bytes=198
		Combine input records=0
		Combine output records=0
		Reduce input groups=34
		Reduce shuffle bytes=11798796
		Reduce input records=793072
		Reduce output records=34
		Spilled Records=1586144
		Shuffled Maps =2
		Failed Shuffles=0
		Merged Map outputs=2
		GC time elapsed (ms)=969
		CPU time spent (ms)=9890
		Physical memory (bytes) snapshot=687804416
		Virtual memory (bytes) snapshot=6560825344
		Total committed heap usage (bytes)=348151808
		Peak Map Physical memory (bytes)=269193216
		Peak Map Virtual memory (bytes)=2185113600
		Peak Reduce Physical memory (bytes)=164540416
		Peak Reduce Virtual memory (bytes)=2190934016
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters
		Bytes Read=181964800
	File Output Format Counters
		Bytes Written=690
2026-03-20 05:42:37,472 INFO streaming.StreamJob: Output directory: /user/dghassan/project/m1/task2_full

dghassan@master-node:~$ hdfs dfs -cat /user/dghassan/project/m1/task2_full/part-00000
ARSON	1717
ASSAULT	54070
BATTERY	151930
BURGLARY	39872
CONCEALED CARRY LICENSE VIOLATION	77
CRIM SEXUAL ASSAULT	2463
CRIMINAL DAMAGE	91241
CRIMINAL SEXUAL ASSAULT	1372
CRIMINAL TRESPASS	21476
DECEPTIVE PRACTICE	30396
DOMESTIC VIOLENCE	1
GAMBLING	1314
HOMICIDE	13173
HUMAN TRAFFICKING	13
INTERFERENCE WITH PUBLIC OFFICER	803
INTIMIDATION	92
KIDNAPPING	1108
LIQUOR LAW VIOLATION	2349
MOTOR VEHICLE THEFT	48494
NARCOTICS	74127
NON-CRIMINAL	1
OBSCENITY	24
OFFENSE INVOLVING CHILDREN	2065
OTHER NARCOTIC VIOLATION	11
OTHER OFFENSE	36893
PROSTITUTION	9100
PUBLIC INDECENCY	17
PUBLIC PEACE VIOLATION	1827
RITUALISM	8
ROBBERY	30991
SEX OFFENSE	3932
STALKING	534
THEFT	162688
WEAPONS VIOLATION	8893
```

---

## Task 3: Location Hotspots

**Research Question**: Where do most crimes occur?

### Mapper: `src/mapper_task3.py`

### Top 5 Results (Full Dataset)
```
STREET            245437
RESIDENCE         136238
APARTMENT          60925
SIDEWALK           47407
OTHER              29213
```

### Interpretation
Streets are by far the most common crime location, indicating that outdoor public spaces require the highest patrol priority, with residential areas following as the second most dangerous zone.

### Execution Log
*(To be added by Sema)*

---

## Task 4: The Time Dimension

**Research Question**: How has the total number of crimes changed over the years?

### Mapper: `src/mapper_task4.py`

### Top 5 Results (Full Dataset)
```
2001    467301
2002    205267
2023     81461
2025     12710
2022      4678
```

### Interpretation
Crime volume was highest in the early 2000s, with a sharp decline over the following decades, suggesting a long-term downward trend in reported incidents across Chicago.

### Execution Log
*(To be added by Yomna)*

---

## Task 5: Law Enforcement Analysis

**Research Question**: What percentage of crimes result in an arrest?

### Mapper: `src/mapper_task5.py`

### Results (Full Dataset)
```
false    551554
true     215199
```

### Interpretation
Only approximately 28% of crimes result in an arrest, meaning nearly 3 out of 4 criminal incidents do not lead to a direct apprehension, indicating significant room for improvement in patrol efficiency.

### Execution Log
selhams@master-node:~/se446-project-group-4/src$ nano mapper_task5.py
selhams@master-node:~/se446-project-group-4/src$ hdfs dfs -rm -r /user/selhams/task5_output
Deleted /user/selhams/task5_output
selhams@master-node:~/se446-project-group-4/src$ mapred streaming -files mapper_task5.py,reducer_sum.py \
-mapper "python3 mapper_task5.py" \
-reducer "python3 reducer_sum.py" \
-input /data/chicago_crimes.csv \
-output /user/selhams/task5_output
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob6033867016865857457.jar tmpDir=null
2026-03-24 03:14:23,488 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-24 03:14:23,920 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-24 03:14:24,443 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/selhams/.staging/job_1771402826595_0151
2026-03-24 03:14:26,255 INFO mapred.FileInputFormat: Total input files to process : 1
2026-03-24 03:14:26,291 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-03-24 03:14:26,292 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-03-24 03:14:26,942 INFO mapreduce.JobSubmitter: number of splits:2
2026-03-24 03:14:27,706 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0151
2026-03-24 03:14:27,706 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-03-24 03:14:28,024 INFO conf.Configuration: resource-types.xml not found
2026-03-24 03:14:28,025 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-03-24 03:14:28,137 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0151
2026-03-24 03:14:28,198 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0151/
2026-03-24 03:14:28,200 INFO mapreduce.Job: Running job: job_1771402826595_0151
2026-03-24 03:14:45,733 INFO mapreduce.Job: Job job_1771402826595_0151 running in uber mode : false
2026-03-24 03:14:45,735 INFO mapreduce.Job:  map 0% reduce 0%
2026-03-24 03:15:11,353 INFO mapreduce.Job:  map 100% reduce 0%
2026-03-24 03:15:24,480 INFO mapreduce.Job:  map 100% reduce 100%
2026-03-24 03:15:27,235 INFO mapreduce.Job: Job job_1771402826595_0151 completed successfully
2026-03-24 03:15:27,468 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=7452337
		FILE: Number of bytes written=15847909
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=181964998
		HDFS: Number of bytes written=25
		HDFS: Number of read operations=11
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters 
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
		Total time spent by all maps in occupied slots (ms)=93810
		Total time spent by all reduces in occupied slots (ms)=20908
		Total time spent by all map tasks (ms)=46905
		Total time spent by all reduce tasks (ms)=10454
		Total vcore-milliseconds taken by all map tasks=46905
		Total vcore-milliseconds taken by all reduce tasks=10454
		Total megabyte-milliseconds taken by all map tasks=24015360
		Total megabyte-milliseconds taken by all reduce tasks=5352448
	Map-Reduce Framework
		Map input records=793074
		Map output records=766753
		Map output bytes=5918825
		Map output materialized bytes=7452343
		Input split bytes=198
		Combine input records=0
		Combine output records=0
		Reduce input groups=2
		Reduce shuffle bytes=7452343
		Reduce input records=766753
		Reduce output records=2
		Spilled Records=1533506
		Shuffled Maps =2
		Failed Shuffles=0
		Merged Map outputs=2
		GC time elapsed (ms)=691
		CPU time spent (ms)=9570
		Physical memory (bytes) snapshot=659865600
		Virtual memory (bytes) snapshot=6560432128
		Total committed heap usage (bytes)=348090368
		Peak Map Physical memory (bytes)=250732544
		Peak Map Virtual memory (bytes)=2186137600
		Peak Reduce Physical memory (bytes)=161832960
		Peak Reduce Virtual memory (bytes)=2190139392
	Shuffle Errors
		BAD_ID=0
		CONNECTION=0
		IO_ERROR=0
		WRONG_LENGTH=0
		WRONG_MAP=0
		WRONG_REDUCE=0
	File Input Format Counters 
		Bytes Read=181964800
	File Output Format Counters 
		Bytes Written=25
2026-03-24 03:15:27,469 INFO streaming.StreamJob: Output directory: /user/selhams/task5_output
selhams@master-node:~/se446-project-group-4/src$ hdfs dfs -cat /user/selhams/task5_output/part-00000
false	551554
true	215199

---

## Member Contributions

| Name | Task | Contribution |
|------|------|-------------|
| Dana Ghassan | Task 2 | Wrote `mapper_task2.py`, ran job on cluster, documented results |
| Sema Raslan | Task 3 | Wrote `mapper_task3.py`, ran job on cluster, documented results |
| Yomna Kassem | Task 4 | Wrote `mapper_task4.py`, ran job on cluster, documented results |
| Sara Elhams | Task 5 | Wrote `mapper_task5.py`, ran job on cluster, documented results |
