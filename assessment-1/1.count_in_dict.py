ip_string = """Hakka and Bukka were brothers and warriors. The brothers wanted to build their own kingdom where people could live without fear. They collected a band of young men and trained them in warfare. They lived in a forest hideout on the banks of the river Tungabhadra in South India.
One day, the brothers were out on a hunt. Ferocious dogs accompanied them. They crossed the river and rode on. A couple of frightened rabbits ran out of the bushes. The dogs gave them chase with the two brothers closely behind on their horses.
It was a long chase. The rabbits were running for their life. The dogs were catching up. Suddenly, in a swift move, the rabbits turned and faced the dogs. Taken aback by the show of defiance, the barking dogs stepped back. Hakka called back the dogs. As the dogs turned back, the rabbits walked away.
Hakka looked around. They were on the other side of the Tungabhadra. It was a rocky land. The sun was blazing in the sky.
"Strange! I’ve never seen rabbits challenging dogs before!" said Bukka.
"That’s the quality of this land," said a quiet voice, "Even rabbits give fight."
Startled to hear a stranger speak, the two brothers turned.
They saw a holy man walking towards them. He was a picture of peace. At the same time, his eyes were blazing bright."""
ip_string = ip_string.replace('.', '')
ip_string = ip_string.replace(',', '')
ip_string = ip_string.replace('!', '')


length = len(ip_string)
words = 0
occurance_dict = {}
ip_list = ip_string.split(' ')
for i in ip_list:
    if i in occurance_dict:
        occurance_dict[i] = occurance_dict[i] + 1
        words = words + 1
    else:
        occurance_dict[i] = 1
        words = words + 1
max_occurance = 0
for i, j in occurance_dict.items():
    if j > max_occurance:
        max_occurance = j
max_occurance_words = []
for i, j in occurance_dict.items():
    if j == max_occurance:
        max_occurance_words.append(i)
repeated_words_count = []
for i, j in occurance_dict.items():
    if j > 1 and j not in repeated_words_count:
        repeated_words_count.append(j)
repeated_words = []
for i, j in occurance_dict.items():
    if j > 1:
        repeated_words.append(i)

resulted_dict = {'Length of string': length,
                 'Number of words': words,
                 'Max Occurance': max_occurance,
                 'Max Occurance word': max_occurance_words,
                 'Repeated words count': repeated_words_count,
                 'Repeated words list': repeated_words}
print(resulted_dict)
