Flaky: datatypes for real world quantities
===============================



### *Abstract:* Modern datatypes for quantities (such as length, time, a number) should employ ideas from functional programming: keep track when the rounding errors arise,  support defining with functions, represent results appropriately to the context. Flaky, an open source framework, wants to make things right.


[Floating point datatype](https://en.wikipedia.org/wiki/Floating_point) is the de-facto standard for real world quantities. Whether it is a banking account or sizes of the bridge nearby (designed in AutoCAD), this datatype lies in the foundation of every system. Since its introduction in the dawn of computing, floating point was accepted almost universally.

Advantages such as scalability, resilence and ease of use make floating point the datatype of choice again and again. However, it is also fragile and prone to errors. This limitations are well known, of course, and could be minimized with appropriate  expertise and focus.

And yet I believe that we, as an industry, could do better. Number respresentation based on functional programming paradigm minimizes flaws manifest to the floating point datatypes. And it could be made as resilient and scalable as the floating point. In this article, I outline why, I decided to write Flaky, an open source library that implements these ideas.

In the first section here we will glance at illustrating cases of when floating point breaks and try to undestand what flaws should be addressed. We then look at other initiatives in this space. Finally, I introduce the design I came up with for Flaky.

When floating point fails
-----------------------
Let us consider illustrative cases of when floating point representation leads to dramatically wrong answers.

#### Accumulating errors ####

Well, this one is obvious. When the number cannot be represented exactly, it has to be rounded up. These rounding errors can accumulate and can lead to silly results.

Let us, for example, take the square root of a number several times, and then try to reproduce the original value with reversal operations by taking squares.

    # price.py listing, a Python script
    import math
    INITIAL_VALUE=1.9934545345

    def reversable_iterations(iteration_number):
        test_floating = INITIAL_VALUE
        for i in range(iteration_number):
            test_floating = math.sqrt(test_floating)
        for i in range(iteration_number):
            test_floating = test_floating**2
        return 'with '+str(iteration_number)+' iterations, we get '+str(test_floating)

    print 'The intial value is ',INITIAL_VALUE
    print reversable_iterations(1)
    print reversable_iterations(10)
    print reversable_iterations(20)
    print reversable_iterations(40)
    print reversable_iterations(50)
    print reversable_iterations(60)

This yields:

    The intial value is  1.9934545345
    with 1 iterations, we get 1.9934545345
    with 10 iterations, we get 1.9934545345
    with 20 iterations, we get 1.99345453444
    with 40 iterations, we get 1.99311204568
    with 50 iterations, we get 1.64872126455
    with 60 iterations, we get 1.0

That the end result breaks is hardly a suprise. Morover, a similar effect could be achieved for any number respresentation datatype. Just from the general principles, if the size  of the [Kolmogorov complexity](http://en.wikipedia.org/wiki/Kolmogorov_complexity) of a number is larger than the memory allocated for the datatype, these types of errors cannot be ruled out.

What I wanted to emphasize here instead is the total equanimity of the floating type. It is very hard to understand what is going on at various stages. In my opinion, it is an incredible engineering design flaw.

To see what I mean, let us figure out why the error is of order of 10% for 50 iterations, but converges to a wrong answer at 60. To do this we have to know how the number is represented internally, look up the default  [mantissa/significand](https://en.wikipedia.org/wiki/Significand) size for the programming language of our choice and make the estimation calculation on a piece of paper. Seriously. In 2013.


#### A square equation ####

Let us take the following quadratic equation:
    \[ 10^{-19} x^2 + 15 x = 0 \]
And solve it using the library of your choice. Here is the first Google result for quadratic equation solver:

\[
![Img](http://dimaborzov.com/img/QuadraticEquation.png)
\]

Yet this is not the feature of a , but a sign of the general deep-rooted problem.

[Obligatory xkcd](http://what-if.xkcd.com/11/)


#### Logarithms. ####

Things could go very bad very quickly with non-analitical terms in the expansion. Let us assume we study function the leading term for which looks as one of this options:
    \[ f(x) =\textrm{Log} \Large( Log(\frac{1}{x}) \Large) + x \]
    \[ f(x) = Log \Large( \frac{1}{x} \Large) + x \]

This is an actual problem I encountered, when we were working on the research study on 2D.

#### Summary. ####
Another feature, that is, in my opinion, completely undervaluated is how. It is very hard to trace when the rounding of error happens with floating point datatypes. It is a well known design concept that .


For the better number datatype, every operation performed with the number should be tracable. Errors and uncertainties also should be traced from each operation and reported when needed.

Doing things right
---------------------------------
This issues are well known and of course are . Not only errors go unreported but it is

#### What is out there. ####

#### Why not flaky. ####

> An infinite number of mathematicians walk into a bar. The first orders a beer. The second orders half a beer. The third orders a quarter of a beer. Before the next one can order, the bartender says, “You’re all assholes,” and pours two beers.
>[TE](http://www.komplexify.com/math/jokes/MathWalksIntoABar3.html)


So we saw that how to make things better than going floating points and why we should. These reasons compeled me start Flaky, an open-source project project, with following features:

Flaky is written in Go.

The easiest way to play is at the FlakyPastry website: a sandbox for playing with FlakyQuantities.
Please join me and to contribute to




