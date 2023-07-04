# Chat GPT Optimized code, Optimized for better readability and performance
# Doing so has removed 23 lines of code, removed redundant annotations from the __init__ method
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import numpy as np
from tkinter import PhotoImage
from PIL import ImageTk, Image

class GUI:
    def __init__(self) -> None:
        self.player_level = 0
        self.optimal_tier = 0
        self.monster_level = 55
        self.static_level = 54
        self.nm_tiers = np.array([])
        self.player_levels = np.array([])

        # Controls
        self.GUI_combo_tiers = None
        self.GUI_entry_tiers_filter = None
        self.GUI_Form = None
        self.GUI_MonsterLevel = None
        self.GUI_PlayerLevels = None
        self.GUI_PlayerLevel_Filter = None
        self.GUI_Optimal_Tier_Label = None

    def create_gui(cls):
        # Create Form Size Variables
        form_width = 600
        form_height = 215

        # Create Form Window
        form = ctk.CTk()
        form.title('Diablo IV - Nightmare Dungeon Calculator')
        form.geometry(f'{form_width}x{form_height}')
        form.configure(fg_color="#161616")
        ctk.set_default_color_theme('dark-red.json')
        form.iconbitmap('icon.ico')
        form.resizable(False, False)
        cls.GUI_Form = form

        # Create GUI For monster LVL Calculator
        # Monster Section Label
        lbl_section_monster_lvl_title = ctk.CTkLabel(form, text='Monster Level Calculator')
        lbl_section_monster_lvl_title.grid(columnspan=1, rowspan=1, column=1, row=1, pady=2, padx=10)

        # Nightmare Tier Combo box Label
        lbl_Nightmare_Tier = ctk.CTkLabel(form, text='Nightmare Tier: ')
        lbl_Nightmare_Tier.grid(columnspan=1, rowspan=1, column=1, row=3, padx=3, pady=5)

        # Nightmare Tier Combo Box
        combo_Nightmare_Tier_level = ctk.CTkComboBox(form, width=100, height=30)
        cls.nm_tiers = np.array([f'Tier {tier_num}' for tier_num in range(1, 101)])
        combo_Nightmare_Tier_level.configure(values=cls.nm_tiers)
        combo_Nightmare_Tier_level.set(cls.nm_tiers[0])  # Select first tier in combo box
        combo_Nightmare_Tier_level.configure(state='readonly', justify=ctk.CENTER)
        combo_Nightmare_Tier_level.grid(column=2, row=3, padx=3, pady=5)
        cls.GUI_combo_tiers = combo_Nightmare_Tier_level

        # Nightmare Tier Filter Label
        lbl_Nightmare_Tier_Filter = ctk.CTkLabel(form, text='Tier Filter: ')
        lbl_Nightmare_Tier_Filter.grid(column=1, row=4, padx=3, pady=5)

        # Nightmare Tier Filter Box
        entry_Nightmare_Tier_Filter = ctk.CTkEntry(form, width=100, height=30, placeholder_text='Int only')
        entry_Nightmare_Tier_Filter.grid(column=2, row=4, padx=3, pady=5)
        entry_Nightmare_Tier_Filter.configure(validatecommand=(form.register(cls.validate_entry), '%P'))
        entry_Nightmare_Tier_Filter.configure(justify=ctk.CENTER)
        entry_Nightmare_Tier_Filter.bind('<Return>', lambda event: cls.filter_tier_combo())
        entry_Nightmare_Tier_Filter.bind('<FocusOut>', lambda event: cls.filter_tier_combo())
        cls.GUI_entry_tiers_filter = entry_Nightmare_Tier_Filter

        # Monster Level Text
        lbl_monster_level = ctk.CTkLabel(form, text=f'Monster Level: {cls.monster_level}')
        lbl_monster_level.grid(column=1, row=5, padx=3, pady=5)
        cls.GUI_MonsterLevel = lbl_monster_level

        # Button Clear
        bttn_clear_MonsterLVL = ctk.CTkButton(form, text='Clear', width=125, height=30)
        bttn_clear_MonsterLVL.grid(column=1, row=6, padx=3, pady=5)
        bttn_clear_MonsterLVL.configure(command=cls.clear_monster_level)

        # Button Calculate
        bttn_calculate_MonsterLVL = ctk.CTkButton(form, text='Calculate', width=125, height=30)
        bttn_calculate_MonsterLVL.configure(command=cls.calculate_monster_level)
        bttn_calculate_MonsterLVL.grid(column=2, row=6, padx=3, pady=5)

        # Seperator
        ctk.CTkFrame(form, width=4, height=form_height, fg_color='#202020').grid(columnspan=8, rowspan=8, column=5, row=1)

        # XP Calculator UI
        # Label Optimal XP Section
        lbl_optimal_XP_Section = ctk.CTkLabel(form, text='Optimal XP Calculator')
        lbl_optimal_XP_Section.grid(row=1, column=15, padx=15, pady=5)

        # Label Player Level
        lbl_player_level = ctk.CTkLabel(form, text='Player Level: ')
        lbl_player_level.grid(row=3, column=15, padx=3, pady=5)

        # combo player level
        combo_player_level = ctk.CTkComboBox(form, width=100, justify=ctk.CENTER, state='readonly')
        combo_player_level.grid(row=3, column=16, padx=3, pady=5)
        cls.player_levels = np.array([f'Level {level_index}' for level_index in range(50, 101)])
        combo_player_level.configure(values=cls.player_levels)
        combo_player_level.set(cls.player_levels[0])
        cls.GUI_PlayerLevels = combo_player_level

        # Label Player Level Filter
        lbl_player_level_filter = ctk.CTkLabel(form, text='Filter Level: ')
        lbl_player_level_filter.grid(row=4, column=15, padx=3, pady=5)

        # Entry Player Level Filter
        entry_player_level_filter = ctk.CTkEntry(form, placeholder_text='Level (int)', width=100, justify=ctk.CENTER)
        entry_player_level_filter.grid(row=4, column=16, padx=3, pady=5)
        cls.GUI_PlayerLevel_Filter = entry_player_level_filter
        entry_player_level_filter.bind('<Return>', lambda event: cls.filter_player_level())
        entry_player_level_filter.bind('<FocusOut>', lambda event: cls.filter_player_level())

        # Optimal Tier Text
        lbl_optimal_tier = ctk.CTkLabel(form, text=f'Optimal XP Tier: {cls.optimal_tier}')
        lbl_optimal_tier.grid(row=5, column=15, padx=3, pady=5)
        cls.GUI_Optimal_Tier_Label = lbl_optimal_tier

        # Clear Button
        bttn_clear_playerLevel = ctk.CTkButton(form, text=f'Clear', width=125, height=30)
        bttn_clear_playerLevel.configure(command=cls.clear_XP_calculation)
        bttn_clear_playerLevel.grid(row=6, column=15)

        # Calculate Button
        bttn_calculate_tier = ctk.CTkButton(form, text='Calculate', width=125, height=30)
        bttn_calculate_tier.grid(row=6, column=16)
        bttn_calculate_tier.configure(command=cls.calculate_dungeon_tier)

        form.mainloop()

    # Form Events
    # Filter Combo Box
    def filter_tier_combo(cls):
        filter_entry = cls.GUI_entry_tiers_filter.get()
        if filter_entry.isdigit():
            tier_index = int(filter_entry) - 1
            if 0 <= tier_index < len(cls.nm_tiers):
                cls.GUI_combo_tiers.set(cls.nm_tiers[tier_index])
            if not 1 <= int(filter_entry) <= 100:
                CTkMessagebox(cls.GUI_Form, width=350, height=200, title='Invalid Entry', icon='warning',
                              message='Must be an integer between 1 and 100')

    # Validate Entry
    def validate_entry(cls):
        filter_entry = cls.GUI_entry_tiers_filter.get()
        return filter_entry.isdigit() and 1 <= int(filter_entry) <= 100

    # Filter Player Level
    def filter_player_level(cls):
        filter_entry = cls.GUI_PlayerLevel_Filter.get()
        if filter_entry.isdigit():
            level_index = int(filter_entry) - 50
            if 0 <= level_index < len(cls.player_levels):
                cls.GUI_PlayerLevels.set(cls.player_levels[level_index])
            if not 50 <= int(filter_entry) <= 100:
                CTkMessagebox(cls.GUI_Form, width=350, height=200, title='Invalid Entry', icon='warning',
                              message='Must be an integer between 50 and 100')

    # Clear Monster Level Calculation
    def clear_monster_level(cls):
        cls.GUI_entry_tiers_filter.delete(0, ctk.END)
        cls.GUI_entry_tiers_filter.configure(placeholder_text='Int Only')
        cls.GUI_combo_tiers.set(cls.nm_tiers[0])
        cls.monster_level = 55
        cls.GUI_MonsterLevel.configure(text=f'Monster Level: {cls.monster_level}')

    # Calculate Monster Level
    def calculate_monster_level(cls):
        selected_tier = cls.GUI_combo_tiers.get()
        int_tier = ''.join(filter(str.isdigit, selected_tier))
        dungeon_monster_level = cls.static_level + int(int_tier)
        cls.monster_level = dungeon_monster_level
        cls.GUI_MonsterLevel.configure(text=f'Monster Level: {cls.monster_level}')

    def calculate_dungeon_tier(cls):
        selected_level = cls.GUI_PlayerLevels.get()
        int_level = ''.join(filter(str.isdigit, selected_level))
        player_level = int(int_level)

        # Calculate Optimal Level
        optimal_level = int(selected_level.split()[1]) + 3

        # Search Array
        nm_dungeon = np.column_stack((np.arange(1, 101), np.arange(54, 154)))
        indices = np.where(nm_dungeon[:, 1] == optimal_level)[0]

        if player_level == 50 or player_level == 51:
            cls.optimal_tier = 1
            optimal_level = cls.static_level + cls.optimal_tier
            cls.GUI_Optimal_Tier_Label.configure(
                text=f'Optimal XP Tier: Tier {cls.optimal_tier}\n\tEnemy Level - {optimal_level}')
        else:
            cls.optimal_tier = ', '.join(map(str, indices))
            cls.GUI_Optimal_Tier_Label.configure(
                text=f'Optimal XP Tier: Tier {cls.optimal_tier}\n\tEnemy Level - {optimal_level}')

    def clear_XP_calculation(cls):
        cls.GUI_PlayerLevels.set(cls.player_levels[0])
        cls.GUI_PlayerLevel_Filter.delete(0, ctk.END)
        cls.GUI_PlayerLevel_Filter.configure(placeholder_text='Level (int)')
        cls.player_level = 50
        cls.optimal_tier = 1
        cls.GUI_Optimal_Tier_Label.configure(text=f'Optimal XP Tier: Tier {cls.optimal_tier}\n\tEnemy Level - {cls.static_level + 1}')
