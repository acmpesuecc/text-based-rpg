import tkinter as tk
from tkinter import ttk

class InventoryScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory")
        self.root.geometry("450x550") # Set a fixed, spacious size
        self.root.resizable(False, False) # Prevent players from resizing

        # --- Define all dynamic variables that will power the UI ---
        self.hp_text = tk.StringVar()
        self.hp_value = tk.DoubleVar() # For the progress bar percentage
        self.gold_text = tk.StringVar()
        self.rooms_text = tk.StringVar()
        self.monsters_text = tk.StringVar()
        self.sword_text = tk.StringVar()
        self.armor_text = tk.StringVar()
        self.small_potion_text = tk.StringVar()
        self.medium_potion_text = tk.StringVar()
        self.ultra_potion_text = tk.StringVar()

        # Create the UI layout (we'll fill this in the next step)
        self.create_widgets()

        # Load initial data using a mock data function for now
        self.update_data(get_player_mock_data())

    def create_widgets(self):
    # --- 1. STATS SECTION ---
        stats_frame = tk.LabelFrame(self.root, text="PLAYER STATS", font=("Arial", 12, "bold"), padx=10, pady=10)
        stats_frame.pack(padx=15, pady=10, fill="x")

        # Static text labels on the left
        tk.Label(stats_frame, text="HP:", font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=2)
        tk.Label(stats_frame, text="Gold:", font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=2)
        tk.Label(stats_frame, text="Rooms Cleared:", font=("Arial", 11)).grid(row=2, column=0, sticky="w", pady=2)
        tk.Label(stats_frame, text="Monsters Defeated:", font=("Arial", 11)).grid(row=3, column=0, sticky="w", pady=2)

        # HP Progress Bar
        s = ttk.Style()
        s.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
        hp_bar = ttk.Progressbar(stats_frame, style="green.Horizontal.TProgressbar", orient="horizontal", length=150, mode="determinate", variable=self.hp_value)
        hp_bar.grid(row=0, column=1, sticky="w", padx=5)

        # Dynamic data labels on the right
        tk.Label(stats_frame, textvariable=self.hp_text, font=("Arial", 11)).grid(row=0, column=2, sticky="w")
        tk.Label(stats_frame, textvariable=self.gold_text, font=("Arial", 11, "bold"), fg="#D4AF37").grid(row=1, column=1, columnspan=2, sticky="w", padx=5)
        tk.Label(stats_frame, textvariable=self.rooms_text, font=("Arial", 11)).grid(row=2, column=1, columnspan=2, sticky="w", padx=5)
        tk.Label(stats_frame, textvariable=self.monsters_text, font=("Arial", 11)).grid(row=3, column=1, columnspan=2, sticky="w", padx=5)

        # --- 2. EQUIPMENT SECTION ---
        equip_frame = tk.LabelFrame(self.root, text="EQUIPMENT", font=("Arial", 12, "bold"), padx=10, pady=10)
        equip_frame.pack(padx=15, pady=10, fill="x")
        tk.Label(equip_frame, text="Sword:", font=("Arial", 11)).grid(row=0, column=0, sticky="w")
        tk.Label(equip_frame, text="Armor:", font=("Arial", 11)).grid(row=1, column=0, sticky="w")
        tk.Label(equip_frame, textvariable=self.sword_text, font=("Arial", 11, "italic"), fg="blue").grid(row=0, column=1, sticky="w", padx=5)
        tk.Label(equip_frame, textvariable=self.armor_text, font=("Arial", 11, "italic"), fg="blue").grid(row=1, column=1, sticky="w", padx=5)

        # --- 3. CONSUMABLES SECTION ---
        consum_frame = tk.LabelFrame(self.root, text="CONSUMABLES", font=("Arial", 12, "bold"), padx=10, pady=10)
        consum_frame.pack(padx=15, pady=10, fill="x")
        tk.Label(consum_frame, textvariable=self.small_potion_text, font=("Arial", 11), fg="blue").pack(anchor="w")
        tk.Label(consum_frame, textvariable=self.medium_potion_text, font=("Arial", 11), fg="blue").pack(anchor="w")
        tk.Label(consum_frame, textvariable=self.ultra_potion_text, font=("Arial", 11), fg="blue").pack(anchor="w")

        # --- 4. CLOSE BUTTON ---
        close_button = tk.Button(self.root, text="Close", command=self.root.destroy, font=("Arial", 12, "bold"))
        close_button.pack(pady=15)

    def update_data(self, player_data):
        # --- Update Stats Section ---
        hp = player_data["hp"]
        max_hp = player_data["max_hp"]
        # Calculate HP percentage for the progress bar
        hp_percent = int((hp / max_hp) * 100)
        
        self.hp_value.set(hp_percent) # This updates the progress bar
        self.hp_text.set(f"{hp}/{max_hp} ({hp_percent}%)") # This updates the text
        
        self.gold_text.set(f"🪙 {player_data['gold']} Gold")
        self.rooms_text.set(str(player_data['rooms_cleared']))
        self.monsters_text.set(str(player_data['monsters_defeated']))
        
        # --- Update Equipment Section ---
        # Check if an item is equipped before displaying it
        if player_data["sword"]:
            sword = player_data["sword"]
            self.sword_text.set(f"{sword['name']} (+{sword['stat']} Damage)")
        else:
            self.sword_text.set("None equipped")
            
        if player_data["armor"]:
            armor = player_data["armor"]
            self.armor_text.set(f"{armor['name']} (+{armor['stat']} Defense)")
        else:
            self.armor_text.set("None equipped")
            
        # --- Update Consumables Section ---
        potions = player_data["potions"]
        self.small_potion_text.set(f"Small Potion x{potions['small']} (+30 HP each)")
        self.medium_potion_text.set(f"Medium Potion x{potions['medium']} (+40 HP each)")
        self.ultra_potion_text.set(f"Ultra Potion x{potions['ultra']} (+50 HP each)")

def get_player_mock_data():
    """Returns a dictionary of sample player data. This is great for testing the UI in isolation."""
    return {
        "hp": 60, "max_hp": 100, "gold": 1450,
        "rooms_cleared": 12, "monsters_defeated": 41,
        "sword": {"name": "Iron Sword", "stat": 20},
        "armor": {"name": "Mythril Armour", "stat": 20},
        "potions": {"small": 3, "medium": 1, "ultra": 0}
    }

if __name__ == "__main__":
    # This allows you to run and test this file directly
    root = tk.Tk()
    app = InventoryScreen(root)
    root.mainloop()