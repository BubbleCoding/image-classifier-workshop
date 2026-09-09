# Build Your Own Image Classifier

A 2.5-hour in-class exercise: pick your own classes, scrape your own training
images, and train a real image classifier with transfer learning — the same
technique Teachable Machine uses behind its UI, except this time you can see
every step.

## Before class

Colab needs a **Google Account**, but that doesn't mean a new Gmail address —
during Google's sign-up flow there's a "use my current email address
instead" option that registers a Google Account against any existing email,
including a school Microsoft address. Do this **tonight**, not during class:
5 minutes now saves everyone waiting on account creation tomorrow.

1. Go to [accounts.google.com](https://accounts.google.com) → Create account.
2. Choose "use my current email address instead" and enter your school
   email.
3. Verify it (a code is emailed to that address) and set a password.
4. Confirm it worked: open [colab.research.google.com](https://colab.research.google.com)
   and check you're signed in.

## Getting started

1. Open `image_classifier_workshop.ipynb` in [Google Colab](https://colab.research.google.com)
   (File → Upload notebook, or open it directly from GitHub/GitLab if your
   instructor shared a link).
2. Run the cells top to bottom. Markdown cells explain what's happening and
   why at each step — read them, don't just run and skip. A few code cells
   have a `___` or a `TODO` comment where you need to write something before
   that cell will run — those are on you, not typos.
3. You'll edit exactly one thing yourself early on: the `CLASSES` dictionary
   in Step 1, where you choose what the model learns to recognize.
4. Step 9 is an assignment, not a read-through: you'll come up with your own
   idea, rebuild the notebook around it, and show it to the class.

No installs on your own laptop — everything runs in the browser.

**Heads up:** the image search sometimes returns fewer results than you ask
for (it depends on how common your search term is) — getting 30-40 images
per class instead of 100 is normal and still plenty to train on.
