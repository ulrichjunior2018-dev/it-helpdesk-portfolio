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

test_tickets = [
    'My laptop screen went black and wont turn on',
    'My account is locked out after too many password attempts',
    'New hire starting Monday, needs an AD account and email',
    'I need access to the Sales shared folder',
    'The internet is really slow today in the office',
    'Excel keeps crashing when I open large files',
]

for ticket in test_tickets:
    print(f'TICKET: {ticket}')
    print(triage_ticket(ticket))
    print('-' * 50)
