Flask Productivity AIO

This is my first attempt at creating a full web application using Python and the Flask framework.

The goal of this project is to combine several of my previous desktop projects into one accessible web application that can be used across multiple devices on the same network.

Currently, the project combines:

A Finance Tracker
A Scheduler / Calendar
A Journal System
A Multi-User Login System

The project is designed as a learning experience for:

Flask web development

Backend logic

JSON data persistence

User authentication

Session handling

Local network hosting

Features

Finance Tracker

Create transactions and income entries

Edit existing transactions

Custom transaction dates

Automatic income/expense balance calculations

Category-based transaction organization

Separate save data for each user

Scheduler

Create scheduled events

Add dates and times to events

Event descriptions

User-specific schedules

Persistent JSON save system

Journal System

Create journal entries

Save dated notes

User-specific journals

Persistent save system

User Accounts

Login system

Account creation

Separate save files per user

Session-based authentication

  Current Technologies

Python

Flask

HTML (rendered through Flask templates)

JSON file storage

Jupyter Notebook (development/testing)

Save System

The application currently uses JSON files for storage.

Each user receives their own files automatically:

username_transactions.json

username_journal.json

username_schedule.json

User login credentials are stored in:

users.json

Network Access

The application can currently be hosted on:

localhost

local networks

virtual LAN networks (such as Hamachi or ZeroTier)

This allows other devices on the same network to access the application through a browser.

Example:

http://192.168.x.x:5000

Planned Features

Dark mode

Better UI styling

Search and filtering

Mobile-friendly layout

File export/import

Recurring scheduled events

Budget goals

Notifications/reminders

  Project Goals

This project is mainly focused on improving my understanding of:

Full-stack web development basics

Flask application structure

Persistent data storage

Multi-user systems

Web networking

Backend application logic

Running The Application

Install Flask:

pip install flask

Run the notebook/app and open:

http://127.0.0.1:5000

Or for LAN access:

http://YOUR-IP:5000
Status

This project is actively being expanded and refactored as I continue learning Flask and web development.
