# Boeing 737MAX: comparison across theories

*Generated 2026-10-29 by compare_tables.py with eu.anthropic.claude-haiku-4-5-20251001-v1:0, from analysis_output/*.csv. Presence: ●●● strong, ●●○ moderate, ●○○ weak, ○○○ absent; n = passages coded. Coverage = presence points ÷ maximum, computed in Python. ⚠ = answer trimmed after failing a rule check.*

## Theory fit

| Theory | Fit | Coverage | What it explains | What it leaves unexplained | Strongest category |
|---|---|---|---|---|---|
| Strain and performance pressure | high | 100% | Boeing's deliberate concealment of MCAS from pilot training and FAA certification resulted from intense strain: aggressive production schedules, competitive pressure from Airbus, contractual commitments to Level B training, and financial incentives tied to cost reduction and schedule adherence that made legitimate design solutions infeasible. | Why Boeing employees collectively rationalized and normalized MCAS expansion across organizational units despite knowing it violated safety standards, and how organizational structures fragmented knowledge to prevent detection. | Choosing the deviant path |
| Normalization of deviance and corruption | high | 95% | MCAS evolved through incremental design expansions from high-speed-only to full-envelope operation, with each step justified by operational needs but collectively transforming risk profiles. Boeing embedded wrongful practices in formal procedures, software code, and approval workflows while using shared vocabulary to frame MCAS as minor and outside normal operations. | The initial strain and competitive pressures that motivated Boeing to pursue cost-reduction strategies, and how organizational fragmentation enabled concealment from regulators despite internal knowledge of MCAS expansion. | Incremental drift and escalation |
| Moral disengagement and neutralization | high | 87% | Boeing employees justified cost-reduction and design decisions through appeal to business imperatives, used euphemistic labeling to obscure MCAS's true scope, displaced responsibility to the FAA, distorted consequences by claiming pilots could overcome failures, and blamed pilots for crashes rather than system defects. | The organizational structures and fragmented knowledge systems that enabled concealment, and how routine business processes and regulatory delegation created opportunities for wrongdoing. | Euphemistic labeling |
| Routine activity theory and the opportunity perspective | high | 100% | Boeing employees in legitimate occupational roles exploited predictable FAA certification routines, delegated oversight, and organizational fragmentation to conceal MCAS expansion. Pilots and passengers lacked information and capability to detect the system, while internal controls failed to prevent wrongdoing despite supervisory concerns. | The psychological mechanisms of moral disengagement that allowed employees to rationalize concealment, and how incremental normalization of deviance embedded wrongful practices into organizational routines. | Weakened, captured or delegated guardianship |
| Attention-based view of the firm | high | 100% | Boeing's organizational structure fragmented attention across multiple positions and FAA groups, preventing integrated understanding of MCAS's full operational scope. Financial incentives and production schedules made cost reduction salient while rendering safety risks invisible, and Boeing intentionally withheld critical information from decision-makers. | The strain and competitive pressures that created incentives for concealment, and how moral disengagement mechanisms allowed employees to justify withholding information despite internal warnings. | Filtering, discounting and neglect of warnings |

## Complementarities

- **Strain and performance pressure + Normalization of deviance and corruption**: Strain from production schedules and cost-reduction targets motivated Boeing to pursue MCAS concealment, which then became normalized through incremental design expansions and embedded in organizational routines and procedures.
- **Moral disengagement and neutralization + Routine activity theory and the opportunity perspective**: Boeing employees used moral disengagement to justify concealment while exploiting organizational fragmentation, delegated FAA oversight, and predictable certification routines that created opportunities for wrongdoing to succeed.
- **Attention-based view of the firm + Normalization of deviance and corruption**: Financial incentives and production schedules directed organizational attention away from safety risks while MCAS expansion became normalized through incremental steps, embedding wrongful practices in formal procedures and shared vocabulary.

## Category detail

### Strain and performance pressure

| Category | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Goals and targets | ●●● strong (n=61, 15 docs) | Boeing set a specific design objective to require no greater than Level B (non-simulator) pilot training for the 737 MAX, which demanded keeping differences training to 16 hours or less of computer-based training, and pursued this goal through contractual guarantees to customers and public commitments made years before FAA certification. | Boeing; Boeing Employee-1; Boeing Employee-2; FAA | 2011 to 2016 | E1, E2, E3 |
| Blocked legitimate means | ●●● strong (n=99, 17 docs) | Boeing faced multiple technical and regulatory constraints that could not be met by legitimate means: the 737 MAX's larger engines created aerodynamic pitch-up characteristics that violated FAA certification requirements unless addressed by MCAS; meeting fuel efficiency goals while maintaining ground clearance required engine placement that altered aerodynamics; and avoiding simulator training requirements to preserve airline cost savings conflicted with the need for pilot training on MCAS, forcing Boeing to exclude MCAS from training and manuals despite its operational scope expansion. | Boeing; FAA; Southwest Airlines | 2012-2017 | E4, E5, E6 |
| Competitive and market pressure | ●●● strong (n=15, 5 docs) | Boeing faced intense competitive pressure from Airbus' A320neo aircraft and the threat of losing major customers like American Airlines, which drove the rapid development and aggressive production schedule of the 737 MAX to maintain market share and meet delivery commitments. | Boeing; Airbus; American Airlines; Jim McNerney | 2010-2018 | E7, E8, E9 |
| Performance shortfall and aspiration gaps | ●●● strong (n=51, 11 docs) | Boeing faced severe production pressures and quality deterioration as it pursued aggressive delivery schedules and profit targets, with factory metrics hitting record lows, quality issues increasing over 30%, and employees reporting undue pressure from managers regarding safety approvals due to time and schedule concerns. | Boeing; Boeing managers; Boeing employees | 2013-2019, particularly 2018-2019 | E10, E11, E12 |
| Incentives and rewards tied to targets | ●●● strong (n=6, 2 docs) | Boeing tied compensation and awards to achieving production schedule targets and cost-saving outcomes, including restricted stock options for the Chief Project Engineer for keeping the MAX on schedule, awards for technical pilots who promoted non-simulator training to reduce costs, and bonus structures where safety measures comprised only 4% of annual incentive awards. | Michael Teal; Chief Technical Pilot; Technical pilots team; Boeing executives | 2016-2022 | E13, E14, E15 |
| Pressure transmitted down the hierarchy | ●●● strong (n=50, 10 docs) | Senior Boeing management communicated non-negotiable production schedules and profit-driven priorities downward through the hierarchy, with middle managers and supervisors pressuring frontline employees and engineers to meet deadlines despite safety concerns, using questions like "when are you going to be done" and emphasizing schedule over safety. | Boeing senior management; Scott Campbell (737 General Manager); Ed Pierson (senior plant supervisor); Boeing frontline employees and engineers | 2016-2018 | E16, E17, E18 |
| Choosing the deviant path | ●●● strong (n=162, 19 docs) | Boeing employees made deliberate decisions to conceal MCAS's expanded operational scope from the FAA AEG, remove MCAS references from pilot manuals and training materials, and withhold information about the AOA disagree alert malfunction to avoid costly Level D training requirements and maintain certification timelines. | Boeing Employee-1; Boeing Employee-2; Boeing management; FAA AEG | 2016-2017 | E19, E20, E21 |

### Normalization of deviance and corruption

| Category | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Incremental drift and escalation | ●●● strong (n=75, 17 docs) | MCAS evolved through successive design expansions from a high-speed-only system (Mach 0.6-0.8) to one operating across nearly the entire flight envelope (Mach 0.2-0.8), with command authority increasing from 0.6 degrees to 2.5 degrees, each step justified by operational needs but collectively transforming the system's scope and risk profile without corresponding safety reassessment. | Boeing engineers and employees; Boeing management; FAA personnel | June 2015 to March 2017 | E22, E23, E24 |
| Redefinition of acceptable risk and standards | ●●● strong (n=99, 20 docs) | Boeing and FAA personnel reinterpreted MCAS hazard classifications and pilot response assumptions to classify risks as acceptable: Boeing classified uncommanded MCAS as "major" rather than "catastrophic" despite knowing consequences could be catastrophic if pilots did not respond within 10 seconds; Boeing assumed repeated MCAS activations posed no greater hazard than single activations; Boeing and employees agreed to exclude MCAS from pilot training documents by claiming it operated "outside normal operating envelope." | Boeing employees; Boeing engineering and test pilots; FAA AEG | 2015-2018 for MCAS coordination sheets; 2016-2017 for FSB edits | E25, E26, E27 |
| Institutionalization in routines, structures and technology | ●●● strong (n=48, 17 docs) | Wrongful practices were embedded in formal procedures, software code, product designs, and approval workflows including MCAS design specifications, FSB Report templates, training materials, removal documentation systems, stamping protocols, and assembly sequences that persisted across organizational units and survived personnel changes. | Boeing; FAA; Boeing Employee-1; Boeing Employee-2 | 2013 to 2023 | E28, E29, E30 |
| Collective rationalizations and shared vocabulary | ●●● strong (n=62, 15 docs) | Boeing employees and officials used shared vocabulary and collective rationalizations to frame MCAS as a minor, background system outside normal operations ("addition to Speed Trim," "way outside the normal operating envelope") and justified design choices by emphasizing pilot capability, industry-standard assumptions, and regulatory compliance rather than safety-based reasoning. | Boeing employees; Boeing management; FAA-AEG; Boeing Authorized Representatives | 2013 to 2017 | E31, E32, E33 |
| Socialization and co-optation of newcomers | ●●○ moderate (n=30, 10 docs) | New technical pilots and managers were drawn into promoting Level B non-simulator training through rewards and status recognition, while schedule pressure and retaliation threats discouraged raising safety concerns. | Boeing technical pilots; Boeing Employee-1; Boeing Employee-2; 737 MAX program leadership | Early 2012 to July 2018 | E34, E35, E36 |
| Structural secrecy and fragmented knowledge | ●●● strong (n=143, 20 docs) | Boeing's organizational structure fragmented knowledge of MCAS across separate groups with different responsibilities, reporting lines, and information access: the Flight Technical Team briefed FAA-AEG on pilot training while a different group disclosed MCAS expansion only to airworthiness certification personnel, and the FAA itself was divided into disconnected groups that received partial information, preventing any single entity from seeing the complete picture of MCAS's operational scope and safety implications. | Boeing Flight Technical Team; FAA Aircraft Evaluation Group; FAA airworthiness certification personnel; Boeing | 2016 to 2019 | E37, E38, E39 |
| Leadership tolerance and cultural endorsement | ●●● strong (n=101, 17 docs) | Senior Boeing leaders prioritized production schedule and financial success over safety, rewarding those who met schedules and pressuring employees to avoid delays, while tolerating design shortcuts and withholding safety information from regulators and customers. | Boeing senior executives; Muilenburg; Campbell; Leverkuhn | 2014-2019 | E13, E40, E41 |

### Moral disengagement and neutralization

| Category | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Moral justification and appeal to higher loyalties | ●●● strong (n=33, 12 docs) | Boeing justified cost-reduction and design decisions by appealing to business imperatives: minimizing pilot training costs to make the 737 MAX competitive with rival aircraft, securing Level B training to avoid contractual penalties and attract airline customers, and maintaining production schedules and profitability. | Boeing; Boeing Employee-1; Boeing Employee-2; Muilenburg | 2011 to 2018 | E42, E43, E44 |
| Euphemistic labeling | ●●● strong (n=56, 12 docs) | Boeing used sanitized and technical language to obscure MCAS's true operational scope and risks, describing it as an "addition to Speed Trim," an "extension" of existing systems, and a minor "control law," while deliberately removing MCAS references from pilot manuals and regulatory documents to avoid triggering higher certification and training requirements. | Boeing employees; FAA AEG; Boeing management | 2016-2017, through 737 MAX certification | E45, E46, E47 |
| Advantageous comparison | ●○○ weak (n=9, 5 docs) | Comparisons made to other aviation accidents and the aviation industry's overall safety record to contextualize the 737 MAX incidents as not uniquely problematic. | FAA; Boeing; foreign airlines | not stated | E48, E49 |
| Displacement of responsibility | ●●● strong (n=114, 22 docs) | Boeing employees withheld critical information about MCAS's expanded operational scope from the FAA, who relied on Boeing's representations to make certification decisions, then concealed the MCAS Expansion when the FAA made its provisional approval based on incomplete information. | Boeing employees; FAA-AEG; Boeing Employee-1; Boeing Employee-2 | 2016 | E50, E51, E52 |
| Diffusion of responsibility and denial of personal involvement | ●●● strong (n=52, 14 docs) | Boeing employees claimed lack of knowledge about MCAS changes and their implications ("no one told us"), senior executives claimed unawareness of critical information, responsibility was diffused across organizational units and processes, and information gaps were attributed to fragmented certification procedures and system design rather than individual accountability. | Boeing employees; Boeing senior executives; FAA; Chief technical pilots | 2016 to 2019 | E53, E54, E55 |
| Distortion or denial of consequences | ●●● strong (n=97, 18 docs) | Boeing and FAA personnel minimized, disputed, or misconstrued the consequences of MCAS failures by claiming pilots could easily overcome them, that risks were statistically trivial or remote, that multiple failures were no worse than single failures, and that harm was limited or manageable through existing procedures. | Boeing; FAA; Boeing engineers; Boeing safety engineers | 2016-2018, certification and pre-crash period | E56, E57, E58 |
| Blaming and dehumanizing victims | ●●● strong (n=34, 13 docs) | Boeing, FAA, and NTSB officials blamed pilots for inadequate response to MCAS failures, citing pilot error, inexperience, and failure to follow procedures, while downplaying or omitting system design defects and MCAS hazards in public communications and investigations. | Boeing; FAA; NTSB; pilots | 2018-2022 | E59, E60, E61 |
| Condemnation of the condemners | ●●● strong (n=17, 7 docs) | Boeing and FAA officials attacked the competence and motives of critics including whistleblowers, the NTSB, and pilots, dismissing whistleblower concerns as "rants," questioning pilot capabilities, and suggesting critics were biased or self-interested rather than engaging substantively with safety concerns. | Boeing; FAA managers; Whistleblowers; NTSB | 2017-2020 | E62, E63, E64 |
| Appeal to legality and technical compliance | ●●● strong (n=79, 18 docs) | Boeing and FAA officials repeatedly invoked formal compliance with regulations, certification standards, and design processes as justification for safety decisions, treating procedural adherence as settling moral questions about aircraft safety despite identified gaps in cumulative effects analysis and system integration. | Boeing; FAA; Muilenburg | 2014-2020 | E65, E66, E67 |
| Metaphor of the ledger | ●○○ weak (n=1, 1 docs) | Boeing argues that the Government has made significant progress to date, implicitly suggesting past compliance efforts should offset current objections to monitor selection and probation conditions. | Boeing; Government | not stated | E68 |

### Routine activity theory and the opportunity perspective

| Category | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Motivated offenders and their positions | ●●● strong (n=58, 20 docs) | Boeing employees in technical and management positions (Chief Technical Pilots, Chief Project Engineer, CEO) with authority over design, certification, and communications deliberately concealed MCAS capabilities and design changes from the FAA to secure lower-cost Level B training requirements and maintain production schedules, motivated by cost savings and schedule pressures. | Boeing Employee-1; Boeing Employee-2; Michael Teal; Dennis Muilenburg | November 2016 through December 2018 | E69, E70, E71 |
| Suitable targets | ●●● strong (n=67, 19 docs) | Pilots and passengers were suitable targets because they lacked information about MCAS and its operational scope, relied on incomplete manuals and training materials, and could not detect the system's activation or malfunction due to absent or inadequate displays and alerts. | Pilots; Passengers; Boeing; FAA AEG | 2017 to 2019 | E72, E73, E74 |
| Capable guardians and their capacity | ●●● strong (n=56, 20 docs) | The FAA and international regulators possessed formal authority and mandate to certify aircraft and determine pilot training requirements, but lacked sufficient resources, expertise, and independence to detect Boeing's withholding of MCAS information, with only 24 senior engineers overseeing 1,500 Boeing-designated representatives and inspectors reporting insufficient training and concerns that safety issues would not be addressed. | FAA Aircraft Evaluation Group; FAA Seattle BASOO office; Joint Authorities Technical Review | 2014-2020 | E75, E76, E77 |
| Weakened, captured or delegated guardianship | ●●● strong (n=150, 20 docs) | The FAA delegated approximately 40% of B737 MAX certification plans to Boeing's ODA; the FAA had inadequate awareness and limited involvement in MCAS certification, preventing independent assessment; Boeing employees withheld critical information about MCAS expansion from the FAA AEG while disclosing it selectively to other FAA personnel, exploiting organizational fragmentation within the FAA. | FAA; Boeing; Boeing ODA; FAA AEG | 2015-2016 | E78, E79, E19 |
| Predictable guardian routines | ●●● strong (n=36, 14 docs) | Boeing exploited predictable FAA certification routines by limiting MCAS disclosure to avoid triggering higher training requirements, withholding expanded operational scope from regulators during provisional approval, and strategically timing information submission to prevent FAA influence on design decisions. | Boeing; Boeing Employee-1; Boeing Employee-2; FAA AEG | 2015 to 2016 | E80, E81, E82 |
| Handlers and place managers (internal controls) | ●●● strong (n=99, 18 docs) | Internal handlers including supervisors, engineers, compliance officers, and board committees were present but largely failed to prevent or stop wrongdoing; supervisors raised concerns about safety and quality issues but were overruled or ignored by management, while compliance functions were absent or ineffective during critical periods, and internal controls failed to detect or stop fraudulent certifications and design decisions. | Scott Campbell, 737 General Manager; Ed Pierson, senior plant supervisor; Boeing senior executives; Global Compliance function | 2014-2019, with remedial measures after 2019 | E83, E84, E85 |
| Legitimate access and separation from victims | ●●● strong (n=54, 19 docs) | Boeing employees in legitimate occupational roles—including senior members of the 737 MAX Flight Technical Team and chief technical pilots—accessed FAA certification processes, provided information to regulators, communicated with airline customers, and submitted design documentation through routine business channels, while remaining spatially and organizationally distant from the pilots and passengers who would operate the aircraft. | Boeing employees; 737 MAX Flight Technical Team; FAA AEG; Airline customers | June 2015 to July 2017 | E86, E87, E88 |
| Superficial legitimacy and concealment | ●●● strong (n=99, 17 docs) | Boeing employees systematically concealed MCAS's expanded operational scope from the FAA by removing references to the system from pilot manuals and training materials, making misleading statements about its limited activation envelope, and withholding information about lower-speed operation to maintain the Level B training determination. | Boeing employees; FAA AEG; Boeing management | 2016-2017 | E89, E90, E91 |
| Convergence breaks and detection | ●●● strong (n=110, 20 docs) | Two fatal crashes (Lion Air October 2018, Ethiopian Airlines March 2019) triggered immediate detection by accident investigators, regulators, and government agencies, leading to emergency airworthiness directives, fleet grounding, technical reviews, congressional investigations, and DOJ criminal investigation into Boeing's certification disclosures. | FAA; NTSB; DOJ; House Transportation Committee | October 29, 2018 to March 13, 2019 and beyond | E92, E93, E94 |

### Attention-based view of the firm

| Category | Presence | Mechanism | Actors | Period | Evidence |
|---|---|---|---|---|---|
| Warning signals and anomalies | ●●● strong (n=152, 20 docs) | Boeing engineers predicted in June 2016 that erroneous AOA sensor data could cause adverse MCAS consequences and questioned whether pilots could combat repetitive activation; the FAA issued emergency airworthiness directives in November 2018 after the crashes; whistleblowers reported safety concerns to Congress after the crashes. | Boeing engineers; FAA; NTSB; whistleblowers | June 2016 (pre-crash); November 2018 onwards (post-crash) | E95, E96, E97 |
| Communication and procedural channels | ●●● strong (n=108, 22 docs) | Information about MCAS was fragmented across multiple certification documents and compartmentalized across different FAA groups and Boeing teams, preventing integrated understanding of the system's full operational scope and safety implications. | Boeing; FAA AEG; FAA BASOO; Boeing Flight Technical Team | 2015-2017 | E98, E99, E100 |
| Structural positions and players | ●●● strong (n=79, 21 docs) | Boeing's organizational structure fragmented attention across multiple positions with different responsibilities: the 737 MAX Flight Technical Team withheld MCAS expansion information from the FAA AEG, while other Boeing engineers and senior executives approved MCAS redesigns without full awareness of critical technical details; the FAA's 45-person BASOO office oversaw 1,500 Boeing ODA members with insufficient senior engineers, and separate FAA groups made airworthiness versus training determinations without coordinated information flow. | Boeing 737 MAX Flight Technical Team; FAA AEG; Boeing senior executives; FAA BASOO | 2012-2019 | E20, E101, E102 |
| Rules of the game and attention-directing incentives | ●●● strong (n=79, 16 docs) | Boeing's financial incentives, production schedules, and performance metrics prioritized cost reduction and schedule adherence over safety considerations, making schedule compliance and cost savings salient while rendering safety risks and comprehensive testing invisible to decision-makers. | Boeing senior program officials; Boeing employees; Boeing management; FAA | 2011-2019 | E103, E104, E105 |
| Focus of attention and dominant agendas | ●●● strong (n=52, 18 docs) | Boeing decision makers prioritized production volume and schedule adherence over design mitigation, while FAA management shifted focus from regulatory compliance to accommodating industry positions and applicant costs. | Boeing senior executives; Boeing program management; FAA management | 2013-2018 | E106, E107, E108 |
| Filtering, discounting and neglect of warnings | ●●● strong (n=134, 21 docs) | Boeing employees intentionally withheld and concealed from the FAA critical information about MCAS's expanded operational scope, deleted MCAS references from certification documents, and misled regulators about the system's capabilities, preventing decision makers from understanding the true scope of the hazard. | Boeing employees; FAA Aircraft Evaluation Group; Boeing senior executives | 2016-2017 | E109, E110, E111 |
| Organizational responses and moves | ●●● strong (n=100, 20 docs) | Boeing delayed fixes, deferred disclosures about MCAS, issued misleading advisories without naming the system, and resisted transparency with regulators while continuing production and sales despite internal safety concerns. | Boeing senior management; Boeing engineers; FAA; Boeing Flight Technical Team | November 2018 to 2019 | E112, E113, E114 |
| Attention shifts and triggering events | ●●● strong (n=60, 18 docs) | Two fatal crashes (Lion Air October 2018, Ethiopian Airlines March 2019) triggered immediate regulatory grounding, congressional investigations, media scrutiny, and internal Boeing safety reviews that redirected organizational attention to MCAS design and certification processes. | FAA; Boeing; Congress; NTSB | October 2018 to March 2019 | E115, E116, E117 |

## Evidence

**E1.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 146

> Ensuring no pilot simulator training was required was also a key feature of Boeing's business strategy for marketing the MAX to airlines.

**E2.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 33

> Principally for this reason, Boeing's stated objectives in designing the 737 MAX included securing the FAA AEG's determination to require no greater than "Level B" differences training in the 737 MAX FSB Report.

**E3.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 146 ≈

> Guaranteeing that the 737 MAX did not require simulator training for pilots transitioning from the 737 NG to the 737 MAX was a key Boeing objective of the 737 MAX program. This goal demanded that pilot differences training be kept to 16 hours or less of Level B (non-simulator) training requirements.

**E4.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 34 ≈

> To achieve its promised fuel efficiency, the 737 MAX used larger engines than the 737 NG. These larger engines, and their placement under the airplane's wings, meant that the aerodynamics of the 737 MAX differed from those of the 737 NG. These different aerodynamics created a new handling characteristic for the 737 MAX that caused the 737 MAX's nose to pitch up during a certain flight maneuver called a high-speed, wind-up turn. A high-speed, wind-up turn generally involved sharply turning the ai…

**E5.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 53 ≈

> To achieve its promised fuel efficiency, the 737 MAX used larger engines than the 737 NG. These larger engines, and their placement under the airplane's wings, meant that the aerodynamics of the 737 MAX differed from those of the 737 NG. These different aerodynamics created a new handling characteristic for the 737 MAX that caused the 737 MAX's nose to pitch up during a certain flight maneuver called a high-speed, wind-up turn. A high-speed, wind-up turn generally involved sharply turning the ai…

**E6.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 31 ≈

> Boeing had tremendous financial incentive to ensure that no regulatory determination requiring pilot simulator training for the 737 MAX was made. Under a contract signed in December 2011 with Southwest Airlines, the U.S. launch customer for the 737 MAX, Boeing was financially obligated to have discounted the price of each MAX airplane it delivered to Southwest by at least $1 million if the FAA had required simulator training for pilots transitioning from the 737 NG to the 737 MAX. Southwest had …

**E7.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 171

> The 737 MAX program was launched under intense financial pressure to aggressively compete with Airbus' new A320neo aircraft.

**E8.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 45 ≈

> According to the New York Times, in the spring of 2011, the CEO of The Boeing Company, Jim McNerney, received a call from Gerard Arpey, the CEO of American Airlines. The call was reportedly serious and the conversation frank. Boeing was told that American Airlines was about to close a deal to purchase hundreds of A320-family airplanes from Airbus. If Boeing wanted to maintain its business with American Airlines, Boeing would need to step up soon and offer a similar alternative aircraft or lose o…

**E9.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 45 ≈

> In December 2010, Boeing's chief competitor in the civil airplane market—the European consortium Airbus—launched the A320neo family of aircraft. The term neo stood for new engine option and was powered by new fuel-efficient engines that promised up to 15-percent greater fuel efficiency over previous aircraft. This translated into significant cost savings for airlines and potentially passengers, and created a competitive advantage for Airbus.

**E10.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 44 ≈

> William Lazonick, a Professor in Economics and Co-Director of the Center for Industrial Competitiveness at the University of Massachusetts in Lowell, Massachusetts, has written that Boeing's attempts to profit undermined its efforts to protect the flying public. Lazonick's research highlighted the fact that between 2013 and 2019, during the critical 737 MAX design, development, and certification process, Boeing spent $17.4 billion on stock dividends and an additional $43.1 billion on stock buyba…

**E11.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 188 ≈

> Mr. Pierson concluded his letter to Boeing's attorneys with a warning about the risks these issues posed to Boeing, its aircraft, and the flying public: 'Taken as a whole, the sheer volume of these issues highlights the considerable & unnecessary risk the company was (is still?) taking to meet ever increasing airplane production rates and delivery schedules. Employees with 20+ years 737 experience stated they had never seen the production system in such bad shape. As you stated, leaders based in…

**E12.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 76 ≈

> During this timeframe, the 737 factory was in chaos. Every single factory health metric was getting record low marks and each one was trending in the wrong direction. Those metrics are detailed in my written testimony and include overtime, quality reports and out-of-sequence work. Keep in mind that, on October 29, 2018, when the Lion Air plane crashed killing 189 people, it was only 2 months old. During the relevant period, the factory saw quality issues increase by over 30%, and NCRs grew rapid…

**E13.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 25

> The Committee has learned that to thank him for keeping to the MAX's production schedule, Boeing gave Michael Teal, the former Chief Project Engineer on the 737 MAX program, restricted stock options after the airplane's first flight in 2016 to show its appreciation for his work.

**E14.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 165 ≈

> In September 2016, one month after the FAA provided Boeing with provisional approval for Level B (non-simulator) training for 737 MAX pilots, Mr. Forkner and his team of technical pilots that had been promoting Level B training were granted an award for their efforts from Boeing. An internal Boeing email said that the technical pilot team received the company's Commercial Aviation Services (CAS) Service Excellence Award on September 14, 2016, 'along with the Training Development Team for their r…

**E15.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 34 ≈

> In December 2017, the Chief Technical Pilot referring to his efforts to talk airlines out of the need for simulator training wrote to a Boeing colleague: I save this company a sick amount of $$$$.

**E16.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 91 ≈

> This relentless schedule pressure was being put on frontline union employees, team leaders and managers by senior management. Understaffed MRB Engineers were also frequently being pressured to process Tags more expeditiously. 'When are you going to be done, done' was a repeatedly asked question. It was one of many questions used to apply schedule pressure on employees under the guise of holding people personally accountable. In other words this meant how come your crew hasn't finished their jobs…

**E17.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 25 ≈

> In June 2018, Ed Pierson, a senior Boeing plant supervisor at the company's Renton, Washington 737 MAX production factory, emailed Scott Campbell, the 737 General Manager, requesting a meeting about safety concerns. Mr. Pierson described multiple concerns about production and schedule pressures that were impacting quality control and safety issues. As a retired Naval Officer and former Squadron Commanding Officer, wrote Pierson, I know how dangerous even the smallest of defects can be to the saf…

**E18.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 184 ≈

> Mr. Pierson finally met with Mr. Campbell on Wednesday, July 18, 2018, in Mr. Campbell's office. Mr. Pierson described the meeting as tense. According to Mr. Pierson's testimony to the Committee in December 2019, when he walked into Mr. Campbell's office, Mr. Campbell asked him: 'Why are you here?' Mr. Pierson reminded him about their email exchange and the safety issues he had raised. Mr. Pierson recalled telling Mr. Campbell: ''In … military operations, if we have these kinds of indications of…

**E19.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 57

> Despite knowing that the FAA AEG had issued its provisional "Level B" determination without any awareness that MCAS's operational scope had been expanded to include high angle of attack conditions in nearly the entire speed range of ordinary commercial flight, Boeing Employee-1 and Boeing Employee-2 did not correct the FAA AEG's understanding of MCAS's operational scope or otherwise ensure that the FAA AEG's "Level B" determination was based on an accurate understanding of MCAS's operation. Inst…

**E20.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 35

> Subsequently, Boeing expanded MCAS's operational scope, including the speed range within which MCAS could activate, significantly altering its original design. Among other things, when the airplane registered a high angle of attack, the change expanded the speed range within which MCAS could activate from approximately Mach 0.6-0.8 to approximately Mach 0.2-0.8—that is, from only high-speed flight to nearly the entire speed range for the 737 MAX, including low-speed flight, which generally occur…

**E21.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 58

> In doing so, Boeing Employee-1 and Boeing Employee-2 deceived the FAA AEG into believing that the basis upon which the FAA AEG had initially "agreed" to remove any information about MCAS from the 737 MAX FSB Report—that MCAS could only activate during the limited operational scope of a high-speed, wind-up turn—remained the same. Boeing Employee-1 and Boeing Employee-2 withheld their knowledge of MCAS from the FAA AEG to avoid risking the FAA AEG taking any action that could threaten the differen…

**E22.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 54

> Subsequently, Boeing expanded MCAS's operational scope, including the speed range within which MCAS could activate, significantly altering its original design. Among other things, when the airplane registered a high angle of attack, the change expanded the speed range within which MCAS could activate from approximately Mach 0.6-0.8 to approximately Mach 0.2-0.8—that is, from only high-speed flight to nearly the entire speed range for the 737 MAX, including low-speed flight, which generally occur…

**E23.** Boeing 737MAX, *SEC_Order_Muilenburg_33-11106_2022-09-22*, p. 4 ≈

> MCAS was originally designed to operate only under conditions involving both high speeds (Mach 0.6-0.8) and high AoA, conditions that were "outside the normal flight envelope." MCAS was therefore not expected to engage during the course of a normal commercial flight. Later in the design and certification process, however, Boeing expanded the operational scope of MCAS to address a tendency of the 737 MAX to pitch upwards at high AoA even at lower speeds. To achieve this, Boeing widened the speed …

**E24.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 110 ≈

> As originally designed, MCAS was only capable of moving the horizontal stabilizer a maximum of 0.6 degrees. However, in March 2016, one year prior to the FAA's certification of the 737 MAX, when Boeing test pilots found the MAX was not handling well when nearing stalls at lower speeds, Boeing redesigned MCAS to enable it to activate at lower speeds. Moreover, the new version of MCAS was capable of moving the horizontal stabilizer a maximum of 2.5 degrees (as opposed to 0.6 degrees as originally …

**E25.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 121 ≈

> Despite the fact that Boeing knew that the consequences could be "catastrophic" if a pilot did not react quickly enough to uncommanded MCAS activation, and the fact that Boeing cited this fact repeatedly over the years in their internal coordination sheets on MCAS, based on their own internal test data, no one at Boeing apparently informed the FAA about this critical data. Between 2015 and 2018 Boeing issued six separate coordination sheets on MCAS that referenced the "catastrophic" consequences…

**E26.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 123 ≈

> Boeing had assumed that repetitive MCAS activations would not adversely impact the ability of the MAX pilots to maintain control of the aircraft despite the fact that a Boeing AR raised this question. Boeing "Engineering and Test pilots discussed scenario of repeated unintended MCAS activation during MAX development," according to a December 2018 Boeing presentation to the FAA, "and deemed [it] no worse than single unintended MCAS activation." Those assumptions were proven tragically wrong.

**E27.** Boeing 737MAX, *FAA_737MAX_Technical_Advisory_Board_Report*, p. 23 ≈

> Boeing concluded during the design phase that multiple rapidly successive MCAS events, when dwelling in the high AOA region, are no more hazardous than a single MCAS event, since it was assumed the pilot would use the electric trim to completely counteract any out-of-trim forces. Boeing engineers and test pilots discussed the scenario of repeated unintended MCAS activation during MAX development and deemed it no worse than single unintended MCAS activation.

**E28.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 75 ≈

> While this change relieved FAA of an administrative burden, it limited the interactions between ARs and FAA staff, which as the JATR report noted, prevented the free communication of issues and concerns. In Boeing's item tracking compliance system database, called ITRACS, that documented this decision suggested that cost was also a factor in the plan to downplay MCAS and to describe it as merely an addition to the Speed Trim System. On May 21, 2013, as part of that strategy meeting, the issue wa…

**E29.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 40 ≈

> From in or around January 2017 through in or around July 2017 (when the 737 MAX FSB Report was published), Boeing Employee-1 and Boeing Employee-2 sent and caused to be sent emails to representatives of various Boeing airline customers that had agreed to purchase the 737 MAX, including major U.S.-based airlines. In these emails, Boeing Employee-1 and Boeing Employee-2 or members of their 737 MAX Flight Technical Team referenced and included drafts of the forthcoming 737 MAX FSB Report and airpla…

**E30.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 41 ≈

> On or about July 5, 2017, the FAA AEG published the first 737 MAX FSB Report, which included the FAA AEG's 'Level B' differences-training determination for the 737 MAX. Because of Boeing's intentional withholding of information from the FAA AEG, the final version of the 737 MAX FSB Report lacked information about MCAS, and relevant portions of this 737 MAX FSB Report were materially false, inaccurate, and incomplete. In turn, airplane manuals and pilot-training materials for U.S.-based airlines …

**E31.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 99 ≈

> In May 2013, a group of Boeing employees working on the 737 MAX met to address another concern: If we emphasize MCAS is a new function there may be greater certification and training impact, one Boeing employee wrote in a June 7, 2013, email summarizing the minutes of that meeting. They planned to, Treat [MCAS] as an addition to Speed Trim . . . Externally we would communicate it as an addition to Speed Trim. Internally continue using the acronym MCAS. They agreed to run the strategy by an Autho…

**E32.** Boeing 737MAX, *SEC_Order_Muilenburg_33-11106_2022-09-22*, p. 5 ≈

> Boeing employees responsible for communicating with the FAA-AEG presented MCAS to the FAA-AEG as a feature that could only activate in a very specific, high-speed scenario that was outside the normal flight envelope and therefore unlikely to ever be encountered by a commercial pilot. They made these representations to FAA-AEG personnel beginning in or around June 2015.

**E33.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 59

> Flight Controls: Delete MCAS, recall we decided we weren't going to cover it [. . .] since it's way outside the normal operating envelope.

**E34.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 124

> To thank Mr. Teal for his leadership of the 737 MAX program and for helping to keep the program on schedule, Mr. Teal received a bonus in the form of restricted Boeing stock shares after the first flight of the 737 MAX in January 2016.

**E35.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 147 ≈

> In September 2016, the Committee has learned, Boeing granted its team of technical pilots the company's Commercial Aviation Services (CAS) Service Excellence Award for their role in "developing the MAX Level B [non-simulator] differences training...." The Committee's investigation has confirmed that in September 2016, one month after the FAA provided Boeing with provisional approval for Level B (non-simulator) training for 737 MAX pilots, Mr. Forkner and his team of technical pilots that had bee…

**E36.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 79

> At the new Town Hall meetings, 737 program leadership increased schedule pressure by publicly grilling lower-level managers about delays in front of a hundred or more of their peers, even when the cause of a delay was completely beyond the individual employee's control.

**E37.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 100

> The FAA was not completely unaware of MCAS; however, because the information and discussions about MCAS were so fragmented and were delivered to disconnected groups within the process, it was difficult to recognize the impacts and implications of this system.

**E38.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 50

> Boeing's 737 MAX Flight Technical Team was principally responsible for identifying and providing to the FAA AEG all information that was relevant to the FAA AEG in connection with the FAA AEG's publication of the 737 MAX FSB Report. The 737 MAX Flight Technical Team was separate and distinct from another group within Boeing that was responsible for providing information to the FAA for certification of whether the airplane met U.S. federal airworthiness standards.

**E39.** Boeing 737MAX, *Boeing_Non-Prosecution_Agreement_2025-05-29*, p. 28

> Boeing disclosed this expansion to FAA personnel, but only to those personnel who were responsible for determining whether the 737 MAX met U.S. federal airworthiness standards. Boeing did not disclose the expansion to the FAA AEG personnel responsible for publishing the 737 MAX FSB Report and making the training-related determination.

**E40.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 44

> Boeing senior executives prioritized the movement of aircraft through Boeing's factories over reducing out-of-sequence work to ensure production quality.

**E41.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 244

> When people say I changed the culture of Boeing, that was the intent, so it's run like a business rather than a great engineering firm.

**E42.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 52 ≈

> For example, a pilot could complete Level B differences training from anywhere in the world in a matter of hours using a computer or tablet. In contrast, a pilot could complete Level D differences training only by appearing in person wherever the pilot's airline operated a full-flight simulator. Apart from the cost of acquiring one or more multimillion-dollar simulators and other related expenses, airlines that were required by the FAA AEG to train pilots on a full-flight simulator could also lo…

**E43.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 31 ≈

> Under a contract signed in December 2011 with Southwest Airlines, the U.S. launch customer for the 737 MAX, Boeing was financially obligated to have discounted the price of each MAX airplane it delivered to Southwest by at least $1 million if the FAA had required simulator training for pilots transitioning from the 737 NG to the 737 MAX. Southwest had 200 firm orders for the MAX with the option to purchase an additional 191 MAX aircraft. Thus, if Boeing failed to obtain Level B (non-simulator) t…

**E44.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 148

> Financial pressures to limit pilot training requirements permeated critical design and development decisions within the MAX program. Boeing assumed that despite new technologies being added to the MAX aircraft, particularly the inclusion of MCAS, pilots would not need to be specifically trained to respond to potential MCAS failures, for instance, or even to be aware MCAS existed.

**E45.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 26 ≈

> If we emphasize MCAS is a new function there may be a greater certification and training impact. Treat [MCAS] as an addition to Speed Trim . . . Externally we would communicate it as an addition to Speed Trim. Internally continue using the acronym MCAS.

**E46.** Boeing 737MAX, *Boeing_Non-Prosecution_Agreement_2025-05-29*, p. 33 ≈

> On or about January 17, 2017, Boeing Employee-1 again reminded the FAA AEG in an email to delete any reference to MCAS from the forthcoming 737 MAX FSB Report, and wrote, 'Flight Controls: Delete MCAS, recall we decided we weren't going to cover it [. . .] since it's way outside the normal operating envelope.' Again, Boeing Employee-1 deceived the FAA AEG into believing that the basis upon which the FAA AEG had initially 'decided' to remove any information about MCAS from the 737 MAX FSB Report—…

**E47.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 58

> We agreed not to reference MCAS since it's outside normal operating envelope.

**E48.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 34

> I think we also need to remember that in hindsight, there are other accidents that have happened over history where airplanes were not grounded because we didn't have data at the time. And TWA 800 is an example. We have Air France 447, where there were some similar human factors and issues involved there.

**E49.** Boeing 737MAX, *JATR_Joint_Authorities_Technical_Review_2019-10*, p. 3

> The FAA' s aircraft certification process has played a maj or role in producing airliners with an exemplary safety record consisting of a five-year worldwide average of only one fatal airliner crash for every 2 V2 to 3 million flights, and a U.S. record of only one airline passenger fatality in more than 10 years.

**E50.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 5 ≈

> Boeing took the view that pilots transitioning from the 737 NG to the 737 MAX should be required to undergo only a short computer-based training ("CBT") course, as opposed to more extensive, simulator-based training. In advocating for CBT only, Boeing employees responsible for communicating with the FAA-AEG as to differences training and manuals certification – including Boeing Employee-1 and Boeing Employee-2, senior members of the 737 MAX Flight Technical Group – presented MCAS to the FAA-AEG …

**E51.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 59

> Based on Boeing's misleading statements, half-truths, and omissions to the FAA AEG about MCAS, and in reliance on those statements and omissions, the FAA AEG agreed to delete all information about MCAS from the 737 MAX FSB Report.

**E52.** Boeing 737MAX, *Boeing_Non-Prosecution_Agreement_2025-05-29*, p. 32 ≈

> On or about November 22, 2016, the other Boeing employee emailed the draft 737 MAX FSB Report back to the FAA AEG with proposed edits. Boeing Employee-1 and Boeing Employee-2 were included on this email. Boeing Employee-1 included a proposed edit to delete a reference to MCAS, and wrote, 'We agreed not to reference MCAS since it's outside normal operating envelope.' Neither Boeing Employee-1 nor Boeing Employee-2 shared the fact of MCAS's expanded operational scope with the FAA AEG or otherwise …

**E53.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 6

> On or about November 15, 2016, during a test flight of the 737 MAX in a simulator, Boeing Employee-1 experienced what Boeing Employee-1 recognized as MCAS operating at lower speed. Later that day, Boeing Employee-1 and Boeing Employee-2 discussed MCAS in an electronic chat (the "November 15, 2016 Chat") which contained the following exchange: Boeing Employee-1: Oh shocker alerT! / MCAS is now active down to M[ach] .2 / It's running rampant in the sim[ulator] on me… / so I basically lied to the r…

**E54.** Boeing 737MAX, *Boeing_Non-Prosecution_Agreement_2025-05-29*, p. 30 ≈

> On or about November 15, 2016, during a test flight of the 737 MAX in a simulator, Boeing Employee-1 experienced what Boeing Employee-1 recognized as MCAS operating at lower speed. Boeing Employee-1 further recognized that this lower-speed operation was different from what Boeing had briefed and described to the FAA AEG. On or about that same day, Boeing Employee-1 and Boeing Employee-2 discussed MCAS in an internal Boeing electronic chat communication, writing in part: Boeing Employee-1: Oh sho…

**E55.** Boeing 737MAX, *SEC_Order_Muilenburg_33-11106_2022-09-22*, p. 11 ≈

> In or around January 2019, Boeing's in-house counsel informed Muilenburg and other senior executives about the existence of the November 15, 2016 Chat. Following that communication, Muilenburg understood the November 15, 2016 Chat to be 'concerning.' Muilenburg did not take any steps to learn additional details about the November 15, 2016 Chat.

**E56.** Boeing 737MAX, *JATR_Joint_Authorities_Technical_Review_2019-10*, p. 34

> Observation O2.8-C: Although the above guidance is aimed at test pilots conducting test flights, applicants seem to use this guidance as a design assumption that the pilot will be able to respond correctly within 4 seconds of the occurrence of a malfunction. For example, in the case of the B737 MAX, it was assumed that, since MCAS activation rate is 0.27 degrees of horizontal stabilizer movement per second, during the 4 seconds that it would take a pilot to respond to an erroneous activation, th…

**E57.** Boeing 737MAX, *FAA_737MAX_Technical_Advisory_Board_Report*, p. 23

> Issue 1: Boeing concluded during the design phase that multiple rapidly successive MCAS events, when dwelling in the high AOA region, are no more hazardous than a single MCAS event, since it was assumed the pilot would use the electric trim to completely counteract any out-of-trim forces.

**E58.** Boeing 737MAX, *JATR_Joint_Authorities_Technical_Review_2019-10*, p. 54

> Observation O6.9-H: Boeing concluded that multiple erroneous MCAS activations were not worse than a single erroneous activation, based on the assumption that the crew would return the aircraft to a trimmed state (consistent with AC 25-7C guidance) following each activation.

**E59.** Boeing 737MAX, *Senate_Commerce_Aviation_Safety_Oversight_Whistleblower_Report_2020-12*, p. 44

> On May 2, 2019, Boeing representatives provided a briefing to Committee majority staff in which they presented a clear opinion that the crashes were largely due to pilot inexperience. The representatives minimized the significance of MCAS and stated the crashes would likely never have happened with U.S. - trained pilots. Boeing representatives largely attributed the two MAX crashes to human factors.

**E60.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 149

> In a briefing to Chair DeFazio and Subcommittee on Aviation Chair Larsen in February 2019 concerning the Lion Air crash, Ali Bahrami, the FAA's Associate Administrator for Aviation Safety, described the crash as a "one off" event and attributed it to poor pilot performance.

**E61.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 197

> Both Boeing and the FAA were quick to blame the pilots of Lion Air flight 610 for the crash of that MAX aircraft and were slow to truly and fully understand and acknowledge how dangerous the design decisions and operational authority granted to the Maneuvering Characteristics Augmentation System (MCAS) was to the flight crew and safety of the airplane.

**E62.** Boeing 737MAX, *Senate_Commerce_Aviation_Safety_Oversight_Whistleblower_Report_2020-12*, p. 39 ≈

> When confronted with details of specific events, several managers revealed their lack of understanding of the policies and guidance governing their responsibilities. Some senior managers interviewed were openly dismissive when the Committee mentioned specific whistleblowers. One manager characterized a whistleblower's disclosures as 'rants,' and another dismissed a whistleblower's concern by claiming the whistleblower is difficult to work with in the FAA.

**E63.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 81

> The NTSB's reluctance to interview me, and the limited scope of the interview it conducted, raised alarms that the agency shares Boeing's aversion to exploring systemic causes for the crashes.

**E64.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 163 ≈

> In June 2017, in response to an airline that was considering simulator-based training for its pilots transitioning to the MAX, Mr. Forkner wrote in an email, "Now friggin Lion Air might need a sim to fly the MAX, and maybe because of their own stupidity."

**E65.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 12

> Five days later, on April 29, during a press conference following Boeing's annual shareholders' meeting, a reporter asked Muilenburg whether the MCAS design was deeply flawed. Muilenburg, on behalf of Boeing, responded in relevant part: "We have gone back and confirmed again … that we followed exactly the steps in our design and certification processes that consistently produce safe airplanes. It was designed per our standards. It was certified per our standards."

**E66.** Boeing 737MAX, *SEC_Order_Muilenburg_33-11106_2022-09-22*, p. 12

> We have gone back and confirmed again … that we followed exactly the steps in our design and certification processes that consistently produce safe airplanes. It was designed per our standards. It was certified per our standards.

**E67.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 243 ≈

> In the weeks after the Lion Air crash, Boeing defended its development and certification of MCAS to the FAA, writing that there was "no process violation or non-compliance" regarding the inconsistencies in the system's development and Boeing's actions, including (1) removing reference to MCAS from the FCOM, (2) determining "repeated unintended MCAS" activation to be no worse than a single unintended activation, (3) determining the loss of one AOA sensor followed by erroneous readings from the ot…

**E68.** Boeing 737MAX, *Court_Order_re_Plea_Agreement_2024-12-05*, p. 4

> Boeing does not address the objections to the selection of the monitor or the failure to make compliance with the recommendations a condition of probation. It argues instead that the Government has made significant progress to date.

**E69.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 51 ≈

> From at least in and around November 2016 through at least in and around December 2018, in the Northern District of Texas and elsewhere, Boeing, through Boeing Employee-1 and Boeing Employee-2, knowingly, and with intent to defraud, conspired to defraud the FAA AEG. At all times during the conspiracy, Boeing Employee-1 and Boeing Employee-2 were acting within the scope of their employment and with the intention, at least in part, to benefit Boeing.

**E70.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 31

> Boeing Employee-1 and Boeing Employee-2 understood that the FAA AEG relied on them, as members of Boeing's 737 MAX Flight Technical Team, to identify and provide to the FAA AEG all information that was relevant to the FAA AEG in connection with the FAA AEG's publication of the 737 MAX FSB Report, including information that could impact the FAA AEG's differences-training determination.

**E71.** Boeing 737MAX, *Court_Order_Crime_Victims_Rights_Act_2022-10-21*, p. 4

> The Government alleges that two Boeing employees hid MCAS's low-speed expansion from the AEG. Both employees held the position of chief technical pilot for the 737 MAX program at different times. Part of the chief technical pilot's duties were to work with the AEG on the differences training level determination. According to the Government, the chief technical pilots intentionally hid MCAS's low-speed expansion from the AEG so that they could secure the less rigorous—and less expensive—Level B t…

**E72.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 41 ≈

> Because of Boeing's intentional withholding of information from the FAA AEG, the final version of the 737 MAX FSB Report lacked information about MCAS, and relevant portions of this 737 MAX FSB Report were materially false, inaccurate, and incomplete. In turn, airplane manuals and pilot-training materials for U.S.-based airlines lacked information about MCAS, and relevant portions of these manuals and materials were similarly materially false, inaccurate, and incomplete as a result. After the FA…

**E73.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 125

> The unions representing pilots at American Airlines and Southwest Airlines, both of which operate the 737 MAX, allege their members were not made aware of MCAS and the system's ability to command the 737 MAX into a dive until after the Lion Air crash. Captain Dan Carey, then-President of the Allied Pilots Association, which represents American Airlines pilots, testified before the Subcommittee on Aviation in June 2019 that, "[t]he huge error of omission was the fact that Boeing failed to disclos…

**E74.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 127

> The pilots had no previous knowledge of MCAS and the aircraft provided no displays to indicate that MCAS was acting on the aircraft trim, nor any displays to help them understand that it was getting erroneous data. They were in the dark regarding the functioning of MCAS in these accidents.

**E75.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 72 ≈

> In October 2019, the Joint Authorities Technical Review (JATR) commissioned by the FAA to review the 737 MAX certification process reported that the Seattle-based Boeing Aviation Safety Oversight Office (BASOO), under the AIR Systems Oversight Division, was comprised of 45 FAA employees, including 24 total engineers, only 6 of whom were senior engineers, who overseeing the 1,500 Boeing-designated ODA unit members, or authorized representatives.

**E76.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 72 ≈

> The allocated staffing levels of 24 BASOO engineers may not be sufficient to carry out the work associated with retained items and with the conduct of oversight duties. There may be a lack of capacity and depth of experience of BASOO engineering members to approve and make findings of compliance for retained items. Depending on the number of entry-level engineers in the BASOO, there could be an imbalance of working-level engineers in relation to the number of senior engineers reasonably expected…

**E77.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 76

> Within AVS overall, 52 percent did not believe they had enough resources and manpower dedicated to safety, 49 percent believed that safety concerns/incidents will not be addressed so they don't report them, and 43 percent do not believe the FAA appropriately delegates certification activities to organizational and individual designees.

**E78.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 73

> The FAA initially delegated acceptance of approximately 40% of the B737 MAX project's certification plans to the Boeing ODA. Additional certification plans that were originally retained for acceptance by the FAA were later delegated to the Boeing ODA as the certification project progressed. While the JATR team did not conduct an exhaustive review of other ODAs, the team observed that delegating the acceptance of certification plans does not appear to be a widespread practice for the FAA.

**E79.** Boeing 737MAX, *JATR_Joint_Authorities_Technical_Review_2019-10*, p. 13

> The BASOO delegated a high percentage of approvals and findings of compliance to the Boeing ODA for the B737 MAX program. With adequate FAA engagement and oversight, the extent of delegation does not in itself compromise safety. However, in the B737 MAX program, the FAA had inadequate awareness of the MCAS function which, coupled with limited involvement, resulted in an inability of the FAA to provide an independent assessment of the adequacy of the Boeing proposed certification activities assoc…

**E80.** Boeing 737MAX, *Boeing_Non-Prosecution_Agreement_2025-05-29*, p. 29 ≈

> On or about August 16, 2016, before the FAA AEG published the 737 MAX FSB Report, the FAA AEG issued a provisional 'Level B' differences-training determination for the 737 MAX. At the time of this provisional determination, the FAA AEG was unaware that Boeing had expanded MCAS's operational scope. As Boeing Employee-1 and Boeing Employee-2 knew, the FAA AEG based its provisional 'Level B' differences training for the 737 MAX in part on its understanding that MCAS could only activate during the l…

**E81.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 58 ≈

> On or about November 17, 2016, the FAA AEG emailed three Boeing employees, including Boeing Employee-1, Boeing Employee-2, and another Boeing employee, a draft of the forthcoming 737 MAX FSB Report. That same day, Boeing Employee-1 asked Boeing Employee-2 and the other Boeing employee to review the draft 737 MAX FSB Report "for any glaring issues." On or about November 22, 2016, the other Boeing employee emailed the draft 737 MAX FSB Report back to the FAA AEG with proposed edits. Boeing Employe…

**E82.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 6

> And in a January 17, 2017 email to the FAA-AEG, Boeing Employee-1 reminded the FAA-AEG to delete any references to MCAS from the FSB Report, saying "Flight Controls: Delete MCAS, recall we decided we weren't going to cover it in the [manuals] or the CBT … since it's way outside the normal operating envelope."

**E83.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 79

> To address the worsening factory conditions, I recommended that Boeing ''[s]hut down the production line to allow our team time to regroup so we can safely finish the planes.'' In response, Mr. Campbell assured me that ''safety and quality is number one and schedule come [sic] after that,'' but he did not acknowledge, let alone act on, my recommendation that Boeing shut down the line to allow workers time to safely address the production backlog. Over the following weeks, factory conditions wors…

**E84.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 25 ≈

> In June 2018, Ed Pierson, a senior Boeing plant supervisor at the company's Renton, Washington 737 MAX production factory, emailed Scott Campbell, the 737 General Manager, requesting a meeting about 'safety concerns.' Mr. Pierson described multiple concerns about production and schedule pressures that were impacting quality control and safety issues. 'As a retired Naval Officer and former Squadron Commanding Officer,' wrote Pierson, 'I know how dangerous even the smallest of defects can be to th…

**E85.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 25 ≈

> In July 2018, five weeks after Mr. Pierson's email, he finally met with Mr. Campbell in Mr. Campbell's office. According to Mr. Pierson's testimony to the Committee, he told Mr. Campbell that in the military they would temporarily halt production if they had the kinds of safety problems that Mr. Pierson was seeing on the MAX factory floor. Mr. Campbell allegedly responded: 'The military is not a profit-making organization.' Rather than heeding Mr. Pierson's dire warnings and thoroughly evaluatin…

**E86.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 5 ≈

> Boeing employees responsible for communicating with the FAA-AEG as to differences training and manuals certification – including Boeing Employee-1 and Boeing Employee-2, senior members of the 737 MAX Flight Technical Group – presented MCAS to the FAA-AEG as a feature that could only activate in a very specific, high-speed scenario that was outside the normal flight envelope and therefore unlikely to ever be encountered by a commercial pilot. They made these representations to FAA-AEG personnel b…

**E87.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 51 ≈

> Boeing Employee-1 and Boeing Employee-2 understood that the FAA AEG relied on them, as members of Boeing's 737 MAX Flight Technical Team, to identify and provide to the FAA AEG all information that was relevant to the FAA AEG in connection with the FAA AEG's publication of the 737 MAX FSB Report, including information that could impact the FAA AEG's differences-training determination. Boeing Employee-1 and Boeing Employee-2 also understood that, because flight controls were vital to flying moder…

**E88.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 59

> From in or around January 2017 through in or around July 2017 (when the 737 MAX FSB Report was published), Boeing Employee-1 and Boeing Employee-2 sent and caused to be sent emails to representatives of various Boeing airline customers that had agreed to purchase the 737 MAX, including major U.S.-based airlines. In these emails, Boeing Employee-1 and Boeing Employee-2 or members of their 737 MAX Flight Technical Team referenced and included drafts of the forthcoming 737 MAX FSB Report and airpla…

**E89.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 6

> In fact, during the certification of the 737 MAX, Boeing actively pushed the FAA to remove references to MCAS from the flight crew operating manual, as revealed in the emails and instant messages from Boeing executive Mark Forkner, which Boeing initially failed to provide to the committee. The FAA accepted Boeing's push, and Forkner went on to boast that he was ''Jedi mind-tricking'' other civil aviation regulators around the world to adopt the FAA's faulty decision.

**E90.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 6

> Following this exchange, Boeing employees responsible for communicating with the FAA-AEG did not inform the FAA-AEG about the MCAS Expansion. And in a January 17, 2017 email to the FAA-AEG, Boeing Employee-1 reminded the FAA-AEG to delete any references to MCAS from the FSB Report, saying "Flight Controls: Delete MCAS, recall we decided we weren't going to cover it in the [manuals] or the CBT … since it's way outside the normal operating envelope."

**E91.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 57

> For example, shortly after the simulated test flight described in paragraph 30, Boeing Employee-1 talked with FAA AEG Employee-1, who asked Boeing Employee-1 about the simulated test flight. Boeing Employee-1 intentionally withheld and concealed from FAA AEG Employee-1 the fact that MCAS's operational scope had been expanded beyond what the FAA AEG relied upon when it issued its provisional "Level B" differences-training determination for the 737 MAX.

**E92.** Boeing 737MAX, *FAA_737MAX_Technical_Advisory_Board_Report*, p. 2

> On October 29, 2018, Lion Air flight 610 (JT610), a Boeing Model 737-8 airplane, crashed approximately twelve minutes after takeoff in Jakarta, Indonesia. On March 10, 2019, Ethiopian Airlines flight 302 (ET302), also a Boeing Model 737-8 airplane, crashed approximately six minutes after takeoff in Addis Ababa, Ethiopia. The B737 MAX automated flight control system is an area of interest in both accidents. The FAA determined that the implementation of a Technical Advisory Board (TAB), consisting…

**E93.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 2

> On March 13, 2019, three days after the Ethiopian Airlines Crash, the U.S. Federal Aviation Administration ("FAA") issued an order grounding the entire 737 MAX fleet due to ongoing safety concerns; similar grounding orders were issued by regulators around the world. Ultimately, more than 20 months would pass before a 737 MAX was once again permitted to fly.

**E94.** Boeing 737MAX, *JATR_Joint_Authorities_Technical_Review_2019-10*, p. 7

> On October 29, 2018, Lion AIR Flight JT610 (JT610), a B737-8 MAX, crashed shortly after takeoff in Jakarta, Indonesia. On November 7, 2018, the FAA issued Emergency Airworthiness Directive (AD) 2018-23-51 to require revising certificate limitations and operating procedures of the Airplane Flight Manual (AFM) for the B737 MAX to provide the flight crew with runaway horizontal stabilizer trim procedures to follow under certain conditions. On March 10, 2019, Ethiopian Airlines Flight 302 (ET302), a…

**E95.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 197

> In June 2016, more than two years prior to the October 2018 crash of the Lion Air flight, Boeing engineers had predicted some of the key issues that led to the Lion Air crash, including the potential adverse consequences of erroneous AOA sensor data on MCAS, and they questioned whether or not pilots would have trouble combatting repetitive MCAS activation. These concerns, however, were either not adequately addressed or largely dismissed by their Boeing colleagues.

**E96.** Boeing 737MAX, *SEC_Order_Muilenburg_33-11106_2022-09-22*, p. 6

> On or about November 15, 2016, during a test flight of the 737 MAX in a simulator, Boeing Employee-1 experienced what Boeing Employee-1 recognized as MCAS operating at lower speed. Later that day, Boeing Employee-1 and Boeing Employee-2 discussed MCAS in an electronic chat (the "November 15, 2016 Chat") which contained the following exchange: Boeing Employee-1: Oh shocker alerT! / MCAS is now active down to M[ach] .2 / It's running rampant in the sim[ulator] on me… / so I basically lied to the r…

**E97.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 7

> On November 7, 2018, the FAA issued a public emergency airworthiness directive to airlines operating the 737 MAX, informing them of the potential for repeated nose-down movements of the aircraft which, "if not addressed, could cause the flight crew to have difficulty controlling the airplane … and [could result in] possible impact with terrain." The airworthiness directive identified the issue as an "unsafe condition" on the 737 MAX, and, as an "interim action" pending further analysis, referred…

**E98.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 100

> The FAA was not completely unaware of MCAS; however, because the information and discussions about MCAS were so fragmented and were delivered to disconnected groups within the process, it was difficult to recognize the impacts and implications of this system. If the FAA technical staff had been fully aware of the details of MCAS function, the JATR team believes the agency likely would have required an issue paper for using the stabilizer in a way that it had not previously been used.

**E99.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 35

> Boeing disclosed this expansion to FAA personnel, but only to those personnel who were responsible for determining whether the 737 MAX met U.S. federal airworthiness standards. Boeing did not disclose the expansion to the FAA AEG personnel responsible for publishing the 737 MAX FSB Report and making the training-related determination.

**E100.** Boeing 737MAX, *JATR_Joint_Authorities_Technical_Review_2019-10*, p. 44

> Although MCAS may have been briefed to some FAA personnel, key aspects of the MCAS function such as intended function description, its interfaces, and architecture, were not directly visible to the FAA in a straightforward manner through the certification deliverable documents.

**E101.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 51

> Boeing Employee-1 and Boeing Employee-2 understood that the FAA AEG relied on them, as members of Boeing's 737 MAX Flight Technical Team, to identify and provide to the FAA AEG all information that was relevant to the FAA AEG in connection with the FAA AEG's publication of the 737 MAX FSB Report, including information that could impact the FAA AEG's differences-training determination.

**E102.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 27

> In March 2016, the General Manager of Boeing's 737 MAX program, Keith Leverkuhn, and Michael Teal, the former Chief Project Engineer on the 737 MAX program, both approved a redesign of MCAS to increase its authority to move the aircraft's stabilizer at low speed, in order to address "stall characteristics" requirements necessary for FAA certification.

**E103.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 24

> In 2012, in order to lower costs of the 737 MAX program, Boeing reduced the work hours involved in avionics regression testing on the 737 MAX by 2,000 hours. It also examined other reductions to save costs, including a reduction to flight test support by 3,000 hours and a reduction to the engineering flight deck simulator (E-CAB) by 8,000 hours.

**E104.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 133

> For example, it was reported in the media that a survey found that one in three Boeing employees reported they felt undue pressure from managers regarding safety-related approvals due to time and schedule concerns, and some 15% reported encountering such problems several times or frequently.

**E105.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 24 ≈

> To emphasize the significance of the 737 MAX program's schedule to Boeing employees, the Committee learned that senior program officials kept a "countdown clock" in their conference room. Keith Leverkuhn, the former Vice President and General Manager of the MAX program, described the clock as an "excitement generator" for Boeing's staff. But he also acknowledged it was to remind staff about the MAX's schedule. "One of the mantras that we had was the value of a day," he said, "and making sure tha…

**E106.** Boeing 737MAX, *Boeing_Non-Prosecution_Agreement_2025-05-29*, p. 18

> Boeing senior executives prioritized the movement of aircraft through Boeing's factories over reducing out-of-sequence work to ensure production quality.

**E107.** Boeing 737MAX, *SEC_Order_Muilenburg_33-11106_2022-09-22*, p. 8

> On November 20, 2018, Muilenburg expressed disappointment in Boeing's response to the negative post-crash media coverage, stating in an email that "[w]e are spending too much time playing defense… [we] need to start playing some offense."

**E108.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 261

> FAA management has changed their focus from one that prioritized compliance to regulations and policy thirty years ago to a management culture that gives priority to applicants' positions, their costs and schedules over compliance to FAA regulations and policy.

**E109.** Boeing 737MAX, *Boeing_DPA_incl_Statement_of_Facts_2021-01-07*, p. 38

> Despite knowing that the FAA AEG had issued its provisional "Level B" determination without any awareness that MCAS's operational scope had been expanded to include high angle of attack conditions in nearly the entire speed range of ordinary commercial flight, Boeing Employee-1 and Boeing Employee-2 did not correct the FAA AEG's understanding of MCAS's operational scope or otherwise ensure that the FAA AEG's "Level B" determination was based on an accurate understanding of MCAS's operation. Inst…

**E110.** Boeing 737MAX, *Boeing_Criminal_Information_2021-01-07*, p. 2

> On or about January 17, 2017, an employee of THE BOEING COMPANY emailed an employee of the FAA AEG about the 737 MAX FSB Report, stating in part, "Flight Controls: Delete MCAS, recall we decided we weren't going to cover it [. . .] since it's way outside the normal operating envelope."

**E111.** Boeing 737MAX, *Boeing_Proposed_Plea_Agreement_2024-07-29*, p. 56 ≈

> At this point, Boeing Employee-1 and Boeing Employee-2 recognized that the FAA AEG was under the misimpression that MCAS operated only during a high-speed, wind up turn and could not operate at lower Mach speeds, such as at Mach 0.2. Boeing Employee-1 and Boeing Employee-2 therefore knew, at least as of the time of this chat communication, that the FAA AEG's provisional 'Level B' differences-training determination had been based in part on outdated and inaccurate information about MCAS. . . . De…

**E112.** Boeing 737MAX, *House_TI_Hearing_FAA_Oversight_Pierson_testimony_2019-12-11*, p. 6

> In November 2018, a few days after a powerful system running in the background of the 737 MAX called MCAS pushed Lion Air flight 610 into an unrecoverable dive, the FAA issued an emergency airworthiness directive that purported to inform pilots on how to respond to an erroneous activation of MCAS, while it actually never mentioned that system by name. In fact, during the certification of the 737 MAX, Boeing actively pushed the FAA to remove references to MCAS from the flight crew operating manua…

**E113.** Boeing 737MAX, *SEC_Order_Muilenburg_33-11106_2022-09-22*, p. 7

> On or about November 15, 2018, Boeing safety engineers concluded that, in light of the SRB's findings, the MCAS software should be redesigned and re-installed on the 737 MAX fleet to remediate the high crew workload "airplane safety issue." They determined that the software redesign had to be completed within approximately 27 months, but that the 737 MAX fleet could continue to operate in the interim in light of Boeing's bulletin and the FAA emergency airworthiness directive.

**E114.** Boeing 737MAX, *Boeing_Non-Prosecution_Agreement_2025-05-29*, p. 31

> Despite knowing that the FAA AEG had issued its provisional "Level B" determination without any awareness that MCAS's operational scope had been expanded to include high angle of attack conditions in nearly the entire speed range of ordinary commercial flight, Boeing Employee-1 and Boeing Employee-2 did not correct the FAA AEG's understanding of MCAS's operational scope or otherwise ensure that the FAA AEG's "Level B" determination was based on an accurate understanding of MCAS's operation. Inst…

**E115.** Boeing 737MAX, *House_TI_Final_Committee_Report_737MAX_2020-09*, p. 107

> Lion Air flight 610 crashes 13 minutes after takeoff killing 189 people. MCAS is quickly determined to be a major factor in the crash. Faulty AOA data erroneously caused MCAS to repetitively activate more than 20 times as the pilots battled MCAS for control of the aircraft.

**E116.** Boeing 737MAX, *FAA_737MAX_Return_to_Service_Summary_2020-11*, p. 19 ≈

> On March 10, 2019, ET302 crashed shortly after takeoff in Addis Ababa, Ethiopia. Partial data (e.g., altitude, airspeed and vertical speed) was available from a land-based Automatic Dependent Surveillance—Broadcast (ADS-B) system. On March 11, 2019, the FAA issued another CANIC (see Appendix D) indicating the FAA was actively involved in supporting the investigations. On March 11, the FAA received additional ADS-B data. The data was analyzed and reviewed on March 12 and through the early hours o…

**E117.** Boeing 737MAX, *SEC_Order_Boeing_33-11105_2022-09-22*, p. 7 ≈

> The Lion Air Crash occurred on October 29, 2018. Soon after the crash, investigators identified repeated unintended activations of MCAS triggered by erroneous AoA data as a cause of the accident. In the weeks following the Lion Air Crash, Boeing convened a series of meetings of its Safety Review Board ("SRB") – an internal body comprised of Boeing personnel that evaluate in-service aircraft safety issues – on November 4, 2018, November 6, 2018, and November 15, 2018, to assess the ongoing safety…
