# Analysis

## Text

The text is chosen from [Google News](https://www.nytimes.com/2019/09/20/us/politics/trump-whistle-blower-ukraine.html).

## Result

Running `python3 stem.py text.txt` gives the following result:

```
to                  to
it                  it
has                 ha                  *
a                   a
also                also
added               ad                  *
mounting            mount               *
investigate         investig            *
know                know
phone               phone
s                   s
complaint           complaint
ridiculous          ridicul             *
for                 for
part                part
question            question
interactions        interact            *
murky               murki               *
the                 the
emerged             emerg               *
amid                amid
shouldn             shouldn
and                 and
dealings            deal                *
call                call
new                 new
at                  at
away                away
told                told
though              though
person              person
even                even
with                with
government          govern              *
least               least
pushed              push                *
ought               ought
have                have
of                  of
acknowledged        acknowledg          *
said                said
political           polit               *
revelation          revel               *
remained            remain              *
country             countri             *
hold                hold
recently            recent              *
t                   t
aid                 aid
on                  on
involve             involv              *
reporters           report              *
waved               wave                *
publicly            publicli            *
brought             brought
increased           increas             *
identity            ident               *
about               about
rival               rival
military            militari            *
but                 but
into                into
had                 had
did                 did
related             relat               *
leaders             leader              *
in                  in
immediately         immedi              *
asked               ask                 *
story               stori               *
partisan            partisan
scrutiny            scrutini            *
dismissed           dismiss             *
that                that
not                 not
up                  up
relationship        relationship
as                  as
attack              attack
connected           connect             *
questions           question            *
look                look
whether             whether
he                  he
his                 hi                  *
during              dure                *
was                 wa                  *
released            releas              *
```

## Analysis

| Stemmed correctly(1) | Stemmed incorrectly(2) | Failed to stem(3) | Stemmed unncessarily(4) |
| :------------------: | :--------------------: | :---------------: | :---------------------: |


|

Words in group (1) are words stemmed correctly.

Since the purpose is not finding the root of the word, but the stem, I put cases like `investigate => investig` into this category, assuming it is trying to reduce `investigation` and `investigate` into the same stem.

Words in group (2) are words stemmed incorrectly.

-   `added` is stemmed into `ad`, which should have been `add`.

This behavior is dictated by the rule

>     (*d and not (*L or *S or *Z))
>        -> single letter
>                                     hopp(ing)    ->  hop
>                                     tann(ed)     ->  tan
>                                     fall(ing)    ->  fall
>                                     hiss(ing)    ->  hiss
>                                     fizz(ed)     ->  fizz

But it should exclude `*D` as well, apart from `*L or *S or *Z`

Words in group (3) turned out to be very rare. The only example I observed is `relationship`, which could arguably be stemmed into `relate` or `relation`, but it is also arguable.

Words in group (4) are words stemmed unnecessarily.
For example, the word `investigate` is stemmed into `investig`, but in fact it doesn't need to be stemmed. This is probably because the algorithm identify

-   Another example is `has`, which is stemmed into `ha`, according to the rule `S=>` in step `1a`.

Below is the same list of words labeled with one of the four categories above:

```
1		to                  to
1		it                  it
4		has                 ha                  *
1		a                   a
1		also                also
2		added               ad                  *
1		mounting            mount               *
1		investigate         investig            *
1		know                know
1		phone               phone
1		s                   s
1		complaint           complaint
1		ridiculous          ridicul             *
1		for                 for
1		part                part
1		question            question
1		interactions        interact            *
1		murky               murki               *
1		the                 the
1		emerged             emerg               *
1		amid                amid
3		shouldn             shouldn
1		and                 and
1		dealings            deal                *
1		call                call
1		new                 new
1		at                  at
1		away                away
1		told                told
1		though              though
1		person              person
1		even                even
1		with                with
1		government          govern              *
1		least               least
1		pushed              push                *
1		ought               ought
1		have                have
1		of                  of
1		acknowledged        acknowledg          *
1		said                said
1		political           polit               *
2		revelation          revel               *
1		remained            remain              *
4		country             countri             *
1		hold                hold
1		recently            recent              *
1		t                   t
1		aid                 aid
1		on                  on
4		involve             involv              *
1		reporters           report              *
1		waved               wave                *
2		publicly            publicli            *
1		brought             brought
2		increased           increas             *
4		identity            ident               *
1		about               about
1		rival               rival
4		military            militari            *
1		but                 but
1		into                into
1		had                 had
1		did                 did
2		related             relat               *
1		leaders             leader              *
1		in                  in
2		immediately         immedi              *
1		asked               ask                 *
2		story               stori               *
1		partisan            partisan
4		scrutiny            scrutini            *
1		dismissed           dismiss             *
1		that                that
1		not                 not
1		up                  up
3		relationship        relationship
1		as                  as
1		attack              attack
1		connected           connect             *
1		questions           question            *
1		look                look
1		whether             whether
1		he                  he
4		his                 hi                  *
4		during              dure                *
4		was                 wa                  *
2		released            releas              *
```
