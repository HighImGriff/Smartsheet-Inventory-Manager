from constants import *
from helpers import *

class SheetCache():

    def __init__(self, smart, sheet_id):
        self.sheet = None
        self.sheet_id = sheet_id
        self.smart = smart

        self.columns_by_title = {}
        self.rows_by_id = {}

    def get_sheet(self):
        if self.sheet is None:
            self.sheet = self.smart.Sheets.get_sheet(self.sheet_id)
        return self.sheet
    
    def get_cell_value(self, row_id, column_title):
        column_id = self.columns_by_title[column_title].id
        row = self.rows_by_id[row_id]
        for cell in row.cells:
            if cell.column_id == column_id:
                return cell.value
        return None
    
    def get_parent_row_id(self, row_id):
        row = self.rows_by_id[row_id]
        if row.parent_id:
            return row.parent_id
        raise ValueError(f"Row {row_id} does not have a parent row.")