# Senior Project - Face Detector/Recognizer

## Project description
This project consist of a website that is able to take user's two uploaded videos and detect their face. The first video is to train the model with a name given by the user, we created this model using opencv. The second video the user uploads will actaully put the model to use and detect the face that was given in any video.

## Demo
![demo](https://user-images.githubusercontent.com/43011353/202584930-1277d529-6f7b-4a4e-a3c9-895ca5b6548e.gif)



## Project components

This project will be using 
 * Python
 * opencv
 * AWS

## Creating training video
- In order to test this software you will need to train the algorithm with a video of your face. This video must be taken with a camera at an arms length away. You should move the camera to get many angles of your face. The more angles and variations the smarter the algorithm is. The video should no longer than 30 seconds. This video must be in .mp4 format.
- There are example videos in the /Source_Code/Example_Videos/ if you want to give it a try.

## Testing video
- To test this algorithm you can use any video (must be .mp4 files), it will tell you if it recognizes your face or not.

## Running Locally 
- You want to clone this repository onto your machine. Included is a requirments.txt that will have our dependencies that you should run.
- Using your terminal navigate to the Source_code folder, and run the following command: 
```bash 
flask run
```
## Website/IP - AWS server is no longer running
- Access through this IP to test your own pictures: http://34.201.9.122:5000/
