#!/bin/bash
ollama serve &
ollama pull "gemma3:1b" &
fastapi dev --host 0.0.0.0