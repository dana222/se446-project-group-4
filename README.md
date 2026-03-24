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
```
soraslan@master-node:~$ ssh soraslan@134.209.172.50
soraslan@134.209.172.50's password: 
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-170-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Mon Mar 23 21:43:05 UTC 2026

  System load:  0.19               Processes:             130
  Usage of /:   21.8% of 77.35GB   Users logged in:       2
  Memory usage: 50%                IPv4 address for eth0: 134.209.172.50
  Swap usage:   0%                 IPv4 address for eth0: 10.17.0.5

Expanded Security Maintenance for Applications is not enabled.

12 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

New release '24.04.4 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


*** System restart required ***
Last login: Wed Feb 18 07:23:06 2026 from 5.163.161.127
soraslan@master-node:~$ cat > mapper_task3.py << 'EOF'
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split(',')
    if len(parts) <= 7:
        continue
    if parts[0] == 'ID':
        continue
    location = parts[7]
    print(f"{location}\t1")
EOF
soraslan@master-node:~$ mapred streaming -files mapper_task3.py,reducer_sum.py -mapper "python3 mapper_task3.py" -reducer "python3 reducer_sum.py" -input /data/chicago_crimes_sample.csv -output /user/semaraslan/project/m1/task3
Exception in thread "main" java.io.FileNotFoundException: File reducer_sum.py does not exist
	at org.apache.hadoop.fs.RawLocalFileSystem.deprecatedGetFileStatus(RawLocalFileSystem.java:917)
	at org.apache.hadoop.fs.RawLocalFileSystem.getFileLinkStatusInternal(RawLocalFileSystem.java:1238)
	at org.apache.hadoop.fs.RawLocalFileSystem.getFileStatus(RawLocalFileSystem.java:907)
	at org.apache.hadoop.fs.FilterFileSystem.getFileStatus(FilterFileSystem.java:462)
	at org.apache.hadoop.util.GenericOptionsParser.validateFiles(GenericOptionsParser.java:461)
	at org.apache.hadoop.util.GenericOptionsParser.validateFiles(GenericOptionsParser.java:406)
	at org.apache.hadoop.util.GenericOptionsParser.processGeneralOptions(GenericOptionsParser.java:338)
	at org.apache.hadoop.util.GenericOptionsParser.parseGeneralOptions(GenericOptionsParser.java:579)
	at org.apache.hadoop.util.GenericOptionsParser.<init>(GenericOptionsParser.java:181)
	at org.apache.hadoop.util.GenericOptionsParser.<init>(GenericOptionsParser.java:163)
	at org.apache.hadoop.util.ToolRunner.run(ToolRunner.java:76)
	at org.apache.hadoop.util.ToolRunner.run(ToolRunner.java:97)
	at org.apache.hadoop.streaming.HadoopStreaming.main(HadoopStreaming.java:50)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
	at org.apache.hadoop.util.RunJar.run(RunJar.java:330)
	at org.apache.hadoop.util.RunJar.main(RunJar.java:245)
soraslan@master-node:~$ hdfs dfs -cat /user/semaraslan/project/m1/task3/part-00000
cat: `/user/semaraslan/project/m1/task3/part-00000': No such file or directory
soraslan@master-node:~$ mapred streaming -files mapper_task3.py,reducer_sum.py -mapper "python3 mapper_task3.py" -reducer "python3 reducer_sum.py" -input /data/chicago_crimes.csv -output /user/semaraslan/project/m1/task3_full
Exception in thread "main" java.io.FileNotFoundException: File reducer_sum.py does not exist
	at org.apache.hadoop.fs.RawLocalFileSystem.deprecatedGetFileStatus(RawLocalFileSystem.java:917)
	at org.apache.hadoop.fs.RawLocalFileSystem.getFileLinkStatusInternal(RawLocalFileSystem.java:1238)
	at org.apache.hadoop.fs.RawLocalFileSystem.getFileStatus(RawLocalFileSystem.java:907)
	at org.apache.hadoop.fs.FilterFileSystem.getFileStatus(FilterFileSystem.java:462)
	at org.apache.hadoop.util.GenericOptionsParser.validateFiles(GenericOptionsParser.java:461)
	at org.apache.hadoop.util.GenericOptionsParser.validateFiles(GenericOptionsParser.java:406)
	at org.apache.hadoop.util.GenericOptionsParser.processGeneralOptions(GenericOptionsParser.java:338)
	at org.apache.hadoop.util.GenericOptionsParser.parseGeneralOptions(GenericOptionsParser.java:579)
	at org.apache.hadoop.util.GenericOptionsParser.<init>(GenericOptionsParser.java:181)
	at org.apache.hadoop.util.GenericOptionsParser.<init>(GenericOptionsParser.java:163)
	at org.apache.hadoop.util.ToolRunner.run(ToolRunner.java:76)
	at org.apache.hadoop.util.ToolRunner.run(ToolRunner.java:97)
	at org.apache.hadoop.streaming.HadoopStreaming.main(HadoopStreaming.java:50)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
	at org.apache.hadoop.util.RunJar.run(RunJar.java:330)
	at org.apache.hadoop.util.RunJar.main(RunJar.java:245)
soraslan@master-node:~$ cat > reducer_sum.py << 'EOF'
#!/usr/bin/env python3
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    key, value = line.split('\t')
    value = int(value)
    if key == current_key:
        current_count += value
    else:
        if current_key is not None:
            print(f"{current_key}\t{current_count}")
        current_key = key
        current_count = value

if current_key is not None:
    print(f"{current_key}\t{current_count}")
EOF
soraslan@master-node:~$ mapred streaming -files mapper_task3.py,reducer_sum.py -mapper "python3 mapper_task3.py" -reducer "python3 reducer_sum.py" -input /data/chicago_crimes_sample.csv -output /user/soraslan/project/m1/task3
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob4864450002323427621.jar tmpDir=null
2026-03-23 21:45:22,842 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-23 21:45:23,185 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-23 21:45:23,604 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/soraslan/.staging/job_1771402826595_0142
2026-03-23 21:45:25,251 INFO mapred.FileInputFormat: Total input files to process : 1
2026-03-23 21:45:25,945 INFO mapreduce.JobSubmitter: number of splits:2
2026-03-23 21:45:26,909 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0142
2026-03-23 21:45:26,909 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-03-23 21:45:27,243 INFO conf.Configuration: resource-types.xml not found
2026-03-23 21:45:27,244 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-03-23 21:45:27,375 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0142
2026-03-23 21:45:27,437 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0142/
2026-03-23 21:45:27,440 INFO mapreduce.Job: Running job: job_1771402826595_0142
2026-03-23 21:45:43,156 INFO mapreduce.Job: Job job_1771402826595_0142 running in uber mode : false
2026-03-23 21:45:43,159 INFO mapreduce.Job:  map 0% reduce 0%
2026-03-23 21:46:05,075 INFO mapreduce.Job:  map 100% reduce 0%
2026-03-23 21:46:16,078 INFO mapreduce.Job: Task Id : attempt_1771402826595_0142_r_000000_0, Status : FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 1
	at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:326)
	at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:539)
	at org.apache.hadoop.streaming.PipeReducer.reduce(PipeReducer.java:127)
	at org.apache.hadoop.mapred.ReduceTask.runOldReducer(ReduceTask.java:445)
	at org.apache.hadoop.mapred.ReduceTask.run(ReduceTask.java:393)
	at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:178)
	at java.base/java.security.AccessController.doPrivileged(Native Method)
	at java.base/javax.security.auth.Subject.doAs(Subject.java:423)
	at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1953)
	at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:172)

2026-03-23 21:46:25,929 INFO mapreduce.Job: Task Id : attempt_1771402826595_0142_r_000000_1, Status : FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 1
	at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:326)
	at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:539)
	at org.apache.hadoop.streaming.PipeReducer.reduce(PipeReducer.java:127)
	at org.apache.hadoop.mapred.ReduceTask.runOldReducer(ReduceTask.java:445)
	at org.apache.hadoop.mapred.ReduceTask.run(ReduceTask.java:393)
	at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:178)
	at java.base/java.security.AccessController.doPrivileged(Native Method)
	at java.base/javax.security.auth.Subject.doAs(Subject.java:423)
	at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1953)
	at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:172)

2026-03-23 21:46:34,514 INFO mapreduce.Job: Task Id : attempt_1771402826595_0142_r_000000_2, Status : FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 1
	at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:326)
	at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:539)
	at org.apache.hadoop.streaming.PipeReducer.reduce(PipeReducer.java:127)
	at org.apache.hadoop.mapred.ReduceTask.runOldReducer(ReduceTask.java:445)
	at org.apache.hadoop.mapred.ReduceTask.run(ReduceTask.java:393)
	at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:178)
	at java.base/java.security.AccessController.doPrivileged(Native Method)
	at java.base/javax.security.auth.Subject.doAs(Subject.java:423)
	at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1953)
	at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:172)

2026-03-23 21:46:47,838 INFO mapreduce.Job:  map 100% reduce 100%
2026-03-23 21:46:49,468 INFO mapreduce.Job: Job job_1771402826595_0142 failed with state FAILED due to: Task failed task_1771402826595_0142_r_000000
Job failed as tasks failed. failedMaps:0 failedReduces:1 killedMaps:0 killedReduces: 0

2026-03-23 21:46:49,835 INFO mapreduce.Job: Counters: 40
	File System Counters
		FILE: Number of bytes read=0
		FILE: Number of bytes written=795008
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=2391502
		HDFS: Number of bytes written=0
		HDFS: Number of read operations=6
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=0
		HDFS: Number of bytes read erasure-coded=0
	Job Counters 
		Failed reduce tasks=4
		Launched map tasks=2
		Launched reduce tasks=4
		Data-local map tasks=2
		Total time spent by all maps in occupied slots (ms)=75694
		Total time spent by all reduces in occupied slots (ms)=63450
		Total time spent by all map tasks (ms)=37847
		Total time spent by all reduce tasks (ms)=31725
		Total vcore-milliseconds taken by all map tasks=37847
		Total vcore-milliseconds taken by all reduce tasks=31725
		Total megabyte-milliseconds taken by all map tasks=19377664
		Total megabyte-milliseconds taken by all reduce tasks=16243200
	Map-Reduce Framework
		Map input records=10001
		Map output records=10000
		Map output bytes=146196
		Map output materialized bytes=166208
		Input split bytes=212
		Combine input records=0
		Spilled Records=10000
		Failed Shuffles=0
		Merged Map outputs=0
		GC time elapsed (ms)=608
		CPU time spent (ms)=2880
		Physical memory (bytes) snapshot=515158016
		Virtual memory (bytes) snapshot=4372615168
		Total committed heap usage (bytes)=303120384
		Peak Map Physical memory (bytes)=263802880
		Peak Map Virtual memory (bytes)=2187567104
	File Input Format Counters 
		Bytes Read=2391290
2026-03-23 21:46:49,854 ERROR streaming.StreamJob: Job not successful!
Streaming Command Failed!
soraslan@master-node:~$ rm reducer_sum.py
soraslan@master-node:~$ cat > reducer_sum.py << 'EOF'
#!/usr/bin/env python3
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 2:
        continue
    key = parts[0]
    try:
        value = int(parts[1])
    except ValueError:
        continue
    if key == current_key:
        current_count += value
    else:
        if current_key is not None:
            print(f"{current_key}\t{current_count}")
        current_key = key
        current_count = value

if current_key is not None:
    print(f"{current_key}\t{current_count}")
EOF
soraslan@master-node:~$ hdfs dfs -rm -r /user/soraslan/project/m1/task3
Deleted /user/soraslan/project/m1/task3
soraslan@master-node:~$ mapred streaming -files mapper_task3.py,reducer_sum.py -mapper "python3 mapper_task3.py" -reducer "python3 reducer_sum.py" -input /data/chicago_crimes_sample.csv -output /user/soraslan/project/m1/task3
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob4762180983214250182.jar tmpDir=null
2026-03-23 21:48:33,457 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-23 21:48:33,777 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-23 21:48:34,229 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/soraslan/.staging/job_1771402826595_0144
2026-03-23 21:48:35,908 INFO mapred.FileInputFormat: Total input files to process : 1
2026-03-23 21:48:36,567 INFO mapreduce.JobSubmitter: number of splits:2
2026-03-23 21:48:37,518 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0144
2026-03-23 21:48:37,519 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-03-23 21:48:37,834 INFO conf.Configuration: resource-types.xml not found
2026-03-23 21:48:37,835 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-03-23 21:48:37,950 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0144
2026-03-23 21:48:38,008 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0144/
2026-03-23 21:48:38,011 INFO mapreduce.Job: Running job: job_1771402826595_0144
2026-03-23 21:48:53,744 INFO mapreduce.Job: Job job_1771402826595_0144 running in uber mode : false
2026-03-23 21:48:53,746 INFO mapreduce.Job:  map 0% reduce 0%
2026-03-23 21:49:12,748 INFO mapreduce.Job:  map 100% reduce 0%
2026-03-23 21:49:24,849 INFO mapreduce.Job:  map 100% reduce 100%
2026-03-23 21:49:27,688 INFO mapreduce.Job: Job job_1771402826595_0144 completed successfully
2026-03-23 21:49:27,923 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=166202
		FILE: Number of bytes written=1275555
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=2391502
		HDFS: Number of bytes written=2673
		HDFS: Number of read operations=11
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters 
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
		Total time spent by all maps in occupied slots (ms)=66878
		Total time spent by all reduces in occupied slots (ms)=17988
		Total time spent by all map tasks (ms)=33439
		Total time spent by all reduce tasks (ms)=8994
		Total vcore-milliseconds taken by all map tasks=33439
		Total vcore-milliseconds taken by all reduce tasks=8994
		Total megabyte-milliseconds taken by all map tasks=17120768
		Total megabyte-milliseconds taken by all reduce tasks=4604928
	Map-Reduce Framework
		Map input records=10001
		Map output records=10000
		Map output bytes=146196
		Map output materialized bytes=166208
		Input split bytes=212
		Combine input records=0
		Combine output records=0
		Reduce input groups=116
		Reduce shuffle bytes=166208
		Reduce input records=10000
		Reduce output records=115
		Spilled Records=20000
		Shuffled Maps =2
		Failed Shuffles=0
		Merged Map outputs=2
		GC time elapsed (ms)=632
		CPU time spent (ms)=3100
		Physical memory (bytes) snapshot=641925120
		Virtual memory (bytes) snapshot=6559076352
		Total committed heap usage (bytes)=348143616
		Peak Map Physical memory (bytes)=251813888
		Peak Map Virtual memory (bytes)=2184675328
		Peak Reduce Physical memory (bytes)=144707584
		Peak Reduce Virtual memory (bytes)=2190299136
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
		Bytes Written=2673
2026-03-23 21:49:27,938 INFO streaming.StreamJob: Output directory: /user/soraslan/project/m1/task3
soraslan@master-node:~$ hdfs dfs -cat /user/soraslan/project/m1/task3/part-00000
BUS	4
FISTS	131
MOTOR VEHICLE"	12
SCOOTER	38
"VEHICLE - OTHER RIDE SHARE SERVICE (LYFT	5
ABANDONED BUILDING	2
AIRCRAFT	1
AIRPORT BUILDING NON-TERMINAL - NON-SECURE AREA	2
AIRPORT EXTERIOR - NON-SECURE AREA	2
AIRPORT EXTERIOR - SECURE AREA	3
AIRPORT PARKING LOT	8
AIRPORT TERMINAL LOWER LEVEL - NON-SECURE AREA	5
AIRPORT TERMINAL LOWER LEVEL - SECURE AREA	5
AIRPORT TERMINAL UPPER LEVEL - NON-SECURE AREA	4
AIRPORT TERMINAL UPPER LEVEL - SECURE AREA	11
AIRPORT TRANSPORTATION SYSTEM (ATS)	1
AIRPORT VENDING ESTABLISHMENT	1
AIRPORT/AIRCRAFT	1
ALLEY	216
ANIMAL HOSPITAL	2
APARTMENT	1868
APPLIANCE STORE	5
ATHLETIC CLUB	14
ATM (AUTOMATIC TELLER MACHINE)	8
AUTO	2
AUTO / BOAT / RV DEALERSHIP	9
BANK	37
BAR OR TAVERN	84
BARBERSHOP	5
BOAT / WATERCRAFT	1
BRIDGE	2
CAR WASH	9
CEMETARY	2
CHA APARTMENT	15
CHA HALLWAY / STAIRWELL / ELEVATOR	7
CHA PARKING LOT / GROUNDS	17
CHURCH / SYNAGOGUE / PLACE OF WORSHIP	16
CLEANING STORE	1
COIN OPERATED MACHINE	1
COLLEGE / UNIVERSITY - GROUNDS	3
COLLEGE / UNIVERSITY - RESIDENCE HALL	2
COMMERCIAL / BUSINESS OFFICE	121
CONSTRUCTION SITE	11
CONVENIENCE STORE	51
CREDIT UNION	1
CTA BUS	44
CTA BUS STOP	16
CTA PARKING LOT / GARAGE / OTHER PROPERTY	5
CTA PLATFORM	24
CTA STATION	22
CTA TRACKS - RIGHT OF WAY	3
CTA TRAIN	49
CURRENCY EXCHANGE	6
DAY CARE CENTER	6
DEPARTMENT STORE	134
DRIVEWAY - RESIDENTIAL	25
DRUG STORE	46
FACTORY / MANUFACTURING BUILDING	3
FEDERAL BUILDING	1
GAS STATION	124
GAS STATION DRIVE/PROP.	1
GOVERNMENT BUILDING / PROPERTY	19
GROCERY FOOD STORE	91
HALLWAY	1
HIGHWAY / EXPRESSWAY	3
HOSPITAL BUILDING / GROUNDS	42
HOSPITAL BUILDING/GROUNDS	1
HOTEL / MOTEL	41
HOTEL/MOTEL	3
HOUSE	1
JAIL / LOCK-UP FACILITY	2
LAKEFRONT / WATERFRONT / RIVERBANK	4
LIBRARY	6
MEDICAL / DENTAL OFFICE	11
MOTOR VEH"	1
MOVIE HOUSE / THEATER	5
NURSING / RETIREMENT HOME	42
NURSING HOME/RETIREMENT HOME	1
OTHER	9
OTHER (SPECIFY)	154
OTHER COMMERCIAL TRANSPORTATION	5
OTHER RAILROAD PROPERTY / TRAIN DEPOT	3
PARK PROPERTY	91
PARKING LOT / GARAGE (NON RESIDENTIAL)	355
PARKING LOT/GARAGE(NON.RESID.)	1
PAWN SHOP	1
POLICE FACILITY / VEHICLE PARKING LOT	38
POLICE FACILITY/VEH PARKING LOT	1
PORCH	2
RESIDENCE	1344
RESIDENCE - GARAGE	114
RESIDENCE - PORCH / HALLWAY	100
RESIDENCE - YARD (FRONT / BACK)	126
RESIDENCE PORCH/HALLWAY	1
RESIDENCE-GARAGE	1
RESTAURANT	186
RETAIL STORE	1
SCHOOL - PRIVATE BUILDING	13
SCHOOL - PRIVATE GROUNDS	9
SCHOOL - PUBLIC BUILDING	76
SCHOOL - PUBLIC GROUNDS	75
SIDEWALK	524
SMALL RETAIL STORE	234
SPORTS ARENA / STADIUM	13
STREET	2686
TAVERN / LIQUOR STORE	17
TAXICAB	6
VACANT LOT	1
VACANT LOT / LAND	30
VACANT LOT/LAND	2
VEHICLE - COMMERCIAL	10
VEHICLE - DELIVERY TRUCK	1
VEHICLE NON-COMMERCIAL	138
VESTIBULE	1
WAREHOUSE	9
soraslan@master-node:~$ mapred streaming -files mapper_task3.py,reducer_sum.py -mapper "python3 mapper_task3.py" -reducer "python3 reducer_sum.py" -input /data/chicago_crimes.csv -output /user/soraslan/project/m1/task3_full

# View full results
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob3112774066996495010.jar tmpDir=null
2026-03-23 21:50:31,773 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-23 21:50:32,082 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-23 21:50:32,536 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/soraslan/.staging/job_1771402826595_0145
2026-03-23 21:50:34,290 INFO mapred.FileInputFormat: Total input files to process : 1
2026-03-23 21:50:34,318 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-03-23 21:50:34,320 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-03-23 21:50:34,924 INFO mapreduce.JobSubmitter: number of splits:2
2026-03-23 21:50:35,899 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0145
2026-03-23 21:50:35,899 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-03-23 21:50:36,254 INFO conf.Configuration: resource-types.xml not found
2026-03-23 21:50:36,255 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-03-23 21:50:36,406 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0145
2026-03-23 21:50:36,457 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0145/
2026-03-23 21:50:36,460 INFO mapreduce.Job: Running job: job_1771402826595_0145
2026-03-23 21:50:53,125 INFO mapreduce.Job: Job job_1771402826595_0145 running in uber mode : false
2026-03-23 21:50:53,128 INFO mapreduce.Job:  map 0% reduce 0%
2026-03-23 21:51:17,177 INFO mapreduce.Job:  map 100% reduce 0%
2026-03-23 21:51:30,732 INFO mapreduce.Job:  map 100% reduce 100%
2026-03-23 21:51:33,656 INFO mapreduce.Job: Job job_1771402826595_0145 completed successfully
2026-03-23 21:51:33,884 INFO mapreduce.Job: Counters: 54
	File System Counters
		FILE: Number of bytes read=12346200
		FILE: Number of bytes written=25635545
		FILE: Number of read operations=0
		FILE: Number of large read operations=0
		FILE: Number of write operations=0
		HDFS: Number of bytes read=181964998
		HDFS: Number of bytes written=4757
		HDFS: Number of read operations=11
		HDFS: Number of large read operations=0
		HDFS: Number of write operations=2
		HDFS: Number of bytes read erasure-coded=0
	Job Counters 
		Launched map tasks=2
		Launched reduce tasks=1
		Data-local map tasks=2
		Total time spent by all maps in occupied slots (ms)=86192
		Total time spent by all reduces in occupied slots (ms)=21308
		Total time spent by all map tasks (ms)=43096
		Total time spent by all reduce tasks (ms)=10654
		Total vcore-milliseconds taken by all map tasks=43096
		Total vcore-milliseconds taken by all reduce tasks=10654
		Total megabyte-milliseconds taken by all map tasks=22065152
		Total megabyte-milliseconds taken by all reduce tasks=5454848
	Map-Reduce Framework
		Map input records=793074
		Map output records=793072
		Map output bytes=10760050
		Map output materialized bytes=12346206
		Input split bytes=198
		Combine input records=0
		Combine output records=0
		Reduce input groups=218
		Reduce shuffle bytes=12346206
		Reduce input records=793072
		Reduce output records=217
		Spilled Records=1586144
		Shuffled Maps =2
		Failed Shuffles=0
		Merged Map outputs=2
		GC time elapsed (ms)=593
		CPU time spent (ms)=9330
		Physical memory (bytes) snapshot=669429760
		Virtual memory (bytes) snapshot=6560256000
		Total committed heap usage (bytes)=348241920
		Peak Map Physical memory (bytes)=251404288
		Peak Map Virtual memory (bytes)=2184609792
		Peak Reduce Physical memory (bytes)=172478464
		Peak Reduce Virtual memory (bytes)=2191224832
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
		Bytes Written=4757
2026-03-23 21:51:33,903 INFO streaming.StreamJob: Output directory: /user/soraslan/project/m1/task3_full
soraslan@master-node:~$ hdfs dfs -cat /user/soraslan/project/m1/task3_full/part-00000
BUS	2658
FISTS	1157
MOTOR VEHICLE"	194
NON-MOTOR VEHICLE"	7
SCOOTER	477
"CTA ""L"" PLATFORM"	10
"CTA ""L"" TRAIN"	11
"SCHOOL	20516
"VEHICLE - OTHER RIDE SHARE SERVICE (LYFT	37
ABANDONED BUILDING	829
AIRCRAFT	34
AIRPORT BUILDING NON-TERMINAL - NON-SECURE AREA	33
AIRPORT BUILDING NON-TERMINAL - SECURE AREA	16
AIRPORT EXTERIOR - NON-SECURE AREA	33
AIRPORT EXTERIOR - SECURE AREA	20
AIRPORT PARKING LOT	81
AIRPORT TERMINAL LOWER LEVEL - NON-SECURE AREA	60
AIRPORT TERMINAL LOWER LEVEL - SECURE AREA	42
AIRPORT TERMINAL MEZZANINE - NON-SECURE AREA	4
AIRPORT TERMINAL UPPER LEVEL - NON-SECURE AREA	41
AIRPORT TERMINAL UPPER LEVEL - SECURE AREA	133
AIRPORT TRANSPORTATION SYSTEM (ATS)	12
AIRPORT VENDING ESTABLISHMENT	7
AIRPORT/AIRCRAFT	2753
ALLEY	18258
ANIMAL HOSPITAL	13
APARTMENT	60925
APPLIANCE STORE	269
ATHLETIC CLUB	465
ATM (AUTOMATIC TELLER MACHINE)	66
AUTO	1370
AUTO / BOAT / RV DEALERSHIP	92
BANK	3325
BANQUET HALL	2
BAR OR TAVERN	3380
BARBER SHOP/BEAUTY SALON	26
BARBERSHOP	642
BASEMENT	34
BEACH	1
BOAT / WATERCRAFT	4
BOAT/WATERCRAFT	66
BOWLING ALLEY	85
BRIDGE	28
BUS	427
CAR WASH	363
CASINO/GAMBLING ESTABLISHMENT	6
CEMETARY	31
CHA APARTMENT	8340
CHA BREEZEWAY	3
CHA ELEVATOR	3
CHA GROUNDS	48
CHA HALLWAY	39
CHA HALLWAY / STAIRWELL / ELEVATOR	60
CHA HALLWAY/STAIRWELL/ELEVATOR	4773
CHA LOBBY	7
CHA PARKING LOT	57
CHA PARKING LOT / GROUNDS	166
CHA PARKING LOT/GROUNDS	11846
CHA PLAY LOT	4
CHA STAIRWELL	10
CHURCH	6
CHURCH / SYNAGOGUE / PLACE OF WORSHIP	224
CHURCH PROPERTY	2
CHURCH/SYNAGOGUE/PLACE OF WORSHIP	1344
CLEANERS/LAUNDROMAT	1
CLEANING STORE	786
CLUB	18
COACH HOUSE	3
COIN OPERATED MACHINE	108
COLLEGE / UNIVERSITY - GROUNDS	43
COLLEGE / UNIVERSITY - RESIDENCE HALL	12
COLLEGE/UNIVERSITY GROUNDS	449
COLLEGE/UNIVERSITY RESIDENCE HALL	87
COMMERCIAL / BUSINESS OFFICE	8219
CONSTRUCTION SITE	1206
CONVENIENCE STORE	610
COUNTY JAIL	2
CREDIT UNION	42
CTA BUS	2147
CTA BUS STOP	182
CTA GARAGE / OTHER PROPERTY	10
CTA PARKING LOT / GARAGE / OTHER PROPERTY	68
CTA PLATFORM	4938
CTA PROPERTY	10
CTA STATION	185
CTA SUBWAY STATION	2
CTA TRACKS - RIGHT OF WAY	4
CTA TRAIN	1932
CURRENCY EXCHANGE	1277
DAY CARE CENTER	246
DELIVERY TRUCK	149
DEPARTMENT STORE	10818
DRIVEWAY	27
DRIVEWAY - RESIDENTIAL	1902
DRUG STORE	4469
DUMPSTER	7
ELEVATOR	2
EXPRESSWAY EMBANKMENT	1
FACTORY	2
FACTORY / MANUFACTURING BUILDING	53
FACTORY/MANUFACTURING BUILDING	910
FEDERAL BUILDING	85
FIRE STATION	125
FOREST PRESERVE	62
FUNERAL PARLOR	1
GANGWAY	73
GARAGE	73
GARAGE/AUTO REPAIR	11
GAS STATION	7703
GAS STATION DRIVE/PROP.	69
GOVERNMENT BUILDING	2
GOVERNMENT BUILDING / PROPERTY	365
GOVERNMENT BUILDING/PROPERTY	1447
GROCERY FOOD STORE	13029
HALLWAY	103
HIGHWAY / EXPRESSWAY	13
HIGHWAY/EXPRESSWAY	115
HOSPITAL	16
HOSPITAL BUILDING / GROUNDS	552
HOSPITAL BUILDING/GROUNDS	1962
HOTEL	27
HOTEL / MOTEL	513
HOTEL/MOTEL	3166
HOUSE	675
JAIL / LOCK-UP FACILITY	20
JUNK YARD/GARBAGE DUMP	1
KENNEL	1
LAGOON	1
LAKE	4
LAKEFRONT / WATERFRONT / RIVERBANK	31
LAKEFRONT/WATERFRONT/RIVERBANK	66
LAUNDRY ROOM	2
LIBRARY	585
LIQUOR STORE	13
LIVERY AUTO	1
LIVERY STAND OFFICE	2
LOADING DOCK	1
MEDICAL / DENTAL OFFICE	123
MEDICAL/DENTAL OFFICE	753
MOTEL	7
MOTOR VEH"	757
MOVIE HOUSE / THEATER	47
MOVIE HOUSE/THEATER	297
NEWSSTAND	32
NON-VEH"	89
NURSING / RETIREMENT HOME	311
NURSING HOME	6
NURSING HOME/RETIREMENT HOME	1538
OFFICE	19
OTHER	29213
OTHER (SPECIFY)	1843
OTHER COMMERCIAL TRANSPORTATION	359
OTHER RAILROAD PROP / TRAIN DEPOT	586
OTHER RAILROAD PROPERTY / TRAIN DEPOT	61
PARK PROPERTY	5745
PARKING LOT	257
PARKING LOT / GARAGE (NON RESIDENTIAL)	3340
PARKING LOT/GARAGE(NON.RESID.)	21876
PAWN SHOP	10
POLICE FACILITY	1
POLICE FACILITY / VEHICLE PARKING LOT	415
POLICE FACILITY/VEH PARKING LOT	869
POOL ROOM	40
POOLROOM	1
PORCH	398
PRAIRIE	2
PUBLIC GRAMMAR SCHOOL	2
PUBLIC HIGH SCHOOL	2
RAILROAD PROPERTY	15
RESIDENCE	136238
RESIDENCE - GARAGE	1116
RESIDENCE - PORCH / HALLWAY	1270
RESIDENCE - YARD (FRONT / BACK)	964
RESIDENCE PORCH/HALLWAY	12619
RESIDENCE-GARAGE	14266
RESIDENTIAL YARD (FRONT/BACK)	44
RESTAURANT	11996
RETAIL STORE	99
RIVER	4
RIVER BANK	5
ROOF	1
ROOMING HOUSE	1
SAVINGS AND LOAN	48
SCHOOL - PRIVATE BUILDING	123
SCHOOL - PRIVATE GROUNDS	148
SCHOOL - PUBLIC BUILDING	803
SCHOOL - PUBLIC GROUNDS	759
SCHOOL YARD	16
SEWER	2
SIDEWALK	47407
SMALL RETAIL STORE	13755
SPORTS ARENA / STADIUM	84
SPORTS ARENA/STADIUM	349
STAIRWELL	25
STREET	245437
TAVERN	37
TAVERN / LIQUOR STORE	238
TAVERN/LIQUOR STORE	3764
TAXI CAB	6
TAXICAB	701
TRAILER	4
TRUCK	9
TRUCKING TERMINAL	1
VACANT LOT	135
VACANT LOT / LAND	346
VACANT LOT/LAND	1892
VEHICLE - COMMERCIAL	107
VEHICLE - COMMERCIAL: ENTERTAINMENT / PARTY BUS	2
VEHICLE - COMMERCIAL: TROLLEY BUS	1
VEHICLE - DELIVERY TRUCK	20
VEHICLE NON-COMMERCIAL	7738
VEHICLE-COMMERCIAL	435
VESTIBULE	27
WAREHOUSE	1286
WOODED AREA	7
YARD	311
YMCA	3
soraslan@master-node:~$
```

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
```bash
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
```

---

## Member Contributions

| Name | Task | Contribution |
|------|------|-------------|
| Dana Ghassan | Task 2 | Wrote `mapper_task2.py`, ran job on cluster, documented results |
| Sema Raslan | Task 3 | Wrote `mapper_task3.py`, ran job on cluster, documented results |
| Yomna Kassem | Task 4 | Wrote `mapper_task4.py`, ran job on cluster, documented results |
| Sara Elhams | Task 5 | Wrote `mapper_task5.py`, ran job on cluster, documented results |
