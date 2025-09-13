from PIL import Image
# Importujemy specjalne narzędzia z biblioteki google.colab
from google.colab import files
import io

def remove_metadata_in_colab():
    """
    Używa interfejsu Google Colab do wgrania pliku, usunięcia metadanych
    i automatycznego pobrania przetworzonego pliku.
    """
    print("Proszę wybrać plik graficzny do przetworzenia...")
    # Otwiera okno dialogowe przeglądarki do wyboru pliku
    try:
        uploaded = files.upload()
    except Exception as e:
        # Obsługa błędu, który może wystąpić w niektórych środowiskach poza Colab
        if 'google.colab' not in str(e):
             print(f"Wystąpił błąd: {e}")
        # Błąd 'Could not forward port' jest częsty i można go zignorować, ponawiając próbę
        print("\nWystąpił błąd podczas przesyłania. Spróbuj uruchomić komórkę ponownie.")
        return


    if not uploaded:
        print("\nNie wybrano żadnego pliku. Przerwano operację.")
        return

    # Przetwarzamy każdy wgrany plik (zazwyczaj będzie to jeden)
    for original_filename, file_content in uploaded.items():
        try:
            print(f"\nPrzetwarzanie pliku: {original_filename}")
            
            # Wczytujemy obraz z danych w pamięci
            oryginalny_obraz = Image.open(io.BytesIO(file_content))

            # Logika usuwania metadanych pozostaje bez zmian
            dane_pikseli = list(oryginalny_obraz.getdata())
            obraz_bez_metadanych = Image.new(oryginalny_obraz.mode, oryginalny_obraz.size)
            obraz_bez_metadanych.putdata(dane_pikseli)

            # Przygotowujemy nazwę nowego pliku
            nazwa, rozszerzenie = original_filename.rsplit('.', 1)
            nowa_nazwa_pliku = f"{nazwa}_bez_metadanych.{rozszerzenie}"

            # Zapisujemy przetworzony obraz do bufora w pamięci
            byte_buffer = io.BytesIO()
            # Musimy jawnie podać format, ponieważ Pillow nie może go wywnioskować z nazwy pliku
            format_obrazu = oryginalny_obraz.format if oryginalny_obraz.format else rozszerzenie.upper()
            obraz_bez_metadanych.save(byte_buffer, format=format_obrazu)
            
            # Zapisujemy zawartość bufora do fizycznego pliku na serwerze Colab,
            # aby funkcja `download` mogła go znaleźć.
            with open(nowa_nazwa_pliku, "wb") as f:
                f.write(byte_buffer.getvalue())

            # Inicjujemy pobieranie pliku przez przeglądarkę
            files.download(nowa_nazwa_pliku)
            
            print(f"Sukces! Plik '{nowa_nazwa_pliku}' został przygotowany do pobrania.")

        except Exception as e:
            print(f"Wystąpił błąd podczas przetwarzania pliku {original_filename}: {e}")

# --- Główna część aplikacji ---
if __name__ == "__main__":
    remove_metadata_in_colab()

