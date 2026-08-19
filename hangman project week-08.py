import random

words = ["python", "computer", "gaming", "school", "hangman", "programming", "challenge", "developer", "keyboard", "algorithm" ,"function", "variable", "syntax", "debugging", "iteration", "condition", "exception", "library", "framework", "object" , "movie", "music", "art", "science", "history", "geography", "literature", "philosophy", "psychology", "sociology", "economics", "politics", "mathematics", "physics", "chemistry", "biology", "astronomy", "engineering", "architecture" , "design" , "photography" , "travel" , "adventure" , "sports" , "fitness" , "nutrition" , "health" , "wellness" , "meditation" , "yoga" , "mindfulness" , "creativity" , "innovation" , "entrepreneurship" , "leadership" , "teamwork" , "communication" , "collaboration" , "problem-solving" , "critical-thinking" , "decision-making" , "time-management" , "organization" , "productivity" , "motivation" , "inspiration" , "self-improvement" , "personal-development" , "career-growth" , "financial-literacy" , "investing" , "budgeting" , "saving" , "spending" , "debt-management" , "retirement-planning" , "insurance" , "taxes" , "real-estate" , "stocks" , "bonds" , "mutual-funds" , "cryptocurrency" , "blockchain" , "artificial-intelligence" , "machine-learning" , "data-science" , "cloud-computing" , "cybersecurity" , "virtual-reality" , "augmented-reality" , "internet-of-things" , "big-data" , "analytics" , "robotics" , "automation" , "3d-printing" , "nanotechnology" , "biotechnology" , "genetics" , "neuroscience" , "psychology", "sociology", "anthropology", "linguistics", "philosophy", "ethics", "political-science", "economics", "history", "geography", "literature", "art-history", "music-theory", "film-studies", "theater-studies", "dance-studies", "cultural-studies", "media-studies", "communication-studies", "education-studies", "environmental-studies" , "public-health" , "global-health" , "epidemiology" , "nutrition-science" , "exercise-science" , "sports-science" , "kinesiology" , "physical-therapy" , "occupational-therapy" , "speech-language-pathology" , "audiology" , "nursing" , "medicine" , "dentistry" , "pharmacy" , "veterinary-medicine" , "optometry" , "chiropractic-medicine" , "alternative-medicine" , "holistic-health" , "wellness-coaching"]
word = random.choice(words)

guessed = []
wrong = 0
max_wrong = 6

print("🎮 HANGMAN 🎮")

while wrong < max_wrong:
    display = "0" \
    "            incorrect guesses: " + str(wrong) + "/" + str(max_wrong) + "\n"

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong, "/", max_wrong)

    if "_" not in display:
        print("🎉 You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter ONE letter.")
        continue

    if guess in guessed:
        print("You already guessed that!")
        continue

    guessed.append(guess)

    if guess not in word:
        wrong += 1
        print("❌ Wrong! only " + str(max_wrong - wrong) + " guesses left.")
    else:
        print("✅ Correct! keep it up!")

else:
    print("\n💀 You lost!")
    print("The word was:", word)