import numpy as np
import librosa
from pydub import AudioSegment
import re
import argparse
import tensorflow.keras as keras
import os


def to_wav(src, dst):
    print(src, dst)
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

    return True


def load_data(data_dict):
    X = np.array(data_dict["mfcc"])

    return X


def get_mfcc(FILE_PATH, SAMPLE_RATE=22050, hop_length=512):
    data = {
        "mfcc": []
    }

    try:
        signal, sample_rate = librosa.load(FILE_PATH, sr=SAMPLE_RATE)

        mfcc = librosa.feature.mfcc(signal, sample_rate, hop_length=hop_length)
        mfcc = mfcc.T

        data["mfcc"].append(mfcc.tolist())

        return data

    except:
        pass


def predict(FILE_PATH, MODEL_PATH, SHAPE):
    labels = [
        'blues',
        'classical',
        'country',
        'disco',
        'hiphop',
        'jazz',
        'metal',
        'pop',
        'reggae',
        'rock'
    ]

    if FILE_PATH.endswith(".mp3"):
        print("CONVERTING TO WAV")
        OUT_PATH = f"{FILE_PATH[:-4]}.wav"
        to_wav(FILE_PATH, OUT_PATH)
        FILE_PATH = OUT_PATH

    model = keras.models.load_model(MODEL_PATH)

    data = get_mfcc(FILE_PATH)

    X = np.array(data["mfcc"][0])
    X = np.resize(X, SHAPE)
    X = X[np.newaxis, ...]

    prediction = model.predict(X)
    predicted_index = np.argmax(prediction, axis=1)
    
    os.remove(FILE_PATH)
    return labels[predicted_index[0]]



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-a', '--audio',
        help="Audio File with Path",
        type=str,
        required=True
    )
    parser.add_argument(
        '-m', '--model',
        help="Saved Model Directory",
        type=str,
        required=True
    )
    parser.add_argument(
        '-s', '--shape',
        help="Desired shape of input file",
        type=str,
        default="130,20"
    )
    args = parser.parse_args()


    FILE_PATH = args.audio
    MODEL_PATH = args.model
    SHAPE = args.shape
    SHAPE = re.findall('[0-9]+', SHAPE)
    SHAPE = tuple([int(s) for s in SHAPE])

    predicted = predict(FILE_PATH=FILE_PATH, MODEL_PATH=MODEL_PATH, SHAPE=SHAPE)
    print(predicted)