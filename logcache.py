from sheetcache import SheetCache
from constants import *

class LogCache(SheetCache):
    def __init__(self, smart, sheet_id):
        super().__init__(smart, sheet_id)
        self.dates_by_location = {}
        self.transactions_by_location_date = {}

        self.build_cache()
        
    def build_cache(self):
        self.sheet = self.get_sheet()
        sheet = self.sheet
        for column in sheet.columns:
            self.columns_by_title[column.title] = column
        for row in sheet.rows:
            self.rows_by_id[row.id] = row
            location = self.get_cell_value(row.id, LOCATION_COLUMN_TITLE)
            if location is not None:
                self.dates_by_location.setdefault(location, {})
            date = self.get_cell_value(row.id, DATE_COLUMN_TITLE)
            if date is not None:
                if row.parent_id:
                    location = self.get_cell_value(row.parent_id, LOCATION_COLUMN_TITLE)
                if location is None:
                    raise ValueError(f"Row {row.row_number} in {self.sheet.name} has a date but no location")
                self.dates_by_location.setdefault(location, {})[date] = row.id
                self.transactions_by_location_date.setdefault((location, date), {})
            if row.parent_id is not None:
                date = self.get_cell_value(row.parent_id, DATE_COLUMN_TITLE)
                if date is not None:
                    location = self.get_cell_value(self.rows_by_id[row.parent_id].parent_id, LOCATION_COLUMN_TITLE)
                    if location is None:
                        raise ValueError(f"Row {row.row_number} in {self.sheet.name} has a parent row with a date but no location")
                    self.transactions_by_location_date.setdefault((location, date), {})[row.id] = row