import sys
import unittest
from unittest.mock import MagicMock, patch
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

# Create QApplication instance for testing
app = QApplication(sys.argv)

class TestKScratchP(unittest.TestCase):
    """Test suite for KScratchP plugin components."""

    def setUp(self):
        """Set up test fixtures before each test method."""
        # Mock Krita instance and required components
        self.mock_krita = MagicMock()
        self.mock_window = MagicMock()
        self.mock_view = MagicMock()
        self.mock_document = MagicMock()
        
        # Set up the mock chain
        self.mock_krita.activeWindow.return_value = self.mock_window
        self.mock_window.activeView.return_value = self.mock_view
        self.mock_view.document.return_value = self.mock_document
        
        # Patch Krita.instance()
        self.patcher = patch('krita.Krita.instance')
        self.mock_krita_instance = self.patcher.start()
        self.mock_krita_instance.return_value = self.mock_krita
        
        # Import our plugin modules after patching
        from .kscratchp_widget import KScratchPWidget
        from .kscratchp_utils import (validate_mode, calculate_zoom_factor,
                                    calculate_brush_size, format_brush_size)
        
        # Create widget instance
        self.widget = KScratchPWidget()

    def tearDown(self):
        """Clean up after each test method."""
        self.patcher.stop()
        self.widget.deleteLater()

    def test_initialization(self):
        """Test proper widget initialization."""
        self.assertEqual(self.widget.windowTitle(), "KScratchP")
        self.assertTrue(hasattr(self.widget, 'scratchpad'))
        self.assertTrue(hasattr(self.widget, 'history_list'))

    def test_mode_switching(self):
        """Test mode switching functionality."""
        # Test painting mode
        self.widget._set_mode('painting')
        self.assertTrue(self.widget.draw_button.isChecked())
        self.assertFalse(self.widget.pan_button.isChecked())
        self.assertFalse(self.widget.sample_button.isChecked())
        
        # Test panning mode
        self.widget._set_mode('panning')
        self.assertFalse(self.widget.draw_button.isChecked())
        self.assertTrue(self.widget.pan_button.isChecked())
        self.assertFalse(self.widget.sample_button.isChecked())
        
        # Test color sampling mode
        self.widget._set_mode('colorsampling')
        self.assertFalse(self.widget.draw_button.isChecked())
        self.assertFalse(self.widget.pan_button.isChecked())
        self.assertTrue(self.widget.sample_button.isChecked())

    def test_zoom_control(self):
        """Test zoom control functionality."""
        initial_zoom = self.widget.zoom_spin.value()
        
        # Test zoom in
        self.widget._handle_zoom_change(initial_zoom * 2)
        self.assertEqual(self.widget.zoom_spin.value(), initial_zoom * 2)
        
        # Test zoom out
        self.widget._handle_zoom_change(initial_zoom / 2)
        self.assertEqual(self.widget.zoom_spin.value(), initial_zoom / 2)
        
        # Test zoom constraints
        self.widget._handle_zoom_change(1)  # Should be constrained to minimum
        self.assertGreaterEqual(self.widget.zoom_spin.value(), 10)
        
        self.widget._handle_zoom_change(2000)  # Should be constrained to maximum
        self.assertLessEqual(self.widget.zoom_spin.value(), 1000)

    def test_brush_size_control(self):
        """Test brush size control functionality."""
        initial_size = self.widget.brush_slider.value()
        
        # Test size increase
        new_size = initial_size + 10
        self.widget._handle_brush_size_change(new_size)
        self.assertEqual(self.widget.brush_slider.value(), new_size)
        
        # Test size decrease
        new_size = initial_size - 10
        self.widget._handle_brush_size_change(new_size)
        self.assertEqual(self.widget.brush_slider.value(), new_size)
        
        # Test size constraints
        self.widget._handle_brush_size_change(0)  # Should be constrained to minimum
        self.assertGreaterEqual(self.widget.brush_slider.value(), 1)
        
        self.widget._handle_brush_size_change(101)  # Should be constrained to maximum
        self.assertLessEqual(self.widget.brush_slider.value(), 100)

    def test_history_logging(self):
        """Test history logging functionality."""
        initial_count = self.widget.history_list.count()
        test_message = "Test action performed"
        
        self.widget.log_history(test_message)
        
        self.assertEqual(self.widget.history_list.count(), initial_count + 1)
        self.assertEqual(
            self.widget.history_list.item(self.widget.history_list.count() - 1).text(),
            test_message
        )

    def test_fill_options(self):
        """Test background fill options."""
        # Test each fill option
        fill_options = ["Background Color", "Foreground Color", 
                       "Transparent", "Gradient"]
        
        for option in fill_options:
            self.widget._handle_fill_change(option)
            # Verify that appropriate method was called on scratchpad
            if option == "Background Color":
                self.widget.scratchpad.fillBackground.assert_called_once()
            elif option == "Foreground Color":
                self.widget.scratchpad.fillForeground.assert_called_once()
            elif option == "Transparent":
                self.widget.scratchpad.fillTransparent.assert_called_once()
            elif option == "Gradient":
                self.widget.scratchpad.fillGradient.assert_called_once()

    def test_canvas_changed(self):
        """Test canvas change handling."""
        # Test with valid canvas
        mock_canvas = MagicMock()
        self.widget.canvasChanged(mock_canvas)
        self.assertTrue(self.widget.isEnabled())
        
        # Test with no canvas
        self.widget.canvasChanged(None)
        self.assertFalse(self.widget.isEnabled())

    def test_event_filtering(self):
        """Test event filtering for mouse wheel and modifier keys."""
        # Create mock wheel event
        mock_wheel_event = MagicMock()
        mock_wheel_event.type.return_value = Qt.WheelEvent
        mock_wheel_event.angleDelta().y.return_value = 120
        
        # Test zoom with Ctrl pressed
        self.widget.ctrl_pressed = True
        self.widget.alt_pressed = False
        initial_zoom = self.widget.zoom_spin.value()
        self.widget.eventFilter(self.widget.scratchpad, mock_wheel_event)
        self.assertNotEqual(self.widget.zoom_spin.value(), initial_zoom)
        
        # Test brush size with Alt pressed
        self.widget.ctrl_pressed = False
        self.widget.alt_pressed = True
        initial_size = self.widget.brush_slider.value()
        self.widget.eventFilter(self.widget.scratchpad, mock_wheel_event)
        self.assertNotEqual(self.widget.brush_slider.value(), initial_size)

if __name__ == '__main__':
    unittest.main()
