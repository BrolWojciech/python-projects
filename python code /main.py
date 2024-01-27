import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from spotify_module import get_top_tracks_info, spotify

def main():
    st.set_page_config(
    page_title="Spotify Brolu Cool App",
    page_icon="🧊",
    layout='centered',
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/BrolWojciech',

    }
)
    
    st.title('Spotify Top Tracks Dashboard')

    # Input użytkownika
    artist_name = st.text_input('Enter Artist Name: ')

    # Przycisk do uruchomienia
    if st.button('Generate Dashboard'):
        top_tracks_df = get_top_tracks_info(artist_name)

        # Wyświetlanie informacji
        st.markdown(f"## Top Tracks for {artist_name}")

        # Podział na kolumny
        col1, col2 = st.columns(2)

        # DataFrame po lewej stronie
        col1.table(top_tracks_df[['Song Name', 'Popularity','key']])

        # Obraz z pierwszego wiersza po prawej stronie
        first_image_url = top_tracks_df.iloc[0]["Cover Art"]
        col2.markdown("### Cover Art")
        col2.image(first_image_url, caption=f"Cover Art for {top_tracks_df.iloc[0]['Song Name']}", use_column_width=True)
        
        # Odtwarzacz audio dla pierwszego utworu
        first_audio_url = top_tracks_df.iloc[0]["Preview URL"]
        col2.markdown("### Audio Preview")
        if pd.notna(first_audio_url):
            col2.audio(first_audio_url, format="audio/mp3", start_time=0)
        else:
            col2.markdown("No preview available for this song.")

        # Popularity Distribution Chart
        st.markdown("### Popularity Distribution")
        fig, ax = plt.subplots()
        ax.hist(top_tracks_df['Popularity'], bins=20, edgecolor='black')
        ax.set_xlabel('Popularity')
        ax.set_ylabel('Frequency')
        st.pyplot(fig)

        # Energy vs Danceability Chart
        st.markdown("### Energy vs Danceability")
        fig, ax = plt.subplots()
        ax.scatter(top_tracks_df['energy'], top_tracks_df['danceability'], color='blue')
        ax.set_xlabel('Energy')
        ax.set_ylabel('Danceability')
        st.pyplot(fig)

if __name__ == "__main__":
    main()























    

