import pandas as pd
import requests

pd.set_option('display.max_colwidth', None)
pd.reset_option('display.max_rows')

quran_df = pd.DataFrame(columns=['Surah Number', 'Name', 'English Name', 'English Name Translation', 
                                 'Ayah Number', 'Juz', 'Ruku', 'Ayah Text', 'Ayah Translation', 'Audio'])

# Define the function to fetch and extract details
def get_details(quran_edition_text, quran_edition_eng_text, quran_edition_audio, surah_index):
    try:
        url_text = f'http://api.alquran.cloud/v1/quran/{quran_edition_text}'
        response_text = requests.get(url_text)
        assert(response_text.status_code==200), 'The connection was unseuccessful'
        quran_text = response_text.json()

        # Fetch english translation detail
        url_eng_text = f'http://api.alquran.cloud/v1/quran/{quran_edition_eng_text}'
        response_eng_text = requests.get(url_eng_text)
        assert(response_eng_text.status_code==200), 'The connection was unseuccessful'
        quran_eng_text = response_eng_text.json()
        
        # Fetch audio details
        url_audio = f'http://api.alquran.cloud/v1/quran/{quran_edition_audio}'
        response_audio = requests.get(url_audio)
        assert(response_audio.status_code==200), 'The connection was unseuccessful'
        quran_audio = response_audio.json()
        
        # Extract surah details from both responses
        surah_text = quran_text['data']['surahs'][surah_index]
        surah_eng_text = quran_eng_text['data']['surahs'][surah_index]
        surah_audio = quran_audio['data']['surahs'][surah_index]
        
        surah_number = surah_text['number']
        name = surah_text['name']
        english_name = surah_text['englishName']
        english_name_translation = surah_text['englishNameTranslation']
        
        # Combine Ayah text and audio
        ayah_entries = []
        for text_ayah, text_eng_ayah, audio_ayah in zip(surah_text['ayahs'], surah_eng_text['ayahs'], surah_audio['ayahs']):
            ayah_entries.append({
                'Surah Number': surah_number,
                'Name': name,
                'English Name': english_name,
                'English Name Translation': english_name_translation,
                'Ayah Number': text_ayah['numberInSurah'],
                'Juz': text_ayah['juz'],
                'Ruku': text_ayah['ruku'],
                'Ayah Text': text_ayah['text'],
                'Ayah Translation': text_eng_ayah['text'],
                'Audio': audio_ayah['audio']
            })
        
        return ayah_entries
    except Exception as e:
        print(f"Error: {e}")
        return []

# Fetch and append Surah details iteratively
quran_edition_text = 'quran-uthmani'  # Text edition
quran_edition_eng_text = 'en.asad'    # Text translation edition
quran_edition_audio = 'ar.alafasy'   # Audio edition
surah_indices = range(0, 114)  # Fetching the first three Surahs (114 full quran)

for index in surah_indices:
    details = get_details(quran_edition_text, quran_edition_eng_text, quran_edition_audio, index)
    if details:
        quran_df = pd.concat([quran_df, pd.DataFrame(details)], ignore_index=True)
        print(f"Surah at index {index} added to the DataFrame.")

# Save dataframe into a csv
quran_df.to_csv('quran.csv', index=False)

# Display the combined DataFrame
quran_df.head()