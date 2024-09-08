import streamlit as st
import random
import hangman_art
import hangman_words 

st.title("HANGMAN GAME")

st.sidebar.title("Instructions:")
st.sidebar.info("1. Please select a difficulty level before you begin the game. The default difficulty level is 'Easy'")
st.sidebar.info("2. Before you enter a new letter make sure you have removed your previous responce.")
st.sidebar.info("3. When you enter a correct letter, click 'Backspace' and then 'Enter' so your progress is dispalyed on the screen.")

difficulty_levels = {
    "Easy": hangman_words.word_list1,
    "Medium": hangman_words.word_list2,
    "Hard": hangman_words.word_list3
}

difficulty = st.selectbox("Choose the Difficulty level", list(difficulty_levels.keys()))

def game_initialization():
  st.session_state.chosen_word = random.choice(difficulty_levels[difficulty])
  st.session_state.word_meaning = hangman_words.word_meaning[st.session_state.chosen_word]
  st.session_state.word_length = len(st.session_state.chosen_word)
  st.session_state.display = ["_"] * st.session_state.word_length
  st.session_state.lives = 6
  st.session_state.guessed = set()
  st.session_state.game_status = False


if 'chosen_word' not in st.session_state:
  game_initialization()


st.subheader('Current Word')
st.write(' '.join(st.session_state.display))
user_guess = st.text_input('Guess a letter').lower()

if user_guess in st.session_state.guessed:
    st.write("You have already guessed the letter")
elif user_guess not in st.session_state.guessed and st.session_state.game_status == False:
    st.session_state.guessed.add(user_guess)
    if user_guess in st.session_state.chosen_word:
        for position in range(st.session_state.word_length):
            letter = st.session_state.chosen_word[position]
            if letter == user_guess:
                st.session_state.display[position] = letter
                st.balloons()
                st.success("You have entered the right word")
    else:
        st.session_state.lives -= 1
        st.write(f"You have {st.session_state.lives} lives left")

    if "_" not in st.session_state.display:
        st.session_state.game_status = True
        st.success(f"You Won! The word was: {st.session_state.chosen_word}")
        st.success(f"It means {st.session_state.word_meaning}")
        st.balloons()

    if st.session_state.lives == 0:
        st.session_state.game_status = True
        st.error(f"You Lose! The word was: {st.session_state.chosen_word}")
        st.error(f"It means {st.session_state.word_meaning}")

st.markdown(f"```{hangman_art.stages[st.session_state.lives]}```")

if st.session_state.game_status:
    if st.button('Play Again'):
        game_initialization()
