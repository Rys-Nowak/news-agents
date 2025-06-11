import json
import yaml
from pathlib import Path
from typing import Dict, Any, List
import os

class FileReader:
    def load_json(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)