<h1 align="center" id="title">AI-Assistant</h1>

<p align="center"><img src="https://socialify.git.ci/its-nihal-patel/AI-Assistant/image?font=Source%20Code%20Pro&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Circuit%20Board&amp;theme=Dark" alt="project-image"></p>

<p align="center"><img src="https://img.shields.io/badge/-made%20with%20python-green" alt="shields"></p>

<p id="description">It is a voice assistant which can be used to interact with your computer to accomplish daily goals. A python based programme that uses speech recognition and text-to-speech functions. This AI is desined in ubuntu linux and works only when system is online.</p>

<p>NOTE: 1) This project is built in linux OS it will not work properly on windows.
         2) To run on windows change espeak to sapi5
         3) play music command needs to code again.</p>
        
          >>> elif 'play music' in query:
                 music_dir = 'path goes here'
                 songs = os.listdir(music_dir)
                 print(songs)    
                 os.startfile(os.path.join(music_dir, songs[0]))


  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   final word - plays 'Quran' recitation on youtube.
*   tell time - when command 'tell time' is given it tells time
*   greet - upon waking it will greet you according to the time
*   day - tells you the day of week
*   recite - plays recitation of quran from youtube
*   open youtube - opens youtube
*   wikipedia - tells you information from wikipedia
*   play music - plays music from computer

  
  
<h2>💻 Built with</h2>

Technologies used in the project:

*   Python
*   pyttsx3
*   speech recognition
*   pywhatkit
*   espeak
