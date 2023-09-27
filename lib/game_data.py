class GameData:
    def __init__(self):
        self.story_texts = {
            "intro": (
                "You find yourself amidst a vibrant party with your friends, the music pulsating through the air as laughter fills the room. "
                "You're faced with a choice:\n"
                "1. Join your friends for more shots and dive headfirst into the night's revelry.\n"
                "2. Opt for a more mellow approach, sipping on lemonade as you enjoy the company of your friends."
            ),
            "more_shots_outcome": (
                "You choose to have more shots with your friends, and the night spirals into a blur of fun and laughter. However, as the night progresses, "
                "so does the intoxication. You’ve gone too far and have to taxi home before midnight."
            ),
            "sip_lemonade_outcome": (
                "You sip on lemonade, savoring the refreshing taste as you engage in delightful conversations with your friends. "
                "At one point, you decide to step outside for a quick vape break."
            ),
        }
            
        self.story_segments = {
                 "intro": {
                      "choices": [
                    "1. Join your friends for more shots and dive headfirst into the night's revelry.",
                    "2. Opt for a more mellow approach, sipping on lemonade as you enjoy the company of your friends.",
                ],
                "outcomes": {
                    "1": "more_shots_outcome",
                    "2": "sip_lemonade_outcome",
                },
            },
            "more_shots_outcome": {
                "narrative_text": self.story_texts["more_shots_outcome"],
                "choices": [],
                "outcomes": {
                    "continue": "next_segment_id", 
                },
            },
            "sip_lemonade_outcome": {
                "narrative_text": self.story_texts["sip_lemonade_outcome"],
                "choices": [
                    "1. Continue the story.",
                ],
                "outcomes": {
                    "1": "next_segment_id", 
                },
            },
          
        }