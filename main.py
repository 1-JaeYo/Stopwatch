import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt


class Stopwatch(QWidget):
    """
    A simple stopwatch application built using PyQt5.

    Features:
    - Start, stop, and reset the stopwatch.
    - Displays elapsed time in the format HH:MM:SS:MS.
    """

    def __init__(self):
        """
        Initializes the stopwatch UI and core functionalities.
        """
        super().__init__()
        # Initialize time to zero
        self.time = QTime(0, 0, 0, 0)

        # Label to display the time
        self.time_label = QLabel("00:00:00.00", self)

        # Buttons for controlling the stopwatch
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)

        # Timer to update the stopwatch at regular intervals
        self.timer = QTimer(self)

        # Set up the user interface
        self.initUI()

    def initUI(self):
        """
        Sets up the user interface for the stopwatch.
        """
        self.setWindowTitle("Stopwatch")

        # Vertical layout to organize the time label and buttons
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        # Align the time label to the center
        self.time_label.setAlignment(Qt.AlignCenter)

        # Set style for the time label
        self.time_label.setStyleSheet("""
            font-size: 120px;
            font-family: 'Courier New', monospace;
            background-color: hsl(200, 100%, 85%);
            border-radius: 20px;
        """)

        # Horizontal layout for buttons
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        # Add the horizontal layout (buttons) to the vertical layout
        vbox.addLayout(hbox)

        # Apply layout to the widget
        self.setLayout(vbox)

        # Apply styles to buttons
        self.setStyleSheet("""
            QPushButton, QLabel {
                padding: 20px;
                font-weight: bold;
            }
            QPushButton {
                font-size: 50px;
            }
        """)

        # Connect button clicks to their respective functions
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        # Connect the timer's timeout signal to the display update function
        self.timer.timeout.connect(self.update_display)

    def start(self):
        """
        Starts the stopwatch timer.
        """
        self.timer.start(10)  # Timer updates every 10 milliseconds

    def stop(self):
        """
        Stops the stopwatch timer.
        """
        self.timer.stop()

    def reset(self):
        """
        Resets the stopwatch to its initial state.
        """
        self.timer.stop()  # Stop the timer
        self.time = QTime(0, 0, 0, 0)  # Reset the time
        self.time_label.setText(self.format_time(self.time))  # Update the display

    def format_time(self, time):
        """
        Formats the QTime object into a string representation.

        Args:
            time (QTime): The time object to format.

        Returns:
            str: Time formatted as "HH:MM:SS.MS".
        """
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        """
        Updates the stopwatch display by adding 10 milliseconds to the current time.
        """
        self.time = self.time.addMSecs(10)  # Add 10 milliseconds
        self.time_label.setText(self.format_time(self.time))  # Update the time label


if __name__ == "__main__":
    # Create the PyQt application
    app = QApplication(sys.argv)

    # Create and display the stopwatch widget
    stopwatch = Stopwatch()
    stopwatch.show()

    # Execute the application event loop
    sys.exit(app.exec_())
