import os

folders = {
    "admin": {"auth": [], "partials": [], "components": [], "includes": []},
    "user": {"auth": [], "partials": [], "components": [], "includes": []},
    "libs": {},
    "config": {"functions": []},
    "assets": {"images": [], "css": [], "js": []},
    "pages": {"images": []},
    "blogs": {"images": []},
    "emails": {}
}

files = {
    "admin": ["index.php"],
    "admin/auth": ["login.php", "logout.php"],
    "admin/partials": ["header.php", "footer.php"],
    "admin/includes": ["email-user.php", "sidebar.php"],
    "admin/components": ["dashboard-content.php", "manage-users.php", "manage-tickets.php", "manage-testimonials.php", "manage-pages.php", "manage-blogs.php", "global-settings.php", "show-user.php", "show-ticket.php", "show-testimonial.php", "show-blog.php", "show-page.php", "create-user.php", "create-ticket.php", "create-testimonial.php", "create-page.php", "create-blog.php", "edit-user.php", "edit-ticket.php", "edit-testimonial.php", "edit-page.php", "edit-blog.php", "delete-user.php", "delete-ticket.php", "delete-testimonial.php", "delete-page.php", "delete-blog.php"],
    "user": ["index.php"],
    "user/auth": ["login.php", "logout.php", "register.php", "forgot-password.php", "reset-password.php"],
    "user/components": ["dashboard-content.php", "my-profile.php", "edit-profile.php", "my-tickets.php", "show-ticket.php"],
    "user/includes": ["reply-ticket.php", "close-ticket.php"],
    "config": ["db.php", "router.php"],
    "config/functions": ["admin-funtions.php", "home-functions.php", "user-functions.php"],
    "user/partials": ["header.php", "footer.php"],
    "assets/css": ["style.css"],
    "assets/js": ["admin.js", "user.js", "home.js"],
    "pages": ["index.php", "pages.php", "page.php"],
    "blogs": ["index.php", "blogs.php", "blog.php"],
    "libs": ["mailer.php", "input.php", "output.php", "payment.php"],
    "emails": ["email-confirmation.html", "message-from-admin.html", "support-email.html", "reset-password.html"],
    "": ["index.php", "README.md"]  # Files at the root level
}

# Content for db.php file
db_content = """<?php

// Production Env values

// $servername = "localhost";
// $username = "afrishar_remotasks";
// $password = "rzcb5lAlf-GH#0n~O8";
// $database = "afrishar_remotasks";

// Local Env values

$servername = "127.0.0.1";
$username = "root";
$password = "";
$database = "your_db_name";

// Create connection
$conn = new mysqli($servername, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}"""

# Custom content for specific files
custom_content = {
    "index.php": """<?php
session_start();
include 'config/functions/home-functions.php';
include 'config/db.php';
echo 'This is home/index.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title><?= $functions->getSetting('site_name'); ?></title>
    <meta name="description" content="<?= $functions->getSetting('site_description'); ?>"/>
    <meta name="keywords" content="<?= $functions->getSetting('site_keywords'); ?>">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <link rel="stylesheet" href="<?= $functions->getSetting('site_url'); ?>assets/styles/main.css">
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=<?= $functions->getSetting('g_analytics'); ?>"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
    
      gtag('config', '<?= $functions->getSetting('g_analytics'); ?>');
    </script>
</head>
<body>

<?php include 'partials/header.php'; ?>

<!-- homepage content -->
<div class="mt-5 mb-5">

   <section class="courses mt-5">
        <p>homepage content</p>
    </section>
</div>

<?php include 'partials/footer.php'; ?>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script>
</body>
</html>""",
    ".htaccess": """<IfModule mod_rewrite.c>
RewriteEngine On
RewriteBase /
RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ index.php [L]
</IfModule>
""",
    # Add more custom content mappings as needed
}

# Class and constructor template
class_template = """<?php
class {class_name} {{
    private $conn;

    public function __construct($conn) {{
        $this->conn = $conn;
    }}

    public function create($data) {{
        // Create logic here
    }}

    public function read($id) {{
        // Read logic here
    }}

    public function update($id, $data) {{
        // Update logic here
    }}

    public function delete($id) {{
        // Delete logic here
    }}
}}
"""

def create_folders_and_files(base_path, folders, files):
    for folder_name, subfolders in folders.items():
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        if subfolders:
            create_folders_and_files(folder_path, subfolders, {})

    for file_path, file_names in files.items():
        full_path = os.path.join(base_path, file_path)
        for file_name in file_names:
            final_path = os.path.join(full_path, file_name)
            if final_path.endswith("db.php"):
                with open(final_path, "w") as f:
                    f.write(db_content)
            elif final_path in custom_content:
                with open(final_path, "w") as f:
                    f.write(custom_content[final_path])
            elif "functions" in file_path:
                class_name = os.path.splitext(file_name)[0].replace('-', '_').title().replace('_', '')
                with open(final_path, "w") as f:
                    f.write(class_template.format(class_name=class_name))
            elif "admin" in file_path or "user" in file_path:
                with open(final_path, "w") as f:
                    f.write("<?php\nsession_start();\n")
                    if file_name == "index.php":
                        f.write("include 'config/functions/admin-functions.php';\n")
                        f.write("include 'config/db.php';\n")
                    elif file_name == "login.php" or file_name == "logout.php":
                        f.write("include 'config/functions/user-functions.php';\n")
                        f.write("include 'config/db.php';\n")
                    else:
                        f.write("include 'config/functions/user-functions.php';\n")
                        f.write("include 'config/db.php';\n")
                    f.write("echo 'This is " + file_name + "';\n")
            else:
                with open(final_path, "w") as f:
                    f.write("<?php\n")
                    f.write("echo 'This is " + file_name + "';\n")
            print("Created file:", final_path)

# Start from the root directory
starting_path = os.getcwd()
create_folders_and_files(starting_path, folders, files)

print("Directory structure and files created successfully!")


