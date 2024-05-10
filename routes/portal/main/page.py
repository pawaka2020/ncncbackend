# routes/portal/main/page.py

from flask import Flask, Blueprint, render_template, send_file
from os.path import dirname, join
from blueprints import main_bp

def calculate(starting_number):
    return (starting_number * 2)

# Define the function to handle button click
def handleButtonClick():
    print("wss  !")

# Define a function to handle form submission
def handleFormSubmit():

    print("Form submitted!")

page_style = """
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            padding: 20px;
        }
        h1 {
            color: #333333;
        }
        .container {
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin: 0 auto;
            max-width: 600px;
        }
    </style>
"""

container = f"""
    <div class="container">
        <h1>Welcome to My Website</h1>
        <p>This is dynamically generated web content with embedded CSS styles!</p>
    </div>
"""

# @main_bp.route('/', methods=['GET'])
# def page():
#     html_content = f"""
#     <head>
#         <meta charset="UTF-8">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>Dynamic Web Content with CSS</title>
#         {page_style}
#     </head>
#     <!-- This is a comment. It will not be displayed in the browser -->
#     <body>
#         {container}
#     </body>
#     """
#     return html_content