# CSCI171 Assignment Templates

This repository holds the reusable assignment materials for CSCI171.

Use folders instead of one template repository per assignment.

## Folder Map

```text
group-builds/
individual-projects/
reflections/
shared/
```

## Course Workflow

Wednesday group builds:

- used for in-class practice
- groups may collaborate on one shared solution
- not usually a GitHub turn-in
- each student submits a short reflection in Canvas when assigned

Friday individual projects:

- required textbook-level individual work
- copied into each student's semester repository
- submitted through the student's semester repository

Take-home extensions:

- optional extra credit
- stretch beyond the Friday requirement

## Student Semester Repo Pattern

Each student should usually have one semester repo:

```text
fa26-csci171-<github-username>
```

Inside that repo:

```text
week-01-profile/
week-02-calculator/
week-03-decision-quiz/
week-04-guessing-game/
```


## Branch Naming Rule

Use the assignment folder name as the feature branch name.

Examples:

```text
week-01-profile
week-02-calculator
week-03-decision-quiz
```

Keep branch names lowercase, hyphenated, and exactly matching the assignment README. This makes grading easier because every student uses the same branch name for the same assignment.

Submission pattern:

1. Start from `main`.
2. Create the assignment branch.
3. Commit your work.
4. Push the branch.
5. Open a pull request into your own `main` branch.
6. Submit the PR link in Canvas.

## Group Code Policy

For weekly ad hoc groups, do not put group code in only one student's folder.

Better options:

1. Group builds are practice only, with a short Canvas reflection.
2. If code must be submitted, each student saves their own copy with a note naming the group members.
3. For larger multi-day group projects, create a dedicated group repo.

Recommended default: option 1.
