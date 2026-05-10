# Playwright Python Automation

Automation testing project using Playwright + Pytest.

## 🚀 Tech Stack

- Python
- Playwright
- Pytest

---

### Clone repository

```bash
git clone <your-repo-url>
cd <project-folder>

### Init
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

playwright install

### Run Test:
- pytest --html=report.html tests/test_login.py → for generate html report
- PWDEBUG=1 pytest -s -v tests/test_login.py → for debuging
- pytest --tracing=on tests/test_login.py → for tracing
- pytest -s tests/test_login.py → for run test