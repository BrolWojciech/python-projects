import panel as pn
import hvplot.pandas
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import streamlit as st

def spotify():
    SPOTIPY_CLIENT_ID = '319830f7c85a4a02889ad9e1f41c90c6'
    SPOTIPY_CLIENT_SECRET = 'c6b21ccca01e4185a13484006481f189'

    auth_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    return sp

def get_top_tracks_info(artist_name, sp, limit=10):
    try:
        artists = sp.search(q='artist:' + artist_name, type='artist', limit=10)
        artist_uri = artists['artists']['items'][0]['uri']
        results = sp.artist_top_tracks(artist_uri)
        track_result = []
        features_result = []

        for i, item in enumerate(results['tracks'][:limit]):
            track_id = item['id']
            track_name = item['name']
            popularity = item['popularity']
            preview_url = item['preview_url'] if 'preview_url' in item else 'N/A'
            cover_art = item['album']['images'][0]['url'] if 'album' in item and 'images' in item['album'] and item['album']['images'] else 'N/A'

            track_result.append((i, artist_name, track_id, track_name, popularity, preview_url, cover_art))

            # Pobranie informacji o funkcjach audio tylko raz
            audio_features = sp.audio_features(track_id)
            features_result.extend(audio_features)

        track_df = pd.DataFrame(track_result, columns=('Item', 'Artist', 'Id', 'Song Name', 'Popularity', 'Preview URL', 'Cover Art'))
        features_df = pd.DataFrame(features_result)

        final_df = pd.concat([track_df, features_df], axis=1)
        final_df_sorted = final_df.sort_values(by=['Popularity'], ascending=False)

        return final_df_sorted

    except Exception as e:
        return f"Error: {e}"

def main():
    st.title('Spotify Top Tracks Dashboard')

    # Input użytkownika
    artist_name = st.text_input('Enter Artist Name: ')

    # Przycisk do uruchomienia
    if st.button('Generate Dashboard'):
        sp = spotify()
        top_tracks_df = get_top_tracks_info(artist_name, sp)

        # Wyświetlanie informacji
        st.markdown(f"## Top Tracks for {artist_name}")
        st.dataframe(top_tracks_df)

if __name__ == "__main__":
    main()






    
