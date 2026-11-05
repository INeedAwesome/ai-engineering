# Group 9 - Ollama

## Attempt 1:
Modell: Bonsai-2: 
GPU: RTX 3050 4GB Laptop GPU

Prompt: “What is the capital of Sweden?” 
Time: ~10 sec 
Answer: The capital of Sweden is **Stockholm** 

## Attempt 2
Modell: Bonsai-2: 
GPU: RX 9060 XT 8 GB 

Prompt: “What is the capital of Sweden?” 
Time: ~3 sec 
Answer: The capital of Sweden is **Stockholm** 

## Attempt 3
Modell: llama3.2: 
GPU: RX 9060 XT 8 GB 

Prompt: “What is the capital of Sweden?” 
Time: ~0.5 sec 
Answer: The capital of Sweden is Stockholm 

## Attempt 4
Model: nemotron-3.5-bolt
GPU: RX 9060 XT 8 GB 

Prompt: “What is the capital of Sweden?” 
Time: ~5 sec 
Answer: The capital of Sweden is Stockholm

# Thoughts on the models
When running the first test we noticed it was very slow, at first we thought something was wrong with the python install or ollama, but then an answer popped up in the console. Then we moved to another computer and the speed was massively increased (notice the GPU in the attempts). When combining all models into the script and running it, we noticed that the last model took ~15 seconds to complete. They were all correct but some of them seemed slow, especially when comparing to commercial models like ChatGPT or Claude as they answered under 2 sec.