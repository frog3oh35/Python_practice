from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class StudySession:
    topic: str
    start: datetime
    end: Optional[datetime] = None # 진행 중이면 None

    def duration_minutes(self) -> Optional[int]:
        if self.end is None:
            return None
        delta = self.end - self.start
        return int(delta.total_seconds() // 60)