# Eurodyne (Previously GPT4ALL CLI)
A program designed for (in theory) easy AI training. Its still in VERY early development and doesn't work great but Its a start. 

# But How does this work
By using the Transformers Library (Tnx Hugging face) we have access to several Pre made models and Datasets. At the current phase Eurodyne is a CLI that is able to load these from hugging face and do extra training. Its very basic (you can make some very narcissistic robot) but as this goes on I hope that as the training abilities get better my (very little)  knowledge on machine learning will grow.  

How do I use it

	Git clone and open the repository

	Run pip install -r requirements.txt

	run python3 main.py 

This will initialize GPT4ALL and A model. In the future this will serve as the "Manager". However for custom trained models you will have to use the transformers library for now (i haven't wrote a safe-tensor to gguf or wrote a custom loader yet ;_;

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

For testing your models i haven't written anything good yet (though when I do i will share it here lol

WARNING THIS SOFTWARE IS WRITEN BY A 16 YEAR OLD UNTIL I HAVE HAD A 3RD PARTY TEST THIS 
DONT RELY ON IT HEAVILY THINGS WILL BREAK OR GET UNSTABLE 