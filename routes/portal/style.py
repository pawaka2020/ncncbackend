# routes/portal/style.py

# Provides a common CSS style that will be used for all portal webpages in this app.

def portal_style():
    return """
        <style>
        body, html {
            height: 100%;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: flex-start;
        }
        .container {
            text-align: center;
        }
        .item {
            display: block;
            margin-bottom: 10px; /* Adjust spacing between items as needed */
        }
        .margin {
            display: block;
            margin-top: 40px;
            margin-bottom: 40px;
        }
        </style>
    """