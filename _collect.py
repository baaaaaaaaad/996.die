from pathlib import Path

root = Path("events")
lines = ["# Event Timeline\n"]

for year in sorted(root.iterdir(), reverse=True):
    lines.append(f"\n## {year.name}")
    for f in sorted(year.glob("*.md"), reverse=True):
        title = f.stem
        lines.append(f"- [{title}]({f.as_posix()})")

Path("timeline.md").write_text("\n".join(lines), encoding="utf-8")
