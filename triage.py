import os
import anthropic

client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))

def triage_ticket(ticket_text):
    prompt = f'''You are an IT support triage system.
Analyze this support ticket and respond ONLY in this exact format:
CATEGORY: [Hardware/Software/Network/Account/Other]
PRIORITY: [Critical/High/Medium/Low]
REASON: [One sentence]
SUGGESTED_RESPONSE: [Professional reply to user]

Ticket: {ticket_text}'''

    message = client.messages.create(
        model='claude-sonnet-5',
        max_tokens=500,
        messages=[{'role': 'user', 'content': prompt}]
    )
    for block in message.content:
        if block.type == 'text':
            return block.text
    return '(no text response)'

phase5_tickets = [
    'Server is down, entire office cannot work. All systems offline.',
    'My account is locked, I cannot log in and I have a deadline.',
    'Cannot connect to company VPN from home.',
    'New employee Marie Ngassa starts Monday — needs account, email, and Sales access.',
    'I need access to the Sales shared folder for a project.',
    'Microsoft Word keeps freezing when saving documents.',
    'Employee in Operations left the company Friday — account needs to be secured.',
    'My email inbox is full, cannot receive new messages.',
    'Please update my display name in the company directory.',
    'The office printer is making a grinding noise.',
]

for i, ticket in enumerate(phase5_tickets, start=1):
    print(f'TICKET {i}: {ticket}')
    print(triage_ticket(ticket))
    print('-' * 50)
