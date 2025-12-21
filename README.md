<div align="center">

# 🌌 Space Environment Simulation
*Day & Night Visualization with OpenGL*

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-brightgreen.svg)
![OpenGL](https://img.shields.io/badge/OpenGL-PyOpenGL-red.svg)

</div>

---

An interactive 2D computer graphics project that simulates a dynamic space environment with day and night cycles, featuring animated objects like satellites, airplanes, UFOs, wind turbines, and celestial bodies. Built using Python and OpenGL for real-time rendering and smooth animations.

> *Experience the beauty of earth and space with seamless transitions between day and night modes* 🌅🌙

---

## 📸 Project Preview

### 🌞 Day Mode
<!-- Add screenshot here -->
*Beautiful sky with clouds, sun, airplane, and city skyline*

### 🌙 Night Mode
<!-- Add screenshot here -->
*Starry milky way, moon, UFO, and illuminated city buildings*

---
## 🎮 Controls

| Key | Action |
|-----|--------|
| `D` | Switch to **Day Mode** ☀️ |
| `N` | Switch to **Night Mode** 🌙 |
| `F` | Satellite moves **Forward** ⏩ |
| `B` | Satellite moves **Backward** ⏪ |
| `+` | **Increase** animation speed by 10% ⚡ |
| `-` | **Decrease** animation speed by 10% 🐌 |

---
### 🎬 Project Demo

https://github.com/user-attachments/assets/191dd4f9-3e34-4987-827b-fcec93329231

---
## ✨ Features

| Feature | Description |
|---------|-------------|
| 🌅 **Day/Night Toggle** | Switch between day and night modes with realistic backgrounds |
| ☀️ **Celestial Bodies** | Animated sun and moon with smooth transitions |
| 🛰️ **Satellite Animation** | Orbiting satellite with controllable speed and direction |
| ✈️ **Aircraft & UFO** | Hot air balloon in day mode, UFO in night mode |
| 🏙️ **City Skyline** | Dynamic city buildings with day/night lighting |
| 💨 **Wind Turbines** | Rotating wind turbines with adjustable blade speed |
| ☁️ **Moving Clouds** | Animated clouds drifting across the sky |
| ⭐ **Starfield** | Twinkling stars and milky way glow in night mode |
| 🎮 **Interactive Controls** | Keyboard controls for mode switching and speed adjustment |
| 🔄 **Real-time Animation** | Smooth 60 FPS animations with OpenGL rendering |

---

## 🧰 Technology Stack

| Technology | Purpose |
|------------|---------|
| 🐍 **Python 3.x** | Core programming language |
| 🎨 **PyOpenGL** | OpenGL bindings for Python |
| 🖼️ **GLUT** | Window management and input handling |
| 🔧 **GLU** | OpenGL utility functions |
| 📐 **2D Graphics** | Custom primitive rendering (circles, polygons, lines) |

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.x installed on your system
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/Computer-Graphics-project.git
```

### Step 2: Install Dependencies
```bash
pip install PyOpenGL PyOpenGL_accelerate
```

### Step 3: Run the Project
```bash
python main.py
```

The application window will open with the night mode view. Use keyboard controls to interact!

---

## 📁 Project Structure

```
Computer-Graphics-project/
├── main.py                      # Main application entry point
├── background.py                # Background rendering (stars, sky, milky way)
├── sun.py                       # Sun animation and rendering
├── moon.py                      # Moon rendering
├── earthsurface_satellite.py    # Earth surface and satellite dish
├── satellite.py                 # Orbiting satellite animation
├── airplane.py                  # Hot air balloon (day mode)
├── ufo.py                       # UFO animation (night mode)
├── clouds.py                    # Cloud system and animation
├── citybuildings.py             # City skyline rendering
├── windturbine.py              # Wind turbine with rotating blades
└── README.md                    # Project documentation
```

---

## 🎯 Key Modules

### 🌟 Background System
- **Stars**: Randomly generated twinkling stars with varying brightness
- **Milky Way**: Glowing effect creating atmospheric depth
- **Sky Gradient**: Smooth color transitions for realistic day sky

### 🛰️ Dynamic Objects
- **Satellite**: Orbits around a central point with adjustable speed
- **Wind Turbine**: Rotating three-blade system
- **Aircraft/UFO**: Context-aware objects based on day/night mode
- **Clouds**: Multiple cloud layers with independent movement

### 🏙️ Environment
- **City Buildings**: Procedurally rendered with windows
- **Earth Surface**: Ground level with satellite dish
- **Lighting**: Mode-dependent color schemes

---

## 🎨 Graphics Techniques Used

- ✅ **Primitive Rendering**: Custom functions for circles, polygons, and lines
- ✅ **Double Buffering**: Smooth animation without flickering
- ✅ **Alpha Blending**: Transparency effects for clouds and glows
- ✅ **Timer-based Animation**: Consistent 60 FPS frame rate
- ✅ **Viewport Management**: Responsive window resizing
- ✅ **Color Interpolation**: Smooth transitions between modes
- ✅ **Parametric Equations**: Circle and arc generation

---

## 👨‍💻 Developer

| Member | Role |
|--------|------|
| **Sazzad Mahmud Joy** | 🎨 Lead Developer | 
| **Anika Afrin Moumeta** | 💻 Project Designer | 
| **Mohusina Tasnim** | 🎯 Module Developer | 

---

---

## 🐛 Known Issues & Future Enhancements

### 🔧 Future Features
- [ ] Add more celestial objects (planets, comets)
- [ ] Implement weather effects (rain, snow)
- [ ] Add sound effects for ambiance
- [ ] 3D transformation support
- [ ] Save/load custom configurations
- [ ] Multiple camera views
- [ ] Day/night cycle automation

---

## 📚 Learning Resources

This project demonstrates concepts from:
- Computer Graphics fundamentals
- OpenGL 2D rendering pipeline
- Animation timing and interpolation
- Event-driven programming
- Modular code architecture

---

## 🎓 Academic Information

**Course**: CSE422 - Computer Graphics  
**Institution**: Daffodil International University
**Semester**: Fall25
**Year**: 2025

---

## 📞 Contact & Support
- 📧 Email: joy15-5777@diu.edu.bd

---

## 🌟 Acknowledgments

- OpenGL community for excellent documentation
- PyOpenGL developers for Python bindings
- All contributors and supporters

---

<div align="center">

### Made with 💙 and lots of ☕

**Star ⭐ this repo if you found it helpful!**

</div>
