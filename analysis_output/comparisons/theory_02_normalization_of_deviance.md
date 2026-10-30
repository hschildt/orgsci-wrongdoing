# Normalization of deviance and corruption: comparison across cases

*Generated 2026-10-29 by compare_tables.py with eu.anthropic.claude-haiku-4-5-20251001-v1:0, from analysis_output/02_normalization_of_deviance.csv. Presence: ●●● strong, ●●○ moderate, ●○○ weak, ○○○ absent; n = passages coded. Coverage = presence points ÷ maximum, computed in Python. ⚠ = answer trimmed after failing a rule check.*

## Presence by category

| Category | Boeing 737MAX | Dieselgate | Enron | Ford Pinto | Purdue OxyContin |
|---|---|---|---|---|---|
| Incremental drift and escalation | ●●● 75 | ●●● 65 | ●●● 69 | ●●● 17 | ●●● 64 |
| Redefinition of acceptable risk and standards | ●●● 99 | ●●● 74 | ●●● 80 | ●●● 21 | ●●● 34 |
| Institutionalization in routines, structures and technology | ●●● 48 | ●●● 38 | ●●● 61 | ●●● 11 | ●●● 63 |
| Collective rationalizations and shared vocabulary | ●●● 62 | ●●● 66 | ●●● 68 | ●●● 19 | ●●● 33 |
| Socialization and co-optation of newcomers | ●●○ 30 | ●●○ 10 | ●●● 47 | ○○○ 0 | ●●● 34 |
| Structural secrecy and fragmented knowledge | ●●● 143 | ●●● 90 | ●●● 106 | ●●● 19 | ●●● 38 |
| Leadership tolerance and cultural endorsement | ●●● 101 | ●●● 48 | ●●● 129 | ●●● 14 | ●●● 87 |
| **Coverage** | **95%** | **95%** | **100%** | **86%** | **100%** |

Ranking by coverage: Enron (100%) > Purdue OxyContin (100%) > Boeing 737MAX (95%) > Dieselgate (95%) > Ford Pinto (86%)

## Cross-case pattern

Normalization of deviance operates across all five cases through incremental escalation, reframed standards, embedded routines, shared vocabularies, and leadership tolerance, though socialization and structural secrecy vary in prominence and mechanism.

| Category | Common pattern | Key difference | Most pronounced | Least pronounced |
|---|---|---|---|---|
| Incremental drift and escalation | All five cases show wrongdoing growing through successive small steps, each justified by operational or financial necessity, with each step building on prior accepted practices and collectively transforming the scope or risk profile without corresponding reassessment. | Boeing and VW show technical escalation through design and software iterations; Enron through financial structure complexity; Ford through production timeline compression; Purdue through marketing scope expansion and prescriber targeting intensity. | Enron | Ford Pinto |
| Redefinition of acceptable risk and standards | All five cases involve systematic reinterpretation of technical, safety, or regulatory standards to classify non-compliant or dangerous practices as acceptable by reframing the problem, narrowing the scope of concern, or invoking exceptions. | Boeing and Ford reframe safety standards through risk classification and cost-benefit analysis; VW through testing condition exceptions; Enron through accounting standard reinterpretation; Purdue through medical and scientific evidence misrepresentation. | Enron | Dieselgate |
| Institutionalization in routines, structures and technology | All five cases embed wrongful practices in formal procedures, organizational structures, technological systems, and approval workflows that persist across units and personnel changes. | Boeing and Dieselgate embed wrongdoing in product design and software; Enron in financial procedures and organizational structures; Ford in engineering specifications and production procedures; Purdue in sales structures and compensation systems. | Dieselgate | Ford Pinto |
| Collective rationalizations and shared vocabulary | All five cases develop specialized vocabularies, euphemisms, and collective rationalizations that frame wrongful practices as legitimate business activities and normalize them across organizational communication. | Boeing and VW use technical euphemisms to minimize system scope; Enron uses financial euphemisms to obscure fraud; Ford uses ideological framing about market priorities; Purdue uses medical and therapeutic language to justify aggressive promotion. | Enron | Ford Pinto |
| Socialization and co-optation of newcomers | Four cases show newcomers drawn into wrongdoing through gradual involvement, direct instruction, rewards, and threats, with senior perpetrators actively recruiting and mentoring them into complicity. | Enron and Purdue show strong systematic co-optation through financial incentives and direct recruitment; Dieselgate shows moderate co-optation through instruction and compartmentalization; Boeing shows moderate co-optation through schedule pressure and retaliation; Ford shows no evidence of socialization mechanisms. | Enron | Ford Pinto |
| Structural secrecy and fragmented knowledge | All five cases use specialization, compartmentalization, and restricted information flow to prevent any single entity from seeing the complete picture of wrongdoing, enabling practices to persist without detection. | Boeing and Dieselgate fragment knowledge through technical specialization and regulatory compartmentalization; Enron through organizational silos and deliberate withholding; Ford through chain-of-command compartmentalization; Purdue through departmental restrictions and oral communications. | Enron | Boeing 737MAX |
| Leadership tolerance and cultural endorsement | All five cases show senior leaders and boards approving, authorizing, or tolerating wrongful practices, prioritizing financial or schedule success over safety or compliance, and rewarding those who advance these goals. | Boeing and Ford prioritize production schedules and cost savings; VW prioritizes market competitiveness; Enron prioritizes reported earnings through complex structures; Purdue prioritizes sales growth and opioid market expansion. | Purdue OxyContin | Boeing 737MAX |

## Category detail

### Incremental drift and escalation

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=75, 17 docs) | MCAS evolved through successive design expansions from a high-speed-only system (Mach 0.6-0.8) to one operating across nearly the entire flight envelope (Mach 0.2-0.8), with command authority increasing from 0.6 degrees to 2.5 degrees, each step justified by operational needs but collectively transforming the system's scope and risk profile without corresponding safety reassessment. | Boeing engineers and employees; Boeing management; FAA personnel | June 2015 to March 2017 | E1, E2, E3 |
| Dieselgate | ●●● strong (n=65, 15 docs) | VW engineers developed defeat device software through successive generations (Gen1, Gen2, Gen3) and iterative refinements between 2006-2015, with each version adding new detection features (steering wheel angle, temperature conditioning, AdBlue dosing strategies) to evade emissions tests while maintaining marketability. | VW engineers; Audi engineers; Dorenkamp; Neusser | 2006 to 2015 | E4, E5, E6 |
| Enron | ●●● strong (n=69, 16 docs) | Enron's use of SPEs for financial manipulation evolved through successive stages: from early legitimate securitizations (Condor) to increasingly complex off-balance-sheet structures (Chewco, LJM, Raptors), with each iteration building on prior techniques and escalating commitment as earlier steps made later ones seem necessary to meet financial targets. | Fastow; Skilling; Causey; Enron Board | 1997 through October 2001 | E7, E8, E9 |
| Ford Pinto | ●●● strong (n=17, 6 docs) | Ford accelerated the Pinto's production timeline from the normal 43 months to under 25 months, causing tooling to proceed simultaneously with product development; when crash tests revealed serious fuel tank defects, the tooling was already underway and the defective design was released to production despite known safety failures and available alternatives like the Capri tank. | Lee Iacocca; Bob Alexander; Ford engineers; Ford Motor Co. | 1970-1971 design and production planning | E10, E11, E12 |
| Purdue OxyContin | ●●● strong (n=64, 12 docs) | Purdue's wrongdoing escalated through successive steps: initial false marketing claims about addiction risk (1996), expansion of sales force and prescriber targeting (1996-2001), promotion for non-cancer pain, intensified detailing of highest-volume prescribers (2010-2013), and continued marketing to known diverters despite evidence of abuse, with each step building on prior accepted practices and generating profits that justified further escalation. ⚠ | Purdue Pharma; Sackler family; sales representatives | 1996 to 2017 | E13, E14, E15 |

### Redefinition of acceptable risk and standards

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=99, 20 docs) | Boeing and FAA personnel reinterpreted MCAS hazard classifications and pilot response assumptions to classify risks as acceptable: Boeing classified uncommanded MCAS as "major" rather than "catastrophic" despite knowing consequences could be catastrophic if pilots did not respond within 10 seconds; Boeing assumed repeated MCAS activations posed no greater hazard than single activations; Boeing and employees agreed to exclude MCAS from pilot training documents by claiming it operated "outside normal operating envelope." | Boeing employees; Boeing engineering and test pilots; FAA AEG | 2015-2018 for MCAS coordination sheets; 2016-2017 for FSB edits | E16, E17, E18 |
| Dieselgate | ●●● strong (n=74, 12 docs) | Technical and legal standards for emissions testing and compliance were reinterpreted by manufacturers, regulators, and authorities to treat deviations from real-world emissions limits as acceptable when they occurred outside narrow laboratory test conditions, and motor protection exceptions were construed broadly to justify shutdown devices that reduced emissions control in normal driving situations. | Volkswagen; EU Member States; KBA; EPA | 2000s through 2015 | E19, E20, E21 |
| Enron | ●●● strong (n=80, 15 docs) | Enron executives, Andersen auditors, and board members systematically reinterpreted accounting standards to classify non-compliant structures as acceptable: SPE equity requirements were treated as satisfiable through hidden loans and restricted investments, mark-to-market valuations were applied to speculative long-term contracts without independent verification, hedging transactions were reframed as legitimate despite lacking economic substance, and side agreements were kept oral or unwritten to avoid triggering consolidation rules. | Enron executives and management; Arthur Andersen auditors; Enron Board of Directors | 1997 to 2001 | E22, E23, E24 |
| Ford Pinto | ●●● strong (n=21, 5 docs) | Ford reinterpreted safety standards by using cost-benefit analysis to justify accepting fuel tank failures at 20-30 mph that failed proposed standards, reframing the problem as impact rather than fire, and proceeding without remedies despite knowing inexpensive fixes existed. | Ford; NHTSA; Ford management; Ford accountants | 1971-1977 | E25, E26, E27 |
| Purdue OxyContin | ●●● strong (n=34, 11 docs) | Purdue and affiliated organizations systematically reinterpreted addiction risk, abuse potential, and dosing standards by misrepresenting scientific evidence, reframing drug-seeking behavior as "pseudoaddiction," classifying physical dependence as "normal," and claiming no ceiling dose exists, thereby redefining dangerous practices as acceptable medical treatment. | Purdue Pharma; FDA; American Academy of Pain Medicine; Sackler family executives | 1995 to 2014 | E28, E29, E30 |

### Institutionalization in routines, structures and technology

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=48, 17 docs) | Wrongful practices were embedded in formal procedures, software code, product designs, and approval workflows including MCAS design specifications, FSB Report templates, training materials, removal documentation systems, stamping protocols, and assembly sequences that persisted across organizational units and survived personnel changes. | Boeing; FAA; Boeing Employee-1; Boeing Employee-2 | 2013 to 2023 | E31, E32, E33 |
| Dieselgate | ●●● strong (n=38, 12 docs) | Defeat device software was embedded in electronic control modules across multiple vehicle models and model years (2009-2015 for 2.0L engines, 2009-2016 for 3.0L engines), installed during manufacturing and distributed through software updates during routine maintenance, affecting approximately 585,000 vehicles sold in the United States across multiple VW and Audi product lines. | Volkswagen AG; Audi AG; Bosch; VW GOA | 2009 through 2015 | E34, E35, E36 |
| Enron | ●●● strong (n=61, 16 docs) | Enron embedded fraudulent financial practices in formal procedures, organizational structures, and approval workflows—including budget target systems, deal approval sheets, reserve accounts, and SPE transactions—that persisted across business units and survived personnel changes through systematic institutionalization. | Skilling; Causey; Fastow; Enron Board | 1997 to October 2001 | E37, E38, E39 |
| Ford Pinto | ●●● strong (n=11, 4 docs) | Ford embedded unsafe design decisions in formal product objectives, engineering specifications, production procedures, and approval workflows that persisted through the chain of command, with the Pinto's fuel tank vulnerability built into the vehicle's structure and replicated across product lines like the Mercury Bobcat. | Iacocca; Ford engineers; Vice Presidents Alexander and MacDonald | Pinto development and production | E40, E41, E42 |
| Purdue OxyContin | ●●● strong (n=63, 12 docs) | Purdue embedded aggressive opioid promotion in formal sales structures, compensation systems, targeting protocols, training programs, and monitoring systems that persisted across years and survived personnel changes, with the practice institutionalized through decile-based call plans, bonus formulas tied to prescription volume, standardized scripts and messaging, and formal procedures like the ADD Program that were used selectively to continue marketing to flagged prescribers. | Purdue Pharma; Sackler family; Sales representatives; McKinsey & Company | 1996 to 2018 | E43, E44, E45 |

### Collective rationalizations and shared vocabulary

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=62, 15 docs) | Boeing employees and officials used shared vocabulary and collective rationalizations to frame MCAS as a minor, background system outside normal operations ("addition to Speed Trim," "way outside the normal operating envelope") and justified design choices by emphasizing pilot capability, industry-standard assumptions, and regulatory compliance rather than safety-based reasoning. | Boeing employees; Boeing management; FAA-AEG; Boeing Authorized Representatives | 2013 to 2017 | E46, E47, E48 |
| Dieselgate | ●●● strong (n=66, 11 docs) | VW employees and managers used euphemisms like "acoustic function," "cycle beating," "emissions-tight mode," and "dyno mode" to describe the defeat device across internal communications, presentations, and meetings, while collectively attributing discrepancies between lab and real-world emissions to inadequate testing standards rather than intentional cheating, creating shared organizational vocabulary that normalized the practice. | Volkswagen AG employees and managers; Audi engineers; VW Powertrain Development division | 2006 to 2015 | E49, E50, E51 |
| Enron | ●●● strong (n=68, 15 docs) | Enron executives and finance staff used specialized vocabulary and euphemisms—"gap," "stretch," "overview," "off-balance-sheet," "monetizing," "syndicating," "dirty close," "nuisance fee," "nuclear waste," "parking," "warehousing," "Friends of Enron," "dot-com luster," and "Enron time machine"—to describe fraudulent transactions in ways that made them seem like legitimate business practices. | Skilling; Fastow; Causey; Enron management | 1997 through 2001 | E52, E53, E54 |
| Ford Pinto | ●●● strong (n=19, 4 docs) | Ford leadership and engineers developed shared vocabularies and ideologies that normalized safety compromises: "safety doesn't sell," prioritizing trunk space over tank safety, and using cost-benefit calculations to justify trading lives for profits as standard corporate practice. | Lee Iacocca; Ford engineers; Ford management | 1970-1977 | E55, E56, E57 |
| Purdue OxyContin | ●●● strong (n=33, 8 docs) | Purdue and allied actors used euphemisms ("Improving the Length Of Therapy," "appropriate patients," "identify care gaps"), framed opioid prescribing as addressing undertreated pain, blamed addiction on "reckless criminals" rather than the drug, and contracted with third parties using language that concealed the true goal of increasing prescriptions while claiming adherence to evidence-based guidelines. | Purdue Pharma; Sackler family; Practice Fusion | 1995 to 2018 | E58, E59, E60 |

### Socialization and co-optation of newcomers

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●○ moderate (n=30, 10 docs) | New technical pilots and managers were drawn into promoting Level B non-simulator training through rewards and status recognition, while schedule pressure and retaliation threats discouraged raising safety concerns. | Boeing technical pilots; Boeing Employee-1; Boeing Employee-2; 737 MAX program leadership | Early 2012 to July 2018 | E61, E62, E63 |
| Dieselgate | ●●○ moderate (n=10, 4 docs) | New engineers and managers joining VW were drawn into the cheating practice through direct involvement and instruction: engineers explained the defeat software to senior managers GOTTWEIS and NEUSSER, who then instructed them to conceal it; managers like PETER directed employees to develop misleading arguments for regulators; and employees were positioned to avoid consciously lying by being excluded from meetings. | GOTTWEIS; NEUSSER; PETER; DORENKAMP | 2006 to 2015 | E64, E65, E66 |
| Enron | ●●● strong (n=47, 12 docs) | New employees and managers were drawn into fraudulent SPE schemes through gradual involvement in transactions, co-optation via extraordinary financial returns on small investments, threats of firing or bonus loss if they did not cooperate, and mentoring by senior perpetrators like Fastow and Kopper who directly recruited them into partnerships. | Fastow; Kopper; Glisan; NatWest bankers | 1997-2001 | E67, E68, E69 |
| Ford Pinto | ○○○ absent (n=0, 0 docs) | No passages coded. |  | not stated |  |
| Purdue OxyContin | ●●● strong (n=34, 10 docs) | Purdue systematically trained sales representatives with false claims about addiction risk and abuse potential, rewarded them based on prescription volume, and co-opted physicians through speaker programs, paid speaking fees, and targeted recruitment at resort conferences, while board members and executives aligned with the Sacklers' strategy to expand the sales force and drive opioid prescriptions. | Purdue sales representatives; Purdue executives and Sacklers; Physicians and healthcare providers; Board members | 1996 to 2018 | E70, E71, E72 |

### Structural secrecy and fragmented knowledge

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=143, 20 docs) | Boeing's organizational structure fragmented knowledge of MCAS across separate groups with different responsibilities, reporting lines, and information access: the Flight Technical Team briefed FAA-AEG on pilot training while a different group disclosed MCAS expansion only to airworthiness certification personnel, and the FAA itself was divided into disconnected groups that received partial information, preventing any single entity from seeing the complete picture of MCAS's operational scope and safety implications. | Boeing Flight Technical Team; FAA Aircraft Evaluation Group; FAA airworthiness certification personnel; Boeing | 2016 to 2019 | E73, E74, E75 |
| Dieselgate | ●●● strong (n=90, 15 docs) | Specialization and compartmentalization within VW prevented full visibility: engineers knew only their module, EEO staff kept knowledge restricted within their department, and regulators received only partial information from manufacturers who controlled what documentation was disclosed, while type-approval authorities relied on manufacturer-provided test documentation without access to source code or ability to verify software independently. | VW engineers and EEO staff; EPA and CARB regulators; KBA type-approval authority | 2007-2015 | E76, E77, E78 |
| Enron | ●●● strong (n=106, 15 docs) | Specialization and compartmentalization prevented people from seeing the whole picture: board members received only high-level summaries and minimal transaction details; auditors and lawyers reviewed narrow scopes without seeing full context; different business units and finance staff operated in silos; information about side agreements, buyback commitments, and credit problems was deliberately withheld from oversight bodies. | Board members; Arthur Andersen auditors; Enron management; Causey | 1999-2001 | E79, E80, E81 |
| Ford Pinto | ●●● strong (n=19, 5 docs) | Ford engineers conducted crash tests showing fuel tank rupture at low speeds and forwarded results up the chain of command, but this critical safety information was compartmentalized and not shared with decision-makers who chose production, regulators who received incomplete data, and the public who were kept unaware of the tests' existence. | Ford engineers; Ford management; NHTSA; juries | 1971 to 1977 | E82, E83, E84 |
| Purdue OxyContin | ●●● strong (n=38, 8 docs) | Purdue compartmentalized knowledge through specialized departments with restricted information flow, used oral communications and avoided written records to prevent discovery, and provided Board members only summaries and selected data rather than complete information about wrongdoing and compliance violations. | Purdue Sales and Marketing Department; Abuse and Diversion Detection Program; Board of Directors | 2007 to 2016 | E85, E86, E87 |

### Leadership tolerance and cultural endorsement

| Case | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Boeing 737MAX | ●●● strong (n=101, 17 docs) | Senior Boeing leaders prioritized production schedule and financial success over safety, rewarding those who met schedules and pressuring employees to avoid delays, while tolerating design shortcuts and withholding safety information from regulators and customers. | Boeing senior executives; Muilenburg; Campbell; Leverkuhn | 2014-2019 | E88, E89, E90 |
| Dieselgate | ●●● strong (n=48, 7 docs) | Senior VW managers authorized and approved the defeat device software despite knowing it violated emissions standards; managers instructed engineers to destroy evidence and approved concealment strategies presented in briefings. | Winterkorn; Neusser; Gottweis; Hadler | 2006-2015 | E91, E92, E93 |
| Enron | ●●● strong (n=129, 15 docs) | Senior leaders and the Board approved conflict-of-interest waivers for Fastow, set earnings targets that required off-balance-sheet transactions to meet, approved complex SPE structures despite known risks, and rewarded executives with stock options and bonuses tied to reported earnings, signaling that achieving financial targets through these means was acceptable. ⚠ | Skilling; Lay; Causey; Fastow | 1998-2001 | E94, E95, E96 |
| Ford Pinto | ●●● strong (n=14, 4 docs) | Senior Ford management, including the Product Planning Committee and executives like Iacocca and MacDonald, approved the Pinto's production despite knowing from crash tests that the fuel tank was vulnerable to rupture at low speeds, and prioritized cost savings and production schedules over safety fixes, creating a culture where safety was not a popular subject and engineers who raised concerns faced dismissal. | Ford Product Planning Committee; Lee Iacocca; Robert Alexander; Harold MacDonald | 1968-1971 | E97, E98, E99 |
| Purdue OxyContin | ●●● strong (n=87, 11 docs) | Senior leaders and board members, particularly the Sackler family, tolerated and actively endorsed aggressive opioid marketing to high-volume prescribers, rewarded sales performance regardless of abuse signals, overruled compliance concerns, and pressured executives to increase sales targets and dosages despite evidence of diversion and addiction. | Sackler family members; Board of Directors; Richard Sackler; Purdue executives | 2009-2016 | E100, E101, E102 |

## Evidence

**E1.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 54

> Subsequently, Boeing expanded MCAS's operational scope, including the speed range within which MCAS could activate, significantly altering its original design. Among other things, when the airplane registered a high angle of attack, the change expanded the speed range within which MCAS could activate from approximately Mach 0.6-0.8 to approximately Mach 0.2-0.8—that is, from only high-speed flight to nearly the entire speed range for the 737 MAX, including low-speed flight, which generally occur…

**E2.** Boeing 737MAX, *SEC_Order_Muilenburg_33-11106_2022-09-22*, p. 4 ≈

> MCAS was originally designed to operate only under conditions involving both high speeds (Mach 0.6-0.8) and high AoA, conditions that were "outside the normal flight envelope." MCAS was therefore not expected to engage during the course of a normal commercial flight. Later in the design and certification process, however, Boeing expanded the operational scope of MCAS to address a tendency of the 737 MAX to pitch upwards at high AoA even at lower speeds. To achieve this, Boeing widened the speed …

**E3.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 110 ≈

> As originally designed, MCAS was only capable of moving the horizontal stabilizer a maximum of 0.6 degrees. However, in March 2016, one year prior to the FAA's certification of the 737 MAX, when Boeing test pilots found the MAX was not handling well when nearing stalls at lower speeds, Boeing redesigned MCAS to enable it to activate at lower speeds. Moreover, the new version of MCAS was capable of moving the horizontal stabilizer a maximum of 2.5 degrees (as opposed to 0.6 degrees as originally …

**E4.** Dieselgate, *DOJ_EPA_Amended_Civil_Complaint_2016*, p. 20 ≈

> Prior to 2005, engineers at Audi AG developed a software function, which engineers at Volkswagen AG later referred to as the "Akustikfunktion," among other aliases. On or about November 10, 2006, Volkswagen AG's contractor submitted a request, on behalf of Volkswagen AG, for a software design change to the Akustikfunktion for 2.0L diesel engines that created the dual-mode strategy referred to in Paragraphs 88-89. Between 2006 and 2014, employees in Volkswagen AG's Powertrain Development division…

**E5.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 18 ≈

> Following the launch of the Gen 1 2.0 Liter Subject Vehicles in the United States, DORENKAMP, HADLER, and their co-conspirators worked on a second generation of the diesel engine (the "Gen 2"), which also contained software designed to detect, evade, and defeat U.S. emissions tests. The Gen 2 2.0 Liter Subject Vehicles were launched in the United States starting in or around 2011.

**E6.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 20

> To solve the hardware failures, VW engineers decided to start the 2.0 Liter Subject Vehicles in the "street mode" and, when the defeat device recognized that the vehicle was being tested, switch to the "dyno mode." To increase the likelihood that the software in fact recognized that the vehicle was being tested on the dynamometer, the VW engineers activated a "steering wheel angle recognition" feature. The steering wheel angle recognition interacted with the software by enabling the vehicle to d…

**E7.** Enron, *House_EC_Hearing_Pt3_Watkins_testimony_2002-02-14*, p. 21 ≈

> when you and I spoke yesterday you described that in your earlier days working for Mr. Fastow, the special purpose entities were basically legitimate. They seemed to be garden variety, securitized entities that were designed to serve legitimate financial purposes with which you had no qualms. And as you explained, Condor was one of those early SPEs that fit that category. As you described your time with the company, it seemed to me that it was like the story of the frog in the pot on the stove. …

**E8.** Enron, *Fastow_Superseding_Information*, p. 7 ≈

> By 1999, Enron was increasingly dependent on transactions with SPEs to close the gap between its actual business performance and its financial reporting goals. By June 1999, in order to have an off-balance-sheet SPE to which Enron regularly could turn, Enron's Board of Directors (the "Board") agreed to permit FASTOW to create and serve as the managing partner of a new SPE known as LJM Cayman. The Board later approved FASTOW's participation in another SPE, known as LJM2 (the LJM entities hereafte…

**E9.** Enron, *Skilling_Lay_Causey_Superseding_Indictment*, p. 20 ≈

> Beginning in the spring of 2000, Enron and LJM engaged in a series of financial transactions with four SPEs called Raptor I, Raptor II, Raptor III and Raptor IV (collectively referred to as the 'Raptors'). Defendants JEFFREY K. SKILLING and RICHARD A. CAUSEY, Fastow, Enron Treasurer Ben F. Glisan, Jr., and their coconspirators used the Raptors to manipulate fraudulently Enron's reported financial results. They designed and approved Raptor I, among other things, to protect Enron from having to re…

**E10.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Like the Mustang, the Pinto became known in the company as "Lee's car." Lee Iococca wanted that little car in the showrooms of America with the 1971 models. So he ordered his engineering vice president, Bob Alexander, to oversee what was probably the shortest production planning period in modern automotive history. The normal time span from conception to production of a new car model is about 43 months. The Pinto schedule was set at just under 25.

**E11.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> A quick glance at the bar chart below will show you what that speed-up meant. Design, styling, product planning,advance engineering and quality assurance all have flexible time frames, and engineers can pretty much carry these on simultaneously. Tooling, on the other hand, has a fixed time frame of about 18 months. Normally, an auto company doesn't begin tooling until the other processes are almost over: you don't want to make the machines that stamp and press and grind metal into the shape of c…

**E12.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo* ≈

> So why wasn't the Capri tank used in the Pinto? Or, why wasn't that plastic baffle placed between the tank and the axle—something that would have saved the life of Sandra Gillespie and hundreds like her? Why was a car known to be a serious fire hazard deliberately released to production in August of 1970? In pre-production planning, engineers seriously considered using in the Pinto the same kind of gas tank Ford uses in the Capri. The Capri tank rides over the rear axle and differential housing.…

**E13.** Purdue OxyContin, *Senate_Judiciary_Brownlee_Testimony_2007-07-31*, p. 3

> Despite knowing that OxyContin contained high concentrations of oxycodone HCL, had an abuse potential similar to that of morphine, and was at least as addictive as other pain medications on the market, Purdue, beginning in January 1996, marketed and promoted OxyContin as less addictive, less subject to abuse and diversion, and less likely to cause tolerance and withdrawal than other pain medications.

**E14.** Purdue OxyContin, *Senate_Judiciary_Brownlee_Testimony_2007-07-31*, p. 2

> Backed by an aggressive marketing campaign, Purdue's OxyContin became a promising pain medication for many doctors and patients. Purdue claimed it had created a new, low risk drug that could provide long acting pain relief but was less addictive and less subject to abuse than other pain medications. But OxyContin was not what Purdue claimed it was. Purdue's assertions that OxyContin was less addictive and less subject to abuse and diversion were false - and the company knew its claims were false…

**E15.** Purdue OxyContin, *Purdue_Criminal_Information_DNJ_2020-11-24*, p. 6 ≈

> PURDUE PHARMA directed its sales representatives to repeatedly visit the most prolific Prescribers of its opioid products and encourage those Prescribers to prescribe increased numbers of PURDUE PHARMA opioid products. PURDUE PHARMA adopted this marketing strategy, in part, because it knew that the top 2 percent of opioid Prescribers wrote close to 80 percent of OxyContin prescriptions nationwide. PURDUE PHARMA identified these highest-prescribing Prescribers as "Super Core" and "Core" prescribe…

**E16.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 121 ≈

> Despite the fact that Boeing knew that the consequences could be "catastrophic" if a pilot did not react quickly enough to uncommanded MCAS activation, and the fact that Boeing cited this fact repeatedly over the years in their internal coordination sheets on MCAS, based on their own internal test data, no one at Boeing apparently informed the FAA about this critical data. Between 2015 and 2018 Boeing issued six separate coordination sheets on MCAS that referenced the "catastrophic" consequences…

**E17.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 123 ≈

> Boeing had assumed that repetitive MCAS activations would not adversely impact the ability of the MAX pilots to maintain control of the aircraft despite the fact that a Boeing AR raised this question. Boeing "Engineering and Test pilots discussed scenario of repeated unintended MCAS activation during MAX development," according to a December 2018 Boeing presentation to the FAA, "and deemed [it] no worse than single unintended MCAS activation." Those assumptions were proven tragically wrong.

**E18.** Boeing 737MAX, *FAA_737MAX_Technical_Advisory_Board_Report*, p. 23 ≈

> Boeing concluded during the design phase that multiple rapidly successive MCAS events, when dwelling in the high AOA region, are no more hazardous than a single MCAS event, since it was assumed the pilot would use the electric trim to completely counteract any out-of-trim forces. Boeing engineers and test pilots discussed the scenario of repeated unintended MCAS activation during MAX development and deemed it no worse than single unintended MCAS activation.

**E19.** Dieselgate, *EuroParl_EMIS_Inquiry_Final_Report_A8-0049-2017*, p. 54

> In their written answers and during the hearings, Member States and car manufacturers stated that they interpreted the legislation in such a way that the NEDC test in the laboratory was the only requirement for vehicles to pass, despite the air-quality objectives of the legislation [Renault, VW, ACEA, Mitsubishi, MIT, KBA, UTAC, Millbrook, Verheugen, Q:OEM].

**E20.** Dieselgate, *Bundestag_Abgas_Untersuchungsausschuss_Report_Drs18-12900_2017_DE*, p. 514

> Statt den Schutz des Motors vor einem Schaden zu verlangen, beschränkt sich die Ausnahmevorschrift auf einen weitaus weniger gravierenden Schutz vor einer Beschädigung. Konsequenz der Regelungsunschärfe ist, dass unter Berufung auf den Motorschutz die Verwendung von Abschalteinrichtungen letztlich stets dann gerechtfertigt werden kann, wenn von Seiten des Fahrzeugherstellers nachvollziehbar dargestellt wird, dass ohne die Verwendung einer solchen Einrichtung dem Motor irgendeine Beschädigung dro…

**E21.** Dieselgate, *Bundestag_Abgas_Untersuchungsausschuss_Report_Drs18-12900_2017_DE*, p. 513 ≈

> Im geltenden Recht begünstigen diese Auslegungsspielräume die Position der Hersteller... Ein zentrales Problem bei der Anwendung der Verordnung (EG) Nr. 715/2007 ist, was die normalen Betriebsbedingungen sind, unter denen die Wirksamkeit des Emissionsminderungssystems gewährleistet sein muss... Nach Aussage der Zeugen aus dem Kraftfahrt-Bundesamt und dem Bundesverkehrsministerium besteht in diesem Punkt eine erhebliche Rechtsunsicherheit, die sich nur durch klare Vorgaben zu Fahrstrecke, Fahrwei…

**E22.** Enron, *SEC_Complaint_Fastow_2002*

> Under applicable accounting rules, an SPE could receive off-balance-sheet treatment only if independent third-party investors made a substantive capital investment, generally at least three percent of the SPE's assets, and the third-party investment were genuinely at risk, among other things. If the third-party were not truly independent, or its investment were not truly at risk, those transactions using the SPEs were improper.

**E23.** Enron, *Causey_Indictment_2004*, p. 8

> The Raptor I structure, however, was invalid under applicable accounting rules because Talon was not independent from Enron, and LJM2's investment in Talon was not at risk. Defendant RICHARD A. CAUSEY and Fastow had an oral side deal that LJM2 would receive its initial investment in Talon plus a profit of $11 million from Enron, all prior to Talon engaging in any of the hedging transactions for which it was created. As a quid pro quo for this payment to LJM2, Fastow agreed with CAUSEY that Enron…

**E24.** Enron, *SEC_Complaint_Skilling_Causey_2004* ≈

> The Raptor I structure, however, was invalid under applicable accounting rules because Talon was not independent from Enron, and LJM's investment in Talon was not sufficiently "at risk" to qualify as outside equity. Causey and Fastow had an oral side deal that LJM2 would receive its initial investment in Talon plus a profit of $11 million from Enron, all prior to Talon engaging in any of the hedging transactions for which it was created. As a quid pro quo for this payment to LJM2, Fastow agreed …

**E25.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Remember, Ford had gotten the federal regulators to agree to talk auto safety in terms of cost-benefit analysis. But in order to be able to argue that various safety costs were greater than their benefits, Ford needed to have a dollar value figure for the "benefit." Rather than be so uncouth as to come up with such a price tag itself, the auto industry pressured the National Highway Traffic Safety Administration to do so. And in a 1972 report the agency decided a human life was worth $200,725. I…

**E26.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Not long after the government arrived at the $200,725-per-life figure, it surfaced, rounded off to a cleaner $200,000, in an internal Ford memorandum. This cost-benefit analysis argued that Ford should not make an $11-per-car improvement that would prevent 180 fiery deaths a year. (This minor change would have prevented gas tanks from breaking so easily both in rear-end collisions, like Sandra Gillespie's, and in rollover accidents, where the same thing tends to happen.)

**E27.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Ford now had to enter its third round of battling the new regulations. On the "the problem is not X but Y" principle, the company had to look around for something new to get itself off the hook. One might have thought that, faced with all the latest statistics on the horrifying number of deaths in flaming accidents, Ford would find the task difficult. But the company's rhetoric was brilliant. The problem was not burns, but…impact! Most of the people killed in these fiery accidents, claimed Ford,…

**E28.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 26 ≈

> Purdue presented to doctors a concept called "pseudoaddiction." A Purdue pamphlet titled Clinical Issues in Opioid Prescribing urged doctors to look for pseudoaddiction: "A term which has been used to describe patient behaviors that may occur when pain is undertreated. Patients with unrelieved pain may become focused on obtaining medications, may 'clock watch,' and may otherwise seem inappropriately 'drug-seeking.' Even such behaviors as illicit drug use and deception can occur in the patient's …

**E29.** Purdue OxyContin, *VanZee_2009_Promotion_and_Marketing_of_OxyContin_AJPH*, p. 3 ≈

> Purdue trained its sales representatives to carry the message that the risk of addiction was 'less than one percent.' The company cited studies by Porter and Jick, who found iatrogenic addiction in only 4 of 11882 patients using opioids and by Perry and Heidrich, who found no addiction among 10 000 burn patients treated with opioids. Both of these studies, although shedding some light on the risk of addiction for acute pain, do not help establish the risk of iatrogenic addiction when opioids are…

**E30.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 31 ≈

> To "extend average treatment duration," Purdue deceptively claimed that patients' becoming dependent on its drugs was not dangerous or deadly, but "normal." Purdue taught doctors that: "Healthcare professionals should recognize that tolerance and physical dependence are normal consequences of sustained use of opioid analgesics and are not the same as addiction." Purdue deceptively claimed that physical dependence on its opioids was "a normal physiologic response," "an expected occurrence," and n…

**E31.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 75 ≈

> While this change relieved FAA of an administrative burden, it limited the interactions between ARs and FAA staff, which as the JATR report noted, prevented the free communication of issues and concerns. In Boeing's item tracking compliance system database, called ITRACS, that documented this decision suggested that cost was also a factor in the plan to downplay MCAS and to describe it as merely an addition to the Speed Trim System. On May 21, 2013, as part of that strategy meeting, the issue wa…

**E32.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 40 ≈

> From in or around January 2017 through in or around July 2017 (when the 737 MAX FSB Report was published), Boeing Employee-1 and Boeing Employee-2 sent and caused to be sent emails to representatives of various Boeing airline customers that had agreed to purchase the 737 MAX, including major U.S.-based airlines. In these emails, Boeing Employee-1 and Boeing Employee-2 or members of their 737 MAX Flight Technical Team referenced and included drafts of the forthcoming 737 MAX FSB Report and airpla…

**E33.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 41 ≈

> On or about July 5, 2017, the FAA AEG published the first 737 MAX FSB Report, which included the FAA AEG's 'Level B' differences-training determination for the 737 MAX. Because of Boeing's intentional withholding of information from the FAA AEG, the final version of the 737 MAX FSB Report lacked information about MCAS, and relevant portions of this 737 MAX FSB Report were materially false, inaccurate, and incomplete. In turn, airplane manuals and pilot-training materials for U.S.-based airlines …

**E34.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 26

> As a result of the conspiracy, DORENKAMP, NEUSSER, HADLER, GOTTWEIS, PETER, WINTERKORN, and their co-conspirators caused defeat device software to be installed on all of the approximately 585,000 Subject Vehicles and Porsche Vehicles sold in the United States from 2009 through 2015.

**E35.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 21

> VW employees then installed the new software function in new 2.0 Liter Subject Vehicles being sold in the United States, and later installed it in existing 2.0 Liter Subject Vehicles through software updates during routine vehicle maintenance.

**E36.** Dieselgate, *DOJ_EPA_Amended_Civil_Complaint_2016*, p. 14 ≈

> Bosch manufactures and sells ECMs, and a basic ECM software set, to vehicle manufacturers. The basic ECM software offered by Bosch can be customized by manufacturers within certain parameters that are established by the source code for the software. If manufacturers wish to further customize the ECM software for their vehicles, they can request that Bosch change the parameters for a function in the ECM software. Bosch manufactured and sold the Electronic Diesel Control-17 ("EDC17") ECM and its s…

**E37.** Enron, *SEC_Complaint_Skilling_Causey_2004*

> Skilling and Causey set annual and quarterly earnings and cash flow targets ("budget targets") for the company and each of its business units. They did so by determining the numbers necessary to meet analysts' expectations, rather than what could be realistically achieved by legitimate business operations. On a quarterly and year-end basis, Skilling, Causey, and others assessed Enron's progress toward its budget targets. When the budget targets were not met through actual results from business o…

**E38.** Enron, *Skilling_Lay_Causey_Superseding_Indictment*, p. 7 ≈

> Defendants JEFFREY K. SKILLING and RICHARD A. CAUSEY were among the principal architects and operators of the scheme to manipulate Enron's reported financial results and to present Enron in a misleading manner. Together with their coconspirators, they set annual and quarterly earnings and cash flow targets ('budget targets') for the company as a whole and for each of Enron's business units. In furtherance of the scheme to defraud, SKILLING and CAUSEY, together with their coconspirators and other…

**E39.** Enron, *Fastow_Superseding_Information*, p. 8

> From approximately July 1999 through October 2001, Enron entered into transactions with LJM that defrauded Enron, its shareholders, the SEC, credit rating agencies, and others. The transactions with LJM enabled Enron to: (a) manipulate its reported financial results by readily and unobtrusively moving poorly performing assets off balance sheet, when in fact such off-balance-sheet treatment was improper; (b) conceal Enron's poor operating performance by engaging in transactions designed to close …

**E40.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo* ≈

> The product objectives are clearly stated in the Pinto "green book." This is a thick, top-secret manual in green covers containing a step-by-step production plan for the model, detailing the metallurgy, weight, strength and quality of every part in the car. The product objectives for the Pinto are repeated in an article by Ford executive F.G. Olsen published by the Society of Automotive Engineers. He lists these product objectives as follows: 1. TRUE SUBCOMPACT Size Weight 2. LOW COST OF OWNERSH…

**E41.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Heightening the anti-safety pressure on Pinto engineers was an important goal set by Iacocca known as "the limits of 2,000." The Pinto was not to weigh an ounce over 2,000 pounds and not to cost a cent over $2,000. "Iacocca enforced these limits with an iron hand," recalls the engineer quoted earlier. So, even when a crash test showed that that one-pound, one-dollar piece of plastic stopped the puncture of the gas tank, it was thrown out as extra cost and extra weight.

**E42.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 777 ≈

> As the project approached actual production, the engineers responsible for the components of the project 'signed off' to their immediate supervisors who in turn 'signed off' to their superiors and so on up the chain of command until the entire project was approved for public release by Vice Presidents Alexander and MacDonald and ultimately by Mr. Iacocca. The Pinto crash tests results had been forwarded up the chain of command to the ultimate decision-makers and were known to the Ford officials …

**E43.** Purdue OxyContin, *DOJ_Purdue_Civil_Settlement_Agreement_2020-10*, p. 31 ≈

> Purdue ranked the prescribers based on their aggregate opioid prescriptions in deciles from numbers 1 through 10, with 10 being the highest. From 2010 to 2013, Purdue instructed its sales force to primarily focus on the top three deciles of prescribers. The purpose of focusing the sales force on these highest deciles of prescribers was to cause an even higher volume of prescriptions to be written by them. Purdue knew, at that time, that the three highest deciles of prescribers combined accounted…

**E44.** Purdue OxyContin, *Purdue_Plea_Agreement_2020-10-20*, p. 54 ≈

> Purdue ranked the prescribers based on their aggregate opioid prescriptions in deciles from numbers 1 through 10, with 10 being the highest. From 2010 to 2013, Purdue instructed its sales force to primarily focus on the top three deciles of prescribers. Purdue executives closely analyzed Purdue's internal data, including data purchased from vendors, in order to target high-volume prescribers and monitor their prescriptions.

**E45.** Purdue OxyContin, *Purdue_Plea_Agreement_2020-10-20*, p. 67 ≈

> E2E was overseen by the consulting company and some of Purdue's top executives through the creation of the E2E Executive Oversight Team (EOT) and Project Management Office (PMO). Based on a study showing that providers in deciles 7-10 were most responsive to sales calls and were the most prolific writers, the E2E call plans instructed sales representatives to call on the very highest deciles of high-volume prescribers with the most frequency. Specifically, Purdue instructed its sales representat…

**E46.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 99 ≈

> In May 2013, a group of Boeing employees working on the 737 MAX met to address another concern: If we emphasize MCAS is a new function there may be greater certification and training impact, one Boeing employee wrote in a June 7, 2013, email summarizing the minutes of that meeting. They planned to, Treat [MCAS] as an addition to Speed Trim . . . Externally we would communicate it as an addition to Speed Trim. Internally continue using the acronym MCAS. They agreed to run the strategy by an Autho…

**E47.** Boeing 737MAX, *SEC_Order_Muilenburg_33-11106_2022-09-22*, p. 5 ≈

> Boeing employees responsible for communicating with the FAA-AEG presented MCAS to the FAA-AEG as a feature that could only activate in a very specific, high-speed scenario that was outside the normal flight envelope and therefore unlikely to ever be encountered by a commercial pilot. They made these representations to FAA-AEG personnel beginning in or around June 2015.

**E48.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 59

> Flight Controls: Delete MCAS, recall we decided we weren't going to cover it [. . .] since it's way outside the normal operating envelope.

**E49.** Dieselgate, *DOJ_EPA_Amended_Civil_Complaint_2016*, p. 20 ≈

> Prior to 2005, engineers at Audi AG developed a software function, which engineers at Volkswagen AG later referred to as the "Akustikfunktion," among other aliases. Between 2006 and 2014, employees in Volkswagen AG's Powertrain Development division, including managers, regularly communicated with each other, and contractors, regarding the design and later refinements of the dual-mode strategy, referred to as the "extended Akustikfunktion," among other aliases.

**E50.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 14 ≈

> DORENKAMP, HADLER, and their co-conspirators referred to the software as, among other things, the "acoustic function," "switch logic," "cycle beating," or "emissions-tight mode."

**E51.** Dieselgate, *Pamio_Complaint_2017*, p. 21 ≈

> On or about January 23, 2008, Audi engineers who helped design the dosing strategy sent a presentation to senior Audi managers, including PAMIO, to warn that the dosing strategy constituted "cycle beating," which was "[h]ighly problematic in the US[]" because, among other things, it was an undisclosed AECD and possibly a defeat device, and could be discovered by the regulators.

**E52.** Enron, *SEC_Complaint_Skilling_Causey_2004*

> These shortfalls were referred to within Enron variously as the "gap," "stretch," or "overview."

**E53.** Enron, *Fastow_Complaint_Affidavit_2002*, p. 11

> According to Kopper and others, this transaction was referred to as a "dirty close," because participants knew that the Chewco structure failed to comply with SPE rules, as Chewco had made no true equity investment and Enron had guaranteed the banks against risk of loss on the loans. Enron thus planned for financial reporting purposes to replace the structure before year end with one that would qualify Chewco as an off-balance-sheet SPE.

**E54.** Enron, *Kopper_Information_2002*, p. 2

> Enron management preferred the latter result – known as "off-balance-sheet"– because it enabled Enron to present itself more attractively as measured by criteria favored by Wall Street investment analysts and credit rating agencies.

**E55.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> As Lee Iacocca was fond of saying, "Safety doesn't sell."

**E56.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> When it was discovered the gas tank was unsafe, did anyone go to Iacocca and tell him? "Hell no," replied an engineer who worked on the Pinto, a high company official for many years, who, unlike several others at Ford, maintains a necessarily clandestine concern for safety. "That person would have been fired. Safety wasn't a popular subject around Ford in those days. With Lee it was taboo. Whenever a problem was raised that meant a delay on the Pinto, Lee would chomp on his cigar, look out the w…

**E57.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Ford's cost-benefit table is buried in a seven-page company memorandum entitled "Fatalities Associated with Crash-Induced Fuel Leakage and Fires." The memo argues that there is no financial benefit in complying with proposed safety standards that would admittedly result in fewer auto fires, fewer burn deaths and fewer burn injuries. Naturally, memoranda that speak so casually of "burn deaths" and "burn injuries" are not released to the public.

**E58.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 30

> Purdue secretly determined that pushing patients to higher doses would keep them on opioids longer. Purdue developed tactics specifically to keep patients hooked on opioids longer, which it called by the euphemism: "Improving the Length Of Therapy" — sometimes abbreviated as "LOT" or "LoT."

**E59.** Purdue OxyContin, *Purdue_Criminal_Information_DNJ_2020-11-24*, p. 67

> While Practice Fusion and PURDUE employees used euphemisms like "appropriate patients," "identify care gaps," and "better manage patients," both parties understood a goal of the program was to increase ERO use.

**E60.** Purdue OxyContin, *Purdue_Criminal_Information_DNJ_2020-11-24*, p. 75 ≈

> Despite the parties' understanding that the purpose of the Pain CDS was to increase ERO prescriptions, the contract stated that the "Parties agree and acknowledge that the collaboration project will follow national evidenced-based guidelines, and will not encourage the prescribing or utilization of a Purdue-specific product or services." Notwithstanding the Pain CDS Contract, a written internal Practice Fusion recap of the initial conference call between Practice Fusion and PURDUE PHARMA to desi…

**E61.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 124

> To thank Mr. Teal for his leadership of the 737 MAX program and for helping to keep the program on schedule, Mr. Teal received a bonus in the form of restricted Boeing stock shares after the first flight of the 737 MAX in January 2016.

**E62.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 147 ≈

> In September 2016, the Committee has learned, Boeing granted its team of technical pilots the company's Commercial Aviation Services (CAS) Service Excellence Award for their role in "developing the MAX Level B [non-simulator] differences training...." The Committee's investigation has confirmed that in September 2016, one month after the FAA provided Boeing with provisional approval for Level B (non-simulator) training for 737 MAX pilots, Mr. Forkner and his team of technical pilots that had bee…

**E63.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 79

> At the new Town Hall meetings, 737 program leadership increased schedule pressure by publicly grilling lower-level managers about delays in front of a hundred or more of their peers, even when the cause of a delay was completely beyond the individual employee's control.

**E64.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 19 ≈

> In or around July 2012, engineers from the VW Brand Engine Development department met, in separate meetings, with GOTTWEIS and NEUSSER to explain that they suspected the cause of the hardware failures in the Subject Vehicles was the increased stress on the exhaust system from being driven too long in "dyno" mode as a result of the use of software designed to detect, evade and defeat U.S. emission tests. To illustrate the software's function, the engineers used a document. Although GOTTWEIS and N…

**E65.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 33

> On or about May 12, 2015, PETER sent an email to VW AG employees referencing on-road emissions measurements by CARB in mid-April through June. PETER proposed possible misleading and false arguments to present to CARB as to why the vehicles were not passing the emissions tests on the road.

**E66.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 34

> On or about August 17, 2015, Oliver Schmidt wrote to a manager at VW that another manager had just "explained to me on the telephone why [another VW employee] should not come along [to a future CARB meeting] - so he would not have to consciously lie."

**E67.** Enron, *House_EC_Hearing_Pt1_Powers_testimony_2002-02-05*, p. 66 ≈

> You have Glisan who has presented to the Raptor I transaction to the board. He was called the business unit originator and the person negotiating for Enron. He is the guy on the other side of the table, and Fastow says, 'Come on in and be an investor on this side of the table, and you make a million dollars as a result in 6 weeks.'

**E68.** Enron, *Powers_Report_Special_Investigative_Committee_2002-02-01*, p. 95

> Even based on the limited information we have, the Enron employees received massive returns on their modest investments. We have seen documents indicating that, in return for its $25,000 investment, the Fastow Family Foundation received $4.5 million on May 1, 2000. Glisan and Mordaunt separately told us that, in return for their small investments, they each received approximately $1 million within a matter of one or two months, an extraordinary return. Mordaunt told us that she got no explanatio…

**E69.** Enron, *House_EC_Hearing_Pt1_Powers_testimony_2002-02-05*, p. 28

> managers of the partnerships were actually threatening people at Enron with firing if they aggressively negotiated for Enron. They threatened others with loss of their bonuses.

**E70.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 224

> Gasdia knew how sales reps increased prescriptions. He wrote scripts used to train Purdue sales reps — including, for example, the plan to use fake patient profiles to encourage prescribers to prescribe Butrans to patients who were not on opioids.

**E71.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 56 ≈

> From the beginning, the Sacklers were behind Purdue's decision to deceive doctors and patients. Purdue launched OxyContin in 1996. It became one of the deadliest drugs of all time. The company hired hundreds of sales representatives and taught them false claims to use to sell drugs. Purdue managers tested the sales reps on the most important false statements during training at company headquarters. On the crucial issue of addiction, which would damage so many lives, Purdue trained its sales reps…

**E72.** Purdue OxyContin, *DOJ_Purdue_Civil_Settlement_Agreement_2020-10*, p. 32

> In turn, sales representatives were rewarded with incentive compensation tied to the volume of OxyContin prescriptions generated from the health care providers they had detailed and faced corrective action plans, such as performance improvement plans, when they did not meet their sales goals.

**E73.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 100

> The FAA was not completely unaware of MCAS; however, because the information and discussions about MCAS were so fragmented and were delivered to disconnected groups within the process, it was difficult to recognize the impacts and implications of this system.

**E74.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 50

> Boeing's 737 MAX Flight Technical Team was principally responsible for identifying and providing to the FAA AEG all information that was relevant to the FAA AEG in connection with the FAA AEG's publication of the 737 MAX FSB Report. The 737 MAX Flight Technical Team was separate and distinct from another group within Boeing that was responsible for providing information to the FAA for certification of whether the airplane met U.S. federal airworthiness standards.

**E75.** Boeing 737MAX, *Boeing_Non-Prosecution_Agreement_2025-05-29*, p. 28

> Boeing disclosed this expansion to FAA personnel, but only to those personnel who were responsible for determining whether the 737 MAX met U.S. federal airworthiness standards. Boeing did not disclose the expansion to the FAA AEG personnel responsible for publishing the 737 MAX FSB Report and making the training-related determination.

**E76.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 29

> In his cover email, SCHMIDT concluded with, "Within VW GOA, the study is known only to EEO, and we want to keep it that way for the time being."

**E77.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 30 ≈

> On or about April 15, 2014, Oliver Schmidt forwarded GOTTWEIS a copy of the ICCT presentation, and an email chain in which a VW employee stated, "[s]ome presenters indicated that they suspected cheating, where the vehicle recognizes it is an [sic] a dyno and runs different calibration that [sic] what it runs in actual driving. We will have to be careful with this going forward." In his cover email, Schmidt concluded, "[w]ithin VWGoA, the study is known only to EEO, and we want to keep it that wa…

**E78.** Dieselgate, *Bundestag_Abgas_Untersuchungsausschuss_Report_Drs18-12900_2017_DE*, p. 515

> Das Kraftfahrt-Bundesamt prüft fortlaufend im Rahmen von Konformitätsprüfungen (CoP-P-Prüfungen), ob und wie die Fahrzeughersteller ihrer gesetzlichen Selbstverpflichtung nachkommen. Hierbei setzt das Kraftfahrt-Bundesamt grundsätzlich auf der Prüfdokumentation des Herstellers auf.

**E79.** Enron, *Senate_PSI_Role_of_Board_in_Enrons_Collapse_2002*, p. 14

> The Subcommittee interviews indicated that, altogether, Board members appeared to have routine contact with less than a dozen senior officers at Enron. The Board did not have a practice of meeting without Enron management present.

**E80.** Enron, *Powers_Report_Special_Investigative_Committee_2002-02-01*, p. 159

> It appears that, at the meeting for the February 2001 review, the Committees were not provided with important information. The presentation included a discussion of the Raptor vehicles that had been created the preceding year. Apparently, however, the Committees were not told that two of the vehicles then owed Enron approximately $175 million more than they had the capacity to pay. This information was contained in a report that was provided daily to Causey and Buy, but it appears that neither o…

**E81.** Enron, *Senate_PSI_Role_of_Board_in_Enrons_Collapse_2002*, p. 34 ≈

> On paper, the Audit Committee conducted two annual reviews of LJM transactions in February 2000 and February 2001. In reality, these reviews were superficial and relied entirely on management representations with no supporting documentation or independent inquiry into facts. At the first review in 2000, the Audit Committee was given a single sheet of paper listing the names of eight transactions that LJM had entered into with Enron in 1999. The only information provided for each transaction was …

**E82.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> Internal company documents in our possession show that Ford has crash-tested the Pinto at a top-secret site more than 40 times and that every test made at over 25 mph without special structural alteration of the car has resulted in a ruptured fuel tank. Despite this, Ford officials denied under oath having crash-tested the Pinto.

**E83.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 777 ≈

> The Pinto crash tests results had been forwarded up the chain of command to the ultimate decision-makers and were known to the Ford officials who decided to go forward with production. Harley Copp, a former Ford engineer and executive in charge of the crash testing program, testified that the highest level of Ford's management made the decision to go forward with the production of the Pinto, knowing that the gas tank was vulnerable to puncture and rupture at low rear impact speeds.

**E84.** Ford Pinto, *Dowie_1977_Pinto_Madness_MotherJones_incl_Ford_cost-benefit_memo*

> When the Pinto liability suits began, Ford strategy was to go to a jury. Confident it could hide the Pinto crash tests, Ford thought that juries of solid American registered voters would buy the industry doctrine that drivers, not cars, cause accidents.

**E85.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 12

> Purdue used face-to-face sales visits to conceal its deception by trying to avoid witnesses or a paper trail. When one sales rep made the mistake of writing down in an email her sales pitch to a doctor, Purdue's Vice President of Sales Russell Gasdia ordered: "Fire her now!" Purdue's leaders did not want a record of their behavior because they knew they were breaking the law.

**E86.** Purdue OxyContin, *House_Oversight_Hearing_Purdue_Sackler_2020-12-17*, p. 41

> As a director of the company, I would not know the specific actions and speakings of the sales department.

**E87.** Purdue OxyContin, *Massachusetts_AG_First_Amended_Complaint_Purdue_Sacklers_2019-01-31*, p. 148 ≈

> That February report was the last of its kind. After Q4 2013, Purdue abolished the detailed Quarterly Reports that had created a paper trail of targets for sales visits and been emailed among the Board and staff. In 2013, the City of Chicago served Purdue with a subpoena seeking internal documents about Purdue's marketing of opioids. That provoked a flurry of activity, including discussion among the Sacklers. Purdue fought the subpoena, and it was withdrawn. For 2014, Purdue decided to limit man…

**E88.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 25

> The Committee has learned that to thank him for keeping to the MAX's production schedule, Boeing gave Michael Teal, the former Chief Project Engineer on the 737 MAX program, restricted stock options after the airplane's first flight in 2016 to show its appreciation for his work.

**E89.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 44

> Boeing senior executives prioritized the movement of aircraft through Boeing's factories over reducing out-of-sequence work to ensure production quality.

**E90.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 244

> When people say I changed the culture of Boeing, that was the intent, so it's run like a business rather than a great engineering firm.

**E91.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 20 ≈

> Certain VW employees again expressed concern, specifically about the expansion of the defeat device through the steering wheel angle detection, and sought approval for the function from more senior managers. In particular, VW AG engineers asked NEUSSER for a decision on whether or not to use the proposed function. In or about April 2013, NEUSSER authorized activation of the software underlying the steering wheel angle recognition function.

**E92.** Dieselgate, *Dorenkamp_et_al_Second_Superseding_Indictment*, p. 15 ≈

> Throughout in or around 2006, DORENKAMP authorized VW engineers to use the defeat device in the development of the US'07 project, despite concerns expressed by certain VW AG employees about the propriety of designing and activating the defeat device software.

**E93.** Dieselgate, *Winterkorn_et_al_Fifth_Superseding_Indictment*, p. 24 ≈

> When U.S. regulators threatened not to certify VW model year 2016 vehicles for sale in the United States, WINTERKORN requested a briefing on the situation in the United States. On or about July 27, 2015, VW employees presented to WINTERKORN, NEUSSER, and other senior VW AG management at an in-person meeting at VW's headquarters in Wolfsburg. VW AG employees used a PowerPoint presentation to provide to WINTERKORN a clear picture of: (1) how VW was deceiving U.S. regulators, including precisely wh…

**E94.** Enron, *SEC_Complaint_Skilling_Causey_2004*

> In June 1999, in order to have an allegedly independent third party available to provide this outside equity funding so that Enron could more easily create and use SPEs to achieve its desired financial reporting results, Skilling, Causey, and others sought and obtained the approval of Enron's Board of Directors (the "Board") for Fastow to create and serve as the managing partner of an investment partnership named LJM Cayman, L.P. that would invest in SPEs for Enron. The Board later approved Fast…

**E95.** Enron, *House_EC_Hearing_Pt1_Powers_testimony_2002-02-05*, p. 14

> the board waived Enron conflict of interest rules for Mr. Fastow to allow him partial ownership and managerial duties in Chewco and LJM while still on the payroll of Enron as a senior executive.

**E96.** Enron, *Powers_Report_Special_Investigative_Committee_2002-02-01*, p. 9

> The Board approved Fastow's participation in the LJM partnerships with full knowledge and discussion of the obvious conflict of interest that would result. The Board apparently believed that the conflict, and the substantial risks associated with it, could be mitigated through certain controls (involving oversight by both the Board and Senior Management) to ensure that transactions were done on terms fair to Enron.

**E97.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 777 ≈

> Harley Copp, a former Ford engineer and executive in charge of the crash testing program, testified that the highest level of Ford's management made the decision to go forward with the production of the Pinto, knowing that the gas tank was vulnerable to puncture and rupture at low rear impact speeds creating a significant risk of death or injury from fire and knowing that 'fixes' were feasible at nominal cost. He testified that management's decision was based on the cost savings which would inur…

**E98.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 777

> The idea for the Pinto, as has been noted, was conceived by Mr. Iacocca, then executive vice president of Ford. The feasibility study was conducted under the supervision of Mr. Robert Alexander, vice president of car engineering. Ford's Product Planning Committee, whose members included Mr. Iacocca, Mr. Robert Alexander, and Mr. Harold MacDonald, Ford's group vice president of car engineering, approved the Pinto's concept and made the decision to go forward with the project. During the course of…

**E99.** Ford Pinto, *Grimshaw_v_Ford_Motor_Co_1981_CalCtApp_119CalApp3d757*, p. 777 ≈

> At an April 1971 product review meeting chaired by Mr. MacDonald, those present received and discussed a report (exhibit 125) prepared by Ford engineers pertaining to the financial impact of a proposed federal standard on fuel system integrity and the cost savings which would accrue from deferring even minimal 'fixes.' The report refers to crash tests of the integrity of the fuel system of Ford vehicles and design changes needed to meet anticipated federal standards.

**E100.** Purdue OxyContin, *House_Oversight_Supplemental_Staff_Memo_2020-12-14*, p. 3

> Documents obtained by DOJ show that from 2013 to 2018, Purdue—with the express approval of members of the Sackler family—engaged in a marketing initiative called "Evolve to Excellence" (E2E), developed in conjunction with the consulting firm McKinsey & Company, to intensify marketing to the highest-volume opioid prescribers and target them with increased frequency.

**E101.** Purdue OxyContin, *SCOTUS_Harrington_v_Purdue_Pharma_Opinion_2024-06-27*, p. 6

> Purdue was a " 'family company,' " owned and controlled by the Sacklers. Id., at 40. Members of the Sackler family served as president and chief executive officer; they dominated the board of directors; and they "were heavily involved" in the firm's marketing strategies. 69 F. 4th, at 86 (Wesley, J., concurring in judgment). They "pushed sales targets," too, and "accompanied sales representatives on 'ride along' visits to health care providers" in an effort to maximize OxyContin sales.

**E102.** Purdue OxyContin, *House_Oversight_Hearing_Purdue_Sackler_2020-12-17*, p. 38

> According to internal documents that were obtained by the committee and the Massachusetts Attorney General, the Sacklers as board members were ordering a company—this was, again, after the slap on the wrist in 2007—to hire hundreds more sales reps, directed those reps to target the highest prescribers of OxyContin, push highest strength dosage of OxyContin, approve misleading marketing materials that downplayed the risk of the addiction, rewarding employees for selling more drugs.
