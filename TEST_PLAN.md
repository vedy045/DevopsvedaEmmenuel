# Test Plan — ITLDO801 Assignment 3

**Student:** Setako Vedaste  
**Registration number:** 20250203  
**Date:** 26 October 2026  
**Portfolio:** https://vedy045.github.io/DevopsvedaEmmenuel/

| Test ID | What is tested | Steps | Expected result |
|---|---|---|---|
| TC-01 | Open portfolio homepage | Open the portfolio URL in Chrome and wait for the page title. | The page loads, the title is not empty, and the current URL is the portfolio URL. |
| TC-02 | About section | Find element ID `about`, scroll it into view, and check for a navigation link to `#about`. | The About section exists and a matching navigation link is present. |
| TC-03 | Expertise section | Find element ID `services` and a navigation link to `#services`. | The Expertise/Services section exists and a matching navigation link is present. |
| TC-04 | Portfolio section | Find element ID `portfolio` and a navigation link to `#portfolio`. | The Portfolio section exists and a matching navigation link is present. |
| TC-05 | Skills section | Find element ID `skills` and a navigation link to `#skills`. | The Skills section exists and a matching navigation link is present. |
| TC-06 | Contact section | Find element ID `contact` and a navigation link to `#contact`. | The Contact section exists and a matching navigation link is present. |
| TC-07 | Negative test: missing section | Attempt to find an element with ID `missing-section`, intentionally not part of the portfolio. | The missing element is detected and the run records FAIL with the reason and a screenshot when possible. |

## Why these checks matter
The positive checks cover the homepage and main navigation destinations. They verify that expected sections exist rather than merely clicking links. TC-07 is intentionally negative so the log demonstrates how an unsuccessful check is recorded. Its FAIL status is expected and does not mean the actual portfolio navigation is broken.
