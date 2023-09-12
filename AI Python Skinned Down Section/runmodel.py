from gpt4all import GPT4All
model = GPT4All("wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin", device='gpu') # device='amd', device='intel'
output = model.generate(input("User Input: "), max_tokens=3)
print(output)