# Raspberry Pi Cable Harness Tester

This project develops a system using a Raspberry Pi 4 to verify the correct pinning of a cable harness (Y-cable with 3 connectors, each having 6 pins). The system indicates the correct connection through an externally connected LED.

## System Overview

The Raspberry Pi Cable Harness Tester automatically checks the pinning of a cable harness upon startup. It uses a set of GPIO pins to interface with the cable connectors and an additional pin to control an LED indicator. The correct pinning lights up the LED, signaling a successful connection test.

## Getting Started

### Prerequisites

- Raspberry Pi 4 with Raspbian OS
- Python 3.x installed

### Installation

Clone this repository to your Raspberry Pi:


git clone https://github.com/aabdelghani/cableTester.git
cd cableTester




