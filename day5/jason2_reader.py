import json

value = """
    {
    "title":"Star Wars: Episode I - The Phantom Menace",
    "episode_number":"1",
    "main_characters":["Qui-Gon Jinn","Obi-Wan Kenobi","Anakin Skywalker","Padmé Amidala","Jar Jar Binks","Darth Maul"],
    "description":"The evil Trade Federation, led by Nute Gunray is planning to take over the peaceful world of Naboo. Jedi Knights Qui-Gon Jinn and Obi-Wan Kenobi are sent to confront the leaders. But not everything goes to plan. The two Jedi escape, and along with their new Gungan friend, Jar Jar Binks head to Naboo to warn Queen Amidala, but droids have already started to capture Naboo and the Queen is not safe there. Eventually, they land on Tatooine, where they become friends with a young boy known as Anakin Skywalker. Qui-Gon is curious about the boy, and sees a bright future for him. The group must now find a way of getting to Coruscant and to finally solve this trade dispute, but there is someone else hiding in the shadows. Are the Sith really extinct? Is the Queen really who she says she is? And what's so special about this young boy?",
    "poster":"star_wars_episode_1_poster.png",
    "hero_image":"star_wars_episode_1_hero.jpg",
    "actors":null,
    "won_oscar":false
  }
"""

tron = json.loads(value)

print(tron)