# Functional and Non-Functional Requirements

## Overview

The functional and non-functional requirements define how users interact with ScamLens and how the system should operate. The requirements were identified from the project research, user concerns and the main purpose of the application.

The functional requirements are divided into **User Functional Requirements (UFR)** and **System Functional Requirements (SFR)**. The **System Non-Functional Requirements (SNFR)** describe the expected performance, usability, privacy, compatibility and scalability of the application.

## User Functional Requirements

| ID        | Requirement                                                                                                                                  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **UFR 1** | The user should be able to clearly see the different types of content that can be analysed and the text box where the content can be pasted. |
| **UFR 2** | The user should be able to read a warning message advising them not to include personal data or sensitive information in the text box.       |
| **UFR 3** | The user should be able to analyse emails, SMS messages and URLs for potential spam or phishing attacks.                                     |
| **UFR 4** | The user should receive an analysis and prediction based on the submitted content.                                                           |
| **UFR 5** | The user should be able to navigate smoothly between the application pages.                                                                  |
| **UFR 6** | The user should be able to read clear instructions explaining how to use the system.                                                         |
| **UFR 7** | The user should be able to read safety tips explaining how to protect themselves from potential future attacks.                              |
| **UFR 8** | The user should be able to find and select links to official organisations where suspicious or fraudulent content can be reported.           |
| **UFR 9** | The user should have an option to send a question or complaint about the system.                                                             |

## System Functional Requirements

| ID        | Requirement                                                                                                                     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **SFR 1** | The system should display a warning advising users not to enter personal or sensitive information.                              |
| **SFR 2** | The system should provide visible and clickable buttons together with clear instructions explaining how to use the application. |
| **SFR 3** | The system should provide a clear navigation menu and pages that load quickly.                                                  |
| **SFR 4** | The system should allow the user to select the type of content being analysed and enter or paste it into the correct text box.  |
| **SFR 5** | The system should allow the user to submit content and receive its analysis and prediction.                                     |
| **SFR 6** | The system should provide a clear layout and safety tips explaining how users can protect themselves.                           |
| **SFR 7** | The system should analyse the submitted content without storing the user’s text input.                                          |
| **SFR 8** | The system should be accessible without installation, registration or a paid subscription.                                      |
| **SFR 9** | The system should maintain separate analysis modules for emails, SMS messages and URLs.                                         |

## System Non-Functional Requirements

| ID         | Category               | Requirement                                                                                                |
| ---------- | ---------------------- | ---------------------------------------------------------------------------------------------------------- |
| **SNFR 1** | Performance            | The system should return an analysis result within three seconds under normal operating conditions.        |
| **SNFR 2** | Privacy and compliance | The system should follow the principles of the UK GDPR and the Data Protection Act 2018.                   |
| **SNFR 3** | Scalability            | The system should support an increasing number of users without degradation in performance.                |
| **SNFR 4** | Compatibility          | The system should operate correctly on major web browsers.                                                 |
| **SNFR 5** | Usability              | The system should provide a clear interface with readable fonts, suitable colours and a responsive layout. |
| **SNFR 6** | Feedback               | The system should provide clear feedback explaining the result of the content analysis.                    |

## Requirements Summary

These requirements guided the design and development of the ScamLens interface and its main features. They ensured that the application remained simple to use while providing content analysis, clear feedback, privacy warnings, safety guidance and access to official reporting resources.

---

[← Back to the main README](../README.md) |  [Next: Prototype Design →](03_System_Design_and_Architecture.md)
