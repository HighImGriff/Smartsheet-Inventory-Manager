from sheetcache import SheetCache
from constants import *

class MasterCache(SheetCache):
    def __init__(self, smart, sheet_id):
        super().__init__(smart, sheet_id)
        self.location_rows_by_id = {}
        self.item_rows_by_location = {}

        self.build_cache()
        
    def build_cache(self):
        sheet = self.get_sheet()
        for column in sheet.columns:
            self.columns_by_title[column.title] = column
        for row in sheet.rows:
            self.rows_by_id[row.id] = row
            location = self.get_cell_value(row.id, LOCATION_COLUMN_TITLE)
            self.location_rows_by_id[row.id] = location
            