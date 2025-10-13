from datetime import datetime
from pathlib import Path
from models import StudySession
from storage import append_session

def start_session(db: Path, topic: str) -> StudySession:
    session = StudySession(topic=topic, start=datetime.now(), end=None)
    append_session(db, session)
    return session

def end_session(db: Path, topic: str) -> StudySession:
    # 종료는 "가장 최근 시작했지만 end가 빈 것"을 마감한다고 가정하지 않고,
    # 간단히 새 행으로 종료 시점을 기록 (빠르게 연습용)
    session = StudySession(topic=topic, start=datetime.now(), end=datetime.now())
    append_session(db, session)
    return session