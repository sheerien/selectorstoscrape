from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional
from src.etl import read_data_from_json_file
import json
import os


@dataclass
class Selectors:
    ol_tag: str
    li_tag: str
    article: str
    image_container: str


json_file_path = os.path.join(os.path.dirname(__file__), "selectors.json")

data = read_data_from_json_file(json_file_path)

selectors:Selectors = Selectors(**data["selectors"])