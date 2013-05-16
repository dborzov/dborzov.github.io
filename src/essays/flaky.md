Flaky: a datatype standard for quantities in real world
===============================



 *Abstract:* Modern datatype implementations for numbers and quantities (mass, time ,length) should be smarter: keep track of all the possible averaging errors, understand units and conversion. Flaky, an open source framework, solves all these issues (by using classic advances of the functional programming, but if you are a user, you don't have to worry about all this crap).
--------------------------------------

> An infinite number of mathematicians walk into a bar. The first orders a beer. The second orders half a beer. The third orders a quarter of a beer. Before the next one can order, the bartender says, “You’re all assholes,” and pours two beers.[TE](http://www.komplexify.com/math/jokes/MathWalksIntoABar3.html)

Floating point datatype is the de-facto standard accross the industry. Since its introduction, floating point was accepted almost universally accross the technology and nowdays lies in the foundation of every system whether it is money amount in a trading system, size of the bridge built from an AutoCAD file, universally we have the very same representation.

However, the floating point is incredibly fragile and can lead to errors. Let us consider 3 illustrating examples of things going wrong.

Accumulating errors
-----------------------
Well, this one is no brainer. Let one pound of bananas consts $1.99. How much does a kg cost? Let us run a program:
    price_per_pound = 1.99
    pound_in_killograms = 0.453592
    for i in range(10**100):
        price_per_kilogram = price_per_pound/pound_in_killograms
        price_per_pound = price_per_kilogram * pound_in_killograms
    print price_per_pound

Whoah, some free bananas.

Square equation
---------------------
Let us take the following quadratic equation:
    $10^{-19} x^2 + 15 x = 0$
And solve it using the library of your choice. Here is the first Google result for quadratic equation solver:

![Img](http://dimaborzov.com/img/QuadraticEquation.png)

Yet this is not the feature of a , but a sign of the general deep-rooted problem.

[Obligatory xkcd](http://what-if.xkcd.com/11/)


Logarithms.
-----------------------
Things could go very bad very quickly with non-analitical terms in the expansion. Let us assume we study function the leading term for which looks as one of this options:
    $f(x) =Log [Log[\frac{1}{x}]] + x$
    $f(x) = Log [\frac{1}{x}] + x$

This is an actual problem I encountered, when we were working on the research study on 2D.


Doing things right
---------------------------------
This issues are well known and of course are . Not only errors go unreported but it is

Let it be Flaky
----------------
So we saw that how to make things better than going floating points and why we should. These reasons compeled me start Flaky, an open-source project project, with following features:

Flaky is written in Go.

The easiest way to play is at the FlakyPastry website: a sandbox for playing with FlakyQuantities.
Please join me and to contribute to




