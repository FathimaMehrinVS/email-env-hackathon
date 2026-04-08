# Email Triage AI Environment (OpenEnv)

## Overview
This project simulates a real-world email triage system where an AI agent classifies emails into:
- Spam → delete
- Important → mark_important
- Neutral → ignore

## Tasks
- Easy: Basic classification
- Medium: Mixed patterns
- Hard: Ambiguous emails

## Action Space
- delete
- mark_important
- ignore

## Observation Space
- Email text

## Reward Function
+1 → correct action  
-1 → wrong action  

## Goal
Maximize correct classification over all emails.

## Deployment
Running on Hugging Face Spaces with Docker.

## Baseline Score
1.0 (perfect classification)