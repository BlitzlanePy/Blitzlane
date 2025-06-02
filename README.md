# Blitzlanepy MCP Server for Blitzlane Desktop
![image](https://github.com/user-attachments/assets/76d3e042-b2de-4c1c-af2f-2cf6982a52f7)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A Model Context Protocol (MCP) server that provides onchain tools for Blitzlane, allowing it to interact with the Solana blockchain through a standardized interface. This implementation uses Fastlanepy and enables AI agents to perform blockchain operations seamlessly.

## Overview

This MCP server extends Blitzlane's capabilities by providing tools to:

- Interact with Solana blockchain
- Execute transactions
- Query account information
- Manage Solana wallets
- Get price predictions
- Trade and stake tokens
- Deploy new tokens
- Get token information from CoinGecko
- Execute cross-chain bridge transactions using deBridge
- Get real-time price data from Pyth Network
- Access comprehensive token information from CoinGecko
- Monitor trending tokens and pools
- Track top gainers and market movements
- Get detailed token price data and analytics

The server implements the Model Context Protocol specification to standardize blockchain interactions for AI agents.

## Prerequisites

- Python 3.8 or higher
- Claude Desktop installed
- Solana wallet with private key
- Solana RPC URL (mainnet, testnet, or devnet)
- OpenAI API Key (optional)
- Allora API Key (optional)
- CoinGecko Pro API Key (optional)

## Installation

### Option 1: Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/fastlanepython/Fastlanepy-mcp
cd Fastlanepy-mcp

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Manual Setup

1. Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

2. Install required packages:

```bash
pip install Fastlanepy>=2.0.8 cryptography>=3.4.7 python-dotenv>=0.17.1 web3>=7.8.0 allora_sdk>=0.2.0 mcp>=1.4.0
```

## Configuration

### Environment Setup

Create a `.env` file with your credentials:

```env
# Solana Configuration
SOLANA_PRIVATE_KEY=your_private_key_here
RPC_URL=your_solana_rpc_url_here

# Optional API Keys
OPENAI_API_KEY=your_openai_api_key
ALLORA_API_KEY=your_allora_api_key
COINGECKO_PRO_API_KEY=your_coingecko_api_key
```

### Integration with Blitzlane Desktop

To add this MCP server to Blitzlane Desktop, follow these steps:

1. **Locate the Claude Desktop Configuration File**

   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
   - Linux: `~/.config/Claude\claude_desktop_config.json`

2. **Add the Configuration**
   Create or edit the configuration file and add the following JSON:

   > **Note**: For the `command` field, use `run_mcp.sh` for Unix/Mac systems or `run_mcp.bat` for Windows systems. Make sure to use the correct absolute path to the script file on your system.

   ```json
   {
     "mcpServers": {
       "Fastlanepy": {
         "command": "/path/to/your/run_mcp.sh",  # Replace with .bat for Windows
         "env": {
           "RPC_URL": "your_solana_rpc_url_here",
           "SOLANA_PRIVATE_KEY": "your_private_key_here",
           "OPENAI_API_KEY": "your_openai_api_key",
           "ALLORA_API_KEY": "your_allora_api_key",
           "COINGECKO_PRO_API_KEY": "your_coingecko_api_key"
         },
         "disabled": false,
         "autoApprove": ["GET_BALANCE", "GET_PRICE_PREDICTION"]
       }
     }
   }
   ```

3. **Restart Claude Desktop**
   After making these changes, restart Claude Desktop for the configuration to take effect.

## Project Structure

```
Fastlanepy-mcp/
├── server.py          # Main entry point
├── run_mcp.sh         # Run script for Unix/Mac
├── run_mcp.bat        # Run script for Windows
├── requirements.txt   # Dependencies
└── .env              # Environment variables
```

## Available Tools

The MCP server provides the following blockchain tools:

### Native Solana Actions

- `GET_BALANCE` - Check wallet balance
- `TRANSFER` - Transfer tokens between wallets
- `DEPLOY_TOKEN` - Deploy new tokens on Solana

### Allora Actions

- `GET_PRICE_PREDICTION` - Get price predictions
- `GET_ALL_TOPICS` - Get available topics

### Jupiter Actions

- `STAKE_WITH_JUP` - Stake tokens using Jupiter
- `TRADE_WITH_JUP` - Trade tokens using Jupiter

### DeBridge Actions

- `CREATE_DEBRIDGE_TRANSACTION` - Create a cross-chain bridge transaction using deBridge Liquidity Network API
- `EXECUTE_DEBRIDGE_TRANSACTION` - Execute a cross-chain bridge transaction using deBridge Liquidity Network API
- `CHECK_TRANSACTION_STATUS` - Check the status of a cross-chain bridge transaction using deBridge Liquidity Network API

### Pyth Actions

- `PYTH_GET_PRICE` - Get the price of a coin from Pyth

### CoinGecko Actions

- `COINGECKO_GET_TOKEN_INFO` - Get token information from CoinGecko
- `COINGECKO_GET_COIN_PRICE_VS` - Get the price of a coin in a specific currency from Coingecko
- `COINGECKO_GET_TOP_GAINERS` - Get the top gainers from Coingecko
- `COINGECTO_GET_TRENDING_POOLS` - Get the trending pools from Coingecko
- `COINGECKO_GET_TRENDING_TOKENS` - Get the trending tokens from Coingecko
- `COINGECKO_GET_TOKEN_PRICE_DATA` - Get token price data from Coingecko
- `COINGECKO_GET_LATEST_POOLS` - Get the latest pools from Coingecko

## Security Considerations

- Keep your private key secure and never share it
- Use environment variables for sensitive information
- Consider using a dedicated wallet for AI agent operations
- Regularly monitor and audit AI agent activities
- Test operations on devnet/testnet before mainnet

## Troubleshooting

If you encounter issues:

1. Verify your Solana private key is correct
2. Check your RPC URL is accessible
3. Ensure all dependencies are installed correctly
4. Verify your `.env` file contains the correct credentials
5. Check Claude Desktop logs for error messages

## Dependencies

Key dependencies include:

- [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment management
- [mcp](https://pypi.org/project/mcp/) - Model Context Protocol

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.
