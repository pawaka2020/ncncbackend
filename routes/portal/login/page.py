# # routes/portal/login/page.py

# from flask import Blueprint, render_template, send_file, request, redirect, url_for
# from blueprints import portal_bp
# from routes.portal.style import portal_style

# # Counter variable
# counter = 0

# def buttoncounter():
#     global counter
#     return f"""
#     <div class="item">
#         <h1>Button Click Counter</h1>
#         <p>Count: {counter}</p>
#         <form action="/increment_counter" method="post">
#             <button type="submit">Click Me!</button>
#         </form>
#     </div>
# """

# # Increment the counter when the button is clicked
# @portal_bp.route('/increment_counter', methods=['POST'])
# def increment_counter():
#     global counter
#     counter += 1
#     return redirect(url_for('portal_bp.page'))

# # Shows webpage for the login page of a company portal.
# # Expected UI elements: company logo image, login field, password field, login button
# # the CSS style is already defined via 'portal_style', so don't touch this for now.
# @portal_bp.route('/', methods=['GET'])
# def page():
#     html_content = f"""
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Portal login page</title>
#     {portal_style()}
#     </head>
#     <body>
#         <div class="container">
#             {buttoncounter()}
#             <div class="container">
#     <h1>Button Counter</h1>
#     <button id="counterBtn">Click me!</button>
#     <p>Counter: <span id="count">0</span></p>
#   </div>
#   <script>
#     // Get the button and counter elements
#     const counterBtn = document.getElementById('counterBtn');
#     const countSpan = document.getElementById('count');

#     // Initialize counter variable
#     let counter = 0;

#     // Function to update counter and display
#     function increaseCounter() {
#     #   counter++;
#     #   countSpan.textContent = counter;
#     # }

#     // Add event listener to the button
#     counterBtn.addEventListener('click', increaseCounter);
#   </script> 
#         </div>
#     </body>
#     </html>
#     """
#     return html_content