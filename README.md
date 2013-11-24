This is my personal website: borzov.ca.

I wrote a tiny static generator tailored for my own goals. Kinda overkill, and probably could have spent my time better but hey it happened.


### How to run that shitty static generator of yours, Peter?

Why, thank you for asking!

It uses 'markdown2' library to parse the original articles written in Markdown and uses as a 'pystache' simple template language. So first, we need to install these:

    pip install markdown2 pystache

Now we run the file 'src/collect.py' and point to the Markdown file (*.md) in question as an argument:

    python src/collect.py flaky.md

Tadah, we get the 'flaky.html' file as the result in the root directory. Piece of cake really.

