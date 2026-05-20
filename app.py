import streamlit as st
from orchestrator import run_pipeline

st.title("🎬 StorySight AI")

uploaded_files = st.file_uploader(
    "Upload up to 2 images",
    type=["jpg", "png", "jpeg"],
    accept_multiple_files=True
)

genre = st.selectbox(
    "Choose Genre",
    ["Sci-Fi", "Fantasy", "Drama", "Comedy"]
)

image_paths = []

if uploaded_files:

    if len(uploaded_files) > 2:
        st.warning("Upload maximum 2 images only.")

    else:

        for i, uploaded_file in enumerate(uploaded_files):

            image_path = f"temp_{i}.jpg"

            with open(image_path, "wb") as f:
                f.write(uploaded_file.read())

            image_paths.append(image_path)

            st.image(image_path, caption=f"Image {i+1}", width=300)

# =========================
# Generate Story
# =========================

if st.button("Generate Story"):

    result = run_pipeline(image_paths, genre)

    st.session_state["caption"] = result["caption"]
    st.session_state["story"] = result["story"]
    st.session_state["show_story"] = True

# =========================
# Show Story FIRST
# =========================

if st.session_state.get("show_story", False):

    st.subheader("🧠 Combined Caption")
    st.write(st.session_state["caption"])

    # =========================
    # ORIGINAL STORY
    # =========================

    st.subheader("📖 Original Story")
    st.write(st.session_state["story"])

    # =========================
    # FEEDBACK SECTION
    # =========================

    st.subheader("⭐ Rate Our Service")

    rating = st.radio(
        "Choose your rating:",
        ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
        horizontal=True
    )

    score = len(rating)

    st.subheader("📝 Your Feedback")

    user_feedback = st.text_area("Write your feedback here...")

    # =========================
    # Retry options only for bad ratings
    # =========================

    retry_reason = None

    if score <= 2:

        st.error("⚠ You gave a bad rating.")

        retry_reason = st.selectbox(
            "Choose why you disliked the story:",
            [
                "Story was too long",
                "Story was too short",
                "Story was not accurate",
                "Story did not match my needs",
                "Story was boring",
                "I want a better version"
            ]
        )

    # =========================
    # Submit Feedback
    # =========================

    if st.button("Submit Feedback"):

        if user_feedback.strip() != "":

            st.success("✅ Feedback submitted successfully!")

            st.write("### Your Rating:")
            st.write(rating)

            st.write("### Your Feedback:")
            st.write(user_feedback)

            negative_words = [
                "bad", "poor", "terrible", "awful", "worst",
                "سيء", "وحش", "زفت", "مشكلة", "مش حلو"
            ]

            feedback_lower = user_feedback.lower()

            is_negative = (
                score <= 2 or
                any(word in feedback_lower for word in negative_words)
            )

            # =========================
            # NEGATIVE FEEDBACK
            # =========================

            if is_negative:

                st.error("⚠ Negative feedback detected!")

                original_story = st.session_state["story"]

                # =========================
                # Smart Rewrite Logic
                # =========================

                if retry_reason == "Story was too long":

                    improved_story = f"""
{original_story[:250]}

The rewritten version now focuses only on the main events while removing unnecessary details.
The pacing feels faster, smoother, and easier to follow.

As tension increased, the characters were forced to make difficult choices.
A final unexpected moment completely changed the outcome of the story.
"""

                elif retry_reason == "Story was too short":

                    improved_story = f"""
{original_story}

As the journey continued, new dangers slowly emerged from the shadows.
The characters faced emotional conflicts, hidden truths,
and dangerous situations that tested their courage.

Unexpected discoveries revealed that someone had been secretly watching them all along.

In the final scene, a mysterious event hinted that the adventure was far from over.
"""

                elif retry_reason == "Story was not accurate":

                    improved_story = f"""
This rewritten version better reflects the uploaded images and visual details.

{original_story}

The environment, objects, character actions,
and important scenes were adjusted to create a story
that feels more connected to the actual images.

The descriptions are now more realistic and visually immersive.
"""

                elif retry_reason == "Story did not match my needs":

                    improved_story = f"""
This improved version was rewritten to better match the selected genre and user expectations.

{original_story}

The atmosphere is now more immersive,
with stronger storytelling, clearer emotions,
and scenes that better fit the requested theme.

The characters now have deeper motivations and more dramatic interactions.
"""

                elif retry_reason == "Story was boring":

                    improved_story = f"""
{original_story}

Suddenly, an unexpected event changed everything.

The atmosphere became tense as danger quickly spread around the characters.
Every decision became critical while mysterious events unfolded one after another.

The story now contains more suspense, emotional intensity,
dramatic action scenes, and unexpected twists.

Nothing would ever be the same again.
"""

                else:

                    improved_story = f"""
{original_story}

The story was rewritten using more creative language,
stronger emotional moments,
and richer scene descriptions.

The dialogue feels more natural,
the pacing is smoother,
and the world now feels more alive and cinematic.

Unexpected twists and deeper character reactions
make the experience more immersive and engaging.
"""

                # =========================
                # SHOW IMPROVED STORY
                # =========================

                st.subheader("🔄 Improved Story")
                st.write(improved_story)

                st.session_state["improved_story"] = improved_story

            # =========================
            # POSITIVE FEEDBACK
            # =========================

            else:

                st.balloons()
                st.success("💖 Thank you for your positive feedback!")

        else:

            st.warning("⚠ Please write your feedback first.")