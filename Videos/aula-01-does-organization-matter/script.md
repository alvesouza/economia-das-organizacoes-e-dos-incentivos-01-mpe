---
tags: [video, aula-01, explainer, script]
date: 2026-10-09
slug: aula-01-does-organization-matter
---

# Narration — Aula 1: Does Organization Matter? Ford × GM × Toyota

Spoken register: every symbol said in words. `[pause]` marks a silence realised as held frame
time in `scenes.py` (Speechify ignores intra-clip silence). Every historical number is sourced in
`provenance.md`; every stylized number is recomputed by `check_numbers.py`.

---

## BeatOpen - 95 s

Fremont, California. A car plant on the east side of San Francisco Bay.

In 1982, General Motors closed it. It was one of the worst plants GM had. Cars with defects
kept moving down the line, on the understanding that somebody would fix them later. And on some
mornings so many workers stayed home that the line could not even be started.

[pause]

Two years later, in 1984, the plant reopened. Same building. Now it was a joint venture between
General Motors and Toyota, called NUMMI. And more than eighty-five per cent of its first
workforce were the very people GM had laid off.

[pause]

By 1987, a comparable GM plant needed thirty-one hours of assembly work to build a car. NUMMI
needed nineteen. The GM plant had a hundred and thirty-five assembly defects for every hundred
cars. NUMMI had forty-five. The same as Toyota's best plant in Japan.

[pause]

Same building. Same people. Same union. Nothing about the workers had changed. Something else
had.

And here is the part that should bother you. General Motors owned half of this plant. Its
managers could walk the floor every day. And for years it could not make the same thing happen
in its own factories.

If you can see it, why can't you copy it?

That is the question of this class. And by the end of it, you will be able to answer it with
two lines of mathematics.

## BeatFordFacts - 120 s

To answer it, we have to go back to the start of the car industry, and to the firm that
invented mass production.

In 1908, Ford launched the Model T, at about eight hundred and fifty dollars.

In 1913, at its Highland Park plant in Detroit, Ford began moving the work to the worker instead
of the worker to the work. First small parts, then engines, and in August of that year, the
whole chassis, carried along a line past a row of workers, each doing one small task as it went
by.

[pause]

Here is what that did. Under the old method, a chassis was built standing still, in about
twelve and a half hours of work. By early 1914, on the moving line, it took ninety-three
minutes.

Twelve and a half hours, down to about an hour and a half. Roughly eight times less labour for
the same chassis.

[pause]

And the price followed. By the middle of the 1920s, a Model T cost two hundred and sixty
dollars. Less than a third of the launch price.

[pause]

Now, it is tempting to file all this under technology. Ford found a better machine, and that is
the end of the story. But a moving line is not a machine you buy. It is a way of organising
work: who does what, in what order, at what pace, with what tools.

And it only works under conditions. You need to make the same car, over and over again. You
need parts that fit without filing, every single time. You need workers willing to repeat one
motion all day. And above all, you need volume.

So the first question to ask of Ford is not why the line was faster. It is: when does a line
pay at all? That is a calculation. Let us do it.

## BeatScale - 140 s

Two ways of building chassis. The old way, standing still, and the line.

Write C nought of q for the total cost of building q chassis a year the old way. It is a fixed
cost, F nought, plus a cost per chassis, c nought, times q.

The line has its own fixed cost, F L, and its own cost per chassis, c L. The line costs more to
set up, so F L is bigger than F nought. But each chassis is cheaper, so c L is smaller than c
nought.

[pause]

Divide each total cost by q, and you get average cost: the fixed cost spread over the volume,
F over q, plus the cost per chassis. Both curves fall as volume rises, because the fixed cost is
spread thinner. The line's curve starts higher and ends lower.

So where do they cross? The line is cheaper when F L over q, plus c L, is less than F nought
over q, plus c nought.

Move the per-chassis costs to one side and the fixed costs to the other: the difference in
fixed costs, over q, must be less than the saving per chassis, c nought minus c L.

Both sides are positive, so multiply through by q and divide by the saving. The line is cheaper
exactly when q is greater than q bar: the extra fixed cost, divided by the saving per chassis.

[pause]

Put numbers on it. The saving is about eleven labour hours per chassis. Suppose, purely for
illustration, that the line's extra fixed cost is about one point one million labour hours a
year. Then q bar is a hundred thousand chassis a year. Below that, the line loses money.

[pause]

And now notice the loop. Volume is not handed to Ford; it depends on the price. The price
depends on cost. Cost depends on having the line. And the line only pays at volume.

The line needs volume, volume needs a cheap car, and a cheap car needs the line. These are
choices that pay only together. Hold on to that sentence. It is the whole class in miniature.

## BeatFiveDollar - 155 s

The line had a cost that does not show up in that equation.

The work became monotonous. Each worker repeated one motion, all day, at the pace of the line.
And workers voted with their feet. In 1913, labour turnover at Ford reached three hundred and
seventy per cent: for every job on the payroll, Ford was hiring almost four people a year.

On a moving line, that is ruinous. A missing or untrained worker holds up everyone downstream.

[pause]

In January 1914, Ford announced the five dollar day: roughly double the going wage. Most of it
came as a bonus, paid to workers who met the company's rules of conduct.

Why would a profit maximiser pay double? Here is the economics. What the firm cares about is not
the wage, but the cost of a unit of effective work. Write e of w for effort per worker, which
rises with the wage w. The firm minimises w over e of w.

[pause]

Differentiate with respect to w, using the quotient rule: e of w, minus w times e prime of w,
all over e of w squared. Set it to zero.

The denominator is positive, so the numerator must vanish: e equals w times e prime.

Divide both sides by e. The elasticity of effort with respect to the wage, e prime times w over
e, equals one. This is the Solow condition: raise the wage until one per cent more pay buys
exactly one per cent more effort.

[pause]

An illustration, not a calibration. Let effort be the square root of w minus w nought, where w
nought is what the worker could earn elsewhere. The condition gives w minus w nought equals w
over two, so the best wage is twice the outside wage. With an outside wage of two dollars fifty,
the best wage is five.

And turnover fell: to fifty-four per cent in 1914, and sixteen per cent in 1915. Economists still
argue about Ford's motive; Raff and Summers read it as exactly this, an efficiency wage.

[pause]

But here is the point for today. The line made the jobs monotonous, and monotony made a high
wage pay. The wage decision is not separate from the line decision. That is our first sighting
of a complementarity. Incentive pay comes back in Aulas thirteen to sixteen.

## BeatFordSystem - 135 s

So let us write down Ford's choices, not as a list of good ideas, but as a system. Think of an
organisation as a point in a space of designs, with one coordinate for each choice. Ford chose a
very particular point.

Product: one model. Ford later wrote that a customer could have a car painted any colour he
wanted, so long as it was black.

Machines: dedicated. Each one built to make one part of one car, and nothing else.

Process: the moving line.

Jobs: narrow. One motion, learned in minutes.

Pay: high. The five dollar day.

Parts: made in-house, more and more of them, so that every piece arrives exactly to
specification, and fits without filing.

[pause]

Now read the table from the bottom up, and look at how each row props up the others.

Parts that fit every time are what let an unskilled worker fit a part in one motion. Dedicated
machines only pay if there is one model to make, at huge volume. One model is what makes narrow
jobs possible: the same motion, on the same part, all day. Narrow jobs are what make the line
possible. The line makes the jobs monotonous, and so needs the high wage. And the high wage only
pays because the line makes each worker so productive.

Take out any one row and the others start to fail. Give Ford three models, and each set of
dedicated machines runs at a third of the volume it was built for. Pay the old wage, and the
line runs with a workforce that turns over almost four times a year.

[pause]

Here is the name we will use: a coherent system. A set of choices, each of which is the best
response to all the others.

This system was a brilliant answer to a particular problem: millions of first-time buyers who
wanted a car, any car, as cheaply as possible.

So here is the next question. What happens to a perfect answer when the question changes?

## BeatGMFacts - 110 s

By the 1920s the question had changed. But look first at where General Motors stood. In 1921,
the Model T alone held fifty-five per cent of the American car market. All of GM's brands
together held eleven per cent.

A growing share of buyers already owned a car. They were not buying their first car. They were
replacing one.

Think about what a replacement buyer is paying for. She already has transportation. What she
buys now is the difference between her old car and the new one: more comfort, more power, more
style. She cares, a great deal, about getting a car that is different.

General Motors, under Alfred Sloan, answered that buyer.

[pause]

First, a ladder of brands, arranged by price, from Chevrolet at the bottom to Cadillac at the
top. GM's own phrase was a car for every purse and purpose.

Second, a new model every year, so that style itself became a reason to buy.

Third, credit. In 1919 GM set up its own finance company, so buyers could pay in instalments.
Credit brought in buyers who could not pay the whole price at once. It made the market bigger.

[pause]

Ford held on to the Model T for years. In 1927 it finally gave up: production stopped from May
until November while the plants were retooled for the new Model A. Six months without a car to
sell. And by the end of the 1920s, General Motors was selling more cars than Ford. By 1940, Milgrom
and Roberts report, GM held forty-five per cent of the market, and Ford sixteen.

[pause]

Notice what did not happen. GM did not beat Ford by building the Model T more cheaply. Nobody
could. It beat Ford by answering a different question. Buyers who care about difference, and a
bigger market: keep those two changes in mind. To see what they do, we need one formula. How many
models should a firm make?

## BeatVariety - 140 s

Here is a deliberately simple model. Not of the car market, but of one firm's decision.

The firm sells q cars a year, and chooses n, the number of different models, at least one.

Every model has a fixed cost, F. Its own design, its own dies and tooling.

More models means each buyer finds a car closer to what she wants, so she pays more. Write the
price as p bar plus a times the natural log of n. The parameter a measures how much buyers care
about finding the right car. The logarithm says that each extra model adds less than the last.

[pause]

Profit, capital pi of n, is volume times the margin, q times p bar plus a log n minus c, minus
n times F for the models.

Differentiate with respect to n. The constants vanish, and the derivative of log n is one over
n. So capital pi prime of n is q a over n, minus F.

Set it to zero at the optimum, n star: q a over n star equals F.

Multiply both sides by n star and divide by F. The number of models is n star equals a q over
F.

[pause]

Is it a maximum? The second derivative is minus q a over n squared. Negative, for any n. So the
profit curve is concave, and the turning point is the top.

One more case. The firm cannot make fewer than one model. If a q over F is less than one, the
derivative at n equals one, q a minus F, is already negative. Every extra model loses money,
and the best you can do is the corner: n star equals one.

[pause]

Read the formula out loud. The number of models equals the taste for variety, times the size of
the market, divided by the fixed cost of a model.

And now look at Ford's world. First-time buyers who wanted any car: a close to zero. Dedicated
machines: F enormous. a q over F is far below one.

Ford's one model was not a whim. It was the corner solution.

## BeatVarietyStatics - 135 s

Now let the world move, and differentiate the answer.

With respect to a, the taste for variety: the derivative of n star is q over F. Positive.

With respect to q, the size of the market: a over F. Positive.

With respect to F, the fixed cost of a model: minus a q over F squared. Negative.

[pause]

Take logs, and the whole table fits in one line: log n star equals log a, plus log q, minus log
F. Every elasticity is one in size. Ten per cent more taste for variety, or ten per cent more
market, means ten per cent more models. A ten per cent cut in the cost of a model does the same.
With a equal to two, q equal to fifty and F equal to twenty-five, n star is four. Halve F, and n
star doubles to eight.

[pause]

Put the three firms on that table.

The 1920s raised a, through replacement buyers, and raised q, through credit. a q over F crossed
one, and the optimum left the corner. That is GM's ladder.

Now Toyota, after the war. Its market was small, so q was small. By this formula a small firm in
a small market should make very few models. But the Japanese market wanted many different
vehicles in small numbers. The only way to make many models at low volume is to attack the
denominator: to make F small. Cheap, fast changeovers from one model to the next.

So the same formula orders the three firms. Ford sits at the corner. GM rides a and q. Toyota
cuts F.

[pause]

One more derivative, and this is the one to remember. Take the marginal profit of a model, q a
over n minus F, and differentiate it with respect to a. You get q over n. Positive. The extra
profit from one more model is higher when buyers value variety more.

A choice whose return rises with another variable. Keep that sign. In Act Four, it gets a name.

## BeatMForm - 115 s

Variety brought a second problem, and this one is about organisation.

Ford's company was run as one great operation, with decisions taken at the top. With one model,
that can work. There is one thing to decide about. Henry Ford mocked organisation charts: the
genius for organisation, he wrote, results in the birth of a great big chart, on which a message
takes about six weeks to travel from a man at the lower left-hand corner up to the president.

With five brands, each with its own customers, its own prices and its own yearly redesign,
nobody at the top can know enough about all of them.

[pause]

GM's answer, under Sloan, was to organise by division. Each division ran its own product line:
design, production, sales. The central office kept the money. It allocated capital between
divisions, set financial targets, and measured each division's return.

Decentralised operations, centralised financial control. The business historian Alfred Chandler
called it the multidivisional form, and it became the template for the large corporation. The
structure that looked so cumbersome to Henry Ford made GM a fearsome competitor: from 1927 to
1937, Ford lost two hundred million dollars, while GM earned over two billion.

[pause]

Here is the logic in one line. Each product line generates its own stream of information: its
customers, its costs, its rivals. With n lines, the top of the firm would have to absorb n
streams; a division absorbs one. What the centre cannot hand over is the allocation of money
between divisions, because every division will always ask for more. So the centre keeps the
money, and judges each division by its return.

[pause]

Look at what happened. When n went up, the structure had to change with it. Many product lines
and divisional decision making are chosen together. A firm with GM's ladder and Ford's single
command would drown in decisions; a firm with Ford's single model and GM's divisions would have
nothing for its divisions to do.

The same pattern as Ford's table: choices that only make sense as a set. How to divide decisions
between a centre and its units is the subject of Aula seven. Today we only need the pattern.

## BeatToyota - 120 s

After the Second World War, Toyota faced almost the opposite of Ford's situation. A small home
market. Demand for many different vehicles in small numbers. And very little capital: no money
for Ford's dedicated machines, and no money to tie up in mountains of inventory.

Over the decades after the war, Toyota, led on the shop floor by Taiichi Ohno, built a different
system.

[pause]

One. Just in time. Each station produces only what the next station has asked for, signalled by
a card, a kanban. Production is pulled by the next station's request, not pushed by a schedule
from above. Almost no inventory sits between stations.

Two. Quick changeovers. A press can be switched from one part to another fast enough that small
batches pay.

Three. Any worker can stop the whole line when he sees a defect, by pulling a cord. The andon.
The point is not to stop the line. It is that a stopped line forces the cause of the defect to be
found and removed, instead of passed on.

Four. Workers in multi-skilled teams, who rotate jobs and are expected to solve problems, not
only to repeat motions.

Five. A few suppliers, kept for the long term, who share information with the plant.

Milgrom and Roberts add two details. Toyota trained its machine operators to repair their own
equipment; in the United States repair was a separate job, and an operator stood waiting for the
specialist. And because its equipment was flexible, Toyota redesigned its cars about twice as
often as GM, which in the 1950s and 1960s made a major redesign only about once every twelve
years.

[pause]

Now look at each one through Ford's eyes. No inventory? Then any hiccup stops the line. Let
workers stop the line? You are throwing away output. Depend on a handful of suppliers? You are
at their mercy.

Each practice, taken alone, looks like a mistake.

The industrial economist Luis Cabral puts the puzzle well. For many years, Toyota's procurement
system was considered clearly superior to its rivals'. However, the system involved so many
different aspects that it was difficult to pin down what the crucial success factors were.

## BeatTwoProblems - 125 s

Before we compare the three systems, let us name what each of them was doing. Strip away the
cars, and every organisation is solving two problems.

The first is coordination. Thousands of people, each knowing a small piece of the picture, must
do the right things, at the right time, in the right quantities, so that their pieces fit.

At Ford, the line itself coordinates: its speed sets everyone's pace, and with one model there is
almost nothing to decide. At GM, the centre coordinates money, and each division coordinates its
own product. At Toyota, a card travelling back up the line tells each station what to make next.

[pause]

The second is motivation. Each of those people has their own interests. They must want to do
what the plan needs: to show up, to keep the pace, to report the defect instead of passing it on.

At Ford, the five dollar day. At GM, divisions judged, and their managers rewarded, by their
return on capital. At Toyota, teams responsible for their own quality, and long-term employment
that makes it safe for workers to improve the very process they work in.

[pause]

Coordination is about information: who knows what, and how it reaches whoever decides.
Motivation is about interests: who wants what, and how to line it up with what the organisation
needs.

These two words are not a definition to memorise. They are where the three cases lead. And they
organise this whole course. Aulas six to eight are about coordination, by markets and by
management. Aulas nine to sixteen are about motivation: contracts, private information, adverse
selection, moral hazard and incentives.

[pause]

And notice: in every system, the coordination choices and the motivation choices fit each other.
Milgrom and Roberts say it in one line: incentives and delegated authority are complements.
Toyota can let anyone stop the line only because its workers are motivated to stop it for good
reasons. That fit is what the rest of today is about.

## BeatThreeSystems - 100 s

Three firms, one industry. Let us put them side by side, in broad strokes: this is a caricature
of each system, not an inventory.

Products: Ford makes one model. GM a ladder of brands. Toyota many models, in small batches.

Machines: Ford's are dedicated to one car. GM's are specialised for components shared across
many models. Toyota's are flexible, and change over fast.

Inventory: Ford and GM hold buffers, so a problem in one place does not stop another. Toyota
holds almost none.

Jobs: narrow at Ford and GM. Broad, and rotating, at Toyota.

Who may stop the line: at Ford and GM, managers. At Toyota, anyone.

Suppliers: Ford makes its own. GM buys from many, at arm's length. Toyota keeps a few, for
years.

Read the table down a column and it hangs together. Read it across a row and you see three
different answers to the same design question. That is the difference between a list of
practices and a system: in a system, the columns matter more than the rows.

[pause]

Three coherent systems. Each is an answer to its own environment: to a, to q, and to F.

And by the 1980s, as Fremont showed, Toyota's system was beating GM's on GM's own ground.

So the obvious move for GM is to take the best practices from the right-hand column and adopt
them, one at a time. Start with the one that looks most valuable. Then the next.

That is exactly what most managers would do. And it is wrong. Let us see why, by doing it
carefully.

## BeatWrongAttempt - 115 s

Write a firm's organisation as a list of practices, x one to x n, each one either zero, not
adopted, or one, adopted. And write pi of x for the profit it earns.

Now here is the assumption hiding inside the phrase best practices. Profit is pi nought, plus
the sum over all practices of v i times x i. Each practice adds its own value, v i, whatever
else the firm is doing.

[pause]

Under that assumption, compute the gain from adopting practice i. Profit with x i equal to one,
minus profit with x i equal to zero. Every other term cancels, and the gain is just v i.

It does not depend on anything else. So adopt every practice with positive v, in any order you
like, and every single step pays. Copying a system one piece at a time works perfectly.

[pause]

Now test it. Imagine a GM plant that adopts just in time, and only just in time. It throws away
its inventory buffers. But its suppliers still deliver late, and its workers are not trained to
find and fix problems. So every late delivery and every defect now stops the line, because there
is no buffer left to absorb it. Profit falls.

Now imagine the same just in time in a plant with reliable suppliers and problem-solving teams.
There, it removes cost and exposes defects early. Profit rises.

[pause]

The same practice. Two opposite values. The value of just in time depends on what else the
plant does.

And that dependence is precisely what the additive formula sets to zero. The mistake is not in
the arithmetic. It is in the plus sign.

So let us replace the plus sign with something true, and see what it implies.

## BeatIncreasingDiff - 140 s

Take two practices. x is just in time, y is problem-solving teams. Each is zero or one. So the
firm has four possible organisations, and here are illustrative profits, measured from where it
stands today.

Neither: zero. Just in time alone: minus two. Teams alone: minus one. Both: plus five.

[pause]

First, the gain from adopting x when y is zero: f of one zero, minus f of zero zero. Minus two.
A loss.

Second, the gain from adopting x when y is one: f of one one, minus f of zero one. Five minus
minus one. Plus six.

The same practice is worth minus two in one organisation and plus six in another. The difference
between the two, eight, is the cross effect. In the additive world it is zero.

[pause]

Now the definition, arriving as the answer. x and y are complements when the gain from x is at
least as large when y is present: f of one one minus f of zero one, greater than or equal to,
f of one zero minus f of zero zero. This is called increasing differences.

Add f of zero one and subtract f of one zero on both sides. You get f of one one minus f of one
zero, greater than or equal to, f of zero one minus f of zero zero. The gain from y is larger
when x is present. Here, seven against minus one. Complementarity is symmetric.

Now rearrange once more, putting the corners together. f of one one plus f of zero zero, greater
than or equal to, f of one zero plus f of zero one. Both plus neither beats one of each. Five
against minus three. This form is called supermodularity.

[pause]

For whole vectors of practices, write the join, the component-by-component maximum, and the
meet, the minimum. The same inequality reads: f of the join plus f of the meet is at least f of
x plus f of y.

Three ways of writing one idea. Doing more of one thing raises the return to doing more of the
other.

## BeatCrossPartial - 115 s

Many organisational choices are not zero or one. How much inventory, how many models, how much
training. So let us take the same idea to continuous choices.

Increase x by a small amount h and y by a small amount k, both positive.

Increasing differences says: the gain from raising x, with y raised, f of x plus h, y plus k,
minus f of x, y plus k, is at least the gain from raising x with y where it was, f of x plus h,
y, minus f of x, y. Their difference is greater than or equal to zero.

[pause]

Divide everything by h times k. Since both are positive, the inequality keeps its direction.

Now let h shrink to zero. Each difference over h becomes a partial derivative with respect to x.
What is left is f x at y plus k, minus f x at y, all over k, greater than or equal to zero.

Now let k shrink to zero. That is the derivative of f x with respect to y. The cross partial, f
x y, greater than or equal to zero.

And for smooth functions it works backwards too: if the cross partial is never negative,
integrating it gives back increasing differences.

[pause]

Three checks. f equals x times y: the cross partial is one. Complements.

f equals x plus y: the cross partial is zero. That is the additive world of the wrong first
attempt, where nothing depends on anything else.

And our variety model. The cross partial of capital pi with respect to n and a was q over n.
Positive. The number of models and the taste for variety were complements all along. That is
the sign we kept from Act Two.

## BeatSubstitutes - 130 s

Not every pair of practices is complementary. Take two ways of protecting a line from trouble.
One is inventory: buffers of parts between stations, so that when one station stops, the next
keeps working. The other is problem solving: workers trained, and allowed, to find the cause of
a stoppage and remove it.

With big buffers, a stoppage does little damage, so fast problem solving is worth little.
Without buffers, every stoppage halts the plant, and problem solving is worth a great deal. More
of one lowers the return to the other. The cross partial is negative. These are substitutes.

[pause]

Do we need a second theory for substitutes? No. Here is the trick, written out.

Let f of x and y have a cross partial f x y less than or equal to zero.

Define a new variable, z equals minus y. If y measures how much problem solving you do, z
measures how little.

Write g of x and z equals f of x and minus z.

By the chain rule, differentiating with respect to z brings out the derivative of minus z,
which is minus one. So g x z equals minus f x y.

And minus a non-positive number is non-negative. x and z are complements.

[pause]

So everything we prove about complements applies to substitutes, with one variable turned
upside down. In words: inventory, and the absence of problem solving, are complements. So are
low inventory and a lot of problem solving.

Ford's plant, with big buffers and narrow jobs, is one coherent combination. Toyota's, with
almost no buffers and teams that remove causes, is the other. What is incoherent is the mixture:
big buffers with skilled problem solvers who have nothing to fix, or no buffers with workers who
are not allowed to fix anything.

Which is the wrong first attempt again, seen from a new angle. Read an organisation pair by
pair, not practice by practice.

## BeatTopkis - 130 s

Now the payoff. Why do complements move together?

Take a firm choosing x to maximise f of x and t, where t is something the firm does not choose:
a feature of its environment, like the taste for variety. Assume f is smooth, and strictly
concave in x, so f x x is negative.

[pause]

At the optimum x star of t, the first-order condition holds: f x, evaluated at x star of t and
t, equals zero. And it holds for every value of t.

So differentiate both sides with respect to t. The chain rule gives two terms: f x x times the
derivative of x star with respect to t, plus f x t. And the right-hand side is still zero.

Solve for the derivative: d x star d t equals minus f x t over f x x.

[pause]

Now read the signs. The denominator, f x x, is negative: that is the second-order condition. The
numerator, f x t, is greater than or equal to zero: that is increasing differences between the
choice and the environment. Minus a non-negative number over a negative number is non-negative.

So if the environment raises the return to x, the optimal x rises. Always.

Check it on the variety model. f n a is q over n, f n n is minus q a over n squared. Minus their
ratio is n over a, which at n star equals q over F. The same answer we got by differentiating
the formula directly.

[pause]

This argument used derivatives and concavity. In 1978 Donald Topkis proved that neither is
needed. If the objective has increasing differences in the choice and the parameter, the best
choices are non-decreasing in the parameter, for whole lattices of choices at once.

In 1990, Milgrom and Roberts used this result to explain exactly our story: the move from Ford's
mass production to flexible manufacturing. Not one practice changing, but all of them, together.

## BeatTwoChoices - 135 s

Let us see two complementary choices move together, with every line written out.

Profit is t x, plus s y, plus b x y, minus c over two x squared, minus c over two y squared.

Read the terms. x is, say, flexibility; t is how much the environment rewards it. y is worker
skill; s is its own direct return. b, positive, is the complementarity: the cross partial of
this function is exactly b. And the squared terms say each choice gets more expensive the more
you do of it.

[pause]

First-order condition for x: t plus b y minus c x equals zero.

First-order condition for y: s plus b x minus c y equals zero.

Solve the second for y: y equals s plus b x, all over c.

Substitute that into the first: t, plus b times s plus b x over c, minus c x, equals zero.

Multiply through by c: c t plus b s plus b squared x minus c squared x equals zero.

Collect the x terms: x times c squared minus b squared equals c t plus b s.

Divide: x star equals c t plus b s, over c squared minus b squared.

[pause]

Now go back for y. Put x star into y equals s plus b x over c, and bring everything over the
common denominator. The b squared s terms cancel, a c comes out of the numerator, and y star
equals c s plus b t, over c squared minus b squared.

[pause]

One condition remains. For this to be a maximum, the matrix of second derivatives must be
negative definite. Its diagonal is minus c, which is negative. Its determinant is c squared minus
b squared, which must be positive. So c must be greater than b.

In words: the complementarity cannot be stronger than the rising cost of each choice. If it
were, doing more of both would pay forever, and there would be no optimum at all. That is also
what keeps the denominator of both formulas positive.

## BeatMultiplier - 135 s

Now change the environment. Raise t, the reward to flexibility, and differentiate both closed
forms.

The derivative of x star with respect to t is c over c squared minus b squared. Positive.

The derivative of y star with respect to t is b over c squared minus b squared. Also positive.

And look at that second one carefully. t does not appear anywhere in the first-order condition
for y. Nothing in the environment pushed on worker skill. And yet it rises. It rises because x
rose, and y is x's complement.

[pause]

Compare with a world without complementarity: set b to zero. Then x responds by one over c, and
y does not respond at all.

Divide the two responses of x. c over c squared minus b squared, against one over c, is c squared
over c squared minus b squared. Divide top and bottom by c squared: one over one minus b over c,
squared.

And since b is less than c, that is a geometric series: one, plus b over c squared, plus b over c
to the fourth, and so on.

[pause]

Here is what the series means, on the picture. These are the two best-response lines: x as a
function of y, and y as a function of x. Raise t, and the x line shifts. x rises by one over c.
That raises the best y, a little. That raises the best x again, by a smaller step. And again.
A staircase, each step b over c squared times the last, converging to the new crossing.

The ping-pong between the two lines is the systems effect. Milgrom and Roberts describe exactly
these rounds: each increase raises the marginal return to the others, possibly leading to another
round of increases.

[pause]

With c equal to two, b equal to one and s equal to one, raise t from one to three. x star goes
from one to seven thirds, and y star from one to five thirds. Without complementarity, x would go
from a half to one and a half, and y would stay at a half. The system moves four thirds as far.

## BeatEvidence - 125 s

Is all this a tidy story, or is it true? How would you test it?

Complementarity makes two predictions you can take to data.

The first: complementary practices should be adopted together. Firms that have one should tend to
have the others.

The second is sharper. Run a regression of productivity on two practices and their product: y
equals beta nought, plus beta one x, plus beta two z, plus beta three x times z, plus an error.

[pause]

Now compute the effect of x, line by line. When z is zero, switching x on adds beta one. When z
is one, it adds beta one plus beta three. The difference is beta three.

So beta three is the cross effect: the regression version of the double difference, and of the
cross partial. Complementarity predicts that beta three is positive. And the additive world of
best practices predicts that it is zero.

[pause]

The classic test is a study of steel finishing lines by Casey Ichniowski, Kathryn Shaw and
Giovanna Prennushi, published in 1997. Thirty-six lines, owned by seventeen companies, all doing
nearly the same job with nearly the same machines.

Some lines used a bundle of innovative practices together: incentive pay, teams, flexible job
assignments, employment security and training. Others kept narrow jobs, strict work rules and
hourly pay.

The result: lines with the whole bundle were clearly more productive. And individual practices
adopted in isolation had no effect on productivity at all.

[pause]

One warning, because it is the kind of mistake this course trains you to catch. The first
prediction alone proves little. Practices can be adopted together because some unobserved factor,
a good plant manager, say, raises the value of all of them at once. Correlated adoption is
consistent with complementarity; it is not proof of it. The interaction term, measured on
comparable units, is the stronger test.

## BeatCube - 150 s

Now back to practices that are adopted whole: zero or one. Three of them. J, just in time. T,
teams with authority to stop the line. S, a few long-term suppliers.

Three yes-or-no choices make eight organisations: the corners of a cube. Ford's mass production
sits at the bottom corner, zero zero zero. The full Toyota system at the top, one one one.

[pause]

Here is an illustrative profit, measured as an index, with Ford's corner at ten. Ten, minus four
J, minus two T, minus S, plus four J T, plus five J S, plus two T S, plus two J T S.

Read the coefficients as stories. Minus four: just in time alone exposes the line to every late
delivery. Minus two: teams alone are skilled people with little to fix. Minus one: a few
suppliers alone gives up the pressure of competition. Plus five: reliable suppliers make just in
time safe. Plus four: without buffers, problem solvers have plenty to do.

Put it on the cube, corner by corner. Ford's corner: ten. Just in time alone: six. Teams alone:
eight. Suppliers alone: nine. Just in time and teams: eight. Just in time and suppliers: ten.
Teams and suppliers: nine. All three: sixteen.

[pause]

Is it supermodular? Check the pair J and T, line by line.

The gain from J when T is one: pi of one one S, minus pi of zero one S. That is eight plus eight
S, minus eight plus S. Seven S.

The gain from J when T is zero: pi of one zero S, minus pi of zero zero S. Six plus four S, minus
ten minus S. Minus four plus five S.

Their difference is four plus two S. Positive, whatever S is. The same check gives five plus two
T for J and S, and two plus two J for T and S. Every pair is complementary. The function is
supermodular.

[pause]

So the full system is the best organisation on the cube. Sixteen against ten.

Now stand at Ford's corner and look at your three possible first steps. Just in time alone: six.
Teams alone: eight. Suppliers alone: nine. Every one of them is below ten.

A supermodular function. And every first step loses money.

## BeatValley - 120 s

Maybe the order matters. Let us try every path from Ford's corner to Toyota's, one practice at a
time. There are six orders.

J, then T, then S: ten, six, eight, sixteen.

J, then S, then T: ten, six, ten, sixteen.

T, then J, then S: ten, eight, eight, sixteen.

T, then S, then J: ten, eight, nine, sixteen.

S, then J, then T: ten, nine, ten, sixteen.

S, then T, then J: ten, nine, nine, sixteen.

[pause]

Every path dips below ten. The best of them, starting with suppliers, still drops to nine before
it climbs. There is a valley between the two systems, and every road crosses it.

The deepest road starts with just in time: six, a fall of forty per cent in this index. And even
the roads that recover early, like suppliers then just in time, only climb back to exactly where
they started before they gain anything. Every road asks the firm to pay first, for a quarter, a
year, a budget cycle, with nothing to show for it.

[pause]

Here is why this is not bad luck in the numbers. Increasing differences says the gain from a
practice can only grow as its complements are added. Write it out: the gain from adding
practice i to any organisation x is at least its gain when added to nothing. The stand-alone
gain is the smallest gain a practice ever has.

And where does a firm stand when it evaluates its first change? At its old corner, where every
complement of the new practice is missing. At the one place where each practice is worth the
least. Complementarity does not prevent the valley. It creates it.

[pause]

Topkis told us the best choices move together. He never promised that the road between them is
uphill.

## BeatTwoPeaks - 110 s

Let us make that precise. Call an organisation a local optimum if no single change, adopting or
dropping one practice, raises profit. And a global optimum if no organisation at all does better.

Check Ford's corner. Its three neighbours are six, eight and nine. All below ten. Ford's corner
is a local optimum.

Check Toyota's corner. Its neighbours, dropping one practice at a time, are nine, ten and eight.
All below sixteen. A local optimum too, and the global one.

[pause]

Two peaks on one function. Both coherent: at each, every practice is the best response to the
others. And between them, the valley. Milgrom and Roberts use the same image for a richer case:
a profit surface like a mountain with three peaks, any of which might be the highest.

[pause]

Now think about the tool a firm normally uses to improve: marginal analysis. Evaluate each change
on its own, adopt it if it pays. At a local optimum that tool gives the same answer every time:
change nothing. Marginal analysis cannot tell a local peak from the global one.

The right comparison is between packages: the profit of the whole Toyota corner, minus the profit
of the whole Ford corner. Sixteen minus ten, plus six. Against that, the best single step,
suppliers alone, is nine minus ten: minus one. The package says go. Every step says stop.

[pause]

That is why organisational change is lumpy. Why it so often arrives with a new plant, a new
leader or a crisis. Why benchmarking one practice at a time so often disappoints. Not because
managers are foolish. Because they are doing marginal analysis on a function with two peaks.

A firm that judges every change by its own profit never starts the climb. The change has to come
whole. Or from a partner who brings the entire system at once.

## BeatNUMMI - 130 s

Which brings us back to Fremont.

Remember who these workers were. A union official who helped rehire them later called the old
Fremont crew the worst workforce in the American car industry. Those were the people Toyota
hired back.

Toyota did not ask the old GM workforce to adopt one practice, measure the result, and then
consider the next. It brought the whole system at once: just in time, the teams, the cord, the
training. On the cube, that is not a walk along the edges. It is a jump, straight from one corner
to the other.

[pause]

And the results we started with. Assembly hours per car: thirty-one at a comparable GM plant,
nineteen at NUMMI, sixteen at Toyota's Takaoka plant in Japan. Defects per hundred cars: a
hundred and thirty-five, forty-five, and forty-five.

[pause]

GM's managers learned a great deal at NUMMI. Under GM's later leadership the company tried to
spread the Toyota system to its other plants, and those efforts proved largely unsuccessful. By
the late 1990s GM still had not managed to bring lean production to the rest of its plants in the
United States.

On the cube, those are the red paths. Each plant adopts something, measures it, and finds itself
in the valley.

[pause]

There is a coda that matters to us. GM managers who had been trained at NUMMI did succeed in
introducing the approach in GM's unionised factories in Brazil. New plants, new teams, the whole
system at once. A jump, not a walk.

NUMMI itself ended after GM's bankruptcy. GM pulled out of the venture in 2009, and on the first
of April 2010 the plant built its last car, a red Toyota Corolla.

[pause]

Cabral explains the difficulty of copying with causal ambiguity: too many factors to know which
ones matter. That is real. But the cube says something stronger. Even a rival who knew every
factor, and the exact value of every one, would lose money adopting them one at a time.

## BeatClose - 115 s

So, does organisation matter?

At Fremont, the same people, building cars under two systems, differed by more than half in
hours per car and by three to one in defects. Yes. It matters.

Today you derived five results. A moving line pays above q bar: the extra fixed cost over the
saving per car. An efficiency wage sets the elasticity of effort to one. The number of models is
a q over F. A choice rises with its environment at the rate minus f x t over f x x. And two
complements respond with a multiplier of one over one minus b over c squared.

And now we can say why a good organisation is so hard to copy, in two lines.

[pause]

One. Complements move together. When the environment favours one practice, all its complements
follow, and further than any one of them would alone.

Two. The road between two coherent systems runs through a valley, because a practice is worth
the least exactly where its complements are missing.

[pause]

Here is the picture to keep. The cube. Ford's corner at the bottom, ten. Toyota's at the top,
sixteen. The red paths along the edges, every one dipping below ten. And one green arrow,
straight through the middle.

[pause]

Before next class, read Milgrom and Roberts, chapter one, pages two to eighteen, and in chapter
four, the section on complementarities, pages one hundred and eight to one hundred and thirteen.
Then Cabral, section three point five. Try Milgrom and Roberts' food for thought questions one to
three, on page eighteen, and Cabral's exercises one point one and three point fourteen.

And keep the warning that comes with them. Whenever someone shows you a best practice, ask what
it is a complement of. A practice copied without its complements is not the same practice.

Next time: bargaining. What happens when two parties have to agree on how to split something
they can only create together.
