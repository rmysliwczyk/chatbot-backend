#!/bin/bash
ollama serve &
sleep 5
ollama pull "gemma3:1b" &
fastapi dev --host 0.0.0.0