import subprocess
from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_path = f"reports/report_{timestamp}.html"

subprocess.run(["pytest", "test_login.py", "-v", f"--html={report_path}"])
print(f"Report saved to: {report_path}")