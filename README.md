# GreenTech
Green Tech Energy is an online platform created by me as an Admin for selling and managing solar panel products. This project, which is my major internship for the MCA final year, aims to digitize traditional energy solutions. It provides a 24/7 accessible online store, secure payment methods, and real-time inventory management to enhance user convenience.

# Green Tech Energy Solar Panel Website
## Introduction
Green Tech Energy is an online platform designed for the sale and management of solar panel products. Developed by DataCause Analytics Pvt. Ltd., this project aims to transition traditional energy solutions into the digital space, enhancing user convenience with a 24/7 accessible online store, secure payment options, and real-time inventory management.

## Project Overview

The Green Tech Energy platform aims to streamline solar panel ordering and customer management, providing a user-friendly e-commerce site that automates inventory, transactions, and customer interactions. It’s built using the Django framework and features robust back-end support to ensure data security, real-time product updates, and efficient order management.

## Features

- **User Account Management**: Profile management for both customers and administrators.
- **Product Catalog**: Detailed catalog of solar panels and related products, with filtering options.
- **Shopping Cart**: Add, update, or remove items from the cart, with automatic total calculation.
- **Order Tracking**: Real-time order status updates for customers.
- **Payment & Delivery**: Secure payment gateway integration and delivery tracking.
- **Admin Panel**: Manage products, orders, user feedback, and customer profiles.

# Installation

### Prerequisites

- **Python 3.x**
- **Django Framework**
- **SQLite Database** (or another compatible RDBMS)
- **IDE** (PyCharm or VS Code recommended)

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/GreenTechEnergy.git
   cd GreenTechEnergy
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**:
   - Run migrations to set up the database schema.
   ```bash
   python manage.py migrate
   ```

4. **Create a Superuser** for admin access:
   ```bash
   python manage.py createsuperuser
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   - Open your browser and go to `http://localhost:8000`.

## Usage

### Admin

- **Product Management**: Add, update, and delete products.
- **Order Management**: Update order statuses and view order histories.
- **Customer Management**: Manage customer profiles and view customer feedback.

### Customer

- **Product Browsing**: Explore and view solar products and specifications.
- **Order Placement**: Add items to cart, proceed with checkout, and make payments.
- **Order Tracking**: Track order status, view payment history, and manage delivery details.

## System Architecture

The system includes key components:
- **Product Module**: Manages product details, availability, and pricing.
- **Cart Module**: Supports cart operations, including adding and removing items.
- **Order Module**: Handles order creation, status tracking, and transaction history.
- **Payment & Delivery Module**: Manages payment status, delivery updates, and transaction records.

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python, Django
- **Database**: SQLite
- **Hosting**: Compatible with AWS, DigitalOcean, Heroku, etc.

## Future Enhancements

- **Mobile App**: A companion app for mobile order tracking and management.
- **API Integrations**: Real-time weather data and market prices for an enhanced user experience.
- **Community Engagement**: A forum and sustainability challenge to promote renewable energy.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
