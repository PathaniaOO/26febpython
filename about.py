#!/usr/bin/env python3
"""
February 26 - Today's Special Program
A fun program celebrating February 26, 2026
"""

from datetime import datetime, timedelta

def main():
    # Today's date
    today = datetime(2026, 2, 26)
    
    print("=" * 50)
    print(f"📅 Happy February 26, 2026!")
    print("=" * 50)
    
    # Display date information
    print(f"\nToday's Date: {today.strftime('%A, %B %d, %Y')}")
    print(f"Day of Year: {today.timetuple().tm_yday}")
    print(f"Week Number: {today.isocalendar()[1]}")
    
    # Days remaining in February
    feb_end = datetime(2026, 2, 28)  # 2026 is not a leap year
    days_left = (feb_end - today).days
    print(f"\nDays remaining in February: {days_left}")
    
    # Days remaining in the year
    year_end = datetime(2026, 12, 31)
    days_until_year_end = (year_end - today).days
    print(f"Days remaining in 2026: {days_until_year_end}")
    
    # Interesting fact about the number 26
    print("\n" + "=" * 50)
    print("Fun Facts about 26:")
    print("=" * 50)
    print("• 26 is the only number between a square (25) and a cube (27)")
    print("• There are 26 letters in the English alphabet")
    print("• 26 is a repdigit in base 5 (101)")
    
    # Special events on Feb 26 (approximate)
    print("\n" + "=" * 50)
    print("Historical Significance:")
    print("=" * 50)
    print("• Victor Hugo died on February 26, 1885")
    print("• NYC subway opened on February 26, 1968")
    
    print("\n" + "=" * 50)
    print("✨ Make today count! ✨")
    print("=" * 50)
    print("+" * 50)
    print("-" * 50)

if __name__ == "__main__":
    main()
