from pathlib import Path
import yaml

def get_node_info(current_directory):
    with (current_directory / 'info.yaml').open() as f:
        return yaml.safe_load(f)
