# Django Realtime Chat

A backend-focused Django project designed to demonstrate clean architecture,
custom authentication, and real-time communication using Django Channels.

This project is being developed incrementally with clear commits to reflect
real-world engineering workflow.

## Current Features

- Custom user authentication system (mobile number based)
- Shared `BaseModel` for consistent timestamps and UUIDs
- Modular app structure following best practices
- Environment-based configuration (`.env`)
- Git-friendly, production-ready setup

## Planned Features

- Real-time one-to-one and group chat using WebSockets
- Message persistence and read status
- Token-based authentication for WebSocket connections
- REST APIs for chat room and message management

## Tech Stack

- Django
- Django REST Framework
- Django Channels
- Redis (for channel layer – planned)
- PostgreSQL / MySQL (configurable)

## Folder Structure

- config/          # Django project settings
- core/            # Shared BaseModel, utils
- accounts/        # Custom user system
- chat/            # Chat feature app

## Status

🚧 **Active development**  
This repository reflects daily progress and real engineering decisions rather
than a one-shot tutorial project.