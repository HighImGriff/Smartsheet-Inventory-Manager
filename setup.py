from dotenv import load_dotenv
import smartsheet
import os
from sheetcache import SheetCache

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
        sheet = smart.Sheets.get_sheet(sheet_id)
        sheet_caches[name] = SheetCache(sheet)
    return sheet_caches
