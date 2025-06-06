from datetime import datetime
from pydantic import BaseModel
from application.schemas.Book import MiniBookResponse
from application.schemas.User import MiniUserResponse


class LoanAction(BaseModel):
    user_id:  int
    book_id:  int
    due_date: datetime

class LoanResponse(BaseModel):
    id: int
    user_id: int
    book_id:  int
    issue_date: datetime
    due_date: datetime
    status: str

class ReturnAction(BaseModel):
    loan_id: int

class ReturnResponse(BaseModel):
    id: int
    user_id: int
    book_id:  int
    issue_date: datetime
    due_date: datetime
    return_date: datetime
    status: str

class LoanOfUserResponse(BaseModel):
    id: int
    book: MiniBookResponse
    issue_date: datetime
    due_date: datetime
    return_date: datetime | None
    status: str

class OverdueResponse(BaseModel):
    id: int
    user: MiniUserResponse
    book: MiniBookResponse
    issue_date: datetime
    due_date: datetime
    days_overdue: int

class ExtendLoanAction(BaseModel):
    extension_days: int

class UpdateLoanAction(BaseModel):
    extension_days: int
    extensions_count: int
    extended_due_date: datetime

class ExtendedLoanResponse(BaseModel):
    id: int
    user_id: int
    book_id: int
    issue_date: datetime
    original_due_date: datetime
    extended_due_date: datetime | None
    status: str
    extensions_count: int

class LoanIdAction(BaseModel):
    loan_id: int

class ReturnUpdateAction(BaseModel):
    status: str
    return_date: datetime | None