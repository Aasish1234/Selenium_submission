# Selenium Web Automation & Testing Framework Suite

A comprehensive test automation repository comprising hands-on laboratory modules (Modules 1–4) and an enterprise-grade Capstone Project built using **Python**, **Selenium WebDriver**, **PyTest**, and the **Page Object Model (POM)** architecture.

---

## 👨‍💻 Student Information

* **Name:** Aasish Shrestha
* **Enrollment No:** 12023002001003
* **Department:** Computer Science & Engineering (Roll No: 33)
* **Institution:** Institute of Engineering & Management (IEM), Kolkata
* **Email:** aasish.shrestha2023@iem.edu.in | aasishshrestha2005@gmail.com

---

## 📁 Repository Structure

```text
Selenium_submission/
├── Assignments/
│   └── Selenium_Assignments/
│       ├── Module_1_2/           # Locators, multiple elements & CSS child combinators
│       │   ├── exp1_web_element_identification.py
│       │   ├── exp2_multiple_element_identification.py
│       │   ├── exp3_child_nodes_css_part1.py
│       │   └── exp3_child_nodes_css_part2.py
│       ├── Module_3/             # Dynamic controls, actions & alert popups
│       │   ├── exp4_radio_button.py
│       │   ├── exp5_keyboard_actions.py
│       │   ├── exp6_mouse_hover.py
│       │   └── exp7_alerts.py
│       └── Module_4/             # Text areas, mouse drag & drop interactions
│           ├── exp8_locate_left_hand_textbox.py
│           ├── exp9_drag_and_drop.py
│           └── exp10_write_text_in_box.py
│
├── Capstone_project/             # Scalable POM Automation Framework
│   ├── config/                   # Global configuration management (config.ini)
│   ├── pages/                    # Encapsulated Web Element locators and page actions
│   │   ├── base_page.py          # Reusable WebDriver explicit wait wrappers
│   │   ├── home_page.py          # Header, navigation, and global search actions
│   │   ├── login_page.py         # Login form interactions and authentication checks
│   │   ├── register_page.py      # Account registration workflow
│   │   ├── search_results_page.py# Search listing validations and assertions
│   │   └── account_page.py       # User dashboard and session teardown
│   ├── test_data/                # Parameterized CSV test records (login_data, search_data)
│   ├── tests/                    # PyTest test suites and fixtures (conftest.py)
│   ├── utilities/                # Helper utilities (CSV reader, screenshots, reporters)
│   └── reports/                  # Generated HTML test execution reports
│
├── Certificates/                 # Course completion credentials
├── requirements.txt              # Framework dependencies
├── pytest.ini                    # PyTest CLI flags and marker declarations
└── README.md