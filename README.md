# Endoh's quine language (QCLang) in python

QCLang is a language that makes printing out its own source very easy. It turns out that by implementing its interpreter, you can make its implementor a quine just as easily! See [quine.py](quine.py) for details.

Moreover, we can define a language that makes it even easier. What if we make `!` print out the programs own source but quoted? The result is a quine that's simple to understand and write by yourself. See [qsimp.py](qsimp.py) for the resulting program.

See [Endoh's explaination for his quine clique](https://dev.to/mame/quine-clique-51-programs-in-51-languages-that-all-print-each-other-39i0) for more info.
