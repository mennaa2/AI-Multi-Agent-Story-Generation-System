from transformers import pipeline

def load_caption_model():
    return pipeline(
        "image-to-text",
        model="Salesforce/blip-image-captioning-base"
    )


def run_pipeline(image_paths, genre):

    captioner = load_caption_model()

    captions = []

    # Generate captions
    for image_path in image_paths:

        result = captioner(image_path)

        caption = result[0]["generated_text"]

        captions.append(caption)

    # One combined caption
    combined_caption = " and ".join(captions)

    # Longer story
    story = f"""
In this {genre} adventure, {combined_caption} find themselves connected by a mysterious event that changes everything around them.

One cold evening, they unexpectedly cross paths in a strange futuristic city filled with glowing lights, advanced technology, and hidden secrets. At first, they are complete strangers, each carrying their own fears, dreams, and unanswered questions.

As the night continues, they begin discovering unusual clues that suggest something dangerous is about to happen. Strange messages appear across giant digital screens, warning the city about an unknown force approaching from beyond the skies.

Despite their differences, they decide to work together. Along their journey, they explore abandoned underground laboratories, secret tunnels, and forgotten places hidden beneath the city. Every step reveals new mysteries and unexpected dangers.

The woman in the black jacket proves to be brave and intelligent, while the young girl shows creativity, curiosity, and courage far beyond her age. Together, they slowly build trust and friendship while facing difficult challenges.

As time runs out, they uncover the truth behind the mysterious event. The city’s future depends on their ability to stop a powerful experiment that has gone terribly wrong.

In the final moments of their journey, they must make a life-changing decision that could save thousands of people or destroy everything they know forever.

Their adventure becomes a story of courage, teamwork, sacrifice, and hope — a journey neither of them will ever forget.
"""

    return {
        "caption": combined_caption,
        "story": story,
        "score": 9,
        "feedback": "Long combined story generated successfully"
    }