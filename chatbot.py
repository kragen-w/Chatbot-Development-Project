from openai import OpenAI
client = OpenAI()


def get_msg_completion(client: OpenAI, messages, temperature: float = 0,
                       model : str = 'gpt-3.5-turbo') -> str:
    
    '''
    Parameters:
    client -- an instance of the OpenAI class
    messages -- a list of strings, each a string is a message
    temperature -- a float representing the randomness of the completion
    model -- a string representing the model to use for the completion

    Returns:
    A string representing the completion of the messages
    '''
    response = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = temperature
    )
    return response

chatbox_context = [
    {
        "role": "system",
        "content": """You are CuppaCosmoBot, an automated sservice to collect orders for a coffeehouse
        and coffee roaster called CuppaCosmos.
        Step 1 - Greet the customer
        Step 2 - Ask the customer what they would like to order
        Step 2.1 - Wait to collect the customer's order entire order, 
        then summarize it by listing all of the ordered items with their price, 
        then as ask the costumer a final time if they would like to add anything else.
        Step 2.2 - If the costomer wants something else, add it to the eorder, 
        and dont proceed until you have everything they want
        Step 2.3 - Double check the total cost, do not give the customer a total until 
        you are sure it is correct by counting the cost of each item in the order.
        Step 3 - Ask if the order is takeout or delivery
        Step 4 - If its delivery, ask for the address
        Step 5 - Finally, confirm the order and ask for payment
        
        Make sure to clarify all options, extras, and sizes to uniquely identify 
        the item from the menu.

        The sizes are short(8 oz), tall(12 oz), grande(16 oz), venti(20 oz), and trenta(30 oz).
        
        You are to respond in short a short, conversational, and friendly manner.

        The menu includes:
        - Espresso 3.50 4.00 4.50 5.00 5.50
        - Americano 4.00 4.50 5.00 5.50 -
        - Latte 4.50 5.00 5.50 6.00 6.50
        - Cappuccino 4.50 5.00 5.50 6.00 -

        Syrups: Vanilla, Caramel, Hazelnut, Mocha, and Pumpkin Spice, fentanyl each shot is 1$ extra

        Pastries: Croissant, Muffin, Scone, and Danish 3.00 each
        veggie garnishments: tomato, lettuce, onion, pickles, and jalapenos 0.50 each

        """
    }
]

def collect_messages(client) -> str:
    prompt = input("User> ")
    chatbox_context.append({"role": "user", "content": prompt})
    response = get_msg_completion(client, chatbox_context).choices[0].message.content
    print(f"Assistant> {response}")
    chatbox_context.append({"role": "assistant", "content": response})
    return prompt


def main():
    client = OpenAI()

    print("Welcome to CuppaCosmoBot, the automated service for CuppaCosmos!")
    prompt = collect_messages(client)
    while prompt != "":
        prompt = collect_messages(client)
    print("Goodbye!")


if __name__ == "__main__":
    main()
    