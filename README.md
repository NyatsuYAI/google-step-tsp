## Google step tsp

Originally By: [Hayato Ito](https://github.com/hayatoito) (hayato@google.com)  
2020-2022 Versions By: [Hugh O'Cinneide](https://github.com/hkocinneide)
(hughoc@google.com)

## Quick Links

- [Scoreboard]

[scoreboard]:
  https://docs.google.com/spreadsheets/d/18YQHRnnJ-p-PW9OVtXDRtMl02zha1MTEjXYz-cSNXyE/edit?usp=sharing
[github issues]: https://github.com/hayatoito/google-step-tsp/issues

## Problem Statement

In this assignment, you will design an algorithm to solve a fundamental problem
faced by every travelling salesperson, called _Travelling Salesman Problem_
(TSP). I’ll explain TSP in the onsite class. TSP is very famous problem. See
[Wikipedia](http://en.wikipedia.org/wiki/Travelling_salesman_problem). You can
understand the problem without any difficulties.

Quoted from
[Wikipedia](http://en.wikipedia.org/wiki/Travelling_salesman_problem):

> The travelling salesman problem (TSP) asks the following question: Given a
> list of cities and the distances between each pair of cities, what is the
> shortest possible route that visits each city exactly once and returns to the
> origin city?


## Visualizer

The demo page of the visualizer is
[here](https://hkocinneide.github.io/google-step-tsp/visualizer/build/default/).

The assignment includes a helper Web page,
`visualizer/build/default/index.html`, which visualizes your solutions. You need
to run a HTTP server on your local machine to access the visualizer. Any HTTP
server is okay. If you are not sure how to run a web server, use the following
command to run the HTTP server. Make sure that you are in the top directory of
the assignment before running the command.

```shellsession
python -m http.server # For Python 3
python -m SimpleHTTPServer 8000 # If you don’t want to install Python 3
```

Then, open a browser and navigate to the
[http://localhost:8000/visualizer/build/default/](http://localhost:8000/visualizer/build/default/).

Visualizer was only tested by Google Chrome. Using the visualizer is up-to you.
You don’t have to use the visualizer to finish the assignment. The visualizer is
provided for the purpose of helping you understand the problem.

See
[GitHub Help](https://help.github.com/articles/configuring-a-publishing-source-for-github-pages/)
to know how to enable GitHub pages on your repository.


## what I do

coding [my_ans.py](/my_ans.py), [my_ans_min.py](/my_ans_min.py) and [my_ans_random.py](my_ans_random.py)

## Code 

#### my_ans.py

Why is it not enough to choose the closest distance? I was curious if I changed the first point and if the matching would change. Starting from all points, the distance is put into the Index and the closest distance is returned. This time this was also the first easy one I made, but unfortunately it gave the best score.

#### my_ans_random.py

I heard that when calculating page rank, Google skip to random notes with a certain probability. What would happen if we skip to a random one? This program, based on my_ans.py, has a 15% chance of skipping somewhere. The result was terrible.

#### my_ans_min.py

This is my tried and true program to produce the closest distance. Finally, based on solver_greedy.py, I thought to solve it using 2-pot.
