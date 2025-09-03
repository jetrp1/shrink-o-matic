#!/bin/bash

session_name="shrink-o-matic"

SESSION_EXISTS=$(tmux list-sessions | grep $session_name)

if [ -n "$SESSION_EXISTS" ]; then
    echo "Session '$session_name' already exists. Attaching to it..."
    sleep 3
    tmux attach-session -t "$session_name"
    exit 0
fi

tmux new-session -d -s "$session_name"

# Flask Server Window
tmux new-window -t $session_name -n "Flask Server"
tmux send-keys -t "Flask Server" "source venv/bin/activate" C-m
tmux send-keys -t "Flask Server" "flask --app shrink-o-matic run --debug" C-m

# Tailwind CSS Window
tmux new-window -t $session_name -n "Tailwind CSS"
tmux send-keys -t "Tailwind CSS" "cd ~/shrink-o-matic" C-m
tmux send-keys -t "Tailwind CSS" "npm run build:css -- --watch" C-m

tmux join-pane -h -s "$session_name:Tailwind CSS" -t "$session_name:Flask Server"

tmux attach-session -t "$session_name:Flask Server"