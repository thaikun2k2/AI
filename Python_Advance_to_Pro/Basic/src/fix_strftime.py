from pathlib import Path
import re

path = Path(__file__).parent / "Basic" / "Practive_with_time_onPython.py"
text = path.read_text(encoding='utf-8')
# Remove the incorrect second argument (`nowtime`) passed to datetime.strftime
new_text = re.sub(r"strftime\(('.*?')\s*,\s*nowtime\)", r"strftime(\1)", text)

if new_text != text:
    path.write_text(new_text, encoding='utf-8')
    print('Updated file with corrected strftime calls.')
else:
    print('No changes made.')
