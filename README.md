# VibeFramework 🚀

<p align="center">
  <img src="https://img.shields.io/badge/Version-3.0.0-PRODUCTION-blue.svg" alt="Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Platforms-Android%20%7C%20iOS%20%7C%20Desktop-orange.svg" alt="Platforms">
</p>

<p align="center">
  A production-ready cross-platform application development framework for building Android, iOS, and Desktop applications using a single <code>.vibe</code> syntax file.
</p>

---

## 📋 Table of Contents

1. [Project Overview](#1-project-overview)
2. [Prerequisites](#2-prerequisites)
3. [Installation Instructions](#3-installation-instructions)
4. [Quick Start Guide](#4-quick-start-guide)
5. [Building Desktop Applications](#5-building-desktop-applications)
6. [Building Mobile Applications](#6-building-mobile-applications)
7. [Widget Reference Documentation](#7-widget-reference-documentation)
8. [Backend API Reference](#8-backend-api-reference)
9. [Configuration Options](#9-configuration-options)
10. [Troubleshooting](#10-troubleshooting)
11. [Contributing Guidelines](#11-contributing-guidelines)
12. [License Information](#12-license-information)
13. [Contact and Support](#13-contact-and-support)

---

## 1. Project Overview

### What is VibeFramework?

VibeFramework is a comprehensive, production-ready application development framework that enables developers to build cross-platform applications for Android, iOS, and Desktop platforms using a single `.vibe` syntax file. The framework provides a complete widget library, advanced layout system, event handling, reactive state management, and powerful styling capabilities.

### Key Features

| Feature | Description |
|---------|-------------|
| 🎨 **20+ Widget Types** | Buttons, Labels, TextFields, Images, Lists, Grids, Cards, Forms, and more |
| 📐 **5 Layout Systems** | LinearLayout, RelativeLayout, GridLayout, FrameLayout, FlexLayout |
| ⚡ **Event Handling** | on-click, on-change, on-focus, on-submit, on-scroll, gestures |
| 🔄 **State Management** | Reactive data binding with automatic UI updates |
| 🎭 **Theming System** | 4 built-in themes (dark, light, ocean, sunset) + custom styles |
| 🔄 **Backend Logic** | Full Python backend execution within .vibe files |
| 📱 **Cross-Platform** | Deploy to Android, iOS, Windows, macOS, and Linux |

### Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    VibeFramework Engine                      │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Parser    │  │   Widget   │  │    Layout Engine    │  │
│  │  (.vibe)    │  │   Library  │  │                     │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │    State    │  │   Event    │  │     Style Manager   │  │
│  │  Manager    │  │  Manager   │  │                     │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
├─────────────────────────────────────────────────────────────┤
│                    Output Platforms                         │
│         ┌─────────┐ ┌─────────┐ ┌─────────┐                  │
│         │ Android │ │   iOS   │ │ Desktop │                  │
│         └─────────┘ └─────────┘ └─────────┘                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Prerequisites

### System Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| **Operating System** | Windows 10, macOS 10.14, Ubuntu 18.04 | Latest versions |
| **Python** | 3.8+ | 3.10+ |
| **RAM** | 4 GB | 8 GB+ |
| **Disk Space** | 2 GB | 5 GB+ |

### Required Tools and Dependencies

#### Python Dependencies

```
# Core dependencies
python>=3.8
kivy>=2.1.0
kivy-garden>=0.1.5

# Build tools (for desktop)
pyinstaller>=5.0

# Build tools (for mobile)
buildozer>=1.4.0     # For Android
plyer>=2.1.0         # Platform features
```

#### Platform-Specific Requirements

**Windows:**
- Visual Studio Build Tools (for compiling native extensions)
- Windows 10 SDK

**macOS:**
- Xcode Command Line Tools
- Homebrew (optional)

**Linux:**
- GCC compiler
- Python development headers
- SDL2 development libraries

#### Mobile Development Requirements

**Android:**
- Android Studio with SDK
- Java Development Kit (JDK) 11+
- Android NDK (for native modules)

**iOS:**
- macOS computer (required)
- Xcode 13+
- Apple Developer Account (for device deployment)

---

## 3. Installation Instructions

### Step 1: Clone or Download the Framework

```bash
# Clone the repository
git clone https://github.com/vibeframework/vibeframework.git
cd vibeframework

# Or download the latest release
wget https://github.com/vibefrframework/vibefrframework/archive/refs/tags/v3.0.0.zip
unzip v3.0.0.zip
cd vibefrframework-3.0.0
```

### Step 2: Set Up Python Environment

**Windows:**
```cmd
:: Create virtual environment
python -m venv venv

:: Activate virtual environment
venv\Scripts\activate

:: Install dependencies
pip install kivy>=2.1.0
pip install kivy-garden>=0.1.5
pip install pyinstaller>=5.0
```

**macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install kivy>=2.1.0
pip install kivy-garden>=0.1.5
pip install pyinstaller>=5.0
```

### Step 3: Verify Installation

```bash
# Test Kivy installation
python -c "import kivy; print(f'Kivy {kivy.__version__} installed successfully')"

# Test VibeFramework
python vibe_engine.py --version
```

### Platform-Specific Setup

#### Windows Additional Setup

1. Download Visual Studio Build Tools from: https://visualstudio.microsoft.com/visual-cpp-build-tools/
2. Select "Desktop development with C++"
3. Install and restart your terminal

#### macOS Additional Setup

```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install required libraries
brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf gstreamer

# Install Kivy with media support
pip install "kivy[base]" kivy_examples
```

#### Linux Additional Setup

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-dev python3-pip
sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
sudo apt-get install libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev
sudo apt-get install zlib1g-dev xclip xsel

# Fedora
sudo dnf install python3-devel python3-pip
sudo dnf install SDL2-devel SDL2_image-devel SDL2_mixer-devel SDL2_ttf-devel
sudo dnf install portmidi-devel ffmpeg-libswscale-devel ffmpeg-libavcodec-devel
```

---

## 4. Quick Start Guide

### Your First VibeFramework Application

Create a file named `hello_world.vibe`:

```vibe
UI {
    // Simple Hello World Application
    Label("Hello, World! 👋", font_size=32, bold=true)
    Label("Welcome to VibeFramework", font_size=18)
    
    Button("Click Me!", variant="primary")
    Button("Secondary Action", variant="secondary")
}

STYLE {
    theme: ocean
}

BACKEND {
    // Backend logic
    print("Hello World app started!")
    
    def on_button_click(widget):
        print("Button was clicked!")
        App.show_toast("Hello from VibeFramework! 🎉", 2.0)
}
```

### Running the Application

```bash
python vibe_engine.py hello_world.vibe
```

### Understanding the .vibe Syntax

The `.vibe` file consists of three main sections:

```vibe
UI {
    // Widget definitions go here
    // These define your application's user interface
}

STYLE {
    // Styling and theming go here
    // Configure colors, fonts, and custom styles
}

BACKEND {
    // Python code goes here
    // Handle events and implement business logic
}
```

### Example: Interactive Form

Create `contact_form.vibe`:

```vibe
UI {
    Label("📬 Contact Form", font_size=24, bold=true)
    
    Form(fields="text:Name:Enter your name;email:Email:Enter email;text:Subject:Enter subject")
    
    Label("Message:")
    TextField(hint="Type your message...", multiline=true)
    
    Button("Send Message", variant="success")
    Button("Cancel", variant="danger")
}

STYLE {
    theme: light
}

BACKEND {
    user_data = State.create_state("user_data", {})
    
    def on_form_submit(data):
        print(f"Form data: {data}")
        
        name = data.get("Name", "Unknown")
        email = data.get("Email", "Not provided")
        
        App.show_dialog(
            title="Message Sent!",
            content=f"Thank you, {name}!\n\nWe'll contact you at {email} soon.",
            actions=[("OK", lambda x: x.dismiss())]
        )
}
```

---

## 5. Building Desktop Applications

### Building for Windows

**Step 1: Create the Spec File**

Create `vibe_engine.spec`:

```python
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['vibe_engine.py'],
    pathex=[],
    binaries=[],
    datas=[('app.vibe', '.')],
    hiddenimports=['kivy'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='VibeFrameworkApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to True for debugging
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
```

**Step 2: Build the Executable**

```cmd
pyinstaller vibe_engine.spec
```

The executable will be created in the `dist` folder.

**Step 3: Test the Application**

```cmd
dist\VibeFrameworkApp.exe
```

### Building for macOS

**Step 1: Install PyInstaller**

```bash
pip install pyinstaller
```

**Step 2: Create Spec File**

Create `vibe_engine.spec`:

```python
# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['vibe_engine.py'],
    pathex=[],
    binaries=[],
    datas=[('app.vibe', '.')],
    hiddenimports=['kivy', 'PyObjC'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='VibeFrameworkApp',
    console=False,
)

app = BUNDLE(
    exe,
    name='VibeFrameworkApp.app',
    icon=None,
    bundle_identifier='com.vibefrframework.app',
)
```

**Step 3: Build the Application**

```bash
pyinstaller vibe_engine.spec --osx-bundle-identifier='com.vibefrframework.app'
```

**Step 4: Run the Application**

```bash
open dist/VibeFrameworkApp.app
```

### Building for Linux

**Step 1: Install PyInstaller**

```bash
pip install pyinstaller
```

**Step 2: Build the Executable**

```bash
pyinstaller vibe_engine.py --onefile --name VibeFrameworkApp --add-data "app.vibe:."
```

**Step 3: Run the Application**

```bash
./dist/VibeFrameworkApp
```

### Desktop Build Commands Reference

| Platform | Command |
|----------|---------|
| Windows (EXE) | `pyinstaller vibe_engine.spec` |
| Windows (Portable) | `pyinstaller --onefile vibe_engine.py` |
| macOS (App) | `pyinstaller vibe_engine.spec` |
| macOS (DMG) | Use `create-dmg` tool |
| Linux (AppImage) | `pyinstaller --onefile --add-binary "/usr/lib/x86_64-linux-gnu/libSDL2-2.0.so.0:."` |
| Linux (deb) | Use `checkinstall` |

---

## 6. Building Mobile Applications

### Building for Android

#### Using Buildozer (Recommended)

**Step 1: Install Buildozer**

```bash
pip install buildozer
```

**Step 2: Initialize Buildozer**

```bash
cd your_project_directory
buildozer init
```

**Step 3: Configure buildozer.spec**

Edit `buildozer.spec`:

```ini
[app]
title = VibeFramework App
package.name = vibefrframeworkapp
package.domain = org.vibefrframework
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,vibe
version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 31
android.minapi = 21
android.archs = arm64-v8a,armeabi-v7a
```

**Step 4: Build the APK**

```bash
# Initial build (downloads Android SDK)
buildozer android debug

# Or for release build
buildozer android release
```

**Step 5: Locate the APK**

The APK will be at:
- Debug: `bin/VibeFrameworkApp-1.0.0-debug.apk`
- Release: `bin/VibeFrameworkApp-1.0.0-release.apk`

#### Using Android Studio

1. Create a new project in Android Studio
2. Add `vibe_engine.py` and your `.vibe` file to `app/src/main/python/`
3. Add the Kivy JAR to `app/libs/`
4. Configure the AndroidManifest.xml
5. Build using Gradle

### Building for iOS

#### Prerequisites (macOS Only)

1. Install Xcode from Mac App Store
2. Install command line tools: `xcode-select --install`
3. Accept the license: `sudo xcodebuild -license`

#### Using Kivy-iOS

**Step 1: Install Kivy-iOS**

```bash
pip install kivy-ios
```

**Step 2: Initialize the Project**

```bash
cd your_project_directory
python -m kivy_ios.toolchain create VibeFrameworkApp vibe_engine.py
```

**Step 3: Build the Project**

```bash
cd VibeFrameworkApp
python -m kivy_ios.toolchain build
```

**Step 4: Open in Xcode**

```bash
open VibeFrameworkApp.xcodeproj
```

**Step 5: Configure Signing**

1. In Xcode, go to Project Settings → Signing & Capabilities
2. Select your development team
3. Set the bundle identifier

**Step 6: Build and Run**

1. Select your target device/simulator
2. Press Cmd+B to build
3. Press Cmd+R to run

### Mobile Build Commands Reference

| Platform | Command | Output |
|----------|---------|--------|
| Android Debug | `buildozer android debug` | `bin/app-debug.apk` |
| Android Release | `buildozer android release` | `bin/app-release.apk` |
| iOS Simulator | `python -m kivy_ios.toolchain build` | Xcode project |
| iOS Device | `xcodebuild -sdk iphoneos` | `.ipa` file |

---

## 7. Widget Reference Documentation

### Basic Widgets

#### Button

```vibe
UI {
    Button("Click Me", variant="primary")
    Button("Success", variant="success")
    Button("Danger", variant="danger")
    Button("Warning", variant="warning")
    Button("Outline Style", variant="outline")
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `text` | string | Button label | "Button" |
| `variant` | string | Button style: primary, secondary, success, danger, warning, outline | "primary" |
| `on_click` | function | Click event handler | None |

#### Label

```vibe
UI {
    Label("Simple Label")
    Label("Bold Label", bold=true)
    Label("Large Text", font_size=24)
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `text` | string | Label content | "" |
| `font_size` | int | Font size in pixels | 16 |
| `bold` | boolean | Bold text | false |
| `italic` | boolean | Italic text | false |
| `align` | string | Text alignment: left, center, right | "left" |

#### TextField

```vibe
UI {
    TextField(hint="Enter name...")
    TextField(hint="Password", password=true)
    TextField(hint="Multi-line", multiline=true)
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `hint` | string | Placeholder text | "" |
| `text` | string | Initial text value | "" |
| `multiline` | boolean | Multi-line input | false |
| `password` | boolean | Password field | false |
| `on_change` | function | Text change handler | None |
| `on_focus` | function | Focus change handler | None |

### Selection Widgets

#### Checkbox

```vibe
UI {
    Checkbox(label="I agree")
    Checkbox(label="Subscribe", checked=true)
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `label` | string | Label text | "" |
| `checked` | boolean | Initial state | false |
| `on_change` | function | Change handler | None |

#### Switch

```vibe
UI {
    Label("Enable Feature:")
    Switch(active=false)
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `active` | boolean | Initial state | false |
| `on_change` | function | Change handler | None |

#### Slider

```vibe
UI {
    Label("Volume:")
    Slider(min=0, max=100, value=50, step=5)
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `min` | float | Minimum value | 0 |
| `max` | float | Maximum value | 100 |
| `value` | float | Initial value | 50 |
| `step` | float | Step increment | 1 |
| `on_change` | function | Value change handler | None |

#### Radio

```vibe
UI {
    Radio(options="Small;Medium;Large", selected="Medium")
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `options` | string | Options separated by semicolons | "" |
| `selected` | string | Initial selection | None |
| `on_change` | function | Selection change handler | None |

### Progress & Selection

#### ProgressBar

```vibe
UI {
    Label("Download Progress:")
    ProgressBar(value=70, max=100)
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `value` | float | Current value | 0 |
| `max` | float | Maximum value | 100 |

#### Spinner (Dropdown)

```vibe
UI {
    Spinner(options="Apple;Banana;Orange", text="Select Fruit")
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `options` | list | List of options | [] |
| `text` | string | Initial selection | "Select..." |
| `on_change` | function | Selection handler | None |

### Lists & Grids

#### List

```vibe
UI {
    List(items="Item 1;Item 2;Item 3;Item 4")
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `items` | string | Items separated by semicolons | "" |
| `on_item_click` | function | Click handler (index, item) | None |

#### Grid

```vibe
UI {
    Grid(items="Card 1;Card 2;Card 3;Card 4", cols=2)
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `items` | string | Items separated by semicolons | "" |
| `cols` | int | Number of columns | 2 |
| `on_item_click` | function | Click handler | None |

### Search & Navigation

#### SearchBar

```vibe
UI {
    SearchBar(placeholder="Search...")
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `placeholder` | string | Hint text | "Search..." |
| `on_search` | function | Search submit handler | None |
| `on_change` | function | Text change handler | None |

#### Navigation

```vibe
UI {
    Navigation(items="Home;Profile;Settings;Help", position="bottom")
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `items` | list | Navigation items | [] |
| `position` | string | Position: top, bottom | "bottom" |
| `on_change` | function | Selection handler | None |

### Containers

#### Card

```vibe
UI {
    Card(title="Card Title", content="Card content goes here...")
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `title` | string | Card title | "" |
| `content` | string | Card body text | "" |
| `elevation` | int | Shadow depth | 4 |

#### Form

```vibe
UI {
    Form(fields="text:Name:Enter name;email:Email:Enter email;password:Password:Enter password")
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `fields` | string | Field definitions (type:label:hint) | "" |
| `on_submit` | function | Form submit handler (data dict) | None |

### Date & Time

#### Calendar / DatePicker

```vibe
UI {
    Calendar()
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `selected_date` | date | Initial date | today |
| `on_date_select` | function | Date selection handler | None |

#### TimePicker

```vibe
UI {
    TimePicker()
}
```

**Properties:**
| Property | Type | Description | Default |
|----------|------|-------------|---------|
| `selected_time` | time | Initial time | current time |
| `on_time_select` | function | Time selection handler | None |

---

## 8. Backend API Reference

### State Management

#### State.create_state(key, initial_value)

Create a reactive state variable.

```python
user_name = State.create_state("user_name", "Guest")
count = State.create_state("count", 0)
```

#### State.get_state(key, default)

Get the current value of a state variable.

```python
name = State.get_state("user_name", "Default")
```

#### State.set_state(key, value)

Update a state variable, triggering reactive updates.

```python
State.set_state("user_name", "John")
State.set_state("count", State.get_state("count") + 1)
```

#### State.bind_state(key, widget_id, callback)

Bind a callback to state changes.

```python
def on_name_change(old, new):
    print(f"Name changed from {old} to {new}")
    
State.bind_state("user_name", "my_widget", on_name_change)
```

### Application Methods

#### App.show_toast(message, duration)

Display a temporary notification.

```python
App.show_toast("Operation successful!", 2.0)
```

#### App.show_dialog(title, content, actions)

Show a modal dialog.

```python
def on_ok(btn):
    btn.dismiss()

App.show_dialog(
    title="Confirm",
    content="Are you sure?",
    actions=[("Yes", on_ok), ("No", on_ok)]
)
```

#### App.get_widget(widget_id)

Get a widget by its ID.

```python
btn = App.get_widget("my_button")
```

### Event Handlers

Available event handlers:

| Handler | Called When | Arguments |
|---------|-------------|-----------|
| `on_click` | Button clicked | widget |
| `on_change` | Value changed | new_value |
| `on_focus` | Focus gained/lost | focused |
| `on_submit` | Form submitted | data dict |
| `on_item_click` | List/Grid item clicked | index, item |
| `on_search` | Search submitted | query |
| `on_date_select` | Date selected | date object |
| `on_time_select` | Time selected | time object |

### Built-in Functions

Available in BACKEND section:

| Function | Description |
|----------|-------------|
| `print()` | Print to console |
| `len()` | Get length |
| `range()` | Generate range |
| `enumerate()` | Enumerate sequence |
| `datetime` | Date/time utilities |
| `date` | Date object |
| `time` | Time object |
| `State` | State management |
| `Style` | Style manager |
| `Events` | Event manager |

---

## 9. Configuration Options

### Theming

Apply built-in themes in STYLE section:

```vibe
STYLE {
    theme: dark      // dark, light, ocean, sunset
}
```

Available themes:

| Theme | Description |
|-------|-------------|
| `dark` | Dark background with light text |
| `light` | Light background with dark text |
| `ocean` | Blue-tinted theme |
| `sunset` | Warm orange/red theme |

### Custom Styles

```vibe
STYLE {
    theme: ocean
    
    style my_button {
        background: #ff5500
        border_radius: 12
        padding: 16
    }
    
    style my_card {
        background: #ffffff
        elevation: 8
        border_radius: 16
    }
}
```

### Widget Properties

Common widget properties available on all widgets:

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Unique widget identifier |
| `visible` | boolean | Visibility state |
| `enabled` | boolean | Enabled/disabled state |
| `width` | string/int | Width (auto, dp, px) |
| `height` | string/int | Height (auto, dp, px) |
| `size_hint` | tuple | Size hint (x, y) |
| `pos_hint` | dict | Position hints |

---

## 10. Troubleshooting

### Common Issues and Solutions

#### Issue: "ModuleNotFoundError: No module named 'kivy'"

**Solution:**
```bash
pip install kivy
```

#### Issue: "SDL2 library not found"

**Solution (Ubuntu):**
```bash
sudo apt-get install libsdl2-dev
```

**Solution (macOS):**
```bash
brew install sdl2
```

#### Issue: "Permission denied" during build

**Solution:**
```bash
chmod +x your_script.py
```

#### Issue: "ValueError: Empty module name" with PyInstaller

**Solution:**
```bash
pip install --upgrade pyinstaller
```

#### Issue: Application crashes on startup

**Solution:**
1. Enable console mode in spec file: `console=True`
2. Run from terminal to see error messages

#### Issue: Widgets not rendering properly

**Solution:**
- Check that your .vibe file syntax is correct
- Ensure all required properties are provided
- Verify widget nesting is valid

#### Issue: State not updating UI

**Solution:**
```python
# Make sure you're using set_state, not direct assignment
State.set_state("my_var", new_value)  # Correct
State.get_state("my_var")  # Correct

# Not: State._state["my_var"].value = new_value
```

### Debug Mode

Enable debug logging:

```python
# In your .vibe file
BACKEND {
    import kivy
    kivy.config.set('kivy', 'log_level', 'debug')
}
```

### Getting Help

1. Check the widget reference in this document
2. Review example applications in the `examples/` folder
3. Enable console logging to see error messages

---

## 11. Contributing Guidelines

### How to Contribute

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/vibefrframework.git
cd vibefrframework

# Create development environment
python -m venv devenv
source devenv/bin/activate  # or devenv\Scripts\activate on Windows

# Install development dependencies
pip install -e .
pip install pytest flake8

# Run tests
pytest tests/

# Run linter
flake8 vibe_engine.py
```

### Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to new functions
- Keep functions under 100 lines

### Submitting Bug Reports

1. Check if the issue already exists
2. Create a minimal reproduction case
3. Include error messages and stack traces
4. Specify your environment (OS, Python version, Kivy version)

---

## 12. License Information

MIT License

Copyright (c) 2024 VibeFramework Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 13. Contact and Support

### Get Help

- 📧 **Email**: support@vibefrframework.com
- 💬 **Discord**: [Join our community](https://discord.gg/vibefrframework)
- 📖 **Documentation**: https://vibefrframework.readthedocs.io

### Resources

- 📚 [Official Documentation](https://vibefrframework.readthedocs.io)
- 💻 [Examples](https://github.com/vibefrframework/examples)
- 🐛 [Issue Tracker](https://github.com/vibefrframework/vibefrframework/issues)

### Stay Updated

- ⭐ Star us on GitHub
- 🐦 Follow us on Twitter
- 📰 Subscribe to our newsletter

---

<p align="center">
  Made with ❤️ by the VibeFramework Team
</p>
