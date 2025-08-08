# E-Commerce Website

A full-featured e-commerce web application built with Flask, featuring user authentication, product management, and an admin panel. Deployed on AWS Elastic Beanstalk with Docker.

## 🚀 Live Demo

**Deployed Application:** [Your Elastic Beanstalk URL]

**Admin Access:**
- Username: `admin`
- Password: `admin`

## ✨ Features

### User Features
- **User Registration & Authentication** - Secure account creation and login
- **Product Browsing** - View available items with detailed information
- **Shopping Cart** - Purchase items with budget management
- **Inventory Management** - Sell owned items back to the marketplace
- **User Dashboard** - Track budget and owned items

### Admin Features
- **Admin Panel** - Comprehensive management interface
- **User Management** - View and manage all registered users
- **Product Management** - Control product inventory and pricing
- **Real-time Analytics** - Monitor user activity and sales

### Technical Features
- **Responsive Design** - Mobile-friendly Bootstrap interface
- **Secure Authentication** - Password hashing with bcrypt
- **Form Validation** - WTForms with CSRF protection
- **Database Management** - SQLAlchemy ORM with SQLite
- **Production Ready** - Docker containerization for AWS deployment

## 🛠️ Technology Stack

**Backend:**
- Python 3.11
- Flask 3.1.0
- SQLAlchemy 2.0.38
- Flask-Login 0.6.3
- Flask-Bcrypt 1.0.1
- Flask-WTF 1.2.2

**Frontend:**
- Bootstrap 4.5.3
- Jinja2 Templates
- FontAwesome Icons

**Database:**
- SQLite (Development)
- AWS RDS Compatible (Production scaling)

**Deployment:**
- Docker
- AWS Elastic Beanstalk
- Gunicorn WSGI Server

## 📦 Installation & Setup

### Prerequisites
- Python 3.11+
- Docker (for containerized deployment)
- AWS CLI (for cloud deployment)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/syedsajjadaskari/sample-flask-ecommerce.git
   cd sample-flask-ecommerce
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize database**
   ```bash
   python init_db.py
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

6. **Access the application**
   - Local URL: `http://localhost:80`
   - Admin Panel: Login with `admin` / `admin`

### Docker Development

1. **Build Docker image**
   ```bash
   docker build -t flask-ecommerce .
   ```

2. **Run container**
   ```bash
   docker run -p 80:80 flask-ecommerce
   ```

3. **Access application**
   - URL: `http://localhost:80`

## ☁️ AWS Deployment

### Setup AWS CLI

1. **Install AWS CLI**
   ```bash
   # Linux/macOS
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   unzip awscliv2.zip
   sudo ./aws/install
   
   # Install EB CLI
   pip install awsebcli
   ```

2. **Configure AWS credentials**
   ```bash
   aws configure
   ```



### Environment Configuration

The application requires these environment variables in production:

```bash
SECRET_KEY=your-32-character-secret-key
FLASK_ENV=production
```
Steps to Fix This:

Generate a secret key:

bashpython3 -c "import secrets; print(secrets.token_hex(32))"

Copy the generated key (it will look like: a1b2c3d4e5f6789012345678901234567890abcdef1234567890abcdef123456)
Update your Elastic Beanstalk configuration:

## 📁 Project Structure

```
sample-flask-ecommerce/
├── .ebextensions/          # AWS Elastic Beanstalk configuration
│   └── 01_docker.config
├── Market/                 # Main application package
│   ├── __init__.py        # App initialization and database setup
│   ├── models.py          # Database models (User, Item)
│   ├── routes.py          # Application routes and logic
│   ├── forms.py           # WTForms for user input
│   └── templates/         # Jinja2 HTML templates
│       ├── base.html      # Base template with navigation
│       ├── HOME.html      # Landing page
│       ├── LOGIN.html     # User login form
│       ├── REGISTER.html  # User registration form
│       ├── MARKET.html    # Main shopping interface
│       ├── ADMIN.html     # Admin panel
│       └── modals/        # Modal components
├── init_db.py             # Database initialization script
├── main.py                # Development server entry point
├── application.py         # Production entry point
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── .dockerignore         # Docker ignore rules
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

## 🗄️ Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email_address TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    budget INTEGER NOT NULL DEFAULT 10000
);
```

### Items Table
```sql
CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    barcode TEXT UNIQUE NOT NULL,
    price INTEGER NOT NULL,
    description TEXT NOT NULL,
    owner INTEGER REFERENCES users (id)
);
```

## 🎯 Usage Guide

### For Regular Users

1. **Registration**
   - Create account with unique username and email
   - Start with $10,000 budget

2. **Shopping**
   - Browse available items in the marketplace
   - Click "Info" to view item details
   - Click "Buy" to purchase items
   - Manage owned items in the sidebar

3. **Selling**
   - Sell owned items back to the marketplace
   - Receive full purchase price back

### For Administrators

1. **Admin Access**
   - Login with username: `admin`, password: `admin`
   - Access admin panel from navigation

2. **User Management**
   - View all registered users
   - Monitor user budgets and inventories
   - Delete users if necessary

3. **Product Management**
   - View all items and their owners
   - Update item information
   - Delete items from marketplace

## 🔧 Development

### Adding New Features

1. **Database Models** - Add new models in `Market/models.py`
2. **Routes** - Add new routes in `Market/routes.py`
3. **Forms** - Create forms in `Market/forms.py`
4. **Templates** - Add HTML templates in `Market/templates/`

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-flask

# Run tests
pytest
```

### Database Management

```bash
# Reset database
rm Market/e-commerce.db
python init_db.py

# Add sample data
python -c "from init_db import init_database; init_database()"
```

## 🚨 Security Features

- **Password Hashing** - bcrypt for secure password storage
- **CSRF Protection** - Flask-WTF CSRF tokens
- **Session Management** - Secure Flask sessions
- **Input Validation** - WTForms validation
- **SQL Injection Prevention** - SQLAlchemy ORM


## 📝 Dependencies

```
bcrypt==4.3.0
blinker==1.9.0
click==8.1.8
Flask==3.1.0
Flask-Bcrypt==1.0.1
Flask-Login==0.6.3
Flask-SQLAlchemy==3.1.1
Flask-WTF==1.2.2
greenlet==3.1.1
gunicorn==23.0.0
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.2
packaging==24.2
SQLAlchemy==2.0.38
typing_extensions==4.12.2
Werkzeug==3.1.3
WTForms==3.2.1
```

## 🐛 Troubleshooting

### Common Issues

**502 Bad Gateway**
- Check application logs: `eb logs`
- Verify SECRET_KEY is set
- Ensure database initialization completed

**Database Errors**
- Run `python init_db.py` to reinitialize
- Check file permissions in Docker container

**Deployment Issues**
- Verify AWS credentials: `aws sts get-caller-identity`
- Check Elastic Beanstalk configuration files
- Review Docker build logs

### Getting Help

1. Check application logs: `eb logs`
2. Verify environment variables: `eb printenv`
3. Test locally first: `python main.py`
4. Review AWS Elastic Beanstalk console

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Syed Sajjad Askari**
- GitHub: [@syedsajjadaskari](https://github.com/syedsajjadaskari)
- Email: [your-email@example.com]

## 🙏 Acknowledgments

- Flask community for excellent documentation
- Bootstrap team for responsive CSS framework
- AWS for reliable cloud infrastructure
- SQLAlchemy for powerful ORM capabilities

