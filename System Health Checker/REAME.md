# System Health Checker

A lightweight Python command-line utility that collects basic system health metrics and reports whether the system is healthy based on predefined utilization thresholds.

## Problem Statement

System administrators and SREs frequently need to perform quick checks of a server's basic health before troubleshooting an incident, deploying an application, or investigating performance issues. Manually checking CPU, memory, disk usage, and hostname requires executing multiple operating-system commands or tools. This project provides a simple Python utility that collects these metrics programmatically and presents them in a single health report.

## Solution

The application collects the following system information:

- Hostname
- CPU utilization
- Memory utilization
- Disk utilization
  Each metric is collected through a dedicated function. The collected values are then passed to a health evaluation function that determines whether the system is `Healthy` or `Unhealthy`.
  The final results are presented through a simple command-line report.
  The implementation uses Python-native APIs where suitable: - `socket` for hostname information - `psutil` for CPU, memory, and disk metrics `subprocess` was also explored during development to understand Linux command execution, command pipelines, and output parsing.

For more information about the implementation decisions, trade-offs, and approaches considered,
see: **[DESIGN.txt](DESIGN.txt)**
