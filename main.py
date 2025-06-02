import os
from services.rss_feed import fetch_techcrunch_articles
from services.llm_processor import synthesize_content
from services.image_generator import generate_image
from services.facebook_api import post_to_facebook
from utils.logger import logging

def run_daily_pipeline():
    try:
        # Step 1: Fetch articles
        articles = fetch_techcrunch_articles()
        logging.info("Fetched articles successfully.")
        
        # Step 2: Synthesize content
        content_plan = synthesize_content(articles)
        logging.info("Content synthesized.")
        
        # Step 3: Generate image
        image_path = generate_image(content_plan["image_prompt"])
        logging.info("Image generated.")
        
        # Step 4: Post to Facebook
        post_to_facebook(content_plan, image_path)
        logging.info("Post published to Facebook.")
        
    except Exception as e:
        logging.error(f"Error in pipeline: {e}")

if __name__ == "__main__":
    run_daily_pipeline()