Flaky: datatypes for real world quantities
===============================



### *Abstract:* Modern datatype implementations for numbers and quantities (mass, time ,length) should be smarter: keep track of all the possible averaging errors, understand units and conversion. Flaky, an open source framework, solves all these issues.


Floating point datatype is the de-facto standard accross the industry. Since its introduction, floating point was accepted almost universally accross the technology and nowdays lies in the foundation of every system whether it is money amount in a trading system, size of the bridge built from an AutoCAD file, universally we have the very same representation.

However, the floating point is incredibly fragile and can lead to errors. Let us consider 3 illustrating examples of things going wrong.

Accumulating errors
-----------------------
Well, this one is no brainer. Let one pound of bananas consts. How much does a kg cost? Let us run a program:

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
    print reversable_iterations(50)
    print reversable_iterations(40)
    print reversable_iterations(100)

Which yields:

    The intial value is  1.9934545345
    with 1 iterations, we get 1.9934545345
    with 10 iterations, we get 1.9934545345
    with 20 iterations, we get 1.99345453444
    with 50 iterations, we get 1.64872126455
    with 40 iterations, we get 1.99311204568
    with 100 iterations, we get 1.0

Square equation
---------------------
Let us take the following quadratic equation:
    \[ 10^{-19} x^2 + 15 x = 0 \]
And solve it using the library of your choice. Here is the first Google result for quadratic equation solver:

![Img](http://dimaborzov.com/img/QuadraticEquation.png)

Yet this is not the feature of a , but a sign of the general deep-rooted problem.

[Obligatory xkcd](http://what-if.xkcd.com/11/)


Logarithms.
-----------------------
Things could go very bad very quickly with non-analitical terms in the expansion. Let us assume we study function the leading term for which looks as one of this options:
    \[ f(x) =\textrm{Log} \Large( Log(\frac{1}{x}) \Large) + x \]
    \[ f(x) = Log \Large( \frac{1}{x} \Large) + x \]

This is an actual problem I encountered, when we were working on the research study on 2D.


Doing things right
---------------------------------
This issues are well known and of course are . Not only errors go unreported but it is

Let it be Flaky
----------------

> An infinite number of mathematicians walk into a bar. The first orders a beer. The second orders half a beer. The third orders a quarter of a beer. Before the next one can order, the bartender says, “You’re all assholes,” and pours two beers.
>[TE](http://www.komplexify.com/math/jokes/MathWalksIntoABar3.html)


So we saw that how to make things better than going floating points and why we should. These reasons compeled me start Flaky, an open-source project project, with following features:

Flaky is written in Go.

The easiest way to play is at the FlakyPastry website: a sandbox for playing with FlakyQuantities.
Please join me and to contribute to




