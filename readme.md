## Code Solutions to MPMP4

In this repository you will find a bruteforce algorithm to generate all possible combinations of instructions that would solve thepuzzle proposed by Matt Parker in the fourth video of his Math Challenges series during the COVID-19 Pandemic.A recursive algorithm that will generate **one** valid solution for any number of cards. As well as all the sequences that would solve the problem for 3 and 4 cards in the Solutions folder.

To view the video and learn about the challenge [Click Here](https://youtu.be/oCMVUROty0g)

This Algorithm is based in the fact that a sequence of instructions that would work on every possible combination of N cards would require 2^N - 1 instructions. Each instruction will be represented by a number from 0 to N-1 and every starting combination of cards will be represented by a list of N numbers that each represent the state of a card; a 0 will represent a face down card and a 1 will represent a face up card.

### How we represent cards and sequences
Ex: Imagine we are working with 3 cards, so N=3 and we will need a sequence with 7 (2^3 - 1) instructions so they would work with all combinations.
All the possible combination of cards would be represented as follows:
```
[0,0,0] [0,0,1] [0,1,0] [0,1,1] [1,0,0] [1,0,1] [1,1,0] [1,1,1]. 
```
So we read left to right the cards as face down or up, indexing the first card as card 0, second card as 1 and so on. 

A set of instructions would be represented like this: `[0,1,0,2,0,1,0]`
(Note that a leading 0 is not ignored, as it refers to flipping the first card so the above instructions are not the same as `[1,0,2,0,1,0]`)

Using that knowledge we can start to bruteforce through every combination of instructions.

### Calculations with 4 cards
In Matt's Challenge we are interested in working with 4 cards, so we will do all future calculations with that in mind.

If we want to generate a sequence of intructions that would achieve the end goal of having all cards face down at some point, 
we calculated that we would need 15 (2^4 - 1) instructions. Each sequence will be represented by a list of instructions that 
can take any value between 0 and 3. In other words, each sequence will be represented as a number in base 4.
Having that in mind we can start to calculate how many sequences of length 15 there are. 

For starters, there are 4^15 possible sequences of length 15, starting at `[0,...,0]` and ending at `[3,...,3]`. But for our practical needs, having two consecutive instructions be the same would automatically invalidate the sequence (I will elaborate on that further ahead), so we can actually start at 4^13 represented in 15 digits as `[0,1,0,...,0]` (We can actually start further ahead but for simplicity I choose to start here as it will provide a big head start with little effort in the code).

So in the end we can start testing the sequence given by 4^13 represented as a base 4 number and go all the way up to 4^15 to test all the possible sequences of length 15. That number ends up beeing `1.006.632.960`, quite a bit of sequences to test.

### How to optimize the code
In the last section I mentioned that if a sequence contains two equal consecutive instructions, this would invalidate it inmediately. Let me explain why: First we need to have in mind that we are looking to get a sequence of the minimum length possible. We know that the minimum length for a sequence that would work for all combinations of N cards is 2^N - 1, but why is that? 

What we have to notice is that a sequence is applied the same to every combination of cards, so it is impossible for 2 different initial combinations of cards after a K number of instructions (K > 0) to end up at the same final combination. In other words, if we have A and B, two initial combination of cards and after we apply a sequence S to both of them, they end up in the same final sequence C, A and B are the same initial combination. That means that for each instruction, a maximun of one combination of cards will reach the desired state of all face down cards. 

So, if we have a "perfect" sequence that after each move would have the maximum of 1 combination reach the objective, it's length will be the number of combinations or 2^N - 1 (Notice that, although there are 2^N combinations, the first one `[0,...,0]` is already solved in instruction number 0, so we are left with 2^N - 1)

So now we can easily explain that, if we have two consecutive instructions beeing equal (lets call them I0 and I1), I0 may be able to get the maximum of 1 combinations to the goal, but I1 will revert all resting combinations to the original state before we even do I0 so it will not complete any combination and therefore the sequence will not be of minimum lenght.

## The recursive algorithm
This recursive algorithm is capable of generating one valid sequence for any number of cards (small enought to fit in memory).
It works by generating a trivial solution for a 1 card game (only one instruction of character `0`) and then builds the rest of sequences based on that.

The sequence for 2 cards is built by having the sequence for 1 card, the number 1 and the sequence for one card again `[0,1,0]`

And in general the sequence for N cards is built by: (The sequence for N-1 cards) + N-1 + (the sequence for N-1 cards)

We can see the every new sequence duplicates the number of instruction for the previous one and adds one extra number, keeping the 2^N - 1 length 

```(2^N-1) * 2 + 1 = 2^N * 2 - 2 + 1+ 2^(N+1) -1```
