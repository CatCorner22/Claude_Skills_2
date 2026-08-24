# Your Environment — Fitness & Nutrition Science Skill

Fill in this template to tailor the skill to your tracker's cohort, measurement resolution,
and success criteria. Keep this file outside the plugin in `.claude/skills-env/` so your
specifics survive plugin updates.

## Athlete Population

**Demographics (required):**
- Age range: _____
- Sex/gender distribution: _____ (% female, % male, % non-binary, etc.)
- Training status (circle one): Untrained (< 6 months lifting) | Novice (6 mo–2 yrs) | Intermediate (2–5 yrs) | Advanced (5+ yrs)
- Primary goals (rank by % of cohort):
  - Fat loss with muscle retention: ____%
  - Muscle hypertrophy: ____%
  - Strength gain: ____%
  - General cardiovascular fitness: ____%
  - Sport-specific performance: ____%
  - Mobility/flexibility: ____%

**Training history:**
- Average weekly training frequency: _____ sessions/week
- Most common training modalities (e.g., resistance, cardio, mixed): _____
- Injuries or movement restrictions common in cohort: _____

## Tracker Measurement Capabilities

**Quantitative data you can measure (check all that apply):**
- [ ] Bodyweight (frequency: daily / weekly / other: _____)
- [ ] Body composition (DEXA / bioimpedance / other: _____) (frequency: _____)
- [ ] Strength benchmarks (1RM, 3RM, 5RM, etc.; exercises: _____) (frequency: _____)
- [ ] Workout volume (sets × reps × load) (frequency: per-session / weekly)
- [ ] Workout duration
- [ ] Cardiovascular data (VO₂ max testing, max HR, lactate, etc.)
- [ ] Recovery markers (HRV, resting HR, sleep duration/quality)
- [ ] Nutrition (macros: protein, carbs, fat; micronutrients; frequency: _____)
- [ ] Subjective measures (perceived exertion, mood, sleep quality; frequency: _____)

**Data gaps (what you cannot or will not measure):**
_____

## Success Criteria Tuned to Your Cohort

For each primary goal, define testable success metrics. Use realistic rates from the skill.

### Fat Loss with Muscle Retention

**Target population example:** Sedentary to intermediate trainees seeking recomposition.

**Realistic expectations:**
- Fat loss rate: ~0.5–1 lb/week (larger deficits risk muscle loss)
- Muscle retention/gain: ~0 kg (best case) to +0.5 kg/month (if strength trained + high protein)
- Adherence: 80%+ compliance to caloric and protein targets

**Success metrics for your tracker:**
- Bodyweight trending down ~0.5–1 lb/week (allow ±1 lb daily variance; watch 4-week trend)
- Strength maintained or increasing (e.g., 1RM bench should not decline)
- Subjective energy/recovery: adequate to stable (alert to sudden fatigue = underfeeding)
- When to adjust: If bodyweight stable for 2 weeks, reduce calories by 200 kcal

### Muscle Hypertrophy

**Target population example:** Intermediate resistance-trained cohort in caloric surplus.

**Realistic expectations:**
- Muscle gain rate: ~1–1.5 kg/month (beginners); ~0.5 kg/month (intermediate); ~0.25 kg/month (advanced)
- Fat gain: ~1–1.5 kg/month with +300–500 kcal surplus (males gain less fat % than females due to hormones)
- Strength increase: ~2–5% per month (early), ~0.5–1% per month (plateauing)
- Adherence: 80%+ compliance to training volume and protein

**Success metrics for your tracker:**
- Bodyweight gaining ~1–1.5 lb/week (if beginner in surplus)
- Weekly volume (sets per muscle group) increasing or stable; target: 10–20 sets/week per muscle
- Protein intake: ≥0.7 g/lb body weight daily
- Strength: 1RM or RPE-matched reps increasing (e.g., if doing 5 reps at RPE 9, can now do 6 reps at RPE 9 = progress)
- When to adjust: If no strength or volume increase for 3 weeks + protein/calories adequate → increase volume +2 sets/week

### Strength Gain (1RM & Near-Maximal Performance)

**Target population example:** Intermediate to advanced lifters seeking maximal strength.

**Realistic expectations:**
- Strength gain rate: ~2–5% per month (early phase); ~0.5–1% per month (plateauing)
- Hypertrophy: Secondary; muscle gain ~0.25–0.5 kg/month
- Body weight: Relatively stable or gradual accumulation (~0.5 lb/week) depending on caloric target
- Adherence: 85%+ compliance to training intensity and frequency

**Success metrics for your tracker:**
- 1RM or estimated 1RM (via rep-max formula) increasing ≥2% every 4 weeks
- Training frequency: ≥2x/week per movement (e.g., 2x squat, 2x bench, 2x deadlift or variant)
- Recovery adequate: 7–9 hours sleep, low injury complaint
- When to adjust: If no strength gain for 4 weeks despite adequate volume/frequency → deload 1 week, then increase intensity (load) or decrease volume slightly to allow recovery

### Cardiovascular Fitness (VO₂ Max Maintenance/Gain)

**Target population example:** Mixed cohort prioritizing aerobic fitness and longevity.

**Realistic expectations:**
- VO₂ max gain rate: ~5–15% over 8–12 weeks with regular high-intensity training (HIIT or steady-state)
- Maintenance: ≥1x/week high-intensity or 2–3x/week moderate intensity
- VO₂ decay: ~7% after 2 weeks no training; ~15–20% after 10 weeks
- Adherence: 80%+ to target weekly volume

**Success metrics for your tracker:**
- VO₂ max testing: Every 8–12 weeks (measure via treadmill test or submaximal estimate)
- Weekly high-intensity volume: 2–3x/week HIIT sessions (4–6 min bouts) OR 150–300 min/week steady-state
- Max HR stability: No acute change (if training is consistent); resting HR stable or declining
- When to adjust: If VO₂ max flat after 8 weeks of consistent training → increase HIIT frequency or intensity, or add more volume

## Tracker-Specific Notes

**Adherence levers (what your tracker can do to improve protocol compliance):**
- [ ] Automated reminders (meals, training sessions, recovery tracking)
- [ ] Progress visualization (charts showing 4-week trends)
- [ ] Simplified target display (single daily calorie/protein goal vs granular macros)
- [ ] Social/competitive features (if cohort is motivated by comparison)
- [ ] Other: _____

**Common dropout reasons in your cohort (observed or anticipated):**
_____

**Standing constraints or preferences:**
- E.g., "Cohort cannot test VO₂ max in lab; use estimated VO₂ from submaximal HR response"
- E.g., "Protein tracking is too burdensome; switch to meal-based guidance (e.g., 4 oz chicken = ~30g protein)"
- E.g., "Cohort is hourly-wage workers; prioritize time-efficient protocols (HIIT + strength)"

_____

---

## How This Template Shapes the Skill

Once filled in, this environment guide:
1. **Tunes success criteria:** The skill's claims ("1 kg muscle/month") are now contextualized to
   your cohort (e.g., "beginners can expect 1–1.5; advanced lifters, 0.25").
2. **Prioritizes measurement:** The skill knows which outcomes your tracker can measure (VO₂ max
   is optional; bodyweight is default).
3. **Adapts protocols:** If your cohort is time-constrained, the skill emphasizes HIIT + minimal
   strength work. If they are highly adherent competitors, the skill can suggest finer-grained
   optimizations.
4. **Prevents overfitting:** The skill acknowledges real-world constraints (no lab testing) and
   adapts recommendations accordingly.

**Example use:** User asks, "Is my muscle gain rate normal?"
- Skill looks up your cohort (intermediate, 2 kg/month in surplus).
- Skill notes your tracker measures bodyweight weekly.
- Skill responds: "For intermediate lifters, 1–1.5 kg/month is normal. Your tracker measures
  bodyweight; we'll use a 4-week rolling average to account for daily variance. If you're at
  1.5 kg/month, you're tracking well. If below 1 kg/month for 3+ weeks, let's increase calories
  by +200 kcal."

---

## Next Steps

1. **Fill in this template with your specific data** (demographics, measurement capabilities,
   success criteria).
2. **Copy to `.claude/skills-env/fitness-nutrition-science.md`** in your project repo
   (git-ignore if sensitive).
3. **Reference this copy** when invoking the skill (e.g., "Use my environment profile at
   `.claude/skills-env/fitness-nutrition-science.md`").
4. **Update quarterly:** As your cohort evolves, refresh success criteria and adherence notes.
