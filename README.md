# Random Library OOP Analysis

## Final Term Project

Selected Library: Random

Architectural Analysis & Custom Extension of Python 'Random' Library

Group Members & Project Details

- Zeeshan Ijaz (Lead) — F25BDATS1M02086
- Muzafer Shah Bukhari — F25BDATS1M02082
- Muhammad Yousaf Khan — F25BDATS1M02060
- Muhammad Ismail — F25BDATS1M02059

Academic Context

Academic Program: BS Data Science (Semester 2)

Course: Object-Oriented Programming (OOP) Final Term Project

Instructor: Dr. Akmal Khan

Date: 30 May 2026

1. Library Overview

The Python random library is a built-in module used for generating random numbers, selecting random elements, shuffling sequences, and performing probability-based operations. This project analyzes the architecture of the random library and demonstrates how Object-Oriented Programming concepts can be applied through a custom extension.

2. Class Hierarchy & Architectural Diagram

The UML Class Diagram and architecture analysis are included in the project report. The diagram illustrates inheritance relationships, class responsibilities, and extension points used in our custom implementation.

3. Core OOP Principles Analyzed

Inheritance

Our custom class extends the functionality of the Random class and adds additional features without modifying the original implementation.

Polymorphism

Methods are overridden to customize random value generation while maintaining compatibility with the parent class interface.

Encapsulation

Internal calculations and logging mechanisms remain hidden within class methods and are not directly accessible from outside the class.

Abstraction

Complex random generation processes are hidden behind simple methods, making the system easier to use and understand.

4. Custom Extension Implementation

The project includes a custom class named CustomRandomGenerator that extends Python's Random class.

Key Features Implemented

- Random number generation
- Random password generation
- Random OTP generation
- Custom reporting and logging
- User-friendly interface

Quick Start / Demo Execution

python main.py
