import json
from pathlib import Path
from datetime import datetime,timezone
import requests
import logging
import config.logging_config
import socket

 
ROOT_FOLDER=Path(__file__).resolve().parent.parent
URLS_FILE=ROOT_FOLDER/"config"/"urls.json"
logger=logging.getLogger("url_monitor")

def get_url_response(urlname:str,url:str) -> dict:
    result = {
        "name": urlname,
        "url": url,
        "status": None,
        "health": "DOWN",
        "latency": None,
        "error": None
        }
    try:
        response=requests.get(url,timeout=10)
        if ((response.status_code >= 200) and (response.status_code < 400 )):
            result["health"]="UP"
        logger.info(f"Url Name: {urlname} | Url status: {response.status_code}|Health: {result['health']}| Latency: {response.elapsed.total_seconds():.3f} seconds")
        result["status"]=response.status_code
        result["latency"]=response.elapsed.total_seconds()
    except requests.exceptions.Timeout:
        logger.error(f"Url Name: {urlname} |Health: DOWN| Reason: Request Timeout")
        result["error"]="Request Timeout"
    except requests.exceptions.ConnectionError:
        logger.error(f"Url Name: {urlname} |Health: DOWN |ERROR:  Connection could not be established")
        result["error"]="Connection could not be established"
    except Exception as e:
        logger.exception(f"Unexpected error while checking {urlname}")
        result["error"]=str(e)
    return result
        
def get_url_data()->list:
    with URLS_FILE.open("r", encoding="utf-8") as file:
        result=[]
        urls_data = json.load(file)
        for i in urls_data["urls"]:
            response=get_url_response(i["name"],i["url"])
            result.append(response)
        return result

def get_health_summary(url_data:list)->dict:
    up_counter=0
    down_counter=0
    health_dict={}
    total_url=len(url_data)
    for items in url_data:
        if items["health"]=="UP":
            up_counter+=1
        else:
            down_counter+=1
    health_dict["UP"]=up_counter
    health_dict["DOWN"]=down_counter
    health_dict["Total URL"]=total_url
    return health_dict

def wrap():
    url_data=get_url_data()
    health_data=get_health_summary(url_data)
    print("=" *40)
    print(f"URL Health Monitoring Summary")
    print("=" *40)
    print(f"\n Total URLs Monitored: {health_data["Total URL"]}")
    print(f"UP URLs : {health_data["UP"]}")
    print(f"DOWN URLs : {health_data["DOWN"]}")
    print("===========END================")


wrap()

