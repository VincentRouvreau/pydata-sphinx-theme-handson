=============
Generic items
=============

These are the things that don't quite fit into other groupings.

Inline Markup
=============

One of the nice things about markup languages is the ability to have inline
markup. This makes the presentation *much* nicer. The **bold** text shouldn't
be too overbearing. It is very common to have ``inline code`` as well. It is
important to ensure that the inline code doesn't have a line height that is
greater than the regular prose; otherwise the spacing looks weird.

It is also possible to use explicit roles to do things like a :sub:`subscript`,
a :sup:`superscript`, :emphasis:`emphasis`, :strong:`strong`, and
:literal:`literal`.

Hyperlinks
----------

reStructuredText has character-level inline markup too. It's ugly to write, but
someone might be using it, so here's an example: **re**\ ``Structured``\ *Text*.

It is also possible to link to documented items, such as
:class:`api_sample.RandomNumberGenerator`.

Interpreted text
----------------

The default role for "interpreted text" (AKA single backticks) is
`Title Reference`. There are other reference syntaxes as well: :PEP:`287` and
:RFC:`2822`.

If the ``--pep-references`` option was supplied, there should be a live link to
PEP 258 here.

GUI labels
^^^^^^^^^^

According to the RST demo, GUI labels (like :guilabel:`this label`) are a way to
indicate that some action is to be taken by the user. Like inline code literals,
GUI labels should not run over line height.

Keys / Menu labels
^^^^^^^^^^^^^^^^^^

Key-bindings indicate that the read is to press a button on the keyboard or
mouse, for example :kbd:`MMB`, :kbd:`⌘+⇧+M` and :kbd:`Shift-MMB`. Another
useful way is ``menuselection`` to show menus:
:menuselection:`My --> Software --> Some menu --> Some sub menu 1 --> Some sub menu 2 --> Some sub menu 3`

For example, ``menuselection`` should break when it is too long to fit on a
single line.

Long inline code wrapping
^^^^^^^^^^^^^^^^^^^^^^^^^

.. DO NOT RE-WRAP THE FOLLOWING PARAGRAPH!

Let's test wrapping and whitespace significance in inline literals:
``This is an example of --inline-literal --text, --including some--
strangely--hyphenated-words.  Adjust-the-width-of-your-browser-window
to see how the text is wrapped.  -- ---- --------  Now note    the
spacing    between the    words of    this sentence    (words
should    be grouped    in pairs).``

Math
====

This is a test. Here is an equation:
:math:`X_{0:5} = (X_0, X_1, X_2, X_3, X_4)`.
Here is another:

.. math::
    :label: This is a label

    \nabla^2 f =
    \frac{1}{r^2} \frac{\partial}{\partial r}
    \left( r^2 \frac{\partial f}{\partial r} \right) +
    \frac{1}{r^2 \sin \theta} \frac{\partial f}{\partial \theta}
    \left( \sin \theta \, \frac{\partial f}{\partial \theta} \right) +
    \frac{1}{r^2 \sin^2\theta} \frac{\partial^2 f}{\partial \phi^2}

You can add a link to equations like the one above :eq:`This is a label` by using
``:eq:``.


Sidebar
=======

.. sidebar:: Ch'ien / The Creative

    Lorem ipsum dolor sit amet consectetur adipisicing elit.

    .. image:: https://source.unsplash.com/200x200/daily?cute+puppy

    Lorem ipsum dolor sit amet consectetur adipisicing elit.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

Code with Sidebar
-----------------

.. sidebar:: A code example

    With a sidebar on the right.

.. code-block:: python
    :caption: Code blocks can also have captions.
    :linenos:

    print("one")
    print("two")
    print("three")
    print("four")
    print("five")
    print("six")
    print("seven")
    print("eight")
    print("nine")
    print("ten")
    print("eleven")
    print("twelve")
    print("thirteen")
    print("fourteen")
