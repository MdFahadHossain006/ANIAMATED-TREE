import tkinter as tk
import math
import random
import time

# =========================================================
# WINDOW SETTINGS
# =========================================================

WIDTH = 900
HEIGHT = 700

root = tk.Tk()
root.title("Fractal Tree - MD FAHAD HOSSAIN")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)
root.configure(bg="#02030A")

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="#02030A",
    highlightthickness=0
)

canvas.pack()

# =========================================================
# ANIMATION SETTINGS
# =========================================================

FPS_DELAY = 16

# Approximate tree growth duration
TREE_DURATION = 6.0

# Number of background particles
PARTICLE_COUNT = 70

# =========================================================
# COLORS
# =========================================================

BRANCH_COLORS = [
    "#00FF66",   # Green
    "#00F5A0",   # Mint
    "#00D9FF",   # Cyan
    "#008CFF",   # Blue
    "#5555FF",   # Indigo
    "#9B4DFF",   # Purple
    "#D83BFF",   # Magenta
    "#FF3BA7"    # Pink
]

PARTICLE_COLORS = [
    "#00FFFF",
    "#00FF88",
    "#0088FF",
    "#7744FF",
    "#DD44FF",
    "#FF44AA"
]

# =========================================================
# GLOBAL VARIABLES
# =========================================================

branches = []
particles = []
stars = []

start_time = 0
creator_start = None

tree_finished = False


# =========================================================
# GENERATE FRACTAL TREE
# =========================================================

def generate_branch(
    x,
    y,
    angle,
    length,
    width,
    depth,
    start_delay
):

    # Stop recursion
    if depth > 9 or length < 7:
        return

    branch = {
        "x": x,
        "y": y,
        "angle": angle,
        "length": length,
        "width": width,
        "depth": depth,
        "delay": start_delay
    }

    branches.append(branch)

    # Calculate endpoint
    end_x = x + math.cos(angle) * length
    end_y = y + math.sin(angle) * length

    # Branch spread
    spread = random.uniform(
        0.32,
        0.58
    )

    # Smaller branches
    new_length = (
        length *
        random.uniform(
            0.67,
            0.75
        )
    )

    new_width = max(
        1,
        width * 0.70
    )

    # -----------------------------------------------------
    # LEFT BRANCH
    # -----------------------------------------------------

    generate_branch(
        end_x,
        end_y,
        angle - spread,
        new_length,
        new_width,
        depth + 1,
        start_delay + 0.30
    )

    # -----------------------------------------------------
    # RIGHT BRANCH
    # -----------------------------------------------------

    generate_branch(
        end_x,
        end_y,
        angle + spread,
        new_length,
        new_width,
        depth + 1,
        start_delay + 0.30
    )


# =========================================================
# CREATE BACKGROUND PARTICLES
# =========================================================

def create_particles():

    global particles

    particles = []

    for _ in range(PARTICLE_COUNT):

        particles.append({

            "x": random.uniform(
                40,
                WIDTH - 40
            ),

            "y": random.uniform(
                40,
                HEIGHT - 130
            ),

            "speed": random.uniform(
                0.15,
                0.5
            ),

            "size": random.uniform(
                1,
                2.5
            ),

            "phase": random.uniform(
                0,
                math.pi * 2
            ),

            "color": random.choice(
                PARTICLE_COLORS
            )
        })


# =========================================================
# CREATE STARS
# =========================================================

def create_stars():

    global stars

    stars = []

    for _ in range(35):

        stars.append({

            "x": random.randint(
                40,
                WIDTH - 40
            ),

            "y": random.randint(
                40,
                HEIGHT - 150
            ),

            "phase": random.uniform(
                0,
                math.pi * 2
            )
        })


# =========================================================
# RESET ANIMATION
# =========================================================

def reset_animation():

    global branches
    global start_time
    global creator_start
    global tree_finished

    # Clear old tree
    branches = []

    tree_finished = False

    creator_start = None

    # -----------------------------------------------------
    # Create tree
    # -----------------------------------------------------

    generate_branch(
        WIDTH // 2,
        HEIGHT - 110,
        -math.pi / 2,
        180,
        7,
        0,
        0
    )

    # Create environment
    create_particles()
    create_stars()

    # Start timer
    start_time = time.perf_counter()

    animate()


# =========================================================
# DRAW FLOATING PARTICLES
# =========================================================

def draw_particles(current_time):

    for p in particles:

        # Smooth upward movement
        p["y"] -= p["speed"]

        # Gentle horizontal movement
        p["x"] += (
            math.sin(
                current_time * 0.7 +
                p["phase"]
            ) * 0.12
        )

        # Reset particle
        if p["y"] < 20:

            p["y"] = HEIGHT - 130

            p["x"] = random.uniform(
                40,
                WIDTH - 40
            )

        # Pulsing
        pulse = (
            math.sin(
                current_time * 2 +
                p["phase"]
            ) + 1
        ) / 2

        radius = (
            p["size"] +
            pulse * 0.8
        )

        canvas.create_oval(
            p["x"] - radius,
            p["y"] - radius,
            p["x"] + radius,
            p["y"] + radius,
            fill=p["color"],
            outline=""
        )


# =========================================================
# DRAW STARS
# =========================================================

def draw_stars(current_time):

    for star in stars:

        pulse = (
            math.sin(
                current_time * 2 +
                star["phase"]
            ) + 1
        ) / 2

        size = (
            1 +
            pulse * 1.5
        )

        canvas.create_oval(
            star["x"] - size,
            star["y"] - size,
            star["x"] + size,
            star["y"] + size,
            fill="#FFFFFF",
            outline=""
        )


# =========================================================
# GET BRANCH COLOR
# =========================================================

def get_branch_color(depth):

    index = min(
        depth,
        len(BRANCH_COLORS) - 1
    )

    return BRANCH_COLORS[index]


# =========================================================
# DRAW TREE
# =========================================================

def draw_tree(elapsed):

    all_finished = True

    for branch in branches:

        # Time before branch begins
        local_time = (
            elapsed -
            branch["delay"]
        )

        # Branch hasn't started
        if local_time <= 0:

            all_finished = False

            continue

        # Growth duration
        growth_time = 0.48

        progress = min(
            1.0,
            local_time / growth_time
        )

        if progress < 1:

            all_finished = False

        # Smooth easing
        smooth = (
            progress *
            progress *
            (3 - 2 * progress)
        )

        # Current branch length
        current_length = (
            branch["length"] *
            smooth
        )

        # Start position
        x1 = branch["x"]
        y1 = branch["y"]

        # End position
        x2 = (
            x1 +
            math.cos(branch["angle"]) *
            current_length
        )

        y2 = (
            y1 +
            math.sin(branch["angle"]) *
            current_length
        )

        # Branch color
        color = get_branch_color(
            branch["depth"]
        )

        # Branch width
        width = max(
            1,
            int(branch["width"])
        )

        # -------------------------------------------------
        # SOFT GLOW
        # -------------------------------------------------

        if width >= 2:

            canvas.create_line(
                x1,
                y1,
                x2,
                y2,
                fill=color,
                width=width + 3
            )

        # -------------------------------------------------
        # MAIN BRANCH
        # -------------------------------------------------

        canvas.create_line(
            x1,
            y1,
            x2,
            y2,
            fill=color,
            width=width
        )

        # -------------------------------------------------
        # COLORFUL TIPS
        # -------------------------------------------------

        if (
            branch["depth"] >= 7
            and
            progress >= 1
        ):

            pulse = (
                math.sin(
                    elapsed * 5 +
                    branch["x"]
                ) + 1
            ) / 2

            radius = (
                1.5 +
                pulse * 2
            )

            canvas.create_oval(
                x2 - radius,
                y2 - radius,
                x2 + radius,
                y2 + radius,
                fill=color,
                outline=""
            )

    return all_finished


# =========================================================
# CREATOR TEXT
# =========================================================

def draw_creator(elapsed):

    global creator_start

    if creator_start is None:

        creator_start = elapsed

    text = "CREATED BY- MD.FAHAD HOSSAIN"

    text_elapsed = (
        elapsed -
        creator_start
    )

    # Typing speed
    chars = int(
        text_elapsed * 22
    )

    chars = min(
        chars,
        len(text)
    )

    visible = text[:chars]

    if visible:

        # -------------------------------------------------
        # SINGLE TEXT LAYER
        #
        # This prevents overlapping/double text.
        # -------------------------------------------------

        canvas.create_text(
            WIDTH // 2,
            HEIGHT - 45,
            text=visible,
            fill="#00FFCC",
            font=(
                "Consolas",
                20,
                "bold"
            ),
            anchor="center"
        )


# =========================================================
# MAIN ANIMATION
# =========================================================

def animate():

    global tree_finished

    # Current time
    elapsed = (
        time.perf_counter()
        -
        start_time
    )

    # Clear previous frame
    canvas.delete("all")

    # -----------------------------------------------------
    # BACKGROUND
    # -----------------------------------------------------

    canvas.create_rectangle(
        0,
        0,
        WIDTH,
        HEIGHT,
        fill="#02030A",
        outline=""
    )

    # -----------------------------------------------------
    # PARTICLES
    # -----------------------------------------------------

    draw_particles(
        elapsed
    )

    # -----------------------------------------------------
    # STARS
    # -----------------------------------------------------

    draw_stars(
        elapsed
    )

    # -----------------------------------------------------
    # TREE
    # -----------------------------------------------------

    finished_now = draw_tree(
        elapsed
    )

    # -----------------------------------------------------
    # GLOWING BASE
    # -----------------------------------------------------

    pulse = (
        math.sin(
            elapsed * 4
        ) + 1
    ) / 2

    radius = (
        4 +
        pulse * 3
    )

    canvas.create_oval(
        WIDTH // 2 - radius,
        HEIGHT - 110 - radius,
        WIDTH // 2 + radius,
        HEIGHT - 110 + radius,
        fill="#00FF88",
        outline=""
    )

    # -----------------------------------------------------
    # CREATOR TEXT
    # -----------------------------------------------------

    if finished_now:

        tree_finished = True

        # Start creator text after tree
        draw_creator(
            elapsed - TREE_DURATION
        )

    # -----------------------------------------------------
    # RESTART
    # -----------------------------------------------------

    if tree_finished:

        text_time = (
            elapsed -
            TREE_DURATION
        )

        if text_time > 7:

            reset_animation()

            return

    # -----------------------------------------------------
    # 60 FPS
    # -----------------------------------------------------

    root.after(
        FPS_DELAY,
        animate
    )


# =========================================================
# KEYBOARD CONTROLS
# =========================================================

def key_pressed(event):

    # Press R to restart
    if event.keysym.lower() == "r":

        reset_animation()

    # Press ESC to exit
    elif event.keysym == "Escape":

        root.destroy()


root.bind(
    "<Key>",
    key_pressed
)

# =========================================================
# START PROGRAM
# =========================================================

reset_animation()

root.mainloop()