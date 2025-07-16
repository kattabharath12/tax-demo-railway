# Auto Tax Filing Demo - Railway Deployment

## Features
- FastAPI backend with production-ready structure
- User authentication with JWT
- File upload and OCR processing
- Tax calculation engine
- Payment processing integration
- Admin dashboard
- State-specific tax filing support

## Railway Deployment

1. Connect your GitHub repository to Railway
2. Set environment variables in Railway dashboard:
   - `SECRET_KEY`: Your JWT secret key
   - `STRIPE_SECRET_KEY`: Your Stripe secret key
   - `DATABASE_URL`: Automatically provided by Railway PostgreSQL

3. Deploy automatically triggers on push to main branch

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your values
   ```

3. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation
Once deployed, visit `/docs` for interactive API documentation.

## Health Check
The application includes a health check endpoint at `/health` for Railway monitoring.
