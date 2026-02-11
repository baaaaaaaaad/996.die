import re
from pathlib import Path

root = Path("events")
lines = ["# Event Timeline\n"]
lines.append('\n- Thus things flow away day and night.\n- Subfile Naming Convention: `/events/YYYY-MM-DD-title.md`')

# 正则表达式匹配日期格式 YYYY-MM-DD
DATE_PATTERN = re.compile(r'^(\d{4})-(\d{2})-(\d{2})-(.+)$')

events = []

# 收集所有事件文件并解析信息
for f in root.glob("*.md"):
    match = DATE_PATTERN.match(f.stem)
    if match:
        year, month, day, slug = match.groups()
        # 将slug转换为更友好的标题格式
        title = slug.replace('-', ' ').title()
        events.append({
            'file': f,
            'year': year,
            'month': month,
            'day': day,
            'title': title
        })

# 按年份倒序排序，同一年份内按月份和日期倒序排序
events.sort(key=lambda x: (x['year'], x['month'], x['day']), reverse=True)

# 按年份组织事件并生成时间线
current_year = None
for event in events:
    if event['year'] != current_year:
        current_year = event['year']
        lines.append(f"\n## {current_year}\n")
    # 格式化日期为更友好的格式
    date_str = f"{event['month']}/{event['day']}"
    lines.append(f"- **{date_str}**: [{event['title']}]({event['file'].as_posix()})")

Path("README.md").write_text("\n".join(lines), encoding="utf-8")
