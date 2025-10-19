# Connect Four AI with Alpha-Beta Pruning

A Python implementation of the classic Connect Four game with an AI opponent using the Alpha-Beta Pruning algorithm for optimal moves.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Algorithm](#algorithm)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Performance](#performance)
- [Future Work](#future-work)
- [References](#references)


## Introduction

This project is a Connect Four game that allows a human player to compete against an AI. The AI uses the Alpha-Beta Pruning algorithm, which is an optimization of the Minimax algorithm, to efficiently search for the best moves. The game is played in the console, and the AI is designed to be challenging for human players.

## Features

- Human vs AI gameplay
- Alpha-Beta Pruning for AI decision making
- Heuristic evaluation function for board states
- Win condition checking (horizontal, vertical, diagonal)
- Simple console-based interface

## Algorithm

### Alpha-Beta Pruning

Alpha-Beta Pruning is a search algorithm that reduces the number of nodes evaluated by the Minimax algorithm. It cuts off branches in the search tree that cannot possibly influence the final decision, thus making the search more efficient.

### Heuristic Evaluation

The heuristic function evaluates the board by analyzing all possible windows of 4 consecutive cells (horizontal, vertical, diagonal). It assigns scores based on the number of AI and player pieces in these windows, giving higher scores for threatening positions and lower scores for opponent threats.






