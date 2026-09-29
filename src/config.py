import yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_config():
    with open(ROOT / "config" / "assumptions.yaml") as f:
        return yaml.safe_load(f)