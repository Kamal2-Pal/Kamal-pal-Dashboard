name: Daily Auto Email Report

on:
  schedule:
    # Daily Subah 9:00 AM IST (03:30 AM UTC) par automatically chalega
    - cron: '30 3 * * *'
  workflow_dispatch: # Manual test ke liye button bhi dega

jobs:
  send-email:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install Dependencies
        run: |
          pip install pandas openpyxl

      - name: Run Email Script
        env:
          SENDER_EMAIL: ${{ secrets.kamal.2@pw.live }}
          SENDER_PASSWORD: ${{ secrets.8459086224K@m }}
          RECEIVER_EMAIL: ${{ secrets.sher.singh@pw.live }}
        run: python send_daily_report.py
