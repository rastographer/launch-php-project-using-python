# launch-php-project-using-python
 This Python script is meant to fastrack launching of a PHP project .

# PHP Project Setup

This Python script is designed to set up PHP projects by creating folders and files according to a predefined structure. It also includes custom content for specific files and generates classes with CRUD methods for functions files. Comes with all modules such as Content Management System, user panel, admin panel, authentication, landing page and user management.

## Folder Structure

- **admin/**
  - index.php
  - **auth/**
    - login.php
    - logout.php
  - **partials/**
    - header.php
    - footer.php
  - **includes/**
    - email-user.php
    - sidebar.php
  - **components/**
    - dashboard-content.php
    - manage-users.php
    - manage-tickets.php
    - manage-testimonials.php
    - manage-pages.php
    - manage-blogs.php
    - global-settings.php
    - show-user.php
    - show-ticket.php
    - show-testimonial.php
    - show-blog.php
    - show-page.php
    - create-user.php
    - create-ticket.php
    - create-testimonial.php
    - create-page.php
    - create-blog.php
    - edit-user.php
    - edit-ticket.php
    - edit-testimonial.php
    - edit-page.php
    - edit-blog.php
    - delete-user.php
    - delete-ticket.php
    - delete-testimonial.php
    - delete-page.php
    - delete-blog.php
- **user/**
  - index.php
  - **auth/**
    - login.php
    - logout.php
    - register.php
    - forgot-password.php
    - reset-password.php
  - **components/**
    - dashboard-content.php
    - my-profile.php
    - edit-profile.php
    - my-tickets.php
    - show-ticket.php
  - **includes/**
    - reply-ticket.php
    - close-ticket.php
- **config/**
  - db.php
  - router.php
  - **functions/**
    - admin-funtions.php
    - home-functions.php
    - user-functions.php
- **user/partials/**
  - header.php
  - footer.php
- **assets/**
  - **css/**
    - style.css
  - **js/**
    - admin.js
    - user.js
    - home.js
- **pages/**
  - index.php
  - pages.php
  - page.php
- **blogs/**
  - index.php
  - blogs.php
  - blog.php
- **libs/**
  - mailer.php
  - input.php
  - output.php
  - payment.php
- **emails/**
  - email-confirmation.html
  - message-from-admin.html
  - support-email.html
  - reset-password.html
- index.php
- README.md

## Custom Content

Custom content is included for specific files, such as `index.php` and `.htaccess`, to provide boilerplate code and configurations.

## CRUD Operations

Classes with CRUD methods are generated for functions files to facilitate Create, Read, Update, and Delete operations.

## Usage

1. Clone this repository.
2. Navigate to the project directory.
3. Run the Python script to create the project structure and files.

## License

This project is licensed under the [MIT License](LICENSE).