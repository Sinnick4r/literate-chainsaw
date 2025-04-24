# Security Chainsaw | Auditoría de seguridad

**Security Chainsaw** is a modular Python CLI tool for scanning codebases for common security issues and suggesting minimal patches.  
**Security Chainsaw** es una herramienta en Python para escanear código, encontrar errores de seguridad y tirar parches piolas.

---

## Quickstart / Inicio rápido

### Install / Instalar
```bash
pip install security-chainsaw
```
*Then run your first scan* / *Después corrés tu primer análisis*

### Run Scan / Ejecutar análisis
```bash
security-chainsaw ./my_project --report report.json
```  
```bash
security-chainsaw ./mi_proyecto --report resultados.json
```

---

## Features / Características

- **Static Analysis**: Integrates with Bandit for deep AST-based checks.  
  **Análisis estático**: se integra con Bandit si lo tenés instalado
- **Fallback Patterns**: Regex rules for hardcoded secrets, `eval()`, `subprocess ... shell=True`.  
  **Chequeos extra**: regex para secretos en claro, `eval()` y `subprocess con shell=True`
- **Unified-Diff Patches**: Generates diff-friendly patches with `difflib`.  
  **Parches unified-diff**: genera parches copados en formato diff con difflib

---

## Usage / Uso
```bash
security-chainsaw <path> [options]
```
```text
Usage: security-chainsaw [path] [options]

Arguments:
  path                  Directory or file to scan / ruta o archivo para escanear

Options:
  -r, --report <file>   Report output path (default: findings.json) / ruta de resultados (por defecto findings.json)
  -l, --log-level <lvl> Set logging level (DEBUG, INFO, WARNING, ERROR) / nivel de log (DEBUG, INFO, WARNING, ERROR)
  -h, --help            Show this message and exit / mostrar ayuda y salir
```

---

## Project Structure / Estructura del proyecto

```
security-chainsaw/
├── LICENSE
├── .gitignore
├── README.md
├── pyproject.toml
├── src/security_chainsaw/
│   ├── __init__.py
│   ├── __main__.py
│   ├── scanner.py
│   └── patcher.py
└── tests/
    ├── test_scanner.py
    └── test_patcher.py
```

---

## Development / Para arrancar

```bash
# Clone the repo / Clona el repo
git clone https://github.com/Sinnick4r/security-chainsaw.git
cd security-chainsaw

# Setup & install / Preparar e instalar
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt

# Run tests / Corré las pruebas
pytest
```

---

## Contributing / Contribuir

Contributions are welcome! Please open an issue or submit a pull request.  
Contribuciones bienvenidas, abrí un issue o mandá un pull request

---

## License / Licencia

This project is licensed under the MIT License.  
Este proyecto está bajo licencia MIT
