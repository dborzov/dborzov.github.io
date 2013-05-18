Flaky: datatypes for real world quantities
===============================



### *Abstract:* Modern datatypes for quantities (such as length, time or a number) should employ ideas from the functional programming: keep track when the rounding errors arise,  support defining with functions, represent results appropriately to the context. Flaky, an open source framework, wants to make things right.


[Floating point datatype](https://en.wikipedia.org/wiki/Floating_point) is the de-facto standard for real world quantities. Whether it is a banking account or sizes of the bridge nearby (designed in AutoCAD), this datatype lies in the foundation of every system. Since its introduction in the dawn of computing, floating point was accepted almost universally.

Advantages such as scalability, resilence and ease of use make floating point the datatype of choice again and again. However, it is also fragile and prone to errors. This limitations are well known, of course, and could be minimized with appropriate  expertise and focus.

And yet I believe that we, as an industry, could do better. Number respresentation based on the ideas of functional programming minimizes flaws manifest to the floating point datatypes. And it can be made as resilient and scalable as the floating point. In this article, I outline why, I decided to write Flaky, an open source library that attempts to implement such concepts.

In the first section we will glance at illustrating cases of when floating point breaks and try to understand what flaws should be addressed. We then look at other initiatives in this space. Finally, I introduce the design that I came up with for Flaky.

When floating point fails
-----------------------
Let us consider illustrative cases of when floating point representation leads to dramatically wrong answers.

#### Accumulating errors ####

Well, this one is obvious. When the number cannot be represented exactly, it has to be rounded up. These rounding errors can accumulate and can lead to silly results.

Let us, for example, take the square root of a number several times, and then try to reproduce the original value with the reversal operation (that is, taking squares)

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

What I wanted to emphasize here instead is the total equanimity of the floating type. It is very hard to understand what is going on at various stages. In my opinion, this is an incredible engineering design flaw.

To see what I mean, let us figure out why the error is of order of 10% for 50 iterations, but converges to a wrong answer at 60. To do this we have to know how the number is represented internally, look up the default  [mantissa/significand](https://en.wikipedia.org/wiki/Significand) size for the programming language of our choice and make the estimation calculation on a piece of paper.

The lack of the uncertainty estimation defeats the whole purpose of any computation.


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

Quadratic equation is the simplest case of the numerical problem imaginable. Yet even here we see that one needs to manualy implement basic calculus logic behind the known solution.




#### Scaling does not match the problem ####

Let us once again consider the quadratic equation, but this time in terms of the new variable we introduce
\[
y = \frac{\textrm{exp}(x)}{1 + \textrm{exp}(x)}
\]
The quadratic equation in terms of y looks as follows
\[
a \textrm{ log}^2 (\frac{y}{1-y}) + b \textrm{ log} (\frac{y}{1-y}) + c = 0
\]
Here is what the plot of the definition of the y function looks like
\[
![Img](img/softThreshold.png)
\]
The variable y "maps" the whole x range to its (0,1) range. This function is also known as the soft threshold.

Attempting to solve this problem numerically in terms of y should be quite challenging. The number representation for y means that all the "graining" for sufficiently large x values (say, x>5) becomes too rude.

That is, the number representation for the floating point
\[
\underbrace{\text{integer}}_{\text{mantissa}} \cdot \text{base}^\text{exponent}
\] offers the scale that is not appropriate for this problem. The solutions for large x should fail spectacularly. Interestingly, the solutions with the y going to the zero limit (x going negative, for example, x<-5) will be a little more resilient. The lack of the constant term (1. for large x) means that the base of the exponent will scale down gracefully.

How does this issue work for the (relatively) real world problems? Let me share my personal experience. In our research study on [the physics of ultracold gases in 2D](http://prl.aps.org/abstract/PRL/v110/i14/e145301) we derived a complex equation we ended up solving numerically. The solution function was diverging logathmically in the limit in which we were interested

\[ f(x) =  \textrm{Log}( x )^{w} + \text{ non-diverging terms }, x \rightarrow 0 \]

However, it turned out practically impossible to learn the order of the divergency w from this numerical solution. The floating point representation meant that the log of the number is represented inefficiently for the problem.

The solution was to introduce the new variable
\[
z = -\textrm{Log}( x )
\]
and express the whole problem and the solution in terms of z.

Matching the number representation scale to the problem in the general case, is of course, impossible. It depends on the interpretation of the problem , what we are actually interested in.

However, it would have been helpful if it was possible to tweak the scaling used without too much hassle.

#### Summary. ####
Here is how the new quantity datatypes could be better:

+ We saw in the example of accumulating errors that every operation performed with the number should be tracable. Errors and uncertainties should be recorded from each operation and reported when needed.
+ With the quadratic equation solver it is obvious that tracing analytic expressions used for computations allow for automatic implementation of the marginal cases and can save the developer a lot of time.
+ Datatype representation scaling should match the problem at hand and not be fixed. Tools must exist to do this with ease.

Doing things right
---------------------------------

> An infinite number of mathematicians walk into a bar. The first orders a beer. The second orders half a beer. The third orders a quarter of a beer. Before the next one can order, the bartender says, “You’re all assholes,” and pours two beers. [TE](http://www.komplexify.com/math/jokes/MathWalksIntoABar3.html)

 Now we let us discuss the solutions that can fix these issues.

#### What is out there. ####

Apparently, th best way to approach the problem is to use the functional programming concepts. To retain the analytical expression used for the value definition, at least to some limit, and to have tools to change it when needed.

A classic case where the functional number representation was implemented is the language behind Wolphram Mathematica.
Too bad that for the non-technical reasons it is apparently destined to go into obscurity and not fulfill its full potential.

Another example when things seem to be done right is the [SymPy](http://sympy.org/en/index.html), a Python package for symbolic computations. Functional number representation is very solid. Although the focus is on making tools for symbolic calculations, not the viable alternative to the floating point.

#### Why not flaky. ####



So we saw how to make things better and why we should. These reasons compeled me start Flaky, the open-source project for quantity datatype based on the concepts of functional programming.

Numbers are represented as operations to the other numbers. Together they can make up long layers (or flakes). Simplifying occurs whenever possible.

\[
(\textrm{frac},4,\textrm{pow}(5,(\textrm{frac},1,2))) = \frac{4}{\sqrt{5}}
\]

The size parameter defines when the datatype length is judged to be too long, then the rounding up occurs. There is a logging method to keep track of it. There is also the uncertainty estimation for margins of confidence.

One may choose the specific representation of the number. Matching, rounding and scaling happens seamlessly.

Flaky is written in the [Go programming language](http://www.golang.org). The repository is available on [Github](https://github.com/dborzov/FlakyPastry) (or will be soon :)) .

It should be fun! Also, here is an image of the flaky pastry from Wikipedia:

<br><br><br><br>

\[
![Img](http://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Sweet_potato_flaky_pastry.jpg/282px-Sweet_potato_flaky_pastry.jpg)
\]




