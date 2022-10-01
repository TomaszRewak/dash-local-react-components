from dash import Dash  # type: ignore
from typing import NamedTuple


AppKey = str
LibraryKey = NamedTuple('LibraryKey', [('dash', Dash), ('public_path', str)])
ComponentKey = NamedTuple('ComponentKey', [('dash', Dash), ('public_path', str), ('file_path', str), ('export_name', str)])
