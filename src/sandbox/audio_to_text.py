import speech_recognition as sr

def audio_to_text(audio_file_path):
    """
    Convert an audio file to text using speech recognition.
    
    Args:
        audio_file_path (str): Path to the audio file (e.g., 'sample.wav').
    
    Returns:
        str: Transcribed text from the audio, or an error message if transcription fails.
    """
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    # Load the audio file
    try:
        with sr.AudioFile(audio_file_path) as source:
            # Listen to the audio file
            audio_data = recognizer.record(source)
            
            # Convert audio to text using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        return "Could not understand the audio."
    except sr.RequestError as e:
        return f"Error with the recognition service: {e}"
    except FileNotFoundError:
        return "Audio file not found."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage
if __name__ == "__main__":
    # Replace 'sample.wav' with the path to your audio file
    result = audio_to_text("C:\Users\calif\Documents\air_traffic_controller\air-traffic-controller\training-dataset\audio\Flex-333-landing.mp3")
    print(result)