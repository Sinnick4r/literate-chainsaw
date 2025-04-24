"""
PatchGenerator: generates unified-diff patches for findings.
"""
from typing import List, Dict, Any
import difflib
from pathlib import Path


class PatchGenerator:
    def __init__(self, findings: List[Dict[str, Any]]) -> None:
        self.findings = findings

    def generate_patches(self) -> List[Dict[str, Any]]:
        patches: List[Dict[str, Any]] = []
        issues_by_file = {}
        for f in self.findings:
            issues_by_file.setdefault(f['file'], []).append(f['line'])

        for file, lines in issues_by_file.items():
            original = Path(file).read_text(encoding='utf-8').splitlines(keepends=True)
            modified = self._apply_fixes(original, sorted(lines))
            diff = ''.join(
                difflib.unified_diff(
                    original,
                    modified,
                    fromfile=file,
                    tofile=file,
                    lineterm=''
                )
            )
            patches.append({'file': file, 'diff': diff})
        return patches

    def _apply_fixes(self, original: List[str], lines: List[int]) -> List[str]:
        modified = original.copy()
        for line_no in lines:
            idx = line_no - 1
            line = modified[idx]
            if 'password' in line:
                modified[idx] = '    import os  # patched: fetch password securely\n'
                modified.insert(idx+1, '    password = os.getenv("PASSWORD")  # patched fetch\n')
        return modified
    