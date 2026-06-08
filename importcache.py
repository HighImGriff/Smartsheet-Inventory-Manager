from sheetcache import SheetCache
from constants import *

class ImportCache(SheetCache):
    def __init__(self, smart, sheet_id):
        super().__init__(smart, sheet_id)
        self.common_transactions = {"Check-In": {}, "Check-Out": {}, "Audit": {}}

        self.build_cache()

    def build_cache(self):
        sheet = self.get_sheet()
        for column in sheet.columns:
            self.columns_by_title[column.title] = column
        for row in sheet.rows:
            self.rows_by_id[row.id] = row
            transaction_type = self.get_cell_value(row.id, TRANSACTION_COLUMN_TITLE)
            location = self.get_cell_value(row.id, LOCATION_COLUMN_TITLE)
            date = self.get_cell_value(row.id, DATE_COLUMN_TITLE)
            if transaction_type is not None:
                self.common_transactions[transaction_type].setdefault(location, {}).setdefault(date, []).append(row.id)