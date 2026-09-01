import random
import time

# ============================================================
# ZOMBIE CURE: THE LAST HOPE
# ============================================================

# Player stats
health = 100
max_health = 100
day = 1
supplies = 5
zombies_defeated = 0
cure_progress = 0

# Inventory
inventory = []

# Required cure ingredients
required_items = [
    "Zombie Blood",
    "Blue Mushroom",
    "Medical Serum",
    "Ancient Virus Sample"
]

# Locations
locations = [
    "Abandoned Hospital",
    "Old Laboratory",
    "Dead Forest",
    "Military Base",
    "Abandoned Pharmacy"
]


# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def slow_print(text, delay=0.015):
    """Print text with a small delay."""
    for character in text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()


def divider():
    print("\n" + "=" * 60 + "\n")


def show_stats():
    divider()
    print("PLAYER STATUS")
    print("-" * 30)
    print(f"❤️ Health: {health}/{max_health}")
    print(f"📅 Day: {day}")
    print(f"🥫 Supplies: {supplies}")
    print(f"🧟 Zombies defeated: {zombies_defeated}")
    print(f"🧪 Cure progress: {cure_progress}/{len(required_items)}")
    
    print("\n🎒 Inventory:")
    
    if inventory:
        for item in inventory:
            print(f"  - {item}")
    else:
        print("  Empty")
    
    divider()


def pause():
    input("\nPress ENTER to continue...")


# ============================================================
# ZOMBIE ENCOUNTERS
# ============================================================

def zombie_attack():
    global health
    global supplies
    global zombies_defeated

    divider()
    slow_print("🧟 A zombie suddenly appears!")

    zombie_health = random.randint(30, 60)

    print(f"The zombie has {zombie_health} HP.")

    while zombie_health > 0 and health > 0:
        print("\nWhat will you do?")
        print("1. Attack")
        print("2. Run")
        print("3. Use supplies")

        choice = input("> ")

        if choice == "1":
            damage = random.randint(10, 25)
            zombie_health -= damage

            slow_print(f"You attack the zombie for {damage} damage!")

            if zombie_health <= 0:
                slow_print("💥 You defeated the zombie!")
                zombies_defeated += 1
                supplies += 1
                return True

            zombie_damage = random.randint(5, 18)
            health -= zombie_damage

            slow_print(
                f"The zombie attacks you for {zombie_damage} damage!"
            )

            if health <= 0:
                health = 0
                return False

        elif choice == "2":
            escape_chance = random.randint(1, 100)

            if escape_chance <= 70:
                slow_print("🏃 You escaped!")
                return True
            else:
                slow_print("You failed to escape!")

                zombie_damage = random.randint(10, 20)
                health -= zombie_damage

                slow_print(
                    f"The zombie bites you for {zombie_damage} damage!"
                )

                if health <= 0:
                    health = 0
                    return False

        elif choice == "3":
            if supplies > 0:
                supplies -= 1
                heal = random.randint(15, 30)

                health += heal

                if health > max_health:
                    health = max_health

                slow_print(
                    f"🥫 You use a supply and recover {heal} HP."
                )
            else:
                print("You have no supplies!")

        else:
            print("Invalid choice!")

    return health > 0


# ============================================================
# FINDING ITEMS
# ============================================================

def search_location(location):
    global supplies
    global health
    global day
    global cure_progress

    divider()

    slow_print(f"📍 You arrive at the {location}.")

    time.sleep(0.5)

    # Chance of zombie
    zombie_chance = random.randint(1, 100)

    if zombie_chance <= 45:
        survived = zombie_attack()

        if not survived:
            return False

    # Possible item
    available_items = [
        "Zombie Blood",
        "Blue Mushroom",
        "Medical Serum",
        "Ancient Virus Sample",
        "Bandage",
        "Food",
        "Nothing"
    ]

    found_item = random.choice(available_items)

    if found_item == "Nothing":
        slow_print("You search the area but find nothing useful.")

    elif found_item == "Bandage":
        heal = random.randint(10, 25)
        health += heal

        if health > max_health:
            health = max_health

        slow_print(
            f"🩹 You found a bandage and recovered {heal} HP!"
        )

    elif found_item == "Food":
        supplies += 2
        slow_print("🥫 You found food! +2 supplies.")

    else:
        if found_item in inventory:
            slow_print(
                f"You found another {found_item}, "
                "but you already have one."
            )
        else:
            inventory.append(found_item)
            cure_progress += 1

            slow_print(f"🧪 YOU FOUND: {found_item}!")
            slow_print(
                "This could be an important ingredient for the cure."
            )

    day += 1

    return True


# ============================================================
# LABORATORY
# ============================================================

def create_cure():
    global health

    divider()

    slow_print("🧪 You enter the secret laboratory.")
    slow_print("The room is covered with old scientific equipment.")
    slow_print("You place your samples on the laboratory table.")

    missing_items = []

    for item in required_items:
        if item not in inventory:
            missing_items.append(item)

    if missing_items:
        slow_print("\nThe computer flashes RED.")
        print("\nYou are missing:")

        for item in missing_items:
            print(f"❌ {item}")

        pause()
        return False

    slow_print("\nThe computer flashes GREEN.")
    slow_print("All required ingredients have been found!")

    print()
    slow_print("Beginning cure creation...")

    for i in range(5):
        print(f"Processing sample {i + 1}/5...")
        time.sleep(0.7)

    success_chance = random.randint(1, 100)

    if success_chance <= 85:
        divider()
        slow_print("🧪 THE CURE HAS BEEN CREATED!")
        slow_print("🎉 YOU SAVED HUMANITY!")
        slow_print(
            "The cure is sent to emergency stations around the world."
        )
        slow_print(
            "Millions of infected people can now be saved."
        )
        return True

    else:
        divider()
        slow_print("💥 THE EXPERIMENT FAILED!")
        slow_print("The samples were contaminated.")

        health -= 20

        if health < 0:
            health = 0

        slow_print("You lost 20 HP from the chemical explosion.")

        return False


# ============================================================
# RANDOM EVENTS
# ============================================================

def random_event():
    global health
    global supplies

    event = random.randint(1, 5)

    if event == 1:
        slow_print(
            "\n🌧️ A massive storm begins."
        )
        slow_print(
            "The roads become difficult to travel."
        )

    elif event == 2:
        supplies += 1
        slow_print(
            "\n📦 You find a forgotten supply box."
        )
        slow_print(
            "You gained 1 supply!"
        )

    elif event == 3:
        damage = random.randint(5, 15)
        health -= damage

        slow_print(
            f"\n🪤 You stepped into a trap!"
        )
        slow_print(
            f"You lost {damage} HP."
        )

    elif event == 4:
        slow_print(
            "\n📻 You discover an old radio."
        )
        slow_print(
            "A scientist broadcasts a message:"
        )
        print(
            '"The cure requires four specific ingredients..."'
        )

    elif event == 5:
        slow_print(
            "\n🌙 Night is approaching."
        )
        slow_print(
            "The zombies are becoming more active."
        )


# ============================================================
# MAIN GAME
# ============================================================

def main():
    global health
    global day

    divider()

    print("🧟 ZOMBIE CURE: THE LAST HOPE 🧪")

    divider()

    slow_print(
        "The apocalypse began three months ago."
    )

    slow_print(
        "A mysterious virus has turned most of humanity into zombies."
    )

    slow_print(
        "You are one of the last surviving scientists."
    )

    slow_print(
        "Your mission is simple:"
    )

    slow_print(
        "FIND THE FOUR INGREDIENTS AND CREATE THE CURE."
    )

    print("\nRequired ingredients:")

    for item in required_items:
        print(f"🧪 {item}")

    pause()

    while health > 0:
        divider()

        print(f"DAY {day}")
        print(f"❤️ Health: {health}/{max_health}")
        print(f"🥫 Supplies: {supplies}")

        print("\nWhat do you want to do?")
        print("1. Explore a location")
        print("2. Check inventory")
        print("3. Rest")
        print("4. Attempt to create the cure")
        print("5. Quit")

        choice = input("\n> ")

        if choice == "1":

            divider()

            print("Choose a location:")

            for i, location in enumerate(locations, 1):
                print(f"{i}. {location}")

            location_choice = input("\n> ")

            if location_choice.isdigit():
                number = int(location_choice)

                if 1 <= number <= len(locations):
                    selected_location = locations[number - 1]

                    survived = search_location(selected_location)

                    if not survived:
                        break

                    random_event()

                else:
                    print("Invalid location.")

            else:
                print("Please enter a number.")

            pause()

        elif choice == "2":
            show_stats()
            pause()

        elif choice == "3":
            divider()

            slow_print("😴 You decide to rest.")

            heal = random.randint(10, 20)
            health += heal

            if health > max_health:
                health = max_health

            day += 1

            slow_print(
                f"You recovered {heal} HP."
            )

            random_event()

            pause()

        elif choice == "4":

            if create_cure():
                divider()
                print("🏆 VICTORY")
                print(f"Days survived: {day}")
                print(f"Zombies defeated: {zombies_defeated}")
                print("Humanity has been saved!")

                break

            pause()

        elif choice == "5":
            print("\nYou abandoned the mission...")
            print("Humanity's last hope is gone.")
            break

        else:
            print("Invalid choice!")

    if health <= 0:
        divider()

        print("💀 GAME OVER")
        print("You were overwhelmed by the zombies.")
        print(f"You survived for {day} days.")
        print(f"Zombies defeated: {zombies_defeated}")

        divider()


# ============================================================
# START GAME
# ============================================================

if __name__ == "__main__":
    main()