# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal website/blog for Tomislav Suhina built with **Pelican**, a Python-based static site generator. The site showcases professional experience, services, projects, and blog posts. The generated static site is deployed to GitHub Pages at `https://tsuhina.github.io`.

## Technology Stack

- **Static Site Generator**: Pelican 4.11.0+
- **Content Format**: Markdown
- **Python Version**: 3.12+
- **Deployment**: GitHub Pages (gh-pages branch)
- **Task Runner**: Invoke (tasks.py) and Make (Makefile)

## Key Commands

### Development Workflow

```bash
# Build the site locally (output to ./output)
make html
# OR
invoke build

# Serve locally with live reload (recommended for development)
invoke livereload
# This opens browser at localhost:8000 and auto-rebuilds on file changes

# Serve without live reload
make serve
# OR
invoke serve

# Clean generated files
make clean
# OR
invoke clean

# Rebuild from scratch (clean + build)
invoke rebuild
```

### Publishing

```bash
# Build production version (uses publishconf.py settings)
make publish
# OR
invoke preview

# Deploy to GitHub Pages
make github
# OR
invoke gh-pages
```

The `make github` command:
1. Builds with production settings (publishconf.py)
2. Uses ghp-import to commit output to gh-pages branch
3. Pushes to GitHub

## Architecture

### Content Organization

```
content/
├── articles/          # Blog posts organized by year
│   └── 2025/
├── pages/            # Static pages (About, Services, Experience, Projects, Contact)
├── images/           # Images referenced in content
└── extra/            # Additional static files
```

**Key Configuration (pelicanconf.py)**:
- Articles are saved to: `blog/{year}/{slug}.html`
- Pages are saved to: `{slug}.html` (root level)
- Static paths: images and extra files are copied to output
- Menu items are manually defined in MENUITEMS (not auto-generated from pages)

### Theme & Templates

- Uses default Pelican theme with custom template overrides
- Template overrides in `templates/` directory (currently just `base.html`)
- `THEME_TEMPLATES_OVERRIDES = ['templates']` allows selective template customization
- The base template has been customized to remove default Pelican attribution footer

### Configuration Files

- **pelicanconf.py**: Development settings (RELATIVE_URLS=True for local testing)
- **publishconf.py**: Production settings (inherits from pelicanconf.py, sets SITEURL to `https://tsuhina.github.io`, RELATIVE_URLS=False, enables feeds)

### Task Management

Two task systems are available (functionally equivalent):

1. **Invoke tasks** (tasks.py): Python-based, provides livereload functionality
2. **Makefile**: Traditional make commands

The invoke tasks include additional features:
- `livereload`: Auto-rebuild with browser refresh (watches content, templates, theme files)
- `OPEN_BROWSER_ON_SERVE = True`: Automatically opens browser when serving

## Content Guidelines

### Creating Blog Posts

Blog posts go in `content/articles/{year}/` with frontmatter:

```markdown
Title: Post Title
Date: 2025-01-15
Category: Machine Learning
Tags: python, ml
Slug: post-slug

Content here...
```

### Creating Pages

Pages go in `content/pages/` with minimal frontmatter:

```markdown
Title: Page Title
Slug: page-slug

Content here...
```

**Important**: New pages need to be manually added to MENUITEMS in pelicanconf.py to appear in navigation.

### Images

Reference images in content using:
- `{static}/images/path/to/image.jpg` for images in content/images/
- Images are automatically copied to output/images/

## Development Notes

- The site uses relative URLs in development and absolute URLs in production
- Feeds (Atom/RSS) are disabled in development, enabled in production
- The output/ directory is gitignored (generated content)
- Python virtual environment is in .venv/
- Dependencies managed via pyproject.toml (UV package manager based on uv.lock presence)
