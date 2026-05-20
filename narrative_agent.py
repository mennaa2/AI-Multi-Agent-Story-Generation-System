from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

def generate_story(caption, genre):

    prompt = f"""
You are a professional creative writer.

Write a COMPLETE {genre} story between 180 and 220 words.

Rules:
- Do NOT stop early
- Must include: beginning, conflict, ending
- Make it emotional and engaging
- No repetition

Caption:
{caption}

Story:
"""

    result = generator(
    prompt,
    max_new_tokens=300,
    do_sample=True,
    temperature=0.9,
    top_p=0.95,
    repetition_penalty=1.2
)

    return result[0]["generated_text"]


def improve_story(caption, genre, feedback):

    prompt = f"""
You are a professional story editor.

Improve the story below.

Caption: {caption}
Genre: {genre}
Feedback: {feedback}

Rewrite a better emotional story (180-220 words).
Make it more engaging and structured.

Story:
"""

    result = generator(
        prompt,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.8
    )

    return result[0]["generated_text"]