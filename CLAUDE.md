# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based documentation migration and generation toolset for the **brainCloud backend-as-a-service API documentation**. It migrates content from Slate (ERB/HTML) and WordPress formats to Docusaurus-compatible Markdown (MDX), and also generates TypeScript definition files (.d.ts) for the brainCloud PortalX Monaco editor's intellisense.

## Running Scripts

All utilities are standalone Python scripts — there is no build system or test suite. Activate the venv first:

```bash
source venv/bin/activate
```

Then run scripts directly:

```bash
python main.py                      # Interactive proxy JSON → Markdown converter
python generate-md-from-json.py     # JSON API definition → tabbed MDX with code examples
python migrate-erb-md.py            # Slate ERB templates → Markdown
python read-files-folder.py         # Generate TypeScript proxy .d.ts files
python js_to_dart_converter.py      # Auto-generate Dart examples from JavaScript
python wordpress-page-refactor.py   # Fix image/API links in WordPress HTML exports
python scan_swap_block.py           # Reorganize code blocks within Markdown files
python update-docUrl.py             # Validate/correct doc URLs in JSON files
```

Most scripts are interactive (prompting for service/proxy names) or require editing hardcoded configuration variables near the top of the file before running.

## Architecture

### Migration Pipeline

The pipeline has four stages:

1. **Source Parsing** — Reads JSON API definitions from local brainCloud portal checkout (hardcoded path: `/bitbucket/braincloud-portal/...`), Slate ERB templates, or WordPress HTML exports.

2. **Transformation** — The main conversion scripts:
   - `migrate-erb-md.py`: ERB → Markdown. Converts `<aside>` tags to Docusaurus admonitions (`:::tip`, `:::warning`), extracts service/operation metadata from `<%= partial %>` calls, rewrites image links and internal anchors.
   - `generate-md-from-json.py`: JSON schema → MDX. Creates API reference pages with multi-language tabbed code examples (C#, C++, Objective-C, Java, JavaScript, Dart, Cloud Code/CFScript, Raw JSON). Uses Docusaurus `<Tabs>` / `<TabItem>` MDX components.
   - `read-files-folder.py`: Reads JSON proxy definitions and emits TypeScript `interface` declarations with JSDoc for IDE intellisense.

3. **Post-Processing** — `wordpress-page-refactor*.py` normalizes paths and URLs; `js_to_dart_converter.py` derives Dart from JS blocks; `scan_swap_block.py` reorganizes code sections.

4. **Output** — Writes to `generated-md-files/` or target `api/` subdirectory trees (`2_capi/`, `1_wrapper/`, etc.), creating per-service `index.md` files.

### Key Conventions

- **Hardcoded local paths**: All scripts reference absolute local paths (`/Users/jasonl/...`, `/bitbucket/...`). These must be updated when running on a different machine.
- **Configuration via code**: Section names, target service names, and output directories are set as variables at the top of each script — edit them before running.
- **Regex-heavy**: Transformation logic uses extensive `re` patterns. `re-test.py` is a scratch file for iterating on regex patterns before adding them to main scripts.
- **Output structure**: Generated files follow Docusaurus conventions — lowercase kebab-case filenames, frontmatter-free (navigation defined in `sidebars.js` externally), MDX tabs for multi-language examples.
