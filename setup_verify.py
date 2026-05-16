#!/usr/bin/env python
"""
Quick setup and verification script for the test automation framework.
"""
import sys
import subprocess
import os

def print_header(message):
    print("\n" + "="*60)
    print(message)
    print("="*60)

def verify_installation():
    """Verify all required packages are installed."""
    print_header("VERIFICATION: Checking Installed Packages")
    
    packages = {
        'selenium': 'Selenium WebDriver',
        'pytest': 'Pytest Test Framework',
        'webdriver_manager': 'WebDriver Manager',
        'dotenv': 'Python Dotenv',
        'PIL': 'Pillow Image Library'
    }
    
    for package, name in packages.items():
        try:
            __import__(package)
            print(f"✓ {name}: OK")
        except ImportError:
            print(f"✗ {name}: MISSING")
            return False
    
    return True

def cleanup_webdriver_cache():
    """Clean up old WebDriver cache."""
    print_header("CLEANUP: Clearing WebDriver Cache")
    
    cache_dirs = [
        os.path.expanduser("~/.wdm"),
        os.path.join(os.path.expanduser("~"), ".cache", "wdm")
    ]
    
    for cache_dir in cache_dirs:
        if os.path.exists(cache_dir):
            print(f"Cleaning: {cache_dir}")
            try:
                import shutil
                shutil.rmtree(cache_dir)
                print(f"✓ Cleaned: {cache_dir}")
            except Exception as e:
                print(f"✗ Error cleaning {cache_dir}: {e}")

def main():
    """Run all verification steps."""
    print_header("OLG TEST AUTOMATION - SETUP VERIFICATION")
    
    # Step 1: Verify Installation
    if not verify_installation():
        print("\n✗ Some packages are missing. Running: pip install -r requirements.txt")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Step 2: Cleanup WebDriver Cache
    cleanup_webdriver_cache()
    
    print_header("SETUP VERIFICATION COMPLETE")
    print("\nTo run tests, execute:")
    print("  pytest -v")
    print("\nFor specific test suites:")
    print("  pytest -v -m part1    # Run Part 1 tests")
    print("  pytest -v -m part2    # Run Part 2 tests")
    print("\nFor HTML reports:")
    print("  pytest --html=reports/report.html --self-contained-html")

if __name__ == "__main__":
    main()
