# Sifra AI Authentication Backend

Built using Azure Functions (Python) for:
- Signup
- Login (JWT-based)
- Forgot Password (SendGrid)
- Password Reset

## Environment Variables (set via Azure portal):
- MONGO_URI
- DB_NAME
- JWT_SECRET
- SENDGRID_API_KEY
- SENDGRID_FROM_EMAIL

## Deploy:
1. Deploy using Azure Functions Core Tools or via Azure Portal.
2. Add environment variables in Application Settings.

## Flutter Frontend
Integrate REST APIs:
- `/api/auth/signup`
- `/api/auth/login`
- `/api/auth/forgot`
- `/api/auth/reset`
