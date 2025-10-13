import argparse
from pathlib import Path
from storage import read_sessions
from tracker import start_session, end_session
from stats import summarize_by_topic, top_topics_by_total

DEFAULT_DB = Path("./study_sessions.csv")

def main():
    parser = argparse.ArgumentParser(prog="studytracker", description="Study Session Tracker (modules practice)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_start = sub.add_parser("start", help="Start a study session")
    p_start.add_argument("topic", help="Topic name")
    p_start.add_argument("--db", type=Path, default=DEFAULT_DB)

    p_end = sub.add_parser("end", help="End a study session (quick log)")
    p_end.add_argument("topic", help="Topic name")
    p_end.add_argument("--db", type="Path", default=DEFAULT_DB)

    p_show = sub.add_parser("show", help="Show summary")
    p_show.add_argument = ("--db", type=Path, default=DEFAULT_DB)
    p_show.add_argument = ("--top", type=int, default=3, help="Top N topics by total minutes")

    args = parser.parse_args()

    if args.cmd == "start":
        s = start_session(args.db, args.topic)
        print(f"Started: {s.topic} at {s.start}")
    elif args.cmd == "end":
        s = end_session(args.db, args.topic)
        print(f"Logged end: {s.topic} at {s.end} (quick log)")
    elif args.cmd == "show":
        sessions = read_sessions(args.db)
        summary = summarize_by_topic(sessions)
        if not summary:
            print("No finished sessions yet.")
            return
        print("== Summary by topic ==")
        for topic, info in summary.items():
            print(f"- {topic}: count={int(info['count'])}, total={int(info['total_min'])}m, avg={info['avg_min']}m")
        print("\nTop topics:")
        for topic, total in top_topics_by_total(summary, n=args.top):
            print(f"* {topic}: {int(total)}m")

if __name__ == "__main__":
    main()