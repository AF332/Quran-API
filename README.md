# Quran-API

# Quran API Data Extraction

## Overview

This project extracts the complete contents of the Quran using the [Al-Quran Cloud API](https://alquran.cloud/) and saves the data into a CSV file. The extracted data includes Surah information, Ayah texts, English translations, and audio recitations.

## Features

- Fetches Quranic text from the API using the **Uthmani script edition**.
- Retrieves English translations using **Muhammad Asad's edition**.
- Collects audio recitations from **Mishary Rashid Alafasy's edition**.
- Combines all extracted data into a structured **CSV file**.
- Iterates over all **114 Surahs** to create a complete dataset.

## Technologies Used

- **Python**
- **Pandas** (for data handling)
- **Requests** (for API interaction)

## Installation & Setup

### Prerequisites

Ensure you have Python installed (>=3.6) along with the required libraries:

```sh
pip install pandas requests
```

### Running the Script

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/quran-api-extraction.git
   cd quran-api-extraction
   ```
2. Run the Python script:
   ```sh
   python API_exercise.py
   ```
3. The extracted data will be saved in `quran.csv` in the same directory.

## Code Breakdown

### 1. **Setting Up the Dataframe**

A Pandas DataFrame is initialized with the following columns:

- `Surah Number`: Number of the Surah (1-114)
- `Name`: Arabic name of the Surah
- `English Name`: Transliteration of the name
- `English Name Translation`: English meaning of the name
- `Ayah Number`: The verse number within the Surah
- `Juz`: Juz (section) of the Quran to which the verse belongs
- `Ruku`: Ruku (sub-section) of the Surah
- `Ayah Text`: Arabic text of the verse
- `Ayah Translation`: English translation of the verse
- `Audio`: URL of the recitation audio

### 2. **Fetching Data from the API**

The function `get_details()` performs the following steps:

- Sends requests to the Al-Quran Cloud API to retrieve text, translation, and audio.
- Extracts the relevant details and formats them into a list of dictionaries.
- Appends the data to the Pandas DataFrame.

### 3. **Saving Data to CSV**

After processing all 114 Surahs, the dataset is exported as `quran.csv` for further analysis or use.

## Example Output

Example of the first few rows of the CSV file:

| Surah Number | Name    | English Name | English Name Translation | Ayah Number | Juz | Ruku | Ayah Text                              | Ayah Translation                                           | Audio       |
| ------------ | ------- | ------------ | ------------------------ | ----------- | --- | ---- | -------------------------------------- | ---------------------------------------------------------- | ----------- |
| 1            | الفاتحة | Al-Fatihah   | The Opening              | 1           | 1   | 1    | بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ | In the name of Allah, the Most Gracious, the Most Merciful | [Audio URL] |

## Future Improvements

- Implement additional language translations.
- Enable filtering by Surah, Juz, or Ruku.
- Develop a web-based interface for real-time queries.

## License

This project is open-source under the MIT License.

---

**Author:** Arif

For any questions or contributions, feel free to submit a pull request or open an issue!


