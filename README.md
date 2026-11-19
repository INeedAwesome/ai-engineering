# Group 9 - Ollama
GPU: RX 9060 XT 8 GB 

When running the program several times, it always gave an OK. Nothing failed, except in the beginning when the program wasn't fully developed yet.

The tests will not necessarily give us the same result each time. This is because the LLM is non-deterministic. Both the model and the judge is running "gemma4", which can and will generate different answers and evaluations each run.

We can not automatically know whether the model being tested or the judge failed, because the judge could've made an incorrect evaluation, or the prompt wasn't clear enough so the judge missunderstood the expected answer.