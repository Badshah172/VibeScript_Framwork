
# 🚀 VibeScript Framework (v1.0)

**VibeScript** is a high-performance, transpiler-based framework designed for developers who want to build cross-platform applications (Android, iOS, Desktop) using a single, intuitive `.vibe` syntax.

---

## 🏗️ Architecture
VibeScript uses a **Transpiler Approach**. Unlike traditional interpreters, it converts your `.vibe` source code into high-performance execution instructions handled by the **Vibe Engine**.



* **Core Engine (`vibe_engine.py`):** The heart of the framework that manages UI rendering and backend logic.
* **Vibe Syntax (`.vibe`):** A unified language for both UI design and logic.

---

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure you have **Python 3.11 or 3.12** installed (Recommended for stability).

### 2. Environment Setup
Run the following command to update your environment and install the core rendering engine:

```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install kivy

```

### 3. Project Structure

Create a folder named `VibeFramework` and organize your files like this:

```text
VibeFramework/
├── vibe_engine.py   # The Core Engine
└── app.vibe         # Your Application Code

## 🚀 Usage

To run your VibeScript application, use the Vibe Engine to parse your code:

```bash
python vibe_engine.py app.vibe

## 📱 Multi-Platform Deployment

VibeScript bridges your logic to native kits for maximum performance.

| Platform | Bridge Method | Build Tool |
| --- | --- | --- |
| **Desktop** | C++ / Qt / Kivy | PyInstaller |
| **Android** | Kotlin / JVM Bridge | Buildozer |
| **iOS** | Swift Bridge | Kivy-iOS / Xcode |

### **▶️ Run Your First App**
Terminal / Command Prompt me VibeFramework folder open karein:
```bash
python vibe_engine.py app.vibe
```
### Build Commands:

#### **🖥️ Desktop Build (EXE / APP)**

```bash
python -m pip install pyinstaller
python -m PyInstaller --onefile vibe_engine.py

```

#### **📱 Android Build (APK)**

*(Requires Linux or Google Colab)*

```bash
pip install buildozer
buildozer init
buildozer -v android debug

```

```

#### ** 🍎 iOS Build iOS / Mac required:**
```bash
Requirements:
macOS
Xcode
kivy-ios
Steps:
Use kivy-ios to generate an Xcode project
Compile & sign using Xcode
Deploy to device or App Store
```


```bash
pip install buildozer
buildozer init
buildozer -v android debug

```
---

## 📄 VibeScript Syntax Example (`app.vibe`)

Writing apps in VibeScript is simple:

```vibe
Define App: "MyVibeApp"
Create Button:
    text: "Click the Vibe"
    on_press: print("Vibe is High!")

```

---

## 🛠️ Roadmap

* [ ] Add Hot-Reloading support.
* [ ] Native Material Design 3 components.
* [ ] Integrated SQLite Vibe-Database.

## **📜 License**

MIT License (Planned)

**Developed with ❤️ by Syed Hassnain ALi Shah**
```
