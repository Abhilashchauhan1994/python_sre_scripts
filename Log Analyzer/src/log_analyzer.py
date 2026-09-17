import re
from pathlib import Path
from collections import Counter


def validate_file(file_path)->bool:
    if not file_path.exists():
        print("Invalid File Path")
        return False
    if Path(file_path).suffix!=".log":
        print("This is not a log file.")
        return False
    return True

def parse_data(line:str)->dict|None:
    log_pattern=re.compile(r"^(?P<timestamp>\d{4}\-\d{2}\-\d{2}\s+\d{2}:\d{2}:\d{2})\s+"
                           r"(?P<log_level>INFO|ERROR|WARN|DEBUG)\s+"
                           r"(?P<message>.*)$")
    match_line=log_pattern.match(line)
    if not match_line:
        return None
    return match_line.groupdict()

def initialize_report_data() -> dict:
    return {
        "level_count": Counter(),
        "message_count": Counter(),
        "error_start": None,
        "error_end": None,
    }
def collect_report_data(report_data: dict,parsed_data: dict) -> None:

    log_level = parsed_data["log_level"]
    message = parsed_data["message"]
    timestamp = parsed_data["timestamp"]

    report_data["level_count"][log_level] += 1
    report_data["message_count"][message] += 1

    if log_level == "ERROR":

        if report_data["error_start"] is None:
            report_data["error_start"] = timestamp

        report_data["error_end"] = timestamp

def read_file(log_file:Path) ->dict:
    report_data = initialize_report_data()
    with log_file.open("r") as file:
        for line in file:
            parsed_data=parse_data(line)
            if parsed_data:
                collect_report_data(report_data,parsed_data)
    return report_data

def generate_report(report_data:dict,log_file:str):
    print("=" *30)
    print("Log Analyzer")
    print("=" *30) 
    print("\n")
    print(f"Log File: {log_file}\n\n")
    print("Log Level")
    print("="*10)
    print("\n")
    for level,count in report_data["level_count"].items():
        print(f"{level}: {count}")
    print("\nMost Common Errors")
    print("="*20)
    print("\n")
    for message,count in report_data["message_count"].items():
        print(f"{message}: {count}")
    print("\n Error Time Range\n")
    print(f"Start Time: {report_data["error_start"]}")
    print(f"End Time: {report_data["error_end"]}")
    print("="*30)

def log_analyzer():
    log_file=Path(input("Enter the log file path:"))

    if not validate_file(log_file):
        return 
    report_data = read_file(log_file)
    generate_report(report_data,log_file)


if __name__ == "__main__":
    log_analyzer()
    
