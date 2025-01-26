#typing challenge code

import time

difficulty = int(input("What difficulty would you like? \n Easy: 1 \n Medium: 2 \n Hard: 3\n"))
timer_start = time.time()
accuracy = 0
user_input = ""

if difficulty == 1:
    paragraph = ("He heard the crack echo in the late afternoon about a mile away. His heart started racing and he bolted into a full sprint. 'It wasn't a gunshot, it wasn't a gunshot,' he repeated under his breathlessness as he continued to sprint")
elif difficulty == 2:
    paragraph = ("Dave watched as the forest burned up on the hill, only a few miles from her house. The car had been hastily packed and Marta was inside trying to round up the last of the pets. Dave went through his mental list of the most important papers and documents that they couldn't leave behind. He scolded himself for not having prepared these better in advance and hoped that he had remembered everything that was needed. He continued to wait for Marta to appear with the pets, but she still was nowhere to be seen.")
elif difficulty == 3:
    paragraph = ("Her hand was balled into a fist with her keys protruding out from between her fingers. This was the weapon her father had shown her how to make when she walked alone to her car after work. She wished that she had something a little more potent than keys between her fingers. It would have been nice to have some mace or pepper spray. He had been meaning to buy some but had never gotten around to it. As the mother bear took another step forward with her cubs in tow, she knew her fist with keys wasn't going to be an adequate defense for this situation.")

print(paragraph)
user_input = input()

for i in range(len(paragraph)):
    if i < len(user_input) and paragraph[i] == user_input[i]:
        accuracy += 1

timer_end = time.time()
total_time = timer_end - timer_start

print("The time it took is ", total_time)
print("Your accuracy was ", accuracy, "out of", len(paragraph))
