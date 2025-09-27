from js import document

def generate_message(*args, **kwargs):
    # Get input values
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value

    # Create message
    message = f"""\
Student Profile:
    Name: "{name}"
    Age: {age}
    School: {school} Campus
"""

    # Display result
    output = document.getElementById("output")
    output.innerHTML = f"<pre>{message}</pre>"

