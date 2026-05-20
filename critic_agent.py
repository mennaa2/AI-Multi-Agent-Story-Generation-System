from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

explainer = pipeline("text2text-generation", model="google/flan-t5-base")

def evaluate_story(story):

    labels = ["good story", "bad grammar", "low emotion", "coherent", "incoherent"]

    classification_result = classifier(story, labels)

    top_label = classification_result["labels"][0]
    confidence = classification_result["scores"][0]

    score = round(confidence * 10, 1)

    prompt = f"""
Give short critique (2-3 lines only).

Story:
{story}
"""

    explanation = explainer(
        prompt,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.7,
        repetition_penalty=1.2
    )[0]["generated_text"]

    return top_label, score, explanation


if __name__ == "__main__":
    test_story = "A robot with a computer on his head discovers emotions in a futuristic city."

    label, score, feedback = evaluate_story(test_story)

    print("ZERO-SHOT RESULT")
    print("Label:",label)
    print("Score:", score)
    print("FEEDBACK", feedback)
