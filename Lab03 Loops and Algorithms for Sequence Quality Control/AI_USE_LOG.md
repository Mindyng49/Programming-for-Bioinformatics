# AI USE LOG

<!-- SECB3203 prompt log. Policy: PROPOSED - for approval by the SECB3203 course team before circulation to students. Fill in, then run: python tools/check_ai_log.py AI_USE_LOG.md --assessment <key> -->

- Course: SECB3203
- Assessment: <Lab 3>
- Student name: <MINDY NG>
- Matric no: <A24CS0267>
- Group ID: <n/a>
- AI level: <1>
- Tools cited: <UTM format, ChatGPT (OpenAI), GPT-6, accessed on 4 November 2026. URL: https://chatgpt.com>

## Declaration (tick exactly one)

- [ ] NIL RETURN: I did not use any generative AI tool for this assessment.
- [/] I used AI. Every interaction that influenced my work is logged below. The log is true and complete.

## Entry 1

- Date: <4 November 2026, 2:28am>
- Tool: <ChatGPT (OpenAI), GPT-6, accessed on 4 November 2026. URL: https://chatgpt.com>
- Purpose: <review>
- Prompt: <Help me to check my pseudocode>
- Output: <ChatGPT explained the pseudocode step by step and checked whether the conditions and sequence of steps followed the lab requirements>
- Verified by: <Compared the pseudocode with the lab instructions and the required algorithm>
- My change: <I reviewed the suggested explanations and adjusted my pseudocode to make the steps clearer and more accurate>
- Used in: <design/qc_design.md>

## Entry 2

- Date: <4 November 2026, 11:12am>
- Tool: <ChatGPT (OpenAI), GPT-6, accessed on 4 November 2026. URL: https://chatgpt.com>
- Purpose: <hint>
- Prompt: <Based on my word file I need to code the flowchart only right? No need to draw just code in VS Code right?>
- Output: <ChatGPT explained how to write flowcharts using Mermaid syntax. It also guided me to install the Markdown Preview Mermaid Support extension in VS Code and use the Markdown Preview to display the flowchart>
- Verified by: <Installed the extension and opened qc_design.md using the Markdown Preview>
- My change: <I used Mermaid syntax to create my own flowcharts for classify_read and trim_low_quality>
- Used in: <design/qc_design.md>

## Entry 3

- Date: <4 November 2026, 11:34am>
- Tool: <ChatGPT (OpenAI), GPT-6, accessed on 4 November 2026. URL: https://chatgpt.com>
- Purpose: <debug>
- Prompt: <Still nothing.Why cant run the flowchart>
- Output: <ChatGPT explain the custom styling that break VS Code dark themes. It also provided step-by-step guidance on reloading the VS Code window webview and configuring extension settings to fix rendering glitches>
- Verified by: <Cleaned up non-standard syntax and reloaded the VS Code window to verify the flowcharts render correctly in Markdown Preview>
- My change: <I corrected the Markdown formatting and succesfull to displat the flowchart>
- Used in: <design/qc_design.md>

## Entry 4

- Date: <4 November 2026, 12:05pm>
- Tool: <ChatGPT (OpenAI), GPT-6, accessed on 4 November 2026. URL: https://chatgpt.com>
- Purpose: <hint>
- Prompt: <Explain the classify_read function and give me hints>
- Output: <ChatGPT explain what the function used for and also the use of if, or and return>
- Verified by: <Compared the conditions with the lab requirements>
- My change: <I wrote my own conditional statements based on the explanations and checked the output>
- Used in: <src/qc.py – classify_read()>

## Entry 5

- Date: <4 November 2026, 12:40pm>
- Tool: <ChatGPT (OpenAI), GPT-6, accessed on 4 November 2026. URL: https://chatgpt.com>
- Purpose: <hint>
- Prompt: <Give me hints and list[dict] what is the dict means?>
- Output: <ChatGPT explained that a dictionary stores information using key-value pairs and that list[dict] means a list containing multiple dictionaries. It also gave hints on how to count the pass, review and reject records.>
- Verified by: <Compared the conditions with the lab requirements>
- My change: <I wrote my own conditional statements based on the explanations and understand how to access dictionary values>
- Used in: <src/qc.py – qc_summary()>

## Entry 6

- Date: <4 November 2026, 1:35pm>
- Tool: <ChatGPT (OpenAI), GPT-6, accessed on 4 November 2026. URL: https://chatgpt.com>
- Purpose: <explain>
- Prompt: <Don't understand about the trimming>
- Output: <ChatGPT explained how the trimming algorithm works by checking quality scores from the right side of the list. It used examples to explain the threshold>
- Verified by: <Practised with different quality score lists and compared the conditions with the lab requirements>
- My change: <I used the examples to understand the while loop and wrote my own test case for trim_low_quality()>
- Used in: <src/qc.py – trim_low_quality()>

## Entry 7

- Date: <4 November 2026, 4:42pm>
- Tool: <ChatGPT (OpenAI), GPT-6, accessed on 4 November 2026. URL: https://chatgpt.com>
- Purpose: <review>
- Prompt: <assert trim_low_quality([30, 10, 35, 8]) == 2?>
- Output: <ChatGPT used examples to demonstrate how the function trims low-quality scores from the 3' end>
- Verified by: <Compared the explanation with the trimming algorithm>
- My change: <I understanding that how the threshold count and change my code into the correct answer>
- Used in: <test_lab03_own.py – test_trim_low_quality()>

## Entry 8

- Date: <4 November 2026, 5:25pm>
- Tool: <ChatGPT (OpenAI), GPT-6, accessed on 4 November 2026. URL: https://chatgpt.com>
- Purpose: <debug>
- Prompt: <KeyError: 'gc' when running pytest>
- Output: <ChatGPT explained that the dictionary did not contain the key gc>
- Verified by: <ran py -m pytest again and all 9 tests passed.>
- My change: <I corrected the dictionary key from gc to gc_percent to match the CSV data>
- Used in: <Terminal>

## Entry 9

- Date: <4 November 2026, 6:01pm>
- Tool: <ChatGPT (OpenAI), GPT-6, accessed on 4 November 2026. URL: https://chatgpt.com>
- Purpose: <debug>
- Prompt: <E902 The system cannot find the file specified. (os error 2)--> src:1:1 Found 1 error.>
- Output: <ChatGPT explained that ruff could not find the src and tests folders because the terminal was running from the parent directory instead of the lab03 project directory>
- Verified by: <Checked the terminal directory and ran the ruff command again from the lab03 folder>
- My change: <I used cd lab03 to enter the project directory and run ruff check again>
- Used in: <Terminal>