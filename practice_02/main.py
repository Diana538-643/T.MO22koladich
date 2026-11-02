def minutes_per_lap(minutes, lap):
    if lap == 0:
        return "На ноль делить нельзя"
    return minutes / lap


assert minutes_per_lap(40, 5) == 8
assert minutes_per_lap(40, 0) == "На ноль делить нельзя"
assert minutes_per_lap(140, 2) == 70

words = ["зал", "фойе", "аудитория"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)