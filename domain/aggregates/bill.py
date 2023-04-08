from datetime import datetime
from domain.aggregates.base_old import Entity


class Bill(Entity):
    _student_id: int
    _type: str
    _amount: float
    _partial_amount: float
    _is_paid: bool
    _due_date: datetime

    def __init__(
        self,
        id: int,
        student_id: int,
        type_: str,
        amount: float,
        partial_amount: float,
        is_paid: bool,
        due_date: datetime,
    ):
        super().__init__(id)
        self._student_id = student_id
        self._type = type_
        self._amount = amount
        self._partial_amount = partial_amount
        self._is_paid = is_paid
        self._due_date = due_date


class Payment(Entity):
    _bill_id: int
    _amount: float
    _date: datetime

    def __init__(self, id: int, bill_id: int, amount: float, date: datetime):
        super().__init__(id)
        self._bill_id = bill_id
        self._amount = amount
        self._date = date
