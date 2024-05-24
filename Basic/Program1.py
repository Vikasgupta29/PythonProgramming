"""
The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows: 
Rate per Adult: Rs. 37550.0 
Rate per Child: 1/3rd of the rate per adult 
Service Tax: 7% of the ticket amount (including all passengers) 
As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax).
Find and display the total ticket cost for a group which had adults and children.
"""

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    total_ticket_cost=no_of_adults*37550
    total_ticket_cost+=no_of_children*(37550/3)
    total_ticket_cost+=total_ticket_cost*0.07
    total_ticket_cost-=total_ticket_cost*0.1
    return total_ticket_cost

# Provide different values for no_of_adults, no_of_children and test your program.
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)
