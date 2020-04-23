## Code Solutions to MPMP4

In this repository you will find a bruteforce algorithm to generate all possible combinations of instructions that would solve the
puzzle proposed by Matt Parker in the fourth video of his Math Challenges series during the COVID-19 Pandemic.

To view the video [Click Here](https://youtu.be/oCMVUROty0g)

This Algorithm is based in the fact that a set of instructions that would work on every possible combination of N cards
would require 2^N - 1 instructions. Each instruction will be represented by a number from 0 to N-1 and every starting combination
of cards will be represented by a list of N numbers that each represent the state of a card; a 0 will represent a face down card
and a 1 will represent a face up card.

Ex: Imagine we are working with 3 cards, so N=3 and we will need a set with 7 (2^3 - 1) instructions so they would work with all combinations.
All the possible combination of cards would be represented as follows:

[0,0,0] [0,0,1] [0,1,0] [0,1,1] [1,0,0] [1,0,1] [1,1,0] [1,1,1]. 

So we read left to right the cards as face down or up, indexing the first card as card 0, second card as 1 and so on. 

A set of instructions would be represented like this: [0,1,0,2,0,1,0]
(Note that a leading 0 is not ignores, as it refers to flipping the first card so the above instructions are not the same as [1,0,2,0,1,0])

Using that knowledge we can start to bruteforce through every combination of instructions begining at [0,1,0,...,0] with 2^N - 1 instructions
and finishing with [N-1, N-1,..., N-1]
