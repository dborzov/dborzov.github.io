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

To see what I mean, let us figure out why the error is of order of 10% for 50 iterations, but converges to a wrong answer at 60. To do this we have to know how the number is represented internally, look up the default  [mantissa/significand](https://en.wikipedia.org/wiki/Significand) size for the programming language of our choice and make the estimation calculation on a piece of paper.


#### The quadratic equation ####

Even writing a program that solves the quadratic equation
for arbitrary constant values is a serious task.
For example, let us consider the following equation
\[
![Img](./img/quadratic.gif)
\]
Note that there is no constant term and thus one solution is simply zero. However, the naive solution with the quadratic formula fails to reflect this. Here is the first Google result for "quadratic equation solver":

\[
![Img](http://dimaborzov.com/img/QuadraticEquation.png)
\]
For the general case implementation, we must treat each marginal case separately. First, if the constant term is zero, then if the quadratic term is absent, and so on, one by one.

Quadratic equation is the simplest case of a numerical problem imaginable. Yet even here we see that one needs to manualy implement basic calculus behind the known solution.




#### Logarithms. ####

Logarithmic terms are notoriously hard to work with. Let us assume we study an unknown function numerically the leading term for which looks as one of this options:

\[ f(x) = \textrm{Log} \Large( x \Large)^{N} + x \]

This is an actual problem I encountered, when we were working on the research study on 2D.

#### Summary. ####
Here is how the new quantity datatypes could be better:

+ We saw in the example of accumulating errors that every operation performed with the number should be tracable. Errors and uncertainties should be recorded from each operation and reported when needed.
+ With the quadratic equation solver it is obvious that tracing analytic expressions used for computations allow for automatic implementation of the marginal cases and can save the developer a lot of time.
+ Datatype representation scaling should match the problem at hand and not be fixed.

Doing things right
---------------------------------
This issues are well known. Now we let us discuss the solutions that solve these issues.

#### What is out there. ####

One good classic where the functional number representation was implemented and used since the days of yan is in the language behind Wolphram Mathematica. Numbers are represented.

Too bad that for reasons that is destined to slowly go into obscurity being locked despite its technological briliance.

Another example when things are done right is the SymPy, a Python package for symbolic computations. Functional number representation is very solid, Although the focus is on making tools for symbolic calculations, not the viable alternative to the floating point.

#### Why not flaky. ####

> An infinite number of mathematicians walk into a bar. The first orders a beer. The second orders half a beer. The third orders a quarter of a beer. Before the next one can order, the bartender says, “You’re all assholes,” and pours two beers.
>[TE](http://www.komplexify.com/math/jokes/MathWalksIntoABar3.html)


So we saw that how to make things better than going floating points and why we should. These reasons compeled me start Flaky, an open-source project project.

Numbers are represented as operations to the other numbers. Together they can make up long layers (or flakes). Simplifying occurs whenever possible.

\[
(\textrm{frac},4,\textrm{pow}(5,(\textrm{frac},1,2))) = \frac{4}{\sqrt{5}}
\]

The size parameter defines when the datatype length is too long, the rounding up occurs. When the rounding occurs there is a logging method to keep track of it. There is also the uncertainty estimation for margins of confidence.

Flaky is written in the [Go programming language](http://www.golang.org). The repository is available on [Github](https://github.com/dborzov/FlakyPastry).




