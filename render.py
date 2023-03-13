import json
import os
import sys
import urllib.request

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
    'external_links': [
        {{
            'name': 'View on GitHub',
            'url': 'https://github.com/{repo}',
        }},
    ]
}}
html_title = project
html_static_path = ['_static']
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
if not os.path.exists(conf := "conf.py"):
    with open(conf, "w") as f:
        f.write(conf_template.format(**config))

# change README to index
exts = ["md", "rst"]
if not any(os.path.isfile(f"index.{ext}") for ext in exts):
    for ext in exts:
        if os.path.isfile(f"README.{ext}"):
            os.rename(f"README.{ext}", f"index.{ext}")
            break
