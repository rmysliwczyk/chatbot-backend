#!/bin/bash
ollama serve &
sleep 5
ollama create custom_model -f ./Modelfile
fastapi dev --host 0.0.0.0