<div align="center">
  
# 🌳✨ Animated Fractal Tree — Python



# 🌈 Animated Fractal Tree

### 🎨 A colorful, smooth, and interactive fractal tree animation built with Python & Tkinter

**Created by MD. FAHAD HOSSAIN**

<br>

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange?style=for-the-badge)
![Animation](https://img.shields.io/badge/Animation-Smooth-purple?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

</div>

---

## 🌳 About The Project

**Animated Fractal Tree** is a visually attractive Python animation project that generates a fractal-style tree using recursive branching.

The project combines:

- 🌳 Recursive fractal tree generation
- 🌈 Multiple colorful branch gradients
- ✨ Floating particles
- ⭐ Animated stars
- 💫 Smooth branch-growth animation
- 🟢 Glowing tree base
- ⌨️ Keyboard controls
- 💻 Tkinter GUI
- 🎨 Dark futuristic background

The tree grows smoothly from the bottom of the screen and creates a colorful neon-style visual effect.

---

## 🖼️ Project Preview

> Add your project screenshot or GIF here.

```text
📸 Add Screenshot / GIF

Example:

![Fractal Tree Preview](preview.gif)
```

You can upload a GIF or screenshot to your GitHub repository and replace the line above with:

```markdown
![Fractal Tree Preview](preview.gif)
```

---

## ✨ Features

### 🌳 Recursive Fractal Tree

The tree is generated recursively. Each branch creates two smaller branches, producing a natural fractal structure.

```python
generate_branch(...)
```

The recursion continues until the maximum depth or minimum branch length is reached.

---

### 🌈 Colorful Neon Branches

The tree uses multiple colors including:

- 🟢 Green
- 🩵 Mint
- 🔵 Cyan
- 💙 Blue
- 🟣 Indigo
- 🟪 Purple
- 💗 Magenta
- 🌸 Pink

This creates a futuristic neon appearance.

---

### ✨ Floating Particles

The background contains animated particles that slowly move upward while gently moving horizontally.

The particles also have a pulsing effect to make the animation feel more dynamic.

---

### ⭐ Animated Stars

Small stars are randomly positioned around the scene and continuously pulse in brightness and size.

---

### 💫 Smooth Animation

The project uses a smooth easing function for branch growth:

```python
smooth = progress * progress * (3 - 2 * progress)
```

This produces a more natural animation instead of linear movement.

---

### 📝 Animated Creator Text

After the tree finishes growing, the project displays:

```text
CREATED BY- MD.FAHAD HOSSAIN
```

The text appears with a typing-style animation.

---

### ⌨️ Keyboard Controls

| Key | Action |
|---|---|
| `R` | 🔄 Restart animation |
| `ESC` | ❌ Exit application |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Main programming language |
| 🖼️ Tkinter | GUI and canvas |
| 📐 Math | Branch calculations |
| 🎲 Random | Randomized branches & particles |
| ⏱️ Time | Animation timing |

The project uses Python's built-in modules and does **not require external packages**.

---

## 📂 Project Structure

```text
Animated-Fractal-Tree/
│
├── Tree.py
├── README.md
└── preview.gif
```

> `preview.gif` is optional and can be added later.

---

## 🚀 How To Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Animated-Fractal-Tree.git
```

### 2️⃣ Enter the Project Folder

```bash
cd Animated-Fractal-Tree
```

### 3️⃣ Run the Python Program

```bash
python Tree.py
```

On some systems you may need:

```bash
python3 Tree.py
```

---

## 💻 Requirements

You only need:

```text
Python 3.x
Tkinter
```

### Windows

Tkinter is normally included with standard Python installations.

Check Python:

```bash
python --version
```

---

## 🎮 Controls

```text
R      → Restart Animation

ESC    → Exit Program
```

---

## ⚙️ Customization

You can easily customize the project by changing the values in the Python file.

### 🖥️ Window Size

```python
WIDTH = 900
HEIGHT = 700
```

### 🎞️ Animation Speed

```python
FPS_DELAY = 16
```

### 🌳 Tree Growth Duration

```python
TREE_DURATION = 6.0
```

### ✨ Particle Count

```python
PARTICLE_COUNT = 70
```

### 🌈 Branch Colors

```python
BRANCH_COLORS = [
    "#00FF66",
    "#00F5A0",
    "#00D9FF",
    "#008CFF",
    "#5555FF",
    "#9B4DFF",
    "#D83BFF",
    "#FF3BA7"
]
```

Experiment with different colors to create your own visual style.

---

## 🧠 How It Works

The project follows a simple animation pipeline:

```text
Start Program
     │
     ▼
Generate Fractal Tree
     │
     ▼
Create Particles & Stars
     │
     ▼
Start Animation Loop
     │
     ├── Draw Background
     │
     ├── Animate Particles
     │
     ├── Animate Stars
     │
     ├── Grow Tree Branches
     │
     └── Draw Creator Text
     │
     ▼
Animation Complete
     │
     ▼
Restart
```

---

## 🌱 Fractal Generation

Each branch calculates a new endpoint using trigonometry:

```python
end_x = x + math.cos(angle) * length
end_y = y + math.sin(angle) * length
```

The program then creates two smaller branches:

```text
             🌿
            /  \
           /    \
          🌿    🌿
         / \    / \
        🌿 🌿  🌿 🌿
```

This recursive process creates the final fractal tree.

---

## 🎨 Visual Design

The project uses a dark background:

```text
#02030A
```

combined with bright neon colors to create a futuristic visual style.

The tree also uses a soft glow effect by drawing a wider branch underneath the main branch.

---

## 🔥 Future Improvements

Possible future upgrades:

- [ ] 🎵 Add background music
- [ ] 🎨 Add color theme selector
- [ ] 🌳 Add different tree styles
- [ ] 🎚️ Add animation speed control
- [ ] 🖥️ Add fullscreen mode
- [ ] 💾 Add screenshot/export feature
- [ ] 🎬 Export animation as GIF
- [ ] 🌙 Add multiple backgrounds
- [ ] 🖱️ Add mouse interaction
- [ ] ⚡ Add interactive GUI controls

---

## 👨‍💻 Developer

<div align="center">

# MD. FAHAD HOSSAIN

### 💻 Software Developer | Web Developer | Python Developer

**Building creative projects with code 🚀**

</div>

---

## 🌐 Connect With Me

<div align="center">

[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/share/1D7ExweqoM/)

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/mdfahadhossain006/)

[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://youtube.com/@brightnessworld)

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MdFahadHossain006)

</div>

---

## ⭐ Support

If you like this project, please consider giving it a ⭐ on GitHub.

It helps support future creative coding projects!

---

<div align="center">

### 🌳 Made with Python & Creativity

**© 2026 MD. FAHAD HOSSAIN**

</div>
