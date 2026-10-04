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
</div>

# 🌌 Live Preview

<div align="center">

<a href="https://i.postimg.cc/nVmtYwcB/Screenshot-2026-10-04-194852.png">

<img
src="https://i.postimg.cc/nVmtYwcB/Screenshot-2026-10-04-194852.png"
alt="Web Game"
width="98%"
style="border-radius:18px;box-shadow:0 20px 60px rgba(0,0,0,.4);"/>

</a>

---

</div>

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

</div>
---

<div align="center">

## 👨‍💻 DEVELOPER

 **MD FAHAD HOSSAIN** 
 <div align="center">
   
<img src="https://i.postimg.cc/DZQ8Tmcc/Whats-App-Image-2026-09-119-at-1-26-32-AM.jpg" width="190" style="border-radius:80%;">

</div>



<div align="center">

## DEVELOPER CONTRACT 

<a href="https://www.facebook.com/share/1D7ExweqoM/">
<img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white">
</a>

<a href="https://www.instagram.com/mdfahadhossain006?igsh=ZzhhbzljaXVxcmFw">
<img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white">
</a>

<a href="https://youtube.com/@brightnessworld?si=0pf1lSEkvWSLXASs">
<img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white">
</a>

<a href="https://github.com/MdFahadHossain006">
<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
</a>

</div> 

---
</div> 

### ⚠️ Copyright & License

**© 2026 MD. FAHAD HOSSAIN. All Rights Reserved.**

This project is **proprietary Website & Software**. Unauthorized copying, distribution, 
modification, or use of this code is strictly prohibited.

- ❌ **No forking** without permission
- ❌ **No copying** of source code
- ❌ **No commercial use**
- ✅ **Personal use only** as an end-user

**Legal action will be taken against violators.**

[Contact for Licensing](https://www.instagram.com/mdfahadhossain006)
****

> ### 💌 "Every line of code carries a little emotion."

<br>

⭐ **If you enjoyed this project, consider starring the repository.**

</div>


<div align="center">

### 🌳 Made with Python & Creativity

**© 2026 MD. FAHAD HOSSAIN**

</div>
