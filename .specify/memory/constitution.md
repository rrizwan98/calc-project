<!-- Sync Impact Report:
Version change: 0.0.0 -> 1.0.0
List of modified principles:
  - PRINCIPLE_1_NAME -> Write Tests First (TDD)
  - PRINCIPLE_2_NAME -> Python 3.12+ with Type Hints
  - PRINCIPLE_3_NAME -> Clean and Readable Code
  - PRINCIPLE_4_NAME -> Architectural Decision Records (ADRs)
  - PRINCIPLE_5_NAME -> Essential OOP Principles
Added sections:
  - Technical Stack
  - Quality Requirements
Removed sections:
  - None
Templates requiring updates:
  - .specify/templates/plan-template.md: ⚠ pending
  - .specify/templates/spec-template.md: ⚠ pending
  - .specify/templates/tasks-template.md: ⚠ pending
  - .specify/templates/adr-template.md: ✅ updated (no placeholders to change in this template, but content will align)
  - .specify/templates/checklist-template.md: ⚠ pending
  - .specify/templates/phr-template.prompt.md: ✅ updated (no placeholders to change in this template, but content will align)
  - .specify/templates/agent-file-template.md: ✅ updated (no placeholders to change in this template, but content will align)
Follow-up TODOs: None
-->
# Calc-Project Constitution

## Core Principles

### 1. Write Tests First (TDD)
All development must follow a Test-Driven Development (TDD) approach. Tests must be written and approved before implementation begins. The Red-Green-Refactor cycle is strictly enforced.

### 2. Python 3.12+ with Type Hints
All Python code must use Python version 3.12 or newer. Type hints must be used comprehensively across the entire codebase to improve readability and maintainability.

### 3. Clean and Readable Code
Code must be clean, well-structured, and easy to understand. Adherence to established coding standards and best practices is mandatory to ensure maintainability.

### 4. Architectural Decision Records (ADRs)
All significant architectural decisions must be documented using Architectural Decision Records (ADRs). ADRs provide context, rationale, and consequences for key technical choices.

### 5. Essential OOP Principles
Adherence to essential Object-Oriented Programming (OOP) principles, including SOLID, DRY (Don't Repeat Yourself), and KISS (Keep It Simple, Stupid), is mandatory to promote robust, maintainable, and scalable code.

## Technical Stack

*   Python 3.12+ with UV package manager
*   pytest for testing
*   All project files must be kept in a Git repository.

## Quality Requirements

*   All tests must pass.
*   Achieve at least 80% code coverage.
*   Use dataclasses for data structures where appropriate.

## Governance
The project constitution supersedes all other practices. Amendments require thorough documentation, explicit approval from stakeholders, and a clear migration plan. All Pull Requests (PRs) and code reviews must verify compliance with these principles. Justification is required for any increase in complexity.

**Version**: 1.0.0 | **Ratified**: 2025-11-20 | **Last Amended**: 2025-11-20