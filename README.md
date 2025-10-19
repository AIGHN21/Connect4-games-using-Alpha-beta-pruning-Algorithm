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






🎯 **AI chơi game Connect Four sử dụng thuật toán Alpha-Beta Pruning**

## 📋 Giới thiệu

Dự án này triển khai trò chơi Connect Four (4 nước liên tiếp) với AI sử dụng thuật toán Alpha-Beta Pruning để tìm nước đi tối ưu. AI có thể đánh bại người chơi ở độ khó trung bình đến cao.

## 🧠 Ý tưởng thuật toán

### Alpha-Beta Pruning

Alpha-Beta Pruning là một thuật toán tối ưu hóa của Minimax, giúp giảm đáng kể số lượng nút cần duyệt trong cây trò chơi:

- **Alpha**: Giá trị tốt nhất mà người chơi maximizing (MAX) có thể đảm bảo
- **Beta**: Giá trị tốt nhất mà người chơi minimizing (MIN) có thể đảm bảo
- **Pruning**: Cắt bỏ các nhánh không thể ảnh hưởng đến quyết định cuối cùng

### Hàm đánh giá (Heuristic Function)

Hàm heuristic được thiết kế để đánh giá trạng thái bàn cờ:

```python
def evaluate_window(window, player_id):
    # Đánh giá cửa sổ 4 ô theo các tiêu chí:
    # - 4 nước liên tiếp: +10000 điểm (thắng)
    # - 3 nước + 1 trống: +100 điểm (đe dọa thắng)
    # - 2 nước + 2 trống: +10 điểm (tiềm năng)
    # - Chặn đối thủ 3 nước: -1000 điểm (phòng thủ)
