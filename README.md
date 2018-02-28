# python90minutes
There's a lot of hour-of-code lessons out there in the world; this one is mine. A live version of these pages is at https://morris.cloud/python so you may want to review it there to decide if it is something you want to use.

Background on why I created this. I volunteer-taught one class period at a high school through Microsoft's TEALS program, and through that the other volunteers and I generated a lot of content, which you can see today at https://xenotropic.net/skyline. This year I was asked to teach eighth graders at another school for a ninety-minute period, who had done some scratch programming but were eager to do "real programming". So I went searching through those old resources to try to find something suitable. I adapted one of the assignments to be more free-standing, and formatted it to be one self-contained lesson, using trinket.io as the interface for the students. This is the webpages I used to teach a ~90 minute class in Python to kids (this is probably good for 8th-12th) who had done some Scratch coding but no previous Python. It's a little bit of a "throw them into the deep end and see if they can swim" lesson, but for the most part they did. I thought it might be too hard, but it wasn't really; however these did seem like particuarly motivated and engaged eighth-graders. Your students may vary.

What this lesson addresses. The main computer science concepts that this teaches are Python syntax, setting variables, doing math, data typing, and while loops. There is an online file of a partially-completed program ("problem_outline.py"), and essentially they will be spending the period going through that and trying to figure out what each line needs in order to get the program to "work". The first problem they will have is on line four of that file, getting user input as a string (which is what input() returns) and casting it to an integer using int() so they can do math on it. 

Here's a manifest of some the files:

intro.html - a quick overview I used to introduce myself and python

index.html - contains an overview of the problem to be solved, which is a jelly bean counter. The user gives a number of beans, and then a while loop repeats, asking the user how many beans they ate. When the number of beans is zero, the while loop condition is satisfied, and it exits. 

pyref.html - an overview of some Python basics and examples. The main one students will need for the bean counter problem is the while loop and type casting (section 5, all the way at the end). 
    
The .py files are not linked by the html files, because they are saved in trinket.io instances, the URLs of which are in the index.html page. However, including that code here to preserve it in case trinket.io doesn't keep the URLs alive forever or you want to use a different interface. 
