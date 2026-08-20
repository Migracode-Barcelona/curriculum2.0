+++
title = "Submitting Assignments"
layout = "module"
menu = ["important information", "syllabus"]
description = "A practical guide for MigraCode students on how to submit assignments based on their type, including complete guidelines on opening and managing Pull Requests (PRs)."
weight = 3
emoji = "📝"
time = "30"
[objectives]
1 = "Understand how to submit assignments based on their submission type"
2 = "Learn how to create, format, and manage professional Pull Requests"
[build]
  render = "never"
  list = "local"
  publishResources = false
+++

# 📤 Submitting Assignments & PR Guidelines

At MigraCode, submitting your work isn't just about handing in assignments — it's about practicing a real-world web development workflow using **Pull Requests (PRs)** to collaborate, receive feedback, and improve your code.

---

## 📌 Quick Links

- 🧾 [MigraCode PR Submission Form (Google Form)](https://docs.google.com/forms/d/e/1FAIpQLSesj1TzRyeaV5unZVI4Iqbgxf78qs3QVu0WSkxfr5W68HSlbg/viewform?usp=sharing&ouid=117762897010037598835)
- 📋 [End-of-Module Airtable Submission Form](https://airtable.com/appHB49eVBBLG0KZH/pagHBHn5kyBE8IjEH/form)
- 📘 [GitHub Writing Guide](https://docs.github.com/en/get-started/writing-on-github)
- 🧭 [Git Branching Overview](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository)

---

## 🛠️ The 3 Types of Assignments

Every assignment at MigraCode falls under one of three types. Check your task instructions to see which process to follow.

### 1️⃣ PR for Self Review

This exercise is **compulsory to complete**, but **you don’t need to submit it for volunteer review**.

- **Goal:** Practice the full PR cycle and develop good coding and git habits.
- **Workflow:** Create a branch, write your code, open a PR against your `main` branch, self-review, and merge your final changes into `main`.
- **Optional Support:** If you'd like extra feedback, you can share your PR directly with your **CodeBuddy or classmates**.

➡️ **Example – Help me with my kid’s homework**

- 📋 [Curriculum Backlog](https://migracode-itp.netlify.app/onboarding/sprints/1/backlog/)
- 🐙 [GitHub Issue](https://github.com/Migracode-Barcelona/Module-Onboarding/issues/8)

---

### 2️⃣ PR with CodeBuddy Review

This exercise **must be reviewed** by a **CodeBuddy** or **volunteer**.

- **Deadline:** Submit your assignment on time (before the end of the sprint).
- **Workflow:**
  1. Follow the [PR Guidelines](#-how-to-do-a-good-pull-request-pr) below.
  2. Fill out and submit the 🧾 [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSesj1TzRyeaV5unZVI4Iqbgxf78qs3QVu0WSkxfr5W68HSlbg/viewform?usp=sharing&ouid=117762897010037598835).
  3. Incorporate feedback when your reviewer comments on your PR, then merge to `main`.

> 💡 **Tip:** Keep your PRs focused! Try to keep PRs under 100 lines of changed code.

➡️ **Example – Bikes for Refugees**

- 📋 [Curriculum Backlog](https://migracode-itp.netlify.app/onboarding/sprints/1/backlog/)
- 🐙 [GitHub Repository](https://github.com/Migracode-Barcelona/bikes-for-refugees)

---

### 3️⃣ PRs to Include in End-of-Module Submissions

This exercise is **compulsory**, requires volunteer review, and must be recorded in your **end-of-module assessment**.

To evaluate your progress module-by-module, you must complete each step in sequence:

#### ✅ Submission Checklist

- [ ] **1.** Create your PR following the [PR Guidelines](#-how-to-do-a-good-pull-request-pr).
- [ ] **2.** Submit the 🧾 [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSesj1TzRyeaV5unZVI4Iqbgxf78qs3QVu0WSkxfr5W68HSlbg/viewform?usp=sharing&ouid=117762897010037598835) on time.
- [ ] **3.** Receive feedback from a volunteer, incorporate changes, and complete your PR.
- [ ] **4.** Submit the 📋 [Airtable Form](https://airtable.com/appHB49eVBBLG0KZH/pagHBHn5kyBE8IjEH/form) at the end of the module, adding all requested links.

⚠️ **Note:** Type 3 PRs **must be submitted through the Google Form and reviewed** before submitting the final Airtable form.

➡️ **Example – Wireframe to Web Code**

- 📋 [Curriculum Backlog](https://migracode-itp.netlify.app/onboarding/sprints/1/backlog/)
- 🐙 [GitHub Directory](https://github.com/Migracode-Barcelona/Module-Onboarding/tree/main/Wireframe)

---

## 👩‍💻 How to Do a Good Pull Request (PR)

### 🧭 What Is a Pull Request?

A **Pull Request (PR)** is how you propose code changes before merging them into your main branch. At MigraCode, you open PRs **within your own project repository** (personal or group) to simulate a full professional software development lifecycle:

1. Create a **feature branch** from `main`
2. Write and commit your code
3. Open a **PR against your own `main` branch**
4. Receive feedback from volunteers or instructors
5. Make improvements based on feedback
6. Merge your branch into `main`

---

### 🌿 1. Preparing Your Branch

- **Keep it focused:** Always create a new branch from `main` before coding. Never code directly on `main`. Keep each branch isolated to one feature or assignment.
- **Write clean code:** Follow the **MigraCode Code Style Guide**, use descriptive variable and function names, and remove unused code, dead imports, and unnecessary `console.log` statements.

---

### 🚀 2. Opening the PR

1. Push your branch to GitHub.
2. Open a Pull Request against **your own `main` branch**.
   > ⚠️ Do _not_ open PRs against upstream repositories like MigraCode Barcelona or CodeYourFuture.
3. Verify your configuration:
   - **Target branch:** `main`
   - **Source branch:** `your-feature-branch`

![Screenshot showing correct PR target and source branches](screenshot_merge.png)

---

### 🧩 3. PR Title & Description Standards

#### 🏷️ Title Format

Structure your PR title as follows:

```text
Name | Class | Module | Sprint | Assignment
```
