Requirement

Build a Python CLI tool that analyzes a Linux application log file and produces a summary of the log activity. The program should read a log file, identify different log levels such as INFO, WARNING, and ERROR, count how many entries exist for each level, identify the most common error messages, and provide a small summary of the time range covered by the log. It should handle missing or unreadable files gracefully and should be structured into small functions where each function has one clear responsibility. The analyzer should work with a realistic log format rather than relying on hardcoded line numbers or fixed positions in the file.

Example Input

Create a sample file such as:

2026-09-16 10:00:01 INFO Application started
2026-09-16 10:01:12 INFO User request received
2026-09-16 10:02:45 WARNING Connection pool usage is high
2026-09-16 10:03:10 ERROR Database connection failed
2026-09-16 10:03:15 ERROR Database connection failed
2026-09-16 10:04:20 INFO Retry initiated
2026-09-16 10:04:25 ERROR Timeout while connecting to database
2026-09-16 10:05:10 WARNING Memory usage is high

# Expected Output

# LOG ANALYZER

Log File : application.log
Total Entries : 8

## Log Levels

INFO : 3
WARNING : 2
ERROR : 3

## Most Common Errors

Database connection failed : 2
Timeout while connecting to database : 1

## Time Range

Start : 2026-09-16 10:00:01
End : 2026-09-16 10:05:10

========================================
