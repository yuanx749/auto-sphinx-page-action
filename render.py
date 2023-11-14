import json
import sys
import urllib.request
from pathlib import Path

conf_template = """
project = '{project}'
author = '{author}'
copyright = '{year}, {author}'

extensions = [
    'myst_parser',
    'sphinx_copybutton',
]
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
templates_path = ['_templates']

html_theme = 'pydata_sphinx_theme'
html_theme_options = {{
    'navigation_with_keys': False,
    'show_toc_level': 2,
    'external_links': [
        {{
            'name': 'View on GitHub',
            'url': 'https://github.com/{repo}',
        }},
    ]
}}
html_title = project
html_show_sourcelink = False
"""

# read sys.argv
config = {}
for arg in sys.argv[1:]:
    if arg.startswith("-"):
        k, v = arg.lstrip("-").split("=")
        config[k] = v

# get created year of repo
if "year" not in config:
    url = f"https://api.github.com/repos/{config['repo']}"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read().decode("utf-8"))
    config["year"] = data["created_at"][:4]

# create conf.py
if not (conf := Path("conf.py")).is_file():
    conf.write_text(conf_template.format(**config))

# change README to index
exts = ["md", "rst"]
if not any(Path(f"index.{ext}").is_file() for ext in exts):
    for ext in exts:
        if (p := Path(f"README.{ext}")).is_file():
            p.rename(f"index.{ext}")
            break
