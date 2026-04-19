# Step 1: Define the Custom Exception Class
class InvalidTicketIDError(Exception):
    """Exception raised for errors in the input Ticket ID."""
    
    def __init__(self, ticket_id, message="Ticket ID must be a 6-digit numeric value"):
        self.ticket_id = ticket_id
        self.message = message
        super().__init__(self.message)

# Step 2: Function that uses the Custom Exception
def process_ticket(ticket_id):
    # Check if the ID is numeric and exactly 6 digits
    if not str(ticket_id).isdigit() or len(str(ticket_id)) != 6:
        raise InvalidTicketIDError(ticket_id)
    
    print(f"Ticket #{ticket_id} is being processed successfully.")

# Step 3: Demonstrate Exception Handling
ticket_samples = [129425, "99A123", 456, 131394]

print("--- Ticket Validation System ---")

for t_id in ticket_samples:
    try:
        process_ticket(t_id)
    except InvalidTicketIDError as e:
        print(f"Error: {e.message} (Received: {e.ticket_id})")
    finally:
        print("Verification check complete.")
        print("-" * 30)