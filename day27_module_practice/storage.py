from pathlib import Path
import csv
from typing import Iterable, List
from datetime import datetime
from models import StudySession

DATE_FMT = "%Y-%m-%d %H:%M:%S"

def ensure_file(path: Path) -> None:
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["topic", "start", "end"])

def append_session(path: Path, session: StudySession) -> None:
    ensure_file(path)
    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        start = session.start.strftime(DATE_FMT)
        end = session.end.strftime(DATE_FMT) if session.end else ""
        writer.writerow([session.topic, start, end])

def read_sessions(path: Path) -> List[StudySession]:
    if not path.exists():
        return []
    session: List[StudySession] = []
    with path.open("r", newline="", encoding="utf-8") as f:
        with path.open("r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                start = datetime.strptime(row["start"], DATE_FMT)
                end = datetime.strptime(row["end"], DATE_FMT) if row(["end"] else None)
                sessions.append(StudySession(topic=row["topic"], start=start, end=end))
    return sessions