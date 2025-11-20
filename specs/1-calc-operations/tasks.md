# Tasks: Basic Calculator Operations

**Input**: Design documents from `/specs/1-calc-operations/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/, quickstart.md

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create `src/` and `tests/` directories if they don't exist
- [X] T002 Initialize a new `uv` project in the root directory (creating `pyproject.toml`) and install `pytest` and `ruff` with `uv add pytest ruff`
- [X] T003 Create `src/calculator/__init__.py` to define the calculator module
- [X] T004 Create `src/main.py` for the command-line interface entry point

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T005 Implement basic argument parsing for operations in `src/main.py`
- [X] T006 Configure `pytest` and `ruff` for code quality (using the installed packages) in `pyproject.toml`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Numbers (Priority: P1) 🎯 MVP

**Goal**: User can add two numbers, including positive, negative, zero, and decimal values.

**Independent Test**: Fully tested by providing two numeric inputs and verifying that the sum returned by the calculator is mathematically correct.

### Tests for User Story 1 ⚠️

- [X] T007 [US1] Create unit test file for add operation in `tests/unit/calculator/test_add.py`
- [X] T008 [US1] Implement test cases for adding positive integers (e.g., 5, 3 -> 8) in `tests/unit/calculator/test_add.py`
- [X] T009 [US1] Implement test cases for adding negative integers (e.g., -5, -3 -> -8) in `tests/unit/calculator/test_add.py`
- [X] T010 [US1] Implement test cases for adding positive and negative integers (e.g., 5, -3 -> 2) in `tests/unit/calculator/test_add.py`
- [X] T011 [US1] Implement test cases for adding numbers with decimals (e.g., 2.5, 3.2 -> 5.7) in `tests/unit/calculator/test_add.py`
- [X] T012 [US1] Implement test cases for adding zero values (e.g., 5, 0 -> 5) in `tests/unit/calculator/test_add.py`

### Implementation for User Story 1

- [X] T013 [US1] Create `src/calculator/add.py` with `add(num1: float, num2: float) -> float` function
- [X] T014 [US1] Implement `add` function logic in `src/calculator/add.py`
- [X] T015 [US1] Integrate `add` function into `src/main.py` CLI dispatch

**Checkpoint**: User Story 1 is fully functional and testable independently

---

## Phase 4: User Story 2 - Subtract Numbers (Priority: P1)

**Goal**: User can subtract two numbers, covering all combinations of positive, negative, zero, and decimal values.

**Independent Test**: Fully tested by providing a minuend and subtrahend, and verifying that the difference returned by the calculator is mathematically correct.

### Tests for User Story 2 ⚠️

- [ ] T016 [US2] Create unit test file for subtract operation in `tests/unit/calculator/test_subtract.py`
- [ ] T017 [US2] Implement test cases for subtracting various number combinations (positive, negative, zero, decimals) in `tests/unit/calculator/test_subtract.py`

### Implementation for User Story 2

- [ ] T018 [US2] Create `src/calculator/subtract.py` with `subtract(num1: float, num2: float) -> float` function
- [ ] T019 [US2] Implement `subtract` function logic in `src/calculator/subtract.py`
- [ ] T020 [US2] Integrate `subtract` function into `src/main.py` CLI dispatch

**Checkpoint**: User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Multiply Numbers (Priority: P1)

**Goal**: User can multiply two numbers, including handling edge cases like multiplication by zero.

**Independent Test**: Fully tested by providing two numeric inputs and verifying that the product returned by the calculator is mathematically correct.

### Tests for User Story 3 ⚠️

- [ ] T021 [US3] Create unit test file for multiply operation in `tests/unit/calculator/test_multiply.py`
- [ ] T022 [US3] Implement test cases for multiplying various number combinations (positive, negative, decimals) in `tests/unit/calculator/test_multiply.py`
- [ ] T023 [US3] Implement test cases for multiplying by zero in `tests/unit/calculator/test_multiply.py`

### Implementation for User Story 3

- [ ] T024 [US3] Create `src/calculator/multiply.py` with `multiply(num1: float, num2: float) -> float` function
- [ ] T025 [US3] Implement `multiply` function logic in `src/calculator/multiply.py`
- [ ] T026 [US3] Integrate `multiply` function into `src/main.py` CLI dispatch

**Checkpoint**: All user stories 1, 2, and 3 should now be independently functional

---

## Phase 6: User Story 4 - Divide Numbers (Priority: P1)

**Goal**: User can divide two numbers, excluding the case of division by zero.

**Independent Test**: Fully tested by providing a dividend and a non-zero divisor, and verifying that the quotient returned by the calculator is mathematically correct.

### Tests for User Story 4 ⚠️

- [ ] T027 [US4] Create unit test file for divide operation in `tests/unit/calculator/test_divide.py`
- [ ] T028 [US4] Implement test cases for dividing various number combinations (positive, negative, decimals) with non-zero divisor in `tests/unit/calculator/test_divide.py`
- [ ] T029 [US4] Implement test cases for zero as dividend and non-zero divisor (e.g., 0, 5 -> 0) in `tests/unit/calculator/test_divide.py`
- [ ] T030 [US4] Implement test case for division by zero (expecting `ZeroDivisionError`) in `tests/unit/calculator/test_divide.py`

### Implementation for User Story 4

- [ ] T031 [US4] Create `src/calculator/divide.py` with `divide(num1: float, num2: float) -> float` function
- [ ] T032 [US4] Implement `divide` function logic, including `ZeroDivisionError` handling, in `src/calculator/divide.py`
- [ ] T033 [US4] Integrate `divide` function into `src/main.py` CLI dispatch and handle `ZeroDivisionError` from CLI

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T034 Code cleanup and refactoring across `src/calculator/` files
- [ ] T035 Ensure all functions have clear docstrings as per `spec.md`
- [ ] T036 Run `ruff check .` to ensure code style and type hint compliance
- [ ] T037 Run `pytest --cov=src/` to verify 100% test coverage
- [ ] T038 Update `quickstart.md` with any final usage instructions or examples
- [ ] T039 Add integration tests for CLI argument parsing and error handling in `tests/integration/test_cli.py`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion
- **User Stories (Phase 3-6)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel or sequentially in priority order (P1 → P1 → P1 → P1)
- **Polish (Phase 7)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 4 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Function implementation before integration into CLI

### Parallel Opportunities

- All Setup tasks (T001-T004) can run in parallel (if directories/files don't conflict)
- All Foundational tasks (T005-T006) can run in parallel (if files don't conflict)
- Once Foundational phase completes, all user stories (Phases 3-6) can start in parallel (if team capacity allows)
- Within each User Story phase, test creation tasks (e.g., T007-T012) can be parallelized.
- Within each User Story phase, implementation tasks (e.g., T013-T014) can be parallelized if they are for separate files (e.g., creating separate add.py and subtract.py files)
- Polish tasks (T034-T039) marked [P] can run in parallel (e.g., T034 refactoring, T035 docstrings, T036 ruff check)

---

## Parallel Example: User Story 1 (Add Numbers)

```bash
# Tests for User Story 1:
- [ ] T007 [US1] Create unit test file for add operation in tests/unit/calculator/test_add.py
- [ ] T008 [P] [US1] Implement test cases for adding positive integers (e.g., 5, 3 -> 8) in tests/unit/calculator/test_add.py
- [ ] T009 [P] [US1] Implement test cases for adding negative integers (e.g., -5, -3 -> -8) in tests/unit/calculator/test_add.py
# ... and so on for other test cases in the same file

# Implementation for User Story 1:
- [ ] T013 [P] [US1] Create src/calculator/add.py with add(num1: float, num2: float) -> float function
- [ ] T014 [US1] Implement add function logic in src/calculator/add.py
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3.  Complete Phase 3: User Story 1
4.  **STOP and VALIDATE**: Test User Story 1 independently
5.  Deploy/demo if ready

### Incremental Delivery

1.  Complete Setup + Foundational → Foundation ready
2.  Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3.  Add User Story 2 → Test independently → Deploy/Demo
4.  Add User Story 3 → Test independently → Deploy/Demo
5.  Add User Story 4 → Test independently → Deploy/Demo
6.  Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1.  Team completes Setup + Foundational together
2.  Once Foundational is done:
    -   Developer A: User Story 1 (Add Numbers)
    -   Developer B: User Story 2 (Subtract Numbers)
    -   Developer C: User Story 3 (Multiply Numbers)
    -   Developer D: User Story 4 (Divide Numbers)
3.  Stories complete and integrate independently

---

## Notes

-   [P] tasks = different files, no dependencies
-   [Story] label maps task to specific user story for traceability
-   Each user story should be independently completable and testable
-   Verify tests fail before implementing
-   Commit after each task or logical group
-   Stop at any checkpoint to validate story independently
-   Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
