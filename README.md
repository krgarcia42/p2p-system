# P2P Event System
- Asynchronous: Uses `threading`.
- **Nodes**: 4 units acting as Transmitters (Servers) and Receivers (Clients).
- **Events**: Handles OrderCreated, PaymentProcessed, EmailSent, and OrderCancelled.
- **Coupling**: Handles spatial/temporal coupling via local port management and error handling.
- **No Cloud**: Runs in a local virtual environment via GitHub Actions.
