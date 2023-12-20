from pydantic import BaseModel
from typing import List


class Entry(BaseModel):
    id: int
    amount: float
    name: str
    comment: str


class Income(Entry):
    isMonthly: bool


class Expense(Entry):
    isMonthly: bool


class FinancialAccount(BaseModel):
    balance: float
    expenses: List[Expense] = []
    incomes: List[Income] = []
