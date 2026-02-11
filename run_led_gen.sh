#!/bin/bash

# Universal Lead Generation Tool - Quick Run Scripts

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║     UNIVERSAL LEAD GENERATION TOOL                         ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""
echo "Select an option:"
echo "1. Search for schools in Dar es Salaam"
echo "2. Search for businesses"
echo "3. Search for restaurants"
echo "4. Load and analyze existing database"
echo "5. Research missing contacts"
echo ""
read -p "Enter choice (1-5): " choice

case $choice in
    1)
        echo "Searching for schools..."
        python contact-inder_enhanced.py --mode search --type school --location "Dar es Salaam, Tanzania" --keywords "English medium" "private" --limit 50 --service all
        ;;
    2)
        echo "Searching for businesses..."
        python contact-inder_enhanced.py --mode search --type business --location "Dar es Salaam, Tanzania" --limit 30 --service all
        ;;
    3)
        echo "Searching for restaurants..."
        python contact-inder_enhanced.py --mode search --type restaurant --location "Dar es Salaam, Tanzania" --limit 25 --service all
        ;;
    4)
        read -p "Enter CSV filename: " filename
        python contact-inder_enhanced.py --mode load --file "$filename"
        ;;
    5)
        read -p "Enter CSV filename: " filename
        python contact-inder_enhanced.py --mode research --file "$filename" --service all
        ;;
    *)
        echo "Invalid choice"
        ;;
esac