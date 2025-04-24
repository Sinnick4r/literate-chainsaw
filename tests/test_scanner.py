import pytest
from pathlib import Path
from security_chainsaw.scanner import CodeScanner

@pytest.fixture
def temp_py_file(tmp_path):
    file = tmp_path / "vuln.py"
    file.write_text(
        'def foo():\n'
        '    password = "secret"  # Hardcoded password\n'
    )
    return file


def test_regex_scan_finds_password(temp_py_file):
    scanner = CodeScanner(temp_py_file.parent)
    findings = scanner._regex_scan()
    assert any(f['issue'] == 'Hardcoded password' for f in findings)
    assert any(f['file'].endswith('vuln.py') for f in findings)


def test_run_scan_returns_list(monkeypatch, temp_py_file):
    monkeypatch.setattr('security_chainsaw.scanner._BANDIT_AVAILABLE', False)
    scanner = CodeScanner(temp_py_file.parent)
    result = scanner.run_scan()
    assert isinstance(result, list)