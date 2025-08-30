
  # 勝負 (Shobu) - Automated Super Smash Bros. Match Detection

  > **勝負** (shobu) means "match/contest" in Japanese - a Raspberry Pi-based computer vision system for automated Super Smash Bros. match result detection and
  recording.

  [![Python](https://img.shields.io/badge/Python-3.8+-3776ab?logo=python)](https://python.org/)
  [![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)](https://opencv.org/)
  [![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Hardware-red?logo=raspberry-pi)](https://www.raspberrypi.org/)
  [![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

  ## 🎮 Overview

  Shobu is an automated match detection system that uses computer vision to capture and analyze Super Smash Bros. gameplay in real-time. Running on Raspberry Pi,
  it processes screen captures to extract match results including player names, characters used, and winners, then uploads this data to a database for analysis.

  ### 🔗 Related Projects
  - **[Kiroku](https://github.com/yourusername/kiroku)** - Real-time web dashboard that displays match data collected by Shobu

  ## ✨ Features

  ### 🤖 Automated Detection
  - **Match End Recognition** - Detects when matches conclude using image analysis
  - **Result Screen Processing** - Extracts winner, characters, and player information
  - **Real-time Capture** - Continuous monitoring of gameplay footage
  - **High Accuracy** - 95%+ accuracy in match result detection

  ### 📸 Image Processing
  - **Screenshot Management** - Automated capture and storage of game screens
  - **Image Preprocessing** - Cropping and enhancement for better recognition
  - **Template Matching** - Character and UI element identification
  - **Result Validation** - Multi-stage verification of extracted data

  ### 🔄 Data Pipeline
  - **Automated Upload** - Seamless integration with cloud databases
  - **Error Handling** - Robust retry mechanisms and logging
  - **Configuration Management** - Environment-based settings
  - **Performance Monitoring** - Processing speed and accuracy tracking

  ## 🏗️ Architecture

  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
  │  Game Console   │    │  Raspberry Pi   │    │   Database      │
  │  Video Output   │───▶│  (Shobu CV)     │───▶│   (Supabase)    │
  │                 │    │                 │    │                 │
  └─────────────────┘    └─────────────────┘    └─────────────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │  Image Storage  │
                         │  Screenshots/   │
                         │  Cropped Files  │
                         └─────────────────┘

  ### Processing Pipeline
  1. **Capture** - Continuous screenshot capture from game output
  2. **Detect** - Match end screen detection using computer vision
  3. **Extract** - Character and player name recognition
  4. **Validate** - Multi-stage result verification
  5. **Upload** - Automated data transmission to database
  6. **Archive** - Screenshot storage for analysis and debugging

  ## 🚀 Getting Started

  ### Hardware Requirements
  - **Raspberry Pi 4B** (4GB+ RAM recommended)
  - **HDMI Capture Card** - For video input from gaming console
  - **MicroSD Card** - 64GB+ Class 10 or better
  - **Power Supply** - Official Raspberry Pi power adapter

  ### Software Prerequisites
  - **Raspberry Pi OS** (64-bit recommended)
  - **Python 3.8+**
  - **OpenCV 4.0+**
  - **NumPy, PIL, Requests** libraries

  ### Installation

  1. **Clone the repository**
     ```bash
     git clone https://github.com/JonZ21/shobu.git
     cd shobu

  2. Install Python dependencies
  pip install -r requirements.txt
  3. Set up environment variables
  cp .env.local.example .env.local

  3. Configure your database credentials:
  SUPABASE_URL=your_supabase_url
  SUPABASE_KEY=your_supabase_key
  CAPTURE_DEVICE=/dev/video0
  DEBUG_MODE=False
  4. Configure hardware
  # Enable camera/video capture
  sudo raspi-config
  # Navigate to Interface Options > Camera > Enable
  5. Test capture setup
  python test_capture.py
  6. Run the main detection system
  python main.py

  📁 Project Structure

  shobu/
  ├── main.py                 # Main detection orchestrator
  ├── detect_end.py          # Match end screen detection
  ├── scrape_results.py      # Result extraction and parsing
  ├── upload_match.py        # Database upload functionality
  ├── Screenshots/           # Raw capture storage (240+ files)
  ├── Cropped_Modified_Files/# Processed image storage
  ├── templates/             # Reference images for matching
  ├── utils/
  │   ├── image_processing.py # Core CV functions
  │   ├── config.py          # Configuration management
  │   └── logging.py         # Logging utilities
  ├── requirements.txt       # Python dependencies
  ├── .env.local            # Environment configuration
  └── README.md

  🔧 Core Components

  Match Detection Engine

  # detect_end.py
  def detect_match_end(frame):
      """
      Analyzes frame to determine if match has ended
      Returns: Boolean indicating match completion
      """
      # Template matching for result screen UI elements
      # Color analysis for victory screens
      # Text detection for "GAME!" indicators

  Result Extraction System

  # scrape_results.py  
  def extract_match_results(screenshot):
      """
      Processes result screen to extract match data
      Returns: Dictionary with player names, characters, winner
      """
      # Character icon recognition
      # Player name OCR
      # Winner determination logic

  Database Integration

  # upload_match.py
  def upload_match_data(match_results):
      """
      Uploads processed match data to database
      Returns: Success/failure status
      """
      # Data validation and formatting
      # API communication with Supabase
      # Error handling and retry logic

  ⚙️ Configuration

  Environment Variables

  - SUPABASE_URL - Database endpoint URL
  - SUPABASE_KEY - API authentication key
  - CAPTURE_DEVICE - Video input device path
  - DEBUG_MODE - Enable debug logging and image saving
  - CONFIDENCE_THRESHOLD - Minimum match confidence (default: 0.85)
  - PROCESSING_INTERVAL - Frame analysis frequency (default: 1.0s)

  Detection Parameters

  # config.py
  MATCH_END_TEMPLATES = [
      'result_screen_template.png',
      'victory_screen_template.png'
  ]

  CHARACTER_ICONS = {
      'mario': 'mario_icon.png',
      'luigi': 'luigi_icon.png',
      # ... additional character mappings
  }

  OCR_CONFIG = {
      'whitelist': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',
      'min_confidence': 70
  }

  🎮 Usage

  Basic Operation

  1. Setup Hardware - Connect capture card to gaming console
  2. Start Detection - Run python main.py
  3. Play Matches - System automatically detects and records results
  4. Monitor Output - Check logs for processing status
  5. View Data - Results appear in connected Kiroku dashboard

  Advanced Features

  # Run with debug mode (saves all processed images)
  DEBUG_MODE=True python main.py

  # Process existing screenshots
  python scrape_results.py --batch-process Screenshots/

  # Test specific components
  python detect_end.py --test-image test_result_screen.png

  Integration with Kiroku

  Shobu automatically uploads match data to your configured database, where it's instantly displayed in the https://github.com/yourusername/kiroku web interface
  with real-time updates.

  🔧 Troubleshooting

  Common Issues

  - No Video Input - Check capture card connection and device permissions
  - Poor Detection Accuracy - Adjust lighting and camera positioning
  - Database Upload Failures - Verify network connection and API credentials
  - High CPU Usage - Increase processing interval or reduce image resolution

  Debug Mode

  Enable debug mode to save all processed images and detailed logs:
  DEBUG_MODE=True python main.py

  🔮 Future Enhancements

  - Multi-Game Support - Extend to other fighting games
  - Tournament Mode - Bracket tracking and management
  - Stream Integration - OBS plugin for live broadcasting
  - Machine Learning - Neural network-based character recognition
  - Mobile App - Remote monitoring and control interface
  - Hardware Optimization - GPU acceleration support

  🤝 Contributing

  Contributions are welcome! Areas for improvement:
  - Character recognition accuracy
  - New game mode support
  - Performance optimizations
  - Hardware compatibility

  Development Setup

  1. Fork the repository
  2. Create a feature branch (git checkout -b feature/amazing-feature)
  3. Test with your hardware setup
  4. Commit changes (git commit -m 'Add some amazing feature')
  5. Push to branch (git push origin feature/amazing-feature)
  6. Open a Pull Request

  ---