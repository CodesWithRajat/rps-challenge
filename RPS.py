def player(prev_play, opponent_history=[]):
    # Add opponent's last move to history
    if prev_play:
        opponent_history.append(prev_play)

    # Counter the opponent's moves using frequency analysis
    counter = {"R": "P", "P": "S", "S": "R"}

    if not opponent_history:
        return "R"  # Default to "Rock" for the first move

    # Use frequency analysis to predict the most likely next move
    most_common = max(set(opponent_history), key=opponent_history.count)
    return counter[most_common]
