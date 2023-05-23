'''
Structuring your project effectively is essential for organization, maintainability, and scalability. While the specific structure may vary depending on your project's size and complexity, here's a general guide to help you structure your project:

1. Root Directory:
   - README.md: Document your project, its purpose, and any instructions or notes for other developers or visitors.
   - index.html: The main HTML file that serves as the entry point for your website.
   - styles: Directory for your CSS or SCSS files.
   - scripts: Directory for your JavaScript files.
   - images: Directory to store images used in your project.
   - assets: Directory for other static assets like fonts, icons, or external libraries.
   - .gitignore: Specify files or directories that should be ignored by Git when committing changes.

2. Styles:
   - main.css: The main CSS file where you can define global styles.
   - components: Directory to store CSS files specific to individual components or sections.
   - utilities: Directory for utility classes or helper CSS files (e.g., for spacing, typography, colors).
   - responsive.css: CSS file for handling responsive styles or media queries.
   - _variables.scss (if using SASS): File to define variables for colors, font sizes, etc.

3. Scripts:
   - main.js: The main JavaScript file where you can define global scripts.
   - components: Directory to store JavaScript files specific to individual components or sections.
   - utilities: Directory for utility scripts or helper functions.
   - vendors: Directory to store third-party libraries or scripts.

4. Images:
   - hero.jpg, logo.png, etc.: Store images used in your project.

5. Assets:
   - fonts: Directory to store custom fonts.
   - icons: Directory for icon files.
   - libraries: Directory to store any external libraries or frameworks used in your project.

6. Additional directories:
   - pages: If your website has multiple pages, create a directory for each page with their respective HTML, CSS, and JavaScript files.
   - data: If your website requires data storage or JSON files, create a directory for data-related files.

7. Build tools (if applicable):
   - If you're using build tools like webpack, Gulp, or npm scripts, you can create additional directories or files specific to your chosen build tool.

Remember that this is a general structure, and you can adapt it to your specific project needs. If you're using a specific framework or tool, it might have its own recommended project structure that you can follow.

Maintaining a clean and well-organized project structure will help you navigate your codebase easily, collaborate with others, and ensure scalability as your project grows.


'''

import os


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


def create_file(path):
    if not os.path.exists(path):
        with open(path, 'w'):
            pass


def create_project_structure():
    root_dir = os.getcwd()  # Set the current working directory as the root directory

    # Top-level directories
    directories = [
        'assets/fonts',
        'assets/icons',
        'assets/libraries',
        'data',
        'images',
        'pages',
        'scripts/components',
        'scripts/utilities',
        'scripts/vendors',
        'styles/components',
        'styles/utilities'
    ]

    for directory in directories:
        create_directory(os.path.join(root_dir, directory))

    # Create individual files
    files = [
        '.gitignore',
        'README.md',
        'index.html',
        'scripts/main.js',
        'styles/main.css',
        'assets/fonts/README.md',
        'assets/icons/README.md',
        'assets/libraries/README.md',
        'data/README.md',
        'images/README.md',
        'pages/README.md',
        'scripts/components/README.md',
        'scripts/utilities/README.md',
        'scripts/vendors/README.md',
        'styles/components/README.md',
        'styles/utilities/README.md'
    ]

    for file in files:
        create_file(os.path.join(root_dir, file))

    print("Project structure created successfully.")


# Run the script to create the project structure
create_project_structure()
