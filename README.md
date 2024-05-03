# Eurodyne (Previously GPT4ALL CLI)
A program designed for (in theory) easy AI training. It's still in VERY early development and doesn't work great, but It's a start. 

# But How does this work
By using the Transformers Library (Tnx Hugging face) we have access to several Pre made models and Datasets. At the current phase Eurodyne is a CLI that is able to load these from hugging face and do extra training. Its very basic (you can make some very narcissistic robot) but as this goes on I hope that as the training abilities get better my (very little)  knowledge on machine learning will grow.  

## How do I use it (Old Ver To be phased out in the future) 

	Git clone and open the repository

	Run pip install -r requirements.txt

	run python3 old_main.py 

This will initialize GPT4ALL and A model. In the future this will serve as the "Manager". However, for custom trained models you will have to use the transformers library for now (I haven't written a safe-tensor to gguf or wrote a custom loader yet ;_;

This project is under HEAVY development things will be buggy and unstable and change alot.

	Commands
		ls displays the GPT4ALL Models
		ch allows you to change the model
		hw allows you to set the compute hardware for GPT4ALL
		help gives you a list of commands
		train
		loads The Ripper doc (if you didnt guess already i love cyberpunk 2077) 

	Ripper doc is what makes this project special in that it is the thing that manages training. 
	Its far from  perfect but it is getting somewhere. The nice part is you can use ripper doc as
	a "library" for your other project
	
	Ripper doc will then ask for a model tag off of hugging face a data set off hugging face and an
	output directory then well assuming all the info was filled out correctly it will go to work

## New Version

    git clone the repo
    run pip install -r requirements.txt

when running commands (only training thus far) you do python3 eurodyne.py then your flags
For instance to start training 

    python3 eurodyne.py -t -m gpt2 -d imdb -out /blah/blah/blah/
    
    -t is telling eurodyne you would like to train a model
    -m the model tag from huggingface
    -d the data from huggingface
    -out the directory you would like the files to be stored

Like I said only training is supported in eurodyne.py but soon everything else will be supported

## Conclusion

This project is  going to be tough since IDK exactly what im doing. But considering I still have about a year of dev time left and I have gotten alot done so far (especially considering the challenges I faced when it came to hardware and software amongst other challenges) I think we are getting somewhere

So I leave this note here for now 

## With <3 
Jackisapi

For testing your models I haven't written anything good yet (though when I do I will share it here lol
WARNING THIS SOFTWARE IS WRITEN BY A 16 YEAR OLD UNTIL I HAVE HAD A 3RD PARTY TEST THIS 
DON'T RELY ON IT HEAVILY THINGS WILL BREAK OR GET UNSTABLE 