# Quora Clone

The Quora Clone is a Django-based web application that allows users to create and manage topics, ask questions in any topic and answer any question in any topic, user can like and dislike any answer or any questions and can follow any topics. It provides a platform for users to have discussions of different topics related to anything world has to offer.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Features
- User registration, authentication, password reset and user info reset 
- Create Topics t have discussion in.
- Add Question to any topic.
- Add answer/comment to any topic
- Like/dislike any Question or Answer
- See Profile of any User

## Installation

1. Clone the repository.
2. Install the required dependencies: `pip install -r requirements.txt`.
3. Configure the environment variables (see [Configuration](#configuration)).
4. Run the migrations: `python manage.py migrate`.
5. Start the development server: `python manage.py runserver`.

## Usage

1. Register a new user account.
2. Log in to your account.
3. Create new topic or browse existing ones.
4. Ask Question in any topic about anything.
5. Asnswer any question in any topic.
6. Like or Dislike any Answer.
7. Like or Dislike any Question.
8. Follow Any Topic
8. Manage your profile.
9. Log out from your account when finished.

## Configuration

The following environment variables are required:

- `EMAIL_HOST_USER`: SMTP email host username.
- `EMAIL_HOST_PASSWORD`: SMTP email host password.
- `SECRET_KEY`: Django secret key.
- `DB_PASSWORD`: Database name.
- `DB_NAME`: Database password.
- `CLOUD_NAME`: Cloudinary cloud name.
- `API_KEY`: Cloudinary API key.
- `API_SECRET`: Cloudinary API secret.


