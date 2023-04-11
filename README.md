# Interactive Text-based RPG with GPT-3.5 Turbo

This is a simple interactive text-based role-playing game (RPG) using the GPT-3.5 Turbo model from OpenAI. The game allows users to input their actions, and the AI responds accordingly, providing a dynamic and engaging experience.

## Getting Started

To run the game, you'll need Python, the OpenAI API key, and the `openai` Python package. Install the `openai` package using `pip install openai`. Make sure to place your API key in the `.config/openai.token` file or set the `OPENAI_API_KEY` environment variable.

## How to Play

1. Run the `main.py` script.
2. Follow the prompts to input the game genre and theme.
3. Choose a character name from the list provided.
4. Start the game by inputting your actions or decisions.
5. Type 'quit' to exit the game.

Be warned though, this program appears to easily consume lot of tokens. I used 2$ while testing it.

## Features

- Dynamic story generation based on the user's input and chosen genre/theme.
- AI-generated character names.
- Player actions have a direct impact on the story progression.
- Uses OpenAI's GPT-3.5 Turbo model for advanced text generation.
- Interactive gameplay through a text-based interface.

This project was developed with the help of GPT-4, the latest AI language model from OpenAI.

## Known limitations

While the game is designed to provide an engaging and dynamic experience, it's
important to note that the AI, GPT-3.5 Turbo, has some limitations that might
affect gameplay:

1. The AI might sometimes generate responses that are repetitive or don't make logical sense.
2. The AI might not always remember the game state, which could result in inconsistencies.
3. The AI could sometimes ignore the user's input or not provide the expected choices.
4. The AI might not always integrate the user's input into the story as instructed.
5. The AI might sometimes produce inaccurate or anachronistic information, which could affect the game's immersion, especially in specific genres or settings. While the game is a work of fiction, please be aware that some generated content might not be entirely accurate or consistent.
6. The AI may insert multiple storytelling elements it doesn't use later in the story.
7. You may be able to influence story too much with your input. AI is generally non-critical of the input it gets.

There are good reasons why it's recommended to have a human in the loop when using GPT.
This project is completely automated though.

Please keep these limitations in mind while playing the game. The AI's performance might improve as updates are made to the underlying language model.

## Gameplay demonstration

    Enter the genre: Western
    Enter the theme: Mecha warriors
    Main Quest:

    The player character is a Mecha Warrior, a warrior enhanced with mechanical enhancements to give them special abilities and powers. The character is tasked with protecting their home, a small frontier town, from an impending invasion of hostile mecha forces. 

    Act 1:

    The player character is first introduced to their hometown and the people they will be protecting. They meet with the local sheriff and other townspeople, learning about the town and the people who live there. 

    Act 2: 

    The player character receives a warning from the sheriff about the impending mecha invasion. They are also told that the local silver mine, which is vital to the town's economy, is in danger of being taken over by the invaders. The player must then venture into the mine to find the source of the threat and prevent the takeover. 

    Act 3: 

    The player character discovers that the mecha forces have been sent by a mysterious entity known as the Iron Emperor, who wants to take the silver mine for himself. The player then has to find a way to stop the invasion, and ultimately defeat the Iron Emperor. 

    Side Quests:

    -The player character must help the people of the town by taking on various tasks - such as helping to build defences, gathering resources, and finding missing people. 

    -The player has the option of searching for new technology to upgrade their mechanical parts, which can give them access to new abilities and powers. 

    -The player can also explore various dungeons and caves, which will reveal more about the Iron Emperor's plans and the source of his power. 

    -The player may also have to rescue hostages taken by the mecha forces, and free prisoners held by the Iron Emperor. 

    Major Plot Points:

    -The player defeats the Iron Emperor and his mecha forces, saving the town from destruction. 

    -The player discovers the true identity of the Iron Emperor and learns why he was trying to take the silver mine. 

    -The player upgrades their mecha warrior, giving them an edge in battle and granting them access to new powers. 

    -The player saves the hostages, rescues the prisoners, and returns the silver mine to its rightful owners. 

    -The town celebrates the victory over the Iron Emperor, and the player is hailed as a hero.
    Generated character names: ['Charlie', 'John', 'Max', 'Liam ', 'Beth ']
    Please choose a character name from the following list:
    1. Charlie
    2. John
    3. Max
    4. Liam 
    5. Beth 
    Enter the number corresponding to your chosen name: 1
    Your chosen character name is: Charlie
    Welcome to the RPG prototype!
    Please enter your actions or type 'quit' to exit the game.
    You are Charlie, a Mecha Warrior tasked with protecting your hometown from an impending invasion of hostile mecha forces. You stand at the edge of town, surveying the horizon for any sign of the enemy. The town is quiet, except for the hum of machines and the occasional grunt of a worker hauling a load of silver ore.

    You can:

    1. Head to the sheriff's office to gather more information about the mecha invasion and what needs to be done to prepare for it.
    2. Visit the local blacksmith to upgrade your mechanical enhancements, giving you an edge in battle.
    3. Explore the outskirts of town to map the area and discover any potential enemy bases.
    >>> 1   
    You make your way to the sheriff's office in the center of town, a building constructed of sturdy logs reinforced with metal strips. You enter the office and find the sheriff poring over a map spread out on his desk. He looks up as you enter, and nods.

    "Charlie, good to see you. I've been expecting you," he says, marking a spot on the map with a red pen. "As you know, the mecha invasion is imminent. We've seen scout units in the area, and they're getting closer every day. We need to prepare ourselves, and fast."

    He hands you a list of tasks that need to be completed before the mecha forces arrive. "We need to fortify our defenses," he says. "We've got a good start, but we need more hands. See if you can gather some folks to help us reinforce the walls and build some more guard towers. We'll also need extra supplies of ammo and food, so if you can head out to the mines and get some more ore, that would be a great help."

    You nod, studying the map. "I see there's a cave system near the mine. Do you think the mecha forces will use that as a route of attack?"

    "I wouldn't be surprised," the sheriff replies. "It's a tricky place to navigate, but it could be a major advantage to them if they can get through it. We need you to explore that area and see what you can find."

    You take the list and map, and head outside. You know you have a lot of work to do, and not much time to do it. But you're determined to protect your home, no matter what it takes.

    You can:

    1. Gather some folks to help build defenses and gather supplies.
    2. Head to the mines to get more ore.
    3. Explore the cave system near the mine to see what you can find.
    {
      "completion_tokens": 391,
      "prompt_tokens": 699,
      "total_tokens": 1090
    }
    >>> quit
    Thanks for playing! Goodbye.

## Code Overview

`main.py` contains the primary logic for the game, including:

- `load_api_key()`: Loads the OpenAI API key from the file or environment variable.
- `generate_ai_response()`: Generates AI responses using the OpenAI API.
- `generate_story_outline()`: Generates a story outline based on the provided genre and theme.
- `generate_character_names()`: Generates a list of character names based on the story outline.
- `sanitize_input()`: Sanitizes the user's input by removing problematic characters.
- `sanitize_output()`: Sanitizes the AI's output by removing problematic characters.
- `main()`: The main function that runs the game.

Enjoy the game!

