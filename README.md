# Song Detector (MACOS ONLY)

In order to use Song Detector you must have the following requirements:

- Any form of Mac based computer (Macbook, Mac Mini, Mac Studio etc)
- Python
- Spotify Developer program created

This isn't an application, it's a script you can run this whenever you want. You can either compile this yourself or download an already compiled version.

Spotify Developer Guide:

Steps:
  - Head to https://developers.spotify.com/
  - Click on your profile
  - Then click on dashboard
  - Click on "Create App"
  - Name your application whatever you wanna name it
  - Give your application a good description as well
  - Click on the "Settings" button
  - Copy your Client ID and paste it in the Client ID part of the script
  - Click on "View Client Secret"
  - Copy your Client Secret and paste it in the Client Secret part of the script
  - Scroll down then click "Edit" on your application
  - Head to the "Redirect URLs" tab and edit it and put this in there http://localhost:8080/callback then hit the "Save" button
  - Paste the redirect URL you just pasted in there into your script at the Redirect URL part.

When you run the program after that it will redirect you to spotify's confirmation page to authenticate you to allow you to use the application. The only thing we require is to be able to view what songs you're listening to on Spotify and your playback state. It will talk about viewing your profile etc but that is Spotify's default authentication scope.

Once you run the program successfully you're done! If you're not listening to music you will get a notification stating nothing is being played, If you're listening to a song you will get a notification stating you're listening to that song and who it's by! 
