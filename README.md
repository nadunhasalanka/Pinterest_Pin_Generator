# Pinterest_Pin_Generator
Welcome to the Pinterest Pin Generator Bot! 🎉
This bot helps you create catchy, SEO-friendly Pinterest pins based on keywords using the power of ChatGPT and Google Sheets API. Perfect for Pinterest marketers and content creators looking to level up their pin game and save time on pin generation! This bot even creates pin titles and descriptions for each pin.

## Features 🌟
#### Template-Based Generation: Create pins using two professional templates with:

* Random background coloring
* Overlay images
* Custom shapes (rectangles, circles)
* Customized footer generation
* Random background image selection
#### AI-Powered Content:

* SEO-optimized titles
* Engaging descriptions
* Custom tips generation
* GPT model integration
#### Google Integration:

* Seamless Google Sheets connectivity
* Automated data reading/writing
* Bulk pin generation

## Understanding the Core Files 🔍

### base.py
The backbone of our Pinterest Generator. Handles all basic operations like file management, CSV operations, and logging. It defines crucial constants and paths used throughout the project. Think of it as the command center that keeps everything organized and flowing smoothly.

### settings.py
This is the design control center! Contains template settings. Each class manages visual aspects like colors, fonts, spacing, and layout parameters. Want to change how your pins look? This is where the magic happens. Modify colors, adjust text sizes, or tweak spacing - all through simple parameter adjustments.

### writer.py - The Content Creator
The AI-powered writing assistant. Connects with GPT to generate engaging titles, descriptions, and tips for your pins. It handles Google Sheets integration, reading your keywords, and transforming them into Pinterest-ready content. This file manages all the text generation workflow, from prompt processing to saving the final content.

### image_generator.py - The Design Studio
The artistic powerhouse! Takes all the settings and content, then transforms them into visually stunning Pinterest pins. It handles:

* Background image placement and manipulation
* Text positioning and styling
* Shape drawing (rectangles, circles)
* Footer generation
* Template-specific layouts

Template1ImageGenerator: Creates pins with numbered tips and circular markers

Template2ImageGenerator: Produces pins with stylish text layouts and different font combinations

### main.py
The central control file that brings everything together. It's where you specify your project name, choose templates, and start the generation process. Simple and straightforward - just set your preferences and let it coordinate all the other components.


## Setup Guide 🛠️
#### 1. Initial Setup
* Clone this repository
* Install Python 3.x
#### 2. Google Cloud Configuration
* Create new project in Google Cloud Console
* Enable required APIs:
* Google Sheets API
* Google Drive API
* Create Service Account:
* Navigate to Credentials > Manage Service Accounts
* Generate new JSON key
* Save as data/keyfile.json
#### 3. Google Sheet Structure
#### Create a Google Sheet that like Provided one


### Customization 🎨
#### Background Images
* Place images in: projects/project_name/assets/backgrounds
* Ensure images match template dimensions
#### Fonts
* Location: image_assets/template/fonts/
* Customize fonts to match your brand
#### Settings
* Modify settings.py for template customization
* Toggle features using boolean values
* Adjust colors, sizes, and positions
### Usage 🚀
#### 1. Configure main.py:
project_name = 'YourProject'
generator_modes = ['template_1', 'template_2']

image_generator(project_name, generator_modes[0])

#### 2. Run the generator:
python main.py


## Requirements 📋
Python 3.x & Google Sheets API credentials

Your generated pins will be saved in the Projects folder, ready for Pinterest upload! 🎯
#### 🔗 Links

[![Link to Sample Google Sheet](https://img.shields.io/badge/Link%20to%20Sample%20Google%20Sheet-34A853?style=for-the-badge&logo=google-sheets&logoColor=white)](https://docs.google.com/spreadsheets/d/1c_eXPXtE21FlCAR0CcKgGjbUJ8HjaafnOs967pqJ_KQ/edit?usp=sharing)



