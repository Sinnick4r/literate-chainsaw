"""
CodeScanner: scans a path for security issues using Bandit or regex rules.
"""
import logging
import re
from pathlib import Path
from typing import List, Dict, Any

try:
    from bandit.core.manager import BanditManager
    from bandit.core.config import Config as BanditConfig
    _BANDIT_AVAILABLE = True
except ImportError:
    _BANDIT_AVAILABLE = False


class CodeScanner:
    def __init__(self, code_path: Path) -> None:
        self.code_path = code_path

    def run_scan(self) -> List[Dict[str, Any]]:
        """Run Bandit if available, else use regex fallback."""
        if _BANDIT_AVAILABLE:
            try:
                return self._run_bandit()
            except Exception as e:
                logging.warning(f"Bandit failed: {e}. Falling back to regex scan.")
        return self._regex_scan()

    def _run_bandit(self) -> List[Dict[str, Any]]:
        config = BanditConfig()
        manager = BanditManager(config=config, plugin_conf='file')
        manager.discover_files(start_dir=str(self.code_path))
        manager.run_tests()
        results = []
        for issue in manager.get_issue_list():
            results.append({
                'file': issue.fname,
                'line': issue.line_number,
                'issue': issue.text.strip(),
                'severity': issue.severity.name,
                'confidence': issue.confidence.name,
                'test_id': issue.test_id
            })
        return results

    def _regex_scan(self) -> List[Dict[str, Any]]:
        patterns = {
            'Hardcoded password': re.compile(r"password\s*=\s*['\"].+['\"]"),
            'Use of eval': re.compile(r"\beval\("),
            'Subprocess shell=True': re.compile(r"subprocess\..+shell\s*=\s*True")
        }
        findings: List[Dict[str, Any]] = []
        for filepath in self.code_path.rglob('*.py'):
            for idx, line in enumerate(filepath.open(), start=1):
                for desc, pattern in patterns.items():
                    if pattern.search(line):
                        findings.append({
                            'file': str(filepath),
                            'line': idx,
                            'issue': desc
                        })
        return findings