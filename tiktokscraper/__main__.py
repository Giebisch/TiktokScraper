import argparse

from .TiktokScraper import TiktokScraper

if __name__ == "__main__":
    # requests has to be installed
    try:
        import requests
    except:
        print("Make sure you have 'requests' installed on your system")
        quit()

    parser = argparse.ArgumentParser(prog="TiktokScraper", description="Scrape all relevant data from Tiktok")
    
    parser.add_argument("--video", type=str, help="Scrape all information regarding a specific video including comments. Provide video url or video id", required=False)
    parser.add_argument("--profile", type=str, help="Scrape all information regarding a specific profile. Provide profile url or username", required=False)

    # use webserver to interact with the program
    parser.add_argument("--web", action="store_true", default=False)

    args = parser.parse_args()
    
    if args.web:
        try:
            from flask import Flask
        except:
            print("Make sure you have 'flask' installed on your system")
            quit()
        # from .webserver import *
        from .webserver import *
    else:
        TiktokScraper(args)
