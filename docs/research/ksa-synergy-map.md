# KSA Synergy Map — top-tier candidates × existing skills

Companion to [cross-industry-ksa-study.md](cross-industry-ksa-study.md). Eight top-tier
candidates (rounded boxes, grouped by proposed build wave) and the existing skills they
mount onto (rectangles). Edge labels name the combination pattern from the study's §4.

```mermaid
flowchart LR
    subgraph WA["Wave A — continuous-improvement-skills (extend)"]
        FMEA(["fmea (44)"])
        TOC(["theory-of-constraints (39)"])
    end

    subgraph WB["Wave B — safety-and-reliability-skills (new)"]
        CHK(["checklist-design (45)"])
        BOW(["bowtie-barrier-analysis (42)"])
        SBAR(["sbar-structured-communication (39)"])
    end

    subgraph WC["Wave C — decision-science-skills (new)"]
        CHA(["competing-hypotheses-analysis (44)"])
        RCF(["reference-class-forecasting (43)"])
        NEG(["principled-negotiation (41)"])
    end

    subgraph EXISTING["Existing skills (mount points, file-verified)"]
        MEC["accounting-skills:<br/>month-end-close"]
        BR["cash-management-skills:<br/>bank-reconciliation"]
        CMC["cash-management-skills:<br/>cash-management-controls"]
        CF["cash-management-skills:<br/>cash-forecasting"]
        BFA["banking-skills:<br/>bank-fee-analysis"]
        VSM["continuous-improvement-skills:<br/>value-stream-mapping"]
        DMAIC["continuous-improvement-skills:<br/>dmaic-problem-solving"]
        LSS["continuous-improvement-skills:<br/>lean-six-sigma-for-software"]
        FARD["oracle-fusion-finance-skills:<br/>fusion-auto-reconciliation-design"]
        MRD["deep-research-skills:<br/>medical-research-detective"]
        MPA["coding-agent-skills:<br/>master-prompt-architect"]
        DENTAL["the dental practice app<br/>(chicken-little-college-kid,<br/>curve-hero-design-language)"]
    end

    CHK -- "P2 formalize<br/>96 checklist artifacts" --> MEC
    CHK -- "P2 clinical workflows" --> DENTAL
    FMEA -- "P3 break triage" --> BR
    FMEA -- "P3 Detection = silent mis-match?" --> FARD
    FMEA -- "P3 gauntlet scoring" --> LSS
    CHA -- "P6 break = 3-6 rival causes" --> BR
    CHA -- "P6 generalize disconfirmation" --> MRD
    CHA -- "P6 audit alternatives" --> MPA
    RCF -- "P1 MAPE/bias history<br/>= reference class" --> CF
    BOW -- "P3 fraud controls<br/>as owned barriers" --> CMC
    NEG -- "P1 case built,<br/>ask missing" --> BFA
    NEG -- "P1 carrier fee schedules" --> DENTAL
    TOC -- "P5 where is<br/>the constraint" --> VSM
    TOC -- "P5 subordinate the calendar" --> MEC
    SBAR -- "P4 Control-phase<br/>handoff format" --> DMAIC
    SBAR -- "P4 front-desk to clinical" --> DENTAL
    SBAR -- "P4 PACE = human barrier" --> CMC
```

Reading the map: the densest mount points are `bank-reconciliation`, `month-end-close`,
`cash-management-controls`, and the dental app — the user's daily surfaces. Tier-2
candidates (pre-mortem, evolutionary-operation, measurement-systems-analysis,
design-of-experiments, tabletop-wargaming, qfd, after-action-review, and others) are
tabled in the study's §6 and omitted here for legibility.
