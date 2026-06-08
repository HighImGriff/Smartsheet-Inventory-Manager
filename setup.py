from dotenv import load_dotenv
import smartsheet
import os
from mastercache import MasterCache
from logcache import LogCache
from importcache import ImportCache
from constants import *

def connect_api():
    load_dotenv()
    API_key = os.getenv("smartsheet")
    smart = smartsheet.Smartsheet(API_key)
    return smart

def get_sheet_caches(smart):
    load_dotenv()
    sheet_caches = {}
    sheet_ids = {"checkin": os.getenv("checkinlog"), "checkout": os.getenv("checkoutlog"), "audit": os.getenv("auditlog"), "master": os.getenv("master"), "import": os.getenv("import"),}

    for name, sheet_id in sheet_ids.items():
        if name in LOG_SHEET_TITLES:
            sheet_caches[name] = LogCache(smart, sheet_id)
        elif name == "master":
            sheet_caches[name] = MasterCache(smart, sheet_id)
        else:
            sheet_caches[name] = ImportCache(smart, sheet_id)
    return sheet_caches
