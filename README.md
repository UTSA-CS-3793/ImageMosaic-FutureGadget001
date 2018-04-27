# ImageMosaic-FutureGadget001
Spring 2018 - Repository for Team Abracadabra

## Dependencies

  -Apparently this thing only works on Linux. Out of all of us, the only one who could get it to work was running Ubuntu 17.10
  
  -You'll need Python 3.6, Tensorflow 1.5, and numpy 1.13.3. At least, those are the versions we used. 
  
  -You'll need the PIL module. I installed it with the command `sudo apt-get install python-imaging`
  
  -You'll need the psutil module. I installed it with `pip install psutil`
  
  -You'll need the annoy, scipy, and nltk modules. I used the commands `pip install annoy`, `pip install scipy`, and `pip install nltk`
  
## How to run ("short" version)

  Unfortunately even running the project with all image vectors pre-generated takes a few hours (approx. 3). There are several thousands of images the program has to step through, and for each one it compares it to several hundred other images. The good news is that it saves partial output so you can kill it once you're tired of waiting and look at whatever it managed to output and compare it to what we have in the slides. It also tracks progress so you can tell how far along it is when you decide to kill it. 
  
  Anyway, to do this all you have to do is run the run.py file with the arguments 'mickey.jpg' and 'flower_images'. You should also be sure to have the main_img_vectors and tile_vectors directories in the same directory as you're running the program from. Everything is provided in the repo. 
  
## How to run (long version)

  To follow every step we took in producing our output, first you'd need to run classify_images.py with the argument 'flower_images/\*'. This will generate image vectors for the images used to replace each tile of the main image, and place them in a directory called "tile_vectors". This'll take a while, but not hours. After that, run main_img_splitter.py with arguments 'mickey.jpg' and 'flower_images'. Obviously the flower_images part shouldn't be needed but I didn't modify the program to accept only one argument. Oops. Anyway, this should output into a directory called "chopped" every image tile that composes the main image, which probably number in the thousands. Now, you must run classify_images2.py with the argument 'chopped/\*'. It's the same program as before but now it outputs the image vectors to a directory called "main_img_vectors". THIS part takes several hours, approximately 3, as there's probably thousands of images in that directory. Once that's done, you can now follow the same instructions as in the short version. That is, run the run.py file with the arguments 'mickey.jpg' and 'flower_images'.

## References
https://github.com/codebox/mosaic 

   An implementation of a mosaic creator without Tensorflow. 

http://douglasduhaime.com/posts/identifying-similar-images-with-tensorflow.html

   We followed this to integrate Tensorflow into the above project. 
