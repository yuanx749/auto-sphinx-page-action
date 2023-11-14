# auto-sphinx-page-action

GitHub action that creates website using Sphinx.

This action creates a website from your repository, by building with Sphinx.

## Features

- Set up the configuration of Sphinx automatically.
- Use `README` as the homepage if `index` does not exist at the root level.
- Use [PyData](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) theme.
- Support MyST Markdown. For more information, see [MyST-Parser](http://myst-parser.readthedocs.io/).
- Publish to GitHub Pages.
- Can customize with `conf.py`.

## Usage

Refer to the GitHub [docs](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow) to enable publishing to GitHub Pages.

Set up a workflow in Actions. An example `.yml` file is as below.

```YAML
on:
  workflow_dispatch:
  push:
    branches:
      - main
      - master

jobs:
  build-deploy:
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - id: deployment
        uses: yuanx749/auto-sphinx-page-action@main
        with:
          project: "project"  # project's name, optional, default repository name
          author: "author"  # author name, optional, default username
```

Or use a reusable workflow:

```YAML
on:
  workflow_dispatch:
  push:

jobs:
  build-deploy:
    permissions:
      pages: write
      id-token: write
    uses: yuanx749/auto-sphinx-page-action/.github/workflows/main.yml@main
```

For repository with customized docs folder:

```YAML
on:
  workflow_dispatch:
  push:
    branches:
      - main

jobs:
  build-deploy:
    permissions:
      pages: write
      id-token: write
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - id: deployment
        uses: yuanx749/auto-sphinx-page-action@main
        with:
          sourcedir: "docs"  # source directory, optional, default .
          requirements: "docs/requirements.txt"  # path to the requirements file, optional
```
