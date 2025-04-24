# demo_scan.py
from pathlib import Path
from security_chainsaw.scanner import CodeScanner

if __name__ == "__main__":
    repo_path = Path("tests")  # o la carpeta que quieras escanear
    scanner = CodeScanner(repo_path)
    findings = scanner.run_scan()
    if not findings:
        print("No issues found")
    else:
        for f in findings:
            print(f"Archivo: {f['file']}, Línea: {f['line']}, Issue: {f['issue']}")
