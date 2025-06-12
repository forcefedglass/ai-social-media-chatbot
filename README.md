# AI-Powered Social Media Chatbot

This project implements an AI-powered chatbot using N8N that monitors WhatsApp, Snapchat, and Instagram. It leverages advanced AI to enhance fan engagement, drive sales, and personalize interactions.

## Features

- 24/7 Automated, Personalized Chat
- Impeccable Memory and Context Awareness
- Custom Requests and Interactions
- Drip-Method Sales Funnels
- Automated Content Promotion and Delivery
- Revenue Optimization Tools
- Fan Segmentation and Scoring
- Dynamic Pricing
- Automated Tip Collection
- Re-engagement Campaigns
- Multi-language Support
- Analytics and Insights

## Prerequisites

- Docker and Docker Compose
- WhatsApp Business API access
- Instagram Graph API access
- Snapchat Marketing API access
- OpenAI API key

## Setup Instructions

1. Clone this repository
2. Copy `.env.example` to `.env` and fill in your API credentials
3. Start the N8N instance:
   ```bash
   docker-compose up -d
   ```
4. Access N8N at http://localhost:8000
5. Import the workflow files from the `workflows` directory

## Workflow Structure

### 1. WhatsApp Integration
- Monitors incoming WhatsApp messages
- Processes messages using OpenAI
- Maintains conversation context
- Handles automated responses and sales funnels

### 2. Instagram Integration
- Monitors Instagram DMs and comments
- Processes interactions with AI
- Manages content delivery and promotions
- Handles automated engagement

### 3. Snapchat Integration
- Monitors Snapchat interactions
- Processes snaps and messages
- Manages content distribution
- Handles automated responses

### 4. AI Processing
- OpenAI integration for natural language processing
- Context awareness and memory management
- Personality matching and response generation
- Content recommendation system

### 5. Revenue Optimization
- Fan segmentation and scoring
- Dynamic pricing system
- Automated tip collection
- Re-engagement campaigns

## Configuration Details

### WhatsApp Setup
1. Configure WhatsApp Business API credentials in .env
2. Import whatsapp-bot.json workflow
3. Configure webhook endpoints
4. Test message handling

### Instagram Setup
1. Configure Instagram Graph API credentials in .env
2. Import instagram-bot.json workflow
3. Set up Instagram webhooks
4. Test DM and comment handling

### Snapchat Setup
1. Configure Snapchat Marketing API credentials in .env
2. Import snapchat-bot.json workflow
3. Configure Snapchat webhooks
4. Test interaction handling

### AI Configuration
1. Set up OpenAI API key in .env
2. Configure AI parameters in workflows
3. Test response generation
4. Fine-tune personality matching

## Development

To modify the workflows:

1. Access the N8N editor at http://localhost:8000
2. Import the relevant workflow
3. Make your changes
4. Export and save the updated workflow

## Security Considerations

- All API keys and tokens are stored in .env
- Webhook endpoints are secured
- User data is encrypted
- Compliance with platform guidelines

## Monitoring and Analytics

- Real-time interaction monitoring
- Revenue tracking
- Engagement metrics
- Performance analytics

## License

This project is open-source and available under the MIT License.

## Support

For issues and feature requests, please create an issue in the repository.
