# Introduction

Date: 2026-04-05

Have you ever wondered how virtual machines work under the hood? This project is my attempt to demystify the process by building a simple virtual machine in Python. The objective of this project is to create a simple virtual machine that can execute a basic imaginary instruction set.

# Why am I doing this?

- Sharpen my coding skills without relying on modern conveniences like IDE autocomplete or AI tools. Asking questions is fine, but I want to avoid letting tools write the code for me.
- Revisit the fundamentals of machine code and memory.

# What has been done so far?

So far, I've laid the foundation for the virtual machine:

- Decided on a memory size of 1024 bytes, implemented basic registers, and designed the stack behavior.
- Implemented a basic instruction set.
- Designed the fetch-decode-execute cycle using Python's table dispatching.

# What needs to be done?

Next steps include:

- Writing test cases to thoroughly test the stack implementation.
- Deciding whether to use exceptions or error codes for error handling. For now, I'm using True/False, but this might need refinement.


If you're curious about the code or have suggestions for improvement, feel free to reach out or contribute!