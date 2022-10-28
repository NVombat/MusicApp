## 📌 Prerequisites

### 💻 System requirement :

1. Any system with basic configuration.
2. Operating System : Any (Windows / Linux / Mac).

### 💿 Software requirement :

1. Updated browser
2. Node.js installed (If not download it [here](https://nodejs.org/en/download/)).
3. Python installed (If not download it [here](https://www.python.org/downloads/)).
4. Any text editor of your choice.

## 🔧 Installation & Setup

### 🚧 Server :

Install python dependencies

```
$ pip install -r server/requirements.txt
```

#### 🏗️ AWS Setup :

```
- Login/Create an account

- Navigate to S3 and create a public bucket
- Alter the Bucket Policy and CORS Policy

- Navigate to IAM and create an IAM user
- If an existing IAM user is to be used go to the next step
- Give the IAM user full access to S3 items

- Store the credentials in the .env file
```

#### 📦️ MONGODB Setup :

```
- Login/Create an account

- Create a new project
- Within the project, create a new cluster
- Within the cluster, create a new collection

- Store the credentials in the .env file
```

### 🚚 EMAIL API Setup :

```
- Use any email API (MailGun & EmailJS is used in the app)

- Store the email and password in the .env file
```

Setup the .env file for Database, AWS & Mail functionality

Start the Django server

```
$ python3 manage.py runserver
```

## 🤝 Contributing

Please read [`Contributing.md`](https://github.com/NVombat/MusicApp/blob/main/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.