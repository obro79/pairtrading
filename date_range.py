from datetime import datetime, timedelta
from typing import Union

DateLike = Union[str, datetime]


class DateRange:
    """
    Represents an inclusive date range between start_date and end_date.

    Supports initialization from ISO strings or datetime objects.
    Provides common utilities: duration, containment, overlap.
    """

    def __init__(self, start: DateLike, end: DateLike):
        self.start_date = self._to_datetime(start)
        self.end_date = self._to_datetime(end)
        if self.start_date > self.end_date:
            raise ValueError(f"start_date ({self.start_date}) must be <= end_date ({self.end_date})")

    @staticmethod
    def _to_datetime(d: DateLike) -> datetime:
        if isinstance(d, datetime):
            return d
        # Expect ISO format 'YYYY-MM-DD'
        return datetime.fromisoformat(d)

    def contains(self, date: DateLike) -> bool:
        """Check if a date falls within the range (inclusive)."""
        dt = self._to_datetime(date)
        return self.start_date <= dt <= self.end_date

    @property
    def duration(self) -> timedelta:
        """Total length of the range."""
        return self.end_date - self.start_date

    def overlaps(self, other: 'DateRange') -> bool:
        """Returns True if this range overlaps with another."""
        return not (self.end_date < other.start_date or other.end_date < self.start_date)

    def __iter__(self):
        """Iterate day by day (datetime) through the range."""
        current = self.start_date
        while current <= self.end_date:
            yield current
            current += timedelta(days=1)

    def __repr__(self):
        return f"DateRange({self.start_date.date()} to {self.end_date.date()})"

    def as_tuple(self) -> tuple[datetime, datetime]:
        """Return (start_date, end_date)."""
        return (self.start_date, self.end_date)
