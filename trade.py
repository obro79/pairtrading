"""Trade class that stores trade information."""
from dataclasses import dataclass
from datetime import datetime

import CONSTANTS


@dataclass
class Trade:
    date: datetime
    asset: str
    price: float
    quantity: float
    commission: float = CONSTANTS.COMMISSION

    def make_trade(self, action, ):
        pass
