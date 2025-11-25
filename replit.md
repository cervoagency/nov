# Clarity by Nisar Solutions

## Overview
This is a Dash web application called "Clarity" developed by Nisar Solutions. It's a demo application with a questionnaire feature that includes data visualization using Plotly charts.

## Project Structure
- `app.py` - Main Dash app initialization and configuration
- `index.py` - Application entry point with routing and layout
- `layouts.py` - Page layouts including Home and questionnaire pages
- `navbar.py` - Navigation sidebar component
- `callbacks.py` - Dash callbacks including mobile menu toggle
- `data.py` - Sample data for charts
- `assets/` - Static assets including:
  - `bootstrap-grid.css` - Consolidated Bootstrap grid and all custom modern styling
  - Image assets (logos)
- `requirements.txt` - Python dependencies

## Technology Stack
- **Python 3.11**
- **Dash 2.9.2** - Main web framework
- **Dash Bootstrap Components 1.0.3** - UI components
- **Plotly 5.19.0** - Interactive charts
- **Pandas 2.0.2** - Data manipulation
- **Flask 2.0.3** - Web server (used by Dash)
- **Gunicorn 20.1.0** - Production WSGI server

## Configuration
### Development
- Host: 0.0.0.0
- Port: 5000
- Debug mode: enabled

### Production Deployment
- Deployment target: autoscale (stateless web app)
- Server: Gunicorn with reuse-port flag
- Command: `gunicorn --bind=0.0.0.0:5000 --reuse-port index:server`

## Features
1. **Home Page** - Simple landing page
2. **Questionnaire Page** - Interactive form with:
   - Company type dropdown
   - Multiple numeric inputs for financial data
   - Location dropdown (Montreal/Toronto)
   - Submit button
   - Three visualization charts:
     - Pie chart showing data by location
     - Two indicator gauges

## Recent Changes (November 25, 2025 - Final Update)
- **Consolidated CSS Architecture:**
  - Merged all custom styles into existing `assets/bootstrap-grid.css` file
  - Removed separate `custom_styles.css` file
  - All styling now centralized in one CSS file for cleaner codebase
  - Combined Bootstrap grid system with modern UI/UX styles

## Initial Setup (November 25, 2025)
- Imported from GitHub and configured for Replit environment
- Updated server configuration to run on 0.0.0.0:5000
- Installed Python 3.11 and all dependencies
- Configured workflow for automatic startup
- Set up deployment configuration with Gunicorn
- Added .gitignore for Python projects
- **Modernized UI/UX Design:**
  - Created custom CSS stylesheet with modern design system
  - Implemented purple/indigo gradient color scheme
  - Added Inter and Poppins fonts for better typography
  - Redesigned sidebar with gradient background and improved navigation
  - Created modern hero section on home page with gradient text
  - Added feature cards showcasing app capabilities
  - Improved form styling with better spacing and modern inputs
  - Enhanced charts with card containers and shadows
  - Added smooth animations and hover effects
- **Comprehensive Responsive Design:**
  - Mobile-first approach with breakpoints for phone (≤576px), tablet (577-992px), and desktop (≥993px)
  - Mobile hamburger menu with slide-in sidebar and overlay
  - Responsive grid system using Bootstrap breakpoints (xs, sm, md, lg)
  - Optimized typography scaling across all device sizes
  - Full-width buttons and stacked cards on mobile
  - Responsive charts that adapt to screen size
  - Touch-friendly input sizes (16px minimum to prevent iOS zoom)
  - Landscape orientation optimizations for tablets
  - Print-friendly styles

## Notes
- The application uses Bootstrap Zephyr theme with custom CSS overlay
- Navigation uses a fixed gradient sidebar with white active states
- Charts are interactive and editable
- Modern design system with gradients, shadows, and smooth transitions
- Responsive layout with proper spacing and visual hierarchy
- Original deployment was configured for Heroku (Procfile present)
