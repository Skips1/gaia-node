import requests
import random
import time
import logging
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("chatbot.log"),
        logging.StreamHandler()
    ]
)

# Configuration
BASE_URL = "https://ruesandora.gaia.domains"
MODEL = "qwen2-0.5b-instruct"
MAX_RETRIES = 100  # Essentially infinite retries
RETRY_DELAY = 5  # Seconds between retries
QUESTION_DELAY = 1  # Seconds between successful questions

QUESTIONS = [
"How to design and build websites using no-code." ,
"What are the benefits of using no-code platforms for website building?" ,
"What are the most popular no-code website builders currently available?" ,
"How do I choose the right no-code website builder for my project?" ,
"How do I get started with designing my website on a no-code platform?" ,
"How do I add pages, navigation, and other elements to my website using a no-code platform?" ,
"How do I customize the look and feel of my website using a no-code platform?" ,
"What options do I have for integrating third-party tools and services into my website using no-code?" ,
"How do I make sure my website is mobile-friendly using a no-code platform?" ,
"What steps do I need to take to launch my website using a no-code platform?" ,
"Can I use a no-code platform to build an e-commerce website?" ,
"What are the limitations of using a no-code platform to build a website?" ,
"How do I handle SEO for my website when using a no-code platform?" ,
"What resources are available to help me learn more about using no-code for website building?" ,
"Can I hire a professional to help me build my website using a no-code platform?" ,
"How much does it cost to build a website using a no-code platform?" ,
"Can I create a custom domain for my website using a no-code platform?" ,
"How can I get support if I run into issues while building my website using a no-code platform?" ,
"How do I maintain and update my website after it has been built using a no-code platform?" ,
"What are some examples of websites built using no-code platforms?" ,
"What kind of websites can be built using a no-code platform?" ,
"How do I add custom code to my website if needed when using a no-code platform?" ,
"How can I add forms and other interactive elements to my website using a no-code platform?" ,
"What options do I have for hosting my website when using a no-code platform?" ,
"How can I use no-code to create a landing page for my website?" ,
"How do I make sure my website is accessible and inclusive using a no-code platform?" ,
"How do I add and manage images and other media on my website using a no-code platform?" ,
"How can I add blog functionality to my website using a no-code platform?" ,
"Can I use a no-code platform to build a website for a business or organization?" ,
"How do I add e-mail sign-up forms and newsletters to my website using a no-code platform?" ,
"How can I track website analytics using a no-code platform?" ,
"Can I use a no-code platform to build a portfolio website for my creative work?" ,
"How can I add social media integration to my website using a no-code platform?" ,
"Can I use a no-code platform to build a website for a non-profit organization?" ,
"How can I add a search function to my website using a no-code platform?" ,
"How do I ensure the security of my website when using a no-code platform?" ,
"What is the process for publishing and launching a website using a no-code platform?" ,
"How can I integrate payment systems into my e-commerce website using a no-code platform?" ,
"Can I use a no-code platform to build a website for a local business or small enterprise?" ,
"Can I use a no-code platform to build a website for a local business or small enterprsise?" ,
"How do I add a custom favicon to my website using a no-code platform?" ,
"How can I add Google Maps integration to my website using a no-code platform?" ,
"What options do I have for integrating email marketing into my website using a no-code platform?" ,
"How do I add customer reviews and testimonials to my website using a no-code platform?" ,
"How can I add a contact form to my website using a no-code platform?" ,
"What resources are available to help me troubleshoot issues while building my website using a no-code platform?" ,
"How can I use a no-code platform to create a website for a community or social network?" ,
"How can I add a photo gallery to my website using a no-code platform?" ,
"What options do I have for adding custom fonts and typography to my website using a no-code platform?" ,
"Can I use a no-code platform to build a website for a personal blog or diary?" ,
"How can I optimize my website for search engines using a no-code platform?" ,
"How to use no-code for building applications." ,
"What are the benefits of using no-code for building applications?" ,
"What kind of applications can be built using no-code platforms?" ,
"What are the most popular no-code platforms for building applications?" ,
"How do I choose the right no-code platform for building my application?" ,
"How do I get started with designing my application using a no-code platform?" ,
"How do I add and manage data in my application using a no-code platform?" ,
"What options do I have for integrating third-party services into my application using no-code?" ,
"How do I customize the user interface of my application using a no-code platform?" ,
"How do I add and manage users in my application using a no-code platform?" ,
"How do I handle security and privacy when building an application using a no-code platform?" ,
"How do I handle user authentication and authorization in my application using a no-code platform?" ,
"How do I test and debug my application when using a no-code platform?" ,
"How do I handle data migration when building an application using a no-code platform?" ,
"How do I handle data migration when building an application using a no-code platform?" ,
"Can I add custom code to my application when using a no-code platform?" ,
"How do I add user-generated content to my application using a no-code platform?" ,
"How do I handle scalability and performance when building an application using a no-code platform?" ,
"Can I use a no-code platform to build a mobile application?" ,
"How do I handle payments and billing when building an application using a no-code platform?" ,
"How do I handle email and SMS notifications in my application using a no-code platform?" ,
"How do I handle push notifications in my application using a no-code platform?" ,
"How do I handle user analytics and tracking in my application using a no-code platform?" ,
"How do I handle error handling and exception handling in my application using a no-code platform?" ,
"How do I handle user feedback and bug reporting in my application using a no-code platform?" ,
