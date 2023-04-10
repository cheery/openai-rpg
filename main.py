import os
import openai
import re

def load_api_key():
    api_key_path = os.path.join(os.path.expanduser("~"), ".config", "openai.token")
    if os.path.exists(api_key_path):
        with open(api_key_path, "r") as f:
            api_key = f.read().strip()
            return api_key
    else:
        raise FileNotFoundError(f"API key not found at {api_key_path}. Please create the file with your API key or set the OPENAI_API_KEY environment variable.")

if "OPENAI_API_KEY" in os.environ:
    openai.api_key = os.environ["OPENAI_API_KEY"]
else:
    openai.api_key = load_api_key()

def generate_ai_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response

def generate_story_outline(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.8,
    )

    return response.choices[0].text.strip()

def generate_character_names(story_outline, num_names=5):
    prompt = (
        f"Based on the following story outline, generate a list of names suitable for the setting. Player will be named from that list of names:\n"
        f"{story_outline}\n"
        f"Player names:"
    )

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.8,
    )

    names = response.choices[0].text.strip().split("\n")
    return list(map(sanitize_output, names[:num_names]))

def sanitize_input(text):
    # Remove any potentially problematic characters or sequences
    sanitized_text = re.sub(r"[^a-zA-Z0-9\s,.'-]+", "", text)
    return sanitized_text

def sanitize_output(text):
    # Remove any potentially problematic characters or sequences
    sanitized_text = re.sub(r"^[0-9]+\.\s*", "", text)           # Remove list item numbers.
    sanitized_text = re.sub(r"^-\s*", "", sanitized_text)           # Remove list item markers.
    sanitized_text = re.sub(r"^[0-9]+\)\s*", "", sanitized_text) # Remove list item numbers.
    #sanitized_text = re.sub(r"[^a-zA-Z0-9\s,.'-]+", "", sanitized_text)
    return sanitized_text

def main():
    genre = input("Enter the genre: ")
    game_desc = input("Enter the theme: ")
    genre = sanitize_input(genre)
    short_description = sanitize_input(game_desc)

    prompt = (
        f"Create a short story outline for a {genre} role-playing game, including main quest, side quests, and major plot points."
    )
    if short_description != "":
        prompt += f" The story should be based on the following theme: '{short_description}'"
    story_outline = generate_story_outline(prompt)
    print(story_outline)

    character_names = generate_character_names(story_outline)
    print("Generated character names:", character_names)

    print("Please choose a character name from the following list:")
    for idx, name in enumerate(character_names):
        print(f"{idx + 1}. {name}")

    user_choice = int(input("Enter the number corresponding to your chosen name: ")) - 1
    chosen_name = character_names[user_choice]
    print(f"Your chosen character name is: {chosen_name}")

    print("Welcome to the RPG prototype!")
    print("Please enter your actions or type 'quit' to exit the game.")

    # Initialize the game state
    messages=[
        {"role": "system", "content": (
            f"You are a game master.\n"
            f"Player name: {chosen_name}\n"
            f"Game type: Instant messaging roleplay\n"
            f"Integrate the player's input into the story without repeating it or any previous events, and present the consequences of their action or decision. Remember to call the player by their name.\n"
            f"Here's the story outline you follow:\n{story_outline}"
            )},
        {"role": "user", "content": (
            f"Begin the role-playing game. Start with an introduction or setting the scene."
            f" Finally present 2-3 choices.")}
    ]

    # Generate AI response
    response = generate_ai_response(messages)
    print(response.choices[0].message.content)
    messages.append(response.choices[0].message)

    while True:
        # Get player input
        player_input = input(">>> ")

        if player_input.lower() == "quit":
            print("Thanks for playing! Goodbye.")
            break
        if not player_input.strip():
            print("Please provide a valid input.")
            continue

        # Generate AI response
        messages.append({"role": "user", "content": player_input})
        response = generate_ai_response(messages)

        # Update the game state based on the AI response
        print(response.choices[0].message.content)
        print(response.usage)
        messages.append(response.choices[0].message)

if __name__ == "__main__":
    main()

