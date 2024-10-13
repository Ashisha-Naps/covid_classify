import streamlit as st
from audiorecorder import audiorecorder
#from st_files_connection import FilesConnection
#import boto3
import io
import uuid
import librosa
from xgboost import XGBClassifier
import numpy as np
from sklearn.preprocessing import LabelEncoder,StandardScaler
label_encoder = LabelEncoder()
model = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss')
#def uploadFileToS3(bucket, fileName, fileBytes):
    #session = boto3.Session()
    #s3 = session.client('s3', region_name=st.secrets["AWS_DEFAULT_REGION"],aws_access_key_id = st.secrets["AWS_ACCESS_KEY_ID"],aws_secret_access_key = st.secrets["AWS_SECRET_ACCESS_KEY"])
    #s3.upload_fileobj(fileBytes, 
    #bucket, fileName)

def load_model():
    
    model.load_model('model/covid_classify.json')
    label_encoder.classes_ = np.load('model/classes.npy')
    return model

def predict(audio_buffer):
    #if model.get_params() :
    model = load_model()    
    X_new =  audio_vec(audio_buffer)
    #print(X_new)
    scaler = StandardScaler() 
    X_train_ = scaler.fit_transform(X_new.reshape(1,-1))
    y_pred = model.predict(X_train_)
    # Decode predictions back to genre names
    y_pred_decoded = label_encoder.inverse_transform(y_pred)
    return y_pred_decoded

def audio_vec(audio_buffer): 
    try:
        audio, sr = librosa.load(audio_buffer, sr=None)
        # Extract MFCC features using librosa
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
        mfccs_mean = np.mean(mfccs.T, axis=0)  # Get mean of MFCC features
        # Chroma features
        chroma = librosa.feature.chroma_stft(y=audio, sr=sr)
        chroma_mean = np.mean(chroma.T, axis=0)

        return np.concatenate((
            mfccs_mean, chroma_mean
        )) 
    except Exception as e:
        return None
st.title("Audio Recorder")
audio = audiorecorder("Click to record", "Click to stop recording")
#conn = st.connection('s3', type=FilesConnection)
if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.export().read())  
    
    # To save audio to a file, use pydub export method:
    #audio.export("audio.wav", format="wav")
    audio_buffer = io.BytesIO()
    audio.export(audio_buffer, format="wav")
    predictvalue = predict(audio_buffer)
    #uploadFileToS3("covidrecordings",str(uuid.uuid4())+".wav",audio_buffer)
    # To get audio properties, use pydub AudioSegment properties:
    st.write(f"Covid Status: {predictvalue}")
    
    #st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")
   


