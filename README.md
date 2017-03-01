**Q**: Why is there need for yet another decompiler, especially a
crippled one?

**A**: A sad truth is that most decompilers out there are crippled. Many
aren't able to decompile trivial constructs, others can't decompile more
advanced, those which seemingly can deal with them, are crippled by
supporting only the boring architectures and OSes. And almost every
written in such a way that tweaking it or adding a new architecture is
complicated. Decompiler is a tool for reverse engineering, but ironically,
if you want to use a typical decompiler productively or make it suit your
needs, first you will need to reverse-engineer the decompiler itself.

How ScratchABlock is different?
-------------------------------

The central part of a decompiler (and any program transformation framework)
is Intermediate Representation (IR). A decompiler should work on IR, and
should take it as an input, and conversion of a particular architecture's
assembler to this IR should be well decoupled from a decompiler, or
otherwise it takes extraordinary effort to add support for another
architecture (which in turn limits userbase of a decompiler).

Decompilation is a complex task, so there should be easy insight into the
decompilation process. This means that IR used by a decompiler should be
human-friendly, for example use a syntax familiar to programmers, map as
directly as possible to a typical machine assembler, etc.

The requirements above should be quite obvious on their own. If not, they
can be learnt from the books on the matter, e.g.:

> "The compiler writer also needs mechanisms that let humans examine the IR
> program easily and directly. Self-interest should ensure that compiler
> writers pay heed to this last point."
>
> (Keith Cooper, Linda Torczon, "Engineering a Compiler")

However, decompiler projects, including OpenSource ones, routinely violate
these requirements: they are tightly coupled with specific machine
architectures, don't allow to feed IR in, and oftentimes don't expose or
document it to user at all.

ScratchABlock is an attempt to say "no" to such practices and develop a
decompilation framework based on the requirements above. Note that
ScratchABlock can be considered learning/research project, and beyond
good intentions and criticism of other projects, may not offer too much
to a casual user - currently, or possibly at all. It can certainly be
criticised in many aspects too.


Down to Earth part
------------------

ScratchABlock is released under the terms of GNU General Public License v3
(GPLv3).

ScratchABlock is written in Python3 language, and tested with version 3.3
and up, though may work with 3.2 or lower too (won't work with legacy
Python2 versions). For unit testing, "nose" package is required:
https://pypi.python.org/pypi/nose (expected executable name is
`nosetests3`).

Source code and interfacing scripts are in the root of the repository.
The most important scripts are:

* apply_xform.py - A central driver, allows to apply a sequence of
transformations (or in general, high-level analysis/transformation
algorithm) to a single file or a directory of files.

* run_tests - Regregression testsuite runner. The Mmajority of
testsuite is high-level, consisting of running apply_xform.py with
different passes on file(s) and checking the expected results.

Other subdirectories of the repository:

* tests_unit - Classical unit tests for Python modules, written in
Python.

* tests - The main testsuite. While integrational in the nature, it
usually tests one pass on one simple files, so follows unit testing
philosophy. Tests are represented as PseudoC input files, while
expected results - as PseudoC with basic blocks annotation and (where
applicable) CFG in .dot format. Looking at these testcases, trying
to modify them and see the outcome is the best way to learn how
ScratchABlock works.

* docs - Growing collection of documentation. Currently there's a
specification of PseudoC assembler language serving as intermediate
representation (IR) for ScratchABlock and a survey why another
existing IR was not selected.
