import random

# Take user input for word types
noun = input("Enter a noun (e.g., pizza, dog, John): ")
verb = input("Enter a verb (e.g., run, jump, sleep): ")
adjective = input("Enter an adjective (e.g., blue, smelly, pretty): ")
adverb = input("Enter an adverb (e.g., quickly, loudly): ")

# List of story templates using f-strings
stories = [
    f"Our teacher wore a {adjective} {noun} and started to {verb} {adverb} in front of the class.",
    f"An alien with a {adjective} {noun} appeared and began to {verb} {adverb} down the frozen food aisle.",
    f"At night, my dog becomes a {adjective} {noun} and likes to {verb} {adverb} around the neighborhood.",
    f"We packed our {adjective} {noun} and went to the beach, only to find a crab {verb}ing {adverb} on our towels!",
    f"My friend gave me a {adjective} {noun}, and then we started to {verb} {adverb} with the balloons."
]

# Pick and print one random story
print("\n📖 Your Random Story:")
print(random.choice(stories))
