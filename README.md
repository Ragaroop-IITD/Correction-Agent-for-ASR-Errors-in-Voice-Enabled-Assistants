
# Correction Agent for ASR Errors in Voice-Enabled Assistants

## Introduction

ASR (Automatic Speech Recognition) systems convert audio received from a human speaking to the device into corresponding text for further processing. However, ASR systems can make mistakes that lead to errors in the output text extracted from the input audio. These errors can cause the assistant to misunderstand commands and potentially perform the wrong actions.

In this project, we address two main types of errors:

- **Similar-sounding characters** may be incorrectly recognized.
  - Example: "The boy is eating" is recognized as "The eoy is eating" as the characters 'b' and 'e' can be mixed up.
- **Whole words** at the beginning or end of a sentence might be missing, where the speaker's voice might be softer.
  - Example: "I am going to the store" is recognized as "am going to the store".

The goal is to develop an agent that helps fix these errors by analyzing the text and improving its accuracy.

## Table of Contents

- [Problem Statement](#problem-statement)
- [Implementation Details](#implementation-details)
- [Implementation Guidelines](#implementation-guidelines)
- [Installation](#installation)
- [Usage](#usage)

## Problem Statement

The task is to develop a correction agent for text transcribed by an automatic speech recognition (ASR) system. The input to the agent is a text with all words in capital letters, separated by spaces. This text may contain errors due to the ASR system, which can be incorrect character recognition or missing words at the start or end of the sentence.

To correct these errors, the agent will utilize two key resources:

- `phoneme_table.json`: Contains information on which characters might be incorrectly recognized as others, providing possible substitutions.
- `vocabulary.json`: Lists the possible missing words that could appear at the start or end of the text received.

The agent will use a search-based algorithm to explore different correction options and use a cost function to evaluate them. The goal is to find the correction with the lowest cost, improving the accuracy of the ASR system's output.

## Implementation Details

- Implement a search-based algorithm to address the problem described above.
  - Define the key components of the problem, including state representation, operators, transition costs, etc.
  - Analyze the branching factor, or the number of possible corrections at each step.
- Local search methods can handle larger problems, such as correcting sentences up to 100 characters within 120 seconds.
  - Evaluate neighboring states carefully.
  - Graph-search style exploration of the search space may be needed for further improvements.
- Focus exclusively on search-based methods. Avoid using linear/integer programming or any domain-specific natural language processing techniques beyond search-based approaches.
- Do not make any assumptions about the cost function. A different cost function may be used during evaluation.

## Implementation Guidelines

The starter code is provided for your implementation. The code is structured as follows:

```plaintext
A1
├── data
│   ├── phoneme_table.json  # Phoneme table with possible character recognition errors.
│   ├── vocabulary.json  # List of possible words that can be missing at the beginning/end/both of the text.
│   ├── data.pkl  # Sample data file containing audio, ASR incorrect text, and corrected text.
├── driver.py  # A driver code for running your implementation.
├── environment.yml # Conda environment file.
└── solution.py  # The file where you place your implementation.
```

Run the driver program using the command below. It will run your solution for each string in the `data/data.pkl` file and write the solutions to `output.json`:

```bash
python driver.py --output_file=output.json
```

The file `solution.py` provides a template for your implementation. Implement the `asr_corrector()` method in the `class Agent`.

## Installation

To set up the project, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Create a conda environment and install the dependencies:
   ```bash
   conda env create -f environment.yml
   conda activate your-environment-name
   ```

## Usage

To run the correction agent, use the following command:

```bash
python driver.py --output_file=output.json
```



