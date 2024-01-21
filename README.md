# Music-Genre-Webapp

##IMPORTANT - The deployed website is not working because Heroku has stopped giving free Dynos for the API :(

Genre classification, or categorizing music into different categories or genres, is a concept that helps distinguish between the two genres based on the rhythm they compose or maintain.


## Abstract 

This project is primarily aimed to create an automated system for classification model for music genres. The first step includes collecting a properly classified music dataset and preprocess the music for further processes. The dataset used here is GTZAN genre dataset. The second step includes the preprocessing of the data. Here in this step, the data size or the number of samples in each genre is increased in order to make the dataset suitable for feeding a Convolutional Neural Network (CNN). In the third step, the Mel-frequency cepstral coefficients (MFCCs) are calculated for each sample and classification label is added to each sample. Now the final dataset is prepared. In the fourth step, a Convolutional Neural Network is created and then the dataset is feed to the neural network model with 80% training size, 10% testing size and 10% validation size of the dataset. During training the model, a 93% of testing accuracy as well as 81% testing accuracy is obtained. The obtained model is exported and it is ready to be deployed. Lastly, a REST API is created for deployment using Python-Flask and is deployed on Heroku server.



##  Feature Extraction

The music feature vector is extracted using the Librosa library in python. Librosa is a python library specifically used for music/audio processing/analysis. It provides the building blocks necessary to create music information retrieval systems. Each audio file is taken and from that, its feature vector is extracted. The extracted feature vector is called Mel-Frequency Cepstral Coefficients (MFCC). 


## Deployment and Implementation

The music genre detection uses microservice system design architecture. The steps followed for the deployment are as follows

1. Initially the Neural Network Model was integrated into a Flask App to convert it into an API which responds to POST method on endpoint `/file-upload`
2. The Flask App was then assigned a port address and deployed to Heroku with the required authorizations. The deployed url is [https://radiant-river-01801.herokuapp.com/](https://radiant-river-01801.herokuapp.com/)



1. Then the website was designed using HTML, CSS, Bootstrap and Wave-surfer Library.The user can directly upload their audio for detection through the file Input button.
2. At the client side it uses an &quot;Upload&quot; Function which appends the users audio into a form and POST it to the previously Deployed API asynchronously using JS Fetch .
3. The JSON response from the API contains the predicted Genre which is then displayed into the website using Document Object Model (DOM) Manipulation.

1. The website is then deployed to Netlify with the required configurations. [https://guist-genre.netlify.app](https://guist-genre.netlify.app/?#)


<!-- ##  Flask API Input

The API can be directly used by uploading from its homepage.


##  Flask API Output

The API returns JSON output with the label key as the predicted Genre -->


## Client : Landing Page
![image10](https://user-images.githubusercontent.com/70725731/183311592-adbf18b5-d862-4fd0-9302-9c3a38c224d2.png)



## Client : Spectrogram and Predicted Output
![image11](https://user-images.githubusercontent.com/70725731/183311611-ab931617-fb44-47cd-8916-dab22e29bddb.png)


## Conclusion and Future Works

The Music Genre Detection can be a great tool for video and audio streaming services.With the huge increase in online music databases and daily uploads, people find it increasingly difficult and tedious to manually categorize their songs to its genre. Also as music is inherently ambiguous, it may lead to confusion if the artist categorizes its music to a wrong genre. Being able to automatically classify and provide tags to the music will help better recommendations to their users and increase their engagement to the service.

The extension of this work would be to consider bigger data sets and also tracks in different formats(mp4, au etc.). Also, with time the style represented by each genre will continue to change. So the objective for the future will be to stay updated with the change in styles of genres and extending our software to work on these updated styles. This work can also be extended to work as a music recommendation system depending on the mood of the person.

##  References

- [**http://www.practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/**](http://www.practicalcryptography.com/miscellaneous/machine-learning/guide-mel-frequency-cepstral-coefficients-mfccs/)
- [**https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification**](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification)
- **https://cse.iitk.ac.in/users/cs365/2015/\_submissions/archit/report.pdf[https://www.researchgate.net/figure/Spectrogram-generation\_fig2\_330344515](https://www.researchgate.net/figure/Spectrogram-generation_fig2_330344515)**
- [**https://www.internationaljournalssrg.org/IJCMS/2020/Volume7-Issue1/IJCMS-V7I1P102.pdf**](https://www.internationaljournalssrg.org/IJCMS/2020/Volume7-Issue1/IJCMS-V7I1P102.pdf)
- [**https://www.irjet.net/archives/V6/i5/IRJET-V6I5174.pdf**](https://www.irjet.net/archives/V6/i5/IRJET-V6I5174.pdf)
- [**https://towardsdatascience.com/understanding-audio-data-fourier-transform-fft-spectrogram-and-speech-recognition-a4072d228520**](https://towardsdatascience.com/understanding-audio-data-fourier-transform-fft-spectrogram-and-speech-recognition-a4072d228520)
- [**https://devopedia.org/audio-feature-extraction**](https://devopedia.org/audio-feature-extraction)
- [**https://towardsdatascience.com/useful-plots-to-diagnose-your-neural-network-521907fa2f45**](https://towardsdatascience.com/useful-plots-to-diagnose-your-neural-network-521907fa2f45)
