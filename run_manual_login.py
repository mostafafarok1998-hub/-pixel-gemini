#!/usr/bin/env python3
"""
Manual Login + Auto Offer Finder for Pixel Gemini
-------------------------------------------------
You manually login to Google in the opened browser, then the script
searches for the Gemini Pro offer automatically.

Usage:
    python run_manual_login.py

Steps:
    1. Script opens Chrome with Pixel 10 Pro mobile emulation
    2. Navigate to one.google.com
    3. YOU login manually with your Gmail
    4. Press Enter in the terminal when done
    5. Script searches for the Gemini offer and prints the link
"""

import logging
import time
import sys

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

# Import project modules
from device_simulator import create_device_profile
from google_automation import _build_driver, _check_google_one


def main():
    print("=" * 65)
    print("   Pixel Gemini - Manual Login Mode")
    print("=" * 65)

    # Step 1: Create device profile (Pixel 10 Pro simulation)
    logger.info("Creating Pixel 10 Pro device profile...")
    device = create_device_profile()
    print(f"\n📱 Device : {device.model}")
    print(f"🤖 Android: {device.android_version}")
    print(f"🆔 IMEI   : {device.imei}")
    print(f"🔤 Android ID: {device.android_id}")

    # Step 2: Build Chrome driver with mobile emulation
    logger.info("Launching Chrome with Pixel 10 Pro emulation...")
    driver = _build_driver(device, email="manual_session")

    try:
        # Step 3: Open Google One page
        logger.info("Opening one.google.com ...")
        driver.get("https://one.google.com")

        print("\n" + "=" * 65)
        print("👤 MANUAL LOGIN REQUIRED")
        print("=" * 65)
        print("1. The Chrome browser is now open.")
        print("2. Login with your Gmail account manually.")
        print("3. After you're logged in and see the Google One page,")
        print("   come back here and press ENTER to continue.")
        print("=" * 65)

        input("\n⏳ Press ENTER after you have logged in... ")

        # Step 4: Search for Gemini offer
        logger.info("Starting offer search...")
        print("\n🔍 Searching for Gemini Pro offer...")
        print("   Checking one.google.com/offers ...")

        offer_link = _check_google_one(driver)

        print("\n" + "=" * 65)
        if offer_link:
            print("🎉 GEMINI OFFER FOUND!")
            print(f"🔗 Link: {offer_link}")
        else:
            print("❌ No Gemini offer found on this account.")
            print("   (The offer may not be available for your account/region)")
        print("=" * 65)

        # Keep browser open so user can click the link
        print("\n💡 The browser will stay open. You can click the link above.")
        input("\n🛑 Press ENTER to close the browser and exit... ")

    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user.")
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        logger.info("Closing browser...")
        try:
            driver.quit()
        except Exception:
            pass
        print("👋 Done.")


if __name__ == "__main__":
    main()
