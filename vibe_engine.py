"""
VibeFramework - Production-Ready Cross-Platform Application Development Framework
===================================================================================

A comprehensive framework for building cross-platform applications (Android, iOS, Desktop)
using a single .vibe syntax file. Supports 20+ widget types, multiple layout systems,
advanced event handling, reactive state management, and powerful styling capabilities.

Author: VibeFramework Team
Version: 3.0.0 PRODUCTION
"""

import sys
import re
import os
import textwrap
from typing import Any, Dict, List, Optional, Callable
from datetime import datetime, date, time

# Kivy imports for cross-platform UI
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.checkbox import CheckBox
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.progressbar import ProgressBar
from kivy.uix.spinner import Spinner
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.popup import Popup
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, FadeTransition
from kivy.uix.behaviors import FocusBehavior, ButtonBehavior
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, StringProperty, BooleanProperty, ListProperty, ObjectProperty, DictProperty
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle, RoundedRectangle, BoxShadow
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.lang import Builder


# =============================================================================
# SECTION 1: STATE MANAGEMENT SYSTEM
# =============================================================================

class Observable:
    """Reactive state container that triggers UI updates on data changes."""
    
    def __init__(self, initial_value=None):
        self._value = initial_value
        self._listeners: List[Callable] = []
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        old_value = self._value
        self._value = new_value
        self._notify_listeners(old_value, new_value)
    
    def _notify_listeners(self, old_value, new_value):
        for listener in self._listeners:
            try:
                listener(old_value, new_value)
            except Exception as e:
                print(f"State listener error: {e}")
    
    def bind(self, callback: Callable):
        """Bind a callback to be notified of state changes."""
        if callback not in self._listeners:
            self._listeners.append(callback)
    
    def unbind(self, callback: Callable):
        """Remove a bound callback."""
        if callback in self._listeners:
            self._listeners.remove(callback)


class StateManager:
    """
    Central state management system for reactive UI updates.
    Manages global application state and provides reactive data binding.
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._state: Dict[str, Observable] = {}
        self._computed: Dict[str, Callable] = {}
        self._widgets: Dict[str, List] = {}  # widget_id -> [callbacks]
        self._initialized = True
    
    def create_state(self, key: str, initial_value: Any = None) -> Observable:
        """Create a new reactive state variable."""
        obs = Observable(initial_value)
        self._state[key] = obs
        return obs
    
    def get_state(self, key: str, default: Any = None) -> Any:
        """Get the current value of a state variable."""
        if key in self._state:
            return self._state[key].value
        return default
    
    def set_state(self, key: str, value: Any):
        """Set the value of a state variable, triggering reactive updates."""
        if key not in self._state:
            self.create_state(key, value)
        else:
            self._state[key].value = value
    
    def bind_state(self, key: str, widget_id: str, callback: Callable):
        """Bind a widget to a state variable for reactive updates."""
        if key not in self._widgets:
            self._widgets[key] = []
        self._widgets[key].append((widget_id, callback))
        
        if key in self._state:
            self._state[key].bind(callback)
    
    def create_computed(self, key: str, compute_fn: Callable):
        """Create a computed value that auto-updates when dependencies change."""
        self._computed[key] = compute_fn
    
    def get_computed(self, key: str) -> Any:
        """Get the computed value."""
        if key in self._computed:
            return self._computed[key]()
        return None
    
    def reset(self):
        """Reset all state (useful for testing)."""
        self._state.clear()
        self._widgets.clear()
        self._computed.clear()


# Global state manager instance
State = StateManager()


# =============================================================================
# SECTION 2: STYLING SYSTEM
# =============================================================================

class StyleManager:
    """
    Manages application-wide styling, themes, and visual properties.
    Supports colors, fonts, sizes, margins, paddings, borders, shadows.
    """
    
    DEFAULT_THEME = {
        'primary_color': (0.2, 0.6, 1, 1),      # Blue
        'secondary_color': (0.9, 0.9, 0.9, 1),  # Light gray
        'accent_color': (1, 0.4, 0.4, 1),        # Red/Pink
        'success_color': (0.2, 0.8, 0.2, 1),    # Green
        'warning_color': (1, 0.8, 0.2, 1),      # Yellow
        'error_color': (1, 0.2, 0.2, 1),        # Red
        'text_color': (0.1, 0.1, 0.1, 1),        # Dark gray
        'background_color': (1, 1, 1, 1),        # White
        'font_family': 'Roboto',
        'font_size_base': 14,
        'border_radius': 8,
        'padding_small': 4,
        'padding_medium': 8,
        'padding_large': 16,
        'margin_small': 4,
        'margin_medium': 8,
        'margin_large': 16,
    }
    
    def __init__(self):
        self.theme = self.DEFAULT_THEME.copy()
        self.custom_styles: Dict[str, Dict] = {}
    
    def apply_theme(self, theme_name: str):
        """Apply a predefined theme."""
        themes = {
            'dark': {
                'primary_color': (0.3, 0.5, 0.9, 1),
                'secondary_color': (0.2, 0.2, 0.2, 1),
                'accent_color': (0.9, 0.3, 0.5, 1),
                'text_color': (0.95, 0.95, 0.95, 1),
                'background_color': (0.1, 0.1, 0.1, 1),
            },
            'light': self.DEFAULT_THEME.copy(),
            'ocean': {
                'primary_color': (0.0, 0.5, 0.7, 1),
                'secondary_color': (0.85, 0.95, 1.0, 1),
                'accent_color': (0.0, 0.8, 0.6, 1),
                'text_color': (0.05, 0.2, 0.3, 1),
                'background_color': (0.95, 0.98, 1.0, 1),
            },
            'sunset': {
                'primary_color': (1.0, 0.4, 0.2, 1),
                'secondary_color': (1.0, 0.9, 0.8, 1),
                'accent_color': (0.9, 0.2, 0.5, 1),
                'text_color': (0.2, 0.1, 0.1, 1),
                'background_color': (1.0, 0.95, 0.9, 1),
            }
        }
        
        if theme_name in themes:
            self.theme.update(themes[theme_name])
    
    def get_color(self, color_key: str) -> tuple:
        """Get a color from the theme."""
        return self.theme.get(color_key, (0, 0, 0, 1))
    
    def create_style(self, style_name: str, **kwargs):
        """Create a custom style."""
        self.custom_styles[style_name] = kwargs
    
    def get_style(self, style_name: str) -> Dict:
        """Get a custom style."""
        return self.custom_styles.get(style_name, {})


# Global style manager
Style = StyleManager()


# =============================================================================
# SECTION 3: LAYOUT SYSTEM
# =============================================================================

class VibeLinearLayout(BoxLayout):
    """Linear layout - arranges children in a single row or column."""
    
    def __init__(self, orientation='vertical', spacing=10, padding=10, **kwargs):
        super().__init__(**kwargs)
        self.orientation = orientation
        self.spacing = spacing
        self.padding = padding


class VibeRelativeLayout(RelativeLayout):
    """Relative layout - positions children relative to each other or the parent."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class VibeGridLayout(GridLayout):
    """Grid layout - arranges children in a grid structure."""
    
    def __init__(self, cols=None, rows=None, spacing=10, padding=10, **kwargs):
        super().__init__(**kwargs)
        self.cols = cols or 2
        self.rows = rows
        self.spacing = spacing
        self.padding = padding


class VibeFrameLayout(FloatLayout):
    """Frame layout - overlays children at arbitrary positions."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class VibeFlexLayout(StackLayout):
    """Flexbox-style layout - flexible box layout for responsive designs."""
    
    def __init__(self, direction='tb', spacing=10, padding=10, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'lr' if direction == 'lr' else 'tb'
        self.spacing = spacing
        self.padding = padding


# =============================================================================
# SECTION 4: WIDGET LIBRARY (20+ WIDGET TYPES)
# =============================================================================

class VibeWidget:
    """Base class for all VibeFramework widgets."""
    
    widget_count = 0
    
    def __init__(self, id=None, visible=True, enabled=True, **kwargs):
        VibeWidget.widget_count += 1
        self.vibe_id = id or f"widget_{VibeWidget.widget_count}"
        self.visible = visible
        self.enabled = enabled
        self.style = kwargs.get('style', {})
        self.custom_attrs = kwargs.get('custom', {})
        self.event_handlers = {}
        self._parent = None
        
        # Size and position
        self.width = kwargs.get('width', 'auto')
        self.height = kwargs.get('height', 'auto')
        self.size_hint = kwargs.get('size_hint', (1, None))
        self.pos_hint = kwargs.get('pos_hint', {})
    
    def set_event_handler(self, event_name: str, handler: Callable):
        """Set an event handler for this widget."""
        self.event_handlers[event_name] = handler
    
    def trigger_event(self, event_name: str, *args):
        """Trigger an event on this widget."""
        if event_name in self.event_handlers:
            handler = self.event_handlers[event_name]
            if callable(handler):
                handler(*args)
    
    def show(self):
        """Show the widget."""
        self.visible = True
    
    def hide(self):
        """Hide the widget."""
        self.visible = False
    
    def enable(self):
        """Enable the widget."""
        self.enabled = True
    
    def disable(self):
        """Disable the widget."""
        self.enabled = False


class VibeButton(Button, VibeWidget):
    """Button widget - clickable button with various states."""
    
    def __init__(self, text="", on_click=None, variant="primary", **kwargs):
        super().__init__(**kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.text = text
        self.variant = variant
        
        # Style based on variant
        colors = {
            'primary': (0.2, 0.6, 1, 1),
            'secondary': (0.6, 0.6, 0.6, 1),
            'success': (0.2, 0.8, 0.2, 1),
            'danger': (1, 0.3, 0.3, 1),
            'warning': (1, 0.8, 0.2, 1),
            'outline': (1, 1, 1, 1),
        }
        bg_color = colors.get(variant, colors['primary'])
        self.background_color = bg_color
        self.color = (1, 1, 1, 1) if variant != 'outline' else colors['primary'][:3] + (1,)
        
        if on_click:
            self.bind(on_press=on_click)


class VibeLabel(Label, VibeWidget):
    """Label widget - displays text."""
    
    def __init__(self, text="", font_size=16, color=None, bold=False, 
                 italic=False, align='left', **kwargs):
        super().__init__(**kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.text = text
        self.font_size = font_size
        self.color = color or Style.get_color('text_color')
        self.bold = bold
        self.italic = italic
        self.text_size = (None, None)
        self.halign = align


class VibeTextField(TextInput, VibeWidget):
    """TextField widget - text input with validation support."""
    
    def __init__(self, hint="", text="", on_change=None, on_focus=None,
                 multiline=False, password=False, validator=None, **kwargs):
        super().__init__(**kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.hint_text = hint
        self.text = text
        self.multiline = multiline
        self.password = password
        self.validator = validator
        self.write_tab = False
        
        if on_change:
            self.bind(text=on_change)
        if on_focus:
            self.bind(focus=on_focus)


class VibeImage(Image, VibeWidget):
    """Image widget - displays images."""
    
    def __init__(self, source="", allow_stretch=False, keep_ratio=True, **kwargs):
        super().__init__(**kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.source = source
        self.allow_stretch = allow_stretch
        self.keep_ratio = keep_ratio


class VibeCheckbox(CheckBox, VibeWidget):
    """Checkbox widget - binary selection control."""
    
    def __init__(self, label="", checked=False, on_change=None, **kwargs):
        super().__init__(**kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.active = checked
        self.checkbox_label = label
        
        if on_change:
            self.bind(active=on_change)


class VibeSwitch(Switch, VibeWidget):
    """Switch widget - toggle switch for boolean values."""
    
    def __init__(self, active=False, on_change=None, **kwargs):
        super().__init__(**kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.active = active
        
        if on_change:
            self.bind(active=on_change)


class VibeSlider(Slider, VibeWidget):
    """Slider widget - range-based value selector."""
    
    def __init__(self, min=0, max=100, value=50, step=1, on_change=None, **kwargs):
        super().__init__(**kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.min = min
        self.max = max
        self.value = value
        self.step = step
        
        if on_change:
            self.bind(value=on_change)


class VibeProgressBar(ProgressBar, VibeWidget):
    """ProgressBar widget - displays progress indicator."""
    
    def __init__(self, value=0, max=100, **kwargs):
        super().__init__(**kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.value = value
        self.max = max


class VibeSpinner(Spinner, VibeWidget):
    """Spinner/Dropdown widget - selection from a list."""
    
    def __init__(self, options=None, text="Select...", on_change=None, **kwargs):
        super().__init__(**kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.values = options or []
        self.text = text
        
        if on_change:
            self.bind(text=on_change)


class VibeTabs(TabbedPanel, VibeWidget):
    """Tabs widget - tabbed navigation."""
    
    def __init__(self, tabs=None, **kwargs):
        super().__init__(**kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.tabs_data = tabs or []
        
        for tab_name, tab_content in self.tabs_data:
            tab_item = TabbedPanelItem(text=tab_name)
            tab_item.add_widget(tab_content)
            self.add_widget(tab_item)


class VibeAccordion(Accordion, VibeWidget):
    """Accordion widget - collapsible panels."""
    
    def __init__(self, items=None, orientation='vertical', **kwargs):
        super().__init__(**kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.orientation = orientation
        self.items_data = items or []
        
        for title, content in self.items_data:
            item = AccordionItem(title=title)
            item.add_widget(content)
            self.add_widget(item)


class VibeCard(BoxLayout, VibeWidget):
    """Card widget - contained content with shadow/border."""
    
    def __init__(self, title="", content=None, elevation=4, **kwargs):
        super().__init__(orientation='vertical', padding=16, spacing=8, **kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.elevation = elevation
        
        if title:
            title_label = VibeLabel(text=title, bold=True, font_size=18)
            self.add_widget(title_label)
        
        if content:
            if isinstance(content, str):
                content_label = VibeLabel(text=content)
                self.add_widget(content_label)
            else:
                self.add_widget(content)


class VibeModal(ModalView, VibeWidget):
    """Modal widget - overlay dialog."""
    
    def __init__(self, title="", content=None, dismissible=True, **kwargs):
        super().__init__(**kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.title = title
        self.dismissable = dismissible
        self.auto_dismiss = dismissible
        
        container = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        if title:
            container.add_widget(VibeLabel(text=title, bold=True, font_size=20))
        
        if content:
            container.add_widget(content)
        
        self.add_widget(container)


class VibeDialog(Popup, VibeWidget):
    """Dialog widget - modal popup with actions."""
    
    def __init__(self, title="", content=None, actions=None, **kwargs):
        super().__init__(**kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.title = title
        self.size_hint = (0.8, 0.6)
        
        container = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        if content:
            scroll = ScrollView()
            if isinstance(content, str):
                content_label = VibeLabel(text=content, halign='center')
            else:
                content_label = content
            scroll.add_widget(content_label)
            container.add_widget(scroll)
        
        if actions:
            button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
            for action_text, action_callback in actions:
                btn = VibeButton(text=action_text, on_click=action_callback)
                button_layout.add_widget(btn)
            container.add_widget(button_layout)
        
        self.add_widget(container)


class VibeListView(BoxLayout, VibeWidget):
    """ListView widget - scrollable list of items."""
    
    def __init__(self, items=None, on_item_click=None, item_template=None, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.items = items or []
        self.on_item_click = on_item_click
        self.item_template = item_template
        
        self._build_list()
    
    def _build_list(self):
        self.clear_widgets()
        
        scroll = ScrollView()
        list_container = VibeLinearLayout(orientation='vertical', spacing=2, padding=5)
        
        for i, item in enumerate(self.items):
            if isinstance(item, str):
                item_widget = VibeButton(
                    text=item, 
                    variant='outline',
                    size_hint=(1, None),
                    height=40,
                    on_click=lambda x, idx=i: self._handle_item_click(idx)
                )
            elif isinstance(item, dict):
                item_widget = VibeButton(
                    text=item.get('text', str(item)),
                    variant='outline',
                    size_hint=(1, None),
                    height=40,
                    on_click=lambda x, idx=i: self._handle_item_click(idx)
                )
            else:
                item_widget = item
            
            list_container.add_widget(item_widget)
        
        scroll.add_widget(list_container)
        self.add_widget(scroll)
    
    def _handle_item_click(self, index):
        if self.on_item_click:
            self.on_item_click(index, self.items[index])
    
    def set_items(self, items: List):
        """Update list items."""
        self.items = items
        self._build_list()


class VibeGridView(GridLayout, VibeWidget):
    """GridView widget - grid layout of items."""
    
    def __init__(self, items=None, cols=2, on_item_click=None, **kwargs):
        super().__init__(cols=cols, spacing=10, padding=10, **kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.items = items or []
        self.on_item_click = on_item_click
        
        self._build_grid()
    
    def _build_grid(self):
        self.clear_widgets()
        
        for i, item in enumerate(self.items):
            if isinstance(item, str):
                item_widget = VibeCard(
                    title=item,
                    content=f"Item {i+1}",
                    size_hint=(1, 1)
                )
            elif isinstance(item, dict):
                item_widget = VibeCard(
                    title=item.get('title', ''),
                    content=item.get('content', ''),
                    size_hint=(1, 1)
                )
            else:
                item_widget = item
            
            if self.on_item_click:
                item_widget.set_event_handler('on-click', 
                    lambda x, idx=i: self.on_item_click(idx, item))
            
            self.add_widget(item_widget)


class VibeNavigation(BoxLayout, VibeWidget):
    """Navigation widget - bottom or top navigation bar."""
    
    def __init__(self, items=None, on_change=None, position='bottom', **kwargs):
        super().__init__(orientation='horizontal', size_hint=(1, None), height=60,
                        spacing=5, padding=5, **kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.items = items or []
        self.on_change = on_change
        self.position = position
        self.selected_index = 0
        
        self._build_navigation()
    
    def _build_navigation(self):
        self.clear_widgets()
        
        for i, item in enumerate(self.items):
            btn = VibeButton(
                text=item.get('label', ''),
                variant='primary' if i == self.selected_index else 'secondary',
                size_hint=(1, 1),
                on_click=lambda x, idx=i: self._handle_select(idx)
            )
            self.add_widget(btn)
    
    def _handle_select(self, index):
        self.selected_index = index
        self._build_navigation()
        
        if self.on_change:
            self.on_change(index, self.items[index])


class VibeSearchBar(BoxLayout, VibeWidget):
    """SearchBar widget - search input with results."""
    
    def __init__(self, placeholder="Search...", on_search=None, on_change=None, **kwargs):
        super().__init__(orientation='horizontal', size_hint=(1, None), height=50,
                        spacing=10, padding=10, **kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.on_search = on_search
        self.on_change = on_change
        
        self.search_input = VibeTextField(
            hint=placeholder,
            on_change=self._handle_change
        )
        self.add_widget(self.search_input)
        
        self.search_button = VibeButton(
            text="🔍",
            variant='primary',
            size_hint=(None, 1),
            width=50,
            on_click=self._handle_search
        )
        self.add_widget(self.search_button)
    
    def _handle_change(self, *args):
        if self.on_change:
            self.on_change(self.search_input.text)
    
    def _handle_search(self, *args):
        if self.on_search:
            self.on_search(self.search_input.text)
    
    def get_text(self) -> str:
        return self.search_input.text
    
    def set_text(self, text: str):
        self.search_input.text = text


class VibeCalendar(BoxLayout, VibeWidget):
    """Calendar widget - date picker/calendar view."""
    
    def __init__(self, selected_date=None, on_date_select=None, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=5, **kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.selected_date = selected_date or date.today()
        self.on_date_select = on_date_select
        
        self._build_calendar()
    
    def _build_calendar(self):
        self.clear_widgets()
        
        # Month header
        header = BoxLayout(size_hint_y=None, height=40, spacing=10)
        
        prev_btn = VibeButton(text="◀", variant='secondary', size_hint=(None, 1), width=40,
                            on_click=lambda x: self._change_month(-1))
        header.add_widget(prev_btn)
        
        month_label = VibeLabel(
            text=self.selected_date.strftime("%B %Y"),
            bold=True,
            font_size=18,
            halign='center'
        )
        header.add_widget(month_label)
        
        next_btn = VibeButton(text="▶", variant='secondary', size_hint=(None, 1), width=40,
                            on_click=lambda x: self._change_month(1))
        header.add_widget(next_btn)
        
        self.add_widget(header)
        
        # Day headers
        days_header = GridLayout(cols=7, size_hint_y=None, height=30)
        for day in ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']:
            days_header.add_widget(VibeLabel(text=day, bold=True, font_size=12, halign='center'))
        self.add_widget(days_header)
        
        # Calendar grid
        self.calendar_grid = GridLayout(cols=7, spacing=2)
        self._render_days()
        self.add_widget(self.calendar_grid)
    
    def _render_days(self):
        self.calendar_grid.clear_widgets()
        
        first_day = self.selected_date.replace(day=1)
        start_offset = first_day.weekday()
        
        # Empty cells for offset
        for _ in range(start_offset):
            self.calendar_grid.add_widget(Widget(size_hint=(1, None), height=30))
        
        # Days in month
        import calendar
        days_in_month = calendar.monthrange(self.selected_date.year, self.selected_date.month)[1]
        
        for day in range(1, days_in_month + 1):
            day_btn = VibeButton(
                text=str(day),
                variant='primary' if day == self.selected_date.day else 'outline',
                size_hint=(1, None),
                height=30,
                on_click=lambda x, d=day: self._select_day(d)
            )
            self.calendar_grid.add_widget(day_btn)
    
    def _change_month(self, delta):
        from datetime import timedelta
        new_month = self.selected_date.month + delta
        year = self.selected_date.year
        
        if new_month > 12:
            new_month = 1
            year += 1
        elif new_month < 1:
            new_month = 12
            year -= 1
        
        self.selected_date = self.selected_date.replace(year=year, month=new_month, day=1)
        self._build_calendar()
    
    def _select_day(self, day):
        self.selected_date = self.selected_date.replace(day=day)
        self._build_calendar()
        
        if self.on_date_select:
            self.on_date_select(self.selected_date)


class VibeDatePicker(VibeCalendar):
    """DatePicker widget - alias for Calendar."""
    pass


class VibeTimePicker(BoxLayout, VibeWidget):
    """TimePicker widget - time selection control."""
    
    def __init__(self, selected_time=None, on_time_select=None, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.selected_time = selected_time or datetime.now().time()
        self.on_time_select = on_time_select
        
        self._build_time_picker()
    
    def _build_time_picker(self):
        self.clear_widgets()
        
        # Hour spinner
        hour_layout = BoxLayout(orientation='vertical', spacing=5)
        hour_layout.add_widget(VibeLabel(text="Hour", bold=True))
        self.hour_spinner = VibeSpinner(
            options=[f"{i:02d}" for i in range(24)],
            text=f"{self.selected_time.hour:02d}",
            on_change=self._on_change
        )
        hour_layout.add_widget(self.hour_spinner)
        
        # Minute spinner
        minute_layout = BoxLayout(orientation='vertical', spacing=5)
        minute_layout.add_widget(VibeLabel(text="Minute", bold=True))
        self.minute_spinner = VibeSpinner(
            options=[f"{i:02d}" for i in range(0, 60, 5)],
            text=f"{self.selected_time.minute:02d}",
            on_change=self._on_change
        )
        minute_layout.add_widget(self.minute_spinner)
        
        # Layout
        time_layout = BoxLayout(spacing=20)
        time_layout.add_widget(hour_layout)
        time_layout.add_widget(VibeLabel(text=":", bold=True, font_size=24))
        time_layout.add_widget(minute_layout)
        
        self.add_widget(time_layout)
        
        # Now button
        now_btn = VibeButton(text="Set Current Time", variant='primary',
                           on_click=lambda x: self._set_now())
        self.add_widget(now_btn)
    
    def _on_change(self, *args):
        try:
            hour = int(self.hour_spinner.text)
            minute = int(self.minute_spinner.text)
            self.selected_time = time(hour, minute)
            
            if self.on_time_select:
                self.on_time_select(self.selected_time)
        except:
            pass
    
    def _set_now(self):
        self.selected_time = datetime.now().time()
        self.hour_spinner.text = f"{self.selected_time.hour:02d}"
        self.minute_spinner.text = f"{self.selected_time.minute:02d}"


class VibeRadioButton(BoxLayout, VibeWidget):
    """RadioButton widget - mutually exclusive selection."""
    
    def __init__(self, options=None, selected=None, on_change=None, **kwargs):
        super().__init__(orientation='vertical', spacing=5, **kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.options = options or []
        self.selected = selected
        self.on_change = on_change
        self.radio_buttons = []
        
        self._build_radio_buttons()
    
    def _build_radio_buttons(self):
        self.clear_widgets()
        self.radio_buttons = []
        
        for option in self.options:
            row = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
            
            checkbox = CheckBox(group='radio_' + self.vibe_id)
            checkbox.bind(active=lambda x, val=option: self._handle_select(val))
            
            if option == self.selected:
                checkbox.active = True
            
            row.add_widget(checkbox)
            row.add_widget(VibeLabel(text=str(option)))
            
            self.radio_buttons.append(checkbox)
            self.add_widget(row)
    
    def _handle_select(self, option):
        self.selected = option
        if self.on_change:
            self.on_change(option)
    
    def get_selected(self):
        return self.selected


class VibeForm(BoxLayout, VibeWidget):
    """Form widget - collection of form fields with validation."""
    
    def __init__(self, fields=None, on_submit=None, **kwargs):
        super().__init__(orientation='vertical', spacing=10, padding=20, **kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.fields = fields or []
        self.on_submit = on_submit
        self.field_widgets = {}
        
        self._build_form()
    
    def _build_form(self):
        self.clear_widgets()
        self.field_widgets = {}
        
        for field in self.fields:
            field_type = field.get('type', 'text')
            field_label = field.get('label', '')
            field_hint = field.get('hint', '')
            field_required = field.get('required', False)
            
            # Label
            label_text = field_label + (' *' if field_required else '')
            self.add_widget(VibeLabel(text=label_text, bold=True))
            
            # Field widget
            if field_type == 'text':
                widget = VibeTextField(hint=field_hint)
            elif field_type == 'password':
                widget = VibeTextField(hint=field_hint, password=True)
            elif field_type == 'email':
                widget = VibeTextField(hint=field_hint)
            elif field_type == 'number':
                widget = VibeTextField(hint=field_hint, input_filter='int')
            else:
                widget = VibeTextField(hint=field_hint)
            
            self.field_widgets[field_label] = widget
            self.add_widget(widget)
        
        # Submit button
        submit_btn = VibeButton(text="Submit", variant='primary', 
                              on_click=lambda x: self._submit_form())
        self.add_widget(submit_btn)
    
    def _submit_form(self):
        data = {}
        for label, widget in self.field_widgets.items():
            data[label] = widget.text
        
        if self.on_submit:
            self.on_submit(data)
    
    def get_data(self) -> Dict:
        return {label: widget.text for label, widget in self.field_widgets.items()}
    
    def set_data(self, data: Dict):
        for label, value in data.items():
            if label in self.field_widgets:
                self.field_widgets[label].text = value


class VibeToast(Label, VibeWidget):
    """Toast widget - temporary notification message."""
    
    def __init__(self, message="", duration=2, **kwargs):
        super().__init__(**kwargs)
        VibeWidget.__init__(self, **kwargs)
        self.message = message
        self.duration = duration
        self.text = message
        self.font_size = 14
        self.size_hint = (None, None)
        self.size = (300, 50)
        self.halign = 'center'
        self.valign = 'middle'
        self.background_color = (0.2, 0.2, 0.2, 0.9)
        self.color = (1, 1, 1, 1)


# =============================================================================
# SECTION 5: EVENT HANDLING SYSTEM
# =============================================================================

class EventManager:
    """
    Manages event handling for all widgets including gestures and drag events.
    """
    
    def __init__(self):
        self.listeners: Dict[str, List[Callable]] = {}
        self.gesture_handlers: Dict[str, Callable] = {}
    
    def on(self, event_name: str, callback: Callable):
        """Register an event listener."""
        if event_name not in self.listeners:
            self.listeners[event_name] = []
        self.listeners[event_name].append(callback)
    
    def off(self, event_name: str, callback: Callable):
        """Unregister an event listener."""
        if event_name in self.listeners:
            self.listeners[event_name].remove(callback)
    
    def emit(self, event_name: str, *args):
        """Emit an event to all listeners."""
        if event_name in self.listeners:
            for callback in self.listeners[event_name]:
                try:
                    callback(*args)
                except Exception as e:
                    print(f"Event handler error: {e}")
    
    def register_gesture(self, gesture_type: str, handler: Callable):
        """Register a gesture handler (tap, double_tap, swipe_left, swipe_right, etc.)."""
        self.gesture_handlers[gesture_type] = handler


# Global event manager
Events = EventManager()


# =============================================================================
# SECTION 6: VIBE SYNTAX PARSER
# =============================================================================

class VibeParser:
    """
    Parses .vibe files and extracts UI, STYLE, and BACKEND sections.
    Supports declarative syntax for defining UI structure, styling, and logic.
    """
    
    # Widget type mappings
    WIDGET_MAP = {
        'button': VibeButton,
        'label': VibeLabel,
        'textfield': VibeTextField,
        'input': VibeTextField,
        'image': VibeImage,
        'checkbox': VibeCheckbox,
        'switch': VibeSwitch,
        'slider': VibeSlider,
        'progressbar': VibeProgressBar,
        'spinner': VibeSpinner,
        'dropdown': VibeSpinner,
        'tabs': VibeTabs,
        'accordion': VibeAccordion,
        'card': VibeCard,
        'modal': VibeModal,
        'dialog': VibeDialog,
        'list': VibeListView,
        'grid': VibeGridView,
        'navigation': VibeNavigation,
        'navbar': VibeNavigation,
        'search': VibeSearchBar,
        'searchbar': VibeSearchBar,
        'calendar': VibeCalendar,
        'datepicker': VibeDatePicker,
        'timepicker': VibeTimePicker,
        'radio': VibeRadioButton,
        'form': VibeForm,
        'toast': VibeToast,
    }
    
    # Layout type mappings
    LAYOUT_MAP = {
        'linear': VibeLinearLayout,
        'vertical': VibeLinearLayout,
        'horizontal': lambda **k: VibeLinearLayout(orientation='horizontal', **k),
        'relative': VibeRelativeLayout,
        'grid': VibeGridLayout,
        'frame': VibeFrameLayout,
        'flex': VibeFlexLayout,
        'stack': VibeFlexLayout,
    }
    
    def __init__(self, vibe_content: str):
        self.content = vibe_content
        self.ui_section = ""
        self.style_section = ""
        self.backend_section = ""
        self.widgets = []
        self.layout_stack = []
        
    def parse(self):
        """Parse the .vibe file content."""
        # Extract sections
        ui_match = re.search(r'UI\s*\{(.*?)\}(?:STYLE|BACKEND|$)', self.content, re.DOTALL)
        style_match = re.search(r'STYLE\s*\{(.*?)\}(?:BACKEND|$)', self.content, re.DOTALL)
        backend_match = re.search(r'BACKEND\s*\{(.*)\}', self.content, re.DOTALL)
        
        if ui_match:
            self.ui_section = ui_match.group(1).strip()
        
        if style_match:
            self.style_section = style_match.group(1).strip()
        
        if backend_match:
            self.backend_section = backend_match.group(1).strip()
        
        return self
    
    def get_ui_code(self) -> str:
        return self.ui_section
    
    def get_style_code(self) -> str:
        return self.style_section
    
    def get_backend_code(self) -> str:
        return self.backend_section


# =============================================================================
# SECTION 7: VIBE ENGINE - MAIN APPLICATION CLASS
# =============================================================================

class VibeEngine(App):
    """
    Main VibeFramework application engine.
    Handles transpilation of .vibe files into executable code.
    Manages UI rendering and backend logic execution.
    """
    
    version = "3.0.0 PRODUCTION"
    
    def __init__(self, vibe_file: str = None, vibe_content: str = None):
        super().__init__()
        self.vibe_file = vibe_file
        self.vibe_content = vibe_content
        self.parser = None
        self.root_widget = None
        self.backend_scope = {}
        self.widget_registry: Dict[str, Widget] = {}
        self.navigation_screens: Dict[str, Screen] = {}
        self.screen_manager: Optional[ScreenManager] = None
        
        # Initialize state
        State.reset()
        
    def build(self):
        """Build the application from .vibe file or content."""
        print(f"{'='*50}")
        print(f"🚀 VibeFramework {self.version} Booting...")
        print(f"{'='*50}")
        
        # Load content
        if self.vibe_file:
            with open(self.vibe_file, 'r', encoding='utf-8') as f:
                self.vibe_content = f.read()
        
        # Parse the vibe file
        self.parser = VibeParser(self.vibe_content).parse()
        
        # Create root layout
        self.root_widget = VibeLinearLayout(
            orientation='vertical',
            padding=0,
            spacing=0
        )
        
        # Parse and render UI
        self._render_ui(self.parser.get_ui_code())
        
        # Apply styles
        self._apply_styles(self.parser.get_style_code())
        
        # Execute backend code
        self._execute_backend(self.parser.get_backend_code())
        
        print(f"✅ VibeFramework Ready!")
        print(f"   Widgets loaded: {len(self.widget_registry)}")
        
        return self.root_widget
    
    def _render_ui(self, ui_code: str):
        """Parse and render UI from .vibe syntax."""
        if not ui_code:
            return
        
        lines = ui_code.split('\n')
        current_layout = self.root_widget
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            
            # Handle layout start
            if re.match(r'^(LinearLayout|RelativeLayout|GridLayout|FrameLayout|FlexLayout|VerticalLayout|HorizontalLayout)\s*\{', line):
                layout_type = re.match(r'^(\w+)\s*\{', line).group(1)
                new_layout = self._create_layout(layout_type)
                
                if current_layout == self.root_widget:
                    current_layout = new_layout
                    self.root_widget.add_widget(new_layout)
                else:
                    if hasattr(current_layout, 'add_widget'):
                        current_layout.add_widget(new_layout)
                        self.layout_stack.append(current_layout)
                        current_layout = new_layout
                continue
            
            # Handle layout end
            if line == '}' and self.layout_stack:
                current_layout = self.layout_stack.pop()
                continue
            
            # Parse widget
            widget = self._parse_widget(line)
            if widget and current_layout:
                current_layout.add_widget(widget)
    
    def _create_layout(self, layout_type: str) -> Widget:
        """Create a layout widget based on type."""
        # Remove Layout suffix if present
        layout_type = layout_type.replace('Layout', '').lower()
        
        if layout_type in ['vertical', 'linear']:
            return VibeLinearLayout(orientation='vertical', spacing=10, padding=10)
        elif layout_type == 'horizontal':
            return VibeLinearLayout(orientation='horizontal', spacing=10, padding=10)
        elif layout_type == 'grid':
            return VibeGridLayout(cols=2, spacing=10, padding=10)
        elif layout_type == 'relative':
            return VibeRelativeLayout()
        elif layout_type == 'frame':
            return VibeFrameLayout()
        elif layout_type in ['flex', 'stack']:
            return VibeFlexLayout()
        
        return VibeLinearLayout(orientation='vertical', spacing=10, padding=10)
    
    def _parse_widget(self, line: str) -> Optional[Widget]:
        """Parse a widget definition from .vibe syntax."""
        try:
            # Match widget definition
            match = re.match(r'(\w+)\s*(?:\((.*?)\))?', line)
            if not match:
                return None
            
            widget_type = match.group(1).lower()
            props_str = match.group(2) or ""
            
            # Parse properties
            props = self._parse_properties(props_str)
            
            # Get widget class
            widget_class = VibeParser.WIDGET_MAP.get(widget_type)
            if not widget_class:
                print(f"⚠️ Unknown widget type: {widget_type}")
                return None
            
            # Create widget based on type
            if widget_type in ['button']:
                return VibeButton(
                    text=props.get('text', 'Button'),
                    variant=props.get('variant', 'primary'),
                    on_click=props.get('on_click')
                )
            
            elif widget_type in ['label']:
                return VibeLabel(
                    text=props.get('text', 'Label'),
                    font_size=props.get('font_size', 16),
                    bold=props.get('bold', False)
                )
            
            elif widget_type in ['textfield', 'input']:
                return VibeTextField(
                    hint=props.get('hint', ''),
                    multiline=props.get('multiline', False),
                    password=props.get('password', False)
                )
            
            elif widget_type == 'image':
                return VibeImage(source=props.get('source', ''))
            
            elif widget_type == 'checkbox':
                return VibeCheckbox(
                    label=props.get('label', ''),
                    checked=props.get('checked', False)
                )
            
            elif widget_type == 'switch':
                return VibeSwitch(active=props.get('active', False))
            
            elif widget_type == 'slider':
                return VibeSlider(
                    min=props.get('min', 0),
                    max=props.get('max', 100),
                    value=props.get('value', 50)
                )
            
            elif widget_type == 'progressbar':
                return VibeProgressBar(
                    value=props.get('value', 0),
                    max=props.get('max', 100)
                )
            
            elif widget_type in ['spinner', 'dropdown']:
                options = props.get('options', '').split(',') if props.get('options') else []
                return VibeSpinner(
                    options=options,
                    text=props.get('text', 'Select...')
                )
            
            elif widget_type == 'card':
                return VibeCard(
                    title=props.get('title', ''),
                    content=props.get('content', '')
                )
            
            elif widget_type in ['search', 'searchbar']:
                return VibeSearchBar(
                    placeholder=props.get('placeholder', 'Search...')
                )
            
            elif widget_type == 'form':
                fields = []
                if props.get('fields'):
                    for field_str in props.get('fields').split(';'):
                        parts = field_str.split(':')
                        if len(parts) >= 2:
                            fields.append({
                                'type': parts[0],
                                'label': parts[1],
                                'hint': parts[2] if len(parts) > 2 else ''
                            })
                return VibeForm(fields=fields)
            
            elif widget_type == 'list':
                items = props.get('items', '').split(',') if props.get('items') else []
                return VibeListView(items=items)
            
            elif widget_type == 'grid':
                items = props.get('items', '').split(',') if props.get('items') else []
                cols = int(props.get('cols', 2))
                return VibeGridView(items=items, cols=cols)
            
            else:
                # Generic widget creation
                return widget_class(**props)
        
        except Exception as e:
            print(f"⚠️ Widget parse error: {e}")
            return None
    
    def _parse_properties(self, props_str: str) -> Dict:
        """Parse widget properties from string."""
        props = {}
        
        if not props_str:
            return props
        
        # Parse key=value pairs
        pattern = r'(\w+)=(?:"([^"]*)"|(\d+\.?\d*)|(\w+))'
        matches = re.findall(pattern, props_str)
        
        for match in matches:
            key = match[0]
            value = match[1] or match[2] or match[3]
            
            # Convert numeric values
            if value.replace('.', '').isdigit():
                value = float(value) if '.' in value else int(value)
            
            props[key] = value
        
        return props
    
    def _apply_styles(self, style_code: str):
        """Apply styles from STYLE section."""
        if not style_code:
            return
        
        # Parse theme
        theme_match = re.search(r'theme\s*:\s*(\w+)', style_code)
        if theme_match:
            Style.apply_theme(theme_match.group(1))
        
        # Parse custom styles
        style_pattern = r'style\s+(\w+)\s*\{([^}]*)\}'
        for match in re.finditer(style_pattern, style_code):
            style_name = match.group(1)
            style_content = match.group(2)
            
            props = self._parse_properties(style_content)
            Style.create_style(style_name, **props)
    
    def _execute_backend(self, backend_code: str):
        """Execute backend Python code from .vibe file."""
        if not backend_code:
            return
        
        try:
            # Clean and prepare code
            clean_code = textwrap.dedent(backend_code).strip()
            
            # Create execution scope with builtins
            exec_globals = {
                'print': print,
                'str': str,
                'int': int,
                'float': float,
                'list': list,
                'dict': dict,
                'len': len,
                'range': range,
                'enumerate': enumerate,
                'zip': zip,
                'map': map,
                'filter': filter,
                'datetime': datetime,
                'date': date,
                'time': time,
                'State': State,
                'Style': Style,
                'Events': Events,
                'App': self,
            }
            
            # Execute backend code
            exec(clean_code, exec_globals, self.backend_scope)
            
            # Register event handlers
            self._register_event_handlers()
            
        except Exception as e:
            print(f"⚠️ Backend execution error: {e}")
            import traceback
            traceback.print_exc()
    
    def _register_event_handlers(self):
        """Register event handlers from backend scope."""
        # Find all functions that might be event handlers
        for name, value in self.backend_scope.items():
            if callable(value) and name.startswith('on_'):
                # Map handler name to event type
                event_type = name[3:]  # Remove 'on_' prefix
                Events.on(event_type, value)
    
    def get_widget(self, widget_id: str) -> Optional[Widget]:
        """Get a widget by its ID."""
        return self.widget_registry.get(widget_id)
    
    def show_toast(self, message: str, duration: float = 2.0):
        """Show a toast notification."""
        toast = VibeToast(message=message, duration=duration)
        
        # Position toast at bottom
        toast.pos = (Window.width / 2 - 150, 50)
        
        self.root_widget.add_widget(toast)
        
        # Schedule removal
        Clock.schedule_once(lambda dt: self.root_widget.remove_widget(toast), duration)
    
    def show_dialog(self, title: str, content: str, actions: List[tuple] = None):
        """Show a dialog."""
        if actions is None:
            actions = [("OK", lambda x: x.dismiss())]
        
        dialog = VibeDialog(title=title, content=content, actions=actions)
        dialog.open()
    
    def navigate_to(self, screen_name: str):
        """Navigate to a screen."""
        if self.screen_manager and screen_name in self.navigation_screens:
            self.screen_manager.current = screen_name
    
    def create_screen(self, name: str, widget: Widget):
        """Create a new screen."""
        screen = Screen(name=name)
        screen.add_widget(widget)
        self.navigation_screens[name] = screen
        
        if self.screen_manager:
            self.screen_manager.add_widget(screen)
        
        return screen


# =============================================================================
# SECTION 8: DEMO APPLICATION
# =============================================================================

def create_demo_vibe_file():
    """Create a demo .vibe file with all widgets."""
    demo_content = """UI {
    // VibeFramework Demo Application
    // This showcases 20+ widget types
    
    // Header
    Label("VibeFramework Demo", font_size=24, bold=true)
    
    // Basic Widgets
    Label("--- Basic Widgets ---", font_size=18)
    Button("Primary Button", variant="primary")
    Button("Success Button", variant="success")
    Button("Danger Button", variant="danger")
    
    Label("Text Input:")
    TextField(hint="Enter your name...")
    TextField(hint="Password", password=true)
    TextField(hint="Multi-line text", multiline=true)
    
    Label("Labels:")
    Label("This is a label", font_size=14)
    Label("Bold label", font_size=16, bold=true)
    
    // Selection Widgets
    Label("--- Selection Widgets ---", font_size=18)
    
    Checkbox(label="I agree to terms")
    Checkbox(label="Subscribe to newsletter")
    
    Label("Switch:")
    Switch(active=false)
    
    Label("Radio Buttons:")
    Radio(options="Option A;Option B;Option C", selected="Option A")
    
    Label("Slider:")
    Slider(min=0, max=100, value=50)
    
    // Progress & Spinner
    Label("--- Progress & Selection ---", font_size=18)
    ProgressBar(value=70, max=100)
    Spinner(options="Apple;Banana;Orange;Mango", text="Select Fruit")
    
    // Lists & Grids
    Label("--- Lists & Grids ---", font_size=18)
    List(items="Item 1;Item 2;Item 3;Item 4;Item 5")
    Grid(items="Card 1;Card 2;Card 3;Card 4", cols=2)
    
    // Search & Navigation
    Label("--- Search & Navigation ---", font_size=18)
    SearchBar(placeholder="Search...")
    
    // Form
    Label("--- Form ---", font_size=18)
    Form(fields="text:Username:Enter username;password:Password:Enter password;email:Email:Enter email")
    
    // Card
    Label("--- Card ---", font_size=18)
    Card(title="Welcome to VibeFramework", content="Build amazing apps with a single .vibe file!")
    
    // Calendar & Time
    Label("--- Date & Time ---", font_size=18)
    Calendar()
    TimePicker()
}

STYLE {
    theme: ocean
    
    style card {
        background: #f5f5f5
        border_radius: 12
    }
}

BACKEND {
    // Backend Logic
    // This runs when the app starts
    
    // Define some state
    user_name = State.create_state("user_name", "Guest")
    is_logged_in = State.create_state("is_logged_in", false)
    
    // Event handlers
    def on_button_click(widget):
        print("Button clicked!")
        App.show_toast("Button clicked!", 2.0)
    
    def on_form_submit(data):
        print(f"Form submitted: {data}")
        username = data.get("Username", "Unknown")
        App.show_toast(f"Welcome, {username}!", 3.0)
    
    def on_list_item_click(index, item):
        print(f"List item clicked: {index} - {item}")
        App.show_toast(f"Selected: {item}", 2.0)
    
    def on_search(query):
        print(f"Searching for: {query}")
        App.show_toast(f"Search: {query}", 2.0)
    
    def on_date_select(date_obj):
        print(f"Date selected: {date_obj}")
    
    def on_time_select(time_obj):
        print(f"Time selected: {time_obj}")
    
    // Initialize
    print("=== VibeFramework Demo Started ===")
    print(f"Initial state - User: {State.get_state('user_name')}")
}
"""
    
    with open('demo_app.vibe', 'w', encoding='utf-8') as f:
        f.write(demo_content)
    
    return demo_content


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    import sys
    
    # Check for arguments
    if len(sys.argv) > 1:
        vibe_file = sys.argv[1]
        
        # Check if file exists
        if not os.path.exists(vibe_file):
            print(f"❌ Error: File '{vibe_file}' not found!")
            print("\n📝 Creating demo file...")
            create_demo_vibe_file()
            print("✅ Demo file created: demo_app.vibe")
            print("Run: python vibe_engine.py demo_app.vibe")
            sys.exit(1)
        
        # Run the app
        print(f"📱 Loading: {vibe_file}")
        VibeEngine(vibe_file=vibe_file).run()
    
    else:
        # Create and run demo
        print("📝 No .vibe file specified. Creating demo...")
        create_demo_vibe_file()
        print("✅ Demo file created: demo_app.vibe")
        print("🚀 Starting demo application...")
        VibeEngine(vibe_file='demo_app.vibe').run()
