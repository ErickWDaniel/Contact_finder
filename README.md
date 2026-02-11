# Tanzania Contact Finder & Lead Generation

A comprehensive Python-based lead generation tool for finding and managing contact information for organizations in Tanzania, with a focus on private schools in Dar es Salaam.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Output Formats](#output-formats)
- [GUI Application](#gui-application)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a systematic approach to identifying and acquiring contact information for private schools in Dar es Salaam, Tanzania. These schools represent high-value prospects for web development services, as they typically:

- Serve growing middle-class families who expect online visibility
- Lack technical resources to build their own websites
- Are underserved by local web development agencies
- Operate primarily through word-of-mouth and physical marketing

The tool supports multiple organization types and uses various online sources to gather contact data efficiently.

## Features

### Core Functionality

- **Multi-source data collection** from Tanzania Yellow Pages, Google Maps, Facebook Business Pages, and more
- **Tier-based priority system** (Tier A/B/C) for contact completeness
- **Tanzania phone number validation and formatting**
- **CSV/JSON export capabilities**
- **Automated research reports**

### Supported Organization Types

- Schools (primary focus)
- Businesses
- Medical facilities
- Restaurants
- Retail establishments
- Service providers
- Nonprofits

### Data Collection

- Real-time web scraping from public sources
- Built-in Tanzania school database (60+ schools)
- Email and phone number extraction
- Address and location data
- Website status detection
- Social media link discovery

## Project Structure

```
hunters/
├── README.md                 # This file
├── contact-inder_enhanced.py # Main lead generation tool (3,000+ lines)
├── gui_app.py               # GUI interface for the tool
├── dar_schools.csv          # School data in CSV format
├── run_led_gen.sh           # Shell script to run the tool
├── plan.md                  # Project planning document
└── contact_research_report.txt  # Generated research report
```

## Quick Start

### Prerequisites

- Python 3.7 or higher
- Required packages (auto-installed):
  - `urllib3` (standard library)
  - `ssl` (standard library)

### Running the Tool

**Option 1: Shell Script (Linux/Mac)**
```bash
./run_led_gen.sh
```

**Option 2: Direct Python Execution**
```bash
python contact-inder_enhanced.py --interactive
```

**Option 3: Command Line Mode**
```bash
python contact-inder_enhanced.py --mode search --type school --location "Dar es Salaam"
```

## Usage

### Interactive Mode

The interactive menu provides an easy-to-use interface:

```
1. Search for organizations (schools, businesses, etc.)
2. Load existing database
3. Research contacts for loaded organizations
4. View statistics
5. Generate report
6. Export data (CSV/JSON)
7. Tanzania-specific research & export
8. Exit
```

### Command Line Examples

**Search for schools:**
```bash
python contact-inder_enhanced.py --mode search --type school --location "Dar es Salaam"
```

**Load and research contacts:**
```bash
python contact-inder_enhanced.py --mode research --file schools.csv --output updated.csv
```

**Generate comprehensive report:**
```bash
python contact-inder_enhanced.py --mode report --file schools.csv --tanzania
```

**Export schools without websites:**
```bash
python contact-inder_enhanced.py --mode export --file schools.csv --no-website
```

### Command Line Arguments

| Argument | Description |
|----------|-------------|
| `--mode` | Operation mode: search, load, research, report, export, stats, interactive |
| `--type` | Organization type: school, business, medical, restaurant, retail, service, nonprofit |
| `--location` | Search location (e.g., "Dar es Salaam, Tanzania") |
| `--keywords` | Search keywords (space-separated) |
| `--limit` | Maximum number of results (default: 50) |
| `--file` | Input CSV file |
| `--output` | Output file (CSV, JSON, or TXT) |
| `--service` | Search service: yellowpages, google_maps, facebook, brela, education_portal, tanzania_only, all |
| `--tanzania` | Generate Tanzania-specific report |
| `--no-website` | Filter to organizations without websites |
| `--verify-websites` | Verify websites using DuckDuckGo HTML search |
| `--use-fallback-db` | Allow fallback to the built-in Tanzania school database |

## Data Sources

The tool queries multiple public data sources:

### Primary Sources

1. **Tanzania Yellow Pages** (yellowpages.co.tz)
   - Comprehensive business directory
   - Phone numbers, addresses, and contact details

2. **Google Maps** (maps.google.com)
   - Location-based business listings
   - Reviews and contact information

3. **Facebook Business Pages**
   - Business page discovery
   - Social media links

4. **BRELA** (brela.go.tz)
   - Business registrations and licensing agency
   - Official company registrations

### Secondary Sources

5. **Tanzania Education Portal** (moe.go.tz, necta.go.tz)
   - School listings and registrations
   - Educational institution data

6. **Tanzapages** (tanzapages.com)
   - Local business directory
   - Category-based listings

7. **School.co.tz**
   - O-level school listings
   - Regional school data

### Built-in Database

The tool includes a hardcoded database of 60+ Tanzania private schools with contact information, serving as a fallback when online sources are unavailable.

## Output Formats

### CSV Export

```csv
Name,Phone/Mobile,Email,Website Status,Website URL,Address/Location,Priority Tier,Contact Status,Notes
Tusiime Schools,+255 754 123456,info@tusiimeschools.ac.tz,No Website,,Tabata Industrial Area,Tier A,Complete,English medium
```

### JSON Export

```json
{
  "metadata": {
    "generated": "2025-02-11T14:33:02.663Z",
    "total": 50,
    "stats": {...}
  },
  "organizations": [...]
}
```

### Report Format

The tool generates detailed research reports including:
- Executive summary
- Organizations by type and tier
- Contact completeness statistics
- Data sources used
- Priority outreach lists

## GUI Application

A graphical user interface is available in `gui_app.py`:

```bash
python gui_app.py
```

The GUI provides:
- Visual organization browser
- Easy data filtering
- Point-and-click export
- Progress tracking for research operations

## Configuration

### Rate Limiting

The tool implements respectful rate limiting between API calls:

```python
rate_limit_delay = (0.3, 0.8)  # Random delay between 0.3 and 0.8 seconds
```

### Data Validation

Tanzania phone numbers are validated against standard formats:
- `+255 XX XXX XXXX` (international format)
- `0XX XXX XXXX` (local format)

### Tier System

| Tier | Criteria | Priority |
|------|----------|----------|
| Tier A | Complete (phone + email + address) | Ready for outreach |
| Tier B | Partial (phone only or incomplete) | Needs enrichment |
| Tier C | No contact information | Requires research |

## Research Workflow

### Phase 1: Data Verification (Days 1-7)

1. Verify all phone numbers
2. Search for missing emails
3. Confirm school operations

### Phase 2: Data Research (Days 8-14)

1. Research Tier C schools
2. Build contact extraction automation
3. Validate all contacts

### Phase 3: Data Export & Setup (Days 15-21)

1. Export to CSV
2. Import to Google Sheets
3. Create outreach templates

## Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Total Schools Identified | 63+ | School count in database |
| Complete Contact Records | 50+ | Records with phone + email |
| Contact Rate | 80%+ | Schools reachable by phone |
| Data Accuracy | 90%+ | Valid phone numbers and emails |
| Outreach-Ready Records | 40+ | Ready for initial contact |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your changes
4. Submit a pull request

## License

This project is provided for educational and business purposes. Users are responsible for complying with all applicable laws and regulations regarding data collection and outreach.

## Support

For issues and feature requests, please open an issue in the repository.

---

**Last Updated:** February 2025  
**Version:** 3.0
