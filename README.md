# Personal Website - Tomislav Suhina

[![Pelican](https://img.shields.io/badge/Pelican-4.11.0+-blue.svg)](https://blog.getpelican.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-v4-38B2AC.svg)](https://tailwindcss.com/)

Modern, responsive personal website built with Pelican and Tailwind CSS.

**Live Site**: [https://tsuhina.github.io](https://tsuhina.github.io)

## 🚀 Technology Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Pelican** | 4.11.0+ | Static Site Generator |
| **Tailwind CSS** | v4 | CSS Framework |
| **Python** | 3.12+ | Backend Language |
| **UV** | Latest | Package Manager |
| **GitHub Pages** | - | Deployment Platform |

## 🛠️ Development Workflow

### 📋 Prerequisites

- **Python** 3.12+ with [UV](https://github.com/astral-sh/uv) installed
- **Node.js** and npm (for Tailwind CSS compilation)

### ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/tsuhina/tsuhina.github.io.git
cd personal_webpage

# Install Python dependencies
uv sync

# Install Node dependencies
npm install

# Build and serve locally
make html && make serve
```

### 🔧 Development Commands

| Command | Description |
|---------|-------------|
| `make html` | Build the site (includes Tailwind CSS compilation) |
| `make serve` | Serve locally at http://localhost:8000 |
| `make clean` | Clean generated files |
| `make github` | Build and deploy to GitHub Pages |

### 🎨 Tailwind CSS Development

```bash
# Watch mode for CSS development (auto-recompile on changes)
npm run dev

# Build optimized CSS for production
npm run build
```

## 🚀 Deployment

### 🌐 Automated Deployment via GitHub Actions

Deployment is fully automated! Simply push to main:

```bash
git push origin main
```

**What happens automatically:**
1. ✅ GitHub Actions workflow triggers
2. ✅ Compiles Tailwind CSS with minification
3. ✅ Builds the site with production settings
4. ✅ Deploys to `gh-pages` branch
5. ✅ Site goes live at https://ts-analytics.eu

**Monitor deployment:**
- View Actions: `https://github.com/tsuhina/tsuhina.github.io/actions`
- Typical deployment time: 1-2 minutes

## 📁 Project Structure

```
.
├── content/              # Markdown content
│   ├── articles/        # Blog posts
│   ├── pages/           # Static pages
│   ├── images/          # Images
│   └── css/             # Tailwind CSS
│       ├── input.css    # Tailwind source (committed)
│       └── output.css   # Compiled CSS (gitignored)
├── templates/           # Custom Jinja2 templates
│   ├── base.html       # Base template with navigation
│   ├── about.html      # Homepage with hero section
│   ├── services.html   # Services with card grid
│   ├── contact.html    # Contact page
│   └── page.html       # Default page template
├── output/              # Generated site (gitignored)
├── pelicanconf.py      # Development settings
├── publishconf.py      # Production settings
└── Makefile            # Build commands
```

## 🎨 Styling

The site uses **Tailwind CSS v4** with an editorial / minimal-premium design system:

| Feature | Description |
|---------|-------------|
| **Aesthetic** | Editorial premium — warm "paper" canvas, near-black ink, hairline rules, generous whitespace |
| **Colors** | Semantic tokens: `paper`, `ink`, `muted`, `line`, `accent` (terracotta), `surface` |
| **Typography** | Fraunces (display serif) · Inter (body) · IBM Plex Mono (labels & metrics) |
| **Approach** | Mobile-first, accessible (skip link, focus styles, `prefers-reduced-motion`) |
| **Components** | Reusable classes: `.eyebrow`, `.btn`, `.tag`, `.metric-value`, `.link-arrow` |
| **Performance** | Optimized CSS output (~25KB), no runtime JS beyond the mobile menu |

## 📝 Important Notes

> **Build Process**: The `make html` command automatically compiles Tailwind CSS before building the site.

### 🔄 CSS Compilation Flow

1. **Source**: `content/css/input.css` (Tailwind source)
2. **Process**: `npm run build` compiles with minification
3. **Output**: `content/css/output.css` (optimized CSS)
4. **Result**: Only `output.css` is included in the final site

### ⚙️ Build Automation

- The **Makefile** handles all build steps automatically
- No need to run Tailwind separately for production builds
- CSS compilation is integrated into the Pelican build process

## 📚 Documentation

For detailed development documentation, see [CLAUDE.md](CLAUDE.md).

---

**Built with ❤️ using Pelican and Tailwind CSS**
